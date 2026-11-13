#!/usr/bin/env python3
"""Addendum 2 analysis (beta.6 candidate on a second fresh sample): independent recomputation from the raw batch CSVs,
paired bootstrap (seed 20261113), the pre-registered hypotheses, the release rule and the arm-G reading."""
import csv, json, glob, random, collections, re
B = "/home/claude/bench"
U = {u["id"]: u for u in json.load(open(f"{B}/set3_units_reference.json"))}
fresh = sorted(json.load(open(f"{B}/splits_addendum2.json"))["set3_fresh2"])
earlier = set(json.load(open(f"{B}/splits.json"))["set3"]) | set(json.load(open(f"{B}/splits_addendum.json"))["set3_fresh"])
emo = open(f"{B}/codex_beta3/03_goemotions/emotions.txt").read().split()
ref = {k: set(U[k]["reference"]) for k in U}
FLAGS = ("context_missing", "possible_irony", "competing_codes", "insufficient_basis", "other")
ARMS = "AEHJG"

def raw(arm, run):
    p = collections.defaultdict(set); rev = collections.defaultdict(int); kinds = collections.Counter()
    for f in sorted(glob.glob(f"{B}/runs/set3/{arm}/run{run}/fresh2/batch*.csv")) + sorted(glob.glob(f"{B}/runs/set3/{arm}/run{run}/fresh2/gap*.csv")):
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
nref = sum(1 for u in fresh if "neutral" in ref[u])
res = {"n": len(fresh), "reference_labels": sum(len(ref[u]) for u in fresh), "neutral_ref": nref, "arms": {}, "bootstrap": {}, "review": {}, "hypotheses": {}}
print(f"second fresh sample: {len(fresh)} comments, {res['reference_labels']} reference labels; overlap with earlier samples: {len(set(fresh) & earlier)}")
print(f"\n{'arm/run':8s} {'assign':>6s} {'P':>5s} {'R':>5s} {'microF1':>7s} {'exNeut':>6s} {'macro':>6s} {'exact':>6s} {'review%':>7s} {'neutral':>8s} {'disappr':>8s}")
for (a, r), (p, rev, kinds) in sorted(P.items(), key=lambda kv: (ARMS.index(kv[0][0]), kv[0][1])):
    tp, fp, fn = counts(p, fresh); n = sum(len(p[u]) for u in fresh)
    ex = f1(*counts(p, fresh, set(emo)-{"neutral"})); m, mn = macro(p, fresh)
    exact = sum(1 for u in fresh if p[u] == ref[u])/len(fresh); rs = sum(rev[u] for u in fresh)/n if a != "A" else None
    dp = sum(1 for u in fresh if "disapproval" in p[u]); dr = sum(1 for u in fresh if "disapproval" in ref[u]); npred = sum(1 for u in fresh if "neutral" in p[u])
    res["arms"][f"{a}{r}"] = {"assignments": n, "precision": tp/(tp+fp), "recall": tp/(tp+fn), "micro_f1": f1(tp, fp, fn), "micro_f1_excl_neutral": ex, "macro_f1": m, "macro_n": mn,
                              "exact_match": exact, "review_share": rs, "review_kinds": dict(kinds), "flagged_comments": sum(1 for u in fresh if rev[u]),
                              "neutral_pred": npred, "disapproval_pred": dp, "disapproval_ref": dr}
    print(f"{a}{r:<7d} {n:6d} {100*tp/(tp+fp):5.1f} {100*tp/(tp+fn):5.1f} {100*f1(tp,fp,fn):7.1f} {100*ex:6.1f} {100*m:6.1f} {100*exact:6.1f} {'       ' if rs is None else f'{100*rs:7.1f}'} {npred:4d}/{nref} {dp:4d}/{dr}")

rng = random.Random(20261113); NB = 2000
idx = [[rng.randrange(len(fresh)) for _ in fresh] for _ in range(NB)]
pu = {k: [(len(p[u] & ref[u]), len(p[u] - ref[u]), len(ref[u] - p[u])) for u in fresh] for k, (p, _, _) in P.items()}
def boot(k1, k2):
    d = []
    for ix in idx:
        s1 = [sum(pu[k1][i][j] for i in ix) for j in range(3)]; s2 = [sum(pu[k2][i][j] for i in ix) for j in range(3)]
        d.append(f1(*s1) - f1(*s2))
    d.sort(); obs = f1(*[sum(x[j] for x in pu[k1]) for j in range(3)]) - f1(*[sum(x[j] for x in pu[k2]) for j in range(3)])
    return obs, d[int(0.025*NB)], d[int(0.975*NB)-1]
print("\npaired bootstrap, micro-F1 difference (2000 resamples of the 500 comments, seed 20261113), 95% interval:")
for x, y in (("H", "E"), ("H", "A"), ("E", "A"), ("J", "A"), ("J", "G"), ("G", "A"), ("J", "H")):
    for r1, r2 in ((1, 1), (2, 2), (1, 2), (2, 1)):
        o, lo, hi = boot((x, r1), (y, r2)); res["bootstrap"][f"{x}{r1}-{y}{r2}"] = [o, lo, hi]
        print(f"  {x}{r1} − {y}{r2}: {100*o:+.1f}  [{100*lo:+.1f}, {100*hi:+.1f}]  {'excludes 0' if lo > 0 or hi < 0 else 'includes 0'}{'' if r1 == r2 else '   (cross-run, not a decision pairing)'}")
