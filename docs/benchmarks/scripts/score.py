#!/usr/bin/env python3
"""Score one (set, arm, run, split) against the reference. Prints a summary and writes
runs/<set>/<arm>/run<N>/<split>/out/metrics.json. Usage: score.py SET ARM RUN [--split test]"""
import csv, json, sys, collections, math
SET, ARM, RUN = sys.argv[1], sys.argv[2], int(sys.argv[3])
SPLIT = sys.argv[sys.argv.index("--split")+1] if "--split" in sys.argv else "test"
BENCH = "/home/claude/bench"
d = f"{BENCH}/runs/{SET}/{ARM}/run{RUN}/{SPLIT}"
rows = list(csv.DictReader(open(f"{d}/out/coded_data.csv", encoding="utf-8-sig")))
expected = [u for b in json.load(open(f"{d}/index.json")) for u in b["units"]]

def ukey(r): return f"{r['Document ID']}|{r['Unit ID']}"

# ---- predictions and references as sets of codes per unit
pred = collections.defaultdict(set); review = collections.defaultdict(set); notes = {}
for r in rows:
    k = ukey(r)
    if r["Code ID"] != "UNCODED": pred[k].add(r["Code ID"])
    if r.get("Review"): review[k].add(r["Code ID"])
ref = collections.defaultdict(set)
if SET == "set1":
    for doc, u, c in json.load(open(f"{BENCH}/set1_units_reference.json"))["reference"]:
        ref[f"{doc}|{u}"].add(c)
elif SET == "set2":
    R = json.load(open(f"{BENCH}/set2_units_reference.json"))["reference"]
    for k, fields in R.items():
        ref[k].add(f"GOV_RELEVANT={fields['GOV_RELEVANT']}")
        if fields["GOV_RELEVANT"] != "N":
            for f in ("PHASE", "AUTH_REQ", "GC_PRIMARY", "INTEREST_ORIENTATION"):
                ref[k].add(f"{f}={fields[f]}")
else:
    for u in json.load(open(f"{BENCH}/set3_units_reference.json")):
        ref[f"{u['id']}|1"] = set(u["reference"])
units = expected
codes = sorted(set(c for k in units for c in ref[k]) | set(c for k in units for c in pred[k]))

def prf(tp, fp, fn):
    p = tp/(tp+fp) if tp+fp else 0.0; r = tp/(tp+fn) if tp+fn else 0.0
    f = 2*p*r/(p+r) if p+r else 0.0
    return p, r, f
def kappa(tp, fp, fn, tn):
    n = tp+fp+fn+tn; po = (tp+tn)/n
    pe = ((tp+fp)*(tp+fn) + (fn+tn)*(fp+tn))/(n*n)
    return (po-pe)/(1-pe) if pe < 1 else float("nan")
def alpha_binary(tp, fp, fn, tn):
    # Krippendorff's alpha, nominal, 2 coders, binary: 1 - Do/De with disagreement counts
    n = tp+fp+fn+tn
    # values: coder1 (pred) 1s = tp+fp, 0s = fn+tn; coder2 (ref) 1s = tp+fn, 0s = fp+tn
    n1 = (tp+fp)+(tp+fn); n0 = (fn+tn)+(fp+tn); N = n1+n0
    Do = (fp+fn)  # disagreeing pairs (each unit one pair)
    if N <= 1 or n1 == 0 or n0 == 0: return float("nan")
    De = (n1*n0)/(N-1)  # expected disagreements per unit-pair scaled: for 2 coders, alpha = 1 - (N-1)*Do/(n1*n0)
    return 1 - (N-1)*Do/(n1*n0)

per = {}
TP = FP = FN = 0
macro = []
for c in codes:
    tp = sum(1 for k in units if c in pred[k] and c in ref[k]); fp = sum(1 for k in units if c in pred[k] and c not in ref[k])
    fn = sum(1 for k in units if c not in pred[k] and c in ref[k]); tn = len(units)-tp-fp-fn
    p, r, f = prf(tp, fp, fn)
    per[c] = {"ref_pos": tp+fn, "pred_pos": tp+fp, "tp": tp, "fp": fp, "fn": fn, "precision": p, "recall": r, "f1": f,
              "kappa": kappa(tp, fp, fn, tn), "alpha": alpha_binary(tp, fp, fn, tn), "ratio": ((tp+fp)/(tp+fn) if tp+fn else None),
              "review_flags": sum(1 for k in units if c in review[k])}
    TP += tp; FP += fp; FN += fn
    if tp+fn > 0: macro.append(f)
