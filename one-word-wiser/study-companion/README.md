# The Rabbi’s Notes

**Approved editorial model: the chapters of Lawrence Kushner and Kerry M. Olitzky’s *Sparks Beneath the Surface*. Evan confirmed September 15, 2026: “each chapter here should be a model for our study sheets.”**

The September 16 paid-sheet pilot is approved and configured. See the [verified delivery record](delivery-2026-09-16.md) and [pilot rationale](free-letter-pilot-2026-09-16.md). This document defines the reusable study format; no daily or weekly production cadence is promised.

## Editorial standard

**Start with a human question someone already cares about.** Evan’s September 15 correction rejected “forgiveness leading to reverence” as the organizing focus. The sheet should be human, real, simple to understand, and deep. A reader should understand the title before knowing any Hebrew or rabbinic terminology. Choose a recognizable hurt, desire, fear, relationship, or mystery; then find the textual difficulty and substantial commentaries that help the reader explore it.

Kushner and Olitzky’s titles show how this can work: “Two Kinds of Horror,” “What Are You Looking For?,” and “Sorrow Not Impurity.” Their appeal comes from a real interpretive question developed in the chapter. Write an equally clear, intriguing title whose promise the sheet fulfills. Do not imitate the titles mechanically, make every title a question, or add dramatic language to an abstract lesson. The familiar format can support a different human concern each time.

Evan corrected the earlier prototype: four miniature summaries were too shallow. The aim is a page readers can actually study. Use complete short commentaries or substantial, faithful excerpts that retain the teacher’s reasoning. Do not turn each source into a slogan or force all sources into equal word counts.

The reference is Lawrence Kushner and Kerry M. Olitzky’s *Sparks Beneath the Surface*. Its “How to Use This Book” describes a primary biblical text, a traditional teaching, explanation, context, and related tradition. The chapter “Teshuvah as Rewriting the Past” (printed pp. 55–56) informed the first revised sheet. Evan’s approval applies to the book’s chapters as the recurring model across the series, beyond this one example. Borrow the structure, depth, and way of guiding a reader through a teaching; write original explanations and verify the traditional sources independently. The user’s book PDF remains outside the repository.

## A chapter as the model for each sheet

Give each sheet the coherence of a short chapter: one recognizable human concern, one biblical passage, one substantial interpretive question, and a developed conversation around it. Begin the explanation with a concrete situation or a striking detail in the story. Let the sources complicate and deepen it; do not force agreement or use them only to endorse advice decided in advance. The central verse is the focus of the argument, not a decorative centerpiece. A reader should finish understanding both what a teacher says and how the teacher reaches that reading.

Use these recurring elements, letting the chosen text determine their emphasis:

- **The verse and its setting:** Hebrew, English, and just enough biblical context to understand what is at stake. Explain the word or grammatical detail that opens the reading.
- **The traditional teaching:** a real commentary with its reasoning intact. Select the strongest relevant voices rather than repeatedly filling the same four author slots. The current four-commentary layout remains available; the authors and interpretive approaches vary with the passage.
- **The explanation:** Evan’s accessible rabbinic guidance through the teaching. Define unfamiliar terms, show the interpretive steps, and explain meaningful differences among the sources. Keep newly drafted explanation distinct from source quotations.
- **The wider conversation:** a related teaching, story, historical detail, or practice that develops the central question. Include background when it helps readers understand the teacher, not to fill a recurring box.
- **The invitation to study:** a few questions that require returning to the text, followed by relevant further reading. Application should grow from the interpretation.

Before drafting a sheet, read a relevant chapter in full as a model and record its title and printed pages in the source notes. It may supply a teaching to investigate or demonstrate how to explain a difficult text. The sheet need not cover the same passage as its model chapter; make that relationship clear. Find and read the original traditional sources wherever possible. If a source is available only through the book, attribute it through the book rather than claiming independent verification. Do not claim to have read chapters that have not been inspected.

The supplied local reference is `/Users/evan/Downloads/kushner.pdf`; this is a machine-local location, not a shared repository dependency. Agents elsewhere should use an authorized available copy or request access when the relevant chapter is needed. Store bibliographic references and original working notes in Git, not the book PDF or page scans.

The quality check is simple: **Would someone recognize why this matters from the title? Does the sheet preserve a worthwhile teaching, make its reasoning understandable, and leave the reader with a deeper encounter with the biblical text?** A visually attractive page of short summaries does not meet this standard. Keep the experience elegant and spacious while giving the substance enough room. A compelling title is an editorial judgment, not evidence of paid conversions; learn from actual reader response after an authorized release.

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
- `selichah-2026-09-16.json`: current example, **Why Does It Still Hurt?**, centered on Joseph’s tears in Genesis 50:17 and the slow return of trust.
- `build.py`: entry point; selects the renderer from the JSON layout.
- `commentary_page.py`: current two-page renderer and overflow checks.
- `selichah-2026-09-16-sources.md`: source and interpretation review.
- `../../output/pdf/rabbis-notes-forgiveness-2026-09-16.pdf`: current two-page review PDF.
- `revisions/selichah-2026-09-16-short-readings.json`: preserved miniature-summary version, rejected as too shallow.
- `revisions/selichah-2026-09-16-linear.json`: earlier linear version.
- `revisions/selichah-2026-09-16-reverence.json` and `-reverence-sources.md`: preserved Psalm 130 version, rejected for its abstract organizing focus.
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

This template does not activate a new membership offer or cadence. The daily letter can deliver a complete teaching while the sheet offers close reading, several substantial Jewish voices, and questions for personal or group study. The September 16 free-letter/paid-sheet draft and automatic welcome delivery are configured and verified in the dated delivery record. The article remains unpublished. Future sheets need their own approved content and verified delivery placement.
