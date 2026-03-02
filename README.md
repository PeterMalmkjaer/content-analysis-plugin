# Content Analysis Plugin

Scientific content analysis for academic research, built for Claude Cowork.

**Author:** Peter Malmkjaer (spm.om@cbs.dk)
Independent project by Peter Malmkjaer. Thanks for the support from Copenhagen Business School (CBS) and Department of Operations Management.
**Version:** 4.0.0
**Status:** Development — use at own risk

## What It Does

This plugin enables Claude to perform rigorous, methodologically grounded content analysis on textual material. It follows established social-science conventions from Krippendorff (2018), Hsieh & Shannon (2005), Mayring (2014), and Braun & Clarke (2006).

It supports the full workflow from research question to publication-ready output files.

## Components

### Skill: content-analysis

Activates automatically when you mention "Use Content analysis", "codebook", "thematic analysis", "code the data", "qualitative coding", or similar phrases.

Provides an eight-step workflow:
1. Clarify research question and unit of analysis
2. Select approach (quantitative / qualitative / mixed)
3. Select coding logic (deductive / inductive / abductive)
4. Develop coding scheme (codebook)
5. Pilot-code a sample
6. Assess inter-coder reliability
7. Code the full corpus
8. Analyse and report

Reference files included:
- `references/reliability-guide.md` — Inter-coder reliability metrics and Python code
- `references/coding-approaches.md` — Comparison of Mayring, Hsieh & Shannon, and Braun & Clarke

### Command: /content-analysis

Run `/content-analysis` to start a content analysis session directly.

## Output Files

| File | Format | Description |
|------|--------|-------------|
| Codebook | .xlsx | Codes with definitions, inclusion/exclusion criteria, examples |
| Coded data | .xlsx | Every coded unit with excerpts, codes, and notes |
| Theme summary | .md / .docx | Narrative findings with method note |
| Thematic map | .mermaid | Visual theme hierarchy |
| Reliability report | .xlsx | ICR calculations (when applicable) |

## Usage

Simply say "Use Content analysis" followed by your research question or upload documents and ask Claude to analyse them. The skill will guide you through the process.

## License

This plugin is released under a **dual license**:

### Academic & Non-Commercial Use (Free)
Free for academic research, teaching, and non-commercial use. You may use, copy, and adapt the skill for scholarly purposes provided you credit the author:

> Content Analysis Skill by Peter Malmkjaer, Copenhagen Business School (spm.om@cbs.dk)

### Commercial Use (Paid License Required)
Any commercial use — including integration into paid products, consulting services, corporate training, or resale on marketplaces — requires a separate commercial license. Contact the author for terms and pricing:

**Peter Malmkjaer** — spm.om@cbs.dk

© 2026 Peter Malmkjaer. All rights reserved.
