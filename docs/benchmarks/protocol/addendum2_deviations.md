# Addendum 2 deviations and run log — beta.6 candidate on a second fresh sample

Written as the work proceeded. `protocol_addendum2.md` and `splits_addendum2.json` are frozen (see `protocol_addendum2.sha256`) and are not edited.

## A2-1 — Run log (13 November 2026)

101 subagent calls, all on `claude-opus-5-5` (model name read from the harness's subagent transcripts): 20 per arm, plus one gap batch. One comment (`T03870`) was omitted by one batch of arm A, run 1, and coded by a fresh blind subagent with the same prompt, as `deviations.md` D7 prescribes. No other omissions, no invalid codes, no repaired rows, no `neutral` combined with an emotion. Validator `RESULT: PASS` for all ten outputs. Four subagents used Edit on their own output file, which the audit rule allows. Blindness audit: every tool call of every subagent was a Read, Write or (own output) Edit of a file its prompt names.

## A2-2 — Analyses added after the results were known

`explore_fresh2.py` (the split of arms E and H by their own flag against arm A on the same comments, precision and recall of `neutral`, macro-F1 intervals, flag kinds) was written after `analyse_fresh2.py` had produced the pre-registered results. Its output is reported as exploratory. E − A and G − A were computed by `analyse_fresh2.py` alongside the pre-registered comparisons; they have no decision rule and are reported for reference.

## A2-3 — Cost

About $47 at list price with assumed cache multipliers, against an estimate of $35–40 given to the repository owner beforehand; the fifth arm (beta.5 on the same comments, needed for a paired comparison with beta.6) was added when the design was fixed, before coding, and the owner was told then.

## A2-4 — A cost expectation that did not hold

Before the test the orchestrator told the repository owner that a shorter calibrated procedure would make a run about a fifth cheaper. Measured: arm G cost $10.74 per 1,000 codings against $10.82 for arm J. The expectation was wrong; cost follows the length of the codebook and the skill text, not the number of procedure steps.

## A2-5 — Outcome and release decision

H-1 holds as direction only; H-2, H-3, H-4 and H-5 hold; the release rule is met. The text at `d510a60` is released unchanged as 5.0.0-beta.6. The changelog and the summary say "direction only", not "improves". Arm G: no demonstrated difference; the variant text (`ddb7a48`) is not released, as fixed in advance.

## A2-6 — Statements in the published documentation revised in the light of this test

(1) `README.md` in this folder and the repository README said that beta.5 without calibration was "not distinguishable" from beta.3. On this sample its shortfall has an interval that excludes zero in both runs; the summaries now say that beta.5 was about two points below beta.3. (2) "Which part does the work" was listed as not shown; arm G gives a partial answer and the summary now states it. (3) The gain in macro-F1 seen in the first fresh sample did not recur; the summaries say so.
