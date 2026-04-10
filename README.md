# Content Analysis Plugin

Scientific content analysis for academic research, built for Claude Code.

**Author:** Peter Malmkjaer (spm.om@cbs.dk)
Independent project by Peter Malmkjaer. Thanks for the support from Copenhagen Business School (CBS) and Department of Operations Management.
**Version:** 4.1.0
**Status:** Development — use at own risk

---

## Quick Install

**From GitHub (no clone required):**

```bash
claude plugin marketplace add PeterMalmkjaer/content-analysis-plugin --name content-analysis-plugin && claude plugin install content-analysis@content-analysis-plugin
```

**From a local clone:**

```bash
git clone https://github.com/PeterMalmkjaer/content-analysis-plugin
bash content-analysis-plugin/install.sh
```

Restart Claude Code after installing. The `/content-analysis` command is then available in any project.

---

## What It Does

This plugin enables Claude to perform rigorous, methodologically grounded content analysis on textual material. It follows established social-science conventions from Krippendorff (2018), Hsieh & Shannon (2005), Mayring (2014), and Braun & Clarke (2006).

It supports the full workflow from research question to publication-ready output files — for both single interviews and multi-interview corpora.

---

## Getting Started

### 1. Install the plugin

See [Quick Install](#quick-install) above. After installation the plugin is available globally — you do not need to keep the repository in your project directory.

### 2. Place your transcripts in the `input/` folder

The `input/` folder controls how Claude interprets your corpus. There are two modes:

#### Standalone mode — one file, one analysis

Drop transcript files directly into `input/`. Each file is treated as an independent interview and analysed separately.

```
input/
├── Participant_1.txt     → analysed independently → output/Participant_1/
├── Participant_2.txt     → analysed independently → output/Participant_2/
└── Participant_3.txt     → analysed independently → output/Participant_3/
```

#### Project mode — a folder, one shared codebook

Create a subfolder inside `input/` and place all transcripts that belong to the **same research project** inside it. Claude will treat them as a multi-interview corpus, build a shared cumulative codebook, and produce both per-interview and cross-interview outputs.

```
input/
└── my-study/                  → one project, shared codebook
    ├── Participant_1.txt
    ├── Participant_2.txt
    └── Participant_3.txt
```

Output will mirror the structure:

```
output/
└── my-study/
    ├── codebook_my-study.xlsx          ← shared, versioned
    ├── coded_data_Participant_1.xlsx
    ├── coded_data_Participant_2.xlsx
    ├── coded_data_Participant_3.xlsx
    ├── coded_data_ALL.xlsx             ← merged corpus
    ├── frequency_report_Participant_1.xlsx
    ├── frequency_report_CROSS.xlsx     ← cross-interview comparison
    ├── theme_summary_Participant_1.md
    ├── theme_summary_CROSS.md          ← comparative findings
    └── thematic_map_CROSS.mermaid
```

You can mix both modes — standalone files and project folders can coexist in `input/` at the same time.

### 3. Start the analysis

Open your project directory in Claude Code and run:

```
/content-analysis
```

Claude will:
- Immediately scan `input/` in your current working directory
- Detect standalone files or project subfolders automatically
- Ask you to confirm the research question, unit of analysis, approach, and coding logic
- Guide you through the eight-step workflow
- Write all output files to `output/` in your current working directory

---

## Eight-Step Workflow

| Step | Description |
|------|-------------|
| 1 | Clarify research question and unit of analysis |
| 2 | Select approach (quantitative / qualitative / mixed) |
| 3 | Select coding logic (deductive / inductive / abductive) |
| 4 | Develop coding scheme (codebook) |
| 5 | Pilot-code a sample |
| 6 | Assess inter-coder reliability |
| 7 | Code the full corpus |
| 8 | Analyse and report |

For multi-interview corpora, the codebook grows cumulatively across interviews. See `skills/content-analysis/references/multi-interview-guide.md` for details.

---

## Output Files

### Per-interview outputs

| File | Format | Description |
|------|--------|-------------|
| `codebook_[project].xlsx` | .xlsx | Codes with definitions, inclusion/exclusion criteria, examples |
| `coded_data_[ID].xlsx` | .xlsx | Every coded unit with excerpts, codes, and coder notes |
| `frequency_report_[ID].xlsx` | .xlsx | Code frequencies for this interview |
| `theme_summary_[ID].md` | .md | Narrative findings with method note |
| `thematic_map_[ID].mermaid` | .mermaid | Visual theme hierarchy |

### Cross-interview outputs (project mode only)

| File | Format | Description |
|------|--------|-------------|
| `coded_data_ALL.xlsx` | .xlsx | All coded units from all interviews in one table |
| `frequency_report_CROSS.xlsx` | .xlsx | Code × participant frequency matrix |
| `theme_summary_CROSS.md` | .md | Comparative narrative: core vs. idiosyncratic themes |
| `thematic_map_CROSS.mermaid` | .mermaid | Full corpus thematic map |

---

## Reference Files

| File | Contents |
|------|----------|
| `references/reliability-guide.md` | Formulas and Python code for Cohen's κ, Fleiss' κ, and Krippendorff's α |
| `references/coding-approaches.md` | Comparison of Mayring, Hsieh & Shannon, and Braun & Clarke frameworks |
| `references/multi-interview-guide.md` | Cumulative codebook management, versioning, retroactive coding, and theoretical saturation |

---

## Supported Transcript Formats

Plain text files (`.txt`) are the primary format. WhisperX output, interview transcripts with speaker labels (e.g., `[MOD]:`, `[P1]:`), and unformatted prose are all supported. Files should be UTF-8 encoded.

---

## License

This plugin is released under a **dual license**:

### Academic & Non-Commercial Use (Free)

Free for academic research, teaching, and non-commercial use. You may use, copy, and adapt the skill for scholarly purposes provided you credit the author:

> Content Analysis Skill by Peter Malmkjaer, Copenhagen Business School (spm.om@cbs.dk)

### Commercial Use (Paid License Required)

Any commercial use — including integration into paid products, consulting services, corporate training, or resale on marketplaces — requires a separate commercial license. Contact the author for terms and pricing:

**Peter Malmkjaer** — spm.om@cbs.dk

© 2026 Peter Malmkjaer. All rights reserved.
