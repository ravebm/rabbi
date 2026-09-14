---
name: one-word-wiser
description: Draft, revise, or format Rabbi Evan Moffic's One Word Wiser Substack posts, including weekday Hebrew words, Shabbat posts, Sunday Your Verse posts, and a full week. Preserve his edits and prepare readable Substack copy with short paragraphs, subheadings, and restrained dividers. Not for Already Home or pulpit sermons.
---

# One Word Wiser — post production

Read the repository’s `AGENTS.md`, then `one-word-wiser/01-positioning.md`, `02-daily-format.md`, `03-monetization.md`, and [the readability standard](references/substack-readability.md). The dated samples show Evan’s voice; newer edits and current user instructions take precedence.

## Before drafting

1. Read the weekday and Shabbat samples. Match the short paragraphs, direct address, and one central idea, without copying an old heading or formula.
2. Consult `one-word-wiser/word-bank.md` for the week’s words and source leads. The bank is a proposal, not source verification. Check the ledger for repetition. A new word needs useful Hebrew, a teachable passage, and a grounded reading; a hidden meaning is not required.
3. Verify each source in its actual context. Check book/chapter/verse, tractate/page, and relevant commentary. Note Hebrew/English numbering differences. Distinguish the literal meaning, the verse’s form, and a later rabbinic interpretation. Attribute disagreement to the actual speakers.
4. Use NIV for Bible quotations, within applicable quotation limits. Identify the Hebrew under the English accurately. Never claim a Hebrew noun appears in a verse that uses a related verb. Never describe the whole Bible as originally written in Hebrew.
5. Check niqqud, roots, transliteration, and pronunciation. Use ch for chet and tz for tzadi, with CAPS for stress in pronunciation guides. Explain unfamiliar sources in a few plain words.

## Output contract

Return Substack-ready Markdown with this header, a `---` separator, and the body:

```
# [Date] — [word]
**Subject:** [clear, approved human title or a word title]
**Subtitle:** [only when specified]
**Audience:** [current authorized audience]
**Paywall:** [none during launch; otherwise the approved boundary]
**Status:** draft; delivery requires current authorization
**Cards:** [only the cards actually used, or none]
**Dividers:** [restrained native text/rule, with placement]
**Notes:** [optional proposed Notes; not authorization to post]
```

## The familiar experience

Follow **word → meaning → reflection**, normally about 400–600 words, shorter when complete. Hebrew, transliteration, and a gloss are clear near the top. Use the familiar In English / In Hebrew opening when it helps; never force a dramatic correction or misrepresent translation to create a hook.

Teach one passage clearly. Give free readers a complete useful reading and some of Evan’s rabbinic voice. Then let the same word lead naturally into a fuller reflection on a real human need. One main source or story usually suffices. Application can be a short paragraph, a question, or a quiet ending; do not force it into one sentence.

The current paid benefit is the full weekday reflection. All launch letters are free through September 27, 2026. Saturday and Sunday remain free in full. Follow the current task for any later paywall or delivery decision. The study companion is a proposal under review, not an automatic addition or a promised benefit.

No “secret” product label, compulsory mystical interpretation, or “Let It Change Your Life” heading. Use short content-specific subheadings and restrained dividers. The conclusion should vary with the teaching. A hidden meaning, a puzzle, and a rhetorical question are optional, not production requirements.

## Saturday and Sunday

Saturday uses the week’s Torah reading, checked against the applicable calendar. Avoid a universal claim about every synagogue. A brief recap may gather the week when useful. The full letter is free.

Sunday uses a reader’s verse, or Evan’s clearly identified choice until requests arrive. Do not invent a reader. Obtain permission before naming a correspondent or location; an emailed question alone does not authorize disclosure. The whole letter is free and may close with an invitation to send a verse.

For “write the week,” draft all seven letters and vary questions, sources, emotional movement, and endings. Use the bank’s week as a starting point. Update the ledger for approved planned dates; distinguish drafts from published posts.

## Voice and visual restraint

- Warm, plain, and specific. One to three sentences per paragraph. Explain an unfamiliar Jewish name once.
- No melodrama, generic spiritual slogans, forced etymology, or identical moral attached to every word.
- Show the Hebrew’s beauty in the word itself. Decorative illustrations are not the default. Use a native rule or small centered Hebrew letter for a divider when it helps.
- Preserve cards in the current approved copy. Render only required cards with `one-word-wiser/brand/cards/render.py`; never add a line-day card when the line was cut. Inspect Hebrew and clipping.
- Keep the English/Hebrew and Jewish/Christian distinctions accurate and respectful. Do not treat either tradition as having one interpretation of every passage. A Gospel connection must be sourced and earned, generally once or twice a week at most.
- Banned editorial habits: sales urgency, “unlock,” “exclusive,” “don’t miss,” “let’s dive in,” “journey,” “tapestry,” and repeated aphoristic restatements.
- Sign “— Rabbi Evan” unless preserving a newer user-edited source.

## Before handing over

Check source fidelity, Hebrew, the complete free teaching, the payoff to the title, and the phone layout. Keep source notes and uncertainties below the body for Evan, separate from the post. Preserve materially different user revisions. During upload, do not regenerate or improve approved copy. Save as a draft unless delivery is explicitly authorized. Commit and push the finished sources and instructions in this repository.
