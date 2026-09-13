# The free book: *Seven Hebrew Words Every Christian Should Know*

The welcome gift for every new subscriber. Seven pages, one word on each: *shalom, chesed, emunah, teshuvah, ruach, hallelujah, amen.* It is the free half of the teaching only (the picture, one verse, where a Christian already says the word, a line to carry); the secrets stay in the newsletter. The plan is in `../04-launch-and-growth.md`.

## Files

| File | What it is |
|---|---|
| `seven-words.md` | The book's text, drafted September 13. If it is ever redrafted, keep the `# HEBREW · translit · gloss` headers and follow the drafting brief in `../handoff-prompts.md` under "draft the free book." |
| `build.py` | Turns `seven-words.md` into `seven-words.pdf` and two preview PNGs. Needs Python 3 and Google Chrome or Chromium, nothing else; the fonts are in `../brand/fonts`. It refuses to build while a placeholder remains, and stops if a page overflows. |
| `seven-words.pdf`, `preview-cover.png`, `preview-word.png` | The built book, ten pages. Rebuild after any text change and commit all three. |
| `preview/` | Every page as a PNG, from `build.py --all-previews`. For checking; not committed. |

Build: `python3 one-word-wiser/book/build.py` (add `--chromium /path/to/chrome` if it can't find a browser).

## Where it lives

**SEVEN_WORDS_URL:** *not yet* (fill in the Substack post URL once the book is up; the welcome email links to it)

## How readers get it

Substack cannot attach a file to the welcome email, so the PDF is attached to a post on rabbi.substack.com that is published to the web only, never emailed, and the welcome email (`../samples/welcome-email.md`), which Substack sends to every new subscriber on its own, links the book's title to that post. Nothing else to run; every new signup gets it.

Evan approves the book before it goes up. It was drafted and built on the daily-model pull request (September 13); once he has read the PDF, the Codex prompt in `../handoff-prompts.md` puts it on Substack and wires the welcome email.

## The download post (paste verbatim)

**Title:** `Seven Hebrew Words Every Christian Should Know`

**Subtitle:** `Seven pages, one word on each. Free, for anyone who wants it.`

**Body:**

> *Shalom, chesed, emunah, teshuvah, ruach, hallelujah, amen.* You say some of them already. These seven pages show what each one means in Hebrew, where the Hebrew Bible first says it, and where it turns up in the New Testament.
>
> [attach `seven-words.pdf` here with the editor's file attachment]
>
> Print them. Put one in your Bible.
>
> One Hebrew word arrives here every morning at 6:00.
>
> — Rabbi Evan

**Settings:** audience Everyone · no section · URL slug `seven-words` if the post settings allow · **publish to the web only, do not send it as an email.**
