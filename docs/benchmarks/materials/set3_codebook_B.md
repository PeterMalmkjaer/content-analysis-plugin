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

## Decision rules

Decision-rule columns per Step 4 of the instrument (Content Analysis Skill 5.0.0-beta.4). Developed from the definitions above, the source declaration and the Step 4 development read of 400 unlabelled comments (IDs T…). No pilot or calibration has yet been run. *Nearest alternative codes*, *Decisive difference* and *Boundary example* are filled for every code: in a 28-category emotion scheme every code has adjacent categories on the same valence scale and every code competes with `neutral` (Step 4 names exactly this as the typical locus of confusion), and the development read showed concrete competing cases for each. The calibration (Step 5b) will test and revise them. *Gate* is blank for every code: no code in this scheme depends on another code being assigned first.

General rules that apply to every entry:
- The writer must *express* the emotion. An emotion word that is mentioned, quoted, attributed to someone else, negated, or used as a topic does not meet any required textual basis.
- Emotion words are evidence, not triggers (the codebook forbids keyword assignment): every basis is judged on what the comment as a whole expresses.
- Sarcasm inverts literal sentiment only with a cue in the text (e.g. `/s`, an absurd contrast, an ironic emoji); the inverted reading is then coded.
- Emotion codes may co-occur freely with each other, subject to the exclusions stated per entry; `neutral` is never combined with any emotion (source declaration).
- Uncertainty is recorded in `Review`, never by choosing `neutral`.

### 0: admiration
- **Required textual basis:** The writer praises a specific person, thing, act or quality as impressive, excellent or beautiful (e.g. "[NAME] was a great coach", "What a beauty", "I was impressed").
- **Nearest alternative codes:** approval; love; joy.
- **Decisive difference:** vs approval — admiration praises a *quality of the target* as impressive; approval endorses a claim, idea or action as right or acceptable ("good idea", "true"). vs love — admiration is esteem; love is affection or attachment. vs joy — admiration is directed at the target's merit; joy is the writer's own happiness.
- **Boundary example:** T04587 "More admired than [NAME] [NAME] is admired by starbucks baristas. Unemployed kids. And cat ladies" — the word "admired" reports others' esteem and the comment mocks; the writer praises nothing.
- **Co-coding rule:** May co-occur with any emotion code (commonly approval, gratitude, love, joy, excitement, surprise). Excludes neutral.
- **Gate:**

### 1: amusement
- **Required textual basis:** The writer signals that they find something funny or entertaining: laughter markers reacting to content (lol, lmao, haha, 😂, 🤣), "funny", "made me crack up", or a joke the writer plainly enjoys (playful cue such as :-P or teasing tone).
- **Nearest alternative codes:** joy; neutral; annoyance.
- **Decisive difference:** vs joy — amusement requires humour or entertainment as its object; joy is happiness without that object. vs neutral — a comment that merely mentions a joke, or a pun with no sign that the writer enjoys it, is not amusement unless the playful intent is unmistakable. vs annoyance/disapproval — a laughter token that only softens or sneers at a criticism ("That's just fucked lol") supports amusement only if the writer is also enjoying the humour; otherwise code the negative emotion alone.
- **Boundary example:** T00671 "Someone made a similar joke and got 500 down votes." — reports a joke; the writer expresses no enjoyment of it.
- **Co-coding rule:** May co-occur with any emotion code, including negative ones when the writer both laughs and criticises. Excludes neutral.
- **Gate:**

### 2: anger
- **Required textual basis:** The writer expresses intense hostility: insults or curses directed at someone ("Now fuck off", "Hey dumbass"), wishes of harm, shouted rage (all caps with hostile content), or explicit hatred of a target expressed with heat.
- **Nearest alternative codes:** annoyance; disapproval; disgust.
- **Decisive difference:** vs annoyance — intensity and hostility: anger attacks (insult, curse, violent wish, shouting); annoyance complains or is irritated without attacking. vs disapproval — disapproval is a negative judgement without emotional heat. vs disgust — disgust is revulsion at something repellent; anger is hostility toward an agent.
- **Boundary example:** T04042 "Love the gif but I bloody hate these kinds of captions. It's as annoying and cringey as a fully grown adult doing baby-talk." — "hate" here is mild irritation about a style of caption, stated with its own label "annoying"; annoyance, not anger.
- **Co-coding rule:** May co-occur with any emotion code (commonly disapproval, disgust); co-occurrence with annoyance is allowed only when the comment contains both a mild and a hostile passage. Excludes neutral.
- **Gate:**

