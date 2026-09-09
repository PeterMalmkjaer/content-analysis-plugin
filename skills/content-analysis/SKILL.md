---
name: content-analysis
description: "Systematic scientific content analysis of textual material. Use this skill whenever the user wants to: code or categorize text data (interview transcripts, documents, reports, media articles, survey responses, social media posts); develop a coding scheme or codebook; perform thematic analysis; count category frequencies in a corpus; assess inter-coder reliability; or conduct any form of qualitative or quantitative content analysis. Also trigger when the user mentions 'Use Content analysis', 'content analysis', 'coding scheme', 'codebook', 'thematic analysis', 'code the data', 'categorize these texts', 'qualitative coding', 'frequency analysis of themes', or 'inter-coder reliability'. This skill produces structured output files: codebooks (.xlsx), coded data tables, frequency reports, and theme summaries."
---

# Scientific Content Analysis

This skill enables the assistant to perform rigorous, methodologically grounded content analysis following established social-science conventions (Krippendorff, 2018; Hsieh & Shannon, 2005; Mayring, 2014; Braun & Clarke, 2006). It supports the full workflow from research question to coded output, for both qualitative and quantitative approaches.

## When to Use This Skill

Content analysis is appropriate when the user has a corpus of textual (or visual/audio-transcribed) material and wants to systematically describe, categorize, or quantify its content. Common scenarios:

- Coding interview transcripts for a qualitative study
- Categorizing policy documents or annual reports by theme
- Counting how often specific topics appear in media coverage
- Developing a codebook from scratch (inductive) or applying an existing framework (deductive)
- Combining coding approaches in a mixed-methods design
- Producing publication-ready coded output tables

## Workflow Overview

Every content analysis follows this sequence. Steps can be revisited iteratively.

```
1. Clarify research question, unit of analysis & source declaration
2. Select approach (quantitative / qualitative / mixed)
3. Select coding logic (deductive / inductive / abductive)
4. Develop or apply coding scheme
5. Pilot-code a sample
6. Assess reliability (if applicable)
7. Code the full corpus
8. Analyze and report
```

---

## Step 1: Clarify the Research Question, Unit of Analysis & Sources

> **If the task arrived as a written brief, protocol, or unattended/scheduled run rather than as a live conversation, read `references/protocol-driven-runs.md` before continuing.** It covers deriving the research question when the brief does not state one, the required report skeleton, and how a brief's own deliverable and format requirements take precedence over the conventions below. For the source declaration in an unattended run, fill what the brief and the files support and record the rest as `unknown`.

Before touching any text, establish three things with the user:

**Research question.** What is the analysis trying to answer? The RQ determines everything downstream — the approach, the categories, and the level of inference. If the user's RQ is vague, help sharpen it. A good content-analysis RQ typically asks "what", "how often", or "in what way" rather than "why" (causal questions require different methods).

**Unit of analysis.** What chunk of text counts as one "case" to be coded? Common units:

| Unit | When to use |
|------|-------------|
| Word / phrase | Frequency counts, dictionary-based analysis |
| Sentence | Fine-grained semantic coding |
| Paragraph | Thematic coding of longer texts |
| Document section | Structured texts (e.g., annual report sections) |
| Whole document | When each document gets one or few codes |
| Speaking turn | Interview / focus group transcripts |
| Answer (all turns replying to one question) | Semi-structured interviews; matches the elicitation structure |

Ask the user to specify the unit. If they are unsure, recommend the unit that best matches their RQ and material.

The unit determines the size of the job more than the number of documents does. Thirty interviews coded at speaking-turn level may yield 4,000 units; at answer level, perhaps 900. Choose the unit with the research question, but choose it knowing what it implies for volume — this is the decision that makes a large corpus manageable or not, and it is taken here, before the volume becomes a problem in Step 7.

