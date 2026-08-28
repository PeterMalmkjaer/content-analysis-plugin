# Changelog

All notable changes to the Content Analysis Plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [4.2.2] - 2026-08-28

### Changed
- Al institutionsomtale fjernet fra LICENSE og README, og kontaktadressen ændret til Peter.Malmkjaer@mail.dk i LICENSE, README og `plugin.json`. Begge filer erklærer projektet uafhængigt; taksigelsen til Copenhagen Business School og Department of Operations Management kunne læses som en modsigelse af netop det.
- Krediteringsformlen i README rettet til "Content Analysis Skill by Peter Malmkjaer", så den svarer til den ordlyd, LICENSE faktisk kræver. README bad hidtil om en anden kreditering end licensen.
- Versionslinjen i README fulgte ikke længere `plugin.json`; den opdateres nu sammen med den.

### Notes
- Ingen ændring af licensvilkårene. Ophavsretsangivelsen og begge licensspor står urørt.

## [4.2.1] - 2026-08-18

### Fixed
- Licensangivelsen i `plugin.json` rettet fra `SEE LICENSE` til `SEE LICENSE IN LICENSE`. Den korte form er ikke en gyldig SPDX-streng; konventionen for en licens, der ikke findes i SPDX-registret, er `SEE LICENSE IN <filnavn>`. Peger nu utvetydigt på repoets LICENSE-fil, som er en dual-licens: fri til akademisk og ikke-kommerciel brug med kildeangivelse, kommerciel brug kræver særskilt aftale.

### Notes
- Rent skrivemåde. Hverken licensvilkårene eller LICENSE-filen er ændret.

## [4.2.0] - 2026-08-18

### Changed
- Versionsnummeret rettet fra 1.1.0 til 4.2.0. Nummereringen blev nulstillet til 1.0.0 forud for marketplace-indsendelsen (commit a589d30), efter at projektet allerede havde nået 4.1.0 (commit e3acb11). Dette genopretter den oprindelige rækkefølge.

### Notes
- Rent metadata. Ingen ændring af skill-indhold, workflow, referencer eller output-konventioner.

## [1.1.0] - 2026-08-06

### Added
- `references/protocol-driven-runs.md` — guidance for content analyses commissioned as a written brief or protocol, or run unattended, rather than negotiated in conversation. Four rules: derive the research question from the brief when none is stated (and never proceed without one), use a full report skeleton that opens with the task and the question, let the brief's named deliverables and formats take precedence over the plugin's `.xlsx` conventions, and make and record defensible choices instead of blocking on questions nobody is present to answer.
- Conditional pointer to the new reference in Step 1 of the skill and in the `/content-analysis` command, so the guidance is loaded only when a run is protocol-driven or unattended.

### Changed
- `/content-analysis` no longer states the `.xlsx` output set unconditionally; a brief's own deliverable list now takes precedence.

### Notes
- Backwards compatible. Conversational runs are unaffected: the skill's eight-step workflow, its trigger description, and its default output conventions are unchanged.
- Motivation: in a protocol-driven run, the skill produced the four deliverables the protocol named but omitted the research question entirely, because Step 1 instructs the analyst to establish it *with the user* and no user was available. The omission was invisible until a reader asked what the analysis was for.

## [1.0.0] - 2026-04-28

### Added
- Initial public release.
- `content-analysis` skill with eight-step workflow covering research question clarification, approach selection, codebook development, pilot coding, reliability assessment, full-corpus coding, and reporting.
- `/content-analysis` slash command for direct invocation.
- Reference guide for inter-coder reliability metrics (Cohen's κ, Fleiss' κ, Krippendorff's α, percentage agreement) with formulas, worked examples, and Python implementation.
- Reference guide comparing Mayring's qualitative content analysis, Hsieh & Shannon's three approaches, and Braun & Clarke's thematic analysis, with a decision guide.
- Dual license: free for academic and non-commercial use, paid license for commercial use.
- Structured output conventions for codebooks (.xlsx), coded data tables (.xlsx), theme summaries (.md/.docx), thematic maps (.mermaid), and reliability reports (.xlsx).
- Built-in methodological transparency requirements: every analysis produces a method note documenting research question, corpus, unit of analysis, approach, coding logic, codebook development, reliability assessment, and limitations.
