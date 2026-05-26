# Intro + Lit Review --- working outline

Goal: rip out the old intro + lit review and rebuild them around one
argument: **the model is not the product. the engineering around the model
is what decides whether students learn more, less, or worse.**

Ground everything in the two 2025 RCTs (Kestin = helps, Bastani = hurts)
instead of the older hand-wavy citations I had before.

RULE FOR MYSELF: finish this outline and make sure the source-by-source
logic actually holds before writing a single paragraph. last time i started
writing prose first and rewrote the intro 3 times (see DEVLOG, Apr 4).

---

## Section 1 --- Introduction

Arc: adoption hook -> the real problem (same model, opposite results) ->
my own tutoring angle -> reframe as a design problem -> research question ->
what SimplrAI is -> contributions -> roadmap.

- **Hook (adoption is mainstream now)**
  - Sidoti, Park, & Gottfried 2025 (Pew): ChatGPT-for-schoolwork among teens
    jumped 13% -> 26% in ONE year. n = 1,391. highest in 11th/12th grade.
  - the big general-purpose tools (ChatGPT, Gemini, Copilot, Perplexity)
    were never built for a 13-year-old hitting the chain rule / Krebs cycle /
    French Revolution for the first time.

- **The real problem (thesis seed)**
  - same body of research shows AI tutors can help a LOT or actively hurt.
  - the deciding factor = how the system is built around the model, not the
    model itself. <- this is the whole paper in one sentence.

- **Two anchor studies (just preview here, full detail in 2.1)**
  - Kestin 2025 (Harvard): designed tutor -> >2x learning vs live class.
  - Bastani 2025 (Turkey, ~1000 kids): plain ChatGPT -> -17% on unassisted
    test once it's taken away. safety prompts erased the harm.
  - punchline: "same underlying model, opposite educational results."

- **Personal angle (why i care)**
  - tutoring year: student asks for mitosis / derivatives, gets a dense
    6-paragraph college-level answer, says "still confused," asks for
    "simpler," next answer is LONGER. everyday version of the gap.

- **Reframe**
  - design problem, not a model problem. frontier LLMs already know the
    content. what's missing = the teaching layer: structure, reading level,
    hallucination control, cognitive-load-aware interface.

- **Research question (verbatim-ish)**
  - how can an AI explanation tool be designed to give fast, accurate,
    grade-appropriate explanations that actually help students understand
    the material, not just sound like they do?

- **What SimplrAI is (3 layers, not a new model)**
  1. structured prompting: def -> example -> analogy -> application, +
     retrieval from a small trusted-curriculum library
  2. grade-level layer: classify who's asking, rewrite to that band's
     vocab + sentence complexity
  3. simple interface: chunk the answer, expandable, source links inline

- **Contributions (two)**
  1. document the design choices + tradeoffs
  2. (the part i care about) test whether those choices actually move
     learning. compare SimplrAI vs ChatGPT vs textbook control, across 3
     subjects (Pre-Algebra, Bio, US History) x 3 levels (MS / HS / early
     college).

- **Roadmap**: S2 lit + gaps, S3 method, S4 results, S5 discussion,
  S6-7 limits + conclude.

---

## Section 2 --- Literature Review

framing: 3 clusters = (1) what makes a tutor work, (2) keeping it honest,
(3) matching the reader. all three keep landing on the same idea --- the
model isn't the product.

### 2.1 What makes an AI tutor actually work

- **Bloom 1984 --- the "2 sigma problem"**
  - 1:1 tutoring puts the average student ~98th percentile vs a normal class.
  - the entire field exists to try to scale that. sets the ceiling we chase.

- **Letourneau et al. 2025 --- systematic review (npj Science of Learning)**
  - 28 K-12 ITS studies, 4,597 students. ITSs DO help...
  - ...but the gains shrink a lot vs well-designed non-AI alternatives, not
    just vs passive lectures.
  - takeaway: only helps if the right features are actually built in
    (adaptive feedback, scaffolding, pacing). bridge sentence -> LLMs.

- **Kestin et al. 2025 --- Harvard RCT, Scientific Reports** [ANCHOR 1: helps]
  - 194 undergrads, crossover design, intro physics.
  - arm A = instructor-led active-learning class; arm B = custom GPT-4 tutor
    "PS2 Pal."
  - tutor != GPT-4 + textbook. it was prompted with 7 explicit teaching
    practices: manage info load, one step at a time, never just hand over
    the answer.
  - result: AI tutor BEAT the live class, more learning in less time,
    effect sizes ~0.73-1.3 SD.
  - why: chatbots are built to be helpful, not to teach -> needed
    content-rich prompt engineering.
  - hallucination move: wrote full step-by-step solutions ahead of time,
    fed them into the prompt. <- explicit forward-link to 2.2.

- **Bastani et al. 2025 --- Turkey field experiment, PNAS** [ANCHOR 2: hurts]
  - ~1000 HS math students. 3 arms: textbook control / GPT Base (plain) /
    GPT Tutor (safety prompts).
  - WITH the AI: GPT Base +48%, GPT Tutor +127% on practice problems.
  - AI REMOVED for the real exam: GPT Base scored -17% vs students who never
    had it. crutch effect.
  - safety-prompt version almost entirely fixed it.
  - title says it outright: "Generative AI Without Guardrails Can Harm
    Learning."

