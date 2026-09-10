# Post cards — the visual template

Substack can't carry custom fonts or colors inside a post, so the design lives in two image cards placed between Substack's native text. Everything else is Substack's own serif, a divider, and a blockquote for the verse.

| Card | Where it goes | Size | Variants |
|---|---|---|---|
| **Word card** | The first image in every post — Hebrew word large, transliteration, gloss, date | 1200 × 675 | Day (morning) · Night (evening) |
| **Line card** | Near the end — the day's one line (*to carry* / *to sleep on*) | 1200 × 420 | Day · Night |

**Live template (edit and export PNGs):** https://claude.ai/code/artifact/5bd876b1-3c39-4e8a-a135-6579f2d67c96

**Palette:** navy `#1B2A41` · off-white `#F6F3EC` · cream `#F1EDE3` · gold `#A8781C` (day) / `#C9A24A` (night).
**Type:** Frank Ruehl Libre (Hebrew) · EB Garamond (everything else on the cards).

The `.dc.html` files here are the sources the live template is built from. `render.py` produces the finished PNGs from the same design.

**Daily production (the routine):** Claude runs

```
python3 one-word-wiser/brand/cards/render.py --date 2026-09-11 --hebrew "שָׁנָה" --translit shanah --gloss year \
  --date-label "Friday, September 11" --line-day "…" --line-night "…"
```

and the four PNGs land in `one-word-wiser/posts/cards/`. Evan drops the Word card as the post's first image and the Line card where the italic line sits. (The live template can also export PNGs by hand, but its export may substitute fonts; the script always uses the real ones.)
