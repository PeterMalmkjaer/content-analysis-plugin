#!/usr/bin/env python3
"""Exploratory (NOT pre-registered) follow-ups on the fresh sample. Reuses analyse_fresh's loaders."""
import json, random, collections, io, contextlib, importlib.util
spec = importlib.util.spec_from_file_location("af", "/home/claude/bench/analyse_fresh.py")
af = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(af)
P, fresh, ref, emo, f1, counts = af.P, af.fresh, af.ref, af.emo, af.f1, af.counts
out = {}
rng = random.Random(20261112); NB = 2000; idx = [[rng.randrange(len(fresh)) for _ in fresh] for _ in range(NB)]
def macro_on(p, units):
    fs = []
    for c in emo:
        tp = fp = fn = 0
        for u in units:
            a, b = c in p[u], c in ref[u]; tp += a and b; fp += a and not b; fn += b and not a
        if tp+fn: fs.append(f1(tp, fp, fn))
    return sum(fs)/len(fs)
print("1. macro-F1 difference, paired bootstrap (exploratory)")
for x, y in (("F", "A"), ("E", "A")):
    for r in (1, 2):
        px, py = P[(x, r)][0], P[(y, r)][0]; d = sorted(macro_on(px, [fresh[i] for i in ix]) - macro_on(py, [fresh[i] for i in ix]) for ix in idx)
        o = macro_on(px, fresh) - macro_on(py, fresh); lo, hi = d[int(.025*NB)], d[int(.975*NB)-1]; out[f"macro_{x}{r}-{y}{r}"] = [o, lo, hi]
        print(f"   {x}{r} − {y}{r}: {100*o:+.1f} [{100*lo:+.1f}, {100*hi:+.1f}]")
print("2. micro-F1 excluding neutral, E − A (exploratory)")
codes = set(emo) - {"neutral"}
for r in (1, 2):
    pe, pa = P[("E", r)][0], P[("A", r)][0]
    def d_on(units): return f1(*counts(pe, units, codes)) - f1(*counts(pa, units, codes))
    d = sorted(d_on([fresh[i] for i in ix]) for ix in idx); o = d_on(fresh); out[f"exneutral_E{r}-A{r}"] = [o, d[int(.025*NB)], d[int(.975*NB)-1]]
    print(f"   E{r} − A{r}: {100*o:+.1f} [{100*d[int(.025*NB)]:+.1f}, {100*d[int(.975*NB)-1]:+.1f}]")
print("3. the same comments, both arms: split by arm E's / F's Review flag (exploratory)")
for a in "EF":
    for r in (1, 2):
        p, rev, _ = P[(a, r)]; pa = P[("A", r)][0]
        fl = [u for u in fresh if rev[u]]; un = [u for u in fresh if not rev[u]]
        row = {"flagged_n": len(fl), f"{a}_flagged": f1(*counts(p, fl)), "A_flagged": f1(*counts(pa, fl)), f"{a}_unflagged": f1(*counts(p, un)), "A_unflagged": f1(*counts(pa, un)),
               "neutral_ref_share_flagged": sum("neutral" in ref[u] for u in fl)/len(fl), "neutral_ref_share_unflagged": sum("neutral" in ref[u] for u in un)/len(un)}
        out[f"split_{a}{r}"] = row
        print(f"   {a}{r}: flagged ({len(fl)}): {a} {100*row[f'{a}_flagged']:.1f} vs A {100*row['A_flagged']:.1f} | unflagged ({len(un)}): {a} {100*row[f'{a}_unflagged']:.1f} vs A {100*row['A_unflagged']:.1f} | reference says neutral: flagged {100*row['neutral_ref_share_flagged']:.0f}%, unflagged {100*row['neutral_ref_share_unflagged']:.0f}%")
print("4. flag kinds:", {f"{a}{r}": dict(P[(a, r)][2]) for a in "EF" for r in (1, 2)})
print("5. neutral: predicted / reference 147:", {f"{a}{r}": sum('neutral' in P[(a, r)][0][u] for u in fresh) for a in "AEF" for r in (1, 2)})
json.dump(out, open("/home/claude/bench/results_set3_fresh_exploratory.json", "w"), indent=1)