**Source declaration.** Content analysis infers from text to the context of its use (Krippendorff, 2018) — including who produced it and for whom — so that context must be stated, not assumed. For every source — or every homogeneous group of sources — record: source type, producer, purpose, audience, whether the text was *elicited* by a researcher or *naturally occurring*, date, language, sampling, and completeness. Unknowns are recorded as `unknown`; they are limitations, not blanks. Part of the declaration (source type, producer, elicitation, date, language) travels with every coded unit as provenance columns, alongside the per-unit Prompting and Parent / section columns (Step 7); the rest is recorded in the corpus manifest and the method note.

Source type moves four things: the natural unit, the coding logic that fits, the reliability you can expect, and the traps to watch for. An interview answer is a response to a specific question and must be read against it; an annual-report paragraph may be boilerplate repeated year on year; a user comment is meaningless without its parent in the thread. **Read `references/source-types.md`** when the corpus is anything other than a single set of documents of one kind, or when the user cannot say who produced the text and for whom.

**Heterogeneity gate.** If the corpus mixes source types, ask before Step 4: *can the unit of analysis be defined in the same way across all sources?* If not, the corpus is not one corpus. Stratify by source type, code each stratum under the same codebook with genre-aware inclusion criteria, and compare across strata rather than pooling. Never pool frequencies across genres without normalizing. Say this to the user before coding, not after.

---

## Step 2: Select the Approach

### Quantitative Content Analysis
- Converts text into numerical data via predefined categories
- Counts frequencies, computes proportions, enables statistical testing
- Prioritizes reliability (replicability) over depth
- Output: frequency tables, cross-tabulations, statistical summaries

### Qualitative Content Analysis
- Focuses on meaning, themes, latent content, and interpretation
- Categories may emerge from the data (inductive) or be refined iteratively
- Three established variants (Hsieh & Shannon, 2005):
  - **Conventional**: Categories derived entirely from data; no preconceptions
  - **Directed**: Start with existing theory, extend/refine with data
  - **Summative**: Count keywords, then interpret underlying meaning
- Output: theme descriptions, coded excerpts, thematic maps

### Mixed Approach
- Combines frequency counts with thematic interpretation
- Often: quantitative overview first, then qualitative deep-dive on key categories
- Output: frequencies plus narrative theme descriptions with illustrative quotes

When the user hasn't specified, ask which approach fits their research question. Offer the trade-offs: quantitative gives breadth and replicability; qualitative gives depth and nuance; mixed gives both at cost of complexity.

---

## Step 3: Select the Coding Logic

### Deductive Coding (Theory-Driven)
- Start with a predefined framework, taxonomy, or set of categories from existing literature
- The user provides (or the assistant helps identify) the theoretical framework
- Categories are fixed before coding begins; the analyst applies them to the data
- Strength: directly tests or applies existing theory
- Risk: may miss themes not anticipated by the framework

### Inductive Coding (Data-Driven)
- Categories emerge from close reading of the material
- No predefined categories; the analyst reads, labels, groups, and abstracts
- Follows an iterative process: open coding → axial coding → selective coding
- Strength: captures what is actually in the data
- Risk: labour-intensive; harder to achieve reliability

### Abductive Coding (Combined)
- Start with a loose theoretical lens, but remain open to unexpected themes
- Move back and forth between theory and data
- Strength: balances sensitivity to data with theoretical grounding
- Common in practice and recommended when neither pure deductive nor pure inductive fits

---

## Step 4: Develop the Coding Scheme

The coding scheme (codebook) is the backbone of the analysis. It must be unambiguous enough that a second coder could apply it consistently.

### Codebook Structure

Every codebook produced by this skill should contain these columns:

