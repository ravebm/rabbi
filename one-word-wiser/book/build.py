#!/usr/bin/env python3
"""Build the free book, *Seven Hebrew Words Every Christian Should Know*, as a PDF.

    python3 one-word-wiser/book/build.py
    python3 one-word-wiser/book/build.py --src draft.md --out draft.pdf --chromium /path/to/chrome

Reads seven-words.md (next to this file), writes seven-words.pdf plus two preview PNGs
(preview-cover.png, preview-word.png) next to the source. Needs only Python 3 and a
Chromium or Google Chrome binary; fonts are local in ../brand/fonts, so no network.

The browser is looked for in this order: --chromium, $CHROMIUM, /opt/pw-browsers/chromium,
Google Chrome or Chromium on macOS, google-chrome / chromium / chromium-browser on PATH,
a Playwright cache. The build refuses to run while any [[placeholder]] is left in the
source, and stops if any page overflows (shorten that page and build again).

Source format: pages separated by a line that is exactly `---`. The first line of each
page says what it is: <!-- cover -->, <!-- note -->, <!-- word --> or <!-- last -->.
A word page starts with `# HEBREW · translit · gloss`, then paragraphs; a paragraph
that is only *italic* at the end is the line to carry; `> ` lines are the verse.
"""
import argparse, glob, html, os, pathlib, re, shutil, subprocess, sys, tempfile
from string import Template

HERE = pathlib.Path(__file__).resolve().parent
FONTS = (HERE / ".." / "brand" / "fonts").resolve()
NAVY, OFFWHITE, CREAM, GOLD, GOLD_NIGHT = "#1B2A41", "#F6F3EC", "#F1EDE3", "#A8781C", "#C9A24A"
ORD = ["one", "two", "three", "four", "five", "six", "seven"]


