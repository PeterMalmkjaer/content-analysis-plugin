#!/usr/bin/env python3
"""Recompute the headline figures of the three GoEmotions reports from the two files in ../results/:
units.csv (unit, GoEmotions comment id, split, human reference labels) and assignments.csv
(every code each arm assigned in each run). Standard library only; run from anywhere:

    python3 docs/benchmarks/scripts/recompute.py

Prints, per sample / arm / run: assignments, precision, recall, micro-F1, share of assignments
flagged for review, and micro-F1 on comments with and without a flag."""
import csv, collections, os
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
ref, split = {}, {}
for r in csv.DictReader(open(os.path.join(here, "units.csv"), encoding="utf-8")):
    ref[r["unit"]] = set(r["reference_labels"].split(";")); split[r["unit"]] = r["split"]
pred = collections.defaultdict(lambda: collections.defaultdict(set)); flag = collections.defaultdict(lambda: collections.defaultdict(int))
for r in csv.DictReader(open(os.path.join(here, "assignments.csv"), encoding="utf-8")):
    k = (r["sample"], r["arm"], r["run"]); pred[k][r["unit"]].add(r["code"]); flag[k][r["unit"]] += bool(r["review"])
def f1(units, p):
    tp = sum(len(p[u] & ref[u]) for u in units); fp = sum(len(p[u] - ref[u]) for u in units); fn = sum(len(ref[u] - p[u]) for u in units)
    return tp, fp, fn, (2*tp/(2*tp+fp+fn) if tp else 0.0)
print(f"{'sample':10s} {'arm':3s} {'run':3s} {'assign':>6s} {'P':>5s} {'R':>5s} {'microF1':>7s} {'review%':>7s} {'F1 flagged':>10s} {'F1 unflagged':>12s}")
for k in sorted(pred):
    units = sorted(u for u in ref if split[u] == {"benchmark": "test"}.get(k[0], k[0])); p = pred[k]
    assert set(p) == set(units), f"coverage {k}"
    tp, fp, fn, f = f1(units, p); n = tp + fp; nf = sum(flag[k].values())
    fl = [u for u in units if flag[k][u]]; un = [u for u in units if not flag[k][u]]
    extra = f"{100*nf/n:7.1f} {100*f1(fl, p)[3]:10.1f} {100*f1(un, p)[3]:12.1f}" if nf else f"{'–':>7s} {'–':>10s} {'–':>12s}"
    print(f"{k[0]:10s} {k[1]:3s} {k[2]:3s} {n:6d} {100*tp/(tp+fp):5.1f} {100*tp/(tp+fn):5.1f} {100*f:7.1f} {extra}")