b = res["bootstrap"]
H1_dir = all(b[f"H{r}-E{r}"][0] > 0 for r in (1, 2)); H1_imp = all(b[f"H{r}-E{r}"][1] > 0 for r in (1, 2))
H2 = all(not (b[f"H{r}-A{r}"][2] < 0) for r in (1, 2))
H3 = all(b[f"J{r}-A{r}"][0] > 0 and b[f"J{r}-A{r}"][1] > 0 for r in (1, 2))
print("\nReview flag: micro-F1 on comments with at least one flagged assignment vs none")
H4 = True
for a in "EHJG":
    for r in (1, 2):
        p, rev, _ = P[(a, r)]; fl = [u for u in fresh if rev[u]]; un = [u for u in fresh if not rev[u]]
        ff, fu = f1(*counts(p, fl)), f1(*counts(p, un))
        if a in "HJ": H4 = H4 and ff < fu
        res["review"][f"{a}{r}"] = {"flagged_comments": len(fl), "unflagged_comments": len(un), "f1_flagged": ff, "f1_unflagged": fu}
        print(f"  {a}{r}: flagged {len(fl):3d} comments F1 {100*ff:5.1f} | unflagged {len(un):3d} comments F1 {100*fu:5.1f}")
H5 = all(abs(res["arms"][f"H{r}"]["neutral_pred"] - nref) < abs(res["arms"][f"E{r}"]["neutral_pred"] - nref) for r in (1, 2))
release = H2 and H3 and H1_dir
def g_reading():
    v = [b[f"J{r}-G{r}"] for r in (1, 2)]
    if all(x[1] > 0 for x in v): return "stepwise procedure contributes on this material"
    if all(x[2] < 0 for x in v): return "short procedure does better on this material"
    return "no demonstrated difference"
res["hypotheses"] = {"H-1 direction": H1_dir, "H-1 improvement (both intervals exclude zero)": H1_imp, "H-2": H2, "H-3": H3, "H-4": H4, "H-5": H5, "release_rule_met": release, "arm_G_reading": g_reading()}
print(f"\nH-1 (H − E positive in both runs): {'HOLDS' if H1_dir else 'FAILS'}; called an improvement (both intervals exclude zero): {'YES' if H1_imp else 'NO'}")
print(f"H-2 (H not below A in both runs): {'HOLDS' if H2 else 'FAILS'}\nH-3 (J above A, interval excludes zero, both runs): {'HOLDS' if H3 else 'FAILS'}\nH-4 (flagged < unflagged, both runs of H and J): {'HOLDS' if H4 else 'FAILS'}\nH-5 (H's neutral count closer to the reference than E's, both runs): {'HOLDS' if H5 else 'FAILS'}")
print(f"RELEASE RULE (H-2 and H-3 and H − E positive in both runs): {'MET' if release else 'NOT MET'}\nArm G reading: {g_reading()}")
print("\nper code (mean of two runs): ref+ | pred A/E/H/J/G | F1 A/E/H/J/G")
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
    if rp: print(f"  {c:15s} {rp:3d} | " + " ".join(f"{row[a]['pred']:5.1f}" for a in ARMS) + " | " + " ".join(f"{100*row[a]['f1']:4.0f}" for a in ARMS))
res["per_code"] = pc
for a in ARMS:
    p1, p2 = P[(a, 1)][0], P[(a, 2)][0]
    tp = sum(len(p1[u] & p2[u]) for u in fresh); x = sum(len(p1[u] - p2[u]) for u in fresh); y = sum(len(p2[u] - p1[u]) for u in fresh)
    res["arms"][f"{a}_stability_f1"] = 2*tp/(2*tp+x+y); res["arms"][f"{a}_stability_exact"] = sum(1 for u in fresh if p1[u] == p2[u])/len(fresh)
print("\nrun-to-run F1:", {a: round(100*res['arms'][f'{a}_stability_f1'], 1) for a in ARMS}, "| identical label set:", {a: round(100*res['arms'][f'{a}_stability_exact'], 1) for a in ARMS})
cb = open(f"{B}/materials/set3_codebook_J.md", encoding="utf-8").read(); ids = set(re.findall(r"T\d{5}", cb))
leak = [u for u in fresh if len(U[u]["text"]) >= 25 and U[u]["text"] in cb]
dev = open(f"{B}/materials/set3_development_texts.md", encoding="utf-8").read(); rv = open(f"{B}/materials/set3_calibration_review_input.md", encoding="utf-8").read()
seen_ids = (set(re.findall(r"T\d{5}", dev)) | set(re.findall(r"T\d{5}", rv))) & set(fresh)
seen_txt = [u for u in fresh if len(U[u]["text"]) >= 25 and (U[u]["text"] in dev or U[u]["text"] in rv)]
print(f"\nleakage: codebook unit IDs among the new comments: {len(ids & set(fresh))}; new comments quoted verbatim in the codebook: {len(leak)}; new IDs / texts in drafter or reviewer inputs: {len(seen_ids)} / {len(seen_txt)}")
res["leakage"] = {"codebook_ids_in_fresh2": len(ids & set(fresh)), "fresh2_text_in_codebook": len(leak), "fresh2_ids_in_drafter_or_reviewer_inputs": len(seen_ids), "fresh2_text_in_drafter_or_reviewer_inputs": len(seen_txt)}
json.dump(res, open(f"{B}/results_set3_fresh2.json", "w"), indent=1)
