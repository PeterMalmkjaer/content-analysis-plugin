# Benchmark protocol — 5.0.0-beta.3 vs 5.0.0-beta.4

**Status:** pre-registered 2026-09-10, before any unit was coded under this protocol. Frozen by SHA-256 (see `protocol.sha256`) together with `splits.json`. Deviations are logged in `deviations.md`, never edited into this file.

**Purpose.** Test whether the beta.4 changes (decision-rule columns, Step 5b calibration, stepwise decision procedure, gated codes, `Review` column, batch isolation as mechanism) improve AI–human agreement over beta.3 on the three corpora used in the external evaluation of beta.3 (Codex, 9 September 2026). The aim is a better instrument, not a better number: a result showing no improvement, or a regression, is reported as such.

## 1. Instruments

| Arm | Skill | Codebook state |
|---|---|---|
| **A** | 5.0.0-beta.3 (`13b50b5`) | Original codebook as used in the Codex evaluation |
| **B** | 5.0.0-beta.4 (`05848fc`) | Original codebook + decision-rule columns drafted in Step 4 from definitions and a *development read* of the calibration split's **texts only** (no reference labels). Not calibrated; every reliability figure labelled *not calibrated against human coding*. |
| **C** | 5.0.0-beta.4 (`05848fc`) | As B, then Step 5b: blind coding of the calibration split, per-code P/R/F1 and α against the reference, disagreement review by code pair, revision of the decision-rule columns only, re-test on the retest split, revisions kept only if they hold there, then frozen as `v1`. Sets 1 and 3 only. |

Arm B isolates the effect of the *procedure* (Step 4 columns, Step 7 decision steps, Review) from the effect of *calibration* (C). Arm C is the full beta.4 path.

**Model.** All arms run in the same Claude Cowork session on the same model (configured identifier `claude-fable-5-1`; the serving model can differ and is not observable from inside the session; sampling parameters are not exposed). Each coding batch is a separate subagent context that receives only: the version's `SKILL.md`, the codebook, the source declaration, the batch's units, and (arm B/C) the decision-rule columns. No batch sees reference labels, another batch's output, or the Codex results. This is the 7.2 mechanism for all arms alike.

**Codex beta.3 figures (60.1 / 63.1 / 43.6)** are a third reference point under a different model and protocol. They are not the baseline; arm A is.

## 2. Corpora, splits, references

Seed 20260910. Splits are fixed in `splits.json` and were drawn before any coding.

| Set | Units | Reference | Split (test / calibration / retest) | Arms |
|---|---|---|---|---|
| 1 · TU Delft interviews (Zuiderwijk-van Eijk & van Gend 2022, CC BY 4.0) | 262 Q/A units, 7 interviews, 54-code deductive codebook | Published researcher coding (one coder), mapped to units by the Codex ≥20-character overlap rule; reproduced exactly from the Codex outputs (P 64.6 / R 56.1 / F1 60.1) | 105 / 105 / 52, stratified by interview | A, B, C |
| 2 · AC-ICT (Janssens, Bharosa & Janssen 2026, CC BY-SA 4.0) | 184 recommendation excerpts, 6 reports, Dutch, 5 fields with `GOV_RELEVANT` as gate | The authors' AI-workflow output with researcher review — **not** human gold; reported as agreement with the reference workflow | 184 / — / — | A, B |
| 3 · GoEmotions (Demszky et al. 2020, Apache 2.0) | Official test split, 5,427 comments, 27 emotions + neutral | Three human raters; test split filtered on rater agreement | 500 / 400 / 200, uniform random from the 5,427 | A, B, C |

Reference coverage after the split is what it is and is reported, not adjusted: in set 1 only 3 of 54 codes have ≥10 positives in the calibration split (24 of 54 in the full corpus); in set 3, 17 of 28 labels do, and grief, relief and nervousness are absent from calibration. Codes under ten positives are reported by name as *insufficiently calibrated* and kept out of the averages (beta.4, Step 5b).

**Protocol agreement (set 3).** 181 of 5,427 reference comments carry neutral together with an emotion; the Codex protocol required neutral alone. To keep arms comparable, all arms keep the Codex co-coding rule (neutral only when no emotion is assigned); F1 excluding neutral is reported alongside, and the number of test units affected is stated. Evidence for set 3 is the whole comment, attached mechanically, as in the Codex run; the validator's excerpt check is therefore vacuous for set 3 and is not counted as evidence of citation quality.