def find_browser(explicit=None):
    cands = [explicit, os.environ.get("CHROMIUM"), "/opt/pw-browsers/chromium",
             "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
             "/Applications/Chromium.app/Contents/MacOS/Chromium"]
    cands += [shutil.which(n) for n in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome")]
    cands += sorted(glob.glob(os.path.expanduser("~/.cache/ms-playwright/chromium-*/chrome-linux/chrome")), reverse=True)
    cands += sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium-*/chrome-mac*/Chromium.app/Contents/MacOS/Chromium")), reverse=True)
    for c in cands:
        if c and os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    sys.exit("No Chromium or Google Chrome found. Install Chrome, or pass --chromium /path/to/chrome, or set CHROMIUM.")


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", s)
    return s


def parse(text):
    left = sorted(set(re.findall(r"\[\[[^\]]*\]\]", text)))
    if left:
        sys.exit("Not built: the source still has placeholders to write:\n  " + "\n  ".join(left[:12]) + ("\n  …" if len(left) > 12 else ""))
    pages = []
    for raw in re.split(r"(?m)^---\s*$", text):
        lines = [l.rstrip() for l in raw.strip("\n").splitlines()]
        while lines and not lines[0].strip():
            lines.pop(0)
        if not lines:
            continue
        m = re.match(r"<!--\s*(cover|note|word|last)\s*-->", lines[0].strip())
        if not m:
            sys.exit(f"Every page must begin with <!-- cover -->, <!-- note -->, <!-- word --> or <!-- last -->. Got: {lines[0][:60]!r}")
        pg = {"kind": m.group(1), "title": None, "blocks": []}
        para = []

        def flush():
            if para:
                pg["blocks"].append(["p", " ".join(para)])
                para.clear()

        for ln in lines[1:]:
            if ln.startswith("# ") and pg["title"] is None:
                flush(); pg["title"] = ln[2:].strip(); continue
            if ln.startswith(">"):
                flush(); t = ln[1:].strip()
                if pg["blocks"] and pg["blocks"][-1][0] == "quote":
                    pg["blocks"][-1][1] += " " + t
                else:
                    pg["blocks"].append(["quote", t])
                continue
            if not ln.strip():
                flush(); continue
            para.append(ln.strip())
        flush()
        if pg["kind"] == "word" and pg["blocks"] and pg["blocks"][-1][0] == "p":
            t = pg["blocks"][-1][1]
            if re.fullmatch(r"\*[^*]+\*", t):
                pg["blocks"][-1] = ["carry", t[1:-1]]
        pages.append(pg)
    kinds = [p["kind"] for p in pages]
    if kinds != ["cover", "note"] + ["word"] * 7 + ["last"]:
        sys.exit(f"Expected cover, note, seven word pages, last. Got: {', '.join(kinds)}")
    return pages


def blocks_html(blocks):
    out = []
    for kind, t in blocks:
        if kind == "p":
            cls = ' class="sig"' if t.startswith("—") else (' class="fine"' if t.startswith("Scripture quotations") else "")
            out.append(f"<p{cls}>{inline(t)}</p>")
        elif kind == "quote":
            out.append(f"<blockquote>{inline(t)}</blockquote>")
    return "\n".join(out)


def page_html(pg, word_no, hebrews, page_no):
    k = pg["kind"]
    foot = f'<div class="foot"><span>rabbi.substack.com</span><span>{page_no}</span></div>'
    if k == "cover":
        row = " · ".join(f'<span class="h" dir="rtl">{html.escape(h)}</span>' for h in hebrews)
        lines = "".join(f'<div class="cover-line">{inline(t)}</div>' for _, t in pg["blocks"])
        return (f'<section class="page cover"><div class="kicker">One Word Wiser</div>'
                f'<div class="cover-mid"><h1>{inline(pg["title"] or "")}</h1><div class="heb-row" dir="ltr">{row}</div></div>'
                f'<div class="cover-foot">{lines}<div class="rule"></div><div class="site">rabbi.substack.com</div></div></section>')
    if k == "note":
        return (f'<section class="page note"><div class="kicker">{inline(pg["title"] or "Before you begin")}</div>'
                f'<div class="rule"></div><div class="body big">{blocks_html(pg["blocks"])}</div>{foot}</section>')
    if k == "word":
        parts = [p.strip() for p in (pg["title"] or "").split("·")]
        if len(parts) != 3:
            sys.exit(f"A word page title must be `# HEBREW · translit · gloss`. Got: {pg['title']!r}")
        heb, tr, gloss = parts
        carry = next((t for kind, t in pg["blocks"] if kind == "carry"), None)
        body = blocks_html([b for b in pg["blocks"] if b[0] != "carry"])
        carry_html = f'<div class="carry"><div class="rule"></div><div class="line">{inline(carry)}</div></div>' if carry else ""
        return (f'<section class="page word"><div class="kicker">{ORD[word_no - 1]} of seven</div>'
                f'<div class="head"><div class="heb" dir="rtl">{html.escape(heb)}</div><div class="tr">{inline(tr)}</div><div class="gloss">{inline(gloss)}</div></div>'
                f'<div class="body">{body}</div>{carry_html}{foot}</section>')
    return f'<section class="page last"><div class="last-mid">{blocks_html(pg["blocks"])}<div class="rule"></div><div class="site">rabbi.substack.com</div></div></section>'


SKELETON = Template('''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Seven Hebrew Words</title><style>
@font-face{font-family:"EB Garamond";src:url("$eb") format("truetype");font-weight:400 800;font-style:normal}
@font-face{font-family:"EB Garamond";src:url("$ebi") format("truetype");font-weight:400 800;font-style:italic}
@font-face{font-family:"Frank Ruehl Libre";src:url("$fr") format("truetype");font-weight:300 900}
@page{size:8.5in 11in;margin:0}
html,body{margin:0;padding:0;background:$offwhite}
body{font-family:"EB Garamond",Garamond,Georgia,serif;color:$navy;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:8.5in;height:11in;box-sizing:border-box;padding:.8in 1.15in .7in;position:relative;background:$offwhite;overflow:hidden;break-after:page;page-break-after:always}
.page:last-child{break-after:auto;page-break-after:auto}
.kicker{font-size:9.5pt;letter-spacing:.24em;text-transform:uppercase;color:$gold;font-weight:500}
.rule{border-top:1.2pt solid $gold;margin:.16in 0}
.foot{position:absolute;left:1.15in;right:1.15in;bottom:.5in;display:flex;justify-content:space-between;font-size:8.5pt;letter-spacing:.08em;color:$navy;opacity:.7;border-top:.8pt solid $gold;padding-top:6pt}
.heb{font-family:"Frank Ruehl Libre",David,"SBL Hebrew",serif;color:$navy}
.cover{background:$navy;color:$cream}
.cover .kicker{color:$goldn}
.cover-mid{position:absolute;left:1.15in;right:1.15in;top:3.1in}
.cover h1{font-weight:400;font-size:38pt;line-height:1.12;margin:0 0 .45in;color:$cream}
.heb-row{font-family:"Frank Ruehl Libre",David,"SBL Hebrew",serif;font-size:21pt;color:$goldn;line-height:1.5;white-space:nowrap}
.heb-row .h{unicode-bidi:isolate}
.cover-foot{position:absolute;left:1.15in;right:1.15in;bottom:.8in}
.cover-line{font-size:15pt;line-height:1.4}
.cover-line:first-child{font-size:18pt;font-style:italic}
.cover .rule{border-top-color:$goldn}
.cover .site,.last .site{font-size:9.5pt;letter-spacing:.18em;text-transform:uppercase;color:$goldn}
.last .site{color:$gold}
.body{font-size:12.5pt;line-height:1.52}
.body.big{font-size:14pt;line-height:1.55;margin-top:.1in}
.body p{margin:0 0 .13in}
.body p.sig{font-style:italic;margin-top:.25in}
.body strong{font-weight:500;color:$gold;text-transform:uppercase;letter-spacing:.14em;font-size:9.2pt}
.body blockquote{margin:.05in 0 .16in .05in;padding:.02in 0 .02in .22in;border-left:2pt solid $gold;font-size:13pt;line-height:1.5}
.head{text-align:center;margin:.35in 0 .28in}
.head .heb{font-size:88pt;line-height:1.05;font-weight:400}
.head .tr{font-size:24pt;font-style:italic;line-height:1.1;margin-top:.02in}
.head .gloss{font-size:10.5pt;letter-spacing:.2em;text-transform:uppercase;color:$gold;font-weight:500;margin-top:.1in}
.carry{position:absolute;left:1.15in;right:1.15in;bottom:1.05in;text-align:center}
.carry .line{font-size:17pt;font-style:italic;line-height:1.3;color:$navy;text-wrap:balance}
.last-mid{position:absolute;left:1.15in;right:1.15in;top:3.6in;text-align:center;font-size:17pt;line-height:1.5}
.last-mid p{margin:0 0 .22in}
.last-mid p.sig{font-style:italic}
.last-mid p.fine{font-size:8.5pt;line-height:1.4;opacity:.7;margin:.5in auto 0;max-width:4.6in}
.last-mid .rule{width:1.2in;margin:.35in auto .2in}
</style></head><body>$pages<script>
for(const p of document.querySelectorAll('.page')){p.dataset.overflow=(p.scrollHeight>p.clientHeight+1)?'yes':'no'}
</script></body></html>''')


def wrap(pages_html):
    return SKELETON.substitute(
        eb=(FONTS / "EBGaramond[wght].ttf").as_uri(), ebi=(FONTS / "EBGaramond-Italic[wght].ttf").as_uri(),
        fr=(FONTS / "FrankRuhlLibre[wght].ttf").as_uri(),
        offwhite=OFFWHITE, navy=NAVY, cream=CREAM, gold=GOLD, goldn=GOLD_NIGHT, pages=pages_html)


def crop_png(path, w, h):
    """Trim the screenshot to the sheet; a taller window is used because headless Chrome keeps ~90px for window chrome."""
    try:
        from PIL import Image
    except ImportError:
        return  # leave the extra strip; pip install pillow to trim it
    im = Image.open(path)
    if im.size[1] > h:
        im.crop((0, 0, w, h)).save(path)


def run(browser, args, what):
    base = [browser, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
            "--allow-file-access-from-files", "--virtual-time-budget=10000", "--run-all-compositor-stages-before-draw"]
    r = subprocess.run(base + args, capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        sys.exit(f"{what} failed:\n{r.stderr[-3000:]}")
    return r.stdout


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--src", default=str(HERE / "seven-words.md"))
    a.add_argument("--out", default=None, help="PDF path (default: next to --src, same name)")
    a.add_argument("--chromium", default=None)
    a.add_argument("--all-previews", action="store_true", help="also write preview/page-NN.png for every page")
    o = a.parse_args()
    src = pathlib.Path(o.src).resolve()
    out = pathlib.Path(o.out).resolve() if o.out else src.with_suffix(".pdf")
    for f in ("EBGaramond[wght].ttf", "EBGaramond-Italic[wght].ttf", "FrankRuhlLibre[wght].ttf"):
        if not (FONTS / f).is_file():
            sys.exit(f"Missing font {FONTS / f}; pull the repository again.")
    browser = find_browser(o.chromium)
    pages = parse(src.read_text(encoding="utf-8"))
    hebrews = [p["title"].split("·")[0].strip() for p in pages if p["kind"] == "word"]
    rendered, word_no = [], 0
    for i, pg in enumerate(pages, 1):
        if pg["kind"] == "word":
            word_no += 1
        rendered.append(page_html(pg, word_no, hebrews, i))
    with tempfile.TemporaryDirectory() as td:
        td = pathlib.Path(td)
        book = td / "book.html"
        book.write_text(wrap("\n".join(rendered)), encoding="utf-8")
        dom = run(browser, ["--dump-dom", book.as_uri()], "overflow check")
        flags = re.findall(r'data-overflow="(yes|no)"', dom)
        bad = [i + 1 for i, f in enumerate(flags) if f == "yes"]
        if bad:
            sys.exit(f"Page(s) {bad} overflow the sheet. Shorten them and build again.")
        run(browser, ["--no-pdf-header-footer", "--print-to-pdf-no-header", f"--print-to-pdf={out}", book.as_uri()], "PDF")
        previews = [("preview-cover.png", 0), ("preview-word.png", 2)]
        if o.all_previews:
            pdir = out.parent / "preview"; pdir.mkdir(exist_ok=True)
            previews = [(f"preview/page-{i + 1:02d}.png", i) for i in range(len(pages))]
        for name, idx in previews:
            one = td / (name.replace("/", "-") + ".html")
            bg = NAVY if pages[idx]["kind"] == "cover" else OFFWHITE
            one.write_text(wrap(rendered[idx]).replace("html,body{margin:0;padding:0;background:" + OFFWHITE, "html,body{margin:0;padding:0;background:" + bg), encoding="utf-8")
            png = out.parent / name
            run(browser, ["--window-size=816,1300", "--force-device-scale-factor=2", f"--screenshot={png}", one.as_uri()], name)
            crop_png(png, 816 * 2, 1056 * 2)
    n = len(re.findall(rb"/Type\s*/Page[^s]", out.read_bytes()))
    print(f"wrote {out} ({out.stat().st_size // 1024} KB, {n} pages) and " + ("preview/page-01..%02d.png" % len(pages) if o.all_previews else "preview-cover.png, preview-word.png"))
    if n != len(pages):
        sys.exit(f"Expected {len(pages)} pages, the PDF has {n}. Check the previews.")


if __name__ == "__main__":
    main()
