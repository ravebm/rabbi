"""Spacious one-verse / four-reading page. Content is supplied in JSON."""
from pathlib import Path
from xml.sax.saxutils import escape
from urllib.parse import urlsplit
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont, shapeStr
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import Paragraph

HERE = Path(__file__).resolve().parent
FONTS = HERE.parent / 'brand' / 'fonts'
NAVY = HexColor('#1B2A41')
GRAY = HexColor('#666C70')
RULE = HexColor('#D5D9DC')
POSITIONS = {'upper-left': (44, 638), 'upper-right': (422, 638),
             'lower-left': (44, 436), 'lower-right': (422, 436)}


def validate(data):
    for key in ('series', 'title', 'hebrew', 'pronunciation'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError('Fill every title and word field before building')
    for key in ('english', 'reference', 'translation'):
        if not data['verse'].get(key, '').strip():
            raise ValueError('Fill the verse and its reference before building')
    if not 1 <= len(data['verse']['hebrew_lines']) <= 2:
        raise ValueError('Use one or two short Hebrew verse lines')
    readings = data['readings']
    if len(readings) != 4 or {r['position'] for r in readings} != set(POSITIONS):
        raise ValueError('Use four readings, one in each named position')
    for reading in readings:
        if any(not reading.get(k, '').strip() for k in ('author', 'heading', 'text', 'reference')):
            raise ValueError('Each reading needs an author, heading, text, and reference')
        if len(reading['text'].split()) > 35:
            raise ValueError('Keep each reading to 35 words or fewer; do not shrink type')
    if not 2 <= len(data['questions']) <= 3:
        raise ValueError('Use two or three short questions')
    resources = data['further_reading']
    if not 1 <= len(resources) <= 2:
        raise ValueError('Use one or two further readings')
    if not any(r['author'] in ('Rabbi Evan Moffic', 'Rabbi Jonathan Sacks') for r in resources):
        raise ValueError('Include one verified resource by Evan or Jonathan Sacks')
    for item in [data['verse'], *readings, *resources]:
        url = urlsplit(item['url'])
        if url.scheme not in ('https', 'http') or not url.netloc:
            raise ValueError('Use direct source URLs')
    for resource in resources:
        if not resource.get('verified_on'):
            raise ValueError('Verify each further reading before building')


def build_verse_page(data, output):
    validate(data)
    for name, filename in [('Garamond', 'EBGaramond[wght].ttf'),
                           ('GaramondItalic', 'EBGaramond-Italic[wght].ttf'),
                           ('Hebrew', 'FrankRuhlLibre[wght].ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(FONTS / filename)))
    output.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output), pagesize=(612, 792))
    c.setTitle(data['title'] + ' | The Rabbi’s Notes')
    c.setAuthor('Rabbi Evan Moffic - review copy')
    c.setFillColor(HexColor('#FFFFFF'))
    c.rect(0, 0, 612, 792, fill=1, stroke=0)

    def para(text, x, top, width, size=12, leading=15.5, font='Garamond',
             color=NAVY, align=TA_LEFT, max_height=None):
        style = ParagraphStyle('page', fontName=font, fontSize=size, leading=leading,
                               textColor=color, alignment=align)
        p = Paragraph(text, style)
        _, height = p.wrap(width, 792)
        if max_height is not None and height > max_height:
            raise ValueError(f'Text exceeds its allotted space: {text[:70]}')
        p.drawOn(c, x, top-height)
        return top-height

    def link(label, url):
        return '<a href="' + escape(url, {'"': '&quot;'}) + '"><u>' + escape(label) + '</u></a>'

    def hebrew(text, center_x, baseline, size, width):
        shaped = shapeStr(text, 'Hebrew', size, force=True)
        actual = pdfmetrics.stringWidth(shaped, 'Hebrew', size)
        if actual > width:
            raise ValueError('Hebrew line exceeds its column; split the line')
        c.setFillColor(NAVY)
        c.setFont('Hebrew', size)
        c.drawCentredString(center_x, baseline, shaped)

    c.setFillColor(NAVY)
    c.setFont('Helvetica-Bold', 8.5)
    c.drawString(44, 749, data['series'])
    c.setFont('Helvetica', 8)
    c.drawRightString(568, 749, 'ONE WORD WISER')
    para(escape(data['title']), 44, 725, 305, 29, 33, max_height=34)
    hebrew(data['hebrew'], 494, 706, 31, 148)
    para(escape(data['pronunciation']), 345, 691, 223, 10.5, 13,
         'GaramondItalic', GRAY, TA_CENTER, 14)
    c.setStrokeColor(RULE)
    c.setLineWidth(.55)
    c.line(44, 670, 568, 670)

    # Central text and surrounding commentary share the same reading field.
    for x in (199, 413):
        c.line(x, 635, x, 297)
    verse = data['verse']
    para(link(verse['reference'], verse['url']), 214, 618, 184,
         10.5, 13, 'Helvetica', GRAY, TA_CENTER, 14)
    for i, line in enumerate(verse['hebrew_lines']):
        hebrew(line, 306, 574-i*27, 20.5, 184)
    verse_bottom = para('“' + escape(verse['english']) + '”', 219, 513, 174,
         19, 24, 'GaramondItalic', NAVY, TA_CENTER, 144)
    para(escape(verse['translation']), 219, verse_bottom-15, 174,
         8, 10, 'Helvetica', GRAY, TA_CENTER, 11)

    for reading in data['readings']:
        x, top = POSITIONS[reading['position']]
        para(escape(reading['author']).upper(), x, top, 146,
             8.5, 11, 'Helvetica-Bold', GRAY, max_height=12)
        y = para(escape(reading['heading']), x, top-19, 146,
                 15, 17, 'GaramondItalic', max_height=35)
        y = para(escape(reading['text']), x, y-9, 146, max_height=110)
        para(link(reading['reference'], reading['url']), x, y-9, 146,
             8.1, 10, 'Garamond', GRAY, max_height=20)
        if y-29 < (469 if top > 500 else 267):
            raise ValueError('Commentary is too long for the white-space layout')

    para('READ AND REFLECT', 44, 244, 524, 8.5, 11, 'Helvetica-Bold', GRAY)
    for i, question in enumerate(data['questions'], 1):
        para(str(i) + '.  ' + escape(question), 44, 220-(i-1)*25, 524,
             12, 16, max_height=17)

    c.line(44, 143, 568, 143)
    para('FURTHER READING', 44, 124, 524, 8.5, 11, 'Helvetica-Bold', GRAY)
    for i, resource in enumerate(data['further_reading']):
        para(escape(resource['author']) + ' · ' + link(resource['title'], resource['url']),
             44, 104-i*19, 524, 11.5, 14, max_height=15)
    para(escape(data['footer']), 44, 49, 524, 7.5, 10, color=GRAY, max_height=11)
    c.setFillColor(GRAY)
    c.setFont('Helvetica', 6.5)
    c.drawString(44, 26, 'RABBI EVAN MOFFIC')
    c.drawRightString(568, 26, data['status'])
    c.showPage()
    c.save()
    print(output)
