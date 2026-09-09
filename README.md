# Content Analysis Plugin

Scientific content analysis for academic research, available for ChatGPT, Codex, and Claude.

**Author:** Peter Malmkjaer ([Peter.Malmkjaer@mail.dk](mailto:Peter.Malmkjaer@mail.dk))
Independent project by Peter Malmkjaer.

> **Preview release.** 5.0.0-beta.1 adds a source declaration and a procedure for large corpora, and is the first version to ship Codex/ChatGPT support. Codex/ChatGPT behaviour has had limited testing. Please report what you find via [issues](https://github.com/PeterMalmkjaer/content-analysis-plugin/issues) — the 5.0.0 release depends on it.

**Version:** 5.0.0-beta.1

---

## What It Does

This plugin enables an AI assistant to perform rigorous, methodologically grounded content analysis on textual material. It follows established social-science conventions from Krippendorff (2018), Hsieh & Shannon (2005), Mayring (2014), and Braun & Clarke (2006).

It supports the full workflow from research question to publication-ready output files.

## How This Plugin Can Help You

Use the plugin when you need to turn a collection of texts into systematic, transparent, and research-ready findings. It can help you:

- Analyse interview transcripts, focus-group discussions, open-ended survey responses, reports, policy documents, articles, and other textual material.
- Develop a clear codebook with definitions, inclusion and exclusion criteria, and examples.
- Apply deductive codes from an existing theory or discover inductive themes from the material.
- Pilot and refine a coding scheme before analysing the full collection.
- Code passages consistently while keeping excerpts and rationales traceable.
- Calculate or interpret inter-coder reliability when multiple coders are involved.
- Identify patterns, frequencies, themes, and relationships across documents.
- Produce structured outputs for further review, reporting, or academic writing.

The plugin guides you through the methodological choices and documents important limitations. You remain in control of the research question, interpretations, and final conclusions.

---

## Installation

### Codex

Add the GitHub marketplace and install the plugin with Codex CLI:

```bash
codex plugin marketplace add PeterMalmkjaer/content-analysis-plugin --ref main
codex plugin add content-analysis@content-analysis-plugin
```

Restart Codex or start a new session after installation. The skill activates automatically when you describe a content-analysis task.

### Claude

Add the plugin to your Claude marketplace and install it:

```bash
/plugin marketplace add PeterMalmkjaer/content-analysis-plugin
/plugin install content-analysis@content-analysis-plugin
```

Or from the terminal with the Claude Code CLI:

```bash
claude plugin marketplace add PeterMalmkjaer/content-analysis-plugin
claude plugin install content-analysis@content-analysis-plugin
```

Once installed, the skill activates automatically when you describe a content-analysis task. In Claude, you can also invoke the workflow explicitly with the `/content-analysis` command.

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
- [`skills/content-analysis/references/protocol-driven-runs.md`](skills/content-analysis/references/protocol-driven-runs.md) — Rules for analyses commissioned in writing or run unattended: deriving the research question when the brief does not state one, the required report skeleton, output-format precedence, and how to proceed without blocking on unanswerable questions.

### Claude command: `/content-analysis`

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

The assistant will:
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

## Written Briefs and Unattended Runs

The workflow above assumes a conversation. Analyses are often commissioned differently: a written protocol defines the task, names the deliverables, and no one is available to answer questions while the run proceeds.

For those cases the skill loads `references/protocol-driven-runs.md`, which supplies four rules that replace the conversational assumptions:

1. **Derive the research question.** Briefs typically specify what to do but not what the analysis is for. A deliverable list is not a research question. The skill derives one from the brief's own terms, marks it explicitly as derived, decomposes it into one sub-question per coded dimension, and never proceeds without one.
2. **Use the full report skeleton.** Task · problem statement and analysis questions · constraints declaration · method · findings (one section per question) · uncertainties · deliverables · references. Written briefs mean the report will be read by someone who was not present.
3. **The brief's formats take precedence.** Named deliverables, names and paths override the `.xlsx` conventions in the Output Files table above. The format changes; the substance does not.
4. **Do not block.** In an unattended run, make the most defensible choice, state the assumption at the point it applies, record the rejected alternative, and continue.

Nothing changes for conversational use — the rules apply only when the run is protocol-driven or unattended.

---

## Methodological Transparency

Every analysis produced with this skill includes a method note documenting the research question, corpus description, unit of analysis, approach, coding logic, codebook development process, reliability assessment (when applicable), and limitations. This is essential for academic credibility and reviewers in any peer-reviewed venue.

The skill is explicit about the limitations of LLM-assisted coding: latent content (irony, sarcasm, cultural subtext) may be missed, and results should ideally be validated against a human-coded subsample before publication.

---

## License

This plugin is released under a **dual license**. See [LICENSE](LICENSE) for full terms.

### Academic & Non-Commercial Use (Free)

Free for academic research, teaching, and non-commercial use. You may use, copy, and adapt the skill for scholarly purposes provided you credit the author:

> Content Analysis Skill by Peter Malmkjaer

### Commercial Use (Paid License Required)

Any commercial use — including integration into paid products, consulting services, corporate training, or resale on marketplaces — requires a separate commercial license. Contact the author for terms and pricing:

**Peter Malmkjaer** — [Peter.Malmkjaer@mail.dk](mailto:Peter.Malmkjaer@mail.dk)

© 2026 Peter Malmkjaer. All rights reserved.

---

## Citation

If you use this plugin in academic work, please cite:

> Malmkjaer, P. (2026). *Content Analysis Plugin* (Version 5.0.0-beta.1) [Computer software]. https://github.com/PeterMalmkjaer/content-analysis-plugin