### 3: annoyance
- **Required textual basis:** The writer expresses their own irritation, exasperation or mild frustration: complaint markers ("annoying", "frustrating", "Not cool", "smh", "Are you fucking serious?"), exasperated rhetorical questions, or a tone of being bothered.
- **Nearest alternative codes:** disapproval; anger; disappointment.
- **Decisive difference:** vs disapproval — annoyance requires that the writer's own irritation is expressed; disapproval needs only a negative judgement and can be calm (both may apply). vs anger — no hostile attack or intensity. vs disappointment — disappointment is a let-down of an expectation or hope; annoyance is being bothered.
- **Boundary example:** T04491 "That’s only really annoying if it’s excessively slow" — a conditional statement about when something would be annoying; the writer is not expressing irritation.
- **Co-coding rule:** May co-occur with any emotion code (commonly disapproval, disappointment). Excludes neutral.
- **Gate:**

### 4: approval
- **Required textual basis:** The writer endorses something: agreement with another view ("True!", "Exactly", "you're right"), or a positive judgement of an idea, choice or action ("Good idea", "Wise choice", "good call", "That sounds good").
- **Nearest alternative codes:** admiration; neutral; realization.
- **Decisive difference:** vs admiration — approval endorses something as right/acceptable; admiration praises impressive qualities. vs neutral — a bare "yes" that answers a factual question, or a plain confirmation of fact, is not approval; approval requires an evaluative stance toward a view, idea or action. vs realization — "that makes sense" is realization when the writer newly understands, approval when the writer judges a proposal sensible.
- **Boundary example:** T01603 "Yes owe I believe 13,000$ something on it currently." — "Yes" answers a factual question; nothing is endorsed.
- **Co-coding rule:** May co-occur with any emotion code; it may co-occur with disapproval when the comment endorses one thing and rejects another. Excludes neutral.
- **Gate:**

### 5: caring
- **Required textual basis:** The writer shows concern, compassion or supportive kindness toward another: sympathy for the other's situation ("I'm sorry to hear that friend"), well-wishing ("Good luck", "Bless u", "Happy cake day"), encouragement ("You got this", "reach out to whoever you can"), or advice framed around the other's wellbeing.
- **Nearest alternative codes:** sadness; remorse; optimism.
- **Decisive difference:** vs remorse — "sorry" is caring when it is sympathy for another's situation, remorse when it apologises for the writer's own wrongdoing. vs sadness — caring is directed at another's wellbeing; sadness is the writer's own sorrow (both may apply). vs optimism — wishing someone well ("Good luck") is caring; expecting a good outcome is optimism. Purely practical or instructional advice without concern for the person is not caring.
- **Boundary example:** T00142 "Only bet on games you like. Sometimes go a couple days without action. Betting just for the sake of staking something is never smart." — practical advice with no expressed concern for the person.
- **Co-coding rule:** May co-occur with any emotion code (commonly sadness, optimism, love, gratitude). Excludes neutral.
- **Gate:**

### 6: confusion
- **Required textual basis:** The writer states or shows that they do not understand or are uncertain: "I have no idea", "I can't understand why", "Wait a second what?", "I don't know how to feel", bewildered questions.
- **Nearest alternative codes:** curiosity; surprise; neutral.
- **Decisive difference:** vs curiosity — confusion expresses bewilderment or lack of understanding; curiosity seeks information without bewilderment (one question may carry both). vs surprise — surprise reacts to the unexpected; confusion is that something does not make sense. vs neutral — a hedge ("I think", "not sure if") that softens an opinion is not confusion.
- **Boundary example:** T00830 "Not sure if guys like that are better or worse than regular Incels." — "not sure" is a rhetorical put-down, not bewilderment.
- **Co-coding rule:** May co-occur with any emotion code (commonly curiosity, surprise, annoyance). Excludes neutral.
- **Gate:**

