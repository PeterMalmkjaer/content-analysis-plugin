# Benchmark, set 3 (GoEmotions): 5.0.0-beta.3 vs 5.0.0-beta.4

**Run date:** 12 November 2026 · **Protocol:** `protocol/protocol.md`, pre-registered 10 September 2026 (sha256 `f27178a0…`), with the deviations in `protocol/deviations.md` · **Status:** set 3 only. Sets 1 (TU Delft interviews) and 2 (AC-ICT) have **not** been run under this protocol.

> **Follow-up.** The calibrated result below was tested again on 500 fresh comments under the 5.0.0-beta.5 text: see `2026-11-goemotions-beta5-fresh-test.md`. A plain summary of both is in `README.md`.

## Result in brief

- **beta.4 with Step 5b calibration (arm C) agrees better with the human reference than beta.3 (arm A):** micro-F1 51.4 and 51.0 against 46.2 and 47.4. The paired-bootstrap interval for the difference excludes zero in both runs, which is the improvement criterion fixed in the protocol.
- **beta.4 without calibration (arm B) agrees worse than beta.3:** 44.2 and 43.7. The difference is negative in both runs; its interval excludes zero in one of the two.
- **The gain is therefore attributable to calibrating against human coding, not to the beta.4 coding procedure as such.** Whether calibration would help as much under beta.3's simpler procedure was not tested.
- **The gain sits in the frequent codes.** Macro-F1 is unchanged at about 40 in every arm, and one code (`disapproval`) got worse.

## Design

| | |
|---|---|
| Corpus | GoEmotions official test split, 5,427 Reddit comments, 27 emotions + neutral (Demszky et al., 2020; Apache 2.0) |
| Reference | Labels chosen by at least two of three (or five) human raters, as released |
| Splits (seed 20260910, fixed in September) | test 500 · calibration 400 · retest 200, uniform random, disjoint |
| Arm A | beta.3, original 28-line codebook |
| Arm B | beta.4, same codebook plus Step 4 decision-rule columns drafted by a subagent from the definitions and the 400 calibration **texts only** (no labels) |
| Arm C | Arm B's codebook after one Step 5b round: calibration split coded blind, disagreement review by code pair, decision-rule entries revised, each revision tested on the retest split and kept or reverted per code by a rule fixed in advance (`deviations.md`, D6) |
| Coding model | `claude-opus-5-5` in every arm; calibration review on `claude-fable-5-2` |
| Isolation | One subagent per batch of 50 comments; inputs: the arm's `SKILL.md`, source declaration, codebook, the batch. Every subagent's tool calls were audited afterwards: no file outside its prompt was opened |
| Runs | Two independent runs per arm on the test split: the same ten batches of 50 comments, coded again by fresh subagents in a different batch order (corrected 12 Nov 2026 — an earlier version of this table said "different batch composition") |
| Co-coding rule | Fixed for all arms: `neutral` alone. The reference combines neutral with an emotion on 8 of the 500 test comments, which no arm can match |

## Table 1 · Agreement with the human reference, test split (n = 500 comments, 579 reference labels)

| Arm / run | Assignments | Precision | Recall | Micro-F1 | Micro-F1 excl. neutral | Macro-F1 (27 codes) | Exact label set | Review share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A · beta.3 · run 1 | 567 | 46.7 | 45.8 | **46.2** | 42.7 | 41.2 | 38.2 % | – |
| A · beta.3 · run 2 | 560 | 48.2 | 46.6 | **47.4** | 43.8 | 39.6 | 39.4 % | – |
| B · beta.4 uncalibrated · run 1 | 638 | 42.2 | 46.5 | **44.2** | 41.3 | 37.9 | 32.8 % | 26.5 % |
| B · beta.4 uncalibrated · run 2 | 630 | 41.9 | 45.6 | **43.7** | 40.9 | 40.6 | 33.4 % | 23.8 % |
| C · beta.4 calibrated · run 1 | 564 | 52.1 | 50.8 | **51.4** | 46.5 | 40.0 | 44.0 % | 24.3 % |
| C · beta.4 calibrated · run 2 | 575 | 51.1 | 50.8 | **51.0** | 46.4 | 39.9 | 43.2 % | 23.0 % |

