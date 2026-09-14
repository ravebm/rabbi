# One Word Wiser design handoff

Status checked September 14, 2026. Evan confirmed there were no existing projects and authorized setup. Authenticated browser access works for both services. The new Claude Design system has been generated and its editable candidate archive saved to git, and the private Magnific project has its three folders and provisional brand references. Current project links, source snapshot, and verification state are recorded in `designs/one-word-wiser/README.md`. Reuse these projects. The historical Claude artifact URL in `cards/README.md` is not the new design-system project.

This setup uses file uploads and browser controls. Claude Design requested a separate GitHub connection; it was not granted. Neither tool has been connected to Codex through an API/MCP integration in this task. A git push does not refresh either workspace automatically.

Later September 14 update: Evan reports that Magnific MCP is now connected. Treat the preceding paragraph as the earlier setup record. Its host/client has not yet been established here; this Codex task's callable tool inventory currently has no Magnific tools. Do not ask Evan to repeat setup by default. Inspect the existing connected client when executing a media task.

## Roles and source files

- **Codex and Claude writing:** prepare and verify copy using `../../skills/one-word-wiser/SKILL.md`, preserve Evan’s edits, and maintain the reviewed sources in git.
- **Claude Design:** refine reusable layout, typography, and spacing for the Rabbi’s Notes page or an explicitly requested brand asset. Use the approved copy and existing fonts; return editable source and exports to this repository.
- **Magnific:** produce and refine media for requested growth campaigns: images, video sequences, alternate formats, and reusable creative workflows. Its role extends beyond upscaling. Use the existing MCP connection in the client where it is available. Keep Hebrew, vowel marks, titles, and quotations in a separate typeset layer; do not regenerate them as picture detail. The daily letter can remain restrained while distribution assets use richer media.
- **Evan:** reviews the teaching and design. A design approval does not itself authorize a Substack send.

The daily default remains native text and a restrained divider. Evan’s request to incorporate design tools does not by itself specify illustrations in every letter.

## Paste-ready Claude Design brief

> Refine the One Word Wiser visual system using the supplied current repository files. Start with AGENTS.md, one-word-wiser/01-positioning.md, one-word-wiser/02-daily-format.md, and one-word-wiser/study-companion/README.md. Use the current sample-return.json as exact sample copy and the prototype PDF as the current layout reference. Make one elegant, readable page with navy #1B2A41, white or restrained cream, EB Garamond for English, and Frank Ruhl Libre for Hebrew. Retain selectable Hebrew with all vowel marks and real clickable links. Preserve the passage, Hebrew teaching, two rabbinic observations, two discussion questions, closing thought, and one Further reading resource. Keep primary-source references separate. Improve spacing and hierarchy without rewriting the teaching or adding decorative imagery. Return editable source and a one-page PDF for review, with the fonts and export steps documented. Do not publish, change subscription promises, or replace the approved master until Evan reviews the candidate.

Provide these files through the app’s supported access or upload flow. Do not assume a GitHub commit automatically updates Claude Design. If the app cannot read the repository, supply the specific brief, copy, and font files needed for the named task.

## Magnific handoff when an image is requested

Specify the source file, intended placement, output dimensions, and allowed changes. For enhancement that should preserve the original, start from its fidelity-oriented option and compare the result with the source. Use creative reinterpretation only when that is the requested task. Add exact text and Hebrew after image processing using the typesetting template. Keep the original, candidate, and selected export distinct. Record the actual mode and settings used; never mark an unrun enhancement complete.

## Returning work to git

1. Save candidate editable design sources and exports under `brand/designs/<asset-name>/`, with a short README containing the source commit, project URL, tool used, export steps, and review status. Create this folder only when an actual design exists.
2. Check the full page, phone reading size where applicable, Hebrew vowel marks, selectable text, links, and export dimensions. A screenshot does not prove a link works or the source is editable.
3. After Evan selects a design, update the canonical template and its template-index entry. Keep earlier versions in git and preserve meaningful design alternatives separately.
4. Commit and push. Verify the actual resulting artifact and repository state. Report app connection, source preparation, export, approval, and publication as separate statuses.

## Product documentation checked

- [Magnific MCP](https://www.magnific.com/mcp), checked September 14: documents image, video, audio, vector and 3D generation, media editing, reusable Spaces workflows, and access to prior creations. Generation/transformation through MCP consumes credits; a connected account is not proof of a tested finished-video workflow. See [the growth pilot](../growth/2026-09-14-hyatt-growth-pilot.md).
- [Claude Design](https://www.anthropic.com/news/claude-design-anthropic-labs): supports design-system input, editable design work, and exports including PDF and HTML. These documented capabilities are not evidence of account access in this task.
- [Magnific upscaling](https://docs.magnific.com/api-reference/image-upscaler-creative/image-upscaler): distinguishes creative enhancement that adds detail from precision-oriented upscaling. No API credentials or paid processing job were configured here.
