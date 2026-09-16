# The Rabbi’s Notes

**Current layout: one verse with four surrounding readings. Updated September 15, 2026 at Evan’s request.**

The paid subscriber offer remains a proposal. The [free-letter pilot](free-letter-pilot-2026-09-16.md) describes placement and delivery; this document defines the reusable page.

## The simple template

A single portrait page inspired by a Talmud page: the primary text is central and commentary surrounds it. Use four readings total, two on the left and two on the right. This is a contemporary study-page design, not a reproduction of a Talmud folio.

- Small series name and a clear title at the top; Hebrew word, pronunciation, and meaning beside it.
- One verse in the middle, in Hebrew and English, with its reference. The main text is visibly larger than the commentary.
- Four short, attributed interpretations around that same verse. Aim for 20–30 words each; 35 is the maximum. Explain a real difference in emphasis without manufacturing disagreement. Do not fill space with four versions of the same observation.
- Two or three short questions below the readings.
- One or two further-reading links at the bottom, including a verified piece by Rabbi Evan Moffic or Rabbi Jonathan Sacks.

Keep generous margins and gaps between readings. Use navy text on white, serif body type, and light rules. No illustrations, colored panels, dense paragraphs, or supplementary essay on the page. Shorten the copy when it does not fit; never shrink the type to force it in. Source notes for Evan belong in a separate file.

## Sources and further reading

Read each actual source in context. Name the author, link directly to the relevant passage, and make clear when the wording is a paraphrase. Distinguish a commentator’s interpretation from a lexical definition. If a contemporary reflection is included, label it as such; do not attribute it to an ancient source.

Each page includes one relevant piece of writing by Evan or Jonathan Sacks. Prefer a freely readable essay or excerpt. Verify title, author, destination, and relevance; label any purchase/subscription requirement. Do not link an unpublished draft as a reader resource.

Store `author`, `title`, `url`, `note`, and `verified_on` in the `further_reading` list. The compact page prints the author and linked title; the note records the reason for choosing it in the editable source. A second optional link can point to the full biblical passage or another useful reading.

## Files

- `template.json`: blank reusable content structure. Its empty fields deliberately prevent building until a writer supplies verified content.
- `selichah-2026-09-16.json`: filled working example, **Forgiveness**, centered on Psalm 130:4.
- `build.py`: entry point; chooses the layout from the source JSON.
- `verse_page.py`: renderer and fit checks for this format.
- `selichah-2026-09-16-sources.md`: interpretation and source review for the example.
- `../../output/pdf/rabbis-notes-forgiveness-2026-09-16.pdf`: current one-page review PDF.
- `revisions/selichah-2026-09-16-linear.json`: preserved earlier text and layout source.
- `sample-return.json`: the original linear prototype. Still builds when explicitly selected; it is not the current layout template.

## Build and review

From the repository root:

```sh
python3 one-word-wiser/study-companion/build.py \
  --source one-word-wiser/study-companion/selichah-2026-09-16.json \
  --output output/pdf/rabbis-notes-forgiveness-2026-09-16.pdf
```

Dependencies: ReportLab and `uharfbuzz`. Fonts: existing Garamond and Frank Ruhl Libre files in `one-word-wiser/brand/fonts/`. The renderer performs no network, upload, or scheduling action.

For another word, copy the blank JSON, fill its verse/readings/questions/resources, and pass its paths explicitly. The builder checks four unique reading positions, short commentary, direct links, a verified further reading by Evan or Sacks, and text fit. It cannot verify the truth of an interpretation: that requires reading the sources.

After building, render the PDF to an image and inspect the Hebrew, vowel marks, all four commentaries, links, spacing, and footer. Confirm one page. Keep the review status until Evan approves the artifact for readers. A saved PDF is not proof of a saved Substack attachment or paid access.

## Editorial purpose

The daily letter can offer a complete teaching. This page gives interested readers a small, usable conversation around a biblical text. The paid invitation and its cadence remain subject to the current publication decision; the layout itself makes no new subscriber promise.
