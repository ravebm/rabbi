# Already Home — daily meditation audio

The morning meditation on *Already Home* (alreadyhome.substack.com) ships with an audio version read in Evan's cloned voice. This is how the audio gets made, every day, without Evan touching ElevenLabs.

## The voice

| Voice | ElevenLabs id | Type | Status |
|---|---|---|---|
| **Evan Ram Dass** | `oObUJR88Eqgwj1R5iyF7` | Professional Voice Clone (PVC) | **Not usable until fine-tuning finishes.** Error until then: "Voice … is not fine-tuned and cannot be used." Check ElevenLabs → Voices → Evan Ram Dass: if it says *Verify*, Evan must record the verification phrase; then training runs for several hours. |
| **Evan (instant)** | *(create — see below)* | Instant Voice Clone (IVC) | Works within a minute of creation. Use this until the PVC is ready, then switch. |

**Rule:** the skill uses the PVC if it renders, otherwise the instant clone. Never a stock voice for a meditation.

**To create the instant clone (Evan, once, five minutes):** ElevenLabs → Voices → *Add a new voice* → *Instant Voice Clone* → upload one to three minutes of clean, unhurried speech (a previous recording of Evan reading a meditation is ideal; a phone voice memo in a quiet room is fine) → name it exactly `Evan (instant)` → save. Then tell Claude "the instant clone is up."

## The daily process (version 1 — running now)

1. **Evan finalizes the meditation text.** Either paste it to Claude with "make the audio," or save it as `already-home/audio/queue/YYYY-MM-DD.md` (the date it publishes) and commit.
2. **Claude runs `skills/meditation-audio`:** strips everything that isn't spoken, marks the breaths, renders one take in Evan's voice, listens to the result's status, and delivers the MP3 (in chat, and saved as `already-home/audio/out/YYYY-MM-DD.mp3` when the file can be pulled into the repo; otherwise the ElevenLabs flow link, where *Download* is one click).
3. **Evan adds it to the post.** In the Substack editor: click **+** → **Audio** → upload the MP3. Place it directly under the header image, above the first line. Substack also lets you set the post's audio as a podcast episode; leave that off unless the podcast feed is turned on.

Time cost: one minute of Evan's attention, about a cent of ElevenLabs credit per hundred words.

## Version 2 — automatic (next, once v1 has run cleanly for a week)

- A scheduled routine runs every evening at 8 pm Central: pulls the repo, finds tomorrow's file in `queue/`, renders the audio, saves the MP3 to `out/` and to a Google Drive folder *Already Home Audio*, and sends Evan a push notification with the file.
- Hermes (or another operator agent) attaches the MP3 to the already-scheduled Substack post. Substack has no API, so this last step is an agent driving the editor, or Evan's one click.

Don't build v2 until v1 has produced five good files in a row; the failure modes (voice not ready, a paywall marker read aloud, a name mispronounced) all show up in v1 first.

## What the text needs to look like before it's spoken

The skill does this automatically; listed here so Evan knows what changes.

- Removed: title, subtitle, headers, `[DIVIDER]`, `[PAYWALL]`, image prompts, Notes candidates, attribution/Location citations, the italic share line, anything in brackets.
- A paragraph break becomes a breath: an ellipsis (…) at the end of the paragraph.
- `[DIVIDER]` becomes a longer breath: a line with two ellipses.
- Quotations: "Ram Dass wrote:" then the quote, then a beat.
- Names and Sanskrit/Hindi words spelled phonetically the first time they appear (Maharaj-ji → "Ma-ha-RAJ-jee"), once.
- Numbers, years, and citations spelled out or removed. No book "Location" numbers ever spoken.
- One bolded line in the paid section: keep the words, drop the bold — emphasis comes from a beat before it, not from the markup.

## Log

| Date | Voice | Model | Length | Credits | Notes |
|---|---|---|---|---|---|
| 2026-09-08 | Evan Ram Dass (PVC) | multilingual_v2 | — | ~57 (test line) | Failed: "not fine-tuned and cannot be used." PVC still training/unverified. |
