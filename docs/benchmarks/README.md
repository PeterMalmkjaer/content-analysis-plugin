# What the benchmarks show

This folder documents how well the skill's coding agrees with human coding, where that has been measured, and where it has not. It is written for someone deciding whether, and how, to use the skill.

**The short version.** If you can give the skill some material that humans have already coded, it calibrates the codebook against it, and its coding then agrees clearly better with human coding than without. If you cannot, the skill codes at about the level of the earlier version 5.0.0-beta.3 and marks the decisions it found hard, and those marks are worth reading. All of this has been measured on one corpus with one AI model.

## Table 1 · What you get (5.0.0-beta.6)

| Your situation | What the skill does | What was measured |
|---|---|---|
| **You have human-coded material** from the same kind of text (Step 5b) | Drafts decision rules for each code, tests them against the human coding, keeps a revision only where it improves agreement on fresh items, then codes with the full decision procedure | Agreement score **49–51** against **44–47** for 5.0.0-beta.3, on three separate samples of 500 comments. The difference is larger than sampling error in all six runs |
| **You have no human-coded material** | Codes from the code definitions with a simple procedure; writes no decision rules of its own; labels every quality figure *not calibrated against human coding* | Agreement score **43.5 and 44.7** against **44.3 and 45.3** for 5.0.0-beta.3: not distinguishable given sampling error, and not better |
| **Either way** | Marks an assignment with a `Review` flag when the decision was hard | Flagged comments scored **27–39**, unflagged **46–58**. The flag points at the weaker coding |

*Agreement score* is micro-F1 on a scale from 0 to 100: how far the AI's code assignments coincide with the human raters', counting both the codes the AI assigned that the humans did not and the codes the humans assigned that the AI missed. 100 would be identical coding.

## How to read these numbers

- **The level is low because the task is hard.** The corpus is GoEmotions (Demszky et al., 2020): short Reddit comments without their thread, 27 emotions plus neutral, several labels allowed. The dataset's own authors report macro-F1 .46 for a BERT model trained on 43,000 labelled comments. The skill uses no training data. A score of 50 here says nothing about what the score would be on your material.
- **The difference is what transfers, if anything does.** What the tests support is the comparison: calibrated coding agreed better than uncalibrated coding, three times, on comments that had played no part in the calibration.
- **The gain is not evenly spread.** It sits mostly in frequent codes. Individual codes moved in both directions from one sample to the next, and the average over codes (macro-F1) rose in one sample of three. After calibrating, look at the per-code figures for the codes your argument rests on (Step 5b, "Read the result per code").
- **Human coding is the yardstick, not the truth.** The human raters agree little among themselves on several categories: Cohen's κ between two raters is below 0.25 for disapproval, annoyance, approval, disappointment and realization, against 0.75 for gratitude (Demszky et al., 2020, Table 7).

## What changed between versions, and what the tests said

| Version | Change | Tested result |
|---|---|---|
| 5.0.0-beta.4 | Decision rules per code, calibration against human coding (Step 5b), eight-step decision procedure, `Review` flag | With calibration clearly above beta.3. Without calibration below it: rules drafted from definitions alone widened a code |
| 5.0.0-beta.5 | Two procedures: the eight steps only for a calibrated codebook, a simple one otherwise | Calibrated path confirmed on new comments. Without calibration about two points below beta.3, outside sampling error in the second of two samples |
| 5.0.0-beta.6 | Where the codebook defines a residual category by a threshold, that threshold is applied instead of assigning a flagged substantive code | Without calibration about a point and a half above beta.5 in both runs (direction only; intervals include zero) and no longer distinguishable from beta.3. Calibrated path confirmed a third time |

## What has not been shown

