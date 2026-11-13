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
- **Required textual basis:** The writer signals that they themselves are amused: a laughter marker reacting to content (lol, lmao, haha, 😂, 🤣), or a statement that something is funny ("funny", "made me crack up"). One of these is necessary; it is not sufficient where the marker only softens or sneers (see Decisive difference). Making a joke is not expressing amusement: a pun, a rhyme, wordplay, a tease, a mock-serious remark or a playful exaggeration that carries no laughter marker and no statement that something is funny does not meet the basis, however plainly it is meant as humour.
- **Nearest alternative codes:** neutral; joy; annoyance.
- **Decisive difference:** vs neutral — amusement is the writer's reaction to something funny and is marked in the text; a comment that only produces or reports humour (a joke, pun or quip without a laughter marker) is neutral unless another code's basis is met. vs joy — amusement requires humour or entertainment as its object; joy is happiness without that object. vs annoyance/disapproval — a laughter token that only softens or sneers at an accusation or a complaint ("You’re a liar. 😂") supports amusement only if the writer is also enjoying the humour; otherwise code the negative emotion alone.
- **Boundary example:** T01566 "Ghostbusters 2: ghost-bustier ?" — a pun offered by the writer; there is no laughter marker and no statement that anything is funny, so the writer makes humour without expressing amusement.
- **Co-coding rule:** May co-occur with any emotion code, including negative ones when the writer both laughs and criticises. Excludes neutral.
- **Gate:**

### 2: anger
- **Required textual basis:** The writer expresses hostility or heated displeasure, shown by at least one marker of heat in the text: an insult or curse hurled at someone ("Now fuck off", "Hey dumbass"); a wish of harm; stated hatred of a target in the writer's own voice ("i hate [NAME]", "I bloody hate these kinds of captions"); or profanity or all-caps shouting that intensifies an objection or complaint aimed at a person or at their conduct ("Are you fucking serious? That’s a foul??", "That doesn't mean it had 2 of EVERY FREAKING LAND MAMMAL on it!").
- **Nearest alternative codes:** annoyance; disapproval; disgust.
- **Decisive difference:** vs annoyance — anger has a heat marker (profanity or shouting inside the objection, stated hate, cursing at someone, a wish of harm); irritation, a put-down or name-calling stated without any of these ("You’re a liar", "It's ridiculously expensive") is annoyance. An expletive that only reacts to news or to a situation, with no person or conduct objected to, is not anger. vs disapproval — disapproval is a negative judgement without emotional heat. vs disgust — disgust is revulsion at something repellent; anger is hostility toward an agent.
- **Boundary example:** T05066 "Well fuck. I didn't think anybody cared at all...it's order than that?" — the expletive reacts to a piece of news; nobody is attacked and no conduct is objected to; not anger.
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
- **Required textual basis:** The writer agrees with a statement or a person, or sides with a course of action, in their own voice: an agreement marker ("True!", "Exactly", "you're right", "Same here", "Oh of course!"), or support for doing something ("I think we should definitely take him"). An evaluative stance toward a view, a position or an action is required.
- **Nearest alternative codes:** admiration; neutral; realization.
- **Decisive difference:** vs admiration — approval agrees or sides with; it does not ascribe a quality. Where the positive judgement is made with a quality word about a thing, a piece of content, an option or an idea ("Good meme", "Oh nice", "That sounds good", "Good idea", "the smartest option"), code admiration, not approval. vs neutral — a bare "yes" that answers a factual question, or a plain confirmation of fact, is not approval; approval requires an evaluative stance toward a view, idea or action. vs realization — "that makes sense" or "then I understand" is realization when the writer newly understands, approval when the writer judges a proposal sensible.
- **Boundary example:** T02411 "Subway is the smartest option unless you have tones of stuffs to carry !" — rates an option with a quality word ("smartest") instead of agreeing with a statement; admiration, not approval.
- **Co-coding rule:** May co-occur with any emotion code; it may co-occur with disapproval when the comment endorses one thing and rejects another. A positive word that only qualifies the help or reply being thanked for ("Perfect! Thanks", "This is really helpful, thanks!") is part of the gratitude and is not coded as approval. Excludes neutral.
- **Gate:**

