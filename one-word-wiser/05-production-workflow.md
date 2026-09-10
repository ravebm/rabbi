# 05 · Production Workflow — how we manage 12 posts a week

Twelve posts a week is the one thing that makes people stop. It doesn't have to. Most of it is structure, and structure can be produced; only the voice needs Evan.

## Division of labor

| Who | Does |
|---|---|
| **Evan** | Picks/edits the week's five words · reads and edits every draft (20–40 min/day) · records or approves audio · answers verse replies · hosts *Ask the Rabbi* · writes the Sunday *Your Verse* post when a reply moves him (otherwise the skill drafts it) |
| **Claude (skill)** | Drafts every post from the word bank in the format and voice · subject lines, the lines to carry and to sleep on, Notes · drafts the Saturday recap and Sunday preview from the week's posts · scripts the optional audio |
| **Tools** | Phone voice memos (optional audio) · Substack scheduler |

## The weekly rhythm

**Sunday, 60–90 minutes (the one real session):**
1. Open `word-bank.md`, confirm the week's five words. Swap any that don't feel right — the bank is a plan, not a contract.
2. Run the skill: *"Write the week: Monday teshuvah, Tuesday shema, …"* It returns ten posts (5 morning, 5 evening) in Substack-ready Markdown, plus subject lines, Notes, and optional audio scripts.
3. Read Monday's pair carefully and mark up in the voice you want. Feed the edits back: *"Tighten all the evenings the way I did Monday."* Regenerate.
4. Claude renders the week's cards (`brand/cards/render.py`, four PNGs per day) and sends them.
5. Paste into Substack, drop the Word card as the first image and the Line card in place of the italic line, drop the paywall marker, schedule all ten. 6:00 am and 7:00 pm CT.

**Daily, 10–20 minutes:**
- Morning: glance at yesterday's numbers; reply to two or three reader replies (replies are the relationship — and they're future Sunday posts).
- Evening: nothing. It's scheduled.

**Thursday, 15 minutes (optional):** record the week's five audio memos in one sitting — the word three times, the line to sleep on. Upload to the evening posts.

**Saturday, 15 minutes:** skill drafts Havdalah from the week's five morning posts; Evan edits; schedule for 7 pm.

**Sunday, 30 minutes:** pick a verse from the queue, skill drafts *Your Verse*; edit; schedule 6 am. Skill drafts *Week Ahead*; schedule 7 pm.

Total: ~4 hours a week of Evan's time for 12 posts. The pulpit voice comes from the edit pass, not the draft.

## The skill

`skills/one-word-wiser/SKILL.md` — invoked by "write Tuesday's posts for *chesed*," "write the week," "draft Saturday's recap," "draft Sunday's verse post for Psalm 23." It knows the anatomy in `02`, the voice rules in `01`, the paywall placement in `03`, and it reads `word-bank.md` for the verse and Gospel pairings. See the skill file for the exact output contract.

## Audio

Two paths; **DECIDE**:

- **Phone recording (recommended to start).** Voice memo, 2–3 minutes, no editing. The rawness is the point — it's a rabbi at bedtime, not a podcast. Upload as the post's audio in Substack.
- **ElevenLabs clone.** The connector is available in this environment. Clone Evan's voice once from 10 minutes of clean speech; the skill's audio script is fed to `creative_generate_speech`; the render goes into the post. Hebrew pronunciation from a clone must be checked by ear for the first few weeks — the model will get *chet* and *ayin* wrong until it doesn't. Use the phone for the Hebrew word and the clone for the English, if the difference is audible.

## Images

Four cards per weekday — Word and Line, day and night — rendered by `brand/cards/render.py` from the template sources in `brand/cards/`. See `brand/cards/README.md`. Nothing else. Substack's default post image is the publication logo. The one exception is the *Seven Words* PDF (set in the logo's navy and serif). `fal_connect.py` stays for the occasional editorial image if Evan wants one.

## Verse queue

Keep `verse-queue.md` (create on first reply) with: date received, first name + state, verse, one-line note on what they asked. Sunday picks from the top. Reply to every sender within a week even if their verse won't run for a month — "yours is in the queue for October 18."

## Metrics that matter (check Sundays)

From the Substack dashboard (the MCP connector can pull these once it's pointed at rabbi.substack.com):

1. **Morning open rate, 7-day average.** The health of the habit. Target > 40%.
2. **Free growth net of unsubs.** Target +1% / week from organic; ad cohort on top.
3. **Paid conversions / week** and **which evening posts converted them.** After a month you'll know which *kind* of practice converts (at Already Home: the ones that answer a burning, timestamped ache, not soothing ones). Do more of those.
4. **Reply count.** Replies → Sunday posts → replies. This is the flywheel HfC built with "The Verses You Asked For."
5. **Ad CPA and 60-day paid conversion of the ad cohort.** The two numbers that decide spend.

Keep a one-line-per-week ledger at the bottom of this file:

## Ledger

| Week of | Free | Paid | ARR | Morning open | Evening open | Paid/wk | Notes |
|---|---|---|---|---|---|---|---|
| 2026-09-07 | | | | | | | Week 0 — announcement |