1. **Other kinds of text.** Nothing here covers interviews, reports or policy documents. An external evaluation of 5.0.0-beta.3 on interviews and reports is summarised in `../evaluations/2026-09-beta3-external-review.md`; the versions after it have not been re-run on that material.
2. **Other models.** All coding in these tests ran on one Claude model (`claude-opus-5-5`). The skill also runs in ChatGPT and Codex; that has not been benchmarked here.
3. **Calibration material from a different source than the texts to be coded.** In every test the calibration comments came from the same corpus as the test comments.
4. **That the skill without calibration is better than beta.3 on agreement.** It is not, as far as these tests can tell. What it adds is the flag.
5. **How much the eight-step procedure contributes.** A calibrated codebook coded with a four-step procedure already scored three to four points above beta.3; the eight steps added between nothing measurable and two points (interval excluding zero in one run of two). The procedure was designed for long interview answers, where it has not been tested, so it has been left as it is.
6. **Other codebooks' residual categories.** The rule introduced in beta.6 was tested on one codebook with one residual category (`neutral`).

## The three tests

| | Benchmark | First fresh sample | Second fresh sample |
|---|---|---|---|
| Report | `2026-11-goemotions-beta3-vs-beta4.md` | `2026-11-goemotions-beta5-fresh-test.md` | `2026-11-goemotions-beta6-second-fresh-test.md` |
| Question | Does beta.4 agree better with human coding than beta.3? | Do beta.5's two procedures behave as intended on new comments? | Does beta.6's residual-threshold rule help, and does the eight-step procedure contribute? |
| Sample | 500 comments (plus 400 for calibration, 200 for re-testing revisions) | 500 other comments | 500 other comments |
| Baseline (beta.3) | 46.2 / 47.4 | 44.0 / 44.0 | 44.3 / 45.3 |
| Without calibration | beta.4: 44.2 / 43.7 | beta.5: 42.5 / 42.2 | beta.5: 42.0 / 43.2 · beta.6: 43.5 / 44.7 |
| With calibration | beta.4: 51.4 / 51.0 | beta.5: 50.8 / 51.2 | beta.6: 49.4 / 49.5 |
| Rules fixed in advance | `protocol/protocol.md` | `protocol/protocol_addendum.md` | `protocol/protocol_addendum2.md` |

Each cell gives the two independent runs. The samples are not comparable with each other in level: the baseline alone differs by about three points between them. Compare within a column.

## How the tests were kept honest

- The hypotheses, the samples, and the rule for what counts as an improvement were written down and hashed before coding started (`protocol/*.sha256`). Departures are logged in the three deviation files in `protocol/`, including corrections to earlier reports and one cost expectation that turned out wrong.
- Every batch of 50 comments was coded by a separate AI context that received only the skill text, the codebook and the batch. No coder saw human labels. Afterwards every file each coder opened was checked against the list it was allowed.
- The same model coded every arm. An improvement was claimed only where the uncertainty interval excluded zero in both runs; a difference in the right direction without that is called *direction only*.
- The calibrated codebook was frozen before any test comment was coded, and contains none of them.
- Each new skill text was written after the previous results were known. That is why each was tested on comments not used before, once, with the text and the release rule frozen beforehand.
- Results that did not go the skill's way are in the reports: beta.4 and beta.5 without calibration were below beta.3, and beta.6 without calibration is not above it.

## Check it yourself

```bash
python3 docs/benchmarks/scripts/recompute.py
```

reproduces the headline figures of all three reports from `results/units.csv` (each comment's GoEmotions id and human labels) and `results/assignments.csv` (every code each arm assigned in each run). It needs only Python 3. The comment texts are not redistributed here; they are in the public GoEmotions release, which `units.csv` indexes by id.

## Contents

- `2026-11-goemotions-beta3-vs-beta4.md`, `2026-11-goemotions-beta5-fresh-test.md`, `2026-11-goemotions-beta6-second-fresh-test.md` — the three reports.
- `protocol/` — pre-registered protocol and two addenda, the seeded samples, hashes, deviation logs.
- `materials/` — the codebooks as used (original, with drafted rules, calibrated), the calibration reviewer's revision log, example prompts, and the variant text tested in the second fresh sample.
- `results/` — all figures as JSON; `units.csv` and `assignments.csv`.
- `scripts/` — the scripts as run (documentation), and `recompute.py` (runnable).

## Reference

Demszky, D., Movshovitz-Attias, D., Ko, J., Cowen, A., Nemade, G., & Ravi, S. (2020). GoEmotions: A dataset of fine-grained emotions. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (pp. 4040–4054). Association for Computational Linguistics. https://doi.org/10.18653/v1/2020.acl-main.372
