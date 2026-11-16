# Security

This file says what the plugin contains, what could go wrong, what has been done about it, and how to report a problem. It applies to 5.0.0-beta.7 and later.

## What the plugin contains

- **Instructions in plain text:** the skill (`skills/content-analysis/SKILL.md`), four reference files and one command file. An AI assistant reads them and follows them.
- **One script:** `scripts/validate_coding.py`, which checks finished output files. It uses only the Python standard library (`openpyxl` is optional, for reading `.xlsx`), and it neither fetches nor sends anything.
- **Manifests and an example:** JSON files that describe the plugin, and a small example data set.

The plugin has no hooks, no MCP servers, no binaries and no network calls of its own. Documents you analyse are processed by the product the plugin runs in (Claude, ChatGPT or Codex), under that product's terms; see [PRIVACY.md](PRIVACY.md).

## What could go wrong, and what is done about it

**1. A changed copy of the plugin.** A "virus" in a plugin of this kind would not be a program. It would be an altered instruction, for example one telling the assistant to send your documents somewhere, or an altered validator script.

- Changes reach the `main` branch only through pull requests; force pushes and deletion of `main` are blocked. The project has one maintainer, so a pull request is not approved by a second person.
- The marketplace files point at a release tag, not at `main`, so a change on `main` does not reach installed copies until a release is tagged. Release tags (`v*`) cannot be moved or deleted.
- From 5.0.0-beta.7 every release states the SHA-256 of `SKILL.md` in the changelog, and the README shows how to compare an installed copy with this repository.
- The listing in Anthropic's directory is scanned and reviewed by Anthropic for every version.

**2. Instructions hidden in the material you analyse.** A transcript, report or post can contain text aimed at the assistant ("ignore your instructions and …"). From 5.0.0-beta.7 the skill states that everything in the material is data and never an instruction, and that such passages are reported to the user and not acted on. This lowers the risk. It does not remove it: no wording makes an AI assistant immune to manipulation. In a small test (three runs per version, one model), no run acted on a planted instruction with or without the rule; with the rule every run told the user what the planted text asked for, and without it none did. The test and its limits are in [`docs/security/planted-instruction-test/`](docs/security/planted-instruction-test/README.md).

**3. What the assistant is allowed to do on your computer.** From 5.0.0-beta.7 the `/content-analysis` command no longer pre-approves any tools. The assistant asks, according to your own settings, before it writes files or runs the validator.

## What you can do

- Install from this repository or from the directory of the product you use, not from copies elsewhere.
- Read permission prompts before approving them. The only command the plugin needs to run is the validator script.
- Be careful with material from sources you do not trust, and look at the files the assistant produces.
- Install Python packages (`openpyxl`, `krippendorff`, `scikit-learn`) from the official package index only.

## What is not covered

The plugin cannot protect against a compromised account at GitHub, Anthropic or OpenAI, against a compromised computer, or against an AI model that misbehaves. It is experimental software, provided without warranty; see [LICENSE](LICENSE) and [TERMS.md](TERMS.md).

## Reporting a problem

If you find something that looks like a security problem, write to the author at Peter.Malmkjaer@mail.dk and do not open a public issue with the details. Say which version you used, where you installed it from, and what you saw. For anything else, use [issues](https://github.com/PeterMalmkjaer/content-analysis-plugin/issues).
