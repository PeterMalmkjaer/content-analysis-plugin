#!/usr/bin/env python3
"""Set 3 analysis: independent recomputation from raw batch CSVs, paired bootstrap, restricted averages, hypotheses."""
import csv, json, glob, random, collections, re, sys
B = "/home/claude/bench"
splits = json.load(open(f"{B}/splits.json"))["set3"]
U = {u["id"]: u for u in json.load(open(f"{B}/set3_units_reference.json"))}
test = sorted(k for k, v in splits.items() if v == "test"); cal = sorted(k for k, v in splits.items() if v == "calibration"); ret = sorted(k for k, v in splits.items() if v == "retest")
emo = open(f"{B}/codex_beta3/03_goemotions/emotions.txt").read().split()
ref = {k: set(U[k]["reference"]) for k in U}

def raw(arm, run, split="test"):
    """Read raw batch/gap CSVs directly (independent of assemble.py): first column = Document ID, second = Code ID."""
    p = collections.defaultdict(set); rev = collections.defaultdict(int)
    for f in sorted(glob.glob(f"{B}/runs/set3/{arm}/run{run}/{split}/batch*.csv")) + sorted(glob.glob(f"{B}/runs/set3/{arm}/run{run}/{split}/gap*.csv")):
        rd = csv.reader(open(f, encoding="utf-8-sig")); h = next(rd)
        for v in rd:
            if len(v) >= 2 and v[0].strip() in U and v[1].strip() in emo:
                p[v[0].strip()].add(v[1].strip())
                if "Review" in h and v[-1].strip() in ("context_missing", "possible_irony", "competing_codes", "insufficient_basis", "other"): rev[v[0].strip()] += 1
    return p, rev

def counts(p, units, codes=None):
    tp = fp = fn = 0
    for u in units:
        P = p[u]; R = ref[u]
        if codes is not None: P = P & codes; R = R & codes
        tp += len(P & R); fp += len(P - R); fn += len(R - P)
    return tp, fp, fn
def f1(tp, fp, fn): return 2*tp/(2*tp+fp+fn) if (2*tp+fp+fn) else 0.0
def macro(p, units, codes):
    fs = []
    for c in codes:
        tp = sum(1 for u in units if c in p[u] and c in ref[u]); fp = sum(1 for u in units if c in p[u] and c not in ref[u]); fn = sum(1 for u in units if c not in p[u] and c in ref[u])
        if tp+fn: fs.append(f1(tp, fp, fn))
    return sum(fs)/len(fs), len(fs), min(fs), max(fs)

P = {(a, r): raw(a, r) for a in "ABC" for r in (1, 2)}
# sufficiently calibrated codes: >=10 human positives in the calibration split
calpos = collections.Counter(l for u in cal for l in ref[u])
suff = set(c for c in emo if calpos[c] >= 10); insuff = [c for c in emo if calpos[c] < 10]
print("sufficiently calibrated codes (>=10 human positives in calibration):", len(suff)); print("insufficiently calibrated:", [(c, calpos[c]) for c in insuff])
res = {"arms": {}, "bootstrap": {}, "insufficiently_calibrated": {c: calpos[c] for c in insuff}}
print(f"\n{'arm/run':8s} {'assign':>6s} {'P':>5s} {'R':>5s} {'microF1':>7s} {'exNeut':>6s} {'suffF1':>6s} {'macro':>6s} {'macroSuff':>9s} {'exact':>6s} {'review%':>7s}")
for (a, r), (p, rev) in sorted(P.items()):
    tp, fp, fn = counts(p, test); n = sum(len(p[u]) for u in test)
    ex = f1(*counts(p, test, set(emo)-{"neutral"})); sf = f1(*counts(p, test, suff))
    m, mn, lo, hi = macro(p, test, emo); ms, msn, _, _ = macro(p, test, sorted(suff))
    exact = sum(1 for u in test if p[u] == ref[u])/len(test); rs = sum(rev[u] for u in test)/n if a != "A" else None
    res["arms"][f"{a}{r}"] = {"assignments": n, "precision": tp/(tp+fp), "recall": tp/(tp+fn), "micro_f1": f1(tp, fp, fn), "micro_f1_excl_neutral": ex, "micro_f1_sufficient_codes": sf,
                              "macro_f1": m, "macro_n": mn, "macro_range": [lo, hi], "macro_f1_sufficient_codes": ms, "exact_match": exact, "review_share": rs,
                              "disapproval_pred": sum(1 for u in test if "disapproval" in p[u]), "disapproval_ref": sum(1 for u in test if "disapproval" in ref[u])}
    print(f"{a}{r:<7d} {n:6d} {100*tp/(tp+fp):5.1f} {100*tp/(tp+fn):5.1f} {100*f1(tp,fp,fn):7.1f} {100*ex:6.1f} {100*sf:6.1f} {100*m:6.1f} {100*ms:9.1f} {100*exact:6.1f} {'' if rs is None else f'{100*rs:7.1f}'}")