| Column | Description |
|--------|-------------|
| **Code ID** | Short unique identifier (e.g., `ENV_RISK_01`) |
| **Code name** | Descriptive label (e.g., "Environmental risk disclosure") |
| **Definition** | Precise description of what the code captures |
| **Inclusion criteria** | What counts — with concrete examples from the data |
| **Exclusion criteria** | What does NOT count — boundary cases |
| **Example excerpt** | A verbatim quote from the material that exemplifies the code |
| **Parent category** | Higher-level grouping, if hierarchical |
| **Status** | `active` / `inactive` — codes are never deleted (Step 7.1) |

### For Deductive Coding
1. Ask the user for the theoretical framework or provide candidate frameworks from literature
2. Translate framework constructs into operational codes with definitions
3. Add inclusion/exclusion criteria and example excerpts from a pilot read
4. Present the draft codebook to the user for review before coding

### For Inductive Coding
1. Read through a sample of the material (10–20% of corpus or at least 3–5 documents)
2. Generate initial codes close to the data (open coding)
3. Group related codes into higher-level categories (axial coding)
4. Refine definitions, merge overlapping codes, split ambiguous ones
5. Present the emergent codebook to the user for discussion and refinement

### Codebook Output Format
Generate the codebook as an Excel file (.xlsx) with professional formatting: bold header row, column widths sized to content, and frozen header row. The codebook should be a clean table that the user can share with co-coders or include as an appendix in a paper.

---

## Step 5: Pilot-Code a Sample

Before coding the full corpus, pilot-code a small sample to test the codebook.

1. Select 2–3 documents (or 10% of the corpus, whichever is smaller)
2. Apply the coding scheme systematically, unit by unit
3. Flag any ambiguities: codes that overlap, units that don't fit any code, definitions that are too vague
4. Report the pilot results to the user with specific suggestions for codebook revision
5. Revise the codebook and re-pilot if needed

This step is critical for quality. Skipping it produces unreliable results.

---

## Step 6: Assess Reliability

Reliability matters most for quantitative and mixed approaches, and for any study where the user plans to report inter-coder agreement.

### When the assistant is the sole coder
Since the assistant is a single "coder," traditional inter-coder reliability (ICR) cannot be computed in the usual sense. Instead:
- **Intra-coder consistency**: Code the same sample twice (at different points in the session) and compare
- **Transparency**: Document every coding decision with the exact text excerpt and the reasoning
- **Codebook precision**: The more precise the codebook, the more replicable the coding

### When the user has human coders
If the user intends to use the codebook with human coders, the assistant should:
- Produce a codebook clear enough for independent application
- Suggest an ICR metric appropriate to the data:
  - **Cohen's kappa (κ)**: Two coders, nominal categories
  - **Fleiss' kappa**: Multiple coders, nominal categories
  - **Krippendorff's alpha (α)**: Any number of coders, any measurement level — generally recommended
  - **Percentage agreement**: Simple but inflated by chance; report alongside kappa/alpha, not alone
- Provide a reliability assessment template (see `references/reliability-guide.md`)

### Acceptable thresholds (Krippendorff, 2018)
- α ≥ 0.800: reliable for most purposes
- 0.667 ≤ α < 0.800: acceptable for exploratory research; report the limitation
- α < 0.667: problematic; revise the codebook and retrain coders

---

## Step 7: Code the Full Corpus

Apply the coding scheme to all material. For each unit of analysis:

1. Identify the unit boundary
2. Read the unit in context (surrounding text matters for interpretation — for elicited text, the question that produced the answer is part of the context)
3. Assign one or more codes from the codebook
4. Record the verbatim excerpt that justifies the code assignment
5. If a unit fits no existing code, assign `UNCODED` and write a candidate entry (7.3; for a small corpus coded in one pass, a note in Coder notes suffices) — do not invent a code on the spot

Small corpora (a handful of documents that fit comfortably in one session) can be coded in a single pass. Anything larger — a dozen interviews, thirty reports, a year of press coverage — needs 7.1–7.5. The procedure exists for one reason: with many documents, coding decisions drift. A code applied to document 1 is not the code applied to document 28 unless something holds it in place.

