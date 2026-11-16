# Content Analysis plugin: overview and evidence

Content Analysis is a plugin for Claude, ChatGPT and Codex that guides an AI assistant through a systematic content analysis of texts: from research question and codebook to coded data, frequencies and a method note. This page gathers what the plugin is, where to get it, what is known about how well it works, and the documents behind that knowledge.

- **Version:** 5.0.0-beta.6, a preview release. The skill is experimental software.
- **For whom:** researchers and students doing qualitative or quantitative content analysis. Academic and non-commercial use is free; see the [licence](https://github.com/PeterMalmkjaer/content-analysis-plugin/blob/main/LICENSE).
- **Get it:** installation for Claude, ChatGPT and Codex is described in the [repository README](https://github.com/PeterMalmkjaer/content-analysis-plugin#installation).

**The short verdict.** On the material tested, the skill can be used as a pre-coder or as a supplementary coder. It cannot stand alone: its coding is input for further work by a researcher, not a finished result.

## What the plugin does

It follows established content-analysis conventions (Krippendorff, Hsieh & Shannon, Mayring, and codebook thematic analysis) and supports these steps:

- declaring the sources and the unit of analysis;
- developing a codebook, deductively from a framework or inductively from the material;
- piloting the codebook and, where human-coded material exists, calibrating it against that coding;
- coding the material with verbatim excerpts, and flagging the decisions it found hard for review;
- counting frequencies, summarising themes and writing a method note with limitations;
- checking the output files with a validator script.

The researcher stays in charge of the research question, the interpretations and the conclusions.

## Where it is known to work

"Works" below means measured and repeated. None of the entries means that the coding can be used without human review. Table 1 separates what was measured from what was tried once and from what is not known.

**Table 1. What is known, and how firmly**

| Area | What is known | Basis |
|---|---|---|
| Deductive coding of short texts with a calibrated codebook | Agreement score 49–51 against 44–47 for 5.0.0-beta.3, in all six runs | Three pre-registered tests, one corpus, one model |
| Calibration against human-coded material | Raises agreement by 3.5–7.2 points on texts that were not part of the calibration | Same tests |
| Level compared with one human rater | Calibrated: 6–7 points above a single crowd rater. Uncalibrated: level with one | Comparison with individual raters; not yet in this repository |
| The `Review` flag | Flagged comments score 27–39, unflagged 46–58: the flag points at the weaker coding | Two of the three tests |
| Code frequencies after calibration | Close to the human raters' for the two codes examined. Without calibration they are skewed | Same tests |
| Stability | Two runs of the same task agree at 85–92 | Same tests |
| Output files | Every test run passed the validator: no omitted units, no invalid codes | Same tests |
| Speed and machine cost | Under a second and about one cent per short comment | Measured in the third test |
| Interview transcripts, deductive coding | F1 60.1 against one researcher's coding | Tried once, 5.0.0-beta.3, another model; AI-written report |
| Policy reports in Dutch | 63.1 agreement with another AI workflow, not with people | Tried once, 5.0.0-beta.3, another model; AI-written report |
| Installing and running in Claude, ChatGPT and Codex | It installs and runs | Confirmed technically; coding quality measured on one Claude model only |
| Inductive development of codebooks and themes | Not known | Not tested |
| Long texts (interviews, reports) | Not known for the current version | Last tested in 5.0.0-beta.3 |
| Languages other than English | Not known for the current version | Last tested in 5.0.0-beta.3 (Dutch) |
| Calibrating on one kind of material and coding another | Not known | Not tested |
| Reliability statistics, frequency reports and thematic reporting | Not known | Not tested |
| A person reviewing the flagged coding, as a whole workflow | Not known | Not tested |

The agreement score is micro-F1 on a scale from 0 to 100. The human yardstick in the measured rows is crowd raters who themselves agree little with each other, so the level says little about other material; the comparisons are what the tests support.

## Where to read what

**Table 2. The documents and what each answers**

| Document | What it answers | Written by |
|---|---|---|
| [Test report for 5.0.0-beta.6](test-report-5.0.0-beta.6.md) | Can the skill be used, for what, and under which conditions? Conclusion, method, five results, assumptions, limitations, limits of use, conditions of use and recommended use | AI assistant at the author's direction; carries a notice |
| [Benchmarks](benchmarks/README.md) | What exactly was measured? The three pre-registered tests on GoEmotions (beta.3 to beta.6), with protocols, codebooks, every code assigned and a script that recomputes the headline figures | AI assistant at the author's direction |
| [External evaluation of 5.0.0-beta.3](evaluations/2026-09-beta3-external/README.md) | How did an earlier version do on interview transcripts and policy reports? Four reports in Danish from September 2026, with a note on which of their figures were recomputed | An AI in a separate evaluation; each report carries a notice |
| [Note on that evaluation](evaluations/2026-09-beta3-external-review.md) | What the evaluation triggered in the skill | Author with AI assistance |

## How the parts fit together

The **benchmarks** are the primary evidence. They cover one corpus (short Reddit comments coded for emotion) and one AI model, with fixed samples and two runs per condition.

The **test report** is the reading of that evidence. It adds a comparison with individual human raters, a section on effort and cost, and the conditions and limits that apply to use. Every figure in it comes from the benchmark result files or is marked as an assumption.

The **external evaluation** is older and separate. It tested 5.0.0-beta.3 with another model family and another protocol, on three data sets, two of which (interviews, policy reports) no later version has been run on. Its figures should not be set beside the benchmark figures.

## Before using the skill on research material

Two conditions apply to every use, and the test report sets them out under [Conditions of use](test-report-5.0.0-beta.6.md#conditions-of-use-experimental-software-and-research-ethics):

- **The skill is experimental software.** Results are provisional; record the version, the model and the date of every analysis.
- **Strict compliance with research ethics is necessary.** The skill does not check whether material may be processed. Your own institution may have rules of its own; they come first, and this documentation can only point to them.

## What is not here

- The material behind the comparison with individual raters (Result 2 of the test report) is not yet in this repository.
- The coded data of the external evaluation are not redistributed; see the README of that folder for the reason.
- No version after 5.0.0-beta.3 has been tested on interviews, reports or other long texts, on another model, or with calibration material from a different source than the texts being coded.

## A note on authorship

Almost all text here was written by AI assistants: the test report and the benchmark reports with Claude at the author's direction, the external evaluation by another AI. AI-written text can contain errors that look plausible. Where figures have been recomputed, the documents say so and say what the check did not cover. Treat the rest as claims to verify.
