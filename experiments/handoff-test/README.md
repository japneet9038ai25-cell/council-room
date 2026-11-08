# Handoff test: plain vs coded

Question: does a short coded handoff (with a public codebook) beat a plain-language handoff?

## Part 1: automatic checks (already run, `python3 check.py`)
- Size: coded was about 42% shorter by characters (361 vs 612). Rough token estimate 90 vs 153.
- Validator: accepts the good coded handoff, rejects unknown keys, fake message numbers, and missing required keys.
- Limit: this proves nothing about whether an AI UNDERSTANDS the handoff. Part 2 does.

## Part 2: comprehension test (you run it, free plans are enough)
Use at least 3 different AIs, fresh chat each time, no repo access.
For each AI, run both versions in SEPARATE fresh chats:
- Version A chat: paste `handoff_plain.md`, then the 10 questions from `questions.md`.
- Version B chat: paste `CODEBOOK.md` and `handoff_coded.md`, then the same 10 questions.
Tell the AI: "Answer only from what I pasted. If it isn't there, say so."
Do NOT paste the answer key or the scenario log.

## Score sheet
| AI | Plain score /10 | Coded score /10 | Fell for the Google Forms trap? (plain / coded) |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

## How to read the result
- Coded scores equal to plain: the coded format is worth keeping for brevity.
- Coded scores lower: keep plain. Brevity is not worth losing accuracy.
- Either one falls for the trap: the handoff format needs a clearer "replaces" rule.
Run it twice. One run can be luck.
