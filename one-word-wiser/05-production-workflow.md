# 05 · Production Workflow — seven posts a week without it eating Evan's life

One post a day is the routine Evan already keeps for Already Home. Both publications get edited in the same morning sitting. Only the voice needs Evan; the structure is produced.

## Division of labor

| Who | Does |
|---|---|
| **Evan** | Confirms the week's six words · reads and edits every draft (15–30 min/day) · picks the Shabbat word from his sermon · records or approves audio · answers verse replies · hosts *Ask the Rabbi* · writes the Sunday *Your Verse* post himself when a reply moves him (otherwise the skill drafts it) |
| **Claude (skill)** | Drafts every post from the word bank in the format and voice · subject lines, the line to carry, the line to sleep on, the two Notes · the Shabbat footer from the week's posts · scripts the optional audio · renders the cards · keeps the ledger |
| **Codex / Hermes** | Uploads approved drafts to Substack as drafts with their cards (`handoff-prompts.md`) · runs the setup brief |
| **Tools** | Phone voice memos (optional audio) · Substack scheduler |

## The weekly rhythm

**Sunday (the one real session, and most of it is automatic):**
1. At 4:00 pm Central a scheduled session drafts the coming week from `word-bank.md` with the skill ("write the week"): seven posts, Monday through Sunday, in Substack-ready Markdown with subject lines and Notes; cards rendered; ledger updated; pushed to a `posts/week-NN` branch as a draft pull request. It puts the whole week in one Google Doc shared to Evan and reports the links.
2. Evan edits the Doc in his own words, Monday most carefully. Anything: cut, rewrite, swap a verse. Swap a word by editing `word-bank.md` any time before Sunday; the bank is a plan, not a contract, and a word runs once a year (the ledger).
3. Evan opens that session and says **approved**, or says what to change. It reads the Doc back, applies every edit to the files, fixes anything that broke the format or the voice and says what it fixed, re-renders any card whose line changed, marks the pull request ready, and hands back the Codex upload prompt filled in.
4. Evan pastes that prompt into Codex; Codex schedules the seven posts for 6:00 am Central with their cards. That paste is the one step no agent here can do: Substack has no API.

**Daily, 10–15 minutes:**
- Glance at yesterday's numbers; reply to two or three reader replies (replies are the relationship, and they're future Sunday posts).
- The post is already scheduled. Nothing else.

**Thursday, 15 minutes (optional):** record the week's audio memos in one sitting: the word three times, the line to carry, the one thing, the line to sleep on. Upload to the posts.

**Friday, 10 minutes:** the Shabbat word. Tell Claude which word the sermon is on if it differs from the bank; the skill drafts the Shabbat post from it and the week's lines.

Total: an hour or two a week of Evan's time for seven posts, almost all of it the edit pass. The pulpit voice comes from the edit pass, not the draft.

## The skill

`skills/one-word-wiser/SKILL.md`, invoked by "write Tuesday's post for *chesed*," "write the week," "draft Saturday from the portion," "draft Sunday's verse post for Psalm 23." It knows the anatomy in `02`, the voice rules in `01`, the gate in `03`, and it reads `word-bank.md` for the week's words, verses, secrets, and the five tests for any new word. See the skill file for the exact output contract.

## Audio

Two paths; **DECIDE**:

- **Phone recording (recommended to start).** Voice memo, 2–3 minutes, no editing. The rawness is the point: it's a rabbi, not a podcast. Upload as the post's audio in Substack.
- **ElevenLabs clone.** The connector is available in this environment. Clone Evan's voice once from 10 minutes of clean speech; the skill's audio script is fed to `creative_generate_speech`; the render goes into the post. Hebrew pronunciation from a clone must be checked by ear for the first few weeks; the model will get *chet* and *ayin* wrong until it doesn't. Use the phone for the Hebrew word and the clone for the English, if the difference is audible.

## Images

Three cards per post: Word (day) at the top, Line (day) at the line to carry, Line (night) at the line to sleep on, rendered by `brand/cards/render.py` from the template sources in `brand/cards/`. See `brand/cards/README.md`. Nothing else. Substack's default post image is the publication logo. The one exception is the *Seven Words* PDF (set in the logo's navy and serif). `fal_connect.py` stays for the occasional editorial image if Evan wants one.

## Verse queue

Keep `verse-queue.md` (create on first reply) with: date received, first name + state, verse, one-line note on what they asked. Sunday picks from the top. Reply to every sender within a week even if their verse won't run for a month ("yours is in the queue for October 18"). Until the queue has a verse, Evan picks one, the verse Christians ask a rabbi about most, and the post says so in a line.

## Metrics that matter (check Sundays)

From the Substack dashboard (the MCP connector can pull these once it's pointed at rabbi.substack.com; today it's pointed at Already Home):

1. **Open rate, 7-day average.** The health of the habit. Target > 40%.
2. **Free growth net of unsubs.** Target +1% / week from organic; ad cohort on top.
3. **Paid conversions / week** and **which posts converted them.** After a month you'll know which *kind* of secret converts (at Already Home: the ones that answer a burning, timestamped ache, not soothing ones). Do more of those.
4. **Reply count.** Replies → Sunday posts → replies. This is the flywheel HfC built with "The Verses You Asked For."
5. **Ad CPA and 60-day paid conversion of the ad cohort.** The two numbers that decide spend.

Keep a one-line-per-week ledger at the bottom of this file:

## Ledger

| Week of | Free | Paid | ARR | Open rate | Read-to-end | Paid/wk | Notes |
|---|---|---|---|---|---|---|---|
| 2026-09-07 | | | | | | | Week 0 — launch Saturday Sep 12, two posts; one a day from Sunday |
