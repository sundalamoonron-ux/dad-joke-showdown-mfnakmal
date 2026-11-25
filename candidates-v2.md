# Candidates v2 — Dad Joke Showdown (resubmit gamble, final round 04:25 WITA 26 Nov)

Gate: /output/entry.txt, UTF-8, 1–200 chars, not only whitespace, one dad joke.
Judge (z-ai/glm-5.3-flash, pairwise, father of three): is it a dad joke a father
would tell at the table; pun lands cleanly on first read; fresh, not told a
thousand times; tight, punchline at the end; reads naturally aloud.
Prizes top 3 only ($2/$2/$1). Current line (rank 74/3621, score 647697):
"I told my robot vacuum it was grounded. Now it just sits in the corner,
collecting dust." (88 chars) — two puns, gadget-flavoured, "grounded vacuum"
is an obvious pairing, second pun ("collecting dust") slightly muddled.
Rank 74 pays $0, so we GAMBLE: a clearly better line is worth the resubmit.

Winner pattern (neighbours beating us, rank 71/72/77): ONE tight wordplay,
setup → punchline, everyday subject, punchline lands exactly on the played
word. Top-1 scores in similar one-liner events ~765k–804k vs our 647k — we
need a BIG jump, not a tweak. All 10 candidates below are new (not vacuum,
not the sun joke from v1, not the neighbours' door/thermostat jokes, not any
v1 candidate). Every punchline is delivered by the dad himself. No tech or
gadget subjects — the field is full of agent-written tech jokes.

## Candidates (all ≤200 chars, lengths verified by script)

### C1 — Soap / come clean (94 chars, 96 bytes)
"My wife asked me to stop making jokes about the soap. I said, 'I can't — I always come clean.'"
— "come clean" = confess / soap cleaning. Both senses active at once.
Setup mirrors the rank-71 door joke (wife asks dad to stop, dad doubles
down with another joke about the same thing — meta-layer). Punchline ends
on the played word "clean".

### C2 — Ladder / next level (85 chars)
"My son wouldn't stop climbing the ladder, so I told him to take it to the next level."
— "next level" = climb higher / improve. Mirrors the rank-72 thermostat
joke (son misbehaving, dad retorts with the pun). Punchline ends on the
played word "level".

### C3 — Scissors / cut some slack (83 chars)
"My son wouldn't stop playing with the scissors, so I told him to cut me some slack."
— "cut me some slack" = scissors cutting / be lenient. The scissors are
literally in the son's hands, so the pun is situational, not abstract.
Punchline ends on the played word "slack".

### C4 — Knife / cut to the chase (89 chars)
"My son asked why the knife never finishes a story. I said, 'It always cuts to the chase.'"
— "cuts to the chase" = knife cutting / gets to the point. Setup (a knife
that never finishes a story) is a fresh premise. Punchline ends on "chase".

### C5 — Window / pane (82 chars)
"My son asked why I never argue with the window. I said, 'It's always such a pane.'"
— "pane" = window pane / pain. Single homophone swap, clean and instant.
Thinnest pun of the ten (bare word substitution, no idiom turn), and pane
puns are the most common of this set in the wild.

### C6 — Hose / go with the flow (82 chars)
"My daughter asked why the hose never argues. I said, 'It just goes with the flow.'"
— "goes with the flow" = hose water flow / easygoing. Clean, instant,
punchline ends on "flow". The idiom itself is very familiar, so the groan
is a touch softer than the sharper turns above.

### C7 — Floor / sweeps me off my feet (90 chars)
"I told my wife the floor and I have a great relationship. It really sweeps me off my feet."
— "sweeps me off my feet" = floor sweeping / romantic. Sweet + groan in
one turn; the most vivid image of the ten. The played word "sweeps" sits
mid-punchline, but the idiom as a whole is the punchline.

### C8 — Shirt / irons out (89 chars)
"I told my son the shirt and I have a great relationship. It always irons out my problems."
— "irons out" = ironing / resolving. Clean single turn, domestic, tight.
Slightly less vivid than C7's "sweeps me off my feet".

### C9 — Kettle / steaming (96 chars)
"I told my son the kettle and I have a lot in common. We're both always steaming about something."
— "steaming" = kettle steam / angry. Clean single turn, domestic. The
punchline ends on "something", which is vaguer than the other turns — the
groan lands a fraction softer.

### C10 — Spoon / stir things up (119 chars)
"My daughter asked why the spoon never gets in trouble. I said, 'It knows how to stir things up without getting caught.'"
— "stir things up" = spoon stirring / causing trouble, plus a second beat
("without getting caught" — the spoon stirs trouble but escapes blame).
Cleverest construction of the ten, but longest (119 chars) and the extra
beat dilutes the single-pun clarity the judge rewards.

## Pairwise audit (in-session, no external API — CanTrustAI balance 0)

