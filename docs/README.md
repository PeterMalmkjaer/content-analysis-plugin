# Documentation and evidence

This folder holds what is known about how well the Content Analysis skill codes, how that was measured, and what follows for using it. Start here.

**The short verdict.** On the material tested, the skill can be used as a pre-coder or as a supplementary coder. It cannot stand alone: its coding is input for further work by a researcher, not a finished result. The skill is experimental software in a preview release.

## Where to read what

**Table 1. The documents and what each answers**

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

Almost all text in this folder was written by AI assistants: the test report and the benchmark reports with Claude at the author's direction, the external evaluation by another AI. AI-written text can contain errors that look plausible. Where figures have been recomputed, the documents say so and say what the check did not cover. Treat the rest as claims to verify.
