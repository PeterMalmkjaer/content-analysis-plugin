# Changelog

All notable changes to the Content Analysis Plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Responds to an external evaluation of 5.0.0-beta.3 on three test corpora (9–10 September 2026). The evaluation, its figures and its caveats are summarised in `docs/evaluations/2026-09-beta3-external-review.md`; the open points it raised are tracked as GitHub issues, not here.

### Added
- **Step 5b — Calibrate against human coding before freezing.** A calibration set separate from any test set; blind coding; per-code precision, recall, F1 and α with the human–human ceiling where two human coders exist; codes with fewer than ten positive instances reported by name as *insufficiently calibrated* and kept out of the averages; disagreement review by code pair; revisions made to the decision-rule columns and kept only if they hold on fresh calibration items; freeze to `v1` only afterwards. Without human coding, every reliability figure is labelled *not calibrated against human coding*. A protocol-agreement check (unit, co-coding rules, multi-label treatment, excerpt-matching rule) precedes any measurement.
- **Decision-rule columns in the codebook (Step 4):** Required textual basis · Nearest alternative codes · Decisive difference · Boundary example · Co-coding rule · Gate. The first and the co-coding rule are filled for every code; the three confusion columns are mandatory where the pilot or the calibration shows confusion and may otherwise stay blank. Examples come from development material or are marked constructed; never from a held-out test set.
- **Stepwise decision procedure (Step 7):** locate the passage → check criteria and required textual basis → compare with nearest alternatives (settled / settled narrowly → `Review = competing_codes` / not settled → neither) → assign and record → sweep the remaining codes one by one under the same criterion → mark `UNCODED` or `Review`. **Gated codes** are decided first, with their own excerpt, and get their own precision/recall.
- **`Review` column** in the coded-data table (`context_missing` / `possible_irony` / `competing_codes` / `insufficient_basis` / `other`), keeping the provisional assignment; `other` requires a reason in Coder notes, and its share among the flags is reported separately — above about a fifth, the reason list is extended in the next codebook version. Uncertainty is never expressed by choosing a neutral code or `UNCODED`, and no numeric confidence is output. The **review share** is reported in the summary sheet and next to every quality figure.
- Validator: optional `Review` column checked against the allowed set (check 5b); `other` with empty Coder notes is a FAIL; `other` above a fifth of the flags is a WARN; a missing column is a WARN.
- Fixture: `examples/minimal/coded_data.csv` gains the `Review` column with one `competing_codes` flag (A-007, where `TRUST_01` and `TRUST_REJ` meet in one answer); expected output is now eight PASS lines and no WARN.
- Method note gains: batch mechanism, calibration result, AI-consistency and AI–human agreement as separate quantities, review share, model identifier and version, decoding settings and run date.

### Changed
- **7.2 batch isolation is a mechanism, not an instruction:** each batch is coded in a separate context (subagent, fresh session or scripted call) that receives only the frozen codebook, source declaration, manifest, candidate log and the batch's own text. Coding successive batches in one conversation does not satisfy the rule. Where the platform offers no such mechanism, the method note says so, states the batch order, and the 7.5 drift check becomes mandatory.
- LLM-considerations: repeated-coding agreement is stability, not validity; reproducibility requires model, version, decoding settings and date; an "improvement" claim requires the same model on both sides and fresh test items.
- `/content-analysis` asks at the outset whether human-coded material exists for calibration.
- README: "Verify the install" block for ChatGPT/Codex — check the cached clone's commit against GitHub `main`, check for a second copy, and confirm in-app use with a question only the current version can answer.

## [5.0.0-beta.3] - 2026-09-09

Version bump so that Claude and ChatGPT/Codex update mechanisms, which key on the `version` field, pick up the two fixes below.

### Fixed
- Validator: a run in which a required check could not execute (no manifest, no `--sources`, no `--summary`, a document without `Source file`, translated rows) ended with `RESULT: PASS` and exit 0. It now ends with `RESULT: INCOMPLETE` and exit 2, with `SKIP` lines naming the checks that did not run. Reported by an external review of beta.2 (ChatGPT, 9 September 2026).
- Validator: the excerpt check lowercased both sides, so it was not verbatim. It is now case- and punctuation-exact; only whitespace (including non-breaking spaces and line breaks) is normalized. Documented in the script, SKILL.md and the fixture README.
- Removed a compiled `scripts/__pycache__/*.pyc` that had been committed with beta.2; added `.gitignore`.
- README: ChatGPT/Codex installation rewritten from OpenAI's current documentation and a tested update. `codex plugin add` removed (not a documented command); updating an installed plugin requires uninstall + reinstall in the Plugins directory — a restart does not fetch the new version.

## [5.0.0-beta.2] - 2026-09-09

### Added
- `scripts/validate_coding.py`: an output validator (standard library; `openpyxl` optional) that checks excerpts against source files, coverage against the manifest, code IDs against the codebook, uniqueness of assignments, allowed Prompting values, and regenerated frequencies. Step 7 gains a "Validate the outputs" section; `/content-analysis` runs it where a shell exists.
- `examples/minimal/`: a known-good fixture — two interviews, one report, codebook with an inactive code, manifest, long-format coded data, frequencies — on which the validator must pass. Changes to the skill are checked against it.
- Step 2 scope note: coding-reliability TA and codebook TA are supported; **reflexive** TA (Braun & Clarke, 2019, 2021) is not, and κ/α must not be reported for it. Deductive, inductive and abductive logics are all supported throughout; Step 3 now says so and points to the places where they differ.
- `references/reliability-guide.md`: "Multiple Codes per Unit" — agreement per code as presence/absence, per-code α/κ, mean plus range, and explicit denominators.

