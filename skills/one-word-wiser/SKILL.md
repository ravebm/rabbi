---
name: one-word-wiser
description: Draft posts for Rabbi Evan Moffic's Substack "One Word Wiser" (rabbi.substack.com) — the daily Hebrew-word newsletter for Christians and curious Jews, one post every morning. Use whenever Evan asks to write a day's post, "the week," "Tuesday's post for chesed," Saturday's Shabbat post from the Torah portion, a Sunday "Your Verse" post from a reader's verse, or the week-ahead footer; or when he names a Hebrew word and asks for the post. Reads one-word-wiser/word-bank.md for the week's words and their secrets and follows one-word-wiser/01-positioning.md (voice) and 02-daily-format.md (anatomy). Not for Already Home (Ram Dass) or pulpit sermons — those have their own skills.
---

# One Word Wiser — post production

Everything you need is in `one-word-wiser/`: `01-positioning.md` (voice rules, About copy), `02-daily-format.md` (exact anatomy of the three post types), `03-monetization.md` (where the gate goes and why), `word-bank.md` (the rubric, the calendar, and every week's six words with verse and secret), and `samples/` (the voice standard). One post a day, 6:00 am Central, seven days a week.

## Before drafting

1. **Read the samples.** `samples/week-01-monday.md` is the voice source of truth for a weekday post; `samples/week-01-shabbat-haazinu.md` for a Shabbat post. Match their rhythm: short declaratives, fragments, direct address, one anchor, the word as drumbeat.
2. **Find the week in `word-bank.md`.** Use its verse and secret as the starting point. If Evan gives a word not in the bank, run it through the five tests at the top of the bank (familiar, lost in English, teachable, a secret, sayable; four of five, and the secret is never the missing one), build the same row (Hebrew with niqqud, transliteration with stress, gloss, device, Hebrew Bible verse, the secret, optional Gospel echo), check the ledger at the bottom of the bank so the word hasn't run in the past year, and show the row to him above the draft.
3. **Verify every citation.** Chapter and verse for the Hebrew Bible (note when English and Hebrew numbering differ, e.g. Hosea 14:1/14:2). Tractate and page for the Talmud; section for Midrash; the comment for Rashi. When a Gospel is used, exact reference and NIV wording. The bank marks which gematria, acronyms and letter-plays are classical and which are later; the post says so too.
4. **Translations.** Hebrew Bible: render the verse from the Hebrew yourself, plainly, and mark it *(my translation)*; quote NIV alongside only when the familiar English wording is the point. Gospels: NIV. Never mix translations in one post without saying so. Never put a source in Evan's mouth you aren't sure of; if a story is folklore or disputed, leave it out and flag it below the draft.
5. **Check the Hebrew.** Root letters, niqqud on the headline word, transliteration consistent with the bank (*ch* for chet, *tz* for tzadi, no diacritics). Stress marked with CAPS on the stressed syllable.

## Output contract

Return each post as Substack-ready Markdown with this header block, then the body. Every post is **word → meaning → application**, and nothing else:

```
# [Weekday, Month D] — [☀️ THE WORD | 🕯️ SHABBAT | 📖 YOUR VERSE] · *word*
**Subject:** [per the subject-line system in 02]
**Audience:** Everyone · **Paywall:** at the door (weekdays, from week 3) | none · **Send:** 6:00 am CT
**Cards:** word-day at the top · line-day at the line to carry · line-night at the line to sleep on
**Notes:** (1) the line to carry, plain text, for 9 am  (2) the line to sleep on, plain text, for 9 pm
```

### Weekday post — ☀️ The Word (500–650 words)
Three beats, twice: free, then paid.
**Free half (300–400 words).** Hebrew script large and centered → transliteration (stress in CAPS) + gloss → "say it" line → the picture, only if the word gives one honestly (a root picture is a device, not a requirement) → **one** verse (English, translation named; then transliterated Hebrew with the word bolded) → the turn (2–4 short paragraphs, one idea: the teachable interpretation) → *one line to carry* in italic on its own line → **Today's question** → **the door**: one sentence naming what the secret answers ("*The secret inside teshuvah:* why…").
`` `[PAYWALL]` `` (weeks 1–2: delete the marker; the post runs whole)
**The secret (200–250 words).** The reading, 120–180 words: one **hidden layer** of the word that passes the sod test in `02-daily-format.md`: hidden, grounded, and turning the plain meaning over. Told as a scene, source named in the text, one image the reader keeps. Devices welcome, all the tradition's own and sourced: a gap in the verse, a vanished article, a buried root, an enlarged or dotted or broken letter, a letter's shape, a word used only of God, a re-vowelling, a gematria or acronym the rabbis made, a count. Use the secret named in the bank unless you have a better one; if a day has no real secret, say so instead of shipping a paraphrase. Then: the turn (40–60 words, to the reader's actual day, "you know the one") → one thing to do (one sentence, today or before bed) → *the line to sleep on* in italic → the close ("Tomorrow: *next word*, gloss.") → "— Rabbi Evan" → optional `Audio (~1:30)` script: the word three times, the line to carry, the one thing, the line to sleep on.
No rabbinic sources above the gate. Hebrew Bible only; when a word has a famous Gospel echo, one line ("*Where it echoes:* Mark 12:29") is enough, most days none. Once or twice a week at most the secret may end in a Gospel, when the word itself walks in (Week 9 excepted). No paid language anywhere. The door is a gift, not a tease.

### Shabbat post — 🕯️ the word from the portion (450–550 words + footer) — free, no gate
Open with the portion in one line ("This morning, in every synagogue in the world, the reading is Ha'azinu…"). Then the weekday anatomy with no gate: the secret runs open. Then the footer, **The week in five words**: the five weekday words (Hebrew · translit · gloss · the line to carry, each linked `[…](POST_URL)`), then the five lines to sleep on → the unchanging ask: *"If one of these words opened something for you this week, tell one person. A note from you reaches someone no ad ever could."* → "*Shabbat shalom.*" → "— Rabbi Evan". The word is never one of the week's five; on a festival Shabbat it comes from the festival reading. Mention the referral program here once a month, one line.

### Sunday post — 📖 Your Verse (400–550 words + footer) — free, no gate
Open with first name + state and the verse they sent → the weekday anatomy keyed to the word the verse turns on, secret open → "Send me a verse. Just reply to this email." → the footer, **The week ahead**: the theme and why now (portion, season, holiday) → the six words, Monday to Shabbat, one sentence each → "Tomorrow, 6:00: *word*. Say it once tonight so it's in your mouth: *…*" → "— Rabbi Evan". Until reader verses arrive, the week ahead stands alone as the Sunday post, subject `🌅 The week ahead: [theme]`.

### "Write the week"
When asked for a whole week, produce all seven posts in order, Monday through Sunday. Vary the secrets' sources across the week (never Rashi five days running), vary the closes, and make sure the five *lines to carry* and five *lines to sleep on* read well as sets: they appear together in Saturday's footer. Run the set test from the bank: the Sunday footer must say the week in one paragraph, one sentence per word, as a single thought. Add each word to the ledger at the bottom of `word-bank.md` with its date.

## Voice — non-negotiable
- Short declaratives; fragments; paragraphs of 1–3 sentences.
- Direct address: "Say it with me." "You know the one."
- Hebrew italicized and transliterated, glossed in the same breath, every time after the headline.
- The word appears 5–8 times above the gate.
- One anchor per secret. Told as a story. Named in the text, not footnoted.
- The letters and the numbers: wonder, as the tradition's play (see `01-positioning.md`). Gematria and letter-shapes are welcome in the secret, sourced and delighted in, never offered as proof.
- Warm, never cute. Respectful of Christian readers, never preachy toward them, never apologetic about being a rabbi. Where Jews and Christians read a verse differently: one honest sentence, hold both, move on.
- Never salesy. Banned: unlock, exclusive, don't miss, limited, last chance, upgrade (as a verb aimed at the reader).
- AI-smell list, strike on sight: framework, journey, navigate, leverage, delve, tapestry, "here's the thing," "let's dive in," announced connections ("this brings us to"), stacked adjectives, three-beat escalations, meta-narration.
- Sign "— Rabbi Evan".

## Cards (every post)
After the post is approved, render the day's cards from the template sources:

```
python3 one-word-wiser/brand/cards/render.py --date YYYY-MM-DD --hebrew "<word with niqqud>" \
  --translit <translit> --gloss "<gloss>" --date-label "<Weekday, Month D>" \
  --line-day "<the line to carry>" --line-night "<the line to sleep on>" \
  [--day-label "Shabbat" | "Your Verse"]
```

Output lands in `one-word-wiser/posts/cards/` as `<date>-word-day.png`, `-line-day.png`, `-line-night.png` (and a spare `-word-night.png`). Look at the word-day PNG once (Read) to confirm the Hebrew rendered in Frank Ruehl and nothing is clipped; then send Evan the three (`SendUserFile`) and commit them. Requires Chromium and Pillow; if either is missing, say so rather than substituting a stock image.

## After the draft
Below the post, in a short block for Evan: any citation you're less than certain of; any judgment call (a story left out, a translation choice, a play marked as later rather than classical); and one or two spots you'd tighten if he wants it shorter. Never make Evan find the AI-smell; remove it before presenting.