### 7: curiosity
- **Required textual basis:** The writer seeks information or shows interest in learning: a genuine question that wants an answer ("What was the end result of this?", "Care to explain?", "Do you have the voting link?"), "I wonder", or explicit interest ("Interesting read").
- **Nearest alternative codes:** confusion; disapproval; annoyance.
- **Decisive difference:** The question must be information-seeking. A rhetorical question that makes a point, challenges or mocks is not curiosity; code the judgement or irritation it carries (disapproval, annoyance) instead. vs confusion — see confusion.
- **Boundary example:** T00389 "Other than a lame attempt of being insulting, what part of anything you said has anything to do with what I said?" — rhetorical challenge; no information is sought.
- **Co-coding rule:** May co-occur with any emotion code (commonly confusion, surprise, caring). Excludes neutral.
- **Gate:**

### 8: desire
- **Required textual basis:** The writer states their own wanting or wishing for an outcome, thing or experience: "I want", "I wish", "I need your curly hair routine!", "give me Greedy", "I would watch".
- **Nearest alternative codes:** optimism; excitement; caring.
- **Decisive difference:** vs optimism — desire is wanting; optimism is expecting or hoping that it will happen. vs excitement — excitement adds energetic anticipation; wanting alone is desire. vs caring — wishing something good for another person is caring, not desire.
- **Boundary example:** T04500 "I want this back ""I want us back"" I missed the part where that's my problem" — the wanting is quoted from someone else; the writer dismisses it.
- **Co-coding rule:** May co-occur with any emotion code (commonly excitement, optimism). Excludes neutral.
- **Gate:**

### 9: disappointment
- **Required textual basis:** The writer expresses displeasure that something fell short of a hope or expectation: "sorta disappointing", "Shame", "too bad", "Good meme, but unfortunately the pic is fake", "I was hoping…" with a let-down.
- **Nearest alternative codes:** sadness; annoyance; disapproval.
- **Decisive difference:** vs sadness — disappointment requires an unmet expectation or hope; sadness is sorrow without that frame. vs annoyance — let-down versus being bothered. vs disapproval — a negative judgement of something versus the failure of an expectation.
- **Boundary example:** T04116 "Conservative is massively brigaded on an hourly basis. Unfortunately, it requires strict moderation or else it is unreadable." — "Unfortunately" states a practical constraint; no hope of the writer's is shown to be unmet.
- **Co-coding rule:** May co-occur with any emotion code (commonly sadness, annoyance, disapproval). Excludes neutral.
- **Gate:**

### 10: disapproval
- **Required textual basis:** The writer expresses a negative judgement of a person, act, idea or claim, or disagrees with someone: "No", "you're lying", "This is just wrong", "Misleading", "Not cool", criticism of conduct.
- **Nearest alternative codes:** annoyance; anger; neutral.
- **Decisive difference:** vs annoyance/anger — disapproval needs only the negative judgement; add annoyance or anger only if irritation or hostility is also expressed. vs neutral — a factual statement or alternative belief offered without rejecting or judging anything is neutral.
- **Boundary example:** T04341 "I thought they were motor vehicle accidents." — offers an alternative belief without a negative judgement of anyone or anything.
- **Co-coding rule:** May co-occur with any emotion code (commonly annoyance, anger, disgust, disappointment). Excludes neutral.
- **Gate:**

### 11: disgust
- **Required textual basis:** The writer expresses revulsion at something physically or morally repellent: "disgusting", "makes me sick", "stink", "human trash", "butt ugly".
- **Nearest alternative codes:** anger; disapproval; annoyance.
- **Decisive difference:** Disgust requires revulsion (the object is repellent, gross, vile); anger is hostility at an agent; disapproval and annoyance are judgement or irritation without revulsion.
- **Boundary example:** "The recipe calls for anchovies, which some people find gross." (constructed) — reports other people's revulsion; the writer expresses none.
- **Co-coding rule:** May co-occur with any emotion code (commonly anger, disapproval). Excludes neutral.
- **Gate:**

