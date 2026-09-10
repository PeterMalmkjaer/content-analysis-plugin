---
name: content-analysis
description: "Systematic scientific content analysis of textual material. Use this skill whenever the user wants to: code or categorize text data (interview transcripts, documents, reports, media articles, survey responses, social media posts); develop a coding scheme or codebook; perform thematic analysis; count category frequencies in a corpus; assess inter-coder reliability; or conduct any form of qualitative or quantitative content analysis. Also trigger when the user mentions 'Use Content analysis', 'content analysis', 'coding scheme', 'codebook', 'thematic analysis', 'code the data', 'categorize these texts', 'qualitative coding', 'frequency analysis of themes', or 'inter-coder reliability'. This skill produces structured output files: codebooks (.xlsx), coded data tables, frequency reports, and theme summaries."
---

# Scientific Content Analysis

This skill enables the assistant to perform rigorous, methodologically grounded content analysis following established content-analysis conventions (Krippendorff, 2018; Hsieh & Shannon, 2005; Mayring, 2014). Where the user wants thematic coding with a codebook, the workflow is a *codebook* thematic analysis in the sense of Braun & Clarke (2021); it does not implement Braun & Clarke's reflexive TA (see Step 2, Scope). It supports the full workflow from research question to coded output, for both qualitative and quantitative approaches.

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
   5b. Calibrate against human coding (where it exists) and freeze the codebook
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

**Source declaration.** Content analysis infers from text to the context of its use (Krippendorff, 2018) — including who produced it and for whom — so that context must be stated, not assumed. For every source — or every homogeneous group of sources — record: source type, producer, purpose, audience, whether the text was *elicited* by a researcher or *naturally occurring*, date, language, sampling, and completeness. Unknowns are recorded as `unknown`; they are limitations, not blanks. Part of the declaration (source type, producer, elicitation, date, language) travels with every coded unit as provenance columns, alongside the per-assignment Prompting and Parent / section columns (Step 7); the rest is recorded in the corpus manifest and the method note.

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

### Scope: what this skill is, and is not

This skill is a **content-analysis** instrument: it builds or applies a codebook, codes units against it, and — where the design calls for it — measures agreement. That covers quantitative, qualitative and mixed approaches, and it covers deductive, inductive and abductive coding logics equally (Step 3): an inductive codebook developed from the data is still a codebook; Mayring's inductive category development includes a reliability check, and conventional content analysis (Hsieh & Shannon) is compatible with one.

What it does **not** cover is *reflexive* thematic analysis. Braun & Clarke (2019, p. 593) sort thematic analysis into three clusters — *coding reliability*, *codebook* and *reflexive* TA — and place their own 2006 approach in the third. Of reflexive TA they write that demonstrating coding reliability "is illogical, incoherent and ultimately meaningless in a qualitative paradigm and in reflexive TA" (2021, p. 334), and that they are "critical of" codebooks, consensus coding and coding-reliability measures as practices for it (2021, p. 336). This skill therefore maps onto their typology as follows: **coding-reliability TA** fits the whole workflow; **codebook TA** (template analysis, framework analysis) fits Steps 4–8, but in that tradition "consensus between coders and inter-rater reliability are not usually measures of quality" (2021, p. 333), so Step 6 is optional there and should be reported as a design choice, not a requirement; **reflexive TA** does not fit. If the user wants reflexive TA, say that this skill is the wrong instrument and stop; do not adapt Steps 5–6 to it, and do not report κ or α for a reflexive design. Do not cite Braun & Clarke (2006) as the authority for a codebook-and-agreement procedure; they ask not to be cited for practices they do not advocate (2021, p. 336).

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