### 5: caring
- **Required textual basis:** The writer expresses concern, compassion or comfort directed at a specific other person's hardship or wellbeing, in a passage of its own: sympathy with the person's difficulty, reassurance or comfort about it, encouragement to look after themselves or to seek help ("If you’re struggling reach out to whoever you can!"), or a kindness offered because the other needs it ("You need it more than I do"). Conventional formulas do not meet the basis by themselves: a wish of luck ("Good luck" — see optimism), a greeting or closing pleasantry ("have a great weekend", "Bless u x", "Welcome"), or a courtesy phrase ("Don’t worry about it").
- **Nearest alternative codes:** optimism; neutral; sadness.
- **Decisive difference:** vs optimism — a wish that something turns out well ("Good luck", "Good luck getting it sorted") looks forward to an outcome and is optimism; caring addresses the person's present difficulty or wellbeing. vs neutral — politeness, friendliness or a helpful question ("Do you take any medication?") is not caring unless concern for the person is put into words; purely practical or instructional advice without concern for the person is not caring. vs remorse — "sorry" is caring when it is sympathy for another's situation, remorse when it apologises for the writer's own wrongdoing. vs sadness — caring is directed at another's wellbeing; sadness is the writer's own sorrow (both may apply).
- **Boundary example:** T01103 "thanks for the reply jzplayinggames, have a great weekend." — a closing pleasantry attached to thanks; no concern for the person's difficulty or wellbeing is expressed; gratitude alone.
- **Co-coding rule:** May co-occur with any emotion code (commonly sadness, optimism, love, gratitude), but only where a passage of its own meets the basis; it is not added to thanks, praise or a question on the strength of a friendly tone or a pleasantry. Excludes neutral.
- **Gate:**

### 6: confusion
- **Required textual basis:** The writer states or shows that they do not understand or are uncertain: "I have no idea", "I can't understand why", "Wait a second what?", "I don't know how to feel", bewildered questions.
- **Nearest alternative codes:** curiosity; surprise; neutral.
- **Decisive difference:** vs curiosity — confusion expresses bewilderment or lack of understanding; curiosity seeks information without bewilderment (one question may carry both). vs surprise — surprise reacts to the unexpected; confusion is that something does not make sense. vs neutral — a hedge ("I think", "not sure if") that softens an opinion is not confusion.
- **Boundary example:** T00830 "Not sure if guys like that are better or worse than regular Incels." — "not sure" is a rhetorical put-down, not bewilderment.
- **Co-coding rule:** May co-occur with any emotion code (commonly curiosity, surprise, annoyance). Excludes neutral.
- **Gate:**

### 7: curiosity
- **Required textual basis:** The writer seeks information or shows interest in learning: a question that calls for an answer — in particular an open question asking the addressee for a reason, an explanation or a fact ("What was the end result of this?", "Care to explain?", "Do you have the voting link?", "Why lead him on?", "What reason do you have for not already having been prepared?") — "I wonder", or explicit interest ("Interesting read"). The question counts also when its tone is challenging: no thread is supplied, so whether a question was meant rhetorically cannot be checked against the comment, and the form of the question decides.
- **Nearest alternative codes:** confusion; disapproval; annoyance.
- **Decisive difference:** vs disapproval/annoyance — the form of the question decides, not its presumed intent. An open question (why, what, how, who, where, "Your point?") that the addressee could answer by giving a reason or a fact is curiosity even when it challenges; annoyance or disapproval is added only if a separate passage meets that code's own basis. Not curiosity: a tag or echo question that only restates or doubts what was said ("Are you fucking serious?", "…are they not?", "So what you are saying is that…?"); code what else the comment expresses, or neutral. vs confusion — see confusion.
- **Boundary example:** T04989 "Op literally listed the OS requirements. Those are fairly current operating (last Gen more or less) systems are they not?" — a tag question that asserts the writer's point; nothing is asked for; not curiosity.
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
- **Required textual basis:** The writer states, in their own voice and in the words of the comment, a negative evaluation of an act, idea, claim or state of affairs as wrong, unacceptable, unwise or senseless, or says outright that they disagree or object: "This is just wrong", "Misleading", "Not cool", "never smart", "it just feels wrong", "It makes no sense that this happens", "I disagree" (constructed). Critical content alone is not sufficient. The basis is not met by: (a) a contradiction or correction that only supplies a different fact or reading, also when it opens with "No" or "Nah" ("No. That would be idolatry.", "Nah hes just setting an image", "I wouldnt go that far, but…"); (b) a claim or accusation about what others do, think or intend, with no evaluative word from the writer ("Now you're lying.", "She is asking for trouble.", "They scammed you by wasting your time"); (c) a statement of what should have been done instead ("I think [NAME] should have started"); (d) sarcasm, mockery, a taunt or a roast; (e) a pointed or rhetorical question.
- **Nearest alternative codes:** neutral; annoyance; anger.
- **Decisive difference:** vs neutral — the test is which words of the comment call something wrong, unacceptable, unwise or senseless, or say that the writer disagrees. If no such words can be pointed to — the comment argues, corrects, contradicts with a fact, speculates about motives, mocks or asks a pointed question — it is not disapproval, however critical its content; it is neutral unless another code's own basis is met. vs annoyance — disapproval judges conduct, an idea or a claim against a standard of right, acceptable or sensible ("Not cool", "never smart"); being bothered by something ("ridiculously expensive", "pretty intolerable") or a put-down of a person ("You’re a liar") is annoyance. vs anger/disgust — where the negative passage carries a heat marker (profanity or shouting inside the objection, stated hate, cursing at someone) code anger; where it calls the thing itself repellent or awful ("god awful", "the worst") code disgust.
- **Boundary example:** T01239 "I always keep my purse by my side. She is asking for trouble." — the comment implies blame, but no word of it calls her conduct wrong or unwise and the writer states no objection; not disapproval.
- **Co-coding rule:** May co-occur with any emotion code, but only on a passage of its own: where a passage carries annoyance, anger, disgust or disappointment, that code is assigned and disapproval is not added for the same passage; disapproval is assigned in addition only when a different passage of the comment meets the basis above. Excludes neutral.
- **Gate:**

