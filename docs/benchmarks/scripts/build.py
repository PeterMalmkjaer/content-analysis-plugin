#!/usr/bin/env python3
"""Build batch files and subagent prompts for one (set, arm, run).
Usage: build.py SET ARM RUN [--split test|calibration|retest]
Writes runs/<set>/<arm>/run<RUN>/<split>/batchNN.md + promptNN.md and an index."""
import json, random, sys, os, csv, re
SET, ARM, RUN = sys.argv[1], sys.argv[2], int(sys.argv[3])
SPLIT = sys.argv[sys.argv.index("--split")+1] if "--split" in sys.argv else "test"
SEED = 20260910 + RUN
BENCH = "/home/claude/bench"
SKILL = {"A": f"{BENCH}/skill-beta3", "B": f"{BENCH}/skill-beta4", "C": f"{BENCH}/skill-beta4", "E": f"{BENCH}/skill-beta5", "F": f"{BENCH}/skill-beta5", "H": f"{BENCH}/skill-beta6", "J": f"{BENCH}/skill-beta6", "G": f"{BENCH}/skill-beta6g"}[ARM]
VER = {"A": "5.0.0-beta.3", "B": "5.0.0-beta.4", "C": "5.0.0-beta.4", "E": "5.0.0-beta.5 candidate", "F": "5.0.0-beta.5 candidate", "H": "5.0.0-beta.6 candidate", "J": "5.0.0-beta.6 candidate", "G": "5.0.0-beta.6 candidate"}[ARM]
_UNC = "**uncalibrated** — no Step 5b calibration against human coding has been carried out for this codebook"
_CAL = "**calibrated** — one Step 5b round against human coding has been carried out; the decision rules in the codebook are the calibrated ones"
STATUS = {"E": _UNC, "F": _CAL, "H": _UNC, "J": _CAL, "G": _CAL}.get(ARM)
NEW = ("E", "F", "H", "J", "G")
out = f"{BENCH}/runs/{SET}/{ARM}/run{RUN}/{SPLIT}"
os.makedirs(out, exist_ok=True)
splits = json.load(open(f"{BENCH}/splits.json"))
rng = random.Random(SEED)

def codebook_path():
    if SET == "set1":
        return f"{BENCH}/materials/set1_codebook_A.csv" if ARM == "A" else f"{BENCH}/materials/set1_codebook_{ARM}.csv"
    if SET == "set2":
        return None  # two files, handled in prompt
    if SET == "set3":
        return f"{BENCH}/materials/set3_codebook_A.md" if ARM == "A" else f"{BENCH}/materials/set3_codebook_{ARM}.md"

def units():
    if SET == "set1":
        d = json.load(open(f"{BENCH}/set1_units_reference.json"))
        us = []
        for doc, blocks in d["units"].items():
            for i, b in enumerate(blocks, 1):
                if splits["set1"][f"{doc}|{i}"] == SPLIT:
                    us.append({"doc": doc, "unit": i, "text": b})
        # batches of ~10, grouped by document (document context stays together)
        us.sort(key=lambda u: (u["doc"], u["unit"]))
        batches = []
        for doc in sorted(set(u["doc"] for u in us)):
            du = [u for u in us if u["doc"] == doc]
            for k in range(0, len(du), 10):
                batches.append(du[k:k+10])
        # merge tiny tail batches (<5) into previous of same doc
        merged = []
        for b in batches:
            if merged and len(b) < 5 and merged[-1][0]["doc"] == b[0]["doc"]:
                merged[-1].extend(b)
            else:
                merged.append(b)
        return merged
    if SET == "set2":
        d = json.load(open(f"{BENCH}/set2_units_reference.json"))
        us = []
        for doc, paras in d["units"].items():
            for i, p in enumerate(paras):
                us.append({"doc": doc, "unit": i+2, "text": p})
        batches = []
        for doc in sorted(set(u["doc"] for u in us)):
            du = [u for u in us if u["doc"] == doc]
            for k in range(0, len(du), 25):
                batches.append(du[k:k+25])
        return batches
    if SET == "set3":
        d = json.load(open(f"{BENCH}/set3_units_reference.json"))
        if SPLIT in ("fresh", "fresh2"):   # protocol addenda: 500 comments outside all earlier samples
            fresh = set(json.load(open(f"{BENCH}/splits_addendum.json"))["set3_fresh"]) if SPLIT == "fresh" else set(json.load(open(f"{BENCH}/splits_addendum2.json"))["set3_fresh2"])
            us = [{"doc": u["id"], "unit": 1, "text": u["text"]} for u in d if u["id"] in fresh]
            us.sort(key=lambda u: u["doc"])
            if RUN == 2: rng.shuffle(us)   # addendum: different batch composition in run 2
            return [us[k:k+50] for k in range(0, len(us), 50)]
        us = [{"doc": u["id"], "unit": 1, "text": u["text"]} for u in d if splits["set3"].get(u["id"]) == SPLIT]
        us.sort(key=lambda u: u["doc"])
        return [us[k:k+50] for k in range(0, len(us), 50)]

