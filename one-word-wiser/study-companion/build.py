#!/usr/bin/env python3
"""Build the local one-page study-companion prototype. No upload or delivery."""
import argparse
import json
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont, shapeStr
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FONTS = HERE.parent / 'brand' / 'fonts'
NAVY = HexColor('#1B2A41')
GRAY = HexColor('#5F625F')
PAPER = HexColor('#FFFFFF')
RULE = HexColor('#D5D9DC')


def build(source, output):
    data = json.loads(source.read_text())
    for name, filename in [('Garamond', 'EBGaramond[wght].ttf'),
                           ('GaramondItalic', 'EBGaramond-Italic[wght].ttf'),
                           ('Hebrew', 'FrankRuhlLibre[wght].ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(FONTS / filename)))
    output.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output), pagesize=(612, 792))
    c.setTitle(data['title'] + ' | The Rabbi’s Notes | Prototype')
    c.setAuthor('Draft prepared for Rabbi Evan Moffic')
    c.setFillColor(PAPER)
    c.rect(0, 0, 612, 792, stroke=0, fill=1)
    margin, width = 48, 516
    y = 751

    def para(text, size=11.5, leading=14.6, font='Garamond', color=NAVY,
             space=8, indent=0):
        nonlocal y
        style = ParagraphStyle('body', fontName=font, fontSize=size,
                               leading=leading, textColor=color)
        p = Paragraph(text, style)
        _, height = p.wrap(width-indent, 760)
        p.drawOn(c, margin+indent, y-height)
        y -= height+space

    def label(text):
        para(escape(text), size=10, leading=12.5, font='Helvetica-Bold', space=4)

    c.setFillColor(NAVY)
    c.setFont('Helvetica-Bold', 9)
    c.drawString(margin, y, data['series'])
    c.setFont('Garamond', 10)
    c.drawRightString(564, y, 'ONE WORD WISER')
    y -= 16
    c.setStrokeColor(RULE)
    c.setLineWidth(.6)
    c.line(margin, y, 564, y)
    y -= 15
    para(escape(data['title']), size=26, leading=29, space=8)
    c.setFont('Hebrew', 30)
    shaped = shapeStr(data['hebrew'], 'Hebrew', 30, force=True)
    c.drawString(margin, y-25, shaped)
    c.setFont('GaramondItalic', 12)
    c.drawString(margin+116, y-18, data['pronunciation'])
    y -= 43

    para(escape(data['verse']), size=17, leading=20, font='GaramondItalic', space=3)
    para(escape(data['verse_reference']), size=9.5, leading=12, color=GRAY, space=8)
    para(escape(data['context']), space=10)
    label(data['word_heading'])
    para(escape(data['word_note']), space=10)
    for reading in data['readings']:
        label(reading['heading'])
        para(escape(reading['text']), space=2)
        para(escape(reading['reference']), size=9, leading=11, color=GRAY, space=9)
    label('Read and discuss')
    for number, question in enumerate(data['questions'], 1):
        para(str(number)+'. '+escape(question), space=5)
    y -= 2
    para(escape(data['closing']), size=12, leading=15, font='GaramondItalic', space=7)

    if y < 86:
        raise ValueError(f'Content overflows reserved footer: y={y:.1f}')
    c.setStrokeColor(RULE)
    c.line(margin, 75, 564, 75)
    y = 67
    links = '  ·  '.join('<a href="'+escape(s['url'], {'"':'&quot;'})+'" color="#1B2A41">'+escape(s['label'])+'</a>' for s in data['sources'])
    para('Sources: '+links, size=8, leading=10, space=5)
    para('Rabbinic readings are paraphrased. Bible quotation: NIV. Links open the source texts.', size=7.5, leading=9, color=GRAY, space=5)
    para(escape(data['status']), size=6.8, leading=8, font='Helvetica', color=GRAY, space=0)
    if y < 20:
        raise ValueError('Footer overflow')
    c.showPage()
    c.save()
    print(output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, default=HERE/'sample-return.json')
    parser.add_argument('--output', type=Path, default=ROOT/'output/pdf/rabbis-notes-return-prototype.pdf')
    args = parser.parse_args()
    build(args.source, args.output)
