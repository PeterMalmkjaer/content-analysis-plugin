---
description: Run a scientific content analysis on uploaded documents
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [documents or instructions]
---

Read the content-analysis skill at ${CLAUDE_PLUGIN_ROOT}/skills/content-analysis/SKILL.md and follow its eight-step workflow.

If the user has provided documents, begin the workflow. If not, ask the user to upload or paste the material to be analysed.

Always start by clarifying:
1. The research question
2. The unit of analysis
3. The approach (quantitative, qualitative, or mixed)
4. The coding logic (deductive, inductive, or abductive)

Then proceed through the full workflow: codebook development, pilot coding, reliability assessment, full coding, and reporting.

Produce all outputs as structured files: codebook (.xlsx), coded data (.xlsx), theme summary (.md or .docx), and thematic map (.mermaid).

$ARGUMENTS
