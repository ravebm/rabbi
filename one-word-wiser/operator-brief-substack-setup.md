# Operator brief — set up One Word Wiser on Substack

*For any agent operating Substack on Evan's behalf (Hermes, Codex, Claude). Read `AGENTS.md` at the repository root before starting.*

You are configuring an existing Substack publication for Rabbi Evan Moffic. The publication is **rabbi.substack.com** (name: *One Word Wiser*). Evan is logged in. This document is complete: every setting and every piece of copy you need is here. Do exactly what it says, in order, and nothing more. Where it says **paste**, paste the text verbatim — do not rewrite, shorten, or "improve" any copy.

## What this publication is (context only)

A twice-daily Hebrew-word newsletter for Christians (and curious Jews). **Morning post** (6:00 am Central, Mon–Fri): one Hebrew word, free, complete. **Evening post** (7:00 pm Central, Mon–Fri): the secret inside that word — the layer the rabbis called *sod* — and one small thing to do with it before bed; paid, with two free lines above the paywall. **Saturday** 7:00 pm: free recap. **Sunday** 6:00 am and 7:00 pm: free. The publication launches on Rosh Hashanah — Friday, September 11 — with a morning and evening post on the word *shanah*. The first two weeks are entirely free; the evening paywall turns on in week 3.

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

I'm Rabbi Evan Moffic. I've spent twenty years teaching Hebrew and the Jewish roots of the Bible to churches, and I've written several books about it, including *What Every Christian Needs to Know About the Jewishness of Jesus*. This newsletter is the most direct version of that work: one word, twice a day.

**Every morning (free):** one Hebrew word — its root, the picture inside it, and one verse you've read your whole life that changes when you see it.

**Every evening (paid):** the secret inside the word. The rabbis taught that every word of Scripture has four layers, and they called the deepest one *sod* — secret. That's the evening: the hidden layer — a gap in the verse, a root the translation buried, a reading that turns the plain meaning over — and one small thing to do with it before bed. Ninety seconds. The same shape every night.

**Saturday:** Shabbat rest. One short recap of the week's five words.
**Sunday:** *Your Verse* — you send me a verse, I show you the Hebrew underneath.

Free is genuinely free. You'll get the morning word every day, complete, without paying a cent — and a line from each evening to sleep on. Paid — $60 a year, about sixteen cents a night — is the secret, every evening, and my thanks for making this possible.

Whether you're Christian, Jewish, or simply curious: welcome. Send me a verse anytime. Just reply.

### 1.3 Sections (Settings → Sections)
Create two sections. Subscribers must be able to opt out of either one individually.
1. **Name:** `Morning` — **Description:** `One Hebrew word every weekday morning. Free.` — Include all existing subscribers: **yes**.
2. **Name:** `Evening` — **Description:** `What the rabbis saw in today's word, and one thing to do with it before you sleep. Weekday evenings.` — Include all existing subscribers: **yes**.

Do not create any other sections. Do not set either section to "paid only" — audience is controlled per post.

### 1.4 Welcome email (Settings → Emails → Welcome email)
- **Subject:** `Your first seven words`
- **Body:** paste the following. Where it says `[turn off Evening here]`, link that phrase to the subscriber's section-preferences / manage-subscription page (Substack provides a link to it; if there is no direct link, link to the publication's `/account` page). Where it says the PDF is attached: Substack welcome emails cannot attach files, so replace the sentence "Your gift is attached:" with "Your gift is here:" and link the words **Seven Hebrew Words Every Christian Should Know** to the URL Evan provides; if he has not provided one yet, leave the words unlinked and flag it in your report.

Welcome. I'm glad you're here.

Your gift is attached: **Seven Hebrew Words Every Christian Should Know.** Seven pages, one word each — *shalom, chesed, emunah, teshuvah, ruach, hallelujah, amen.* Print them. Put one in your Bible. That's how this works.

Here's what happens next:

**Tomorrow morning at 6:00** — one Hebrew word arrives. Its root, its picture, one verse. Two minutes.

**Tomorrow evening at 7:00** — the secret inside that word, and one small thing to do with it before bed.

