# External evaluation of 5.0.0-beta.3 (9 September 2026): the reports

This folder holds the four reports from the external evaluation that is summarised in [`../2026-09-beta3-external-review.md`](../2026-09-beta3-external-review.md). They are published so that the figures quoted elsewhere in this repository can be read in their original context. How they fit with the rest of the documentation is shown in [`../../README.md`](../../README.md).

The reports are in Danish. They concern **5.0.0-beta.3 only**. No later version has been run on the interview transcripts or the policy reports.

## Read this first: the reports were written by an AI

- The evaluation was run on 9 September 2026 in a Codex session (the protocol states "GPT-6 family"). The same AI session coded the material, scored it and wrote the reports. The author of the plugin commissioned the evaluation. The reports are published here as the AI wrote them, apart from the changes listed at the end of this file.
- AI-written text can contain errors, including errors that look plausible. **Do not rely on a statement in these reports without checking it.**
- The check described below was also made with an AI assistant (Claude, 13 November 2026), by recomputing figures with scripts. It is one AI checking another's arithmetic. It is not an audit by a person.

## What was checked on 13 November 2026

Table 1 lists what was recomputed and what was not. Every recomputed figure matched the report.

**Table 1. Check of the reports' figures**

| Report | Recomputed, and matching | Basis of the recomputation | Not checked |
|---|---|---|---|
| 1 · Interviews | Shared, AI-only and reference-only assignments (306 / 168 / 239); precision 64.6, recall 56.1, micro-F1 60.1; macro-F1 57.9; identical code set 26.3 %; mean κ per code 0.565 and its range; micro-F1 for each of the seven interviews; the figures for the code "Experience with sharing research data [R]" (7 of 31; F1 35.9) | The evaluation's coded assignments and its own list of disagreements | The mapping of the researchers' coded passages to units, on which every figure rests; the sensitivity figure 53.0; the blind repeat of interview I1 (83.4; 30.8 %; κ 0.774); the validator results and the 100 % figures |
| 2 · AC-ICT | Shared, AI-only and reference-only field values (396 / 280 / 184); precision 58.6, recall 68.3, F1 63.1; all five fields identical in 74 of 184; the five per-field agreements; 34 of 85 non-relevant excerpts coded relevant (23 RESP, 11 MECH); 10 of 99 relevant excerpts coded N | The evaluation's own table pairing reference and predicted values | Whether the reference values in that table are those of the data set's authors; the blind repeat of report D02 (87.5; 61.5 %; κ 0.691); all figures on PDF extraction and excerpt matching; the validator results |
| 3 · GoEmotions | Shared, AI-only and reference-only labels (2,791 / 3,694 / 3,538); precision 43.0, recall 44.1, micro-F1 43.6; macro-F1 38.6; micro- and macro-F1 without neutral (41.1; 38.1); identical label set 32.9 %; the all-neutral baseline (30.4; 29.6 %); counts and F1 for the twelve categories named in the report; 181 comments with neutral plus an emotion; the repeat on 150 comments (85.1; 76.0 %) | The evaluation's table of reference and predicted labels. Its reference labels are identical, for all 5,427 comments, to the `test.tsv` file the evaluation downloaded | The bootstrap interval 42.4–44.7; κ for the repeat (0.762); the validator results; that the predictions were frozen before the comparison |
| Summary | Its three scores and the range 53.0–60.1 are those of reports 1 to 3 | – | – |

Three limits of this check matter more than the rest:

1. **For the interviews the check is partly circular.** The reference used here was rebuilt from the evaluation's own output files, not from the original data set. The check therefore shows that the reported figures follow from the evaluation's files. It does not show that the researchers' coding was mapped to the units correctly.
2. **For AC-ICT the reference is itself an AI workflow** with researcher review, as report 2 says. Agreement with it is not agreement with human coding.
3. **Descriptions of procedure cannot be recomputed.** That coders were blind, that a pilot preceded the coding, that nothing was adjusted afterwards: these rest on the AI's own account.

## How to read these reports beside `docs/benchmarks/`

