---
name: one-word-wiser
description: Draft, revise, or format Rabbi Evan Moffic's One Word Wiser Substack posts, including weekday Hebrew words, Shabbat posts, Sunday Your Verse posts, and a full week. Preserve his edits and prepare readable Substack copy with short paragraphs, subheadings, and restrained dividers. Not for Already Home or pulpit sermons.
---

# One Word Wiser — post production

Everything you need is in `one-word-wiser/`: `01-positioning.md` (voice rules, About copy), `02-daily-format.md` (exact anatomy of the three post types), `03-monetization.md` (where the gate goes and why), `word-bank.md` (the rubric, the calendar, and every week's six words with verse and secret), and `samples/` (the voice standard). One post a day, 6:00 am Central, seven days a week.

## Before drafting

For drafting, revision, or Substack layout, read [the readability standard](references/substack-readability.md). Evan's latest draft edits override older sample wording. Use the recurring application heading **Let It Change Your Life**, short native subheadings, and restrained typographic dividers across all post types. A small centered Hebrew letter can be used in the divider. These presentation choices do not change the free/paid boundary or grant delivery permission.

1. **Read the samples.** `samples/week-01-monday.md` is the voice source of truth for a weekday post; `samples/week-01-shabbat-haazinu.md` for a Shabbat post; `samples/week-01-sunday.md` for a Sunday post. Match their rhythm: short declaratives, fragments, direct address, one anchor, the word as drumbeat.
2. **Find the week in `word-bank.md`.** Use its verse and secret as the starting point. If Evan gives a word not in the bank, run it through the five tests at the top of the bank (familiar, lost in English, teachable, a secret, sayable; four of five, and the secret is never the missing one), build the same row (Hebrew with niqqud, transliteration with stress, gloss, device, Hebrew Bible verse, the secret, optional Gospel echo), check the ledger at the bottom of the bank so the word hasn't run in the past year, and show the row to him above the draft.
3. **Verify every citation.** Chapter and verse for the Hebrew Bible (note when English and Hebrew numbering differ, e.g. Hosea 14:1/14:2). Tractate and page for the Talmud; section for Midrash; the comment for Rashi. When a Gospel is used, exact reference and NIV wording. The bank marks which gematria, acronyms and letter-plays are classical and which are later; the post says so too.
4. **Translations.** Every verse from the NIV, Hebrew Bible and New Testament alike, then one line naming the Hebrew word under the English ("The word under 'hear' is *shema*"), then the transliterated phrase with the word bolded. No "my translation." Never mix translations in one post. Never put a source in Evan's mouth you aren't sure of; if a story is folklore or disputed, leave it out and flag it below the draft.
5. **Check the Hebrew.** Root letters, niqqud on the headline word, transliteration consistent with the bank (*ch* for chet, *tz* for tzadi, no diacritics). Stress marked with CAPS on the stressed syllable.

## Output contract

Return each post as Substack-ready Markdown with this header block, then the body. Every post is **word → meaning → application**, and nothing else:

```
# [Weekday, Month D] — [☀️ THE WORD | 🕯️ SHABBAT | 📖 YOUR VERSE] · *word*
**Subject:** [per the subject-line system in 02]
**Audience:** Everyone · **Paywall:** at the door (weekdays, from week 3) | none · **Send:** 6:00 am CT
**Cards:** word-day at the top · line-day at the line to carry · line-night at the line to sleep on
**Dividers:** [placement and treatment; a centered Hebrew letter or plain rule at a natural pause]
**Notes:** (1) the line to carry, plain text, for 9 am  (2) the line to sleep on, plain text, for 9 pm
```

### Weekday post — ☀️ The Word (400–600 words)
The teaching is the body and it is free; the door hints at a need and at what God asks; the second half delivers both.
**Free half (250–350 words): the teaching.** **Fixed opening, first thing, every post:** two lines — `**In English:** *<the translated word>.*` / `**In Hebrew:** *<translit>* — <the picture, 5–10 words>.` Never "your Bible" or "the Christian Bible"; a translation versus the original. The Hebrew line must feel essential — a correction with stakes ("come home"), never a dictionary gloss ("return"). Then the Word card. Hebrew script large and centered → transliteration (stress in CAPS) + gloss → "say it" line → the picture, only if the word gives one honestly (a root picture is a device, not a requirement) → **one** verse (NIV, then "The word under '…' is *…*", then transliterated Hebrew with the word bolded) → the turn (2–4 short paragraphs, one idea: the teachable interpretation; this is the main body) → the teaching ends on its strongest plain sentence (the italic *line to carry* is optional: cut it when it only repeats the body; it still goes in the header's Notes line and in Saturday's footer) → **the door**: one short italic paragraph that states the surprising teaching in plain words and ends on the question a reader would ask (model: `one-word-wiser/posts/2026-09-14.md`: "*But the Jewish sages said one fascinating thing about teshuvah. They said a person who has done teshuvah is more righteous than a person who never had to make teshuvah. So a person who has sinned is more righteous than someone who has not?*"). It names something the reader wants to know about their own life and promises a deeper understanding of what God asks. A secret and an insight, never a pitch, never a formula. No "Today's question."
`` `[PAYWALL]` `` (weeks 1–2: delete the marker; the post runs whole)
**Paid half (150–250 words): the secret.** The secret, 100–180 words, told simply: one **hidden layer** of the word that passes the sod test in `02-daily-format.md`, told as a scene, the source named in plain words and explained the first time it appears (the Talmud, Rashi, Maimonides, a Midrash: a few words each), a New Testament parallel named plainly when there is a natural one and the week's limit allows, one image the reader keeps (devices welcome, all the tradition's own and sourced; use the bank's secret unless you have a better one; if a day has no real secret, say so instead of shipping a paraphrase) → at most one plain sentence of application, only when there is a concrete one (no "you know the one" paragraphs) → *the line to sleep on*, which carries the action → the close ("Tomorrow: *next word*, gloss.") → "— Rabbi Evan" → optional `Audio (~1:30)` script.
No rabbinic sources above the gate. Hebrew Bible only; when a word has a famous Gospel echo, one line ("*Other mentions:* Mark 12:29") is enough, most days none. Once or twice a week at most the secret may end in a Gospel, when the word itself walks in (Week 9 excepted). No paid language anywhere. The door is a gift, not a tease.

### Shabbat post — 🕯️ the word from the portion (450–550 words + footer) — free, no gate
Open with the portion in one line ("This morning, in every synagogue in the world, the reading is Ha'azinu…"), then the two fixed lines (In English / In Hebrew) for the portion's word. Then the weekday anatomy with no gate: the secret runs open. Then the footer, **The week in five words**: the five weekday words (Hebrew · translit · gloss · the line to carry, each linked `[…](POST_URL)`), then the five lines to sleep on → the unchanging ask: *"If one of these words opened something for you this week, tell one person. A note from you reaches someone no ad ever could."* → "*Shabbat shalom.*" → "— Rabbi Evan". The word is never one of the week's five; on a festival Shabbat it comes from the festival reading. Mention the referral program here once a month, one line.

### Sunday post — 📖 Your Verse (400–550 words + footer) — free, no gate
Open with first name + state and the verse they sent → the two fixed lines (In English / In Hebrew) for the word the verse turns on → the weekday anatomy keyed to that word, secret open → "Send me a verse. Just reply to this email." → "Tomorrow: *word*, gloss." → "— Rabbi Evan". No footer: the week is not previewed beyond that one line. Until reader verses arrive, Evan picks the verse (the one Christians ask a rabbi about most) and the post says so in one plain line at the top; the subject line stays `📖 Your verse: [reference]` (`samples/week-01-sunday.md`).

### "Write the week"
When asked for a whole week, produce all seven posts in order, Monday through Sunday. Vary the secrets' sources across the week (never Rashi five days running), vary the closes, and make sure the five *lines to carry* and five *lines to sleep on* read well as sets: they appear together in Saturday's footer. Run the set test from the bank: the five weekday words must say the week in one paragraph, one sentence per word, as a single thought; they stand together in Saturday's footer. Add each word to the ledger at the bottom of `word-bank.md` with its date.

## Voice — non-negotiable
- Short declaratives; fragments; paragraphs of 1–3 sentences.
- Simple and short, for a reader who knows nothing about Judaism. Explain a name the first time it appears, in a few plain words: the Talmud, a Midrash, Rashi, Maimonides, a Torah scroll, Rosh Hashanah. "The Jewish sages" when a teaching is introduced; "the English translation is usually…" when the English word is named, because it is a choice.
- Say it once. No italic restatement of what the paragraph just said, no aphoristic flourish after the point lands ("The turn can be tiny. The response is wagons." was cut for this). Split a paragraph rather than let it run.
- A New Testament parallel is named plainly when there is a natural one ("one closely paralleling the parable of the prodigal son"), within the week's limit.
- Direct address: "Say it with me." "You know the one."
- Hebrew italicized and transliterated, glossed in the same breath, every time after the headline.
- The word appears 5–8 times above the gate.
- One anchor per secret. Told as a story. Named in the text, not footnoted.
- The letters and the numbers: wonder, as the tradition's play (see `01-positioning.md`). Gematria and letter-shapes are welcome in the secret, sourced and delighted in, never offered as proof.
- Warm, never cute. Never preachy, never apologetic about being a rabbi. No us and them: never sort the reader and the writer into two groups ("a Jew says," "your church," "Christians hear… the rabbis heard…"); describe the practice, not the people. Where a verse is read two ways: one honest sentence, hold both, move on.
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

Output lands in `one-word-wiser/posts/cards/` as `<date>-word-day.png`, `-line-day.png`, `-line-night.png` (and a spare `-word-night.png`). Inspect the word-day PNG to confirm the Hebrew rendered in Frank Ruehl and nothing is clipped; show Evan the cards actually used and commit them. Do not place a line-day card if the separate line to carry was cut. Requires Chromium and Pillow; if either is missing, say so rather than substituting a stock image. The body uses restrained typographic dividers; do not add decorative illustrations by default.

## After the draft
Below the post, in a short block for Evan: any citation you're less than certain of; any judgment call (a story left out, a translation choice, a play marked as later rather than classical); and one or two spots you'd tighten if he wants it shorter. Never make Evan find the AI-smell; remove it before presenting.