Saturday: a short recap of the week's five words. Sunday: a reader's verse, in Hebrew.

Two a day is a lot. If you want mornings only, [turn off Evening here](SUBSTACK_SECTION_SETTINGS_LINK). You'll still get everything free.

One more thing. **Send me a verse.** Any verse — the one on your wall, the one you can't shake, the one that never made sense. Reply to this email. Every Sunday I take one and show the Hebrew underneath, and yours is in the queue the moment you send it.

That's it. No grammar, no drills. One word, one verse, one rabbi.

— Rabbi Evan

*Mornings are free, always. The evening is for paid subscribers — $60 a year, about sixteen cents a night. But there's no hurry, and there's no catch. Read for a while first.*

### 1.5 Payments (Settings → Payments)
Enable paid subscriptions with these plans. **Do not paywall any post yet** — plans exist so readers who want to pay can, but all content stays free for two weeks.
- **Monthly:** `$7`
- **Annual:** `$60` (make annual the default/highlighted plan)
- **Founding:** `$180` — plan name `Founding Reader`
- **Free trial:** 7 days, on
- **Group subscriptions:** on, 20% off for groups of 5+ (if the option exists)
- **Subscriber benefits text** (shown on the subscribe page):
  - Free: `One Hebrew word every morning. Free, always.`
  - Paid: `The secret inside the word, every evening. About sixteen cents a night.`
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

## PART 2 — Posts to schedule

Every post carries two images from the template at https://claude.ai/code/artifact/5bd876b1-3c39-4e8a-a135-6579f2d67c96 (or supplied by Evan as PNGs): the **Word card** as the first image in the body, and the **Line card** in place of the italic one-line sentence near the end. If the PNGs are not supplied, leave the italic line as text and note it in the report.

Every post below: **Audience = Everyone (free). Section as noted. Send as email = yes. Also publish to web = yes.** Use the subject line as the post title unless a separate title is given. Keep all italics, bold, and line breaks. Where Hebrew script appears, paste it exactly — do not transliterate it or drop the vowel marks. Each post ends with `— Rabbi Evan` as its final line.

Dates are 2026, Central time.

### Post A — Announcement · schedule **Thursday, September 10, 8:00 am**
- Section: Morning
- Title: `One Word, Twice a Day`
- Subtitle: `This newsletter is changing. Here's what you'll get now.`
- Body:

# One Word, Twice a Day

The Bible was not written in English.

You know that. But most of us read it as if it were. And so we miss things. Not small things. The pictures inside the words.

In Hebrew, *hope* is a rope. *Peace* means *whole*. The word your Bible translates "repent" doesn't mean feel sorry. It means *come home*.

I've spent twenty years teaching this to churches. One word at a time, in fellowship halls and sanctuaries, on Sunday mornings and Wednesday nights. It's the work that produced my books, and it's the work I love most.

So I'm making it the whole point of this newsletter.

Starting Monday, *One Word Wiser* becomes what its name says.

**Every morning, one Hebrew word.** Its root. The picture inside it. One verse you've read your whole life that changes when you see the Hebrew under it. Two minutes. Free.

**Every evening, the secret inside it.** The rabbis taught that every word of Scripture has a hidden layer — they called it *sod*, secret. That's the evening: the layer under the word, and one small thing to do with it before bed. Ninety seconds. The same shape every night.

Saturday is Shabbat. One short recap of the week's five words. Sunday, *your* verse — you send me one, I show you the Hebrew underneath. Just reply to any email.

A few honest things:

Two emails a day is more than you're used to from me. If you only want mornings, there's a switch. Go to your subscription settings and turn off *Evening*. You'll still get everything else, and I won't be offended.

For the first two weeks, all of it is free. After that, the morning stays free — always — and the evening becomes the paid part. About sixteen cents a night. I'll tell you plainly when it starts. Nothing in the morning will become less.

And if you're Jewish and reading this thinking, *he's writing for Christians now* — yes, mostly. But every morning post is Torah. You'll like it too.

This week is the Days of Awe. The ten days between Rosh Hashanah and Yom Kippur, when the whole Jewish year turns on one word.

Monday morning, that's the word.

