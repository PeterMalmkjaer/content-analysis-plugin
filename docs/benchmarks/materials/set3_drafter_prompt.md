You are developing the codebook for a content analysis (Step 4 of the instrument). Work only from the files named here. Use only the Read and Write tools. Do not search the web, do not open any other file or directory, and do not modify any file except the output file.

Read, in this order:
1. The instrument: `/home/claude/bench/skill-beta4/skills/content-analysis/SKILL.md` (Content Analysis Skill 5.0.0-beta.4). Your task is Step 4, "Develop the Coding Scheme", for a deductive design: the category set and the definitions are given and fixed; what is missing is the instrument's **decision-rule columns**. Read Step 4 in full, and Step 7's decision procedure so that you know how the columns will be used.
2. The source declaration (Step 1 output, fixed, including the co-coding rule for the neutral category): `/home/claude/bench/materials/set3_source_declaration.md`
3. The existing codebook (category names and definitions, fixed): `/home/claude/bench/materials/set3_codebook_A.md`
4. The development material — 400 comments from the same corpus, texts only, no labels: `/home/claude/bench/materials/set3_development_texts.md`. Read all of it before writing rules; this is the Step 4 development read.

Then write the extended codebook to `/home/claude/bench/materials/set3_codebook_B.md`:

- Start with the complete text of the existing codebook, **verbatim and unchanged** (research question, instructions, the 28 category lines).
- Then add a section `## Decision rules` with one entry per category (all 28, in the codebook's order). Each entry gives the instrument's decision-rule columns exactly as Step 4 defines them: **Required textual basis** · **Nearest alternative codes** · **Decisive difference** · **Boundary example** · **Co-coding rule** · **Gate**. Follow Step 4's own rules on which columns must be filled for every code and which may stay blank, and on where examples may come from: a boundary example is either quoted verbatim from the development material (give its ID) or written by you and marked `(constructed)`.
- Do not change, add or remove categories or definitions. Do not contradict the source declaration's co-coding rule.
- No reference labels, human codings or expected frequencies exist in your inputs; do not guess at them, and do not write rules aimed at any assumed label distribution. Base the rules on the definitions and on what you observe in the development texts.

When finished, reply with one line: the number of categories for which each of the six columns was filled (e.g. "basis 28, alternatives 22, difference 22, boundary 20, co-coding 28, gate 0"). Nothing else.