### Changed
- **Coded-data table is long format**: one row per code assignment, with an `Assignment ID`. `Prompting` moves to assignment level and gains `mixed` and `unclear`; one answer may hold a prompted and a volunteered topic in separate rows. Every percentage states its denominator (assignments, units, or documents).
- **Blind re-coding**: the intra-coder check (Step 6) and the drift check (7.5) must run in a separate context that receives the same inputs as the first coding but not the coding itself; "not looking" at a coding already in context is not a control. Repeated AI coding is reported as consistency; comparison with a human coder is reported separately.
- **Large documents**: 7.2 no longer forbids splitting a document; when one exceeds the available context it is split at section or turn boundaries with stable part IDs, carried context, and one manifest row per part. The coded-data workbook is appended on disk, not re-read in full.
- **Pilot selection** (Step 5): at least 3 documents and 10% of units (minimum 50), stratified over source types and compared groups; corpora under 50 units are piloted in full.
- README: the Codex CLI install commands are marked unverified pending a test against a real install; OpenAI's documented route is the Plugins tab.
- Step 4 gains a "For Abductive Coding" block, so all three logics have a codebook-origin procedure. The Decision Guide in `coding-approaches.md` no longer recommends reflexive TA; its Braun & Clarke leaves are labelled codebook TA.
- Manifest rows may be document parts (`Parent document` column); document counts collapse parts to the parent.

### Fixed
- Braun & Clarke (2019, 2021) read in full and cited by page. The skill no longer claims to *follow* Braun & Clarke (2006): they place that approach in reflexive TA and ask not to be cited for codebook or coding-reliability practice (2021, p. 336). Codebook TA is now described as fitting Steps 4–8 with Step 6 optional, per their own account (2021, p. 333). README, SKILL.md, the Decision Guide and the plugin descriptions in `plugin.json` / `marketplace.json` updated accordingly.

### Credits
- The seven points behind this release come from an external review of 5.0.0-beta.1 (ChatGPT, 9 September 2026), commissioned by the author. Points taken in full: method scoping, blind re-coding, multi-code reliability, output validation, document splitting, pilot selection, assignment-level prompting.

### Notes
- Licence terms unchanged.

## [5.0.0-beta.1] - 2026-09-09

### Added
- **Source declaration** in Step 1: source type, producer, purpose, audience, elicitation, date, language, sampling, completeness — recorded per source; part of it is carried on every coded unit as provenance columns.
- `references/source-types.md`: how elicited talk, institutional documents, media texts, user-generated content, open survey responses, naturally occurring records and continuous prose differ in natural unit, fitting coding logic, reliability outlook and signature traps; interviews get the sharpest treatment (the question is the context unit and is recorded; `prompted`/`volunteered` per unit). Includes the **heterogeneity gate**: a corpus whose unit cannot be defined the same way across sources is stratified and compared, never pooled.
- Step 7 rewritten for corpora that do not fit one session: codebook frozen **per pass** with a version log; batching with a corpus manifest; a candidate log that is a deliverable (in directed content analysis it is the theory-extension finding); passes per design (1 for fixed-instrument deductive, 2 for directed/Mayring, 2–3 for abductive, 2+ for inductive); saturation tracking for inductive designs; a drift check on the first batch.
- `Answer` added as a unit of analysis for semi-structured interviews.
- Provenance and versioning columns in the coded data table: Source type, Producer, Elicitation, Prompting, Date, Parent/section, Language, Codebook version, Pass. A `Status` column (`active`/`inactive`) in the codebook; the version log as a `version_log` sheet. Manifest, candidate log and summary become sheets in the same workbook.

### Changed
- `/content-analysis` now asks for the source declaration alongside the four existing clarifications, and points to `source-types.md` and the batching procedure conditionally, not up front.
- The LLM-considerations section no longer claims uniform consistency across a corpus; across batches it is a procedure (Step 7), not a property. The method-note checklist now includes the source declaration and the Step 7 procedure.
- Version bumped to a pre-release: this is a new contract (Step 1 inputs, Step 7 procedure, output columns) and the first release in which the Codex/ChatGPT support from 4.3.0 is exercised end to end; that needs feedback before 5.0.0.

### Credits
- The problem statement in issue #1 and several mechanics in PR #2 — the codebook version log with a "triggered by" column, never deleting a code but marking it inactive, retroactive coding, the saturation table, cross-corpus outputs, and a progress file that here becomes the corpus manifest — are due to **@serbestonline**. The PR itself was not merged: it treated the codebook as always cumulative (inductive logic applied to every design), changed default naming to participant IDs for all corpora, and loaded all references unconditionally. See the discussion on #1 and #2.

### Notes
- Licence terms unchanged.

## [4.3.0] - 2026-09-04

### Added
- Native Codex plugin manifest at `.codex-plugin/plugin.json`.
- Codex marketplace metadata at `.agents/plugins/marketplace.json` for installation from GitHub.
- Public privacy policy and terms pages for plugin listing metadata.

### Changed
- Made the shared skill instructions platform-neutral so the same workflow works in ChatGPT, Codex, and Claude.
- Added Codex installation instructions while retaining the Claude marketplace and slash command.
- Updated the citation and package metadata to version 4.3.0.

### Notes
- The analysis workflow, methodological references, and dual-licence terms are unchanged.

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
