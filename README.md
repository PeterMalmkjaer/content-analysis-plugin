# Content Analysis Plugin

Scientific content analysis for academic research, built for Claude.

**Author:** Peter Malmkjaer ([spm.om@cbs.dk](mailto:spm.om@cbs.dk))
Independent project by Peter Malmkjaer. Thanks to Copenhagen Business School (CBS) and the Department of Operations Management for institutional support.

**Version:** 1.0.0

---

## What It Does

This plugin enables Claude to perform rigorous, methodologically grounded content analysis on textual material. It follows established social-science conventions from Krippendorff (2018), Hsieh & Shannon (2005), Mayring (2014), and Braun & Clarke (2006).

It supports the full workflow from research question to publication-ready output files.

---

## Installation

Add the plugin to your Claude marketplace and install it:

```bash
/plugin marketplace add PeterMalmkjaer/content-analysis-plugin
/plugin install content-analysis@PeterMalmkjaer
```

Once installed, the skill activates automatically when you describe a content-analysis task. You can also invoke the workflow explicitly with the `/content-analysis` command.

---

## Components

### Skill: `content-analysis`

Activates automatically when you mention phrases such as "content analysis", "codebook", "thematic analysis", "code the data", "qualitative coding", or "inter-coder reliability".

Provides an eight-step workflow:

1. Clarify research question and unit of analysis
2. Select approach (quantitative / qualitative / mixed)
3. Select coding logic (deductive / inductive / abductive)
4. Develop coding scheme (codebook)
5. Pilot-code a sample
6. Assess inter-coder reliability
7. Code the full corpus
8. Analyse and report

### Reference Files

- [`skills/content-analysis/references/reliability-guide.md`](skills/content-analysis/references/reliability-guide.md) — Inter-coder reliability metrics (Cohen's κ, Fleiss' κ, Krippendorff's α, percentage agreement) with formulas, worked examples, and Python implementation.
- [`skills/content-analysis/references/coding-approaches.md`](skills/content-analysis/references/coding-approaches.md) — Comparative reference for Mayring's qualitative content analysis, Hsieh & Shannon's three approaches, and Braun & Clarke's thematic analysis, with a decision guide.

### Command: `/content-analysis`

Run `/content-analysis` to start a content-analysis session directly. Optionally pass arguments describing your documents or research focus.

---

## Output Files

| File | Format | Description |
|------|--------|-------------|
| Codebook | `.xlsx` | Codes with definitions, inclusion/exclusion criteria, examples |
| Coded data | `.xlsx` | Every coded unit with excerpts, codes, and notes |
| Theme summary | `.md` / `.docx` | Narrative findings with method note |
| Thematic map | `.mermaid` | Visual theme hierarchy |
| Reliability report | `.xlsx` | ICR calculations (when applicable) |

---

## Usage Example

```
User: "Use Content analysis. I have 12 interview transcripts about
remote work attitudes among knowledge workers. I want to identify
themes inductively."

Claude will:
1. Confirm the research question and propose speaking turns as the
   unit of analysis.
2. Recommend Hsieh & Shannon's Conventional approach (data-driven,
   no preconceived categories).
3. Read a 10–20% sample to develop initial codes through open coding.
4. Group codes into higher-level categories (axial coding) and
   present a draft codebook for your review.
5. Pilot-code a small subset to test the codebook, revise as needed.
6. Code the full corpus and produce coded_data.xlsx and a theme
   summary with a method note.
```

The skill always begins by clarifying your research question and unit of analysis. It will not start coding until these are explicit.

---

## Methodological Transparency

Every analysis produced with this skill includes a method note documenting the research question, corpus description, unit of analysis, approach, coding logic, codebook development process, reliability assessment (when applicable), and limitations. This is essential for academic credibility and reviewers in any peer-reviewed venue.

The skill is explicit about the limitations of LLM-assisted coding: latent content (irony, sarcasm, cultural subtext) may be missed, and results should ideally be validated against a human-coded subsample before publication.

---

## License

This plugin is released under a **dual license**. See [LICENSE](LICENSE) for full terms.

### Academic & Non-Commercial Use (Free)

Free for academic research, teaching, and non-commercial use. You may use, copy, and adapt the skill for scholarly purposes provided you credit the author:

> Content Analysis Skill by Peter Malmkjaer, Copenhagen Business School ([spm.om@cbs.dk](mailto:spm.om@cbs.dk))

### Commercial Use (Paid License Required)

Any commercial use — including integration into paid products, consulting services, corporate training, or resale on marketplaces — requires a separate commercial license. Contact the author for terms and pricing:

**Peter Malmkjaer** — [spm.om@cbs.dk](mailto:spm.om@cbs.dk)

© 2026 Peter Malmkjaer. All rights reserved.

---

## Citation

If you use this plugin in academic work, please cite:

> Malmkjaer, P. (2026). *Content Analysis Plugin for Claude* (Version 1.0.0) [Computer software]. https://github.com/PeterMalmkjaer/content-analysis-plugin
