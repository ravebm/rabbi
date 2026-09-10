#!/usr/bin/env python3
"""Render the four One Word Wiser post cards (word/line × day/night) to PNG.

Usage:
  python3 render.py --date 2026-09-11 --hebrew "שָׁנָה" --translit shanah --gloss year \
      --date-label "Friday, September 11" \
      --line-day "A year is what repeats. A year is what changes. In Hebrew, that’s one word." \
      --line-night "God’s eyes are on the year at the end as much as at the beginning. Yours can be too." \
      [--out one-word-wiser/posts/cards] [--chromium /opt/pw-browsers/chromium]

Outputs: <out>/<date>-word-day.png (1200×675), -line-day.png (1200×420),
         -word-night.png (1200×675), -line-night.png (1200×420)
Requires: Chromium (PLAYWRIGHT path or --chromium) and Pillow (pip install pillow).
Design source of truth: the .dc.html files beside this script; keep the two in step.
"""
import argparse, html, os, shutil, subprocess, sys, tempfile

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500'
         '&family=Frank+Ruehl+Libre:wght@400;700&display=swap">')

def palette(night):
    return dict(bg="#1B2A41" if night else "#F6F3EC",
                ink="#F1EDE3" if night else "#1B2A41",
                gold="#C9A24A" if night else "#A8781C")

def page(body, w, h):
    return f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}
<style>html,body{{margin:0;padding:0;width:{w}px;height:{h}px;overflow:hidden;background:transparent}}</style>
</head><body>{body}</body></html>'''

def word_card(night, label, hebrew, translit, gloss, date):
    p = palette(night); e = html.escape
    return page(f'''<div style="position:relative;width:1200px;height:675px;background:{p['bg']};font-family:'EB Garamond',Garamond,Georgia,serif;overflow:hidden">
  <div style="position:absolute;top:60px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:baseline;font-size:17.4px;letter-spacing:.22em;text-transform:uppercase;color:{p['gold']};font-weight:500">
    <span>One Word Wiser</span><span>{e(label)}</span></div>
  <div style="position:absolute;top:144px;left:0;right:0;display:flex;flex-direction:column;align-items:center;gap:19px">
    <div style="font-family:'Frank Ruehl Libre',David,'SBL Hebrew',serif;font-size:252px;line-height:1.05;color:{p['ink']};direction:rtl">{e(hebrew)}</div>
    <div style="font-size:43px;font-style:italic;color:{p['ink']};line-height:1.1">{e(translit)}</div>
    <div style="font-size:26px;letter-spacing:.18em;text-transform:uppercase;color:{p['gold']};font-weight:500">{e(gloss)}</div></div>
  <div style="position:absolute;bottom:60px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:baseline;border-top:1.5px solid {p['gold']};padding-top:19px;font-size:19px;color:{p['ink']};opacity:.85">
    <span style="font-style:italic">{e(date)}</span><span style="letter-spacing:.08em">rabbi.substack.com</span></div>
</div>''', 1200, 675)

def line_card(night, label, line):
    p = palette(night); e = html.escape
    return page(f'''<div style="position:relative;width:1200px;height:420px;background:{p['bg']};font-family:'EB Garamond',Garamond,Georgia,serif;overflow:hidden;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:29px;padding:0 120px;box-sizing:border-box">
  <div style="width:60px;height:1.7px;background:{p['gold']}"></div>
  <div style="font-size:17.4px;letter-spacing:.22em;text-transform:uppercase;color:{p['gold']};font-weight:500">{e(label)}</div>
  <div style="font-size:49px;font-style:italic;line-height:1.25;color:{p['ink']};text-align:center;text-wrap:balance">{e(line)}</div>
</div>''', 1200, 420)

def shoot(chromium, html_path, png_path, w, h):
    # Headless Chromium's --window-size includes ~85px of window chrome, so the
    # viewport comes out shorter than asked. Render into a taller window and
    # crop to the card's exact box (the card is pinned to the top-left corner).
    pad = 240
    cmd = [chromium, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
           "--force-device-scale-factor=1", f"--window-size={w},{h + pad}",
           "--virtual-time-budget=8000", f"--screenshot={png_path}", f"file://{html_path}"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(png_path):
        sys.exit(f"chromium failed for {png_path}:\n{r.stderr[-2000:]}")
    from PIL import Image  # pip install pillow
    im = Image.open(png_path)
    im.crop((0, 0, w, h)).save(png_path, optimize=True)

def main():
    a = argparse.ArgumentParser()
    for k in ("date","hebrew","translit","gloss","date-label","line-day","line-night"):
        a.add_argument("--"+k, required=True)
    a.add_argument("--out", default="one-word-wiser/posts/cards")
    a.add_argument("--chromium", default=os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium"))
    a.add_argument("--night-label", default="Laila Tov · Evening")
    a.add_argument("--day-label", default="Morning")
    o = a.parse_args()
    os.makedirs(o.out, exist_ok=True)
    cards = [
        ("word-day",   word_card(False, o.day_label,   o.hebrew, o.translit, o.gloss, o.date_label), 1200, 675),
        ("line-day",   line_card(False, "One line to carry", o.line_day), 1200, 420),
        ("word-night", word_card(True,  o.night_label, o.hebrew, o.translit, o.gloss, o.date_label), 1200, 675),
        ("line-night", line_card(True,  "One line to sleep on", o.line_night), 1200, 420),
    ]
    tmp = tempfile.mkdtemp()
    try:
        for name, markup, w, h in cards:
            hp = os.path.join(tmp, name + ".html"); open(hp, "w").write(markup)
            out = os.path.abspath(os.path.join(o.out, f"{o.date}-{name}.png"))
            shoot(o.chromium, hp, out, w, h); print(out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

if __name__ == "__main__":
    main()