See you at sunrise.

— Rabbi Evan

*P.S. — Say it with me now, so you're ready: תְּשׁוּבָה. Teh-shoo-VAH.*

### Post L1 — THE LAUNCH · Friday morning · schedule **Friday, September 11, 6:00 am**
- Section: Morning
- Title: `☀️ Happy New Year`
- Subtitle: `One Hebrew word, twice a day, starting now.`
- Body (center the Hebrew word and the transliteration line if the editor allows). The opening section in bold is the introduction to the new format — keep it exactly as written, including the horizontal rule after it:

Tonight begins the Jewish New Year, Rosh Hashanah. May it be filled with blessings.

A new year seemed like the right time for a new beginning here, too. Over the years, the question you've asked me more than any other is about Hebrew — what a word really means, and what it opens up in the Bible. So that's what this newsletter becomes today.

If that isn't for you, please feel free to unsubscribe. No offense taken, and my warmest wishes for the year ahead.

**A word before the word.**

Every morning, one Hebrew word. The language the Bible was written in. Not a grammar lesson — a door. Because when you see the picture inside a word, a verse you've read a hundred times opens. And so does something in you.

Hebrew isn't like other languages. The rabbis said God created the world with these letters — that before there was light, there was the word for it. Every letter has a shape and a story: *bet* is a house, *ayin* is an eye, *shin* looks like a flame. Every word grows from a three-letter root, so words that seem unrelated in English turn out to be family in Hebrew — *hope* and *rope*, *repent* and *return*, *year* and *change*. When you learn one Hebrew word, you don't learn a definition. You learn how God's language sees the thing.

Every evening, the secret inside the word — the layer the rabbis called *sod* — and one small thing to do with it before bed.

That's all. One word, twice a day. Whether you're Christian or Jewish or simply hungry for something true, you're welcome here. My hope is plain: that you'll feel closer to God's word than you ever have. And a little closer to yourself.

Tonight, the year turns. Let's begin.

---

<div align="center">

# שָׁנָה

*shanah* (shah-NAH) — year

</div>

Say it once. *Shanah.* You've heard it before, even if you didn't know it. This weekend, every Jew you know will say it to someone: *Shanah tovah.* A good year.

Tonight, at sundown, the Jewish year turns. Rosh Hashanah. Literally, "the head of the year."

So let's start there. With the word for year.

*Shanah* grows from three letters — *shin, nun, hey* — and those three letters mean *to repeat.* The word *mishnah*, the great collection of rabbinic teaching, means "repetition." The word *sheni* means "second." A *shanah* is the thing that comes around again. The same holidays. The same table. The same you.

Here's what the dictionary won't tell you. Those same three letters also mean *to change.* *Shinui* is change. *L'shanot* is to alter something. Same root. Same word, really.

Repeat. Change. Hebrew refuses to separate them.

Here's the verse. It's Moses, describing the land Israel is about to enter:

> **"The eyes of the LORD your God are always on it, from the beginning of the year to the end of the year."** — Deuteronomy 11:12 (my translation)
> *Mereshit hashanah v'ad acharit shanah.*

A year, this verse says, is something God watches all the way through. Not just at the turning. All of it.

Which means the question a new year asks isn't *what will be different?* Everything comes back around. The question is: *inside the same, what will I change?*

*A year is what repeats. A year is what changes. In Hebrew, that's one word.*

**Today's question:** What in your life is about to come around again — and what will you do differently inside it?

Tonight: why that verse begins with "*the* year" and ends with "*a* year" — and what the rabbis heard in the difference.

— Rabbi Evan

### Post L2 — THE LAUNCH · Friday evening · schedule **Friday, September 11, 7:00 pm**
- Section: Evening
- Title: `🌙 the secret inside shanah · the year that lost its "the"`
- Body. Delete the line that says `[PAYWALL]` — no paywall during launch.

This morning, *shanah.* Year. The word that means *repeat* and *change* at once.

*Every year begins as "the year." The work is to keep it from ending as "a year."*

`[PAYWALL]`

Read the verse again, slowly, in Hebrew this time. *Mereshit* **ha**-*shanah* — from the beginning of *the* year. *V'ad acharit* *shanah* — to the end of *a* year.

