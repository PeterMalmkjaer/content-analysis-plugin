You are the coder for one batch in a blind content-analysis run. Work only from the files named here. Use only the Read and Write tools. Do not search the web, do not open any other file or directory, and do not modify any file except the output file.

Read, in this order:
1. The instrument: `/home/claude/bench/skill-beta6/skills/content-analysis/SKILL.md` (Content Analysis Skill 5.0.0-beta.6 candidate). Your task is the full-corpus coding of Step 7; Steps 1–6 have been completed for this study and the codebook is frozen (`v1`). Follow Step 7, which gives two coding procedures and says which one applies from the codebook's calibration status, and the Output: Coded Data Table conventions including the Review column. Calibration status of this codebook: **calibrated** — one Step 5b round against human coding has been carried out; the decision rules in the codebook are the calibrated ones.
2. The source declaration (Step 1 output, fixed): `/home/claude/bench/materials/set3_source_declaration.md`
3. The codebook: `/home/claude/bench/materials/set3_codebook_J.md`
4. The batch of units to code: `/home/claude/bench/runs/set3/J/run1/fresh2/batch01.md`

Then code every unit in the batch and write **one CSV file** to `/home/claude/bench/runs/set3/J/run1/fresh2/batch01.csv` with the header exactly:

Document ID,Code ID,Coder notes,Review

Rules for the file: one row per (comment, label); `Code ID` is the label name exactly as in the codebook (e.g. `admiration`, `neutral`); `Coder notes` = a 3–8-word reason. Every comment in the batch must appear (with `neutral` alone if no emotion is expressed).
- `Review` is blank when the decision was clear; otherwise exactly one of context_missing / possible_irony / competing_codes / insufficient_basis / other, as defined in SKILL.md (Step 7 and the coded-data table). `other` requires the reason in Coder notes.
- Quote CSV fields that contain commas or quotes. UTF-8. No extra columns, no commentary in the file.
- No reference labels or expected frequencies exist in your inputs; do not guess at them. Do not use keyword matching or scripts to assign codes — read every unit.
- Do not alter the codebook. If a code seems missing, use the procedure in SKILL.md (UNCODED / note), not a new code.

When finished, reply with one line: the number of units coded and the number of rows written. Nothing else.