### 11: disgust
- **Required textual basis:** The writer, in their own voice, expresses revulsion at something physically or morally repellent, or labels the thing itself with a strongly aversive quality word: "disgusting", "makes me sick", "stink", "human trash", "butt ugly", "that’s awful", "god awful", "THE. FUCKING. WORST.".
- **Nearest alternative codes:** disapproval; anger; annoyance.
- **Decisive difference:** Disgust requires that the object itself is called repellent or awful (gross, vile, disgusting, awful, the worst). vs disapproval — disapproval judges an act, idea or claim as wrong or unwise without calling it repellent ("Not cool" is disapproval; "god awful" is disgust). vs anger — anger is hostility at an agent, shown by a heat marker aimed at a person or their conduct; disgust is aversion to the thing. vs annoyance — annoyance is being bothered ("annoying", "ridiculously expensive") without an aversive quality word.
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
- **Required textual basis:** The writer expresses their own happiness, pleasure or enjoyment in words: "Glad to see…", "Happy that you're happy", "Yay", "pleasing to watch". A smiley or other positive emoticon by itself does not meet the basis: without a happiness word it marks friendliness or courtesy, not joy.
- **Nearest alternative codes:** love; admiration; neutral.
- **Decisive difference:** vs love — a first-person "I love …" ("Thanks, I love it.", "Such season 1 vibes and I love it.") is love, whatever its object, and joy is not added for the same statement; joy needs a happiness word of its own. vs admiration — "nice", "great" or "good" said of a thing is admiration ("Pretty nice to see…"); joy is the writer's own state ("glad", "happy"). vs neutral — a smiley on a factual or friendly remark, with no happiness word, is not joy. vs amusement — joy does not require humour. vs excitement — joy lacks the energetic, anticipatory quality.
- **Boundary example:** T00910 "Thanks very much, so do I! :)" — the smiley is a courtesy marker on the thanks; no happiness is put into words; gratitude alone.
- **Co-coding rule:** May co-occur with any emotion code (commonly gratitude, admiration, excitement) where a happiness word of its own is present; it is not added to thanks, agreement or praise on the strength of a smiley or a positive tone, and not added to love for the same "I love …" statement. Excludes neutral.
- **Gate:**

