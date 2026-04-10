---
description: Run a scientific content analysis on uploaded documents
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [documents or instructions]
---

Before doing anything else, read these four files in order:

1. ${CLAUDE_PLUGIN_ROOT}/skills/content-analysis/SKILL.md
2. ${CLAUDE_PLUGIN_ROOT}/skills/content-analysis/references/multi-interview-guide.md
3. ${CLAUDE_PLUGIN_ROOT}/skills/content-analysis/references/reliability-guide.md
4. ${CLAUDE_PLUGIN_ROOT}/skills/content-analysis/references/coding-approaches.md

These define the complete eight-step workflow and all reference material you will need. Do not proceed until all four are loaded.

## Input Detection

Before asking the user anything, inspect the `input/` directory:

1. **Scan `input/` for files and subfolders.**

2. **Standalone mode** — if there are transcript files directly inside `input/` (not in a subfolder):
   - Each file is an independent interview.
   - Analyse them separately.
   - Write outputs to `output/[filename-without-extension]/`.

3. **Project mode** — if there are subfolders inside `input/`:
   - Each subfolder is a research project containing multiple interviews.
   - All transcripts inside the same subfolder share a single cumulative codebook.
   - Follow the multi-interview workflow from `${CLAUDE_PLUGIN_ROOT}/skills/content-analysis/references/multi-interview-guide.md`.
   - Write outputs to `output/[subfolder-name]/`.

4. **Mixed** — standalone files and project folders can coexist. Handle each independently.

5. **Empty `input/`** — ask the user to paste or upload the material to be analysed.

## Project Initialization

For each project folder detected in Project mode, run this initialization sequence before starting any analysis.

### Step 1 — Check for existing project description

Look for `input/[project-name]/project-description.md`.

- **If it exists**: read it. This project has been worked on before. Skip to Step 3.
- **If it does not exist**: proceed to Step 2.

### Step 2 — Build project description from materials

Look for `input/[project-name]/materials/`. If the folder exists, read every file inside it. These files may contain any combination of: study background, research questions, interview guide, theoretical framework, participant profiles, or other study materials.

Using the materials, fill in as many of the following fields as possible:

| Field | Description |
|-------|-------------|
| Study name | Title or working name of the research project |
| Purpose & research questions | General aim and specific RQ(s) |
| Theoretical framework | Guiding theory or conceptual model, if any |
| Approach | Qualitative / quantitative / mixed |
| Coding logic | Deductive / inductive / abductive |
| Unit of analysis | What counts as one codeable unit (e.g. speaking turn, paragraph) |
| Participant profile | Who was interviewed: number, background, context (anonymised) |
| Interview guide | Key questions or topic flow used in the interviews |

For any field that cannot be inferred from the materials, ask the user directly before proceeding.

Once all fields are filled, write `input/[project-name]/project-description.md` using this structure:

```
# Project Description — [Study name]

## Purpose & Research Questions
...

## Theoretical Framework
...

## Method
- Approach: ...
- Coding logic: ...
- Unit of analysis: ...

## Participant Profile
...

## Interview Guide
...
```

Confirm the saved file with the user before continuing.

### Step 3 — Check progress

Look for `input/[project-name]/progress.md`.

- **If it exists**: read it. Identify which participants have been fully coded, which are in progress, and what the next step is. Resume from where the project left off.
- **If it does not exist**: create it now with the following structure and leave the status rows empty until analysis begins:

```
# Progress — [Study name]

## Status
| Participant | File | Status | Notes |
|-------------|------|--------|-------|

## Cumulative codebook version
Last updated: —

## Next step
—
```

## Starting the Workflow

Once initialization is complete, clarify with the user any items not already answered by `project-description.md`:

1. The research question
2. The unit of analysis
3. The approach (quantitative, qualitative, or mixed)
4. The coding logic (deductive, inductive, or abductive)

Then proceed through the full eight-step workflow: codebook development, pilot coding, reliability assessment, full coding, and reporting.

## Output Structure

### Per-participant outputs

For each transcript, write outputs to `output/[project-name]/[participant-name]/`:
- Codebook → `codebook_[participant].xlsx`
- Coded data → `coded_data_[participant].xlsx`
- Frequency report → `frequency_report_[participant].xlsx`
- Theme summary → `theme_summary_[participant].md`
- Thematic map → `thematic_map_[participant].mermaid`

For standalone files (no named participant subfolder), write to `output/[project-name]/[filename-without-extension]/` using the same file naming pattern.

### Project-level outputs (Project mode only)

Maintain these files at `output/[project-name]/` root. Update them after each participant is coded:

- `codebook_[project].xlsx` — cumulative codebook merging all participant codes; grows with each new interview
- `frequency_report_[project].xlsx` — participant × code matrix showing which codes appear in which interviews and how often

Write these files only after all participants are coded:

- `theme_summary_[project].md` — cross-participant theme analysis identifying patterns across the corpus
- `thematic_map_[project].mermaid` — project-level thematic map

### Progress updates

After completing each participant, update `input/[project-name]/progress.md`:
- Mark the participant as completed
- Note any new codes added to the cumulative codebook
- Record the next step

$ARGUMENTS
