---
name: content-analysis
description: "Systematic scientific content analysis of textual material. Use this skill whenever the user wants to: code or categorize text data (interview transcripts, documents, reports, media articles, survey responses, social media posts); develop a coding scheme or codebook; perform thematic analysis; count category frequencies in a corpus; assess inter-coder reliability; or conduct any form of qualitative or quantitative content analysis. Also trigger when the user mentions 'Use Content analysis', 'content analysis', 'coding scheme', 'codebook', 'thematic analysis', 'code the data', 'categorize these texts', 'qualitative coding', 'frequency analysis of themes', or 'inter-coder reliability'. This skill produces structured output files: codebooks (.xlsx), coded data tables, frequency reports, and theme summaries."
---

# Scientific Content Analysis

This skill enables Claude to perform rigorous, methodologically grounded content analysis following established social-science conventions (Krippendorff, 2018; Hsieh & Shannon, 2005; Mayring, 2014; Schreier, 2012). It supports the full workflow from research question to coded output, for both qualitative and quantitative approaches.

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
1. Clarify research question & unit of analysis
2. Select approach (quantitative / qualitative / mixed)
3. Select coding logic (deductive / inductive / abductive)
4. Develop or apply coding scheme
5. Pilot-code a sample
6. Assess reliability (if applicable)
7. Code the full corpus
8. Analyze and report
```

---

## Step 1: Clarify the Research Question & Unit of Analysis

Before touching any text, establish two things with the user:

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

Ask the user to specify the unit. If they are unsure, recommend the unit that best matches their RQ and material.

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
- The user provides (or Claude helps identify) the theoretical framework
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
Generate the codebook as an Excel file (.xlsx) using the xlsx skill conventions. The codebook should be a clean, professional table that the user can share with co-coders or include as an appendix in a paper.

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

### When Claude is the sole coder
Since Claude is a single "coder," traditional inter-coder reliability (ICR) cannot be computed in the usual sense. Instead:
- **Intra-coder consistency**: Code the same sample twice (at different points in the session) and compare
- **Transparency**: Document every coding decision with the exact text excerpt and the reasoning
- **Codebook precision**: The more precise the codebook, the more replicable the coding

### When the user has human coders
If the user intends to use the codebook with human coders, Claude should:
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

Apply the finalized coding scheme to all material. For each unit of analysis:

1. Identify the unit boundary
2. Read the unit in context (surrounding text matters for interpretation)
3. Assign one or more codes from the codebook
4. Record the verbatim excerpt that justifies the code assignment
5. If a unit fits no existing code, flag it as "uncoded" and note why

### Output: Coded Data Table

Produce an Excel file (.xlsx) with these columns:

| Column | Description |
|--------|-------------|
| **Document ID** | Identifier for the source document |
| **Unit ID** | Sequential number within document |
| **Text excerpt** | The verbatim unit of analysis |
| **Code ID(s)** | Assigned code(s) from the codebook |
| **Code name(s)** | Human-readable label(s) |
| **Coder notes** | Any ambiguity, context, or reasoning |

If the corpus is large, also produce a **summary sheet** with:
- Code frequencies (absolute count and percentage of total coded units)
- Code co-occurrence matrix (which codes appear together)
- Distribution across documents

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

When producing Excel files, follow the xlsx skill conventions for professional formatting.
When producing Word documents, follow the docx skill conventions.

---

## Methodological Transparency

Every content analysis produced with this skill should include a brief **method note** documenting:

1. Research question
2. Corpus description (number and type of documents, time period, source)
3. Unit of analysis
4. Approach (quantitative / qualitative / mixed)
5. Coding logic (deductive / inductive / abductive) and theoretical framework if deductive
6. Codebook development process
7. Reliability assessment (if applicable) or explanation of why not
8. Limitations (single coder, LLM-assisted coding, corpus size)

This note can be appended to the theme summary or produced as a standalone section. It is essential for academic credibility — reviewers and readers need to evaluate the rigor of the analysis.

---

## Important Considerations for LLM-Assisted Content Analysis

Claude should be transparent about what LLM-assisted content analysis can and cannot do:

**Strengths of LLM-assisted coding:**
- Consistency: Claude applies the same codebook uniformly across the corpus (no coder fatigue)
- Speed: large corpora can be coded much faster than by human coders
- Documentation: every coding decision can be traced to a specific excerpt and rationale

**Limitations to acknowledge:**
- Latent content: subtle irony, sarcasm, cultural subtext, and implicit meaning may be missed
- Context dependence: Claude's interpretation depends on the text provided; it does not have the ethnographic or field knowledge a human researcher brings
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

### Key Methodological Sources
- Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology* (4th ed.). Sage.
- Hsieh, H.-F., & Shannon, S. E. (2005). Three approaches to qualitative content analysis. *Qualitative Health Research*, 15(9), 1277–1288.
- Mayring, P. (2014). *Qualitative Content Analysis: Theoretical Foundation, Basic Procedures and Software Solution*. Klagenfurt.
- Schreier, M. (2012). *Qualitative Content Analysis in Practice*. Sage.
- Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77–101.
- Neuendorf, K. A. (2017). *The Content Analysis Guidebook* (2nd ed.). Sage.
