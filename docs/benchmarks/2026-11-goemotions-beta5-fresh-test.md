# Test of 5.0.0-beta.5 on fresh comments (GoEmotions)

**Run date:** 12 November 2026 · **Protocol:** `protocol/protocol_addendum.md`, pre-registered and frozen by SHA-256 (`85bb1574…`) before any of these comments was coded; deviations in `protocol/addendum_deviations.md` · **Tested text:** `skills/content-analysis/SKILL.md` at commit `08c38e5` (sha256 `de3eaf58…`), which is the text released as 5.0.0-beta.5.

## Why this test exists

The first benchmark (`2026-11-goemotions-beta3-vs-beta4.md`) showed that beta.4 agreed better with human coding than beta.3 when its codebook had been calibrated against human coding, and worse when it had not. beta.5 answers with two coding procedures: the full decision procedure for a calibrated codebook, a simple one for an uncalibrated codebook. That text was written after the first results were known, so the first 500 comments could not test it. This test uses 500 comments that no part of the study had touched.

## Result in brief

- **Calibrated path (arm F): the advantage replicates.** Micro-F1 50.8 and 51.2 against 44.0 and 44.0 for beta.3. The interval for the difference excludes zero in both runs (pre-registered criterion H-F: holds).
- **Uncalibrated path (arm E): not distinguishable from beta.3, with a point estimate slightly below it.** Micro-F1 42.5 and 42.2 against 44.0 and 44.0. Both intervals include zero (pre-registered criterion H-E: holds), but both point estimates are negative (−1.5 and −1.8). beta.5 without calibration is no improvement over beta.3 on agreement.
- **The `Review` flag marks the weaker coding (H-R: holds).** Flagged comments agree with the reference far less than unflagged ones in every run of both arms.

## Design

| | |
|---|---|
| Sample | 500 comments drawn uniformly at random (seed 20261112) from the 4,327 comments of the official GoEmotions test split that were in none of the benchmark's splits; 597 reference labels |
| Arm A | 5.0.0-beta.3, original 28-line codebook |
| Arm E | beta.5 text, the same original codebook, coder told the codebook is **uncalibrated** |
| Arm F | beta.5 text, the calibrated codebook frozen in the first benchmark (arm C there), coder told the codebook is **calibrated** |
| Not done | No new calibration. Arm F's codebook was calibrated under beta.4's flow, which beta.5 describes unchanged. The test concerns beta.5's two *coding* procedures |
| Coding model | `claude-opus-5-5` in every arm (read from the harness transcripts, not self-reported) |
| Isolation | One subagent per batch of 50 comments; 60 subagents; every tool call audited afterwards: no file outside the prompt was opened |
| Runs | Two per arm. Run 2 uses different batches (comments reshuffled before batching); within a run all three arms code identical batches |
| Prompt | Arm A's prompt is identical to the benchmark's apart from file paths. Arms E and F are told only that Step 7 has two procedures and what the codebook's status is; the skill text has to carry the rest |
| One shot | The skill text was not to be edited in response to these results, and was not |

## Table 1 · Agreement with the human reference (n = 500 fresh comments, 597 reference labels)

| Arm / run | Assignments | Precision | Recall | Micro-F1 | Micro-F1 excl. neutral | Macro-F1 (26 codes) | Exact label set | Review share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A · beta.3 · run 1 | 594 | 44.1 | 43.9 | **44.0** | 43.5 | 42.1 | 33.8 % | – |
| A · beta.3 · run 2 | 581 | 44.6 | 43.4 | **44.0** | 43.5 | 42.0 | 34.4 % | – |
| E · beta.5 uncalibrated · run 1 | 616 | 41.9 | 43.2 | **42.5** | 43.2 | 42.0 | 31.6 % | 19.8 % |
| E · beta.5 uncalibrated · run 2 | 603 | 42.0 | 42.4 | **42.2** | 42.9 | 42.1 | 31.0 % | 22.1 % |
| F · beta.5 calibrated · run 1 | 591 | 51.1 | 50.6 | **50.8** | 49.9 | 46.1 | 42.4 % | 29.1 % |
| F · beta.5 calibrated · run 2 | 595 | 51.3 | 51.1 | **51.2** | 49.0 | 46.0 | 42.2 % | 26.6 % |