All three logics run through the same Steps 4–8. Where they differ is stated where it matters: the origin of the codebook (Step 4), the number of passes and what a second pass does (Step 7.4), and whether candidates are adopted or reported as limitations (Step 7.3). Nothing below assumes one logic unless it says so.

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
| **Required textual basis** | What the unit must actually *express* for the code to apply — the minimum evidence, stated so that a coder can check it against the excerpt (e.g. "the speaker names a concrete resource or person that helped", not "the speaker had a positive experience") |
| **Nearest alternative codes** | The one to three codes this one is most often confused with |
| **Decisive difference** | The single criterion that settles the choice between this code and each nearest alternative |
| **Boundary example** | A verbatim excerpt that *almost* qualifies but must be rejected, with one line saying why |
| **Co-coding rule** | When this code may be assigned together with others on the same unit, and which combinations are excluded (for instance, a neutral code excludes every valenced code; a dependent code requires its gate) |
| **Gate** | If the code may only be assigned when another code applies first, name that code (Step 7, "Gated codes"); otherwise blank |
| **Parent category** | Higher-level grouping, if hierarchical |
| **Origin** | Abductive designs only: `theory` / `data` / `both` — what the framework did and did not anticipate |
| **Status** | `active` / `inactive` — codes are never deleted (Step 7.1) |

The first three columns define the code; the next five are its **decision rules** (Krippendorff, 2018: a category is defined as much by what it excludes as by what it includes). They are what the coder consults at the moment of choice (Step 7), and they are what the calibration in Step 5b revises. *Required textual basis* and *Co-coding rule* are filled for every code. *Nearest alternative codes*, *Decisive difference* and *Boundary example* are mandatory wherever the pilot or the calibration shows confusion, and may otherwise stay blank — a blank there is itself a claim that the code is not confused with any other, and the calibration will test it. Confusion typically appears between a broad code and a specific one (for instance an experience code against a concrete support or infrastructure code), between a superordinate and a subordinate category, and between adjacent categories on the same scale (in an emotion codebook, for instance, *disapproval* / *annoyance* / *anger*, and any of them against a neutral or residual code).

**Where the examples come from.** Example excerpts and boundary examples are taken from the development material (the Step 4 read, the pilot, and the calibration set after it has been analysed) or written by the analyst and marked as constructed. They are **never** taken from a held-out test set, and a test set that has supplied an example is no longer a test set.

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

### For Abductive Coding
1. Start from a loose framework: list the constructs the theory suggests, with provisional definitions
2. Read a sample as in inductive coding; keep every code that the framework did not predict
3. Build one codebook that marks each code's origin (`theory` / `data` / `both`) — the origin column is what lets the report say what the framework did and did not anticipate
4. Present the draft to the user; expect it to change between passes (Step 7.4), and record every change in the version log

### Codebook Output Format
Generate the codebook as an Excel file (.xlsx) with professional formatting: bold header row, column widths sized to content, and frozen header row. The codebook should be a clean table that the user can share with co-coders or include as an appendix in a paper.

---

## Step 5: Pilot-Code a Sample

Before coding the full corpus, pilot-code a small sample to test the codebook.

1. Select the pilot so that it is large enough to expose ambiguity and varied enough to expose source effects: at least 3 documents (or all documents, if the corpus has fewer) **and** at least 10% of the corpus's units (minimum 50 units); every source type in the corpus, and every group the design compares, must be represented. A corpus of fewer than 50 units is piloted in full. Where the corpus allows, pilot on documents that were *not* used to develop the codebook in Step 4 — the pilot tests the codebook on material it was not built from.
2. Apply the coding scheme systematically, unit by unit
3. Flag any ambiguities: codes that overlap, units that don't fit any code, definitions that are too vague
4. Report the pilot results to the user with specific suggestions for codebook revision
5. Revise the codebook and re-pilot if needed

This step is critical for quality. Skipping it produces unreliable results.

---

## Step 5b: Calibrate Against Human Coding Before Freezing the Codebook

