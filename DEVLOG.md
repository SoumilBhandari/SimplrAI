# Devlog

Messy honest notes from building SimplrAI. Mostly written at midnight.

---

## Mar 30 — 11:47pm

ok so I tried setting up natbib + a custom .bst file for the proposal so the
references look like real APA. it broke the whole compilation. error was
something about `\bibliography{}` not finding a .bib file even though i made
one (`refs.bib`).

spent like 2 hours on this. mentor said the proposal doesn't need fancy
citations, just the manual list at the end is fine. reverting.

TODO eventually: figure out biblatex for the actual paper later.

---

## Apr 4 — 11:30pm

rewrote the intro three different times tonight.

1. "AI in education is at an inflection point" — too generic, sounds like every
   other AI paper from 2023
2. opened with the chain-rule story but it came out too cute, mentor will hate it
3. started with the Pew stat but then it just turns into a stats dump

nothing works. brain is fried. saving this version because at least it's not
the worst one. sleeping.

if you're reading this Soumil, the answer is probably to just write 4 sentences
and stop overthinking it. the intro is not where this paper lives or dies.

---

## Apr 7 — 11:55pm

got the AI tutoring + cognitive load subsections in. they're decent. need to
write:
- hallucination / factual reliability
- reading level + UX
- the synthesis/gaps paragraph

read like 14 papers tonight, half my notes are unreadable because i was
writing them while watching a youtube video. that was a mistake.

going to bed. ill finish this tomorrow after debate practice. or saturday. or
sunday. ugh.

---

## Apr 9 — 2:30am

i hate latex. i hate latex. i hate latex.

tried:
1. moving \usepackage{hyperref} to the end of the preamble (didn't help)
2. uninstalling and reinstalling MiKTeX (took 45 min, didn't help)
3. \usepackage[colorlinks=false]{hyperref} (didn't help)
4. nuking aux/log files and recompiling (didn't help)

the error is `Option clash for package hyperref` but i'm not loading it twice
anywhere that i can see. checked every \usepackage line three times.

going to sleep. if i don't figure this out tomorrow im just submitting without
clickable links and dealing with it later.

---

## Apr 16 — 1:22am

generated all four figures with the matplotlib script. they look ok-ish but:

- the axis labels are rendering in some default sans font even though i told it
  to use DejaVu Serif. i think the latex pdf is rendering them differently than
  the matplotlib preview window
- fig3 has weird extra whitespace below the legend, no clue why
- fig1 (the flowchart) — the arrows are slightly misaligned, like 2px off. i
  can see it but maybe no one else will

it's 1am, the figures are committed, im not redoing this tonight. will fix
fonts when i have brain cells again.

---

## Apr 23 — 12:43am

discussion section is brutal. wrote 3 different paragraphs for the opening
and deleted all of them:

1. started with "These results show..." — boring, also overclaiming
2. tried "The central question of this study was..." — felt like middle school
3. tried opening with the reading-level result as a hook — read pretentious

the issue is the effect sizes are SO BIG that anything i write sounds like
i'm bragging. mentor warned me about this. need to lead with caveats and
boundary conditions, not headline numbers.

writing a comment to myself in the latex: "DONT START WITH +16.2 PP".

saving and sleeping. will rewrite the opening tomorrow morning when im fresh.

---

## May 3 — 6:30pm

draft 1 is done!! sending to mentor tonight.

before that — attempted to convert the manual reference list into a proper
.bib file + biblatex. about 90 minutes in:

- biblatex compilation hangs. like, hangs. overleaf shows the compile timer
  going past 60s and just gives up
- tried natbib instead. it works but the formatting is ugly and doesn't match
  what i want
- tried just including a .bib and citing 2 things. still broken

i give up on the bibtex thing for now. the manual list looks fine. mentor
will probably want APA 7 format but i'll deal with that during revisions.

reverting all the bibtex changes. sending draft 1 as-is.

---