All six outputs: validator `RESULT: PASS`, no omitted comments, no invalid codes. Every figure was recomputed from the raw batch files by a second script (`scripts/analyse_fresh.py`) and by a third that reads only the two published result files (`scripts/recompute.py`); all three agree. Macro-F1 covers the 26 codes that occur in the reference for this sample (`grief` and `relief` do not). None of the 500 comments appears in the calibrated codebook or in the inputs of the rule drafter and the calibration reviewer (checked by comment id and by verbatim text).

## Table 2 · Pre-registered tests (paired bootstrap, 2,000 resamples of the 500 comments, seed 20261112, 95 % interval)

| Hypothesis | Run 1 | Run 2 | Outcome |
|---|---|---|---|
| **H-E** · E − A is positive or its interval includes zero | −1.5 [−3.5, +0.7] | −1.8 [−4.0, +0.2] | **Holds**, narrowly: both intervals include zero, both estimates are negative |
| **H-F** · F − A is positive and its interval excludes zero | +6.8 [+3.9, +9.7] | +7.2 [+4.1, +10.5] | **Holds** |
| **H-R** · flagged comments agree less than unflagged | E: 29.4 vs 46.2 · F: 39.0 vs 57.4 | E: 26.5 vs 47.6 · F: 37.8 vs 57.5 | **Holds** in all four |

F − E: +8.3 [+5.0, +11.5] and +9.0 [+6.0, +12.2]. Cross-run pairings give the same signs and the same verdicts. The intervals cover sampling of comments only, not model or prompt variance.

## Table 3 · Reported without a decision rule

| | A · beta.3 | E · beta.5 uncalibrated | F · beta.5 calibrated |
|---|---:|---:|---:|
| Run-to-run F1 | 85.8 | 86.3 | 89.7 |
| Identical label set between runs | 80.2 % | 78.6 % | 85.2 % |
| `neutral` assigned (reference: 147) | 96 / 93 | 80 / 74 | 147 / 147 |
| `disapproval` assigned (reference: 22) | 78 / 75 | 96 / 93 | 28 / 28 |
| Share of comments with a flag | – | 24 % / 27 % | 34 % / 31 % |

Arm A's level here (44.0) is lower than on the first 500 comments (46.2 and 47.4): two random samples of 500 from the same corpus differ by about three points, which is the scale against which the differences in Table 2 should be read. Run-to-run agreement is lower than in the first benchmark for every arm, as expected when run 2 uses different batches.

## Table 4 · Selected codes (mean of two runs)

| Code | Human positives | AI positives A / E / F | F1 A / E / F |
|---|---:|---|---|
| neutral | 147 | 94.5 / 77.0 / 147.0 | 46 / 39 / 56 |
| admiration | 64 | 50.0 / 52.5 / 61.0 | 55 / 56 / 62 |
| approval | 32 | 28.5 / 34.0 / 32.5 | 31 / 32 / 43 |
| curiosity | 26 | 18.0 / 18.0 / 36.0 | 41 / 41 / 52 |
| amusement | 23 | 38.5 / 44.0 / 23.5 | 52 / 52 / 82 |
| annoyance | 23 | 37.0 / 37.0 / 38.5 | 27 / 25 / 26 |
| disapproval | 22 | 76.5 / 94.5 / 28.0 | 22 / 21 / 26 |
| anger | 21 | 11.5 / 11.5 / 14.5 | 55 / 52 / 45 |
| optimism | 19 | 10.0 / 11.5 / 15.5 | 34 / 36 / 55 |
| caring | 18 | 21.0 / 22.5 / 12.5 | 44 / 47 / 29 |
| gratitude | 28 | 24.0 / 22.5 / 24.0 | 88 / 85 / 88 |

Full table: `results/results_set3_fresh.json`. A code with about twenty human positives moves several F1 points from sample to sample: `disapproval` fell under calibration in the first benchmark (27 → 15) and rose slightly here (22 → 26). Per-code figures at this sample size show direction at most.

## Observations beyond the pre-registered tests (exploratory)

These were looked at after the results were known. They explain; they do not confirm.