Agreement between repeated AI codings (Step 6, "Intra-coder consistency") shows that the codebook is applied *stably*. It does not show that it is applied *as a human researcher would apply it*: an AI coder can agree closely with itself and still diverge substantially from human coders on the same material. Stability is necessary; it is not validity. Where human-coded material exists or can be produced, the codebook is calibrated against it **before** it is frozen as `v1` (7.1).

1. **Calibration set.** Ask the user for, or have them produce, a set of units coded by at least one human coder — preferably two, coded independently, so that human–human agreement on the same units can be reported as the *ceiling* against which AI–human agreement is read. The set is drawn from the corpus (or from material of the same source type), aims at ten positive instances for every code that matters, and is **separate from any held-out test set** the study will later report on. Codes with fewer than ten positive instances in the calibration set are reported by name as *insufficiently calibrated*: their figures are given, but they are not averaged into the micro- and macro-F1. Record the set's size and origin in the method note.
2. **Code it blind.** Code the calibration set in a separate context (Step 6, "blind") that receives the codebook, the source declaration and the elicitation context but not the human codes.
3. **Measure per code.** For every code, as presence/absence per unit: precision, recall and F1 of the AI coding against the human coding, and per-code α (or κ) treating AI and human as two coders (`references/reliability-guide.md`, "Multiple Codes per Unit"). Report the human–human values alongside where two human coders exist. Report micro- and macro-averages together with the per-code range (min–max); never the mean alone. Where the codebook has gated codes (Step 7), report the gate decision separately from the dependent codes.
4. **Review the disagreements.** List every unit where AI and human differ, grouped by code pair (which code was given, which was expected). For each frequent pair, decide whether the human coding is the standard to move towards or whether the codebook is ambiguous; then revise the **decision-rule columns** of Step 4 (required textual basis, nearest alternatives, decisive difference, boundary example, co-coding rule) — not the definition alone. Every revision is a `redefine` row in the candidate log (7.3) with the trigger units.
5. **Re-test on fresh items.** Apply the revised codebook, blind, to calibration units that were *not* used to motivate the revision (hold part of the set back for this). A revision is kept only if the per-code figures improve on the fresh items; a revision that improves the motivating items alone is over-fitting and is reverted.
6. **Freeze.** Only then is the codebook frozen as `v1`. Record in the version log which calibration round produced it.

**If no human coding exists** and none can be produced, say so before coding, proceed with Steps 5–6, and mark every reliability statement in the report as *not calibrated against human coding*: "AI intra-coder consistency: α = … (not calibrated against human coding)". Do not let a consistency figure stand where a validity figure is expected.

**Protocol agreement.** Before measuring, check that the rules the coder is given match the rules under which the reference was coded: the same unit, the same co-coding rules (a reference that allows *neutral* together with an emotion cannot be scored against a protocol that forbids it), the same treatment of multi-label units, and a stated rule for matching excerpts of different length or boundary. A mismatch here is a measurement error, not a coding error, and it is found by comparing the two protocols on paper before a single unit is scored.

---

## Step 6: Assess Reliability

Reliability matters most for quantitative and mixed approaches, and for any study where the user plans to report inter-coder agreement.

**Multiple codes per unit.** When a unit may carry more than one code — the default in the long-format table — compute agreement **per code as presence/absence** (a binary decision per unit per code) and report per-code α or κ; if one headline figure is wanted, give the mean of the per-code values *and* their range, never the mean alone. Rare codes have few positives and unstable per-code values — say so where it applies. Do not force one category per unit. State the denominator of every percentage: assignments, units, or documents (see `references/reliability-guide.md`, "Multiple Codes per Unit"). This applies to the sole-coder checks below as much as to human coders.

