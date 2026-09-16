# The Rabbi’s Notes — a proposal

**Status: local prototype for Evan’s review, September 14, 2026. Not an advertised paid benefit.**

One weekly page a reader can use alone or bring to Bible study. It draws from a passage already being taught in the daily letters, so there is no second content calendar.

## The reader’s experience

One passage, the Hebrew that matters, two brief rabbinic observations, two questions, and one further-reading link. Plain language and a quiet page. The content can vary while the experience stays recognizable. No worksheets with tasks to complete, multi-part kits, or claims of guaranteed personal transformation.

## Further reading

Evan’s September 14 direction: each Rabbi’s Notes page includes one relevant piece of writing by Rabbi Evan Moffic or Rabbi Jonathan Sacks. Place it under **Further reading**, after the closing thought and above the source references. Give the author, a linked title, and one short sentence explaining how it deepens this teaching.

Choose the strongest fit. Look for an existing piece by Evan first when it develops the subject; use Sacks when his piece offers the more useful continuation. Prefer a freely readable essay, published post, or excerpt with a direct link. Read the actual piece and verify the title, author, destination, and relevance. Label a purchase or subscription requirement if that is the only suitable resource. Never link an unpublished draft as though readers can access it. If no suitable piece is verified, flag the missing resource for Evan before handoff instead of inventing a link or filling the slot with an unrelated recommendation.

Keep this to one resource, separate from the primary-source citations. It is an optional next read for the reader, not another assignment or a standing sales pitch. Store its title, author, URL, and explanation in the `further_reading` object in the source JSON, with the verification date. The builder requires this object and places it consistently on the page.

Working public description, only if Evan adopts it: **A weekly Bible study prepared by a rabbi, ready to read or discuss.** “The Rabbi’s Notes” is a working name, not an approved brand change.

## What takes training

- Choosing sources that illuminate the passage and the reader’s question.
- Distinguishing lexical meaning, biblical context, and later rabbinic interpretation.
- Explaining real differences among Jewish teachers without making Judaism monolithic.
- Connecting the passage to ordinary life in Evan’s voice, without overstating the text or requiring a Christian reader to abandon their own faith.

## What can be automated

From a selected word and an approved teaching, tools can prepare source candidates, references, pronunciation, a first draft of the notes and questions, and the page layout. The included builder turns structured copy into a consistent one-page PDF and rejects content that overflows.

Evan approves the sources and final interpretation. Automated retrieval is not source verification by itself; a source has to be read in context. The prototype does not claim Evan has already reviewed it.

## Pilot to consider

Try one companion a week for four weeks, using an existing weekday letter. The first could be a free example, with later access determined by Evan’s final paid offer. Keep the current daily free teaching and paid reflection intact while testing. Do not promise daily sheets, personal replies, live sessions, or new subscription tiers.

Ask what readers actually did with the page: read it alone, discuss it, bring it to a group. Compare attributed paid starts and later retention. Downloads and complimentary replies alone do not establish willingness to pay. No pilot emails, attachments, pricing changes, or recurring jobs have been launched by this task.

## Files and building

- `sample-return.json`: editable prototype text and source links.
- `build.py`: local PDF builder; no network, upload, or scheduling behavior.
- `../../output/pdf/rabbis-notes-return-prototype.pdf`: one-page output.

Run from the repository root:

```sh
python3 one-word-wiser/study-companion/build.py
```

Dependencies: ReportLab with `uharfbuzz` for the Hebrew vowel marks. Uses the existing Garamond and Frank Ruhl Libre fonts in `brand/fonts/`. The builder accepts `--source` and `--output` paths. Render and visually check a new PDF after edits; confirm the source links and one-page count.

## Source notes

The sample uses Hosea 14:1 NIV (Hebrew 14:2), Berakhot 34b:22–23, and Maimonides’ Mishneh Torah, Repentance 2:9. The rabbinic material is paraphrased. Rabbi Abbahu’s statement is presented as one side of a Talmudic disagreement. The Hosea verb is distinguished from the later noun teshuvah; “coming home” is identified as interpretation. Maimonides’ text was checked in the bilingual Moznaim/Chayenu excerpt hosted by TheYeshiva.net, page 6. The source links are embedded in the PDF.

Further reading: Rabbi Jonathan Sacks, [Transforming the Story](https://rabbisacks.org/covenant-conversation/vayechi/transforming-the-story/). The full essay on the official Rabbi Sacks Legacy site was read and its access checked September 14, 2026. It discusses Joseph, his brothers, and repentance as a change in the meaning of the past through changed choices. The PDF’s brief description is a paraphrase, not a quotation.

## September 16 review candidate

Evan’s September 15 suggestion led to a [free-letter pilot proposal](free-letter-pilot-2026-09-16.md), with a completed selichah letter and one-page **Forgiveness and Repair** sheet. It is not yet an adopted paid benefit or a configured welcome-email offer.
