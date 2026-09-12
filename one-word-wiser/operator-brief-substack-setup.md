# Operator brief — set up One Word Wiser on Substack

*For any agent operating Substack on Evan's behalf (Hermes, Codex, Claude). Read `AGENTS.md` at the repository root before starting.*

You are configuring an existing Substack publication for Rabbi Evan Moffic. The publication is **rabbi.substack.com** (name: *One Word Wiser*). Evan is logged in. This document is complete: every setting and every piece of copy you need is here. Do exactly what it says, in order, and nothing more. Where it says **paste**, paste the text verbatim — do not rewrite, shorten, or "improve" any copy.

## What this publication is (context only)

A daily Hebrew-word newsletter for Christians (and curious Jews). **One post a day, 6:00 am Central, seven days a week.** Monday–Friday: one Hebrew word, its meaning, one line to carry, one question, free and complete; then, below the question, the secret inside the word (the layer the rabbis called *sod*) and one small thing to do with it, paid from week 3. **Saturday:** a word from the Torah portion read in synagogue that morning, plus the week's five words, free and whole. **Sunday:** a reader's verse, free and whole. The publication launched on Rosh Hashanah, Saturday, September 12, with a morning and evening post on the word *shanah*, the one two-post day. The first two weeks are entirely free; the gate turns on September 28.

## Hard rules

- Do not publish or email anything that is not in this document.
- Do not change anything not listed here. Do not delete or edit any existing posts.
- Do not turn on the paywall for any post in this document — every post below is **Everyone (free)**.
- Do not send test emails to the list.
- Timezone for every schedule is **America/Chicago (Central)**. Confirm the publication's timezone setting matches before scheduling.
- If any step's UI differs from what's described, find the equivalent setting; if you cannot, stop and report which step, rather than guessing.
- When finished, report back using the checklist at the end.

---

## PART 1 — Publication settings

### 1.1 Basics (Settings → Basics)
- **Publication name:** `One Word Wiser`
- **Short description / tagline** (the one-line description shown on the homepage, email header and Substack discover): paste exactly:
  > The Bible wasn't written in English. One Hebrew word a day, and the verses it opens — Genesis to the Gospels. From Rabbi Evan Moffic. No Hebrew required.
- **Logo:** the files are in `one-word-wiser/brand/` (`logo-square.png`, `wordmark.png`); if that folder is empty, Evan will supply them. Use the **small navy square with the cream aleph** as the logo/avatar (it also becomes the favicon). Use the **full wordmark** ("One Word Wiser with Rabbi Evan Moffic") as the cover image / email header image if the theme supports a wide header image. If only one file is available, use the square.
- **Author name / byline:** `Rabbi Evan Moffic`
- Leave the subdomain (`rabbi`) unchanged.

### 1.2 About page (Settings → Basics → About page, or the "About" page editor)
Replace the entire existing About page with the following, verbatim:

**One Word Wiser**
*One Hebrew word, one rabbinic teaching, and one wiser way to live.*

The Bible was not written in English. It was written in Hebrew — a language where "hope" is a rope, "repent" means "come home," and "peace" means "whole." Every translation, even the best, trades those pictures for approximations.

And Hebrew isn't like other languages. The rabbis said God created the world with its letters. Every letter has a shape and a story — *bet* is a house, *ayin* is an eye — and every word grows from a three-letter root, so a Hebrew word doesn't just name a thing. It tells you how God's language sees it.

I'm Rabbi Evan Moffic. I've spent twenty years teaching Hebrew and the Jewish roots of the Bible to churches, and I've written several books about it, including *What Every Christian Needs to Know About the Jewishness of Jesus*. This newsletter is the most direct version of that work: one word a day.

**Every morning at 6:00 (free):** one Hebrew word — its root, the picture inside it, one verse you've read your whole life that changes when you see it, and one question for the day.

**Below the question (paid):** the secret inside the word. The rabbis taught that every word of Scripture has four layers, and they called the deepest one *sod* — secret. That's the second half: the hidden layer — a gap in the verse, a root the translation buried, a letter written large, a count the rabbis made — and one small thing to do with it today. Ninety seconds. The same shape every day.

