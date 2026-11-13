# Test of the 5.0.0-beta.6 candidate on a second fresh sample (GoEmotions)

**Run date:** 13 November 2026 · **Protocol:** `protocol/protocol_addendum2.md`, pre-registered and frozen by SHA-256 (`413c633c…`) before any of these comments was coded; deviations in `protocol/addendum2_deviations.md` · **Tested text:** `skills/content-analysis/SKILL.md` at commit `d510a60` (sha256 `e0cfbd52…`), which is the text released as 5.0.0-beta.6.

## Why this test exists

The first fresh-sample test (`2026-11-goemotions-beta5-fresh-test.md`) left two questions. Without calibration, beta.5 scored a point and a half below beta.3, and an exploratory look placed the loss where beta.5 assigned a flagged emotion to comments the human raters had coded `neutral`. And it had never been tested whether the eight-step decision procedure adds anything once the codebook is calibrated.

beta.6 changes one rule: where a codebook defines a residual category by a threshold (GoEmotions: *neutral — no sufficiently clear emotion expressed*), a unit that does not clearly meet a substantive code's definition meets the residual category's definition and is coded there. A second text, a variant with a four-step procedure for calibrated codebooks, was written for the test only. Both were tested once, on 500 comments nothing in the study had touched.

## Result in brief

- **Without calibration, beta.6 scores about a point and a half above beta.5 in both runs, and the intervals include zero.** By the rule fixed in advance this is *direction only*, not a demonstrated improvement.
- **Without calibration, beta.6 is not distinguishable from beta.3** (43.5 and 44.7 against 44.3 and 45.3); both estimates remain slightly negative.
- **beta.5 without calibration is below beta.3 on this sample**: −2.2 [−4.2, −0.3] and −2.1 [−4.0, −0.2], both intervals excluding zero. In the first fresh sample the same comparison gave −1.5 and −1.8 with intervals that included zero. Taken together, beta.5's uncalibrated procedure was about two points below beta.3.
- **The calibrated path holds for the third time**: 49.4 and 49.5 against 44.3 and 45.3 for beta.3, intervals excluding zero.
- **The eight-step procedure: no demonstrated difference against a four-step one** on short comments. The estimate favours the eight steps in both runs (+2.0 and +0.4); one interval excludes zero, one does not. Most of the calibrated gain arrives with the calibrated codebook under either procedure.
- The release rule was met, and the text was released unchanged.

## Design

| | |
|---|---|
| Sample | 500 comments drawn uniformly at random (seed 20261113) from the 3,827 comments of the official GoEmotions test split not used in the benchmark or the first fresh sample; 577 reference labels |
| Arm A | 5.0.0-beta.3, original codebook |
| Arm E | 5.0.0-beta.5 as released, original codebook, status *uncalibrated* |
| Arm H | beta.6 text, original codebook, status *uncalibrated* |
| Arm J | beta.6 text, calibrated codebook frozen in the benchmark, status *calibrated* |
| Arm G | Variant text (four-step procedure for calibrated codebooks; **not released**), the same calibrated codebook, status *calibrated* |
| Coding model | `claude-opus-5-5` in every arm (read from the harness transcripts) |
| Isolation | One subagent per batch of 50 comments; 101 subagents; every tool call audited: no file outside the prompt was opened |
| Runs | Two per arm; run 2 with different batches; within a run all arms code identical batches |
| Prompt | Arm A's prompt as before. For the arms with a `Review` column, the one sentence that repeated the skill's uncertainty rule in the prompt was removed, because that rule is what is under test. Arm E therefore ran with a prompt one sentence shorter than in the first fresh-sample test |
| One shot | Neither text was to be edited in response to the results, and neither was |

## Table 1 · Agreement with the human reference (n = 500 comments, 577 reference labels)

| Arm / run | Assignments | Precision | Recall | Micro-F1 | Micro-F1 excl. neutral | Macro-F1 (27 codes) | Exact label set | Review share |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A · beta.3 · run 1 | 566 | 44.7 | 43.8 | **44.3** | 41.1 | 40.9 | 34.4 % | – |
| A · beta.3 · run 2 | 566 | 45.8 | 44.9 | **45.3** | 43.1 | 44.1 | 34.8 % | – |
| E · beta.5 uncalibrated · run 1 | 579 | 42.0 | 42.1 | **42.0** | 40.2 | 40.9 | 31.0 % | 22.3 % |
| E · beta.5 uncalibrated · run 2 | 589 | 42.8 | 43.7 | **43.2** | 41.6 | 40.8 | 31.4 % | 21.9 % |
| H · beta.6 uncalibrated · run 1 | 576 | 43.6 | 43.5 | **43.5** | 40.1 | 39.2 | 33.0 % | 24.0 % |
| H · beta.6 uncalibrated · run 2 | 578 | 44.6 | 44.7 | **44.7** | 41.9 | 42.3 | 34.8 % | 22.8 % |
| J · beta.6 calibrated · run 1 | 588 | 49.0 | 49.9 | **49.4** | 45.2 | 41.0 | 39.0 % | 29.8 % |
| J · beta.6 calibrated · run 2 | 587 | 49.1 | 49.9 | **49.5** | 45.0 | 39.5 | 38.8 % | 28.4 % |
| G · variant, calibrated · run 1 | 577 | 47.5 | 47.5 | **47.5** | 43.4 | 36.5 | 37.6 % | 31.9 % |
| G · variant, calibrated · run 2 | 577 | 49.0 | 49.0 | **49.0** | 45.2 | 40.2 | 39.2 % | 31.9 % |

