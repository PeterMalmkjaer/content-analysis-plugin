#!/usr/bin/env python3
"""Addendum analysis (beta.5 test on fresh comments): independent recomputation from the raw batch CSVs,
paired bootstrap (seed 20261112), the three pre-registered hypotheses, per-code table, leakage checks."""
import csv, json, glob, random, collections, re
B = "/home/claude/bench"
U = {u["id"]: u for u in json.load(open(f"{B}/set3_units_reference.json"))}
fresh = sorted(json.load(open(f"{B}/splits_addendum.json"))["set3_fresh"])
old = json.load(open(f"{B}/splits.json"))["set3"]
emo = open(f"{B}/codex_beta3/03_goemotions/emotions.txt").read().split()
ref = {k: set(U[k]["reference"]) for k in U}
FLAGS = ("context_missing", "possible_irony", "competing_codes", "insufficient_basis", "other")
ARMS = "AEF"

def raw(arm, run):
    p = collections.defaultdict(set); rev = collections.defaultdict(int); kinds = collections.Counter()
    for f in sorted(glob.glob(f"{B}/runs/set3/{arm}/run{run}/fresh/batch*.csv")) + sorted(glob.glob(f"{B}/runs/set3/{arm}/run{run}/fresh/gap*.csv")):
        rd = csv.reader(open(f, encoding="utf-8-sig")); h = [x.strip() for x in next(rd)]
        for v in rd:
            if len(v) >= 2 and v[0].strip() in U and v[1].strip() in emo:
                p[v[0].strip()].add(v[1].strip())
                if "Review" in h and v[-1].strip() in FLAGS: rev[v[0].strip()] += 1; kinds[v[-1].strip()] += 1
    return p, rev, kinds
def counts(p, units, codes=None):
    tp = fp = fn = 0
    for u in units:
        P, R = p[u], ref[u]
        if codes is not None: P, R = P & codes, R & codes
        tp += len(P & R); fp += len(P - R); fn += len(R - P)
    return tp, fp, fn
def f1(tp, fp, fn): return 2*tp/(2*tp+fp+fn) if (2*tp+fp+fn) else 0.0
def macro(p, units):
    fs = []
    for c in emo:
        tp = sum(1 for u in units if c in p[u] and c in ref[u]); fp = sum(1 for u in units if c in p[u] and c not in ref[u]); fn = sum(1 for u in units if c not in p[u] and c in ref[u])
        if tp+fn: fs.append(f1(tp, fp, fn))
    return sum(fs)/len(fs), len(fs)

P = {(a, r): raw(a, r) for a in ARMS for r in (1, 2)}
assert all(set(P[k][0]) == set(fresh) for k in P), "coverage"
res = {"n": len(fresh), "reference_labels": sum(len(ref[u]) for u in fresh), "arms": {}, "bootstrap": {}, "review": {}, "hypotheses": {}}
print(f"fresh sample: {len(fresh)} comments, {res['reference_labels']} reference labels; overlap with earlier splits: {len(set(fresh) & set(old))}")
print(f"\n{'arm/run':8s} {'assign':>6s} {'P':>5s} {'R':>5s} {'microF1':>7s} {'exNeut':>6s} {'macro':>6s} {'exact':>6s} {'review%':>7s} {'disappr':>8s}")
for (a, r), (p, rev, kinds) in sorted(P.items()):
    tp, fp, fn = counts(p, fresh); n = sum(len(p[u]) for u in fresh)
    ex = f1(*counts(p, fresh, set(emo)-{"neutral"})); m, mn = macro(p, fresh)
    exact = sum(1 for u in fresh if p[u] == ref[u])/len(fresh); rs = sum(rev[u] for u in fresh)/n if a != "A" else None
    dp = sum(1 for u in fresh if "disapproval" in p[u]); dr = sum(1 for u in fresh if "disapproval" in ref[u])
    res["arms"][f"{a}{r}"] = {"assignments": n, "precision": tp/(tp+fp), "recall": tp/(tp+fn), "micro_f1": f1(tp, fp, fn), "micro_f1_excl_neutral": ex, "macro_f1": m, "macro_n": mn,
                              "exact_match": exact, "review_share": rs, "review_kinds": dict(kinds), "disapproval_pred": dp, "disapproval_ref": dr}
    print(f"{a}{r:<7d} {n:6d} {100*tp/(tp+fp):5.1f} {100*tp/(tp+fn):5.1f} {100*f1(tp,fp,fn):7.1f} {100*ex:6.1f} {100*m:6.1f} {100*exact:6.1f} {'' if rs is None else f'{100*rs:7.1f}'} {dp:4d}/{dr}")

rng = random.Random(20261112); NB = 2000
idx = [[rng.randrange(len(fresh)) for _ in fresh] for _ in range(NB)]
pu = {k: [(len(p[u] & ref[u]), len(p[u] - ref[u]), len(ref[u] - p[u])) for u in fresh] for k, (p, _, _) in P.items()}
def boot(k1, k2):
    d = []
    for ix in idx:
        s1 = [sum(pu[k1][i][j] for i in ix) for j in range(3)]; s2 = [sum(pu[k2][i][j] for i in ix) for j in range(3)]
        d.append(f1(*s1) - f1(*s2))
    d.sort(); obs = f1(*[sum(x[j] for x in pu[k1]) for j in range(3)]) - f1(*[sum(x[j] for x in pu[k2]) for j in range(3)])
    return obs, d[int(0.025*NB)], d[int(0.975*NB)-1]