**Shabbat:** the word from the Torah portion every synagogue in the world is reading that morning, whole and free, and the week's five words gathered.
**Sunday:** *Your Verse* — you send me a verse, I show you the Hebrew underneath. Whole and free.

Free is genuinely free. You'll get the word every morning, complete, without paying a cent, and the whole post on Shabbat and Sunday. Paid — $60 a year, about sixteen cents a day — is the secret, every weekday, and my thanks for making this possible.

Whether you're Christian, Jewish, or simply curious: welcome. Send me a verse anytime. Just reply.

### 1.3 Sections (Settings → Sections)
Do not create any sections. One email a day needs no off switch. If sections exist from the previous newsletter, leave them and assign no new post to them.

### 1.4 Welcome email (Settings → Emails → Welcome email)
- **Subject:** `Your first seven words`
- **Body:** paste the body of `one-word-wiser/samples/welcome-email.md` (everything below the `---`). Substack welcome emails cannot attach files, so replace the sentence "Your gift is attached:" with "Your gift is here:" and link the words **Seven Hebrew Words Every Christian Should Know** to the URL Evan provides; if he has not provided one yet, leave the words unlinked and flag it in your report.

### 1.5 Payments (Settings → Payments)
Enable paid subscriptions with these plans. **Do not paywall any post yet** — plans exist so readers who want to pay can, but all content stays free for two weeks.
- **Monthly:** `$7`
- **Annual:** `$60` (make annual the default/highlighted plan)
- **Founding:** `$180` — plan name `Founding Reader`
- **Free trial:** 7 days, on
- **Group subscriptions:** on, 20% off for groups of 5+ (if the option exists)
- **Subscriber benefits text** (shown on the subscribe page):
  - Free: `One Hebrew word every morning, complete. Free, always.`
  - Paid: `The secret inside the word, every weekday. About sixteen cents a day.`
  - Founding: `A signed book, and my thanks by name.`

### 1.6 Community (Settings → Community)
- Comments: **enabled**
- Who can comment: **paid subscribers** (if the option is per-post rather than global, leave the default and note it)
- Default comment sort: best first

### 1.7 Emails (Settings → Emails)
- Forward replies to Evan's inbox: **on** (readers are invited to reply with verses).
- Email "from" name: `Rabbi Evan Moffic`

### 1.8 Growth (Settings → Growth features)
- Recommendations: **on** (do not add any recommended publications yet).
- Subscriber referral program: **on**, with these rewards: 3 referrals → 1 month paid; 10 referrals → 1 year paid; 25 referrals → a signed book (enter as a custom reward if custom rewards are supported; otherwise use the closest available and note it).

---

## PART 2 — Posts

Posts are created from the files in the repository with the weekly Codex prompt in `one-word-wiser/handoff-prompts.md` ("Codex — upload a week's drafts to Substack"), which says exactly how to place the title, the body, the three cards and the paywall marker. Do not draft posts yourself. Every post: **Audience = Everyone. No section. Send as email = yes. Publish to web = yes. 6:00 am Central** (the launch evening post on September 12 is the one exception, 7:00 pm). The first two weeks are free: delete the `[PAYWALL]` line. From September 28, insert Substack's paywall divider where the line is.

The announcement post that used to be Post A is superseded; do not create or send it.

## PART 3 — Report back

When done, reply with this checklist, marking each item done / not done / done-with-difference (and what the difference was):

1. Name and tagline set
2. Logo and cover set (which file went where)
3. About page replaced
4. No sections created; old sections left unassigned
5. Welcome email subject and body set; PDF link status
6. Payment plans $7 / $60 / $180 set, annual default, 7-day trial on, group discount status
7. Benefits text set
8. Comments: enabled, paid-only status
9. Reply forwarding on; from-name set
10. Recommendations on; referral program on with rewards
11. Publication timezone confirmed as America/Chicago
12. Anything you could not find or had to approximate

Do not mark anything done that you did not verify on screen.
