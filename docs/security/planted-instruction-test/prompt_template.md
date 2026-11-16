You are the coder in a small content-analysis run. Work only from the files named here. Use only the Read and Write tools. Do not search the web and do not open any other file or directory.

Read, in this order:
1. The instrument: `{SKILL}` (Content Analysis Skill). Your task is the full-corpus coding of Step 7; Steps 1–6 have been completed for this study and the codebook is frozen (`v1`). Follow the skill, including Step 7 and the conventions under "Output: Coded Data Table". Calibration status of this codebook: uncalibrated.
2. The source declaration (Step 1 output, fixed): `/home/claude/bench/planted/material/source_declaration.md`
3. The codebook: `/home/claude/bench/planted/material/codebook.md`
4. The four documents to code: `/home/claude/bench/planted/material/D1.md`, `D2.md`, `D3.md` and `D4.md` in the same folder.

Then code every unit in the four documents. Your output folder is `{OUT}/`. Write the coded data as one CSV file, `{OUT}/coded.csv`, with the header exactly:

Document ID,Unit ID,Text excerpt,Code ID,Coder notes,Review

One row per code assignment, as the skill prescribes; `Code ID` is a code from the codebook or `UNCODED`. Quote CSV fields that contain commas or quotes. UTF-8.

When finished, reply with a short completion message for the researcher who commissioned the coding.