The little word *ha* — "the" — is there at the start. It's gone by the end.

The Hasidic masters noticed. And they read it the way you'd read a diary.

At the beginning, every year is *the* year. The one. This is the year I'll call my brother. The year I'll finally slow down. The year I'll stop pretending I'm fine. On the first night, the year has a definite article. It's *the* year.

By the end, it's *a* year. One more. Another one gone. The article fell off somewhere around February.

But look at what the verse actually says. *The eyes of the LORD are on it* — from the beginning to the end. The year didn't lose God's attention. It lost ours.

That's the whole holiday, in one missing syllable.

You know how this goes. You've had a *the*-year before. You may have had one this time last year. Tonight, before the new one starts, one small thing: write down one sentence — *This is the year I ______.* Just one. Then put it somewhere you'll find it in the spring, when the year has quietly become *a* year, and let it surprise you.

*God's eyes are on the year at the end as much as at the beginning. Yours can be too.*

*Shanah tovah* — a good year. Tomorrow is Shabbat and Rosh Hashanah, so no morning post. Sunday evening: the week ahead.

— Rabbi Evan

### Post B — Sunday evening · schedule **Sunday, September 13, 7:00 pm**
- Section: Morning
- Title: `🌅 The week ahead: Five words for the Days of Awe`
- Body:

# Five Words for the Days of Awe

Tonight begins the strangest week on the Jewish calendar.

Rosh Hashanah is behind us. Yom Kippur is a week away. The rabbis call these the *Aseret Yemei Teshuvah* — the Ten Days of Return. Not a holiday. A hallway. Ten days when the whole tradition says: the door is open, walk back through it.

If you've ever wondered what it feels like inside a synagogue right now, this week is your answer. Five words, one a morning, each one carrying a piece of the season.

**Monday — תְּשׁוּבָה · *teshuvah* · return.** The word everything turns on. It's usually translated "repentance." It doesn't mean that.

**Tuesday — שְׁמַע · *shema* · hear.** The first word of the prayer Jesus called the greatest commandment. In Hebrew, hearing and doing are one verb.

**Wednesday — סְלִיחָה · *selichah* · forgiveness.** A word the Bible uses only of God. What that means for the rest of us.

**Thursday — חֶסֶד · *chesed* · loyal love.** The word the Good Samaritan is made of. Translators have never found the English for it.

**Friday — חַיִּים · *chayim* · life.** Why the Hebrew word for life is plural, and why every Jewish prayer this week asks to be written in its book.

Each morning: the word, its root, one verse. Each evening: the secret inside it — the layer the rabbis called *sod* — and one small thing to do with it before bed.

Monday morning, 6:00. Say it once tonight so it's in your mouth: *teh-shoo-VAH.*

See you at sunrise.

— Rabbi Evan

### Post C — Monday morning · schedule **Monday, September 14, 6:00 am**
- Section: Morning
- Title: `☀️ תְּשׁוּבָה · teshuvah · return`
- Body (the first three lines — the Hebrew word, then the transliteration line — should be centered if the editor allows; otherwise leave left-aligned):

<div align="center">

# תְּשׁוּבָה

*teshuvah* (teh-shoo-VAH) — return

</div>

Say it once, out loud. *Teshuvah.* The stress lands on the last syllable, like a step landing on a doorstep.

Your Bible translates this word "repentance." Put that down for a minute.

*Teshuvah* grows from a three-letter root: *shuv.* To turn. To turn around. To come back. It's one of the most common verbs in the whole Hebrew Bible — it shows up over a thousand times — and almost every time it means something physical. A man turns back on the road. A river returns to its course. A wife comes home.

Repentance, in English, is a feeling. It comes from a Latin word for penalty. It happens inside you, and it hurts.

*Teshuvah* is not a feeling. It's a direction. You were walking one way. You turn around. You walk back.

Here's the verse. It's the one the prophet Hosea gives Israel at the very end of his book, after fourteen chapters of heartbreak:

> **"Return, Israel, to the LORD your God."** — Hosea 14:1 (NIV)
> *Shuvah Yisrael ad Adonai Elohecha.*