## 3. Runs

- Test split: two independent runs per arm (fresh subagents, different batch order in run 2). Run-to-run consistency (F1 between runs, per-code κ) is reported as *stability*, separate from agreement with the reference.
- Batch sizes: set 1 ≈ 10 units, set 2 ≈ 25 units, set 3 = 50 units.
- Pilot: the skill's own Step 5 applies within each arm's procedure; the codebook is not changed during test coding in any arm.
- The validator of the arm's own version is run on every output; `RESULT` is reported verbatim.
- If budget or time forces a cut, the second run of arm B is dropped first, then the second run of arm A; the cut is recorded in `deviations.md`.

## 4. Measures

Per set and arm, on the test split, against the reference: per-code precision, recall, F1, Cohen's κ and Krippendorff's α (binary presence/absence per unit); micro-F1; macro-F1 over codes with ≥1 reference positive in the test split, with per-code min–max; exact label-set match per unit; predicted/reference count ratio per code. For arms B and C: review share overall and per code, and the share of `other`. For set 2: gate false-positive rate (reference N coded RESP/MECH) and gate false-negative rate, and per-field agreement on reference-positive units, as in the Codex report.

Uncertainty: paired bootstrap over units (2,000 resamples, seed 20260910) for the difference in micro-F1 between arms, reported as a 95 % interval; it covers sampling of units only, not model or prompt variance (which the two runs address in part).

## 5. Pre-registered expectations

These are hypotheses, stated before running. P1–P3 are derived from the Codex beta.3 reports, whose error patterns were computed on the *full* sets, so they are directional expectations from overlapping data, not independent predictions.

- **P1 (broad-code drift, set 3).** In the Codex run `disapproval` was predicted 1,112× against 267 reference positives (ratio 4.2). Expectation: the ratio is closer to 1 in arms B and C than in A.
- **P2 (recall on broad codes, set 1).** Codex recall on C29 "Experience with sharing research data [R]" was 7/31. Expectation: recall on C29 higher in B and C than in A.
- **P3 (gate, set 2).** Codex let 34 of 85 reference-N units through the gate. Expectation: gate false-positive rate lower in B than in A.
- **P4 (main).** Micro-F1: C ≥ B ≥ A on sets 1 and 3; B ≥ A on set 2. B < A is a possible and reportable outcome (procedure cost without calibration).
- **P5 (offloading check).** Review share in B and C between 5 % and 30 %. Above 30 %, the procedure is offloading decisions rather than making them, and any agreement gain is read together with that share.
- **P6 (stability).** Run-to-run consistency in B and C not lower than in A.

A result is called an improvement only if the bootstrap interval for ΔF1 excludes zero **and** the direction holds in both runs. Anything else is reported as no demonstrated difference.

## 6. Contamination and blindness — declared

- The orchestrator (the Cowork assistant writing this protocol) has read the Codex beta.3 reports, including aggregate error patterns computed on the full corpora, and the per-unit disagreements for set 1. It does not code units and does not write decision rules.
- Coding subagents receive no reference labels, no disagreement data, no Codex output, and no other batch's output.
- Arm B decision-rule drafting is done by a subagent that receives the codebook and the calibration split's texts only.
- Arm C calibration review is done by a subagent that receives the calibration split's AI-vs-reference disagreements and the current decision rules; it may edit only the decision-rule columns; the orchestrator applies the edits verbatim and runs the retest.
- GoEmotions and the two 4TU datasets are public and may have been in the model's training data; this cannot be checked from here and is a limitation of every arm equally.
- The human–human ceiling for GoEmotions (Demszky et al., 2020) is to be looked up from the paper before the results are interpreted; at pre-registration it has not been.

## 7. Outputs

Per set and arm and run: `coded_data.csv` (long format, the arm's own column set), `codebook` as used (with decision-rule columns for B/C, and the C revision log), `manifest.csv`, `frequencies.csv`, validator output, and the subagent prompts. Metrics in `results/metrics.json` and a report `docs/benchmarks/2026-09-beta3-vs-beta4.md` for the repository, with the figures next to the review shares and the deviations log.
