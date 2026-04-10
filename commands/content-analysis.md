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

## Starting the Workflow

Once the corpus is identified, clarify with the user:

1. The research question
2. The unit of analysis
3. The approach (quantitative, qualitative, or mixed)
4. The coding logic (deductive, inductive, or abductive)

Then proceed through the full eight-step workflow: codebook development, pilot coding, reliability assessment, full coding, and reporting.

Produce all outputs as structured files in the appropriate `output/` subfolder:
- Codebook → `.xlsx`
- Coded data → `.xlsx`
- Frequency report → `.xlsx`
- Theme summary → `.md`
- Thematic map → `.mermaid`

$ARGUMENTS