### 7.1 Freeze the codebook per pass

Before the first full-corpus pass, write the codebook to file and stamp it with a version (`v1`). During a pass, the codebook does not change. New codes, merges, splits and redefinitions are recorded in the candidate log (7.3) and adopted only *between* passes, producing `v2`, `v3`, and so on. Codes are never deleted: a code that turns out to be unusable is marked `inactive` in the codebook so the audit trail survives.

Every coded unit carries the version it was coded under. That one column is what makes a partial re-code both permissible and auditable.

Keep a version log as a `version_log` sheet in the codebook workbook:

| Version | Date | Change | Triggered by |
|---------|------|--------|--------------|
| v1 | YYYY-MM-DD | Codebook frozen after pilot and reliability check (Steps 5–6) | — |
| v2 | YYYY-MM-DD | Added `NETWORK_01`; broadened `BARR_03` to include institutional gatekeeping | Candidates C-04, C-07 (documents 12, 19) |

### 7.2 Batch the corpus

Never read the whole corpus into one working context; never split a document across batches.

1. Build a **corpus manifest** before coding starts: one row per document, in a fixed order, with at least `Document ID`, `Source file`, `Source type`, `Units`, `Status`, `Coded under`, plus any document-level metadata that `references/source-types.md` calls for (participant role, time point, interviewer, outlet, respondent variables). This is the coverage record — how you, and a reviewer, can see that every document was coded, and under which version.
2. Choose a batch size (typically 3–5 interview transcripts, or whatever keeps a batch well within working context) and state it in the method note.
3. For each batch, carry forward only the frozen codebook and the coded-data workbook (coded data, manifest, candidate log — see Output). Do **not** carry forward the raw text of earlier batches.
4. After each batch, update the manifest. A run that stops can be resumed from the manifest without re-coding anything.

### 7.3 Keep a candidate log

The candidate log is a deliverable, not a wastebasket. One row per proposed change:

| Column | Description |
|--------|-------------|
| **Candidate ID** | Sequential (`C-01`, …) |
| **Type** | `new code` / `merge` / `split` / `redefine` |
| **Trigger units** | Document and unit IDs where the need arose |
| **Proposed definition** | As it would appear in the codebook |
| **Decision** | Filled in between passes: `adopt` / `reject` / `defer`, with reason |

In directed content analysis (Hsieh & Shannon) the candidate log *is* the theory-extension result — the material the prior framework could not accommodate. Report it as a finding, not as housekeeping.

### 7.4 Decide, then re-code — how much depends on the coding logic

At the end of a pass, review the candidate log with the user and decide each entry. If anything is adopted, issue a new codebook version and run a second pass over the documents coded under the old version.

| Design (approach × coding logic) | Passes to expect | What the second pass does |
|---|---|---|
| Deductive, quantitative (fixed instrument; reliability reported) | 1 | None. The codebook was fixed before coding; candidates are reported as limitations, not adopted mid-study. |
| Deductive, directed (Hsieh & Shannon) / Mayring structuring | 2 | Adopt the candidates that extend the framework; re-code all documents against `v2`. |
| Abductive | 2–3 | As above, iterated until a pass ends with an empty candidate log or only `defer`. |
| Inductive (conventional, or grounded-theory style) | 2+ | Every document coded before the last revision is re-coded against it (constant-comparison logic). Budget for this before starting. |

For inductive and abductive designs, track saturation as new candidates proposed per document (7.3) and candidates adopted per pass. A common heuristic is that saturation is approaching when two or three consecutive documents yield no new candidates; report the counts, and state it as a heuristic, not a rule. For a closed corpus, saturation is assessed after the fact, not used as a stopping rule.

The cost of the second pass is the method's cost, not the batching's. What batching adds is the ability to prove which documents were coded under which version.

### 7.5 Check for drift