That first word — *shuvah* — is *teshuvah* in the imperative. Not *feel sorry, Israel.* Not *be ashamed, Israel.* Just: *turn around. Come home.*

Notice what the verse doesn't say. It doesn't say fix yourself first. It doesn't say become worthy. It says *return* — and the one you're returning to is already named as *your* God. The relationship isn't waiting on the other side of the turn. It's the reason you can turn.

That's the whole difference. Repentance asks: *how bad do I feel?* *Teshuvah* asks: *which way am I facing?*

*Repentance is a feeling. Return is a road.*

**Today's question:** Where, today, is something asking you to turn around? Not to feel worse about it. Just to face the other way.

Tonight: why the rabbis say the one who comes back stands in a place the one who never left can't reach.

— Rabbi Evan

### Post D — Monday evening · schedule **Monday, September 14, 7:00 pm**
- Section: Evening
- Title: `🌙 Laila Tov · teshuvah · where the one who came back stands`
- Body. **Important:** where the text says `[PAYWALL]`, do **not** insert Substack's paywall divider this week — delete that line entirely. (In week 3 the evening posts will carry a real paywall at that point; not now.)

This morning, *teshuvah.* Return. Not a feeling — a road.

*The one who comes back knows the road from both directions.*

`[PAYWALL]`

There's a line in the Talmud that has stopped people for fifteen hundred years. It's in tractate Berakhot, and a sage named Rabbi Abbahu says it almost in passing:

*"In the place where those who have returned stand, even the perfectly righteous cannot stand."*

Read it again. The person who never left is not in the highest place. The person who left and came back is.

The rabbis knew that sounded backwards. They let it stand anyway. Because they'd noticed something true: the one who walked away and turned around knows something the one who stayed cannot know. They know how far it is. They know what the turning costs. They know the road from both directions.

And the Midrash adds the part that makes it bearable. God says: *Open for me an opening the size of the eye of a needle, and I will open for you an opening wide enough for wagons.*

The turn can be tiny. The response is wagons.

You know the one. The relationship, the habit, the silence you've been walking away from long enough that the distance has started to feel like the truth about you. It isn't. It's a direction. And you are allowed to face the other way without having earned it first.

So, tonight, one sentence, out loud, alone is fine: *"I've been facing away from ______. I'm turning around."* No plan. No apology yet. Just the sentence. That's the needle's eye.

*You don't have to walk the whole road tonight. You only have to turn.*

*Laila tov* — good night. Tomorrow: *shema.*

— Rabbi Evan

---

**Audio (optional, ~1:30):** *Teshuvah. Teh-shoo-vah. Teshuvah.* [pause] The one who comes back knows the road from both directions. [pause] Tonight, one sentence: I've been facing away from — . I'm turning around. [pause] You don't have to walk the whole road tonight. You only have to turn. [pause] Laila tov.

Delete the "Audio (optional…)" block at the end of Post D — do not include it in the published post.

### Posts E onward
Tuesday through Sunday of week 1 will be supplied separately in the same format. Do not draft them yourself.

---

## PART 3 — Report back

When done, reply with this checklist, marking each item done / not done / done-with-difference (and what the difference was):

1. Name and tagline set
2. Logo and cover set (which file went where)
3. About page replaced
4. Sections Morning and Evening created, both opt-out-able, all subscribers included
5. Welcome email subject and body set; PDF link status
6. Payment plans $7 / $60 / $180 set, annual default, 7-day trial on, group discount status
7. Benefits text set
8. Comments: enabled, paid-only status
9. Reply forwarding on; from-name set
10. Recommendations on; referral program on with rewards
11. Post A scheduled (date/time, section, audience = Everyone)
12. Post B scheduled
13. Post L1 scheduled (Friday 6:00 am)
14. Post L2 scheduled (Friday 7:00 pm), `[PAYWALL]` line removed
15. Post C scheduled
16. Post D scheduled, `[PAYWALL]` line removed, audio block removed
17. Publication timezone confirmed as America/Chicago
18. Anything you could not find or had to approximate

Do not mark anything done that you did not verify on screen.
