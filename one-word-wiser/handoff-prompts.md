# Handoff prompts — paste one of these into the agent

All three agents work from the same repository: **github.com/ravebm/rabbi**. Give each one repo access (a clone, a connected GitHub account, or an upload of the folder), then paste the matching prompt. Every prompt starts with "read `AGENTS.md`," which is what keeps them in sync: if you change a skill or a doc in any one of them and it's committed, the others see it on their next pull.

---

## Codex — upload a week's drafts to Substack (the weekly one)

Every Sunday, once you say **approved**, the Sunday session hands you this prompt with the file list filled in; paste it into Codex. (For the launch weekend, fill it in from the list below.) Codex needs a browser and you logged in at rabbi.substack.com.

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
> - `one-word-wiser/samples/week-01-monday.md` — Monday, September 14, 6:00 am
> - `one-word-wiser/samples/week-01-shabbat-haazinu.md` — Saturday, September 19, 6:00 am
> - `one-word-wiser/samples/week-01-sunday.md` — Sunday, September 20, 6:00 am
>
> Schedule: yes

Tuesday through Friday of week 1 are produced by the skill ("write the week") and saved in `one-word-wiser/posts/` once you approve them; add them to the list the same way.

## Hermes — set up Substack (once)

> You have access to my repository `ravebm/rabbi` (pull the latest first). Read `AGENTS.md` at the root, then follow `one-word-wiser/operator-brief-substack-setup.md` exactly, start to finish. I am logged into Substack at rabbi.substack.com. Paste every piece of copy verbatim from the brief and the files it points to; do not rewrite anything. Do not publish, email, or change anything the brief does not list. When you finish, reply with the checklist at the end of the brief, and if anything in Substack's interface didn't match the brief, tell me which step rather than improvising. If you had to change anything in the repository (you shouldn't need to), commit it with a one-line message and push.

## Codex or Claude in Chrome — LAUNCH DAY (the short one)

> Open my repository `ravebm/rabbi` (pull the latest). Read `AGENTS.md`, then follow `one-word-wiser/operator-brief-launch-day.md` exactly, top to bottom. I am logged into Substack at rabbi.substack.com. Upload the logo, set the name and description, clear out the old benefits and welcome email and replace them with the new ones, replace the About page, and create the launch posts as drafts with their images. Do not publish or schedule anything until I say "go". Paste all copy verbatim. When done, send me the draft links and the report at the end of the brief.

## Claude — write, edit, or update the system

> Pull `ravebm/rabbi`, read `AGENTS.md`, and [write Tuesday's post for *shema* / write the week / draft Saturday from the portion / update the skill so that … ]. Commit and push whatever you change so Hermes and Codex see it.

## Codex — write posts

> Open my repository `ravebm/rabbi` and pull the latest. Read `AGENTS.md` at the root, then `skills/one-word-wiser/SKILL.md`, then `one-word-wiser/samples/week-01-monday.md` and `week-01-shabbat-haazinu.md`. Using `one-word-wiser/word-bank.md`, draft [the week of … / Tuesday through Friday of week 1] in the skill's output contract: one post a day, the door and `[PAYWALL]` marker at the question, the secret below it. Save each post as `one-word-wiser/posts/YYYY-MM-DD.md`, commit with the message "Week N drafts: <words>", and push to a branch named `posts/week-NN`. Do not publish anything. Below the drafts, list any citation you are less than certain of.

## Any agent — draft the free book, *Seven Hebrew Words Every Christian Should Know*

Paste this into whichever tool you want to draft in. It stands on its own; the agent does not need the repository. Read the draft before anyone lays it out, and check every citation it lists as uncertain.

> You are drafting a short free book for Rabbi Evan Moffic. It is the welcome gift for new subscribers to *One Word Wiser* (rabbi.substack.com), a newsletter that teaches Christians and curious Jews one Hebrew word a day. Evan is a rabbi handing Christians a key to their own Bible. He is not converting anyone in either direction.
>
> **Title:** *Seven Hebrew Words Every Christian Should Know*. **Author:** Rabbi Evan Moffic. **Length:** about 1,700 words. Ten pages: a cover, a short note from Evan, seven word pages, a last page.
>
> **The seven words, in this order:** *shalom, chesed, emunah, teshuvah, ruach, hallelujah, amen.*
>
> **Every word page has these six parts, in this order, and nothing else:**
>
> 1. The word in Hebrew with vowels, large. Under it, the transliteration in italics and a one- or two-word English gloss. (שָׁלוֹם · *shalom* · peace, wholeness)
> 2. **Say it.** One line: which syllable carries the stress, and how to make any sound English lacks (*chesed* starts in the throat, like the *ch* in Bach).
> 3. **The picture.** Two to four sentences: what the root means in its plainest, most physical sense, and how the familiar meaning grows out of it. *Shalom* is from *shalem*, whole, complete, paid in full: peace is nothing missing. *Emunah* is from *aman*, firm, steady, the root of *amen*: faith is a verb of standing. Give a root picture only where the etymology is real; never force one.
> 4. **One verse** from the Hebrew Bible where the word does its work. Quote the NIV, with book, chapter and verse, then one sentence naming the Hebrew word under the English ("The word under 'peace' is *shalom*."). Where the Hebrew and English verse numbers differ, give both. If you are not certain of a citation, choose another verse you are certain of.
> 5. **Where you already say it.** One or two sentences on where this word lives in a Christian's week: a Gospel or New Testament verse that carries it (Jesus greeting the disciples with *shalom*, John 20:19; Habakkuk 2:4's *emunah* quoted in Romans 1:17), a hymn, a line of the liturgy. Cite chapter and verse. Say "Matthew," "John," "Jesus," never "the Christian Bible."
> 6. **A line to carry.** One sentence, under fifteen words, in italics. Something a reader could keep for the day.
>
> Each word page is 180 to 220 words. The word itself should appear four or five times on its page.
>
> **The note from Evan** (page 2, under 120 words): why one Hebrew word is worth a page, first person, warm, no biography beyond "I'm a rabbi." **The last page** (under 80 words): one sentence that one word arrives every morning at rabbi.substack.com, and the invitation: "Send me a verse. Any verse. I'll show you the Hebrew underneath." No price, no "subscribe," no urgency.
>
> **Voice.** "Hebrew Bible" and "New Testament" are the two names, every time; never "Old Testament," "the Greek Bible," or "your Bible" (the reader and the writer share the book; say "the English" when the point is the wording). Short declaratives; fragments welcome. Direct address ("Say it with me."). Warm, never cute; respectful, never preachy. Hebrew always transliterated, italicized and glossed in the same breath. Where Jews and Christians read a verse differently, say so in one sentence and move on. Strike on sight: framework, journey, navigate, leverage, unlock, delve, tapestry, exclusive, "here's the thing," "let's dive in," announced connections ("this brings us to"), stacked adjectives, three-beat escalations.
>
> **What the book is not.** No grammar, no alphabet chart, no footnotes, no lists of every place the word occurs, no rabbinic sources, no gematria. The book is the free half of the teaching, complete on its own; the newsletter goes deeper each morning.
>
> **Suggested verses** (verify each; swap any you can't confirm):
> - *shalom*: Numbers 6:26 (the priestly blessing ends in it); Isaiah 26:3 (*shalom shalom*). New Testament: John 20:19, 21, 26.
> - *chesed*: Psalm 136 (the refrain *ki l'olam chasdo*); Micah 6:8; Lamentations 3:22. New Testament: Jesus quotes Hosea 6:6, "I desire *chesed*, not sacrifice," in Matthew 9:13 and 12:7; the English there says "mercy."
> - *emunah*: Exodus 17:12 (Moses's hands were *emunah*, steady, until sunset); Habakkuk 2:4; Genesis 15:6. New Testament: Romans 1:17, Galatians 3:11 and Hebrews 10:38 all quote Habakkuk 2:4.
> - *teshuvah*: Hosea 14:2 (14:1 in Christian Bibles), *Shuvah Yisrael*; Deuteronomy 30:2. New Testament: Mark 1:15 ("repent"); Luke 15:17–20, the son who came to himself and went home.
> - *ruach*: Genesis 1:2; Ezekiel 37:9. New Testament: John 3:8, where "wind" and "Spirit" are one word, exactly as in Hebrew.
> - *hallelujah*: Psalm 150:6; Psalm 146:1. New Testament: Revelation 19:1–6, the only place the New Testament says the word, and it says it in Hebrew.
> - *amen*: Deuteronomy 27:15–26 (the people answer *amen* twelve times); Isaiah 65:16 ("the God of *amen*"). New Testament: John 1:51 and the "Amen, amen, I say to you" sayings (in the Hebrew Bible *amen* answers what was just said; Jesus opens with it); 2 Corinthians 1:20; Revelation 3:14.
>
> **Output:** If you have the repository, write the text into `one-word-wiser/book/seven-words.md`, replacing each `[[…]]` placeholder and changing nothing else (the Hebrew, transliterations and glosses there are already correct); `one-word-wiser/book/build.py` makes the PDF. Otherwise: Markdown, one page per section, `---` between pages, so it can be dropped into Google Docs, Pages or Canva. For whoever lays it out: navy `#1B2A41` on off-white `#F6F3EC`, gold `#A8781C` for small caps and rules, EB Garamond for English, Frank Ruehl Libre for Hebrew, one word per page with a lot of air; this matches the newsletter's cards. Below the draft, list every citation you are less than certain of.

## Codex — redraft the free book (only if the text changes)

The book is drafted and built (`one-word-wiser/book/seven-words.pdf`, September 13). Use this only if Evan wants the text changed; otherwise skip to the next prompt.

> Open my repository `ravebm/rabbi` and pull the latest `main`. Read `AGENTS.md`, then `one-word-wiser/01-positioning.md` (the voice rules), then `one-word-wiser/book/README.md`, then the drafting brief in `one-word-wiser/handoff-prompts.md` under "draft the free book." Write the book into `one-word-wiser/book/seven-words.md`: replace every `[[…]]` placeholder following the brief, and change nothing else in that file (the Hebrew, transliterations and glosses are already correct). Verify every citation before you use it; if you are not certain of one, use another verse you are certain of.
>
> Then build it: `python3 one-word-wiser/book/build.py --all-previews`. It needs Python 3 and Google Chrome or Chromium (add `--chromium /path/to/chrome` if it cannot find one). If it reports a placeholder or an overflowing page, fix the text and run it again. Look at every image in `one-word-wiser/book/preview/`: ten pages, the Hebrew with its vowels, nothing cut off, the line to carry at the foot of each word page.
>
> Commit `seven-words.md`, `seven-words.pdf`, `preview-cover.png` and `preview-word.png` (not the `preview/` folder) with the message "Seven Words book: draft and PDF", push to a branch named `book/seven-words`, and open a pull request against `main`. In the pull request description, list every citation you were less than certain of. Do not touch Substack. Stop there: Evan reads the PDF before it goes up.

## Codex — put the free book on Substack and wire the welcome email (once, after Evan has read the PDF)

> Pull the latest `main` of `ravebm/rabbi` (the pull request that carries the book is merged) and open `one-word-wiser/book/README.md`.
>
> On rabbi.substack.com, create a new post from "The download post" in that README: paste the title, subtitle and body verbatim. Where the body says to attach the PDF, use the editor's file attachment (the paperclip or "+" menu, then File) to attach `one-word-wiser/book/seven-words.pdf`. Audience: Everyone. Section: none. Set the post's URL slug to `seven-words` if the post settings allow. Publish it to the web only: in the publish step choose the option that does not send an email. If you cannot find a way to publish without emailing, stop and report; do not send the list an email. Copy the published post's URL.
>
> Then Settings → Emails → Welcome email. Subject: `Your first seven words`. Body: everything below the `---` in `one-word-wiser/samples/welcome-email.md`, entered as formatted text (bold and italics applied in the editor, no markdown symbols), with the book's title linked to the post URL; that link is what `SEVEN_WORDS_URL` stands for. Save it, open the preview, and confirm the link opens the post.
>
> Back in the repository, put the post URL in `one-word-wiser/book/README.md` under "Where it lives" in place of *not yet*, commit with the message "Seven Words book: live at <URL>", and push to `main`. Report the post URL, that it was published without an email, and that the welcome email now links to it. Change nothing else on Substack.

## Sunday night — the week's document (automatic)

A scheduled session runs every Sunday at 4:00 pm Central (3:00 pm once the clocks change) and does the Sunday session on its own: it drafts the coming week from `word-bank.md` with the skill, renders the cards, pushes a `posts/week-NN` branch as a draft pull request, puts all seven posts in one Google Doc shared to Evan, and reports the Doc and the pull request. Evan edits the Doc, then opens that session and says **approved** (or says what to change). The session reads the Doc back, applies every edit to the files, fixes anything that broke the format or the voice and says what it fixed, re-renders any card whose line changed, marks the pull request ready, and hands back the Codex upload prompt above, filled in. Evan pastes it into Codex, and the week is scheduled. That paste is the one step no agent here can do: Substack has no API.

To change the hour, the day, or what the session does, ask Claude to update the routine ("One Word Wiser · Sunday week draft").

---

## When you change something

Make the change in any one agent, and make sure it ends in a commit to the repo. That's it. The other two agents pull before they work, so they inherit it. If an agent ever seems to be working from an old version, tell it: "pull the latest and re-read `AGENTS.md`."

## One-time setup

1. Give Hermes and Codex access to the repository.
2. Upload the two logo files to `one-word-wiser/brand/` (any agent can do this if you give it the files) so the operator brief can point to them.