Do not set the figures side by side. The evaluation used another model family, another protocol and a single run, with shorter code descriptions and a smaller pilot than the skill prescribes (the evaluation's own caveats are listed in the review note). The benchmarks in [`../../benchmarks/`](../../benchmarks/) use fixed samples, two runs per arm and one Claude model, and cover GoEmotions only.

## What is not here, and why

The coded data, audit workbooks, score files and original archives are not in this repository. The interview data are licensed CC BY 4.0 and the AC-ICT data CC BY-SA 4.0; the share-alike terms of the second have not been reconciled with this repository's licence, so no adapted data are redistributed here. The data sets can be obtained from the sources named in each `SOURCE.md`.

The reports refer to files "in the same folder" (`audit_workbook.xlsx`, `validation.txt`, `scores.json`, `audit_bundle.zip` and others). Those files are not included here.

## Files, and what was changed in them

**Table 2. Files in this folder**

| File | Content | Change |
|---|---|---|
| `kvalitetsrapport.md` | Summary of the three tests | Notice added below the title. Seven links to paths on the author's computer replaced: three by relative links to the reports here, four by plain text |
| `01_delft_interviews/rapport.md` | Report 1: interview transcripts | Notice added below the title |
| `01_delft_interviews/SOURCE.md` | Source, licence, changes to the data | None |
| `02_delft_reports/rapport.md` | Report 2: AC-ICT policy reports | Notice added below the title |
| `02_delft_reports/SOURCE.md` | Source, licence, changes to the data | None |
| `03_goemotions/rapport.md` | Report 3: GoEmotions, full test split | Notice added below the title |
| `03_goemotions/SOURCE.md` | Source and changes to the data | None |
| `03_goemotions/protocol.md` | The evaluation's protocol with its addenda for data sets 2 and 3 | None |

SHA-256 of the original files, as they were on the author's computer:

```text
c97a1c5ad0a50e89485192b6bb485ea1e3f41ffde1943f625fdc8dcda0fe93c8  kvalitetsrapport.md
adab351436adea09d49065981bd473a36bc2bebdc6c9252facfa517d766b1867  01_delft_interviews/rapport.md
9234703cc591f7bd787ba787fe7cfe8a152d196457afc94389d12690fffbf203  01_delft_interviews/SOURCE.md
f1da5010733f39f92a6cbfa92e1a916a35fb537e1834c1a4cca5a6ca64a7d786  02_delft_reports/rapport.md
2952dfb4335390efcffc316dac29d3e8f5645e5da3db276ffe499b900464e288  02_delft_reports/SOURCE.md
2691486aefdf31869fe9567b436650726ae006880a9e9e27f50755ca0b5244d6  03_goemotions/rapport.md
3c9637dbe7b6d9e84d0f47f3ccae5357a6ca8e5af1ebfadc93aee8b53c5576cf  03_goemotions/SOURCE.md
4610d901ce3d3041fca9de5bdfaaceab609b6d1decc1e8702a2f92fe40be499e  03_goemotions/protocol.md
```

The four files marked "None" match these checksums as they stand. The four reports differ from their originals only by the changes listed in Table 2.

## Data sources

- Zuiderwijk-van Eijk, A. M. G., & van Gend, T. N. (2022). *Open research data: A case study into institutional and infrastructural arrangements to stimulate open research data sharing and reuse: Interview transcripts and codebook* [Data set]. 4TU.ResearchData. https://doi.org/10.4121/19635147
- Janssens, N., Bharosa, N., & Janssen, M. (2026). *Data supporting the publication: Trustworthy LLM-assisted qualitative content analysis method* [Data set]. 4TU.ResearchData. https://doi.org/10.4121/ea45e84e-d128-4950-9d7a-0338fd7e064e.v1
- Demszky, D., Movshovitz-Attias, D., Ko, J., Cowen, A., Nemade, G., & Ravi, S. (2020). GoEmotions: A dataset of fine-grained emotions. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (pp. 4040–4054). https://doi.org/10.18653/v1/2020.acl-main.372
