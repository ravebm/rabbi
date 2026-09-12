# Handoff prompts — paste one of these into the agent

All three agents work from the same repository: **github.com/ravebm/rabbi**. Give each one repo access (a clone, a connected GitHub account, or an upload of the folder), then paste the matching prompt. Every prompt starts with "read `AGENTS.md`," which is what keeps them in sync: if you change a skill or a doc in any one of them and it's committed, the others see it on their next pull.

---

## Codex — upload a week's drafts to Substack (the weekly one)

Use this every Sunday after you've approved the drafts, and this weekend for the launch. Fill in the file list. Codex needs a browser and you logged in at rabbi.substack.com.

> Open my repository `ravebm/rabbi` and pull the latest. Read `AGENTS.md` at the root, then `one-word-wiser/02-daily-format.md` (the section "The cards" and "Post-body template"). I am logged into Substack at rabbi.substack.com. Create each of the posts below as a **Substack draft**, exactly as written, and do not publish or send anything.
>
> For each file:
> 1. **Title** = the `**Subject:**` line of the file, without the word "Subject". Leave the subtitle empty unless the file has a `**Subtitle:**` line.
> 2. **Body** = everything below the `---` line, ending at `— Rabbi Evan`. Do not paste the header block (Subject, Audience, Cards, Notes) and do not paste any "Notes for Evan" or "Audio" block at the end. Keep every bold, italic, blockquote and line break. Paste Hebrew script exactly, with its vowel marks.
> 3. If the body starts with a large Hebrew word and a transliteration line inside `<div align="center">`, delete those lines; the Word card carries them. Center nothing else.
> 4. **Images:** upload the PNGs named in the file's `**Cards:**` line from `one-word-wiser/posts/cards/`. The `word-day` card goes at the very top of the body. The `line-day` card replaces the italic sentence marked as the line to carry (delete that text line and put the image where it was). The `line-night` card replaces the italic line to sleep on, the same way. If a card file is missing, leave the italic line as text and note it in your report.
> 5. **Paywall:** where the body says `[PAYWALL]`, delete that line. (From September 28 onward, insert Substack's paywall divider at that spot instead of deleting it; the file's `**Paywall:**` line will say which.)
> 6. **Settings:** audience Everyone. Do not assign a section. Send as email: yes. Publish to web: yes. Schedule for the date and time in the file's `**Send:**` line, America/Chicago, only if I say "schedule" below; otherwise save as an unscheduled draft.
> 7. Do not change any other Substack setting, do not touch other posts, do not send test emails.
>
> The files, in order:
> - `[path]` — `[date, time]`
> - …
>
> Schedule: [yes / no]
>
> When done, reply with one line per post: title, draft URL, scheduled time (or "draft"), and whether every card was placed. If any screen didn't match these instructions, tell me which step rather than improvising.

**This weekend, filled in** (the launch is the one two-post day; from Sunday it's one a day):

> - `one-word-wiser/samples/week-00-friday-shanah-morning.md` — Saturday, September 12, 6:00 am
> - `one-word-wiser/samples/week-00-friday-shanah-evening.md` — Saturday, September 12, 7:00 pm
> - `one-word-wiser/samples/week-01-sunday-week-ahead.md` — Sunday, September 13, 6:00 am
> - `one-word-wiser/samples/week-01-monday.md` — Monday, September 14, 6:00 am
> - `one-word-wiser/samples/week-01-shabbat-haazinu.md` — Saturday, September 19, 6:00 am
>
> Schedule: yes

Tuesday through Friday of week 1 and the following Sunday are produced by the skill ("write the week") and saved in `one-word-wiser/posts/` once you approve them; add them to the list the same way.

## Hermes — set up Substack (once)

> You have access to my repository `ravebm/rabbi` (pull the latest first). Read `AGENTS.md` at the root, then follow `one-word-wiser/operator-brief-substack-setup.md` exactly, start to finish. I am logged into Substack at rabbi.substack.com. Paste every piece of copy verbatim from the brief and the files it points to; do not rewrite anything. Do not publish, email, or change anything the brief does not list. When you finish, reply with the checklist at the end of the brief, and if anything in Substack's interface didn't match the brief, tell me which step rather than improvising. If you had to change anything in the repository (you shouldn't need to), commit it with a one-line message and push.

## Codex or Claude in Chrome — LAUNCH DAY (the short one)

> Open my repository `ravebm/rabbi` (pull the latest). Read `AGENTS.md`, then follow `one-word-wiser/operator-brief-launch-day.md` exactly, top to bottom. I am logged into Substack at rabbi.substack.com. Upload the logo, set the name and description, clear out the old benefits and welcome email and replace them with the new ones, replace the About page, and create the launch posts as drafts with their images. Do not publish or schedule anything until I say "go". Paste all copy verbatim. When done, send me the draft links and the report at the end of the brief.

## Claude — write, edit, or update the system

> Pull `ravebm/rabbi`, read `AGENTS.md`, and [write Tuesday's post for *shema* / write the week / draft Saturday from the portion / update the skill so that … ]. Commit and push whatever you change so Hermes and Codex see it.

## Codex — write posts

> Open my repository `ravebm/rabbi` and pull the latest. Read `AGENTS.md` at the root, then `skills/one-word-wiser/SKILL.md`, then `one-word-wiser/samples/week-01-monday.md` and `week-01-shabbat-haazinu.md`. Using `one-word-wiser/word-bank.md`, draft [the week of … / Tuesday through Friday of week 1] in the skill's output contract: one post a day, the door and `[PAYWALL]` marker at the question, the secret below it. Save each post as `one-word-wiser/posts/YYYY-MM-DD.md`, commit with the message "Week N drafts: <words>", and push to a branch named `posts/week-NN`. Do not publish anything. Below the drafts, list any citation you are less than certain of.

---

## When you change something

Make the change in any one agent, and make sure it ends in a commit to the repo. That's it. The other two agents pull before they work, so they inherit it. If an agent ever seems to be working from an old version, tell it: "pull the latest and re-read `AGENTS.md`."

## One-time setup

1. Give Hermes and Codex access to the repository.
2. Upload the two logo files to `one-word-wiser/brand/` (any agent can do this if you give it the files) so the operator brief can point to them.
