# Fonts

The two faces the cards and the book use, kept here so nothing needs the network at build time.

- **EB Garamond** (`EBGaramond[wght].ttf`, `EBGaramond-Italic[wght].ttf`), the English face. SIL Open Font License, see `OFL-EBGaramond.txt`.
- **Frank Ruhl Libre** (`FrankRuhlLibre[wght].ttf`), the Hebrew face. SIL Open Font License, see `OFL-FrankRuhlLibre.txt`.

Both from github.com/google/fonts. `book/build.py` reads them from this folder; the cards script still loads the same faces from Google Fonts.
