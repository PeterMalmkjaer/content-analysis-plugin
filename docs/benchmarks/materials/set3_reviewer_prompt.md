You are carrying out the disagreement review of a codebook calibration (Step 5b, points 3–4, of the instrument). You do not code any unit. Work only from the files named here. Use only the Read and Write tools. Do not search the web, do not open any other file or directory, and do not modify any file except the two output files.

Read, in this order:
1. The instrument: `/home/claude/bench/skill-beta4/skills/content-analysis/SKILL.md` (Content Analysis Skill 5.0.0-beta.4). Read Step 4 (the codebook's decision-rule columns and where examples may come from) and Step 5b ("Calibrate Against Human Coding Before Freezing the Codebook") in full; your task is Step 5b point 4, "Review the disagreements". Read Step 7's decision procedure so that you know how a coder will use what you write.
2. The source declaration (fixed, not open to revision — including the co-coding rule for the neutral category): `/home/claude/bench/materials/set3_source_declaration.md`
3. The current codebook: `/home/claude/bench/materials/set3_codebook_B.md`
4. The calibration result — per-code figures and every disagreement between the AI coder and the human reference on the calibration set, grouped by code pair: `/home/claude/bench/materials/set3_calibration_review_input.md`

Then do what Step 5b point 4 asks. For each frequent code pair, decide whether the human coding is the standard to move towards or whether the codebook is ambiguous, and revise the **decision-rule columns** of the codes concerned (Required textual basis · Nearest alternative codes · Decisive difference · Boundary example · Co-coding rule).

Write two files.

**A. The revised codebook** → `/home/claude/bench/materials/set3_codebook_C_candidate.md`
- It is the current codebook with revisions made **only inside the per-category entries** of the `## Decision rules` section (the entries headed `### <n>: <name>`). Keep every entry's heading and its six bullets (`**Required textual basis:**`, `**Nearest alternative codes:**`, `**Decisive difference:**`, `**Boundary example:**`, `**Co-coding rule:**`, `**Gate:**`) in the same order.
- Everything else stays **byte-for-byte as it is**: the original codebook text at the top (research question, instructions, the 28 category lines with their definitions), the introductory paragraph of the Decision rules section, and the list of general rules. Entries you do not revise stay unchanged.
- A rule must be a textual criterion that a coder can check against the comment in front of them. Do not write quotas, frequency targets or statements about how often a code should be used.
- Examples follow Step 4: a boundary example may now also be quoted verbatim from a calibration comment (give its ID), or be written by you and marked `(constructed)`.
- Do not add, remove or rename categories. Do not contradict the source declaration.

**B. The revision log** → `/home/claude/bench/materials/set3_calibration_revision_log.md`
- One row per revised code, in the form of the instrument's candidate log (`redefine` rows): the code; which column(s) changed; what changed, in one or two sentences; the trigger units (IDs from the calibration set); and your Step 5b decision for that revision — *human coding is the standard* or *codebook was ambiguous* — with a one-line reason.
- Then a short list of frequent disagreement pairs you examined and deliberately left **unrevised**, each with the reason (for instance: the reference looks inconsistent on these units; the difference follows from the fixed co-coding rule; too few cases to generalise).

What happens next, so that you can judge how far to go: each revised entry will be tested, blind, on comments that are not in the calibration set. A code's revision is kept only if that code's agreement with the human reference improves on those fresh comments; otherwise that entry reverts to its current wording. A revision that only fits the comments that motivated it will therefore be thrown away. Prefer revisions that state a general, checkable criterion.

When finished, reply with one line: the number of entries revised, and the number of disagreement pairs examined but left unrevised. Nothing else.