### When the assistant is the sole coder
Since the assistant is a single "coder," traditional inter-coder reliability (ICR) cannot be computed in the usual sense. Instead:
- **Intra-coder consistency**: Code the same sample twice and compare. The second coding must be **blind**: run it in a separate context that receives the same inputs as the first coding — the text, the frozen codebook, the source declaration and the elicitation context (interview guide, section titles) — but **not** the earlier coding: a fresh session, a subagent, or a scripted call, never the conversation where the first coding is visible. "Not looking" at an earlier coding that is already in the working context is not a control. Report the result as *consistency of AI coding*, not as reliability.
- **Human comparison**: Agreement between the assistant's coding and a human coder's is a different quantity from the above; if both are reported, keep them separate and label them. Where it can be measured, it is measured *before* the codebook is frozen (Step 5b); intra-coder consistency never substitutes for it.
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

Apply the coding scheme to all material. For each unit of analysis, follow the **decision procedure** below. It is deliberately stepwise: "read the unit and assign codes" leaves the choice to impression, and impression is where coders — human or AI — drift towards the broad code and away from the specific one.

1. **Bound the unit.** Identify the unit boundary.
2. **Read in context.** Surrounding text matters for interpretation — for elicited text, the question that produced the answer is part of the context.
3. **Locate the passage.** For each code you are considering, find the exact passage that would carry it. No passage, no code.
4. **Check the criteria.** Test the passage against the code's inclusion and exclusion criteria and its *required textual basis* (Step 4). Does the text express what the code requires, or does it merely make it plausible?
5. **Compare with the nearest alternatives.** Consult the code's *nearest alternative codes* and *decisive difference*. Three outcomes: if the decisive criterion settles the choice, assign the code it points to; if it settles the choice only narrowly, assign that code and set `Review = competing_codes`; if it settles nothing, assign neither and go to step 8.
6. **Assign and record.** Assign the code only if steps 4–5 are satisfied; record the verbatim excerpt and apply the *co-coding rule* to anything already assigned to the unit.
7. **Sweep for omissions.** Before leaving the unit, go through the codebook's *remaining* active codes one by one — not "is there anything else here?", but "does this unit meet *this* code's required textual basis?" Each additional code found this way passes steps 3–6 in full. This step raises recall; the criterion discipline in steps 3–5 keeps it from lowering precision.
8. **Mark what remains.** If a passage seems to carry meaning that no code captures, assign `UNCODED` and write a candidate entry (7.3; for a small corpus coded in one pass, a note in Coder notes suffices) — do not invent a code on the spot. If a code *does* apply but the decision was hard, assign it and set `Review` (see the coded-data table) with the reason; use `other` only when none of the named reasons fits, and say why in Coder notes.

**Gated codes.** When one code may be assigned only if another applies first — for instance *relevant to the topic* before any code describing *how* it is treated, or *disclosure present* before *disclosure type* — the codebook names the gate (Step 4, "Gate"), and the coder decides the gate **first, with its own excerpt**, before considering the dependent codes. A unit that fails the gate receives no dependent code, whatever the dependent passages seem to say. Calibration (Step 5b) and any later reliability report give the gate its own precision and recall: a gate that lets through a third of the non-cases corrupts every dependent field, and the fault must be visible where it arises.

Small corpora (a handful of documents that fit comfortably in one session) can be coded in a single pass. Anything larger — a dozen interviews, thirty reports, a year of press coverage — needs 7.1–7.5. The procedure exists for one reason: with many documents, coding decisions drift. A code applied to document 1 is not the code applied to document 28 unless something holds it in place.

### 7.1 Freeze the codebook per pass

Before the first full-corpus pass, write the codebook to file and stamp it with a version (`v1`). During a pass, the codebook does not change. New codes, merges, splits and redefinitions are recorded in the candidate log (7.3) and adopted only *between* passes, producing `v2`, `v3`, and so on. Codes are never deleted: a code that turns out to be unusable is marked `inactive` in the codebook so the audit trail survives.

Every row of the coded-data table carries the version it was coded under. That one column is what makes a partial re-code both permissible and auditable.

Keep a version log as a `version_log` sheet in the codebook workbook:

| Version | Date | Change | Triggered by |
|---------|------|--------|--------------|
| v1 | YYYY-MM-DD | Codebook frozen after pilot and reliability check (Steps 5–6) | — |
| v2 | YYYY-MM-DD | Added `NETWORK_01`; broadened `BARR_03` to include institutional gatekeeping | Candidates C-04, C-07 (documents 12, 19) |

### 7.2 Batch the corpus

Never read the whole corpus into one working context. Keep each document whole within a batch when it fits; when a single document exceeds the context you can give it, split it at **section or turn boundaries**, never mid-unit, give each part a stable ID in the form `DOC-07.§3` — the form the validator understands —, carry the section title and a short running summary of the preceding parts as context, and list each part as its own row in the manifest with the parent document named. The coded-data workbook lives on disk and is appended to; it is not re-read in full for every batch.

1. Build a **corpus manifest** before coding starts: one row per document or document part, in a fixed order, with at least `Document ID`, `Parent document` (required when any row is a part; blank otherwise), `Source file`, `Source type`, `Units`, `Status`, `Coded under`, plus any document-level metadata that `references/source-types.md` calls for (participant role, time point, interviewer, outlet, respondent variables). This is the coverage record — how you, and a reviewer, can see that every document was coded, and under which version.
2. Choose a batch size (typically 3–5 interview transcripts, or whatever keeps a batch well within working context) and state it in the method note.
3. For each batch, carry forward only the frozen codebook, the manifest and the candidate log; coded rows are appended to the workbook on disk and are not re-read. Do **not** carry forward the raw text of earlier batches. This is enforced by **where the batch is coded, not by intention**: each batch is coded in a *separate context* — a subagent, a fresh session, or a scripted call — that receives the frozen codebook, the source declaration, the manifest, the candidate log and the batch's own text, and nothing else. Coding successive batches in one long conversation, with earlier batches still in the history, does not satisfy this rule, whatever the coder is told to ignore (the same principle as the blind checks in Step 6 and 7.5). The method note states the mechanism used. Where the platform offers no such mechanism, the corpus is coded in one context, the method note says so and states the batch order, and the drift check in 7.5 is mandatory rather than optional.
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