Once the final pass is complete, re-code one document from the *first* batch without looking at its earlier coding, and compare. This is the intra-coder check from Step 6, reused as a scale check. Report α (or Cohen's κ, since two codings are compared) and compare it to the Step 6 thresholds; percent agreement may be reported alongside but is not the criterion. If agreement falls below threshold, treat the first batches as suspect and re-code them.

### Output: Coded Data Table

Produce an Excel file (.xlsx) with these columns:

| Column | Description |
|--------|-------------|
| **Document ID** | Identifier for the source document |
| **Unit ID** | Sequential number within document |
| **Source type** | From the source declaration (Step 1) |
| **Producer** | Role or organization, from the source declaration |
| **Elicitation** | `elicited` / `naturally occurring` (source level) |
| **Prompting** | For elicited text: `prompted` / `volunteered` per unit; otherwise `n/a` |
| **Date** | Of production |
| **Parent / section** | Thread parent ID, document section title, or the interview question that produced the answer |
| **Language** | Original; `translated` if coded in translation |
| **Text excerpt** | The verbatim unit of analysis |
| **Code ID(s)** | Assigned code(s) from the codebook, or `UNCODED` |
| **Code name(s)** | Human-readable label(s) |
| **Codebook version** | The version the unit was coded under (7.1) |
| **Pass** | 1, 2, … |
| **Coder notes** | Any ambiguity, context, or reasoning |

When the corpus has a single homogeneous source, the provenance columns are constant — keep them; the method note is derived from them. For a small corpus coded in one pass, `Codebook version` is `v1` and `Pass` is `1`.

For any corpus coded in batches, also produce, as sheets in the same workbook:

- the **corpus manifest** (7.2)
- the **candidate log** (7.3)
- a **summary sheet** with code frequencies (absolute and percentage), a code co-occurrence matrix, and distribution across documents — reported *per source type* when the corpus mixes types, never pooled across genres without normalizing

### Report the procedure

The method note (see Methodological Transparency) states: batch size; number of passes; codebook versions and what changed between them; the number of `UNCODED` units at the end and how they were handled; the drift-check result; and, for a heterogeneous corpus, how strata were compared. If a document was coded under an earlier version and not re-coded, say so and say why.

---

## Step 8: Analyze and Report

### Quantitative Reporting
- Frequency table: codes ranked by count, with percentages
- Cross-tabulation: codes × documents (or codes × time periods, categories, etc.)
- Visualizations: bar charts of category frequencies, heatmaps of co-occurrence
- Statistical tests if appropriate (chi-square for category differences, etc.)

### Qualitative Reporting
- Theme descriptions: for each major theme, write a narrative paragraph with:
  - Definition of the theme
  - How it manifests in the data (with illustrative quotes)
  - Connections to other themes
  - Relationship to existing literature (if deductive)
- Thematic map: a visual representation of themes and sub-themes (produce as a Mermaid diagram or structured outline)

### Mixed Reporting
- Lead with quantitative overview (frequencies, key patterns)
- Follow with qualitative deep-dives on the most prominent or theoretically interesting themes
- Integrate: use frequencies to contextualize qualitative findings and vice versa

---

## Output File Conventions

All structured outputs should be saved to the workspace output directory.

| Output | Format | Naming convention |
|--------|--------|-------------------|
| Codebook | .xlsx | `codebook_[project-name].xlsx` |
| Coded data | .xlsx | `coded_data_[project-name].xlsx` |
| Frequency report | .xlsx | `frequency_report_[project-name].xlsx` |
| Theme summary | .md or .docx | `theme_summary_[project-name].md` |
| Thematic map | .mermaid or .svg | `thematic_map_[project-name].mermaid` |
| Reliability report | .xlsx | `reliability_[project-name].xlsx` |

For corpora coded in batches, the coded-data workbook also contains the sheets `manifest`, `candidate_log` and `summary` (Step 7); the codebook workbook contains a `version_log` sheet (7.1). For corpora with more than one source type, produce the frequency report and theme summary per stratum, plus a comparative summary `theme_summary_[project-name]_CROSS.md` that states which themes are shared across source types and which are specific to one.

When producing Excel files, apply professional formatting: bold headers, appropriate column widths, frozen header row, and zebra-striping for readability where helpful.
When producing Word documents, use clear heading hierarchy (Heading 1 for main sections, Heading 2 for sub-sections), consistent paragraph spacing, and a final references section.

---

## Methodological Transparency

Every content analysis produced with this skill should include a brief **method note** documenting:

1. Research question
2. Corpus description (number and type of documents, time period, source) and the source declaration per source type (see `references/source-types.md`, Reporting)
3. Unit of analysis
4. Approach (quantitative / qualitative / mixed)
5. Coding logic (deductive / inductive / abductive) and theoretical framework if deductive
6. Codebook development process, and — for corpora coded in batches — batch size, number of passes, codebook versions and what changed between them, `UNCODED` handling, and the drift-check result (Step 7)
7. Reliability assessment (if applicable) or explanation of why not
8. Limitations (single coder, LLM-assisted coding, corpus size)

This note can be appended to the theme summary or produced as a standalone section. It is essential for academic credibility — reviewers and readers need to evaluate the rigor of the analysis.

---

## Important Considerations for LLM-Assisted Content Analysis

The assistant should be transparent about what LLM-assisted content analysis can and cannot do:

**Strengths of LLM-assisted coding:**
- Consistency within a working context: The assistant applies the codebook uniformly to the material in front of it (no coder fatigue). Across a large corpus, consistency is not a property but a procedure — it is controlled by Step 7 (7.1–7.5), not assumed
- Speed: large corpora can be coded much faster than by human coders
- Documentation: every coding decision can be traced to a specific excerpt and rationale

**Limitations to acknowledge:**
- Latent content: subtle irony, sarcasm, cultural subtext, and implicit meaning may be missed
- Context dependence: The assistant's interpretation depends on the text provided; it does not have the ethnographic or field knowledge a human researcher brings
- Validation: LLM-coded results should ideally be validated against a human-coded subsample
- Reproducibility: different LLM versions or prompting strategies may produce different results; document the model and approach used

When reporting LLM-assisted content analysis in an academic paper, recommend that the user:
- Describe the LLM and version used
- Report the codebook in full (as an appendix)
- Validate a subsample against human coding and report agreement
- Discuss LLM-specific limitations in the methods section

---

## References for Further Reading

For detailed guidance on specific topics, consult:

- `references/reliability-guide.md` — Formulas and worked examples for Cohen's κ, Fleiss' κ, Krippendorff's α, and percentage agreement
- `references/coding-approaches.md` — Detailed comparison of Mayring's, Hsieh & Shannon's, and Braun & Clarke's frameworks with decision criteria
- `references/source-types.md` — The source declaration; how interviews, institutional documents, media, user-generated content, survey responses, naturally occurring records and continuous prose differ in unit, coding logic, reliability and traps; the heterogeneity gate; provenance columns
- `references/protocol-driven-runs.md` — Rules for analyses commissioned in writing or run unattended: deriving the research question, the full report skeleton, format precedence, and not blocking on unanswerable questions

### Key Methodological Sources
- Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology* (4th ed.). Sage.
- Hsieh, H.-F., & Shannon, S. E. (2005). Three approaches to qualitative content analysis. *Qualitative Health Research*, 15(9), 1277–1288.
- Mayring, P. (2014). *Qualitative Content Analysis: Theoretical Foundation, Basic Procedures and Software Solution*. Klagenfurt.
- Schreier, M. (2012). *Qualitative Content Analysis in Practice*. Sage.
- Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77–101.
- Neuendorf, K. A. (2017). *The Content Analysis Guidebook* (2nd ed.). Sage.
