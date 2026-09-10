# Minimal fixture

A three-document corpus with two source types, a five-code codebook (plus one retired code), a corpus manifest, a long-format coded-data table under codebook `v2`, and the frequency summary that follows from it. It exists so that a change to the skill can be checked against a known-good result instead of by re-reading the skill.

| File | What it is |
|------|------------|
| `sources/INT-01.txt`, `sources/INT-02.txt` | Two short semi-structured interviews (elicited talk); unit = answer |
| `sources/REP-01.txt` | One annual-report section (institutional document); unit = section |
| `codebook.csv` | Codebook with `Status` column; `OLD_01` is `inactive` and must not be used |
| `manifest.csv` | One row per document (or part): parent document, source file, source type, unit count, status, codebook version |
| `coded_data.csv` | One row per **code assignment** (long format); provenance, `Prompting` and `Review` per row |
| `frequencies.csv` | `Assignments`, `Units` and `Documents` per code |

## Expected result

```
python3 scripts/validate_coding.py \
  --coded examples/minimal/coded_data.csv \
  --codebook examples/minimal/codebook.csv \
  --manifest examples/minimal/manifest.csv \
  --sources examples/minimal/sources \
  --summary examples/minimal/frequencies.csv \
  --codebook-version v2
```

must end with `RESULT: PASS` with eight `PASS` lines (seven without `--codebook-version`) and no `WARN`. Any `FAIL` means either the fixture or the validator has changed. `RESULT: INCOMPLETE` means a required check did not run — it is not a pass.

## What the fixture exercises

- **Prompting at assignment level.** INT-01 unit 1 carries both a `prompted` assignment (price, which was asked about) and a `volunteered` one (trust, which was not). INT-02 unit 1 contains both a rejection of relationships as a criterion (`TRUST_REJ`) and an admission that they count (`TRUST_01`) — both are kept, with a coder note.
- **Source types kept apart.** The report rows carry `n/a` for Prompting and `naturally occurring` for Elicitation; frequencies are per code across both types here because the corpus is too small to stratify, and the method note of a real analysis would say so.
- **Inactive code.** `OLD_01` is in the codebook with `Status = inactive`; using it would produce a warning.
- **Review flag.** A-007 (INT-02 unit 1, `TRUST_01`) carries `Review = competing_codes` with the competing code named in Coder notes, because the same answer also rejects relationships as a criterion (`TRUST_REJ`). The assignment stands; the flag says a human should look at it. The review share reported for this fixture is therefore 1 of 12 assignments.

## Breaking it on purpose

Edit a copy of `coded_data.csv` and re-run: change one excerpt so it no longer matches the source (changing its case is enough — the match is case-exact, only whitespace is normalized), point a row at `SCORE_99`, duplicate a row, or set `Prompting` to `maybe`. Each produces a `FAIL` line naming the assignment. Change a number in `frequencies.csv` and the regenerated count is reported next to it. Set `Review` to `maybe`, or to `other` with empty Coder notes, and the row fails; set `other` on more than a fifth of the flagged rows and a `WARN` says the reason list is too short. Blank the `Source file` column in a copy of `manifest.csv`, or drop `--summary` or `--sources`, and the result is `RESULT: INCOMPLETE` with exit status 2 — the checks that could not run are listed as `SKIP` lines.
