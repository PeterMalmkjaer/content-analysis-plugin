# Addendum deviations and run log — beta.5 test on fresh comments

Written as the work proceeds. `protocol_addendum.md` and `splits_addendum.json` are frozen (see `protocol_addendum.sha256`) and are not edited.

## AD1 — Batch composition in run 2 (12 Nov 2026, before any fresh comment was coded)

The addendum says run 2 uses "different batch composition". While preparing the batches I checked what the benchmark had actually done: `protocol.md` says "different batch order in run 2", and the code did exactly that — run 2 coded the **same ten batches of 50 comments** as run 1, numbered in a different order, each by a fresh subagent. The benchmark report (Table 1, row "Runs") wrongly said "different batch composition". That sentence is corrected in the report (erratum, 12 Nov 2026); no figure is affected.

For the fresh test the addendum is followed as written: in run 2 the 500 comments are shuffled (seed 20260910 + 2) before being cut into batches of 50, so no run-2 batch equals a run-1 batch. Within a run, all three arms code identical batches. This makes the two runs more independent than in the benchmark, which is the stricter reading of "holds in both runs".

## AD2 — Prompt wording for arms E and F (12 Nov 2026, before coding)

Arm A's prompt is byte-identical to the benchmark's arm-A prompt apart from file paths (checked by diff). For arms E and F the sentence that in arms B/C summarised the eight steps is replaced by: "Follow Step 7, which gives two coding procedures and says which one applies from the codebook's calibration status", followed by the status (E: uncalibrated; F: calibrated, one Step 5b round). The prompt does not say which procedure to use or what it contains — the skill text has to carry that.

## AD3 — Run log (12 November 2026)

60 subagent calls, all on `claude-opus-5-5` (model name read from the harness's subagent transcripts): 20 per arm. No omitted comments, no gap batches, no invalid codes, no repaired rows, no `neutral` combined with an emotion. Validator `RESULT: PASS` for all six outputs. Blindness audit: every tool call of every subagent was a Read or Write of a file its prompt names. The transcripts hold tool calls and the one-line reply only, so which of Step 7's two procedures a coder followed cannot be read from them.

## AD4 — Analyses added after the results were known

`explore_fresh.py` (macro-F1 intervals, micro-F1 excluding neutral, the split of both arms by arm E's and arm F's flag, flag kinds) was written after `analyse_fresh.py` had produced the pre-registered results. Its output is reported as exploratory.

## AD5 — Corrections to the first report made on the same day

(1) Row "Runs" in the design table: see AD1. (2) The human–human κ values quoted from Demszky et al. (2020) had been taken from a secondary summary and were marked unverified; they were checked against Table 7 of the paper's PDF and are correct as quoted. The description of how they are computed was made precise (two randomly sampled ratings per comment).

## AD6 — Outcome and release decision

H-E, H-F and H-R hold by the rules fixed in the addendum. The skill text at `08c38e5` is released unchanged as 5.0.0-beta.5. H-E holds narrowly: both point estimates are negative; this is stated in the report and in `README.md` rather than rounded to "equal".
