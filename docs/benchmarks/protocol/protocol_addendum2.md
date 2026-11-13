# Protocol addendum 2 — test of the 5.0.0-beta.6 candidate on fresh comments (set 3)

**Status:** pre-registered 13 November 2026, after the benchmark and the first fresh-sample test were scored and published (5.0.0-beta.5, `main` at `d856346`), and before any comment of the new sample was coded. Frozen by SHA-256 together with `splits_addendum2.json` (`protocol_addendum2.sha256`). It adds to `protocol.md` and `protocol_addendum.md`; nothing in those files or their deviation logs is changed by it.

## Why

The first fresh-sample test left two things open.

1. **Without calibration, beta.5 scored a point and a half below beta.3** (not distinguishable, both estimates negative). An exploratory look placed the whole deficit in the flagged comments: where the human raters chose `neutral`, beta.5 assigned an emotion and flagged it, following its rule that uncertainty is flagged and never coded as neutral. The candidate text changes that rule: where a codebook defines a residual category by a threshold, a unit that does not clearly meet a substantive code's definition meets the residual category's definition and is coded there.
2. **Whether the eight-step decision procedure adds anything once the codebook is calibrated** has never been tested: the calibrated arm has always differed from the baseline in codebook and procedure at once.

Both texts below were written by the orchestrator after seeing the earlier results, so the earlier comments cannot test them.

## Texts

| | Commit | `SKILL.md` sha256 | Standing |
|---|---|---|---|
| **T1** — beta.6 candidate | `d510a60` | `e0cfbd52…` | Release candidate. Differs from beta.5 in two sentences: the residual-threshold rule in "Uncertainty is not a code" and its application in step 2 of the uncalibrated procedure |
| **T2** — variant | `ddb7a48` | `ac04aed0…` | **Not a release candidate.** T1 with the eight-step decision procedure for calibrated codebooks replaced by a four-step one (bound and read; assign on definitions, criteria and the calibrated decision rules; no sweep; mark what remains) |

**One shot:** neither text is edited in response to the results.

## Sample

500 comments drawn uniformly at random (seed 20261113) from the 3,827 comments of the official GoEmotions test split that are in none of the earlier samples (`splits_addendum2.json`). No coding subagent, the rule drafter or the calibration reviewer has seen them; the orchestrator has seen only aggregate label counts.

## Arms (all on the same 500 comments)

| Arm | Skill text | Codebook | Status told to the coder |
|---|---|---|---|
| **A** | 5.0.0-beta.3 (`13b50b5`) | Original (`set3_codebook_A.md`) | — |
| **E** | 5.0.0-beta.5 (`08c38e5`, as released) | Original (identical file) | uncalibrated |
| **H** | T1 | Original (identical file) | uncalibrated |
| **J** | T1 | Calibrated codebook frozen in the benchmark (identical to `set3_codebook_C.md`, sha256 `226474a1…`) | calibrated |
| **G** | T2 | The same calibrated codebook | calibrated |

Coding model `claude-opus-5-5` for every arm; one subagent per batch of 50; two runs per arm, run 2 with different batch composition (comments reshuffled, seed 20260910 + 2); within a run all arms code identical batches; same delivery, gap handling, assembly, scoring and blindness audit as before.

**Prompt.** Arm A's prompt is the benchmark's, unchanged apart from paths. In the earlier tests the prompt for the arms with a `Review` column repeated the skill's rule in one sentence ("Uncertainty is recorded in Review, never by choosing neutral/UNCODED/the broadest code"). That sentence is the rule under test here, so it is removed from the prompt of **every** arm with a `Review` column (E, H, J, G): the skill text alone has to carry the rule. Arm E therefore runs beta.5's text with a prompt one sentence shorter than in the first fresh-sample test; its level here is not directly comparable with its level there.

## Hypotheses and decision rules

Paired bootstrap over the 500 comments, 2,000 resamples, seed 20261113, 95 % interval, run 1 against run 1 and run 2 against run 2. Micro-F1 against the published reference throughout.

- **H-1 — the change helps without calibration.** H − E is positive in both runs. It is called an *improvement* only if both intervals exclude zero; positive with an interval that includes zero in either run is reported as *direction only*.
- **H-2 — the uncalibrated procedure is not below beta.3.** In both runs H − A is positive or its interval includes zero.
- **H-3 — the calibrated path is intact under T1.** In both runs J − A is positive and its interval excludes zero.
- **H-4 — the flag still marks weaker coding.** In both runs of H and of J, micro-F1 on comments with at least one flagged assignment is lower than on comments with none.
- **H-5 — mechanism.** In both runs, the number of comments H codes `neutral` is closer to the reference count than the number E codes `neutral`.

**Release rule.** T1 is released as 5.0.0-beta.6 if H-2 and H-3 hold and the point estimate of H − E is positive in both runs. Otherwise it is not released, 5.0.0-beta.5 stands, and the result is reported.

**Arm G — reading fixed in advance.** J − G: interval excludes zero and positive in both runs → the stepwise procedure contributes on this material. Interval excludes zero and negative in both runs → the short procedure does better on this material. Anything else → no demonstrated difference. In no case is T2 released on this evidence: the code-by-code sweep was introduced for low recall on long elicited units (interviews), which short comments cannot speak to. Under the second or third outcome T2 becomes a candidate to be tested on such material.

Reported without a decision rule: macro-F1 and per-code figures, review share, run-to-run stability, `disapproval` and `neutral` counts, measured cost and duration per arm (from the subagent transcripts).

## What this cannot show

One corpus of short comments and one model. No new calibration is run. Nothing here transfers to interviews or documents, to other models, or to codebooks without a residual category defined by a threshold.
