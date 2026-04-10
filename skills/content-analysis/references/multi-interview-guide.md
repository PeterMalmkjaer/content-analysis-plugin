# Multi-Interview Corpus Management Guide

This reference covers how to manage the codebook and outputs when the corpus contains more than one interview. The core principle is **cumulative codebook growth**: codes are never reset between interviews; the codebook expands iteratively as new material is introduced.

---

## Table of Contents

1. [When This Guide Applies](#when-this-guide-applies)
2. [The Cumulative Codebook Principle](#the-cumulative-codebook-principle)
3. [Interview-by-Interview Workflow](#interview-by-interview-workflow)
4. [Codebook Versioning](#codebook-versioning)
5. [Cross-Interview Output Files](#cross-interview-output-files)
6. [Theoretical Saturation](#theoretical-saturation)
7. [Retroactive Coding](#retroactive-coding)
8. [Output File Naming Conventions](#output-file-naming-conventions)

---

## When This Guide Applies

Use this guide whenever the user provides more than one interview transcript for the same research question. A multi-interview corpus is typical in:

- Qualitative studies with multiple informants (e.g., 8–15 semi-structured interviews)
- Longitudinal designs where the same participant is interviewed at multiple time points
- Comparative designs with participants from different groups (e.g., students vs. faculty)

If each interview addresses a **different** research question, treat them as independent analyses and do not merge their codebooks.

---

## The Cumulative Codebook Principle

The codebook is a living document. It is **never reset** between interviews. Instead:

- Codes established in earlier interviews are carried forward and applied to all subsequent interviews.
- New codes are added when a theme emerges that cannot be captured by an existing code.
- Existing code definitions may be refined (broadened or narrowed) if a new interview reveals that the original definition was too narrow or ambiguous — but the code ID is preserved.
- Codes are never deleted mid-analysis. If a code turns out to be irrelevant, mark it as inactive in the codebook rather than removing it, so the audit trail is preserved.

This approach ensures that every interview is coded against the same framework, making cross-interview comparison valid.

---

## Interview-by-Interview Workflow

### First Interview

Follow the full 8-step workflow from `SKILL.md`. By the end you have:

- A codebook (v1.0) derived inductively from this interview.
- A coded data table for this interview.
- A frequency report for this interview.

### Each Subsequent Interview

**Step 1 — Deductive pass:** Apply the current codebook to the new interview. Do not generate new codes yet. Code everything that fits existing codes.

**Step 2 — Gap identification:** Read through the remaining uncoded units. Identify passages that carry meaning not captured by any existing code.

**Step 3 — Inductive extension:** For each gap, generate a candidate new code following the same codebook structure (Code ID, name, definition, inclusion criteria, exclusion criteria, example excerpt, parent category). Decide whether the gap represents:
  - A genuinely new theme → add a new code.
  - A sub-variant of an existing theme → consider splitting the existing code or adding a note, rather than a new top-level code.
  - A one-off artefact of this particular participant → flag as a memo rather than a code.

**Step 4 — Codebook update:** Add new codes to the master codebook and increment the version number.

**Step 5 — Retroactive check:** Scan all previously coded interviews for instances of the new code. Apply retroactively where appropriate (see [Retroactive Coding](#retroactive-coding)).

**Step 6 — Produce per-interview outputs:** Coded data table and frequency report for this interview only, clearly labelled with the participant ID.

---

## Codebook Versioning

Record each change to the codebook in a version log at the top of the codebook file. Suggested format:

| Version | Date | Change | Triggered by |
|---------|------|--------|--------------|
| 1.0 | YYYY-MM-DD | Initial codebook from first interview | Interview 1 (BK) |
| 1.1 | YYYY-MM-DD | Added NETWORK_01 (informal network use) | Interview 2 (XX) |
| 1.2 | YYYY-MM-DD | Broadened BARR_03 definition to include institutional gatekeeping | Interview 3 (YY) |

This log is essential for methodological transparency. Reviewers need to see when and why the codebook changed.

---

## Cross-Interview Output Files

Once all interviews are coded, produce three additional output files.

### 1. Cross-Interview Frequency Matrix (`frequency_report_CROSS.xlsx`)

A matrix where rows are codes and columns are participant IDs. Each cell contains the frequency for that code in that interview. Include:

- Absolute counts per interview.
- Row totals (code frequency across entire corpus).
- Column totals (total coded units per interview).
- A summary sheet with codes ranked by corpus-wide frequency.

This file is the primary basis for cross-interview comparison and pattern reporting.

### 2. Master Coded Data Table (`coded_data_ALL.xlsx`)

A single coded data table containing all coded units from all interviews, with a `Participant ID` column prepended. This enables corpus-wide searching and sorting by code, participant, or theme.

### 3. Comparative Theme Summary (`theme_summary_CROSS.md`)

A narrative report that:
- Identifies themes present across all or most interviews (core themes).
- Identifies themes present in only one or a few interviews (idiosyncratic themes).
- Compares how the same theme manifests differently across participants or groups.
- Notes any systematic differences between participant subgroups if the design is comparative.

---

## Theoretical Saturation

Monitor saturation across interviews by tracking the number of new codes added per interview:

| Interview | New codes added | Running total |
|-----------|----------------|---------------|
| 1 (AB)    | 41             | 41            |
| 2 (XX)    | 7              | 48            |
| 3 (YY)    | 3              | 51            |
| 4 (ZZ)    | 1              | 52            |
| 5 (AA)    | 0              | 52            |

When two or three consecutive interviews add zero new codes, saturation is reached. Report this explicitly in the methods section:

> "Theoretical saturation was reached after [N] interviews; no new codes emerged in the final [n] interviews."

If the user has a fixed number of interviews (a closed corpus), saturation is assessed post-hoc rather than used as a stopping criterion.

---

## Retroactive Coding

When a new code is added in interview N, check all interviews 1 through N−1 for instances of that code.

**Practical approach:**

1. Note the definition of the new code.
2. Search each previous coded data file for units currently marked "uncoded" or assigned to adjacent codes.
3. Re-read those units and apply the new code where appropriate.
4. Update the per-interview coded data tables and frequency reports.
5. Record the retroactive pass in the codebook version log.

Retroactive coding is what makes the cumulative codebook valid: every interview is eventually coded against the full final codebook, not just the codebook that existed when it was first processed.

**When retroactive coding is impractical** (very large corpus, time constraints): document the limitation explicitly. State which interviews were coded against which codebook version. This reduces comparability but does not invalidate the analysis if disclosed.

---

## Output File Naming Conventions

| File | Scope | Naming pattern |
|------|-------|----------------|
| Codebook | Shared across all interviews | `codebook_[project].xlsx` |
| Coded data (single interview) | Per participant | `coded_data_[ParticipantID].xlsx` |
| Coded data (full corpus) | All participants | `coded_data_ALL.xlsx` |
| Frequency report (single interview) | Per participant | `frequency_report_[ParticipantID].xlsx` |
| Frequency report (cross-interview) | All participants | `frequency_report_CROSS.xlsx` |
| Theme summary (single interview) | Per participant | `theme_summary_[ParticipantID].md` |
| Theme summary (comparative) | All participants | `theme_summary_CROSS.md` |
| Thematic map (single interview) | Per participant | `thematic_map_[ParticipantID].mermaid` |
| Thematic map (full corpus) | All participants | `thematic_map_CROSS.mermaid` |

All files for a participant should be written to `output/[ParticipantID]/`. Cross-interview files go in `output/cross/`.