Once the final pass is complete, re-code one document from the *first* batch **in a separate context** that receives the same inputs as the original coding but not the coding itself (a fresh session or a subagent — see Step 6), and compare. This is the blind intra-coder check from Step 6, reused as a scale check. Report α (or Cohen's κ, since two codings are compared) as *consistency*, and use the Step 6 thresholds as a decision rule for re-coding — not as a reliability claim; percent agreement may be reported alongside but is not the criterion. If agreement falls below threshold, treat the first batches as suspect and re-code them.

### Output: Coded Data Table

The table is **long format: one row per code assignment**, not one row per unit. A unit that carries three codes has three rows; a unit that carries none has one row with `UNCODED`. This is what makes per-code reliability, per-assignment prompting, and unambiguous denominators possible.

Produce an Excel file (.xlsx) with these columns:

| Column | Description |
|--------|-------------|
| **Document ID** | Identifier for the source document (or document part, `DOC-07.§3`) |
| **Unit ID** | Sequential number within document |
| **Assignment ID** | Unique across the table (`A-0001`, …) |
| **Source type** | From the source declaration (Step 1) |
| **Producer** | Role or organization, from the source declaration |
| **Elicitation** | `elicited` / `naturally occurring` (source level) |
| **Date** | Of production |
| **Parent / section** | Thread parent ID, document section title, or the interview question that produced the answer |
| **Language** | Original; `translated` if coded in translation |
| **Text excerpt** | The verbatim passage that justifies *this* assignment — it must occur in the source. An `UNCODED` row carries the unit's opening words, so the check is defined for it too |
| **Code ID** | One code from the codebook, or `UNCODED` |
| **Code name** | Human-readable label |
| **Prompting** | For elicited text, per assignment: `prompted` / `volunteered` / `mixed` / `unclear`; otherwise `n/a`. One answer can contain a prompted topic and a volunteered one — they get separate rows and separate values. |
| **Codebook version** | The version this assignment was coded under (7.1) |
| **Pass** | 1, 2, … |
| **Review** | Blank when the decision was clear. Otherwise one of `context_missing` / `possible_irony` / `competing_codes` / `insufficient_basis` / `other` — the assignment stands as the coder's best decision, and the flag says a human should look at it. `other` requires a reason in Coder notes |
| **Coder notes** | Any ambiguity, context, or reasoning; for a `Review` row, which codes competed or what context is missing; for `other`, the reason — a row with `Review = other` and empty notes fails validation |

When the corpus has a single homogeneous source, the provenance columns are constant — keep them; the method note is derived from them. For a small corpus coded in one pass, `Codebook version` is `v1` and `Pass` is `1`.

**Uncertainty is not a code.** "I am not sure" is recorded in `Review`, never by choosing a neutral or residual code (where the codebook has one), `UNCODED`, or the broadest available code as a hedge: a neutral code is a claim about the text, and `UNCODED` is a claim that no code fits. The coder does not output a numeric confidence — a verbalised probability from a language model is not calibrated and must not be read as one. The **review share** (rows with `Review` set, over all assignments and per code) is reported in the summary sheet and the method note next to every quality figure: a coding whose agreement rises because the hard cases were flagged out has not become more accurate, and the reader must be able to see the two numbers together. The share of `other` among the flagged rows is reported separately: when `other` carries a substantial part of the flags — as a rule of thumb, more than a fifth — the reason list is too short for this material, and the recurring reasons in Coder notes become named values in the next codebook version (a `redefine` row in the candidate log). `other` is a signal that the list needs extending, not a permanent home.

**Denominators.** Every percentage in a frequency table states what it is a share of: *assignments* (rows), *units* (distinct Document × Unit), or *documents*. The summary sheet reports all three counts per code so that the reader can choose. Document counts collapse parts (`DOC-07.§3`) to their parent document.

The workbook's sheets are named `coded_data`, `manifest`, `candidate_log` and `summary`; the codebook workbook's sheets are `codebook` and `version_log`. The validator looks them up by these names (case-insensitive). For any corpus coded in batches, also produce, as sheets in the same workbook:

- the **corpus manifest** (7.2)
- the **candidate log** (7.3)
- a **summary sheet** with, per code, the number of assignments, distinct units and distinct documents, the number and share of assignments with `Review` set (and, of those, the share with `other`), a code co-occurrence matrix, and distribution across documents — reported *per source type* when the corpus mixes types, never pooled across genres without normalizing

### Validate the outputs

Where a shell is available, run the validator before reporting (paths relative to the plugin root, `${CLAUDE_PLUGIN_ROOT}`):

```
python3 scripts/validate_coding.py --coded <coded_data> --codebook <codebook> \
    --manifest <manifest> --sources <dir with the source files> --summary <frequencies> \
    --codebook-version <vN>
```

It checks that every excerpt occurs verbatim in its source file, that every document the manifest marks as coded has rows and the unit counts agree, that every Code ID exists in the codebook (inactive codes are flagged), that assignment IDs and (document, unit, code) triples are unique, that Prompting values are allowed, that `Review` values — where the column is present — are from the allowed set, and that the frequency table can be regenerated from the rows. A summary with a `Source type` column is compared per stratum; without one, the pooled per-code sheet is compared. "Verbatim" is exact except for whitespace: runs of spaces, line breaks and non-breaking spaces count as one space, but case, punctuation and quotation marks must match the source. It reads CSV with the standard library and .xlsx if `openpyxl` is installed; it never modifies a file.

The result has three values. `RESULT: PASS` — every check ran and none failed. `RESULT: FAIL` — a `FAIL` line names the assignment, the document, or the code it concerns. `RESULT: INCOMPLETE` — nothing failed, but a required check could not run: no manifest, no `--sources`, no `--summary`, a document with no `Source file` in the manifest, or rows with `Language = translated` (which cannot be matched against the source); `SKIP` lines say which. INCOMPLETE is not a pass. Report the result verbatim in the method note; for FAIL, say what was done about each failure; for INCOMPLETE, either supply what was missing and re-run, or state which check did not run and why. Where no shell is available (some Codex/ChatGPT surfaces), say so in the method note and perform the excerpt and coverage checks by hand on a sample.

`examples/minimal/` is a known-good fixture: the validator must pass on it, and a change to the skill or the validator is checked against it first.

### Report the procedure

The method note (see Methodological Transparency) states: the batch mechanism (subagent / fresh session / scripted call) and batch size; number of passes; codebook versions and what changed between them; the calibration result (Step 5b) or the statement that the coding is not calibrated against human coding; the number of `UNCODED` units at the end and how they were handled; the review share; the drift-check result; and, for a heterogeneous corpus, how strata were compared. If a document was coded under an earlier version and not re-coded, say so and say why.

---

## Step 8: Analyze and Report

### Quantitative Reporting
- Frequency table: codes ranked by count, with percentages and the denominator stated (assignments, units, or documents — Step 7)
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
7. Calibration against human coding (Step 5b): calibration-set size and origin, per-code precision/recall and α, human–human ceiling where available, revisions made — or the explicit statement *not calibrated against human coding*
8. Reliability assessment (if applicable) or explanation of why not, with AI intra-coder consistency and AI–human agreement reported as separate quantities
9. Review share (assignments flagged for human review, overall and per code), reported next to every quality figure
10. Model identifier and version, decoding settings where known (e.g. temperature), and the date of the run
11. Limitations (single coder, LLM-assisted coding, corpus size)

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
- Validation: agreement between repeated LLM codings is *stability*, not *validity*. LLM-coded results are validated against a human-coded subsample before the codebook is frozen (Step 5b) wherever such a sample exists; where it does not, every reliability figure carries the label *not calibrated against human coding*
- Reproducibility: different LLM versions, decoding settings or prompting strategies may produce different results; document the model identifier and version, the decoding settings where known, the date of the run, and the approach used. A claim that a codebook revision "improved" the coding requires the same model and settings on both sides and fresh test items (Step 5b, point 5)

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
- `scripts/validate_coding.py` (plugin root) — Output validator: excerpts in sources, coverage against the manifest, code IDs in the codebook, uniqueness, prompting values, regenerated frequencies
- `examples/minimal/` (plugin root) — Known-good fixture (two interviews, one report, codebook, manifest, long-format coded data, frequencies) on which the validator must pass
- `references/protocol-driven-runs.md` — Rules for analyses commissioned in writing or run unattended: deriving the research question, the full report skeleton, format precedence, and not blocking on unanswerable questions

### Key Methodological Sources
- Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology* (4th ed.). Sage.
- Hsieh, H.-F., & Shannon, S. E. (2005). Three approaches to qualitative content analysis. *Qualitative Health Research*, 15(9), 1277–1288.
- Mayring, P. (2014). *Qualitative Content Analysis: Theoretical Foundation, Basic Procedures and Software Solution*. Klagenfurt.
- Schreier, M. (2012). *Qualitative Content Analysis in Practice*. Sage.
- Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77–101.
- Braun, V., & Clarke, V. (2019). Reflecting on reflexive thematic analysis. *Qualitative Research in Sport, Exercise and Health*, 11(4), 589–597. https://doi.org/10.1080/2159676X.2019.1628806
- Braun, V., & Clarke, V. (2021). One size fits all? What counts as quality practice in (reflexive) thematic analysis? *Qualitative Research in Psychology*, 18(3), 328–352. https://doi.org/10.1080/14780887.2020.1769238
- Neuendorf, K. A. (2017). *The Content Analysis Guidebook* (2nd ed.). Sage.
