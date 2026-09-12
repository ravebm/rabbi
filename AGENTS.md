# AGENTS.md — read this first

This repository is the single source of truth for Rabbi Evan Moffic's Substack publications — **One Word Wiser** (rabbi.substack.com) and, as it migrates in, **Already Home** (alreadyhome.substack.com). Claude, Hermes, and Codex all work from these same files. If you are an agent, this file tells you where everything is and how to behave.

## The rule that keeps three agents in sync

**Everything lives in git. Nothing lives in your memory.**

1. `git pull` before you do anything. Another agent may have changed a file since you last looked.
2. If you change a file — a skill, a doc, a sample post — commit it with a one-line message saying what changed and why, and push. The other agents will see it on their next pull.
3. Never keep a private copy of a skill or brief. If a change is worth making, it's worth making here.
4. If two instructions conflict, the newer commit wins. Check `git log -- <file>` if unsure.

## Where things are

| Path | What it is | Who uses it |
|---|---|---|
| `one-word-wiser/README.md` | The one-page plan | Everyone — start here |
| `one-word-wiser/01-positioning.md` | Name, description (approved, verbatim), About page, voice rules, logo notes | Everyone |
| `one-word-wiser/02-daily-format.md` | Exact anatomy of every post type | Writers |
| `one-word-wiser/03-monetization.md` | Free/paid line, pricing, when paid turns on | Everyone |
| `one-word-wiser/04-launch-and-growth.md` | Six-week transition, ad funnel, welcome sequence | Operators |
| `one-word-wiser/05-production-workflow.md` | Weekly rhythm, who does what, metrics ledger | Everyone |
| `one-word-wiser/word-bank.md` | The rubric and a full year of words: five a week plus a Shabbat word from the Torah portion, each with verse and secret; the ledger | Writers |
| `one-word-wiser/samples/` | The voice standard. Read `week-01-monday.md` and `week-01-shabbat-haazinu.md` before writing anything | Writers |
| `one-word-wiser/operator-brief-substack-setup.md` | Step-by-step Substack configuration with all copy inline | Operators (Hermes/Codex/Claude driving Substack) |
| `one-word-wiser/handoff-prompts.md` | The exact prompt to paste into each agent, including the Codex prompt that uploads drafts to Substack | Evan |
| `skills/one-word-wiser/SKILL.md` | **The skill**: how to draft any post in the format and voice. Tool-neutral location. | Everyone. `.claude/skills/one-word-wiser` is a symlink to it. |
| `already-home/audio/README.md` | How the daily Already Home meditation audio is made: voice ids and status, the daily process, the log | Everyone |
| `skills/meditation-audio/SKILL.md` | **The skill**: turn a finished meditation into an MP3 in Evan's cloned voice | Claude (needs the ElevenLabs connector) |
| `fal_connect.py` | fal.ai connectivity script (optional editorial images) | — |

## Roles

- **Writer** (any agent asked for posts): follow `skills/one-word-wiser/SKILL.md` exactly. Output Substack-ready Markdown. Never publish — Evan approves every post.
- **Operator** (any agent driving Substack's UI): follow `one-word-wiser/operator-brief-substack-setup.md` exactly. Paste copy verbatim. Change nothing not listed. Report back with the checklist at the end of the brief.
- **Evan** decides everything marked **DECIDE** in the docs. Agents do not resolve those on their own; they use the stated defaults and flag it.

## Non-negotiables (all agents)

- One post a day, 6:00 am Central, seven days a week. The Shabbat word comes from the Torah portion.
- The teaching is free, forever: the word, the verse, the line to carry, and today's question. Never gate above the question. Never gate Shabbat or Sunday.
- Every post is **word → meaning → application**. Nothing else.
- The Hebrew Bible is the lane. Gospel echoes once or twice a week at most, only when the word walks in on its own.
- Voice rules in `01-positioning.md` are not suggestions. Banned words are banned.
- Verify every citation (book/chapter/verse, tractate/page). Never put an unverified source in Evan's mouth.
- Nothing salesy. No urgency copy. No "unlock."
- Do not email the list, publish a post, change a price, or delete anything unless the brief you are following says to.

## Current state

See `git log --oneline -20` for what changed recently and the open PR on GitHub for the branch under review. Open decisions are listed at the bottom of `one-word-wiser/01-positioning.md` and `03-monetization.md`.
