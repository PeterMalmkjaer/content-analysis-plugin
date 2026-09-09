# Source Types and Source Context

Content analysis draws inferences from text to the context of its use (Krippendorff, 2018) — which includes who produced it and for whom. That only works if the context is stated rather than assumed. This reference covers what to record about a source before coding it, how the main source types differ, what those differences do to the unit, the coding logic and the reliability you can expect, and when a corpus is too heterogeneous to be treated as one.

Read this reference when the corpus is anything other than a single set of documents of one kind, or when the user cannot say who produced the text and for whom.

---

## Table of Contents

1. [The Source Declaration](#the-source-declaration)
2. [Source Types Compared](#source-types-compared)
3. [Elicited Talk: Interviews and Focus Groups](#elicited-talk-interviews-and-focus-groups)
4. [Institutional Documents](#institutional-documents)
5. [Media Texts](#media-texts)
6. [User-Generated Content](#user-generated-content)
7. [Open Survey Responses](#open-survey-responses)
8. [Naturally Occurring Records](#naturally-occurring-records)
9. [Heterogeneous Corpora: The Gate](#heterogeneous-corpora-the-gate)
10. [Provenance Columns](#provenance-columns)
11. [Reporting](#reporting)

---

## The Source Declaration

Before coding, record the following for every source (or for every homogeneous group of sources). The declaration is made in Step 1, next to the research question and the unit of analysis. Part of it travels with every coded unit as provenance columns (section 10); the rest is recorded in the corpus manifest and the method note.

| Field | What to record | Why it matters |
|-------|----------------|----------------|
| **Source type** | One of the types in section 2 | Sets the natural unit and the traps |
| **Producer** | Who wrote or said it (role, not name, unless names are the point) | Whose voice is being analyzed |
| **Purpose** | Why the text exists — to inform, persuade, comply, vent, answer a question | Purpose shapes what is said and what is left out |
| **Audience** | Who the text was for | Self-presentation varies with audience |
| **Elicitation** | `elicited` (produced in response to a researcher's prompt) or `naturally occurring` | Elicited text must be read against the prompt |
| **Date / period** | When produced | Comparability over time; events that shaped it |
| **Language and translation** | Original language; whether coded in translation | Translation is an interpretive step |
| **Sampling** | How this source came to be in the corpus | Population the findings can speak to |
| **Completeness** | Whole document, excerpt, or truncated | Truncation is a disclosure, not a footnote |

If the user cannot fill a field, record `unknown` explicitly. An unknown producer or purpose is itself a limitation to report.

---

## Source Types Compared

| Type | Producer and purpose | Natural unit | Coding logic that fits | Reliability outlook | Signature trap |
|------|---------------------|--------------|------------------------|---------------------|----------------|
| **Elicited talk** (interviews, focus groups) | Participant answering a researcher | Answer to a question; speaking turn | Inductive, abductive, directed | Moderate; meaning is latent | Reading answers as spontaneous when they are responses to a specific prompt |
| **Institutional documents** (annual reports, policies, strategies) | Organization presenting itself to a known audience | Section; paragraph | Deductive, directed; summative for keyword tracking | High; manifest content, structured | Boilerplate repeated year on year inflates frequencies |
| **Media texts** (news, features, editorials) | Journalist/outlet within genre conventions and an editorial line | Article; paragraph; headline separately | Deductive framing schemes; summative | Moderate–high | Headline and body can carry different frames; outlet is a variable, not noise |
| **User-generated content** (comments, reviews, posts) | Anonymous individuals, unprompted, on a platform with its own affordances | Post/comment; thread as context | Inductive; summative with caution | Low–moderate; short, ironic, noisy | A comment without its parent is uninterpretable; bots and duplicates |
| **Open survey responses** | Respondent answering one fixed prompt in a few words | Whole response | Deductive or inductive at low granularity | Moderate | Prompt wording is the context; responses are not comparable across differently worded items |
| **Naturally occurring records** (minutes, emails, chat logs, transcripts of ordinary talk) | Participants acting, not reporting | Message; turn; agenda item | Inductive, abductive | Varies with genre | Records were made for the participants' purposes, not the researcher's; what is routine is unrecorded |
| **Continuous prose** (books, speeches, essays) | An author with a rhetorical aim | Paragraph; section | Any | High for manifest, lower for latent | Length dominates frequency tables; normalize per 1,000 words |

The table is a starting point. The user's material may straddle types; when it does, declare which row governs the unit and say why. Continuous prose has no section of its own below: the table row and the normalization rule in section 9 cover it.

---

## Elicited Talk: Interviews and Focus Groups

This is the type where context errors are hardest to see, because the text reads as if the participant chose the topic. They did not — the interviewer did.

**The question is the context unit.** The unit is the answer; the question that produced it is its context (Krippendorff's distinction between recording unit and context unit), and it must be recorded — carry it in the `Parent / section` column. Code an answer in light of the question that produced it. A participant who mentions "trust" because they were asked about trust is not evidence of a trust theme in the same way as one who raises it unprompted. Record, per unit, whether the topic was `prompted` or `volunteered`. When the interview guide is available, load it before coding and treat it as the map of what was elicited.

**Unit choices and their consequences.** *Speaking turn* preserves the dialogue but produces many units and splits an answer that spans several turns. *Answer* (everything the participant says in response to one question, across turns) matches the elicitation structure and is usually the right unit for semi-structured interviews. *Paragraph* is a transcription artifact and should not be used unless the transcript was paragraphed by meaning. Whichever is chosen, say in the method note how interviewer turns were handled: excluded from coding but retained as context is the usual answer.

**Participants are documents.** Use a stable participant identifier as the document ID. Keep participant-level metadata (role, group, time point) in the corpus manifest, not in the transcript. For longitudinal designs, the document is the participant × time point, and the manifest must carry both.

**Focus groups.** Attribution of turns to speakers is often uncertain in transcripts; declare how uncertain turns were handled. Group dynamics — agreement cascades, a dominant speaker — are context that a code-frequency table will not show; note them as memos.

**What the interviewer did is data.** Leading questions, reformulations, and interruptions shape the answers. If the same interviewer conducted all interviews, that is a constant; if several did, interviewer is a variable and belongs in the manifest.

---

## Institutional Documents

Annual reports, sustainability reports, policy documents, strategies, and press releases are produced by organizations for known audiences, often under disclosure rules, and often by reusing last year's text.

**Boilerplate.** Identify repeated passages across documents or years before coding. Either code them once and mark recurrence, or exclude them and say so. A frequency table that counts the same paragraph five times says something about disclosure practice, not about content.

**Structure is context.** A section heading tells you what the organization thinks the passage is for. Use section as the unit where the document is sectioned, and carry the section title as a provenance field.

**Audience shapes voice.** A letter to shareholders and a risk section in the same report are written for different readers. Treat them as different sub-sources if the research question turns on tone or emphasis.

---

## Media Texts

News and feature articles come with a genre, an outlet, and an editorial line. Outlet is a variable; record it. Headline and lead are written to a different logic than the body and may carry a different frame — code them as separate units or exclude them and say so. Wire copy reprinted across outlets is the media equivalent of boilerplate.

---

## User-Generated Content

Comments, reviews, and posts are short, unprompted, anonymous, and shaped by the platform (character limits, threading, voting). Three rules:

1. **Keep the thread.** A reply is a unit only together with what it replies to. Carry the parent ID as provenance.
2. **Expect noise.** Sarcasm, in-jokes, bots, duplicates, and spam are part of the material. Decide before coding what is excluded, and report the exclusion rate.
3. **Do not pool with long-form sources.** A 12-word comment and a 40-page report are not comparable counting units. Analyze separately or normalize (section 9).

Summative (keyword) analysis is tempting for this type and often misleading: the same word carries opposite meanings in a review and in a meme.

---

## Open Survey Responses

Each response is a short answer to one fixed prompt. The prompt is the context; responses to differently worded prompts are not one corpus. Code at whole-response level unless responses are long. Expect many near-identical responses; they are genuine data, not duplicates. Respondent metadata from the closed items of the same survey belongs in the manifest and enables the cross-tabulations that give this source type its value.

---

## Naturally Occurring Records

Meeting minutes, email threads, chat logs, and transcripts of ordinary talk were produced for the participants' own purposes. Their strength is that nobody was performing for the researcher; their weakness is that what participants took for granted was never written down. Genre conventions matter: minutes summarize and sanitize; chat logs are elliptical. Declare the genre and its known omissions.

---

## Heterogeneous Corpora: The Gate

A corpus that mixes source types is legitimate — triangulation across sources is a strength of content analysis — but only if the mixture is declared and handled. Apply the following test before Step 4.

**The unit test.** Can the unit of analysis be defined in the same way across all sources? If a "paragraph" of an annual report and a "paragraph" of a comment thread would not be read the same way, the answer is no. If the answer is no, the corpus is not one corpus: stratify by source type, code each stratum under the same codebook but with genre-aware inclusion criteria, and compare across strata rather than pooling.

**Genre-aware inclusion criteria.** A shared codebook is only genuinely shared if each code's inclusion criteria say what the code looks like in each source type. "Expresses distrust" manifests differently in a CEO letter and a Reddit thread. Where the manifestation differs, write it into the criteria; where it cannot be reconciled, the code is not shared.

**Never pool frequencies across genres without normalizing.** Report per-stratum frequencies. If a corpus-wide figure is wanted, normalize per unit count or per 1,000 words and say which.

**Declare the composition.** The method note states the number of documents and units per source type. A reader must be able to see that, say, 90% of the units came from one source type before interpreting a corpus-wide theme.

**When to refuse the pooling.** If the research question requires a single answer across sources whose units cannot be aligned, the honest output is a comparative analysis, not a merged one. Say so to the user before coding, not after.

---

## Provenance Columns

The coded data table (Step 7) carries the source declaration as columns, so that every unit can be filtered, compared, and reported by source:

| Column | Content |
|--------|---------|
| **Source type** | From section 2 |
| **Producer** | Role or organization |
| **Elicitation** | `elicited` / `naturally occurring` (source level) |
| **Prompting** | For elicited text: `prompted` / `volunteered` per unit; otherwise `n/a` |
| **Date** | Of production |
| **Parent / section** | Thread parent ID, document section title, or the interview question that produced the answer |
| **Language** | Original; `translated` if coded in translation |

These are in addition to Document ID, Unit ID, and the coding columns. When a corpus has a single homogeneous source, the columns are constant — keep them anyway; the method note is derived from them.

---

## Reporting

The method note (see Methodological Transparency in `SKILL.md`) states, for each source type in the corpus: what it is, who produced it and for what audience, whether it was elicited, how it was sampled, how many documents and units it contributed, what was excluded (boilerplate, interviewer turns, spam) and at what rate, and how heterogeneity was handled — stratified, normalized, or refused. If the coded units are translations, say so. If the elicitation instrument (interview guide, survey prompt) is available, append it.

---

## Key Sources

- Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology* (4th ed.). Sage. — Chapters on unitizing and on the context of inference.
- Neuendorf, K. A. (2017). *The Content Analysis Guidebook* (2nd ed.). Sage. — Sampling and unit decisions for media and institutional corpora.
- Schreier, M. (2012). *Qualitative Content Analysis in Practice*. Sage. — Building coding frames across heterogeneous material.
