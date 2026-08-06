# Protocol-Driven and Unattended Runs

This reference applies when a content analysis is commissioned **in writing** rather than negotiated
in conversation. The main workflow in `SKILL.md` assumes a dialogue: Step 1 says to *establish the
research question with the user*. That assumption fails when nobody is available to answer.

This file supplies the three rules that replace it.

---

## When This File Applies

Read this file before Step 1 if **any** of the following is true:

1. **A written brief or protocol defines the task.** The instructions arrived as a document — a
   protocol file, a specification, a commissioning note — rather than as a request in conversation.
2. **The run is unattended.** The session was started on a schedule, or the user has said they will
   check back later, or the run is otherwise expected to complete without supervision.
3. **The deliverables were named in advance.** The brief lists specific output files, formats, or
   destination paths.

If none of these hold, ignore this file and follow `SKILL.md` as written.

---

## Rule 1 — Derive the Research Question; Never Proceed Without One

A written brief very often specifies *what to do* (unit of analysis, coding logic, deliverables) but
never states *what the analysis is for*. Step 1's instruction to establish the research question with
the user cannot be followed, and the brief's deliverable list is not a substitute: a list of output
files describes a product, not a question.

**Do not silently drop the research question.** A content analysis without a stated question cannot
be evaluated by a reader, and the analyst has no criterion for deciding which findings matter.

Procedure:

1. **Look for a stated question first.** Read the brief for an explicit research question, aim,
   problem statement, or purpose. If one exists, use it verbatim and attribute it to the brief.
2. **If none exists, derive one from the brief's own terms.** Take the dimensions the brief asks you
   to code and the material it points to, and formulate the narrowest descriptive question those
   dimensions jointly answer. Do not import a question from your own assumptions about the domain,
   from the corpus's apparent purpose, or from what the material seems to be evidence *for*.
3. **Label it as derived.** Write it into the report marked explicitly as derived from the brief and
   open to correction — for example: *"The protocol states no research question. The following is
   derived from its own terms and should be confirmed."*
4. **Decompose it.** Break the question into one sub-question per coded dimension, and map each to
   the report section that answers it. This makes the analysis auditable: a reader can check that
   every question was answered and every dimension was used.
5. **Keep it descriptive.** Content analysis answers *what*, *how often*, and *in what way*. If the
   brief implies a causal or evaluative question, state in the report that the method cannot answer
   it, and answer the descriptive question that lies underneath.

**Boundary case — briefs that are deliberately blind.** Some protocols restrict what may be read
precisely so that categories emerge without contamination from a surrounding argument. Deriving a
research question must respect that restriction: derive it from the brief, not from material the
brief put out of bounds. If the permitted material reveals something about the wider purpose, say so
in the report rather than acting on it.

---

## Rule 2 — Use the Full Report Skeleton

In a conversation, context is shared and much can be left implicit. A written brief usually means the
report will be read by someone who was not present — a reviewer, a co-author, a future self. The
method note described in `SKILL.md` is not sufficient on its own; it must be embedded in a report
that opens with the task and the question.

Use this section order:

| § | Section | Contains |
|---|---------|----------|
| 1 | **The task** | What the brief asked for, in the brief's own terms; any constraints it imposed; what the task explicitly excludes |
| 2 | **Problem statement and analysis questions** | The research question (stated or derived, labelled as such); sub-questions in a table mapping each to its dimension and to the section that answers it |
| 3 | **Constraints declaration** | Only if the brief imposed restrictions (blindness rules, source limits, time bounds): a point-by-point statement of compliance, and every deviation, including choices that were defensible but not obvious |
| 4 | **Method** | Design, corpus, unit of analysis, coding procedure, category system, reliability |
| 5 | **Findings** | One subsection per analysis question, labelled with the question it answers |
| 6 | **Uncertainties and limitations** | Where reliability is too low to bear a conclusion, stated at the conclusion itself; what would resolve each uncertainty |
| 7 | **Deliverables** | Every file produced, with a one-line description |
| 8 | **Method references** | Methodological sources, each marked verified or unverified |

Sections 3 is omitted when no constraints were imposed. All others are required.

**Report a deviation as a deviation, not as a footnote.** If a sample was used where the brief implied
a census, if units were truncated, if a dimension was computed rather than coded — say so in §3 (or
§4 where no §3 exists), with the count. A reader who discovers it themselves will discount everything
else in the report.

---

## Rule 3 — The Brief's Formats Take Precedence

`SKILL.md`'s *Output File Conventions* section specifies `.xlsx` for codebooks, coded data, frequency
reports and reliability reports. Those are defaults for an unspecified request, not requirements.

When a brief names its own deliverables:

- **Produce exactly the named files, with the named names, at the named paths.** Do not add the
  skill's default outputs alongside them, and do not substitute a different format because it is the
  skill's convention.
- **Map the skill's content onto the brief's containers.** If the brief asks for a codebook as `.md`,
  the codebook still needs code ID, name, definition, inclusion criteria, exclusion criteria and an
  anchor example — the format changes, the substance does not.
- **If the brief omits something the method requires** — most often reliability figures — put it in
  the nearest named deliverable rather than creating an unrequested file, and note where you put it.
- **If a named deliverable cannot be produced**, say so explicitly and deliver everything else. Do
  not silently substitute.

---

## Rule 4 — Do Not Block in an Unattended Run

`SKILL.md` describes several points where the user is consulted: confirming the research question,
reviewing the draft codebook, approving revisions after pilot coding. In an unattended run these
become deadlocks.

Instead:

- Make the most defensible choice, **state the assumption in the report at the point it applies**,
  and continue.
- Where the choice is close, record the alternative you rejected and why. That turns a silent
  judgement call into something the reader can overturn.
- Stop only when every remaining path is irreversible and the choice is genuinely the commissioner's.
  Then do all the preparatory work that is safe, and explain exactly what decision is needed.

---

## Worked Example

**Brief received (paraphrased):** *"Open, inductive content analysis of the log files in `corpus/`.
Coding unit: one session entry. Code at minimum: what is worked on, what problems occur and who
causes them, how they are discovered and handled, and phases over time if the data suggest them.
Deliver: codebook.md, codings.csv, frequencies.md, report.md. Read nothing outside `corpus/`."*

**What Rule 1 produces.** The brief states no research question. Its dimensions are activity,
problem, agency, discovery, handling and time. The narrowest descriptive question they jointly
answer: *"What does this work consist of as recorded by its own contemporaneous logs — what occupies
it, what goes wrong, who is held responsible, how are problems found and dealt with, and how does the
pattern shift over time?"* Written into §2, labelled derived, decomposed into five sub-questions
mapped to the six coded dimensions.

**What Rule 2 produces.** §1 restates the four-part task and the read-restriction. §3 declares
compliance with the restriction and discloses three choices that were defensible but not obvious: the
codebook was induced from a sample rather than the full corpus, the longest units were truncated, and
the time dimension was computed from dates rather than coded.

**What Rule 3 produces.** Four files with exactly those names — not `.xlsx`. Reliability figures are
placed in `report.md` under Method, since the brief named no reliability file, and the report says so.

**What Rule 4 produces.** The codebook is not held for approval before full coding; it is applied,
and the sections of it that a reader is most likely to dispute are flagged in §6.
