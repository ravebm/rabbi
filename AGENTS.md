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
| `operations/audience-research/README.md` | Proposed shared Grok scout and agent roles for both publications; ready research assignment | Researchers, chief of staff |
| `one-word-wiser/README.md` | The one-page plan | Everyone — start here |
| `one-word-wiser/01-positioning.md` | Name, description (approved, verbatim), About page, voice rules, logo notes | Everyone |
| `one-word-wiser/02-daily-format.md` | Familiar structure, titles, and source standards | Writers |
| `one-word-wiser/03-monetization.md` | Free/paid line, pricing, when paid turns on | Everyone |
| `one-word-wiser/04-launch-and-growth.md` | Current launch state and proposed growth experiments | Operators |
| `one-word-wiser/operations/README.md` | Whole-publication quality, growth and tool-learning loops; reusable cycle record | Everyone |
| `one-word-wiser/05-production-workflow.md` | Weekly rhythm, who does what, metrics ledger | Everyone |
| `one-word-wiser/word-bank.md` | The rubric and a full year of words: five a week plus a Shabbat word from the Torah portion, each with a verse and a proposed rabbinic reading; the ledger | Writers |
| `one-word-wiser/samples/` | The voice standard. Read `week-01-monday.md` and `week-01-shabbat-haazinu.md` before writing anything | Writers |
| `one-word-wiser/posts/` | The dated drafts, one file a day, cards in `posts/cards/` | Writers, Operators |
| `one-word-wiser/archive/` | Retired plans kept for the record (including the two-post launch brief). Never draft from these | — |
| `one-word-wiser/operator-brief-substack-setup.md` | Step-by-step Substack configuration with all copy inline | Operators (Hermes/Codex/Claude driving Substack) |
| `one-word-wiser/study-companion/README.md` | Proposed weekly study page; local prototype, not an adopted paid benefit | Everyone |
| `one-word-wiser/substack-audit-2026-09-14.md` | Latest consistency corrections and remaining product decisions | Everyone |
| `one-word-wiser/handoff-prompts.md` | The exact prompt to paste into each agent, including the Codex prompt that uploads drafts to Substack | Evan |
| `one-word-wiser/template-index.md` | Template readiness, current sources, and remaining checks | Everyone |
| `one-word-wiser/brand/design-handoff.md` | Claude Design and Magnific roles, project handoff, and export checks | Designers, Operators |
| `one-word-wiser/book/README.md` | The free book, *Seven Hebrew Words*: the text, the script that builds the PDF, the download-post copy, and where it lives once it is on Substack | Codex (draft, build, upload); Evan approves |
| `skills/one-word-wiser/SKILL.md` | **The skill**: how to draft any post in the format and voice. Tool-neutral location. | Everyone. `.claude/skills/one-word-wiser` is a symlink to it. |
| `already-home/audio/README.md` | How the daily Already Home meditation audio is made: voice ids and status, the daily process, the log | Everyone |
| `skills/meditation-audio/SKILL.md` | **The skill**: turn a finished meditation into an MP3 in Evan's cloned voice | Claude (needs the ElevenLabs connector) |
| `fal_connect.py` | fal.ai connectivity script (optional editorial images) | — |

## Roles

- **Writer** (any agent asked for posts): follow `skills/one-word-wiser/SKILL.md` exactly. Output Substack-ready Markdown. Never publish — Evan approves every post.
- **Operator** (any agent driving Substack's UI): follow `one-word-wiser/operator-brief-substack-setup.md` exactly. Paste copy verbatim. Change nothing not listed. Report back with the checklist at the end of the brief.
- **Readable posts:** writers and operators also read `skills/one-word-wiser/references/substack-readability.md`. Evan's September 14 direction calls for a familiar, elegant format, short content-specific subheadings, and restrained typographic dividers. He retired the product label “secret” and the recurring application heading “Let It Change Your Life.” Do not restore them. Apply the current task's scope: editorial polish when authorized; prepared copy preserved during upload; draft-only unless delivery is explicitly authorized.
- **Evan** decides everything marked **DECIDE** in the docs. Agents do not resolve those on their own; they use the stated defaults and flag it.

## Non-negotiables (all agents)

- One post a day, 6:00 am Central, seven days a week. The Shabbat word comes from the Torah portion.
- The daily word and its meaning in Scripture are free, forever. The current paid benefit is the full weekday reflection on Hebrew, Jewish wisdom, and everyday life, in the same email. Evan’s September 14 decision starts paid weekday continuations on September 15, 2026, after a complete free teaching. This supersedes the prior September 27 launch end. Never gate Shabbat or Sunday. A weekly study companion is a proposal for Evan to assess, not a live subscriber promise.
- Every post moves from **word → meaning → reflection**. Keep the experience familiar while letting the word, question, story, and ending vary. A complete free teaching may include rabbinic wisdom and a useful application.
- Use the familiar **In English:** / **In Hebrew:** opening where it serves the word. Make the linguistic point accurate; never invent a mistranslation or force a dramatic correction. Human titles are welcome; Hebrew remains prominent in the body. Never "your Bible" or "the Christian Bible."
- The Hebrew Bible is the lane. Gospel echoes once or twice a week at most, only when the word walks in on its own.
- Voice rules in `01-positioning.md` are not suggestions. Banned words are banned.
- Verify every citation (book/chapter/verse, tractate/page). Never put an unverified source in Evan's mouth.
- Nothing salesy. No urgency copy. No "unlock."
- Do not email the list, publish a post, change a price, or delete anything unless the brief you are following says to.

## Current state

See `git log --oneline -20` for what changed recently and the open PR on GitHub for the branch under review. Open decisions are listed at the bottom of `one-word-wiser/01-positioning.md` and `03-monetization.md`.
