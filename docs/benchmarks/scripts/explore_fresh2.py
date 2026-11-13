#!/usr/bin/env python3
"""Exploratory (NOT pre-registered) follow-ups on the second fresh sample."""
import json, random, io, contextlib, importlib.util
spec = importlib.util.spec_from_file_location("af2", "/home/claude/bench/analyse_fresh2.py")
m = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
P, fresh, ref, emo, f1, counts = m.P, m.fresh, m.ref, m.emo, m.f1, m.counts
out = {}
print("1. the same comments, both arms: split by the arm's own Review flag")
for a in "EH":
    for r in (1, 2):
        p, rev, _ = P[(a, r)]; pa = P[("A", r)][0]
        fl = [u for u in fresh if rev[u]]; un = [u for u in fresh if not rev[u]]
        row = {"flagged_n": len(fl), f"{a}_flagged": f1(*counts(p, fl)), "A_flagged": f1(*counts(pa, fl)), f"{a}_unflagged": f1(*counts(p, un)), "A_unflagged": f1(*counts(pa, un)),
               "neutral_ref_share_flagged": sum("neutral" in ref[u] for u in fl)/len(fl), "neutral_ref_share_unflagged": sum("neutral" in ref[u] for u in un)/len(un)}
        out[f"split_{a}{r}"] = row
        print(f"   {a}{r}: flagged ({len(fl)}): {a} {100*row[f'{a}_flagged']:.1f} vs A {100*row['A_flagged']:.1f} | unflagged ({len(un)}): {a} {100*row[f'{a}_unflagged']:.1f} vs A {100*row['A_unflagged']:.1f} | reference neutral: flagged {100*row['neutral_ref_share_flagged']:.0f}%, unflagged {100*row['neutral_ref_share_unflagged']:.0f}%")
print("2. neutral: precision / recall per arm and run")
for a in "AEHJG":
    for r in (1, 2):
        p = P[(a, r)][0]; tp = sum(1 for u in fresh if "neutral" in p[u] and "neutral" in ref[u]); pp = sum(1 for u in fresh if "neutral" in p[u]); rp = sum(1 for u in fresh if "neutral" in ref[u])
        out[f"neutral_{a}{r}"] = {"pred": pp, "precision": tp/pp, "recall": tp/rp}
        print(f"   {a}{r}: assigned {pp:3d}  precision {100*tp/pp:.0f}  recall {100*tp/rp:.0f}")
print("3. macro-F1 differences, paired bootstrap (seed 20261113)")
rng = random.Random(20261113); NB = 2000; idx = [[rng.randrange(len(fresh)) for _ in fresh] for _ in range(NB)]
def macro_on(p, units):
    fs = []
    for c in emo:
        tp = fp = fn = 0
        for u in units:
            a, b = c in p[u], c in ref[u]; tp += a and b; fp += a and not b; fn += b and not a
        if tp+fn: fs.append(f1(tp, fp, fn))
    return sum(fs)/len(fs)
for x, y in (("J", "A"), ("J", "G"), ("H", "E")):
    for r in (1, 2):
        px, py = P[(x, r)][0], P[(y, r)][0]; d = sorted(macro_on(px, [fresh[i] for i in ix]) - macro_on(py, [fresh[i] for i in ix]) for ix in idx)
        o = macro_on(px, fresh) - macro_on(py, fresh); out[f"macro_{x}{r}-{y}{r}"] = [o, d[int(.025*NB)], d[int(.975*NB)-1]]
        print(f"   {x}{r} − {y}{r}: {100*o:+.1f} [{100*d[int(.025*NB)]:+.1f}, {100*d[int(.975*NB)-1]:+.1f}]")
print("4. flag kinds:", {f"{a}{r}": dict(P[(a, r)][2]) for a in "EHJG" for r in (1, 2)})
json.dump(out, open("/home/claude/bench/results_set3_fresh2_exploratory.json", "w"), indent=1)