batches = units()
if RUN == 2 and SPLIT not in ("fresh", "fresh2"):
    rng.shuffle(batches)
index = []
for n, b in enumerate(batches, 1):
    bf = f"{out}/batch{n:02d}.md"
    with open(bf, "w", encoding="utf-8") as f:
        f.write(f"# Batch {n:02d} — {SET} / arm {ARM} / run {RUN} / {SPLIT}\n\n")
        if SET == "set1":
            f.write(f"Interview {b[0]['doc']} ({'policy maker / support staff' if b[0]['doc'] in ('I1','I2','I3','I4') else 'researcher'}). Each unit below is one numbered question/answer block; the first line is the interviewer's question (context), the rest is the respondent's answer (coded text).\n\n")
            for u in b:
                f.write(f"## Unit {u['doc']}|{u['unit']}\n\n{u['text']}\n\n")
        elif SET == "set2":
            f.write(f"Report {b[0]['doc']}. Each unit is one recommendation excerpt, in report order (Dutch).\n\n")
            for u in b:
                f.write(f"## Unit {u['doc']}|{u['unit']}\n\n{u['text']}\n\n")
        else:
            f.write("One comment per unit. The unit ID is the Document ID; Unit ID is always 1.\n\n")
            for u in b:
                f.write(f"## Unit {u['doc']}\n\n{u['text']}\n\n")
    index.append({"batch": n, "file": bf, "units": [f"{u['doc']}|{u['unit']}" for u in b]})

    # ---- prompt
    outcsv = f"{out}/batch{n:02d}.csv"
    review_col = "" if ARM == "A" else ",Review"
    if SET == "set3":
        cols = "Document ID,Code ID,Coder notes" + review_col
        outrule = ("one row per (comment, label); `Code ID` is the label name exactly as in the codebook (e.g. `admiration`, `neutral`); "
                   "`Coder notes` = a 3–8-word reason. Every comment in the batch must appear (with `neutral` alone if no emotion is expressed).")
    elif SET == "set2":
        cols = "Document ID,Unit ID,Code ID,Text excerpt,Coder notes" + review_col
        outrule = ("one row per (unit, field assignment); `Code ID` is written `FIELD=VALUE` exactly as listed in codebook_codes.csv; "
                   "`Text excerpt` = a verbatim Dutch passage from that unit justifying the assignment; every unit gets exactly one `GOV_RELEVANT=` row, "
                   "and — only if it is MECH or RESP — exactly one row for each of PHASE, AUTH_REQ, GC_PRIMARY, INTEREST_ORIENTATION.")
    else:
        cols = "Document ID,Unit ID,Code ID,Text excerpt,Prompting,Coder notes" + review_col
        outrule = ("one row per (unit, code); `Code ID` is C01–C54 from the codebook, or `UNCODED` (one row, excerpt = the answer's opening words) when nothing in the unit fits any code; "
                   "`Text excerpt` = a verbatim passage from the respondent's answer in that unit (not the question); `Prompting` = prompted / volunteered / mixed / unclear.")
    review_rule = "" if ARM == "A" else ("\n- `Review` is blank when the decision was clear; otherwise exactly one of context_missing / possible_irony / competing_codes / insufficient_basis / other, "
                                         "as defined in SKILL.md (Step 7, step 8, and the coded-data table). `other` requires the reason in Coder notes. Uncertainty is recorded in Review, never by choosing neutral/UNCODED/the broadest code.")
    if ARM in NEW:
        review_rule = ("\n- `Review` is blank when the decision was clear; otherwise exactly one of context_missing / possible_irony / competing_codes / insufficient_basis / other, "
                       "as defined in SKILL.md (Step 7 and the coded-data table). `other` requires the reason in Coder notes." + ("" if SPLIT == "fresh2" else " Uncertainty is recorded in Review, never by choosing neutral/UNCODED/the broadest code."))
    cb = codebook_path()
    cb_lines = (f"3. The codebook: `{cb}`" if cb else
                f"3. The codebook: `{BENCH}/materials/set2_codebook_v21.md`, the governance-relevance rules `{BENCH}/materials/set2_governance_rules.md`, and the exact code list `{BENCH}/materials/set2_codebook_codes.csv`")
    if ARM != "A" and SET == "set2":
        cb_lines += f", plus the decision-rule columns `{BENCH}/materials/set2_decision_rules_{ARM}.md`"
    step7 = ("Step 7 (for each unit: identify boundary, read in context, assign codes, record verbatim excerpt, UNCODED when nothing fits) and the Output: Coded Data Table conventions"
             if ARM == "A" else
             "Step 7's eight-step decision procedure (locate the passage → check criteria and required textual basis → compare with nearest alternatives → assign and record → sweep the remaining codes one by one → mark what remains with UNCODED or Review), the Gated codes rule, and the Output: Coded Data Table conventions including the Review column")
    if ARM in NEW:
        step7 = ("Step 7, which gives two coding procedures and says which one applies from the codebook's calibration status, and the Output: Coded Data Table conventions including the Review column. "
                 f"Calibration status of this codebook: {STATUS}")
    prompt = f"""You are the coder for one batch in a blind content-analysis run. Work only from the files named here. Use only the Read and Write tools. Do not search the web, do not open any other file or directory, and do not modify any file except the output file.

Read, in this order:
1. The instrument: `{SKILL}/skills/content-analysis/SKILL.md` (Content Analysis Skill {VER}). Your task is the full-corpus coding of Step 7; Steps 1–6 have been completed for this study and the codebook is frozen (`v1`). Follow {step7}.
2. The source declaration (Step 1 output, fixed): `{BENCH}/materials/{SET}_source_declaration.md`
{cb_lines}
4. The batch of units to code: `{bf}`

Then code every unit in the batch and write **one CSV file** to `{outcsv}` with the header exactly:

{cols}

Rules for the file: {outrule}{review_rule}
- Quote CSV fields that contain commas or quotes. UTF-8. No extra columns, no commentary in the file.
- No reference labels or expected frequencies exist in your inputs; do not guess at them. Do not use keyword matching or scripts to assign codes — read every unit.
- Do not alter the codebook. If a code seems missing, use the procedure in SKILL.md (UNCODED / note), not a new code.

When finished, reply with one line: the number of units coded and the number of rows written. Nothing else.
"""
    with open(f"{out}/prompt{n:02d}.md", "w", encoding="utf-8") as f:
        f.write(prompt)
json.dump(index, open(f"{out}/index.json", "w"), indent=0)
print(f"{SET} {ARM} run{RUN} {SPLIT}: {len(batches)} batches, {sum(len(b) for b in batches)} units -> {out}")
