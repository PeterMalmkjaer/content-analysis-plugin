#!/usr/bin/env python3
"""Merge batch CSVs of one (set, arm, run, split) into the skill's long-format coded_data.csv,
report coverage gaps / invalid codes, write manifest, frequencies, sources dir, and run the
arm's validator. Usage: assemble.py SET ARM RUN [--split test]  [--gaps-only]"""
import csv, json, os, sys, glob, re, subprocess, collections
SET, ARM, RUN = sys.argv[1], sys.argv[2], int(sys.argv[3])
SPLIT = sys.argv[sys.argv.index("--split")+1] if "--split" in sys.argv else "test"
BENCH = "/home/claude/bench"
SKILL = {"A": f"{BENCH}/skill-beta3", "B": f"{BENCH}/skill-beta4", "C": f"{BENCH}/skill-beta4", "E": f"{BENCH}/skill-beta5", "F": f"{BENCH}/skill-beta5"}[ARM]
d = f"{BENCH}/runs/{SET}/{ARM}/run{RUN}/{SPLIT}"
index = json.load(open(f"{d}/index.json"))
expected = [u for b in index for u in b["units"]]
sq = lambda s: re.sub(r"\s+", " ", s.replace(" ", " ")).strip()

rows = []; repaired = 0; normalized_ids = 0
for f in sorted(glob.glob(f"{d}/batch*.csv")) + sorted(glob.glob(f"{d}/gap*.csv")):
    rd = csv.reader(open(f, encoding="utf-8-sig"))
    header = [h.strip() for h in next(rd)]
    for vals in rd:
        if not any(v.strip() for v in vals): continue
        if len(vals) > len(header):
            # unquoted comma in a free-text field. Anchor on the enumerated fields:
            # Prompting (set1) / Review (B,C) must hold known values; free-text fields are Text excerpt and Coder notes.
            PROMPT = {"prompted", "volunteered", "mixed", "unclear", "n/a"}
            REV = {"", "context_missing", "possible_irony", "competing_codes", "insufficient_basis", "other"}
            fixed_front = [h for h in header if h in ("Document ID", "Unit ID", "Code ID")]
            nf = len(fixed_front); rest = header[nf:]  # e.g. [Text excerpt, Prompting, (Review), Coder notes] or [Text excerpt, Coder notes] or [Coder notes,(Review)]
            tail = vals[nf:]
            if "Prompting" in rest:
                pi = rest.index("Prompting")
                # candidate positions for Prompting in tail: value in PROMPT
                cands = [i for i, v in enumerate(tail) if v.strip().lower() in PROMPT]
                if cands:
                    j = cands[0] if rest.index("Text excerpt") < pi else cands[-1]
                    excerpt = ",".join(tail[:j]); after = tail[j+1:]
                    if "Review" in rest:
                        rev = after[0] if after and after[0].strip() in REV else ""
                        notes = ",".join(after[1:] if rev != "" or (after and after[0].strip() == "") else after)
                        vals = vals[:nf] + [excerpt, tail[j], rev, notes]
                    else:
                        vals = vals[:nf] + [excerpt, tail[j], ",".join(after)]
                    repaired += 1
                else:
                    problems_fmt = True
            elif "Text excerpt" in rest:
                # set2: [Text excerpt, (Review), Coder notes]; assume the surplus commas belong to the excerpt
                extra = len(vals) - len(header); i = header.index("Text excerpt")
                vals = vals[:i] + [",".join(vals[i:i+extra+1])] + vals[i+extra+1:]; repaired += 1
            else:
                # set3: [Coder notes, (Review)]: surplus commas belong to the notes
                extra = len(vals) - len(header); i = header.index("Coder notes")
                vals = vals[:i] + [",".join(vals[i:i+extra+1])] + vals[i+extra+1:]; repaired += 1
        r = {k: (v or "").strip() for k, v in zip(header, vals)}
        if "Unit ID" in r and "|" in r["Unit ID"]:   # coder copied the "DOC|n" label into Unit ID
            r["Unit ID"] = r["Unit ID"].split("|")[-1].strip(); normalized_ids += 1
        r["_src"] = os.path.basename(f)
        rows.append(r)
if repaired: print(f"  repaired {repaired} row(s) with an unquoted comma in the excerpt")
if normalized_ids: print(f"  normalized {normalized_ids} Unit ID value(s) written as DOC|n")