print("\npaired bootstrap, micro-F1 difference (2000 resamples of the 500 fresh comments, seed 20261112), 95% interval:")
for x, y in (("E", "A"), ("F", "A"), ("F", "E")):
    for r1, r2 in ((1, 1), (2, 2), (1, 2), (2, 1)):
        o, lo, hi = boot((x, r1), (y, r2)); res["bootstrap"][f"{x}{r1}-{y}{r2}"] = [o, lo, hi]
        print(f"  {x}{r1} − {y}{r2}: {100*o:+.1f}  [{100*lo:+.1f}, {100*hi:+.1f}]  {'excludes 0' if lo > 0 or hi < 0 else 'includes 0'}{'' if r1 == r2 else '   (cross-run, not a decision pairing)'}")
b = res["bootstrap"]
HE = all(not (b[f"E{r}-A{r}"][2] < 0) for r in (1, 2))
HF = all(b[f"F{r}-A{r}"][0] > 0 and b[f"F{r}-A{r}"][1] > 0 for r in (1, 2))
print("\nReview flag: micro-F1 on comments with at least one flagged assignment vs none")
HR = True
for a in "EF":
    for r in (1, 2):
        p, rev, _ = P[(a, r)]; fl = [u for u in fresh if rev[u]]; un = [u for u in fresh if not rev[u]]
        ff, fu = f1(*counts(p, fl)), f1(*counts(p, un)); HR = HR and ff < fu
        res["review"][f"{a}{r}"] = {"flagged_comments": len(fl), "unflagged_comments": len(un), "f1_flagged": ff, "f1_unflagged": fu}
        print(f"  {a}{r}: flagged {len(fl):3d} comments F1 {100*ff:5.1f} | unflagged {len(un):3d} comments F1 {100*fu:5.1f}")
res["hypotheses"] = {"H-E": HE, "H-F": HF, "H-R": HR}
print(f"\nH-E (E not below A in both runs): {'HOLDS' if HE else 'FAILS'}\nH-F (F above A, interval excludes zero, both runs): {'HOLDS' if HF else 'FAILS'}\nH-R (flagged < unflagged in both runs of E and F): {'HOLDS' if HR else 'FAILS'}")
print("\nper code (fresh, mean of two runs): ref+ | pred A/E/F | F1 A/E/F")
pc = {}
for c in emo:
    rp = sum(1 for u in fresh if c in ref[u]); row = {"ref_pos": rp}
    for a in ARMS:
        fs = []; pr = []
        for r in (1, 2):
            p = P[(a, r)][0]; tp = sum(1 for u in fresh if c in p[u] and c in ref[u]); fp = sum(1 for u in fresh if c in p[u] and c not in ref[u])
            fs.append(f1(tp, fp, rp - tp)); pr.append(tp+fp)
        row[a] = {"f1": sum(fs)/2, "pred": sum(pr)/2}
    pc[c] = row
    if rp: print(f"  {c:15s} {rp:3d} | {row['A']['pred']:5.1f} {row['E']['pred']:5.1f} {row['F']['pred']:5.1f} | {100*row['A']['f1']:4.0f} {100*row['E']['f1']:4.0f} {100*row['F']['f1']:4.0f}")
res["per_code"] = pc
# run-to-run agreement per arm, recomputed
for a in ARMS:
    p1, p2 = P[(a, 1)][0], P[(a, 2)][0]
    tp = sum(len(p1[u] & p2[u]) for u in fresh); x = sum(len(p1[u] - p2[u]) for u in fresh); y = sum(len(p2[u] - p1[u]) for u in fresh)
    res["arms"][f"{a}_stability_f1"] = 2*tp/(2*tp+x+y)
print("\nrun-to-run F1:", {a: round(100*res['arms'][f'{a}_stability_f1'], 1) for a in ARMS})
# leakage
cb = open(f"{B}/materials/set3_codebook_F.md", encoding="utf-8").read(); ids = set(re.findall(r"T\d{5}", cb))
leak = [u for u in fresh if len(U[u]["text"]) >= 25 and U[u]["text"] in cb]
dev = open(f"{B}/materials/set3_development_texts.md", encoding="utf-8").read(); rv = open(f"{B}/materials/set3_calibration_review_input.md", encoding="utf-8").read()
seen_ids = (set(re.findall(r"T\d{5}", dev)) | set(re.findall(r"T\d{5}", rv))) & set(fresh)
seen_txt = [u for u in fresh if len(U[u]["text"]) >= 25 and (U[u]["text"] in dev or U[u]["text"] in rv)]
print(f"\nleakage: unit IDs in the arm-F codebook that are fresh comments: {len(ids & set(fresh))}; fresh comments quoted verbatim in the codebook: {len(leak)}; fresh IDs / texts in drafter or reviewer inputs: {len(seen_ids)} / {len(seen_txt)}")
res["leakage"] = {"codebook_ids_in_fresh": len(ids & set(fresh)), "fresh_text_in_codebook": len(leak), "fresh_ids_in_drafter_or_reviewer_inputs": len(seen_ids), "fresh_text_in_drafter_or_reviewer_inputs": len(seen_txt)}
json.dump(res, open(f"{B}/results_set3_fresh.json", "w"), indent=1)
