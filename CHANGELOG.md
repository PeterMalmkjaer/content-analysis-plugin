# Changelog

All notable changes to the Content Analysis Plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
