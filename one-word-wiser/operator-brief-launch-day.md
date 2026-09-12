# Operator brief — LAUNCH DAY (Saturday, September 12)

*For the agent driving Substack today (Codex, Claude in Chrome, or Hermes). Read `AGENTS.md` at the repository root first. This is the short brief for the launch; the full configuration is in `operator-brief-substack-setup.md` and can be done afterwards.*

Evan is logged into Substack at **rabbi.substack.com**. Do exactly these steps, in order. Paste all copy verbatim from the files named. Do not publish, send, or schedule anything except where a step says so. Stop and report if a screen doesn't match.

Today is the one two-post day. From Sunday, one post a day at 6:00 am Central.

## 1. The graphic (Settings → Basics)

- **Logo** (the square avatar/favicon): upload `one-word-wiser/brand/logo-square.png` if that file exists in the repo; otherwise `one-word-wiser/brand/logo-square-standin.png`.
- **Cover image / wordmark** (if the theme has a wide header or cover slot): upload `one-word-wiser/brand/wordmark.png` if it exists; otherwise `one-word-wiser/brand/wordmark-standin.png`.
- To get a file from GitHub: open the file's page on github.com, click **Download raw file** (the ⤓ icon), then upload from your downloads.
- **Publication name:** `One Word Wiser`
- **Short description:** paste exactly:
  > The Bible wasn't written in English. One Hebrew word a day, and the verses it opens — Genesis to the Gospels. From Rabbi Evan Moffic. No Hebrew required.

## 1b. Simplify the dashboard and the benefits (Settings → Payments, then Settings → Emails)

The publication used to be a different newsletter. Remove what's left of it so the subscribe page says only what we do now.

- **Settings → Payments → Subscriber benefits.** Delete every existing line under Free, Paid, and Founding. Enter exactly these, one line each, nothing more:
  - Free: `One Hebrew word every morning, complete. Free, always.`
  - Paid: `The secret inside the word, every weekday. About sixteen cents a day.`
  - Founding: `A signed book, and my thanks by name.`
- **Plans:** monthly `$7`, annual `$60` (annual highlighted/default), founding `$180` named `Founding Reader`. Free trial: 7 days, on. Leave paid subscriptions **enabled** but do not paywall any post: the first two weeks are free; the gate starts September 28.
- **Settings → Emails → Welcome email.** Replace subject and body with the welcome email in `one-word-wiser/samples/welcome-email.md` (subject `Your first seven words`). If the Seven Words PDF link doesn't exist yet, change "Your gift is attached:" to "Your gift is coming:" and leave the words unlinked; note it in the report.
- **Settings → Basics → Subscribe page / "What readers get" text** (if the theme has one): paste the short description only. Remove any older paragraph.
- **Sections:** do not create any. If old sections exist from the previous newsletter, leave them and assign no post to them.
- Do **not** touch: pricing history, existing subscribers, past posts, the custom domain, or any payout/Stripe setting.

## 2. The About page (Settings → Basics → About page)

Replace the whole page with the About text in `one-word-wiser/01-positioning.md` under "About page (ready to paste)": everything inside the quoted block, without the `>` marks.

## 3. The morning post (New post)

- **Title:** `☀️ Happy New Year`
- **Subtitle:** `One Hebrew word a day, starting now.`
- **Body:** from `one-word-wiser/samples/week-00-friday-shanah-morning.md`, everything below the `---` line, from "Last night began the Jewish New Year" to "— Rabbi Evan". Keep bold and italics.
- **Images (two):**
  1. At the very top of the body, above "Last night began": upload `one-word-wiser/posts/cards/2026-09-12-word-day.png`.
  2. In place of the italic line "A year is what repeats. A year is what changes. In Hebrew, that's one word." — delete that text line and upload `one-word-wiser/posts/cards/2026-09-12-line-day.png` where it was.
- **Settings** (right panel): audience **Everyone**; no section.
- **Do not publish yet.** Save as draft. Note the draft URL.

## 4. The evening post (New post)

- **Title:** `🌙 the secret inside shanah · the year that lost its "the"`
- **Body:** from `one-word-wiser/samples/week-00-friday-shanah-evening.md`, everything below the `---` line, from "This morning, *shanah.*" to "— Rabbi Evan". **Delete the line that says `[PAYWALL]`.** Do not include the "Notes for Evan" block at the end.
- **Images (two):**
  1. At the very top of the body: `one-word-wiser/posts/cards/2026-09-12-word-night.png`.
  2. In place of the italic line "God's eyes are on the year at the end as much as at the beginning. Yours can be too." — delete that text and upload `one-word-wiser/posts/cards/2026-09-12-line-night.png`.
- **Settings:** audience **Everyone**; no section.
- **Do not publish yet.** Save as draft. Note the draft URL.

## 5. Sunday's post (New post)

- **Title:** `🌅 The week ahead: Five words for the Days of Awe`
- **Body:** from `one-word-wiser/samples/week-01-sunday-week-ahead.md`, everything below the `---` line, from "# Five Words for the Days of Awe" to "— Rabbi Evan". No images.
- **Settings:** audience **Everyone**; no section. Save as draft. Note the draft URL.

## 6. Ready to share

- Send Evan all three draft URLs and one screenshot of each draft's preview.
- If Evan replies "go": publish the morning post now (it's already Saturday), **schedule** the evening post for **7:00 pm Central today**, and **schedule** Sunday's post for **6:00 am Central tomorrow**. Confirm the publication timezone is America/Chicago before scheduling. Send all as email, publish to web.
- Do nothing else. Do not run the rest of the setup brief today unless Evan asks. Monday onward is uploaded with the weekly Codex prompt in `handoff-prompts.md`.

## Report

1. Logo uploaded (which file) · 2. Cover uploaded (which file) · 3. Name and description set · 4. Benefits replaced with the three lines; old lines removed · 5. Plans and trial set · 6. Welcome email replaced · 7. About page replaced · 8. Morning draft URL · 9. Evening draft URL · 10. Sunday draft URL · 11. Anything that didn't match this brief.
