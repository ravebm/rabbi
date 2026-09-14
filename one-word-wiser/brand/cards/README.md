# Optional post cards

The current daily format uses native Substack text, visible Hebrew, and a restrained typographic divider. Cards are optional: use only the assets specified in the current approved draft. The older three-card routine is retired. Do not restore the removed line-day card or generate illustrations just to fill a template.

| Source | Size | Use |
|---|---|---|
| WordCardDay.dc.html / WordCardNight.dc.html | 1200 x 675 | Optional Hebrew word card; avoid duplicating the same Hebrew block in the body |
| LineCardDay.dc.html / LineCardNight.dc.html | 1200 x 420 | Legacy line-card designs; include only if the approved copy explicitly requests one |

Historical Claude artifact: https://claude.ai/code/artifact/5bd876b1-3c39-4e8a-a135-6579f2d67c96 . Access and current contents have not been verified in this audit. The local HTML files and renderer are available sources; do not infer that this artifact is the new Claude Design workspace.

Palette: navy #1B2A41, off-white #F6F3EC, cream #F1EDE3, with restrained gold #A8781C or #C9A24A when the approved design uses it. Fonts: Frank Ruhl Libre for Hebrew and EB Garamond for English.

`render.py` is the legacy four-output renderer. It still takes line-day and line-night arguments and emits all four variants; generating files never means all variants belong in a post. Use it only for a specified card request and inspect Hebrew, fonts, and clipping. For the new design workflow, follow `../design-handoff.md` and `../../template-index.md`.