All ten outputs: validator `RESULT: PASS`. One comment omitted by one batch (arm A, run 1) was coded by a fresh blind subagent, as the protocol prescribes. Every figure was recomputed from the raw batch files by a second script (`scripts/analyse_fresh2.py`) and by a third that reads only the published result files (`scripts/recompute.py`); all three agree. `grief` does not occur in the reference for this sample. None of the 500 comments appears in the calibrated codebook or in the inputs of the rule drafter and the calibration reviewer.

## Table 2 · Pre-registered hypotheses (paired bootstrap, 2,000 resamples, seed 20261113, 95 % interval)

| Hypothesis | Run 1 | Run 2 | Outcome |
|---|---|---|---|
| **H-1** · H − E positive (the change helps without calibration) | +1.5 [−0.5, +3.4] | +1.5 [−0.2, +3.1] | **Holds as direction only.** Both intervals include zero, so it is not called an improvement |
| **H-2** · H − A positive or interval includes zero (not below beta.3) | −0.7 [−2.5, +1.1] | −0.6 [−2.5, +1.2] | **Holds**; both estimates slightly negative |
| **H-3** · J − A positive, interval excludes zero (calibrated path intact) | +5.2 [+2.2, +8.1] | +4.2 [+1.1, +7.2] | **Holds** |
| **H-4** · flagged comments agree less than unflagged | H: 27.9 vs 49.1 · J: 39.3 vs 55.1 | H: 29.0 vs 49.9 · J: 37.8 vs 55.4 | **Holds** |
| **H-5** · H's `neutral` count closer to the reference (158) than E's | H 113, E 87 | H 114, E 85 | **Holds** |

**Release rule** (H-2 and H-3 hold, and H − E positive in both runs): **met.**

For reference, E − A: −2.2 [−4.2, −0.3] and −2.1 [−4.0, −0.2]. J − H: +5.9 [+3.0, +8.8] and +4.8 [+1.8, +7.8].

## Table 3 · Does the eight-step procedure contribute? (arm J against arm G, same calibrated codebook)

| | Run 1 | Run 2 | Reading fixed in advance |
|---|---|---|---|
| J − G (eight steps − four steps) | +2.0 [+0.3, +3.6] | +0.4 [−1.0, +1.9] | **No demonstrated difference**: the interval excludes zero in one run only |
| G − A (four steps, calibrated codebook, against beta.3) | +3.2 [+0.3, +6.4] | +3.7 [+0.8, +6.7] | — |

So a calibrated codebook under the short procedure already scores three to four points above beta.3; the eight steps add between nothing measurable and two points. The variant used more flags (31.9 % of assignments against 29.8 % and 28.4 %) and was not cheaper (Table 4). As fixed in advance, the variant is not released: the code-by-code sweep was introduced for low recall on long elicited units, which short comments cannot test.

## Table 4 · Reported without a decision rule

| | A · beta.3 | E · beta.5 uncal. | H · beta.6 uncal. | J · beta.6 cal. | G · variant |
|---|---:|---:|---:|---:|---:|
| Run-to-run F1 | 85.0 | 87.5 | 87.9 | 90.2 | 90.3 |
| Identical label set between runs | 80.0 % | 82.0 % | 83.2 % | 86.4 % | 87.2 % |
| `neutral` assigned (reference: 158) | 105 / 98 | 87 / 85 | 113 / 114 | 161 / 170 | 162 / 159 |
| `disapproval` assigned (reference: 17) | 71 / 70 | 82 / 86 | 69 / 75 | 31 / 29 | 29 / 25 |
| Comments with a flag | – | 26 % / 26 % | 27 % / 26 % | 34 % / 33 % | 37 % / 36 % |
| Seconds per batch of 50 (median) | 25 | 31 | 34 | 48 | 45 |
| List price for 1,000 comment codings | $7.59 | $8.48 | $8.62 | $10.82 | $10.74 |

Cost is driven mostly by loading the skill text and the codebook into each batch's context, not by the number of procedure steps: the calibrated arms cost more because their codebook is fifteen times longer and their coders write more.

## Table 5 · Selected codes (mean of two runs)