- **Kumar et al. 2025 --- AIED, 2 preregistered exp, 1,818 US adults**
  - AI explanations > just being shown the answer, especially if you attempt
    first.
  - even explanations WITH arithmetic errors beat just-the-answer (but lose
    to correct ones).
  - synthesis line for the subsection: how the AI is set up (when it
    explains, what it explains, what it refuses to do) matters more than
    which model is underneath.

### 2.2 Keeping AI explanations honest

- **Ji et al. 2023 --- hallucination survey, ACM Computing Surveys**
  - hallucinated text sounds fluent + looks sourced even when it isn't ->
    uniquely dangerous for a student who can't tell what's right.
  - two kinds: intrinsic (contradicts the source) vs extrinsic (adds
    unverifiable info).

- **callback to Kestin**: full-solutions-in-the-prompt = an applied,
  hand-built version of RAG. nice connective tissue between 2.1 and 2.2.

- **Lewis et al. 2020 --- RAG, NeurIPS**
  - give the model a search engine into a trusted doc set; retrieve relevant
    passages, then answer from them.
  - more specific / diverse / factual than memory-only, and it can point at
    where info came from.

- **Wei et al. 2022 --- chain-of-thought, NeurIPS**
  - show a few worked step-by-step examples -> big gains on arithmetic /
    commonsense / symbolic reasoning = exactly the multi-step stuff in K-12
    STEM.

- **how SimplrAI uses both (smaller scale)**: small retrieval library + a
  strict output schema (def -> example -> analogy -> application). source
  links sit next to the answer so students can check instead of trusting.

### 2.3 Matching the explanation to the reader

- **Paas & van Merrienboer 2020 --- cognitive load, Curr. Dir. Psych. Sci.**
  - working memory ~5-9 items, ~20 sec. goal = spend it on learning, not on
    decoding layout / hunting / untangling dense paragraphs.
  - split-attention effect: one integrated source > info scattered around.
  - worked-example effect: novices learn more from a worked example than
    from solving cold (solving-from-scratch burns working memory).
  - implication: the SHAPE of the answer matters as much as content. chunked
    def/example/analogy/application = handle one piece at a time.
  - callbacks: Kestin's load-management principle, Letourneau's scaffolding
    finding. ties the cluster together.

- **Agrawal & Carpuat 2023 --- grade-specific simplification, EMNLP**
  - core line: what makes a text easy depends on the intended reader.
  - LMs CAN hit a target grade, but corpus-level targets ignore per-input
    difficulty; predicting case-by-case works much better.
  - maps onto exactly what a tutor needs (6th grader on mitosis one minute,
    college soph on the same topic the next).

- **the default-college-prose problem**
  - LLMs default to ~college-level prose. the "simpler" rewrite usually just
    trims a few words and keeps the nested structure. need explicit
    per-question control.

- **SimplrAI grade-level layer** = Agrawal-Carpuat case-by-case approach:
  classify the asker, condition on a reading band, check readability before
  showing. combined w/ the structure piece -> right AMOUNT of info AND right
  KIND of language at once.

### 2.4 Where the gaps are (this is the payoff)

1. no widely-used tool treats grade-appropriate explanation as a core
   feature. reading-level research and tutoring research basically don't
   talk to each other.
2. structured prompting + retrieval have been evaluated for accuracy /
   reasoning benchmarks, NOT for whether students actually understand the
   resulting explanation better.
3. the headline results (Kestin +2x, Bastani -17%) both point the same way:
   the helps-vs-hurts difference is engineering, not model quality. but
   nobody has done the obvious study --- hold the model fixed and vary the
   engineering layer (structure / grade level / interface) to see how much
   each piece matters.

-> SimplrAI is built to push on all three, and the S3 experiment is designed
   to test whether the engineering actually moves student learning.

---

## source checklist (every one must do real work, no decoration)

- [x] Sidoti / Pew 2025      -- adoption hook
- [x] Bloom 1984             -- 2-sigma ceiling
- [x] Letourneau 2025        -- ITS review, "features must be built in"
- [x] Kestin 2025            -- ANCHOR, AI helps when engineered
- [x] Bastani 2025           -- ANCHOR, AI hurts when not
- [x] Kumar 2025             -- explanations help, setup > model
- [x] Ji 2023                -- hallucination taxonomy
- [x] Lewis 2020             -- RAG
- [x] Wei 2022               -- chain-of-thought
- [x] Paas & van Merrienboer 2020 -- cognitive load
- [x] Agrawal & Carpuat 2023 -- per-input grade-level simplification

## voice notes for when i write the prose
- casual but precise, same as the proposal
- contractions are fine (it's, don't, won't)
- NO em-dashes (mentor flagged them as "AI-sounding")
- first person where it's my own experience / choices
- every source has to earn its place -> if i can't say why it's here in one
  line, cut it
