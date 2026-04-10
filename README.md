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
git clone https://github.com/serbestonline/content-analysis-plugin
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

### 2. Set up your project folder

The `input/` folder controls how Claude interprets your corpus.

#### Standalone mode — one file, one analysis

Drop transcript files directly into `input/`. Each file is treated as an independent interview and analysed separately.

```
input/
├── Participant_1.txt
├── Participant_2.txt
└── Participant_3.txt
```

#### Project mode — a folder, one shared codebook

Create a subfolder inside `input/` for each research project. Place all transcripts that belong to the same study inside it. Claude will build a shared cumulative codebook and produce both per-participant and cross-participant outputs.

```
input/
└── my-study/
    ├── materials/              ← research context (see below)
    ├── project-description.md  ← auto-generated on first run
    ├── progress.md             ← auto-generated, tracks analysis state
    ├── Participant_1.txt
    ├── Participant_2.txt
    └── Participant_3.txt
```

You can mix both modes — standalone files and project folders can coexist in `input/` at the same time.

### 3. Add research context (optional but recommended)

Place any study materials inside `input/[project-name]/materials/`. These can be:

- Research questions or study purpose
- Interview guide or topic list
- Theoretical framework notes
- Participant profile descriptions
- Any other background documents

On first run, Claude will read everything in `materials/`, extract what it can, and write a `project-description.md` file in the project folder. It will only ask you for information it could not find in the materials. On subsequent runs it reads the existing `project-description.md` directly and skips this step.

The `project-description.md` follows this structure:

```
# Project Description — [Study name]

## Purpose & Research Questions
## Theoretical Framework
## Method (approach, coding logic, unit of analysis)
## Participant Profile
## Interview Guide
```

### 4. Start the analysis

Open your project directory in Claude Code and run:

```
/content-analysis
```

Claude will:
- Scan `input/` and detect standalone files or project subfolders
- Check for `project-description.md` — build it from `materials/` if missing
- Check for `progress.md` — resume from where the project left off if it exists
- Ask you to confirm or fill in any missing research parameters
- Guide you through the eight-step workflow
- Write all output files to `output/`

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

### Per-participant outputs

Written to `output/[project-name]/[participant-name]/`:

| File | Format | Description |
|------|--------|-------------|
| `codebook_[participant].xlsx` | .xlsx | Codes with definitions, inclusion/exclusion criteria, examples |
| `coded_data_[participant].xlsx` | .xlsx | Every coded unit with excerpts, codes, and coder notes |
| `frequency_report_[participant].xlsx` | .xlsx | Code frequencies for this participant |
| `theme_summary_[participant].md` | .md | Narrative findings with method note |
| `thematic_map_[participant].mermaid` | .mermaid | Visual theme hierarchy |

### Project-level outputs (project mode only)

Written to `output/[project-name]/` root. Cumulative files are updated after each participant; summary files are written after the full corpus is coded.

| File | Format | When written | Description |
|------|--------|-------------|-------------|
| `codebook_[project].xlsx` | .xlsx | After each participant | Cumulative codebook merging all codes |
| `frequency_report_[project].xlsx` | .xlsx | After each participant | Participant × code frequency matrix |
| `theme_summary_[project].md` | .md | After full corpus | Cross-participant theme analysis |
| `thematic_map_[project].mermaid` | .mermaid | After full corpus | Project-level thematic map |

### Example output structure

```
output/
└── my-study/
    ├── codebook_my-study.xlsx
    ├── frequency_report_my-study.xlsx
    ├── theme_summary_my-study.md
    ├── thematic_map_my-study.mermaid
    ├── Participant_1/
    │   ├── codebook_Participant_1.xlsx
    │   ├── coded_data_Participant_1.xlsx
    │   ├── frequency_report_Participant_1.xlsx
    │   ├── theme_summary_Participant_1.md
    │   └── thematic_map_Participant_1.mermaid
    └── Participant_2/
        └── ...
```

### Progress tracking

`input/[project-name]/progress.md` is created automatically when analysis begins. It tracks which participants have been coded, notes any new codes added to the cumulative codebook, and records the next step. On subsequent runs Claude reads this file to resume without repeating completed work.

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