| Code | Human positives | AI positives A / E / H / J / G | F1 A / E / H / J / G |
|---|---:|---|---|
| neutral | 158 | 101.5 / 86.0 / 113.5 / 165.5 / 160.5 | 54 / 49 / 54 / 61 / 59 |
| admiration | 52 | 46.5 / 46.0 / 42.5 / 51.5 / 51.0 | 62 / 62 / 59 / 65 / 63 |
| approval | 39 | 34.0 / 38.0 / 36.5 / 33.0 / 33.5 | 36 / 31 / 36 / 31 / 30 |
| annoyance | 33 | 41.0 / 41.0 / 37.5 / 30.5 / 32.0 | 27 / 27 / 28 / 22 / 23 |
| curiosity | 27 | 24.5 / 26.5 / 25.5 / 36.0 / 37.5 | 54 / 50 / 51 / 59 / 59 |
| love | 23 | 19.0 / 18.5 / 19.5 / 22.0 / 21.0 | 67 / 65 / 68 / 71 / 70 |
| amusement | 22 | 35.0 / 42.5 / 34.5 / 23.5 / 23.0 | 42 / 47 / 46 / 66 / 64 |
| sadness | 21 | 18.5 / 16.5 / 17.0 / 8.5 / 11.0 | 41 / 40 / 37 / 41 / 41 |
| optimism | 20 | 14.5 / 14.0 / 14.5 / 16.5 / 16.5 | 52 / 50 / 49 / 55 / 55 |
| anger | 19 | 9.5 / 8.5 / 7.5 / 19.0 / 19.0 | 28 / 22 / 26 / 29 / 26 |
| disapproval | 17 | 70.5 / 84.0 / 72.0 / 30.0 / 27.0 | 19 / 19 / 13 / 21 / 18 |
| gratitude | 30 | 22.5 / 23.0 / 22.0 / 23.0 / 22.5 | 82 / 83 / 81 / 83 / 82 |

Full table: `results/results_set3_fresh2.json`. As before, a code with twenty human positives moves several points between samples; `sadness` and `annoyance` were not helped by calibration here.

## Observations beyond the pre-registered tests (exploratory)

1. **Where beta.6 recovers ground.** Split by each arm's own flag and scored on the same comments: on beta.5's flagged comments beta.5 scores 27.7 and 34.5 where beta.3 scores 34.1 and 39.6; on beta.6's flagged comments beta.6 scores 27.9 and 29.0 where beta.3 scores 28.5 and 31.0. On unflagged comments both are within about a point of beta.3. The pattern that motivated the change is largely gone.
2. **`neutral`.** beta.6 without calibration assigns it more often than beta.3 (113 and 114 against 105 and 98) at slightly lower precision (65 % against 69 %); all uncalibrated arms remain far below the reference count of 158, which only the calibrated codebook reaches.
3. **The removed prompt sentence did not carry the effect.** With the sentence gone, beta.5's shortfall against beta.3 is no smaller than in the first fresh sample (about two points here, a point and a half there). The comparison is across samples and only indicative, but it points at the skill text, not the prompt, as the source.
4. **Macro-F1.** J − A is +0.1 [−1.9, +4.5] and −4.5 [−6.9, +1.6]. The gain in rarer codes seen in the first fresh sample does not appear here or in the benchmark. Two samples of three show none.

## What this does and does not show

1. Three disjoint samples of 500 comments now show the calibrated path 3.5 to 7.2 points of micro-F1 above beta.3, with an interval excluding zero in all six runs. All three come from the corpus the codebook was calibrated on.
2. Without calibration, beta.6 is at beta.3's level within sampling error and above beta.5 in direction. It has not been shown to be better than beta.3 on agreement. What it adds over beta.3 is the `Review` flag.
3. The residual-threshold rule was tested on one codebook with one residual category. Codebooks without such a category are unaffected by it; codebooks whose residual category is defined differently are untested.
4. The eight-step procedure's contribution on short comments is small and not established. Whether it matters on interviews, where it was meant to, is untested.
5. One corpus, one coding model, one calibration round. Interviews, documents, ChatGPT and Codex remain untested.

## Cost

101 subagent calls on `claude-opus-5-5`: 31.9 million tokens, 81 % cache reads, 18 % cache writes, 1.2 % output. At list price ($4 / $20 per million tokens) and assumed cache multipliers of 1.25× for writes and 0.1× for reads: about $47. The orchestrating session is not included.

## Files

All paths are relative to `docs/benchmarks/`.

- `protocol/` — `protocol_addendum2.md` and `splits_addendum2.json` as frozen (hashes in `protocol_addendum2.sha256`), `addendum2_deviations.md`.
- `materials/` — codebooks (arms A, E, H use `set3_codebook_A.md`; arms J and G use `set3_codebook_C.md`); `example_prompt_round3_arm_H.md` and `example_prompt_round3_arm_J.md`; `variant_T2_step7.diff`, the difference between the released text and the variant used by arm G.
- `results/` — `results_set3_fresh2.json`, `results_set3_fresh2_exploratory.json`, `usage_set3_fresh2.json`, and the shared `units.csv` and `assignments.csv` (sample `fresh2`).
- `scripts/` — `analyse_fresh2.py`, `explore_fresh2.py` (as run) and `recompute.py` (runnable as it stands).

## Reference

Demszky, D., Movshovitz-Attias, D., Ko, J., Cowen, A., Nemade, G., & Ravi, S. (2020). GoEmotions: A dataset of fine-grained emotions. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (pp. 4040–4054). Association for Computational Linguistics. https://doi.org/10.18653/v1/2020.acl-main.372
