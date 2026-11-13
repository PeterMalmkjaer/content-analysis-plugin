# Protocol addendum — test of 5.0.0-beta.5 on fresh comments (set 3)

**Status:** pre-registered 12 November 2026, after the set 3 benchmark was scored and before any fresh comment was coded. Frozen by SHA-256 together with `splits_addendum.json` (`protocol_addendum.sha256`). It adds to `protocol.md`; nothing in that file or in `deviations.md` is changed by it.

## Why

The set 3 benchmark showed that beta.4 with Step 5b calibration agreed better with the human reference than beta.3, and that beta.4 without calibration agreed worse. beta.5 changes the skill text in response: an uncalibrated codebook is coded with a simple procedure (no drafted decision rules, no code-by-code sweep), a calibrated one with the full decision procedure. The skill text was written by the orchestrator after seeing the results on the 500 test comments, so those comments cannot test it. This addendum tests it on comments nobody in the study has coded.

## Tested text

`skills/content-analysis/SKILL.md` at commit `08c38e5` (sha256 `de3eaf58…`). **One shot:** this text is not edited in response to the fresh results. If H-E or H-F below fails, beta.5 is not released in this form and the failure is reported.

## Sample

500 comments drawn uniformly at random (seed 20261112) from the 4,327 comments of the official GoEmotions test split that are in none of the earlier splits (`splits_addendum.json`). No coding subagent, the rule drafter or the calibration reviewer has seen them. The orchestrator has seen only aggregate label counts.

## Arms (all on the same 500 comments)

| Arm | Skill | Codebook | Status told to the coder |
|---|---|---|---|
| **A** | 5.0.0-beta.3 (`13b50b5`) | Original codebook (`set3_codebook_A.md`) | — |
| **E** | beta.5 text (`08c38e5`) | The same original codebook (`set3_codebook_E.md`, identical file) | uncalibrated |
| **F** | beta.5 text (`08c38e5`) | The arm-C codebook frozen in the benchmark (`set3_codebook_F.md`, identical to `set3_codebook_C.md`, sha256 `226474a1…`) | calibrated |

The arm-F codebook was calibrated under beta.4's flow (rules drafted from the definitions, then one Step 5b round). beta.5 describes the same flow. No new calibration is run here; what is tested is beta.5's two **coding** procedures.

Coding model `claude-opus-5-5` for every arm; one subagent per batch of 50; two independent runs per arm with different batch composition; same prompt delivery, gap handling, assembly, scoring and blindness audit as in the benchmark (`deviations.md`, D5–D9). The fixed co-coding rule (neutral alone) applies to all arms.

## Hypotheses and decision rules

Paired bootstrap over the 500 comments, 2,000 resamples, seed 20261112, 95 % interval, run 1 against run 1 and run 2 against run 2.

- **H-E — the uncalibrated procedure does not fall below beta.3.** Holds if, in both runs, E − A in micro-F1 is positive or its interval includes zero. Fails if in either run the whole interval lies below zero.
- **H-F — the calibrated path keeps its advantage on fresh comments.** Holds if, in both runs, F − A is positive and its interval excludes zero.
- **H-R — the Review flag marks weaker coding.** Holds if, in both runs of E and of F, micro-F1 on comments with at least one flagged assignment is lower than on comments with none. (Observed after the fact in the benchmark; pre-registered here.)

Reported without a decision rule: macro-F1 and per-code figures, review share (expected 5–30 %), run-to-run stability per arm, the `disapproval` AI/human ratio, and arm A's level on the fresh sample next to its level on the first 500.

## What this cannot show

One corpus of short comments and one model. The effect of dropping the code-by-code sweep on long elicited units (interviews), where low recall was the reported problem, is not tested here. Calibration of a codebook from scratch under the beta.5 text is not tested here either.
