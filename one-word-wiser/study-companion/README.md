# The Rabbi’s Notes

**Current format: a verse surrounded by real commentary, with explanation and discussion on the reverse. Updated September 15, 2026 after Evan supplied the Kushner book.**

The paid subscriber offer remains a proposal. The [free-letter pilot](free-letter-pilot-2026-09-16.md) describes proposed placement and delivery; this document defines the reusable study format.

## Editorial standard

Evan corrected the earlier prototype: four miniature summaries were too shallow. The aim is a page readers can actually study. Use complete short commentaries or substantial, faithful excerpts that retain the teacher’s reasoning. Do not turn each source into a slogan or force all sources into equal word counts.

The reference is Lawrence Kushner and Kerry M. Olitzky’s *Sparks Beneath the Surface*. Its “How to Use This Book” describes a primary biblical text, a traditional teaching, explanation, context, and related tradition. The chapter “Teshuvah as Rewriting the Past” (printed pp. 55–56) is a useful example of depth across two pages. Borrow this structural principle, not the authors’ prose or page images. The user’s book PDF remains outside the repository.

## A simple, substantial template

One double-sided Letter sheet, two PDF pages:

**Front: the text and its commentators.** Put one verse in Hebrew and English in the center, with four actual commentaries around it: two on each side. Name each commentator, preserve the argument, and link to the exact source. Short editorial headings help readers navigate. Commentaries may differ in length. A clear question draws attention to the interpretive difficulty in the verse. The Hebrew word, pronunciation, and meaning remain prominent at the top.

**Back: understanding the conversation.** Explain what the commentators notice and how their readings relate. Do not manufacture disagreement where two readings overlap. Add one relevant traditional teaching with its own excerpt, source, and explanation when it adds depth. Finish with two or three useful questions and one or two further readings.

Keep generous margins, clear gaps, navy text on white, serif body type, and light rules. The main verse is visibly larger than the commentary. No illustrations or decorative panels. The current format is designed for print; narrow commentary columns need zooming on a phone. Do not describe it as a verified Substack mobile layout.

Depth and white space matter together. The rejected 35-word maximum is retired. Preserve enough source text to make the argument intelligible. If a source does not fit, select a coherent passage, mark omissions, or adapt the layout deliberately. Never make the body type smaller to squeeze it in, and never simplify away the substance.

## Source discipline

Read each original source in context. Distinguish three kinds of writing visibly:

1. **Source excerpt:** a quotation from a named translation or a clearly labeled working translation from the original. Mark omitted material with ellipses; never put a paraphrase in quotation marks.
2. **Explanation:** newly drafted prose that guides the reader through the argument. It is not another quotation from the commentator or a claim that Evan has previously published it.
3. **Application:** a present-day interpretation, with care about what the source does and does not establish.

Do not treat a commentator’s theological interpretation as a dictionary definition. Verify every location and link. Preserve textual differences where they matter. Label a working translation as such and leave the review status until Evan approves it.

Each sheet includes a relevant resource by Evan or Jonathan Sacks. Prefer a free essay or excerpt, verify its content, and label a book or paid resource accurately. A second reading can be another source or a book chapter. Do not link unpublished drafts as reader resources. Store verification dates and selection notes in the JSON and a separate source-review file.

## Files

- `template.json`: blank reusable structure; incomplete fields deliberately prevent a build.
- `selichah-2026-09-16.json`: current example, **Forgiveness**, centered on Psalm 130:4.
- `build.py`: entry point; selects the renderer from the JSON layout.
- `commentary_page.py`: current two-page renderer and overflow checks.
- `selichah-2026-09-16-sources.md`: source and interpretation review.
- `../../output/pdf/rabbis-notes-forgiveness-2026-09-16.pdf`: current two-page review PDF.
- `revisions/selichah-2026-09-16-short-readings.json`: preserved miniature-summary version, rejected as too shallow.
- `revisions/selichah-2026-09-16-linear.json`: earlier linear version.
- `verse_page.py` and `sample-return.json`: legacy layouts retained for rebuilding earlier versions; they do not define the current editorial standard.

## Build and review

From the repository root:

```sh
python3 one-word-wiser/study-companion/build.py \
  --source one-word-wiser/study-companion/selichah-2026-09-16.json \
  --output output/pdf/rabbis-notes-forgiveness-2026-09-16.pdf
```

Dependencies: ReportLab and `uharfbuzz`; existing Garamond and Frank Ruhl Libre fonts in `one-word-wiser/brand/fonts/`. The renderer performs no upload, email, or scheduling action.

For another word, fill the blank template with verified content and pass its source and output paths explicitly. The builder checks required sources, four distinct reading positions, resource links, a verified reading by Evan or Sacks, and text fit. It cannot judge the truth of an interpretation or the accuracy of a translation.

Render and visually inspect **both** pages after the final edit. Check Hebrew and vowel marks, all source excerpts, explanation, links, spacing, page numbers, and footer. Confirm two pages and no clipped text. Keep the review label until Evan approves the artifact for readers. A saved PDF does not establish a saved Substack attachment or working paid access.

## Publication scope

This template does not activate a new membership offer or cadence. The daily letter can deliver a complete teaching while the sheet offers close reading, several substantial Jewish voices, and questions for personal or group study. The proposed free-letter/paid-sheet arrangement still needs Evan’s publication decision and a separately verified delivery setup.