### 12: embarrassment
- **Required textual basis:** The writer expresses awkward self-consciousness or shame about themselves (or explicitly vicarious embarrassment): "oops", "awkward", "embarrassing", "so cringe" about own conduct.
- **Nearest alternative codes:** remorse; amusement; disapproval.
- **Decisive difference:** vs remorse — embarrassment is about how one appears; remorse is guilt about harm or wrongdoing. vs amusement — laughing at one's own mishap is amusement unless self-consciousness is expressed. vs disapproval — calling others' behaviour "cringey" is a judgement, not the writer's embarrassment.
- **Boundary example:** T04202 "I have no shame in saying I still have my blanket from when I was a child. And a favorite [NAME] plushie." — shame is explicitly denied.
- **Co-coding rule:** May co-occur with any emotion code (commonly amusement, remorse). Excludes neutral.
- **Gate:**

### 13: excitement
- **Required textual basis:** The writer expresses eager anticipation or energetic enthusiasm: "Let's gooooo", "Hell yes", "Yay!!", "pretty amped", "can't wait", enthusiastic exclamation tied to content.
- **Nearest alternative codes:** joy; desire; optimism.
- **Decisive difference:** vs joy — excitement is aroused and energetic, often forward-looking; joy is happiness or contentment. vs desire/optimism — wanting or calm expectation without energetic enthusiasm. Exclamation marks alone are not enough.
- **Boundary example:** T01400 "Excited for this project to be finished when I retire in 30 something years." — the absurd timeline is a sarcasm cue; the literal "Excited" is inverted (annoyance/disapproval), not excitement.
- **Co-coding rule:** May co-occur with any emotion code (commonly joy, desire, admiration). Excludes neutral.
- **Gate:**

### 14: fear
- **Required textual basis:** The writer is frightened or feels threatened: "scared", "Deathly afraid", "freaked me out", "terrifying".
- **Nearest alternative codes:** nervousness; surprise.
- **Decisive difference:** vs nervousness — fear is fright at a threat; nervousness is diffuse anxiety or worry. vs surprise — shock at the unexpected without a sense of threat.
- **Boundary example:** T00078 "death of fear is certain." — "fear" is a topic word; no fright is expressed.
- **Co-coding rule:** May co-occur with any emotion code (commonly nervousness, sadness). Excludes neutral.
- **Gate:**

### 15: gratitude
- **Required textual basis:** The writer thanks someone or expresses appreciation for help, kindness or information: "Thanks", "Thank you so much", "Cheers for the reply", "appreciate it".
- **Nearest alternative codes:** approval; admiration; caring.
- **Decisive difference:** Gratitude requires thanking or appreciation directed at a benefactor; approval or admiration evaluate without thanking. Thanks inverted by a sarcasm cue is not gratitude.
- **Boundary example:** T02051 "I hate you for that title. Thanks a lot. /s Right as I’m about to go to sleep too." — the `/s` cue marks the thanks as sarcastic.
- **Co-coding rule:** May co-occur with any emotion code (commonly joy, admiration, approval, realization). Excludes neutral.
- **Gate:**

### 16: grief
- **Required textual basis:** The writer expresses deep sorrow over a loss — a death or a comparably grave loss — as their own mourning.
- **Nearest alternative codes:** sadness; caring.
- **Decisive difference:** vs sadness — grief requires a loss and deep sorrow; general unhappiness is sadness. vs caring — condolence for another's loss is caring; grief only if the writer's own mourning is expressed.
- **Boundary example:** T03980 "Girl I went to school with was killed like this." — reports a death but expresses no sorrow.
- **Co-coding rule:** May co-occur with any emotion code (commonly sadness, caring). Excludes neutral.
- **Gate:**

### 17: joy
- **Required textual basis:** The writer expresses their own happiness, pleasure or enjoyment: "Glad to see…", "Happy that you're happy", "Yay", "Such season 1 vibes and I love it", a positive emoticon that conveys pleasure rather than mere politeness.
- **Nearest alternative codes:** amusement; excitement; love.
- **Decisive difference:** vs amusement — joy does not require humour. vs excitement — joy lacks the energetic, anticipatory quality. vs love — "I love it/this" about an experience or thing expresses enjoyment (joy); affection or attachment to a person, animal or thing is love; both may apply. A smiley used as a courtesy marker alone does not meet the basis.
- **Boundary example:** T00098 "That’s how you know they’re happy." — happiness is attributed to others, not expressed by the writer.
- **Co-coding rule:** May co-occur with any emotion code (commonly gratitude, admiration, love, excitement). Excludes neutral.
- **Gate:**