1. **Where the uncalibrated procedure loses its point and a half.** Split by arm E's own flag and scored on the same comments, E and A are equal on the unflagged comments (46.2 vs 46.1; 47.6 vs 47.8) and E is lower on the flagged ones (29.4 vs 36.6; 26.5 vs 33.0). On the flagged comments the human reference says `neutral` more often (38 % and 34 %) than on the unflagged (27 % and 28 %). Excluding `neutral`, E − A is −0.3 [−2.2, +1.8] and −0.6 [−2.6, +1.4]. The reading that fits: when unsure, beta.3 more often falls back on `neutral`, which this reference also does; beta.5 assigns an emotion and flags it, as its rule "uncertainty is not a code" prescribes. In a codebook whose residual category is *defined* as "no sufficiently clear emotion", that rule and the codebook pull in different directions.
2. **Macro-F1.** F − A is +3.9 [+1.4, +7.0] and +4.0 [+0.9, +7.7] here. In the first benchmark the calibrated arm's macro-F1 was no higher than beta.3's. One sample shows a gain in the rarer codes and one does not; it is not established.
3. **Flag kinds.** In arm F two thirds of the flags are `competing_codes` (114 and 93 of about 165); in arm E the flags are spread over `competing_codes`, `possible_irony` and `context_missing`. `other` was not used.
4. **Which procedure the coders followed** cannot be read from the transcripts: they hold tool calls and a one-line reply, not reasoning. The evidence that arm E did not sweep the codebook is indirect: 616 and 603 assignments, against 638 and 630 for uncalibrated beta.4 on the first sample and 594 and 581 for beta.3 here.

## What this does and does not show

1. The calibrated path's advantage of five to seven points of micro-F1 has now been seen on two disjoint samples of 500 comments, under two versions of the skill text. Both samples come from the same corpus as the calibration material: the advantage is in-distribution, and the calibrated rules encode this reference's conventions.
2. Without calibration, beta.5 gives about the same agreement as beta.3, possibly a little less on corpora with a large residual category. What it adds over beta.3 in that situation is the `Review` flag, which here separated comments at 27–29 from comments at 46–48.
3. One corpus of short comments, one coding model, one calibration round. Nothing here speaks to interviews or long documents, where low recall was the problem reported for beta.3 and where dropping the code-by-code sweep may cost something. That is untested.
4. Calibrating a codebook from scratch under the beta.5 text was not repeated. The Step 5b flow is the one tested in the first benchmark.
5. Arm F differs from arm A in procedure and in codebook at once. A "simple procedure + calibrated codebook" arm was not run, so the share of the gain owed to the stepwise procedure, as opposed to the calibrated rules, is unknown.
6. GoEmotions is public and may be in the model's training data; this applies to every arm equally. The reference is aggregated human judgement, not ground truth.

## Cost

60 subagent calls on `claude-opus-5-5`: 18.3 million tokens, of which 81 % cache reads, 18 % cache writes and 1.2 % output. At list price ($4 / $20 per million tokens, checked 12 November 2026) and assuming cache multipliers of 1.25× for writes and 0.1× for reads (assumed, not checked): about $27. The orchestrating session is not included.

## Files

All paths are relative to `docs/benchmarks/`.

- `protocol/` — `protocol_addendum.md` and `splits_addendum.json` as frozen (hashes in `protocol_addendum.sha256`), `addendum_deviations.md`.
- `materials/` — the codebooks (arm E uses `set3_codebook_A.md`, arm F uses `set3_codebook_C.md`), `example_prompt_arm_A.md`, `example_prompt_arm_E.md`, `example_prompt_arm_F.md`.
- `results/` — `results_set3_fresh.json`, `results_set3_fresh_exploratory.json`, `usage_set3_fresh.json`, and the shared `units.csv` and `assignments.csv`.
- `scripts/` — `analyse_fresh.py`, `explore_fresh.py` (as run) and `recompute.py` (runnable as it stands).

## Reference

Demszky, D., Movshovitz-Attias, D., Ko, J., Cowen, A., Nemade, G., & Ravi, S. (2020). GoEmotions: A dataset of fine-grained emotions. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (pp. 4040–4054). Association for Computational Linguistics. https://doi.org/10.18653/v1/2020.acl-main.372
