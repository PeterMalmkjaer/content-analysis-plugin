#!/usr/bin/env python3
"""Run-to-run consistency of one arm: treat run 1 and run 2 as two coders. Usage: stability.py SET ARM [--split test]"""
import csv, json, sys, collections
SET, ARM = sys.argv[1], sys.argv[2]
SPLIT = sys.argv[sys.argv.index("--split")+1] if "--split" in sys.argv else "test"
B = "/home/claude/bench"
def load(run):
    p = collections.defaultdict(set)
    for r in csv.DictReader(open(f"{B}/runs/{SET}/{ARM}/run{run}/{SPLIT}/out/coded_data.csv", encoding="utf-8-sig")):
        if r["Code ID"] != "UNCODED": p[f"{r['Document ID']}|{r['Unit ID']}"].add(r["Code ID"])
    return p
units = [u for b in json.load(open(f"{B}/runs/{SET}/{ARM}/run1/{SPLIT}/index.json")) for u in b["units"]]
a, b = load(1), load(2)
tp = sum(len(a[u] & b[u]) for u in units); x = sum(len(a[u] - b[u]) for u in units); y = sum(len(b[u] - a[u]) for u in units)
f1 = 2*tp/(2*tp+x+y); exact = sum(1 for u in units if a[u] == b[u])/len(units)
codes = sorted(set(c for u in units for c in a[u] | b[u])); ks = []
for c in codes:
    n11 = sum(1 for u in units if c in a[u] and c in b[u]); n10 = sum(1 for u in units if c in a[u] and c not in b[u])
    n01 = sum(1 for u in units if c not in a[u] and c in b[u]); n00 = len(units)-n11-n10-n01
    po = (n11+n00)/len(units); pe = ((n11+n10)*(n11+n01)+(n01+n00)*(n10+n00))/len(units)**2
    if pe < 1: ks.append((po-pe)/(1-pe))
res = {"set": SET, "arm": ARM, "split": SPLIT, "f1_between_runs": f1, "exact_between_runs": exact, "mean_kappa": sum(ks)/len(ks), "kappa_range": [min(ks), max(ks)], "n_codes": len(ks)}
json.dump(res, open(f"{B}/runs/{SET}/{ARM}/stability_{SPLIT}.json", "w"), indent=1)
print(f"{SET} {ARM} stability ({SPLIT}): F1 between runs {f1*100:.1f}, exact set match {exact*100:.1f}%, mean per-code kappa {res['mean_kappa']:.3f} (range {min(ks):.2f}–{max(ks):.2f}, {len(ks)} codes)")
