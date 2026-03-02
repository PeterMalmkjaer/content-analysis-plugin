# Coding Approaches: A Comparative Reference

This reference compares the major frameworks for qualitative content analysis and thematic analysis, with decision criteria for choosing among them.

## Table of Contents

1. [Mayring's Qualitative Content Analysis](#mayrings-qualitative-content-analysis)
2. [Hsieh & Shannon's Three Approaches](#hsieh--shannons-three-approaches)
3. [Braun & Clarke's Thematic Analysis](#braun--clarkes-thematic-analysis)
4. [Comparison Table](#comparison-table)
5. [Decision Guide](#decision-guide)

---

## Mayring's Qualitative Content Analysis

**Source:** Mayring, P. (2014). *Qualitative Content Analysis: Theoretical Foundation, Basic Procedures and Software Solution*. Klagenfurt.

Mayring developed a systematic, rule-governed approach to qualitative content analysis that aims to preserve the strengths of quantitative content analysis (transparency, replicability) while allowing interpretive depth.

### Three core techniques:

**1. Summarizing (Zusammenfassung)**
- Goal: Reduce material to its essential content while preserving core meaning
- Process: Paraphrase → Generalize → Reduce (merge, omit, select, bundle)
- Use when: You need to condense large volumes of text to manageable summaries
- Abstraction levels are defined in advance

**2. Explication (Explikation)**
- Goal: Clarify ambiguous or unclear passages by drawing on context
- Narrow explication: use only the immediate textual context
- Broad explication: use additional material (other documents, background knowledge)
- Use when: Key passages require deeper interpretation

**3. Structuring (Strukturierung)**
- Goal: Extract and systematize aspects of the material using predefined categories
- This is the most commonly used technique and closest to deductive content analysis
- Categories are defined before coding (deductive), applied to the material, and may be revised
- Four sub-types: formal (structure of text), content-based (themes), type-based (typologies), scaling (ordinal assessment)
- Use when: You have a theoretical framework to apply

### Key features:
- Highly systematic with explicit procedural rules
- Category system developed deductively (usually) but can incorporate inductive revision
- Emphasizes step-by-step documentation of the analytical process
- Strong on reliability and transparency

---

## Hsieh & Shannon's Three Approaches

**Source:** Hsieh, H.-F., & Shannon, S. E. (2005). Three approaches to qualitative content analysis. *Qualitative Health Research*, 15(9), 1277–1288.

This framework distinguishes three approaches based on how categories are derived:

### 1. Conventional Content Analysis
- **Category origin:** Categories emerge entirely from the data (inductive)
- **Starting point:** No preconceived categories; immerse in the data
- **Process:** Read repeatedly → Derive codes from the text → Group into categories → Define and name categories
- **Strength:** Grounded in participants' actual words and meanings; avoids imposing external frameworks
- **Weakness:** May miss broader theoretical connections; findings can be too descriptive
- **Best for:** Exploratory research; topics with limited existing theory

### 2. Directed Content Analysis
- **Category origin:** Categories derived from existing theory or prior research (deductive), then extended
- **Starting point:** Identify key concepts from theory → Develop initial coding scheme
- **Process:** Apply predefined codes → Code data that doesn't fit into new categories → Refine framework
- **Strength:** Builds on and extends existing theory; structured starting point
- **Weakness:** Researcher may be biased toward confirming the theory (confirmation bias)
- **Best for:** Testing, extending, or refining an existing theoretical framework

### 3. Summative Content Analysis
- **Category origin:** Keywords identified from the research question or literature
- **Starting point:** Identify keywords → Count occurrences (manifest content) → Interpret patterns (latent content)
- **Process:** Keyword identification → Frequency counts → Contextual interpretation of usage
- **Strength:** Combines quantitative and qualitative elements; starts with concrete data
- **Weakness:** Keywords may be used differently across contexts; counting alone is insufficient
- **Best for:** Understanding how specific concepts are used in a corpus; policy or discourse analysis

---

## Braun & Clarke's Thematic Analysis

**Source:** Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77–101.

Note: Braun & Clarke distinguish thematic analysis (TA) from content analysis, arguing that TA is a method in its own right rather than a subset of content analysis. In practice, there is significant overlap, and many researchers combine elements of both. This framework is included here because it is widely used for thematic coding.

### Six phases:

1. **Familiarization:** Read and re-read the data; note initial ideas
2. **Generating initial codes:** Code interesting features across the entire dataset systematically
3. **Searching for themes:** Collate codes into candidate themes; gather relevant data for each theme
4. **Reviewing themes:** Check themes against coded extracts and full dataset; refine, split, merge, or discard
5. **Defining and naming themes:** Refine the specifics of each theme; generate clear definitions and names
6. **Producing the report:** Final analysis with selected extracts, relating findings to research question and literature

### Key distinctions:

- **Semantic vs. latent themes:** Semantic themes describe surface meaning; latent themes interpret underlying ideas, assumptions, and ideologies
- **Inductive vs. theoretical:** Inductive TA is data-driven; theoretical TA is driven by the researcher's analytical interest
- **Essentialist vs. constructionist:** Epistemological stance shapes how themes are conceptualized — as reflecting reality or as constructed through language

### Key features:
- Flexible: not tied to a specific theoretical framework or epistemology
- Accessible: clear procedural steps, widely taught
- Emphasis on "telling a story" about the data through themes
- Does not inherently involve counting (though frequencies can be reported)

---

## Comparison Table

| Feature | Mayring | Hsieh & Shannon (Conventional) | Hsieh & Shannon (Directed) | Hsieh & Shannon (Summative) | Braun & Clarke |
|---------|---------|-------------------------------|---------------------------|----------------------------|----------------|
| **Primary logic** | Deductive (usually) | Inductive | Deductive + inductive | Keyword-based | Flexible (both) |
| **Procedural rigour** | Very high | Moderate | Moderate–high | Moderate | Moderate |
| **Flexibility** | Low–moderate | High | Moderate | Moderate | Very high |
| **Role of theory** | Central (structuring) | Minimal | Central | Moderate | Optional |
| **Counting** | Yes (optional) | No (typically) | No (typically) | Yes (starting point) | No (typically) |
| **Reliability focus** | Strong | Moderate | Moderate | Moderate | Low–moderate |
| **Best for** | Structured deductive analysis | Exploration | Theory testing/extension | Concept usage analysis | Flexible thematic exploration |
| **Epistemology** | Post-positivist | Varied | Post-positivist | Post-positivist | Varied |

---

## Decision Guide

Use this flowchart to recommend an approach to the user:

```
START
│
├── Do you have a predefined theoretical framework?
│   ├── YES → Is your goal to test/extend the framework?
│   │         ├── YES → Hsieh & Shannon: Directed Content Analysis
│   │         │         (or Mayring: Structuring)
│   │         └── NO (just want to use it as a lens) → Braun & Clarke: Theoretical TA
│   │
│   └── NO → Are you counting occurrences of specific terms/concepts?
│             ├── YES → Hsieh & Shannon: Summative Content Analysis
│             └── NO → Do you want maximum procedural structure?
│                       ├── YES → Mayring: Summarizing or Structuring
│                       └── NO → Is your goal to identify themes/patterns?
│                                 ├── YES → Braun & Clarke: Inductive TA
│                                 │         (or Hsieh & Shannon: Conventional)
│                                 └── NO → Clarify research question first
```

### Additional considerations:

- **Discipline norms matter.** Health sciences often use Hsieh & Shannon. Psychology uses Braun & Clarke. Education and social work often use Mayring. Management and accounting vary. Check what reviewers in the target journal expect.
- **Mixed approaches are common.** A study might use Mayring's structuring technique with a Braun & Clarke-style reporting format. Transparency about the approach taken is more important than purity.
- **Quantitative content analysis** (Neuendorf, 2017) is a separate tradition that prioritizes measurement, reliability, and statistical generalization. Choose this when the research question is about frequencies, trends, or comparisons across a large corpus.