# ---- unit key per set
def ukey(r):
    if SET == "set3":
        return f"{r['Document ID']}|1"
    return f"{r['Document ID']}|{r['Unit ID']}"

# ---- validity
if SET == "set3":
    valid = set(open(f"{BENCH}/codex_beta3/03_goemotions/emotions.txt").read().split())
elif SET == "set2":
    valid = set(x["Code ID"] for x in csv.DictReader(open(f"{BENCH}/materials/set2_codebook_codes.csv")))
else:
    valid = set(x["Code ID"] for x in csv.DictReader(open(f"{BENCH}/materials/set1_codebook_A.csv", encoding="utf-8-sig"))) | {"UNCODED"}
REVIEW = {"", "context_missing", "possible_irony", "competing_codes", "insufficient_basis", "other"}

coded_units = collections.defaultdict(list)
problems = []
for r in rows:
    k = ukey(r)
    if k not in expected:
        problems.append(f"unexpected unit {k} in {r['_src']}"); continue
    if r["Code ID"] not in valid:
        problems.append(f"invalid code {r['Code ID']!r} on {k} ({r['_src']})"); continue
    if ARM != "A" and r.get("Review", "") not in REVIEW:
        problems.append(f"invalid Review {r.get('Review')!r} on {k}")
    coded_units[k].append(r)

missing = [u for u in expected if u not in coded_units]
# de-duplicate identical (unit, code)
seen = set(); dedup = []; dups = 0
for k in expected:
    for r in coded_units.get(k, []):
        key = (k, r["Code ID"])
        if key in seen: dups += 1; continue
        seen.add(key); dedup.append((k, r))
# set3: neutral + emotion -> keep as coded but flag
neut = 0
if SET == "set3":
    byu = collections.defaultdict(set)
    for k, r in dedup: byu[k].add(r["Code ID"])
    neut = sum(1 for k, s in byu.items() if "neutral" in s and len(s) > 1)

print(f"{SET} {ARM} run{RUN} {SPLIT}: expected {len(expected)} units, coded {len(coded_units)}, missing {len(missing)}, rows {len(dedup)} (dropped {dups} duplicate rows), problems {len(problems)}, neutral+emotion units {neut}")
for p in problems[:20]: print("  !", p)
if missing:
    print("  missing units:", missing[:30], "..." if len(missing) > 30 else "")
    # write a gap batch file for a fresh subagent
    src_batches = {u: b["file"] for b in index for u in b["units"]}
    gapfile = f"{d}/gap01.md"
    n_existing = len(glob.glob(f"{d}/gap*.md"))
    gapfile = f"{d}/gap{n_existing+1:02d}.md"
    with open(gapfile, "w", encoding="utf-8") as g:
        g.write(f"# Gap batch — {SET} / arm {ARM} / run {RUN} / {SPLIT}\n\nUnits omitted by earlier batches; same instructions.\n\n")
        for u in missing:
            txt = open(src_batches[u], encoding="utf-8").read()
            hdr = f"## Unit {u.split('|')[0]}" if SET == "set3" else f"## Unit {u}"
            m = re.search(re.escape(hdr) + r"\n\n(.*?)(?=\n## Unit |\Z)", txt, re.S)
            g.write(f"{hdr}\n\n{m.group(1).strip()}\n\n")
    print("  gap batch written:", gapfile, "-> code it with the same prompt, output", gapfile.replace('.md', '.csv'))
if "--gaps-only" in sys.argv: sys.exit(0)

# ---- write skill-format outputs
os.makedirs(f"{d}/out/sources", exist_ok=True)
cols = ["Document ID", "Unit ID", "Assignment ID", "Source type", "Producer", "Elicitation", "Date", "Parent / section", "Language",
        "Text excerpt", "Code ID", "Code name", "Prompting", "Codebook version", "Pass", "Review", "Coder notes"]
if ARM == "A": cols.remove("Review")
srcinfo = {"set1": ("interview", "interviewee", "elicited", "en"), "set2": ("institutional document", "AC-ICT", "naturally occurring", "nl"),
           "set3": ("user comment", "Reddit user", "naturally occurring", "en")}[SET]
