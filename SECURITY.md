# Security

This file says what the plugin contains and how to report a problem.

## What the plugin contains

- **Instructions in plain text:** the skill (`skills/content-analysis/SKILL.md`), four reference files and one command file. An AI assistant reads them and follows them.
- **No scripts in this copy:** the output validator `scripts/validate_coding.py`, which checks finished output files, is in the repository only. It uses only the Python standard library (`openpyxl` is optional, for reading `.xlsx`), and it neither fetches nor sends anything.
- **Manifests:** JSON files that describe the plugin.

The plugin has no hooks, no MCP servers, no binaries and no network calls of its own. Documents you analyse are processed by the product the plugin runs in (Claude, ChatGPT or Codex), under that product's terms; see [PRIVACY.md](PRIVACY.md).

## Security updates

Security-related changes are listed in the [changelog](CHANGELOG.md) as security updates. Details are not published.

## What you can do

- Install from this repository or from the directory of the product you use, not from copies elsewhere.
- Read permission prompts before approving them. In this copy the plugin runs no commands of its own; the only one it may suggest is the validator, if you have fetched it.
- Look at the files the assistant produces before you rely on them.
- Install Python packages (`openpyxl`, `krippendorff`, `scikit-learn`) from the official package index only.

The plugin is experimental software, provided without warranty; see [LICENSE](LICENSE) and [TERMS.md](TERMS.md).

## Reporting a problem

If you find something that looks like a security problem, write to the author at Peter.Malmkjaer@mail.dk and do not open a public issue with the details. Say which version you used, where you installed it from, and what you saw. For anything else, use [issues](https://github.com/PeterMalmkjaer/content-analysis-plugin/issues).
