# External evaluation of 5.0.0-beta.3 (September 2026)

**Status of this note.** The figures below are reported by an external evaluation run outside this repository (9–10 September 2026) and have not been reproduced by the author. They are recorded here so that the changes made in response to them (see `CHANGELOG.md`, Unreleased) can be traced to their trigger. They are not a benchmark result of the plugin: no benchmark protocol, dataset licence or scoring script is part of this repository yet.

## Corpora and reported figures

| Corpus | What was measured | Reported |
|---|---|---|
| GoEmotions (Demszky et al., 2020) | AI–AI consistency vs AI–human agreement | 85.1 vs 43.6 |
| Interview transcripts | Recall of human-coded assignments | 56.1 % |
| AC-ICT governance extracts | Non-relevant extracts judged relevant | 34 of 85 |

The metric behind "85.1" and "43.6" was reported as an agreement score, not as per-code α; the evaluation did not state the unit of the interview recall figure.

## The evaluation's own caveats

- The runs used shorter code descriptions and a smaller pilot than Step 5 requires.
- F1 was reported rather than the per-code α the skill prescribes.
- The figures therefore measure AI + skill + test protocol together; they cannot be attributed to the skill alone.
- Human–human agreement on GoEmotions was not looked up, so the 43.6 figure has no ceiling to be read against. Demszky et al. (2020) report inter-rater agreement per emotion; that value should be consulted before the figure is interpreted. [unverified — not checked against the paper in this repository]

## What was changed in response

Step 4 decision-rule columns; Step 5b calibration against human coding before freezing; the stepwise decision procedure and gated codes in Step 7; the `Review` column and review share; batch isolation as a mechanism in 7.2; the validator's `Review` checks. Details in `CHANGELOG.md`.

## Open points not addressed in this release

1. Character offsets and PDF page for each excerpt (evaluation point 5); the validator's verbatim check covers presence, not position.
2. A quality benchmark alongside the technical fixture (evaluation point 7): human-labelled sets under fixed protocols, reporting micro/macro-F1, per-code precision/recall, α, review share and run-to-run variance per version. Licences of candidate datasets to be checked first.
3. Human–human agreement on GoEmotions to be looked up before the 43.6 figure is interpreted.

These are tracked as GitHub issues.