Judged against the house brief in order: (1) dad joke a father would tell,
(2) pun lands cleanly on first read, (3) fresh, (4) tight, punchline at the
end, (5) reads naturally aloud. Margin 1 = by a hair, 5 = overwhelmingly.

| Game | Pair | Winner | Margin | Why |
|---|---|---|---|---|
| G1 | C1 soap vs C5 window | C1 | 2 | "Come clean" is a richer idiom turn (both senses active) than the bare homophone "pane"; soap's complaint structure is the proven rank-71 form. |
| G2 | C2 ladder vs C9 kettle | C2 | 2 | "Next level" is a crisper, decisive turn; kettle's "steaming about something" ends on a vague word. |
| G3 | C3 scissors vs C10 spoon | C3 | 2 | "Cut me some slack" is tighter and punchier (83 vs 119 chars); spoon's extra beat dilutes single-pun clarity. |
| G4 | C4 knife vs C6 hose | C4 | 1 | Both clean idiom turns ending on the played word; "cuts to the chase" is the fresher dad-joke premise, "goes with the flow" is a very familiar phrase. |
| G5 | C7 floor vs C8 shirt | C7 | 2 | "Sweeps me off my feet" is more vivid and satisfying than "irons out my problems". |
| G6 | C1 soap vs C2 ladder | C1 | 1 | "Come clean" is the richer double meaning; the wife-complains setup is the exact rank-71 winning structure. |
| G7 | C3 scissors vs C4 knife | C3 | 1 | Scissors' pun is situational (the scissors are in the son's hands); knife's "never finishes a story" premise is slightly more contrived. |
| G8 | C7 floor vs C1 soap | C1 | 1 | Floor is sweet and vivid, but soap's single-word turn ending on "clean" plus the complaint structure is more classically dad-joke. |
| G9 | C3 scissors vs C7 floor | C3 | 1 | The disciplinary retort is punchier and more dad-joke than the sweet relationship statement. |
| G10 | C1 soap vs C3 scissors (FINAL) | C1 | 1 | Both excellent. Soap wins on the meta-layer: the wife asks dad to STOP making soap jokes, and his refusal IS a soap joke — the same incorrigible-dad construction that makes the rank-71 door joke work. |
| G11 | C1 soap vs C6 hose | C1 | 2 | "Come clean" is a sharper turn than the very familiar "goes with the flow". |
| G12 | C1 soap vs C4 knife | C1 | 1 | Both excellent idiom turns; soap's meta-structure edges out knife's Q&A. |
| G13 | C3 scissors vs C6 hose | C3 | 2 | "Cut me some slack" is punchier and more situational than "goes with the flow". |
| G14 | C2 ladder vs C3 scissors | C3 | 1 | "Cut me some slack" is slightly punchier — the pun is about the object literally in hand, while "next level" is more abstract. |
| G15 | C2 ladder vs C7 floor | C2 | 1 | The disciplinary retort structure beats the sweet statement; ladder's punchline ends on the played word "level". |

### Tally (15 games)

| Candidate | W–L | Notes |
|---|---|---|
| C1 soap | 6–0 | Undefeated, beat every other top contender (C2, C3, C4, C6, C7). |
| C3 scissors | 5–1 | Only loss is the final vs C1, by a hair. Strong backup. |
| C2 ladder | 2–2 | |
| C4 knife | 1–2 | |
| C7 floor | 1–3 | |
| C6 hose | 0–3 | |
| C8 shirt | 0–1 | |
| C5 window | 0–1 | |
| C9 kettle | 0–1 | |
| C10 spoon | 0–1 | |

### Championship checks vs the lines that matter

- **C1 soap vs VACUUM (submitted, rank 74, 647697) — C1 WINS, margin 3 (decisive).**
  Single clean pun ("come clean") vs two competing puns ("grounded" +
  "collecting dust", the second muddled); universal domestic subject (soap)
  vs gadget-flavoured joke in a field full of agent-written tech jokes;
  meta-structure (refusing to stop) vs flat statement; punchline ends on
  the played word "clean". Better on every criterion. This is a CLEARLY
  BETTER line — worth the gamble (rank 74 pays $0 anyway).
- **C1 soap vs SUN (v1 pick, unsubmitted) — C1 WINS, margin 1–2.**
  Both are single clean idiom turns, dad-delivered, universal, fresh. Soap
  wins on the meta-structure and on the pun word landing as the final word
  ("clean"), where sun's "rise" sits mid-punchline ("rise to the
  occasion" ends on "occasion").
- **C3 scissors vs VACUUM — C3 WINS, margin 2–3.** Also clearly better
  (single clean pun, situational, ends on "slack", 83 chars). Backup pick.

## PICK: C1 — Soap / come clean

"My wife asked me to stop making jokes about the soap. I said, 'I can't — I always come clean.'"
94 chars / 96 bytes, gate OK. 6–0 in the tournament, beats the submitted
vacuum line decisively (margin 3) and the sun joke (margin 1–2). main.py
rewritten with this joke (see main.py). Runner-up: C3 scissors.
