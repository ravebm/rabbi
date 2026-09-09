---
name: meditation-audio
description: Turn a finished Already Home (Ram Dass) meditation into an MP3 read in Evan's cloned ElevenLabs voice. Use whenever Evan says "make the audio," "record this," "voice for tomorrow," pastes a final meditation and asks for the file, or when a routine finds a file in already-home/audio/queue/. Not for writing the meditation (that's ram-dass-meditation) and not for One Word Wiser.
---

# Meditation audio

Read `already-home/audio/README.md` first — it holds the voice ids, the current voice status, and the delivery steps.

## Steps

1. **Get the text.** From Evan's message, or from `already-home/audio/queue/YYYY-MM-DD.md` (tomorrow's date unless told otherwise). Pull the repo first.
2. **Prepare it for speech.** Produce a spoken-only version:
   - Drop title, subtitle, headers, `[DIVIDER]`, `[PAYWALL]`, image prompts, Notes, attribution, Location citations, share lines, anything in brackets, markdown markers (`*`, `**`, `>`, `#`).
   - End each paragraph with an ellipsis (…). Where `[DIVIDER]` stood, insert a line containing only "……".
   - Before a quotation: "Ram Dass wrote:" (or the actual speaker), a comma, the quote, then "…".
   - Spell tricky names phonetically the first time (Maharaj-ji → Ma-ha-RAJ-jee; Neem Karoli Baba → Neem Ka-RO-lee BA-ba). Once.
   - Spell out numbers. Remove any "Location 1234" citation.
   - Keep contractions and Evan's sentence rhythm exactly; do not "improve" the prose.
   - Show Evan the prepared text only if asked; otherwise just render.
3. **Pick the voice.** Call `creative_list_voices` (search "Evan"). Use **Evan Ram Dass** (`oObUJR88Eqgwj1R5iyF7`) if the README says the PVC is ready; otherwise **Evan (instant)**. Never a stock voice. If neither Evan voice exists or both fail with "not fine-tuned," stop and tell Evan exactly that — do not substitute.
4. **Estimate, then render once.** `creative_generate_speech` with `estimate_only: true` first (surfaces blocking errors free), then the real call with `generations_count: 1`, `model_id: eleven_multilingual_v2`. One take. Never call generate twice for the same text without Evan asking — each call is charged.
5. **Poll** `creative_get_flow_run_status` until `all_completed` or `has_failures`. On failure, report the exact `error_message` and stop.
6. **Deliver.** Send Evan the MP3 (`SendUserFile`) if it can be fetched into the workspace, saving a copy as `already-home/audio/out/YYYY-MM-DD.mp3` and committing it. If the file can't be fetched, send the flow URL and say "Download is the button at the top right." Either way, one line: "Add it in Substack: + → Audio → upload, directly under the header image."
7. **Log.** Append a row to the table at the bottom of `already-home/audio/README.md`: date, voice used, model, duration, credits, anything odd. Commit and push.

## Voice model notes
- `eleven_multilingual_v2` is the default: steadiest for slow narration in a cloned voice.
- Pacing comes from punctuation: commas and periods for natural pauses, ellipses for breaths, em-dashes for short beats. Don't write "[pause]" — v2 will read it aloud.
- Use `eleven_v3` only if Evan asks for inline direction tags (`[whispering]`, `[softly]`); check the result by ear the first time.

## Never
- Never render with a voice that isn't Evan's.
- Never speak a paywall marker, a citation, or an image prompt.
- Never edit the meditation's words beyond the spoken-prep rules above.