# unit texts for sources / excerpts
if SET == "set1":
    U = json.load(open(f"{BENCH}/set1_units_reference.json"))["units"]
    utext = {f"{doc}|{i+1}": b for doc, bl in U.items() for i, b in enumerate(bl)}
    docs = sorted(set(k.split("|")[0] for k in expected))
    for doc in docs:
        open(f"{d}/out/sources/{doc}.txt", "w", encoding="utf-8").write("\n\n".join(U[doc]))
elif SET == "set2":
    U = json.load(open(f"{BENCH}/set2_units_reference.json"))["units"]
    utext = {f"{doc}|{i+2}": p for doc, pl in U.items() for i, p in enumerate(pl)}
    docs = sorted(set(k.split("|")[0] for k in expected))
    for doc in docs:
        open(f"{d}/out/sources/{doc}.txt", "w", encoding="utf-8").write("\n\n".join(U[doc]))
else:
    U = {u["id"]: u["text"] for u in json.load(open(f"{BENCH}/set3_units_reference.json"))}
    utext = {f"{k}|1": v for k, v in U.items()}
    docs = sorted(set(k.split("|")[0] for k in expected))
    for doc in docs:
        open(f"{d}/out/sources/{doc}.txt", "w", encoding="utf-8").write(U[doc])

names = {}
if SET == "set1":
    names = {x["Code ID"]: x["Code name"] for x in csv.DictReader(open(f"{BENCH}/materials/set1_codebook_A.csv", encoding="utf-8-sig"))}
out_rows = []; aid = 0; excerpt_fail = 0
for k, r in dedup:
    doc, unit = k.split("|")
    aid += 1
    ex = r.get("Text excerpt", "") if SET != "set3" else utext[k]
    if SET != "set3" and sq(ex) not in sq(utext[k]):
        excerpt_fail += 1
    if r["Code ID"] == "UNCODED" and not ex:
        ex = utext[k][:60]
    out_rows.append({"Document ID": doc, "Unit ID": unit, "Assignment ID": f"A-{aid:05d}", "Source type": srcinfo[0], "Producer": srcinfo[1],
                     "Elicitation": srcinfo[2], "Date": "", "Parent / section": (utext[k].split("\n")[0][:120] if SET == "set1" else ""),
                     "Language": srcinfo[3], "Text excerpt": ex, "Code ID": r["Code ID"], "Code name": names.get(r["Code ID"], r["Code ID"]),
                     "Prompting": (r.get("Prompting", "") or "n/a") if SET == "set1" else "n/a", "Codebook version": "v1", "Pass": "1",
                     "Review": r.get("Review", ""), "Coder notes": r.get("Coder notes", "")})
with open(f"{d}/out/coded_data.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(out_rows)
# manifest + frequencies + codebook csv
with open(f"{d}/out/manifest.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["Document ID", "Parent document", "Source file", "Source type", "Units", "Status", "Coded under"])
    for doc in docs:
        n_units = len([u for u in expected if u.split("|")[0] == doc])
        w.writerow([doc, "", f"{doc}.txt", srcinfo[0], n_units, "coded", "v1"])
per = collections.defaultdict(lambda: [0, set(), set()])
for r in out_rows:
    if r["Code ID"] == "UNCODED": continue
    p = per[r["Code ID"]]; p[0] += 1; p[1].add((r["Document ID"], r["Unit ID"])); p[2].add(r["Document ID"])
with open(f"{d}/out/frequencies.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["Code ID", "Assignments", "Units", "Documents"])
    for c in sorted(per): w.writerow([c, per[c][0], len(per[c][1]), len(per[c][2])])
with open(f"{d}/out/codebook.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["Code ID", "Status"])
    for c in sorted(valid - {"UNCODED"}): w.writerow([c, "active"])
print(f"  wrote out/coded_data.csv ({len(out_rows)} rows); excerpts not found in unit: {excerpt_fail}")
v = subprocess.run(["python3", f"{SKILL}/scripts/validate_coding.py", "--coded", f"{d}/out/coded_data.csv", "--codebook", f"{d}/out/codebook.csv",
                    "--manifest", f"{d}/out/manifest.csv", "--sources", f"{d}/out/sources", "--summary", f"{d}/out/frequencies.csv", "--codebook-version", "v1"],
                   capture_output=True, text=True)
open(f"{d}/out/validation.txt", "w").write(v.stdout)
print("  validator:", [l for l in v.stdout.splitlines() if l.startswith(("RESULT", "FAIL", "WARN", "SKIP"))][:12])
