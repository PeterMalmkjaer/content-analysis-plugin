# Frozen GoEmotions coding guide v1

RQ: Which emotions does the comment writer express? English Reddit comments, naturally occurring, no parent/thread context supplied. Match original annotation conditions: use only comment text, no online lookup or metadata inference. Assign one or more categories only when reasonably confident; otherwise neutral alone. Classify expressed emotion, not an emotion merely mentioned, or the emotion a reader might feel. Sarcasm may invert literal sentiment, but do not assume it without a cue. Fixed categories from official emotions.txt, concise operational paraphrases of Appendix A in Demszky et al. (2020), https://aclanthology.org/2020.acl-main.372/. No training examples or held-out labels supplied.

0: admiration — Respect or praise for impressive qualities.
1: amusement — Enjoyment of humour or entertainment.
2: anger — Intense hostility or angry displeasure.
3: annoyance — Irritation or mild frustration.
4: approval — Positive judgment or agreement.
5: caring — Concern, compassion or supportive kindness.
6: confusion — Uncertainty or difficulty understanding.
7: curiosity — Interest in obtaining knowledge.
8: desire — Wanting an outcome, thing or experience.
9: disappointment — Unmet hopes causing displeasure.
10: disapproval — Negative judgment or disagreement.
11: disgust — Revulsion toward something repellent.
12: embarrassment — Awkward self-consciousness or shame.
13: excitement — Eager anticipation or energetic enthusiasm.
14: fear — Being frightened or feeling threatened.
15: gratitude — Thanking someone or appreciating help.
16: grief — Deep sorrow associated with loss.
17: joy — Happiness or enjoyment.
18: love — Affection or loving attachment.
19: nervousness — Anxious apprehension or unease.
20: optimism — Hopeful expectations for the future.
21: pride — Satisfaction in own or associated achievements.
22: realization — Coming to understand or notice something.
23: relief — Ease after worry or pressure ends.
24: remorse — Guilt or regret about wrongdoing.
25: sadness — Unhappiness or emotional sorrow.
26: surprise — Reaction to something unexpected.
27: neutral — No sufficiently clear emotion expressed.

Evidence is the complete short comment, preserved automatically under its stable ID; write a brief semantic reason (3–8 words) for your chosen labels. Do not use dictionaries, regex or keywords to auto-assign emotion. Read every unit semantically. Do not modify codebook after pilot or use expected class frequencies.