### 18: love
- **Required textual basis:** The writer expresses affection or loving attachment toward a person, animal, group or thing: "I love you", "i love this subreddit", "<3", "❤️", terms of endearment.
- **Nearest alternative codes:** joy; admiration; caring.
- **Decisive difference:** vs joy — see joy. vs admiration — affection versus esteem for qualities. vs caring — affection versus concern for the other's wellbeing. Quoted or sarcastic "love" (with a cue) does not count.
- **Boundary example:** T02639 """I love animals but I hate PETA."" - [NAME] — the declaration of love is a quotation attributed to someone else.
- **Co-coding rule:** May co-occur with any emotion code (commonly joy, admiration, gratitude, caring). Excludes neutral.
- **Gate:**

### 19: nervousness
- **Required textual basis:** The writer expresses anxious apprehension, worry or unease: "nervous", "anxious", "worried", "I dont know how I feel about…", "This hits a little too close to home".
- **Nearest alternative codes:** fear; confusion; caring.
- **Decisive difference:** vs fear — diffuse unease versus fright at a threat. vs confusion — anxious apprehension versus not understanding. vs caring — worry on another's behalf expressed as support is caring; the writer's own unease is nervousness.
- **Boundary example:** T04237 "It's good worrying about things that can be helped. Lol" — a general remark about worrying; the writer expresses no unease.
- **Co-coding rule:** May co-occur with any emotion code (commonly fear, confusion, sadness). Excludes neutral.
- **Gate:**

### 20: optimism
- **Required textual basis:** The writer expresses a hopeful positive expectation about a future outcome: "Hope so", "I think she has a good chance", "Maybe they'll change their mind one day!", "If we can get a 1st rounder it is without a doubt worth it" when framed hopefully.
- **Nearest alternative codes:** desire; caring; approval.
- **Decisive difference:** vs desire — expectation that a good outcome will come versus wanting it. vs caring — a well-wish for someone ("Good luck") is caring unless the writer also expresses expectation of a good outcome. vs approval — endorsing a plan versus hoping it succeeds. A neutral or negative prediction is not optimism.
- **Boundary example:** T00899 "Too many injuries. I predict he will be off the roster by September." — a prediction, but not a hopeful one.
- **Co-coding rule:** May co-occur with any emotion code (commonly desire, caring, excitement). Excludes neutral.
- **Gate:**

### 21: pride
- **Required textual basis:** The writer expresses satisfaction in their own achievement or that of a group they belong to: "proud", boasting of own feat ("Hell yeah I got the 420 upvote"), "We did it".
- **Nearest alternative codes:** joy; admiration; excitement.
- **Decisive difference:** vs admiration — pride concerns the writer or the writer's own group; admiration concerns others. vs joy — pride requires an achievement credited to self or own group.
- **Boundary example:** T03355 "I mean I would be a [NAME] and I’m pretty reasonable." — a self-description, not satisfaction in an achievement.
- **Co-coding rule:** May co-occur with any emotion code (commonly joy, excitement). Excludes neutral.
- **Gate:**

### 22: realization
- **Required textual basis:** The writer expresses that they have just come to understand or notice something: "Oh ok that makes sense then!", "D'oh, it's even in the title!", "Now I know…", "Turns out…", "I never knew that this is a thing".
- **Nearest alternative codes:** surprise; approval; neutral.
- **Decisive difference:** vs surprise — realization is a shift in understanding; surprise is the reaction to the unexpected (both may apply). vs approval — see approval. vs neutral — stating a belief or known fact without any marker of newly coming to know is neutral.
- **Boundary example:** T05090 "I think all coffee is keto already...." — states a belief; no shift in understanding is expressed.
- **Co-coding rule:** May co-occur with any emotion code (commonly surprise, gratitude, embarrassment). Excludes neutral.
- **Gate:**

### 23: relief
- **Required textual basis:** The writer expresses ease because a worry, burden or pressure has ended: "phew", "relieved", "thank god that's over", "it seems like I don't [need it] anymore" when a prior worry is implied.
- **Nearest alternative codes:** joy; gratitude.
- **Decisive difference:** Relief requires a prior worry or burden that has ended; positive feeling without that release is joy; thanks for the help that ended it is gratitude (both may apply).
- **Boundary example:** "Finally the season starts tomorrow!" (constructed) — "Finally" marks eager anticipation, not the end of a worry; excitement, not relief.
- **Co-coding rule:** May co-occur with any emotion code (commonly joy, gratitude). Excludes neutral.
- **Gate:**

### 24: remorse
- **Required textual basis:** The writer expresses guilt, regret or apology for their own wrongdoing or mistake: "I'm sorry I…", "my bad", "I regret", "I feel bad that I…".
- **Nearest alternative codes:** caring; embarrassment; sadness.
- **Decisive difference:** The writer's own fault is required. "Sorry" expressing sympathy for another's misfortune is caring (or sadness); a rhetorical or sarcastic "sorry" is neither. vs embarrassment — guilt about wrongdoing versus self-consciousness.
- **Boundary example:** T00009 "I’m sorry to hear that friend :(. It’s for the best most likely if she didn’t accept you for who you are" — "sorry" expresses sympathy, not guilt for the writer's own act.
- **Co-coding rule:** May co-occur with any emotion code (commonly sadness, embarrassment). Excludes neutral.
- **Gate:**

### 25: sadness
- **Required textual basis:** The writer expresses their own unhappiness or sorrow: ":(", "😢", "it's hurting my heart", "I miss [NAME]", "I'm crying rn", "I always feel so bad for…".
- **Nearest alternative codes:** disappointment; grief; caring.
- **Decisive difference:** vs disappointment — sorrow without an unmet-expectation frame. vs grief — no loss or no depth of mourning. vs caring — the writer's own sorrow versus support directed at another (both may apply).
- **Boundary example:** T04445 "Apparently we are tragedies!" — "tragedies" is used ironically with an exclamation; no sorrow is expressed.
- **Co-coding rule:** May co-occur with any emotion code (commonly caring, disappointment, grief, remorse). Excludes neutral.
- **Gate:**

### 26: surprise
- **Required textual basis:** The writer reacts to something unexpected: "Wow!", "Omg", "Can't believe…", "Surprised he's in", "You didnt!", "I never knew…".
- **Nearest alternative codes:** realization; confusion; excitement.
- **Decisive difference:** vs realization — reaction to the unexpected versus new understanding. vs confusion — astonishment versus not understanding. vs excitement — enthusiasm without unexpectedness is excitement. Negated surprise does not count.
- **Boundary example:** T02026 "I never went back to the post to see if it was BOA, but I’m not surprised if it was. That was my first guess. " — surprise is explicitly negated.
- **Co-coding rule:** May co-occur with any emotion code (commonly realization, confusion, admiration, excitement). Excludes neutral.
- **Gate:**

### 27: neutral
- **Required textual basis:** After the sweep through all 27 emotion codes, no passage meets any emotion's required textual basis with reasonable confidence — e.g. factual statements, plain reports, emotions that are only mentioned, quoted or attributed to others.
- **Nearest alternative codes:** approval; curiosity; realization.
- **Decisive difference:** Neutral is a claim that no emotion is expressed, not a hedge: if any emotion's basis is met, that emotion is coded instead; if the decision is merely hard, code the best-supported emotion and set `Review`. vs approval/curiosity/realization (the weakly valenced codes most often reached for in near-neutral comments) — the bases stated in those entries decide.
- **Boundary example:** T00177 "Wife just had our baby, and this story freaked me out. I can't imagine going through something like that." — reads like a report, but "freaked me out" expresses the writer's own fear; not neutral.
- **Co-coding rule:** Assigned alone. Excludes every one of the 27 emotion codes (source declaration).
- **Gate:**
