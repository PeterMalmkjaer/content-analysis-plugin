---
description: Run a scientific content analysis on uploaded documents
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]
argument-hint: "[documents or instructions]"
---

Read the content-analysis skill at ${CLAUDE_PLUGIN_ROOT}/skills/content-analysis/SKILL.md and follow its eight-step workflow.

If the user has provided documents, begin the workflow. If not, ask the user to upload or paste the material to be analysed.

Always start by clarifying:
1. The research question
2. The unit of analysis
3. The approach (quantitative, qualitative, or mixed)
4. The coding logic (deductive, inductive, or abductive)
5. The source declaration: source type, producer, purpose, audience, elicited or naturally occurring, date, sampling

If the task arrived as a written brief or protocol rather than as a conversation, or if the run is unattended, read `${CLAUDE_PLUGIN_ROOT}/skills/content-analysis/references/protocol-driven-runs.md` first: it replaces the five clarification points above with rules for deriving the research question from the brief, and it governs the report structure and output formats.

If the corpus contains more than one source type, or the type is unclear, read `${CLAUDE_PLUGIN_ROOT}/skills/content-analysis/references/source-types.md` before Step 4 and apply its heterogeneity gate. If the corpus is larger than fits in one session, follow Step 7's batching procedure (freeze the codebook per pass, keep a manifest and a candidate log).

Then proceed through the full workflow: codebook development, pilot coding, reliability assessment, full coding, and reporting.

Produce all outputs as structured files: codebook (.xlsx), coded data (.xlsx), theme summary (.md or .docx), and thematic map (.mermaid) — unless a brief names its own deliverables and formats, in which case those take precedence.

$ARGUMENTS