# paired bootstrap over units
rng = random.Random(20260910); NB = 2000
idx = [[rng.randrange(len(test)) for _ in test] for _ in range(NB)]
per_unit = {k: [(len(p[u] & ref[u]), len(p[u] - ref[u]), len(ref[u] - p[u])) for u in test] for k, (p, _) in P.items()}
def boot(k1, k2):
    d = []
    for ix in idx:
        s1 = [sum(per_unit[k1][i][j] for i in ix) for j in range(3)]; s2 = [sum(per_unit[k2][i][j] for i in ix) for j in range(3)]
        d.append(f1(*s1) - f1(*s2))
    d.sort(); obs = f1(*[sum(x[j] for x in per_unit[k1]) for j in range(3)]) - f1(*[sum(x[j] for x in per_unit[k2]) for j in range(3)])
    return obs, d[int(0.025*NB)], d[int(0.975*NB)-1]
print("\npaired bootstrap, micro-F1 difference (2000 resamples of the 500 test units, seed 20260910), 95% interval:")
for x, y in (("C", "A"), ("B", "A"), ("C", "B")):
    for r in (1, 2):
        o, lo, hi = boot((x, r), (y, r)); res["bootstrap"][f"{x}{r}-{y}{r}"] = [o, lo, hi]
        print(f"  {x}{r} − {y}{r}: {100*o:+.1f}  [{100*lo:+.1f}, {100*hi:+.1f}]  {'excludes 0' if lo > 0 or hi < 0 else 'includes 0'}")
    # cross-run pairings, to show run noise does not drive it
    for r1, r2 in ((1, 2), (2, 1)):
        o, lo, hi = boot((x, r1), (y, r2)); res["bootstrap"][f"{x}{r1}-{y}{r2}"] = [o, lo, hi]
        print(f"  {x}{r1} − {y}{r2}: {100*o:+.1f}  [{100*lo:+.1f}, {100*hi:+.1f}]")
# per-code table across arms (mean of two runs)
print("\nper code (test, mean of two runs): ref+ | pred A/B/C | F1 A/B/C")
pc = {}
for c in emo:
    rp = sum(1 for u in test if c in ref[u]); row = {"ref_pos": rp}
    for a in "ABC":
        fs = []; pr = []
        for r in (1, 2):
            p = P[(a, r)][0]; tp = sum(1 for u in test if c in p[u] and c in ref[u]); fp = sum(1 for u in test if c in p[u] and c not in ref[u]); fn = rp - tp
            fs.append(f1(tp, fp, fn)); pr.append(tp+fp)
        row[a] = {"f1": sum(fs)/2, "pred": sum(pr)/2}
    pc[c] = row
    if rp: print(f"  {c:15s} {rp:3d} | {row['A']['pred']:5.1f} {row['B']['pred']:5.1f} {row['C']['pred']:5.1f} | {100*row['A']['f1']:4.0f} {100*row['B']['f1']:4.0f} {100*row['C']['f1']:4.0f}{'   (insufficiently calibrated)' if c in insuff else ''}")
res["per_code"] = pc
# leakage checks
cb = open(f"{B}/materials/set3_codebook_C.md", encoding="utf-8").read(); ids = set(re.findall(r"T\d{5}", cb))
rv = open(f"{B}/materials/set3_calibration_review_input.md", encoding="utf-8").read(); rids = set(re.findall(r"T\d{5}", rv))
print(f"\nleakage check: unit IDs quoted in the frozen arm-C codebook: {len(ids)}; of these in test split: {len(ids & set(test))}, in retest: {len(ids & set(ret))}, in calibration: {len(ids & set(cal))}")
print(f"               unit IDs in the reviewer's input: {len(rids)}; in test: {len(rids & set(test))}, in retest: {len(rids & set(ret))}")
# verbatim-text leakage: does any test comment text (>=25 chars) appear in the C codebook?
leak = [u for u in test if len(U[u]["text"]) >= 25 and U[u]["text"] in cb]
print(f"               test comments quoted verbatim in the arm-C codebook: {len(leak)}")
res["leakage"] = {"codebook_ids_in_test": len(ids & set(test)), "codebook_ids_in_retest": len(ids & set(ret)), "review_input_ids_in_test": len(rids & set(test)), "test_text_in_codebook": len(leak)}
json.dump(res, open(f"{B}/results_set3.json", "w"), indent=1)