All six outputs: validator `RESULT: PASS` (the arm's own validator version). For set 3 the excerpt is the whole comment, attached mechanically, so the validator's excerpt check is vacuous here. Every figure in Table 1 was recomputed from the raw batch files by a second script and matches.

Restricted to the 17 codes with at least ten human positives in the calibration split (the other eleven are *insufficiently calibrated* — caring, desire, embarrassment, fear, grief, nervousness, optimism, pride, relief, remorse, sadness): micro-F1 A 46.4 / 47.8, B 44.7 / 43.6, C 52.5 / 51.9; macro-F1 A 40.2 / 41.6, B 39.7 / 39.1, C 41.8 / 42.1.

## Table 2 · Paired bootstrap of the micro-F1 difference (2,000 resamples of the 500 test comments, seed 20260910)

| Comparison | Run 1 | Run 2 | Criterion met? |
|---|---|---|---|
| C − A | +5.2 [+2.2, +8.2] | +3.5 [+0.7, +6.6] | Yes: both intervals exclude zero, same direction |
| B − A | −2.0 [−4.3, +0.2] | −3.7 [−6.2, −1.3] | No improvement. Negative in both runs; one interval includes zero |
| C − B | +7.2 [+4.2, +10.5] | +7.3 [+4.3, +10.5] | Yes |

Cross-run pairings (C1−A2, C2−A1 and so on) give the same signs and intervals that exclude zero for all three comparisons. The intervals cover sampling of comments only, not model or prompt variance.

## Table 3 · Run-to-run stability (run 1 against run 2, same arm)

| Arm | F1 between runs | Identical label set | Mean per-code κ |
|---|---:|---:|---:|
| A | 89.4 | 85.2 % | 0.847 |
| B | 90.2 | 82.6 % | 0.854 |
| C | 91.7 | 88.4 % | 0.903 |

This is stability of AI coding, not reliability. Arm B is as stable as arm A while agreeing less with the reference: the case Step 5b warns about.

## Table 4 · Selected codes, test split (mean of two runs)

| Code | Human positives | AI positives A / B / C | F1 A / B / C |
|---|---:|---|---|
| neutral | 178 | 143.5 / 114.5 / 179.0 | 56 / 53 / 62 |
| disapproval | 25 | 83.0 / 122.5 / 28.5 | 27 / 22 / **15** |
| amusement | 30 | 33.5 / 42.5 / 30.0 | 58 / 57 / 75 |
| curiosity | 29 | 26.0 / 28.5 / 36.5 | 40 / 43 / 52 |
| admiration | 37 | 27.5 / 28.5 / 39.5 | 46 / 53 / 56 |
| approval | 42 | 26.0 / 32.5 / 29.0 | 31 / 35 / 35 |
| annoyance | 30 | 35.5 / 38.0 / 40.0 | 31 / 30 / 29 |
| surprise | 13 | 15.0 / 25.5 / 13.5 | 39 / 42 / 26 |
| confusion | 9 | 11.0 / 9.0 / 5.5 | 45 / 39 / 14 |
| gratitude | 34 | 26.0 / 25.5 / 26.0 | 82 / 82 / 82 |

The full per-code table is in `results_set3.json`.

## The calibration round (Step 5b)

Calibration split under arm B's rules: micro-F1 38.0; 296 of 400 comments differed from the reference. The largest disagreement groups were `disapproval` where the reference has `neutral` (35), `disapproval` for `anger` (10) and `amusement` for `neutral` (10). The reviewer revised the decision-rule entries of 15 codes and left 22 examined pairs unrevised, with reasons (`set3_calibration_revision_log.md`). Nothing outside the per-category entries was changed; this was checked mechanically.

Retest split (200 fresh comments): micro-F1 42.7 under the unrevised rules, 49.2 under the candidate. By the rule fixed in advance, 12 revisions were kept (amusement, anger, approval, caring, curiosity, disapproval, disgust, joy, love, optimism, surprise, neutral) and 3 reverted (admiration, annoyance, desire). `love` and `surprise` had fewer than five reference positives in the retest split and were kept on the overall result; for `love` the code's own F1 fell (44 → 36). The frozen mix was not re-tested before the test split, because no fresh comments remained.

No comment from the test or retest split appears in the reviewer's input or in the frozen codebook (checked by unit ID and by verbatim text).

## Pre-registered expectations

| | Expectation | Outcome |
|---|---|---|
| P1 | `disapproval` AI/human ratio closer to 1 in B and C than in A | A 3.3 · B 4.9 · C 1.1. **Holds for C, fails for B.** In C the count is right but the code lands on the wrong comments (F1 15) |
| P4 | Micro-F1: C ≥ B ≥ A | **C > A > B.** The protocol named B < A as a possible outcome |
| P5 | Review share between 5 % and 30 % | B 26.5 / 23.8 %, C 24.3 / 23.0 %: within range. On the retest split the candidate reached 32.1 % |
| P6 | Stability in B and C not lower than in A | Holds (Table 3) |

P2 and P3 concern sets 1 and 2 and are untested.

## Observations beyond the protocol (exploratory)

- **The `Review` flag carries information.** In arm C, comments with at least one flagged assignment (26–27 % of comments) have micro-F1 35–36; unflagged comments 57–58. In arm B: 31–34 against 49–50. The flag points a human reviewer at the cases where the coding is in fact weaker.
- **Where arm B lost ground.** Its drafted rule for `disapproval` read "a negative judgement … or disagrees with someone", which is wider than the codebook's definition; together with Step 7's sweep for omitted codes this raised `disapproval` from 83 to 122 assignments and lowered `neutral` from 143 to 115. A decision rule written from the definition alone can widen a code.

## Reference points (not baselines)

- Codex run of beta.3 on the full test split, 9 September 2026, GPT-6-family model: micro-F1 43.6.
- Arm A on `claude-fable-5-1`, September, run 1 on the same 500 comments: 43.0. Raw outputs lost (`deviations.md`, D2).
- Demszky et al. (2020), Table 4: a BERT model fine-tuned on the training split reaches macro-F1 .46 (precision .40, recall .63) on the full test split. The arms here use no training data and reach macro-F1 of about .40 on a 500-comment sample.
- Human–human agreement in the paper is per emotion and low for the codes that are weak here: Cohen's κ in its Appendix C is 0.234 for disapproval, 0.192 for annoyance, 0.187 for approval, 0.184 for disappointment, 0.155 for realization, against 0.749 for gratitude and 0.468 for admiration. The values were checked against Table 7 in the paper's PDF on 12 November 2026 (an earlier version of this report had them from a secondary summary). They are computed between two randomly sampled ratings per comment, whereas the reference used here is the aggregate of several raters, so they indicate where the ceiling is low rather than give a number to compare against.

## What this does and does not show

1. One corpus, one model, one calibration round, 500 test comments. The result is indicative.
2. Calibration, retest and test comments come from the same corpus and split. The gain is an in-distribution gain: the calibrated rules encode this reference's conventions, such as treating argument and correction as neutral.
3. Arm C differs from arm A in three things at once: the beta.4 procedure, the decision-rule columns, and the calibration. Arm B shows that the first two without the third do not help here. An arm "beta.3 procedure + calibrated codebook" would be needed to say whether the beta.4 procedure contributes anything beyond carrying the calibrated rules.
4. The arm-C codebook is about 39,000 characters against 2,600 for arm A. Length alone does not explain the gain, since arm B's codebook is about 30,000 characters and did worse; but the calibrated entries contain worked examples from the calibration comments, and part of the gain may come from those examples as such.
5. Macro-F1 did not improve, and `disapproval`, `confusion` and `surprise` got worse. A user who cares about rare or contested codes gains nothing from this calibration as measured.
6. GoEmotions is public and may be in the model's training data. That applies to every arm equally.
7. The reference is not ground truth; on the weakest codes the human raters themselves agree little.

## Cost

81 subagent calls. About 25 million tokens passed through the coding model, 80 % of them as cache reads of the same context and 19 % as cache writes; output was 1.3 %. At list prices (Opus 5.5 $4 / $20, Fable 5.2 $8 / $40 per million tokens, checked 12 November 2026) and assuming the usual cache multipliers (write 1.25×, read 0.1× — assumed, not checked): about $38 for coding and $6 for the review. The orchestrating session is not included.

## Files

All paths are relative to `docs/benchmarks/`.

- `protocol/` — `protocol.md` and `splits.json` as frozen in September (hashes in `protocol.sha256`), `deviations.md`.
- `materials/` — source declaration; codebooks for arm A (`set3_codebook_A.md`), arm B (`set3_codebook_B.md`) and arm C as frozen (`set3_codebook_C.md`); the drafter's and the reviewer's prompts; the reviewer's revision log and the keep/revert decisions; one example coding prompt per arm.
- `results/` — `results_set3.json` (all figures, per code), `results_set3_kappa.json`, `usage_set3.json`; `units.csv` and `assignments.csv`, from which `scripts/recompute.py` reproduces Table 1 without any other input.
- `scripts/` — the scripts as they were run (`build.py`, `assemble.py`, `score.py`, `stability.py`, `audit.py`, `analyse_set3.py`). They carry the study workspace's paths and are documentation, not a runnable package; `recompute.py` is runnable as it stands.

Not in the repository: the comment texts (public in the GoEmotions release; `units.csv` gives each comment's GoEmotions id), the 120 raw batch files and the subagent transcripts. They are archived by the author.

## Reference

Demszky, D., Movshovitz-Attias, D., Ko, J., Cowen, A., Nemade, G., & Ravi, S. (2020). GoEmotions: A dataset of fine-grained emotions. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (pp. 4040–4054). Association for Computational Linguistics. https://doi.org/10.18653/v1/2020.acl-main.372
