# Inter-Coder Reliability Guide

This reference provides formulas, worked examples, and implementation guidance for the four main inter-coder reliability (ICR) metrics used in content analysis.

## Table of Contents

1. [Percentage Agreement](#percentage-agreement)
2. [Cohen's Kappa (κ)](#cohens-kappa)
3. [Fleiss' Kappa](#fleiss-kappa)
4. [Krippendorff's Alpha (α)](#krippendorffs-alpha)
5. [Choosing the Right Metric](#choosing-the-right-metric)
6. [Python Implementation](#python-implementation)

---

## Percentage Agreement

The simplest measure: proportion of units on which coders agree.

**Formula:**
```
PA = (number of agreements) / (total number of units coded)
```

**Example:**
Two coders code 100 paragraphs into 3 categories. They agree on 78.
PA = 78/100 = 0.78 (78%)

**Limitations:**
- Does not account for chance agreement
- Inflated when categories are unevenly distributed (if 90% of units fall in one category, two random coders would agree ~81% of the time by chance)
- Report alongside a chance-corrected metric, never alone

---

## Cohen's Kappa (κ)

Chance-corrected agreement for **two coders** with **nominal categories**.

**Formula:**
```
κ = (P_o - P_e) / (1 - P_e)
```

Where:
- P_o = observed proportion of agreement (same as percentage agreement)
- P_e = expected proportion of agreement by chance

**Computing P_e:**
For each category k, compute the proportion each coder assigned to that category, then:
```
P_e = Σ_k (p_1k × p_2k)
```
where p_1k is the proportion coder 1 assigned to category k, and p_2k is the proportion coder 2 assigned to category k.

**Worked Example:**

Two coders, 3 categories (A, B, C), 50 units:

|          | Coder 2: A | Coder 2: B | Coder 2: C | Total |
|----------|-----------|-----------|-----------|-------|
| Coder 1: A | 15        | 2         | 1         | 18    |
| Coder 1: B | 3         | 12        | 2         | 17    |
| Coder 1: C | 1         | 1         | 13        | 15    |
| Total    | 19        | 15        | 16        | 50    |

P_o = (15 + 12 + 13) / 50 = 40/50 = 0.80

P_e = (18/50 × 19/50) + (17/50 × 15/50) + (15/50 × 16/50)
    = 0.1368 + 0.1020 + 0.0960 = 0.3348

κ = (0.80 - 0.3348) / (1 - 0.3348) = 0.4652 / 0.6652 = 0.699

**Interpretation (Landis & Koch, 1977):**
- κ < 0.00: Less than chance agreement
- 0.00–0.20: Slight
- 0.21–0.40: Fair
- 0.41–0.60: Moderate
- 0.61–0.80: Substantial
- 0.81–1.00: Almost perfect

---

## Fleiss' Kappa

Extension of kappa for **multiple coders** (≥ 2) with **nominal categories**.

**Formula:**
```
κ = (P̄ - P̄_e) / (1 - P̄_e)
```

Where:
- P̄ = mean proportion of pairwise agreements across all units
- P̄_e = expected agreement by chance

**Computing P̄:**
For each unit i, let n_ij be the number of coders who assigned category j. With n coders total:
```
P_i = (1 / (n(n-1))) × Σ_j (n_ij × (n_ij - 1))
P̄ = (1/N) × Σ_i P_i
```

**Computing P̄_e:**
```
p_j = (1/(N×n)) × Σ_i n_ij    (overall proportion for category j)
P̄_e = Σ_j p_j²
```

**Use when:** 3+ coders, all coders code all units, nominal categories.

---

## Krippendorff's Alpha (α)

The most general and recommended metric. Works with any number of coders, any measurement level, and handles missing data.

**Formula:**
```
α = 1 - (D_o / D_e)
```

Where:
- D_o = observed disagreement
- D_e = expected disagreement by chance

**For nominal data:**
```
D_o = (1 / (n×N)) × Σ over all pairs of values within units: δ²(c, k)
```
where δ²(c, k) = 0 if c = k, 1 if c ≠ k (the difference function for nominal data).

**Thresholds (Krippendorff, 2018):**
- α ≥ 0.800: Good reliability
- 0.667 ≤ α < 0.800: Acceptable for exploratory work; acknowledge the limitation
- α < 0.667: Unacceptable; revise codebook and retrain

**Why prefer α over κ?**
- Handles any number of coders (not just 2)
- Works with nominal, ordinal, interval, and ratio data
- Handles missing data gracefully (not all coders need to code all units)
- More conservative than κ (less likely to overestimate agreement)

---

## Choosing the Right Metric

| Situation | Recommended metric |
|-----------|-------------------|
| 2 coders, nominal categories, no missing data | Cohen's κ (report PA alongside) |
| 3+ coders, nominal categories, no missing data | Fleiss' κ or Krippendorff's α |
| Any number of coders, any data level, missing data possible | Krippendorff's α |
| Quick preliminary check | Percentage agreement (but always follow up with chance-corrected metric) |

**General recommendation:** Use Krippendorff's α as the default. It is the most versatile and is increasingly expected by reviewers.

---

## Python Implementation

When computing ICR in Python, use the `krippendorff` and `sklearn` packages:

```python
# Install if needed:
# pip install krippendorff scikit-learn

import numpy as np

# --- Krippendorff's Alpha ---
import krippendorff

# Data format: each row is a coder, each column is a unit
# Use np.nan for missing values
reliability_data = np.array([
    [1, 2, 3, 1, 2, 3, 1, 2],  # Coder 1
    [1, 2, 3, 1, 2, 2, 1, 2],  # Coder 2
    [1, 2, 3, 1, 2, 3, 1, np.nan],  # Coder 3 (missing one unit)
])

alpha = krippendorff.alpha(
    reliability_data=reliability_data,
    level_of_measurement='nominal'  # or 'ordinal', 'interval', 'ratio'
)
print(f"Krippendorff's alpha: {alpha:.3f}")

# --- Cohen's Kappa (2 coders only) ---
from sklearn.metrics import cohen_kappa_score

coder1 = [1, 2, 3, 1, 2, 3, 1, 2]
coder2 = [1, 2, 3, 1, 2, 2, 1, 2]

kappa = cohen_kappa_score(coder1, coder2)
print(f"Cohen's kappa: {kappa:.3f}")

# --- Percentage Agreement ---
agreements = sum(1 for a, b in zip(coder1, coder2) if a == b)
pa = agreements / len(coder1)
print(f"Percentage agreement: {pa:.1%}")
```

### Reporting Template

When reporting ICR in a paper, include:

> "Inter-coder reliability was assessed on a random subsample of [N] units ([X]% of the corpus), coded independently by [number] coders. Agreement was measured using Krippendorff's alpha (α = [value]), indicating [interpretation] reliability. [If marginal: The codebook was revised and coders retrained until acceptable reliability was achieved.]"