mp, mr, mf = prf(TP, FP, FN)
exact = sum(1 for k in units if pred[k] == ref[k]) / len(units)
n_assign = sum(len(pred[k]) for k in units); n_review = sum(len(review[k]) for k in units)
uncoded = sum(1 for k in units if not pred[k])
res = {"set": SET, "arm": ARM, "run": RUN, "split": SPLIT, "units": len(units), "assignments": n_assign,
       "micro": {"precision": mp, "recall": mr, "f1": mf, "tp": TP, "fp": FP, "fn": FN},
       "macro_f1": sum(macro)/len(macro) if macro else None, "macro_n_codes": len(macro),
       "macro_f1_range": [min(macro), max(macro)] if macro else None, "exact_match": exact,
       "uncoded_units": uncoded, "review_share": (n_review/n_assign if n_assign else None), "review_flags": n_review,
       "other_share_of_flags": None, "per_code": per}
if ARM != "A":
    oth = sum(1 for r in rows if r.get("Review") == "other")
    res["other_share_of_flags"] = oth/n_review if n_review else None
if SET == "set3":
    # excluding neutral
    tp = fp = fn = 0
    for k in units:
        P = pred[k]-{"neutral"}; Rf = ref[k]-{"neutral"}
        tp += len(P & Rf); fp += len(P-Rf); fn += len(Rf-P)
    res["micro_f1_excl_neutral"] = prf(tp, fp, fn)[2]
    res["neutral_plus_emotion_in_ref"] = sum(1 for k in units if "neutral" in ref[k] and len(ref[k]) > 1)
if SET == "set2":
    g_ref = {k: [c for c in ref[k] if c.startswith("GOV_RELEVANT=")][0] for k in units}
    g_pred = {k: ([c for c in pred[k] if c.startswith("GOV_RELEVANT=")] or ["(none)"])[0] for k in units}
    refN = [k for k in units if g_ref[k] == "GOV_RELEVANT=N"]; refPos = [k for k in units if g_ref[k] != "GOV_RELEVANT=N"]
    res["gate"] = {"ref_N": len(refN), "ref_N_coded_relevant": sum(1 for k in refN if g_pred[k] in ("GOV_RELEVANT=RESP", "GOV_RELEVANT=MECH")),
                   "ref_pos": len(refPos), "ref_pos_coded_N": sum(1 for k in refPos if g_pred[k] == "GOV_RELEVANT=N"),
                   "gate_agreement": sum(1 for k in units if g_pred[k] == g_ref[k])/len(units)}
    fields = {}
    for f in ("PHASE", "AUTH_REQ", "GC_PRIMARY", "INTEREST_ORIENTATION"):
        agree = 0
        for k in refPos:
            rv = [c for c in ref[k] if c.startswith(f+"=")]; pv = [c for c in pred[k] if c.startswith(f+"=")]
            if rv and pv and rv[0] == pv[0]: agree += 1
        fields[f] = agree/len(refPos)
    res["field_agreement_on_ref_positive"] = fields
json.dump(res, open(f"{d}/out/metrics.json", "w"), indent=1)
print(f"{SET} {ARM} run{RUN} {SPLIT}: units {len(units)}  assignments {n_assign}  micro P/R/F1 = {mp*100:.1f}/{mr*100:.1f}/{mf*100:.1f}  "
      f"macro-F1 {res['macro_f1']*100:.1f} over {len(macro)} codes (range {res['macro_f1_range'][0]*100:.0f}–{res['macro_f1_range'][1]*100:.0f})  "
      f"exact {exact*100:.1f}%  uncoded {uncoded}" + (f"  review share {res['review_share']*100:.1f}% ({n_review} flags, other {res['other_share_of_flags']})" if ARM != "A" else ""))
if SET == "set3": print(f"  micro-F1 excl. neutral {res['micro_f1_excl_neutral']*100:.1f}; ref units with neutral+emotion: {res['neutral_plus_emotion_in_ref']}")
if SET == "set2": print("  gate:", res["gate"], " fields:", {k: round(v*100, 1) for k, v in fields.items()})
