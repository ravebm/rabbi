# Post cards — the visual template

Substack can't carry custom fonts or colors inside a post, so the design lives in two image cards placed between Substack's native text. Everything else is Substack's own serif, a divider, and a blockquote for the verse.

| Card | Where it goes | Size | Variants |
|---|---|---|---|
| **Word card** | The first image in every post — Hebrew word large, transliteration, gloss, date | 1200 × 675 | Day (morning) · Night (evening) |
| **Line card** | Near the end — the day's one line (*to carry* / *to sleep on*) | 1200 × 420 | Day · Night |

**Live template (edit and export PNGs):** https://claude.ai/code/artifact/5bd876b1-3c39-4e8a-a135-6579f2d67c96

**Palette:** navy `#1B2A41` · off-white `#F6F3EC` · cream `#F1EDE3` · gold `#A8781C` (day) / `#C9A24A` (night).
**Type:** Frank Ruehl Libre (Hebrew) · EB Garamond (everything else on the cards).

The `.dc.html` files here are the sources the template is built from. Daily production: open the template, retype the Hebrew, transliteration, gloss, date, and line on the two cards for the day; export each as PNG; drop the Word card as the post's first image and the Line card where the italic line sits.