### 18: love
- **Required textual basis:** The writer expresses, in the first person, affection, loving attachment or love for a person, animal, group, thing or piece of content: "I love you", "i love this subreddit", "Thanks, I love it.", "I love your response", "they're both my favorite characters", "<3", "❤️", terms of endearment.
- **Nearest alternative codes:** joy; admiration; caring.
- **Decisive difference:** vs joy — a first-person "I love …" is love whatever its object (a person, a show, a reply, a food); joy is coded only if happiness is put into words separately. vs admiration — affection versus esteem for qualities: "I love your response" is love; a quality word applied to the target is admiration. vs caring — affection versus concern for the other's wellbeing. Quoted or sarcastic "love" (with a cue) does not count.
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
- **Required textual basis:** The writer expresses hope for, or a hopeful expectation of, a good future outcome, with the hope put into words: "Hope so", "Its wonderful to have hope of being off medications one day", or a wish that something turns out well for someone ("Good luck", "Good luck getting it sorted"). An estimate of chances, a conditional judgement or a recommendation that contains no expression of hope does not meet the basis.
- **Nearest alternative codes:** caring; desire; neutral.
- **Decisive difference:** vs caring — a wish that things turn out well ("Good luck", "Good luck with writing in the future") looks forward to an outcome and is optimism; caring requires expressed concern for the person's present difficulty or wellbeing (both may apply where both are in the text). vs desire — hoping or expecting that a good outcome will come versus wanting it. vs neutral/approval — a prediction, an estimate of chances or a conditional judgement of worth states a view, not a hope: it is not optimism, and is approval only if it sides with a course of action ("I think we should definitely take him"). A neutral or negative prediction is not optimism.
- **Boundary example:** T03110 "If we can get a 1st rounder it is without a doubt worth it." — a conditional judgement of worth; no hope is put into words; not optimism.
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
- **Required textual basis:** The writer says or shows that something is contrary to what they expected or hard to believe, and the comment itself contains what the surprise is about: "Wow! That's awesome!", "Can't believe…", "Surprised he's in", "what a coincidence", "I've always found it weird how…". The basis is not met by an interjection or expletive that stands alone or only intensifies thanks, praise or a complaint ("Omg, thank you!", "Dang...", "Goddamn.", "Well fuck."), nor by a short exclamation whose object the comment does not name ("You didnt!", "Oh oh oh", "LOOK!!!").
- **Nearest alternative codes:** neutral; realization; annoyance.
- **Decisive difference:** vs neutral — the comment must itself state the unexpectedness (a surprise word, "can't believe", "what a coincidence", "weird how") or react with "Wow" to something it names; an exclamation that could express any feeling, depending on a context the comment does not supply, is not surprise. vs annoyance — an expletive reacting to something unwelcome ("Well fuck.", "wtf") is annoyance, not surprise. vs realization — reaction to the unexpected versus new understanding. vs confusion — astonishment versus not understanding. vs excitement — enthusiasm without unexpectedness is excitement. Negated surprise does not count.
- **Boundary example:** T00689 "Omg, thank you!" — "Omg" intensifies the thanks; nothing is said to be unexpected; gratitude alone.
- **Co-coding rule:** May co-occur with any emotion code (commonly realization, confusion, admiration, excitement) where the unexpectedness is stated; an interjection that only intensifies another emotion's passage (thanks, praise, a complaint) is not coded as surprise. Excludes neutral.
- **Gate:**

### 27: neutral
- **Required textual basis:** After the sweep through all 27 emotion codes, no passage meets any emotion's required textual basis: the coder cannot point to words in the comment — a feeling word or evaluative word in the writer's own voice, an interjection of feeling, a laughter marker, an emoji — that express the writer's emotion as that code's entry requires. This covers factual statements and plain reports; emotions that are only mentioned, quoted or attributed to others; arguments, counter-claims, corrections and opinions about a topic that are stated without such words, however critical their content; jokes, puns and quips without a laughter marker; and short exclamations or fragments whose feeling depends on a context the comment does not supply.
- **Nearest alternative codes:** disapproval; amusement; annoyance.
- **Decisive difference:** Neutral is a claim that the text expresses no emotion, not a hedge, and two situations are kept apart. (1) An emotion's basis is met by words in the comment, but the choice between codes is hard: code the best-supported emotion and set `Review`; neutral is not available. (2) No emotion's basis is met by the words themselves — the emotion is only plausible, or is inferred from the topic, from a tone the coder supplies, or from a thread the comment does not contain: this is absence of basis, not uncertainty, and the code is neutral (source declaration: an emotion is assigned only when reasonably confident that the writer expresses it). The check: if the reason for an emotion code would have to cite what the writer probably feels or what the context probably was, and not words of the comment, the basis is not met. vs disapproval — content that is critical, contrary or sarcastic is not thereby disapproval; that entry's basis requires the writer's own words of negative evaluation or disagreement. vs amusement — making a joke is not being amused; that entry's basis requires a laughter marker or a statement that something is funny. vs annoyance — irritation that is only imaginable behind a rebuttal or a pointed question is not annoyance; that entry's basis requires a marker in the words.
- **Boundary example:** T00177 "Wife just had our baby, and this story freaked me out. I can't imagine going through something like that." — reads like a report, but "freaked me out" expresses the writer's own fear; not neutral.
- **Co-coding rule:** Assigned alone. Excludes every one of the 27 emotion codes (source declaration).
- **Gate:**
