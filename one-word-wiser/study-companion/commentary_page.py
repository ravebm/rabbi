"""Two-page study: a central verse and sources, then explanation and discussion."""
from pathlib import Path
from urllib.parse import urlsplit
from xml.sax.saxutils import escape

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont, shapeStr
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

HERE = Path(__file__).resolve().parent
FONTS = HERE.parent / 'brand' / 'fonts'
NAVY, GRAY, RULE = map(HexColor, ('#1B2A41', '#666C70', '#D5D9DC'))
POSITIONS = {'upper-left': (44, 625, 440), 'upper-right': (422, 625, 440),
             'lower-left': (44, 425, 104), 'lower-right': (422, 425, 104)}


def validate(data):
    for key in ('series', 'title', 'hebrew', 'pronunciation', 'guiding_question', 'footer', 'status'):
        if not data.get(key, '').strip():
            raise ValueError('Fill all title, word, question, and footer fields')
    verse = data['verse']
    if not 1 <= len(verse['hebrew_lines']) <= 2 or not all(verse['hebrew_lines']):
        raise ValueError('Use one or two filled Hebrew verse lines')
    for key in ('english', 'reference', 'translation'):
        if not verse.get(key, '').strip():
            raise ValueError('Fill the verse and reference')
    readings = data['readings']
    if len(readings) != 4 or {r['position'] for r in readings} != set(POSITIONS):
        raise ValueError('Use four sources, one in each named position')
    for reading in readings:
        for key in ('author', 'heading', 'text', 'reference', 'selection', 'verified_on'):
            if not reading.get(key, '').strip():
                raise ValueError('Each source needs its text, reference, selection note, and verification date')
    for section in (data['commentary'], data['related_teaching']):
        if not section.get('title') or not section.get('paragraphs') or not all(section['paragraphs']):
            raise ValueError('Supply an explanation and related teaching')
    teaching = data['related_teaching']
    for key in ('author', 'excerpt', 'reference', 'verified_on'):
        if not teaching.get(key, '').strip():
            raise ValueError('Verify and attribute the related teaching')
    if not 2 <= len(data['questions']) <= 3 or not all(data['questions']):
        raise ValueError('Use two or three filled questions')
    resources = data['further_reading']
    if not 1 <= len(resources) <= 2:
        raise ValueError('Use one or two further readings')
    if not any(r['author'] in ('Rabbi Evan Moffic', 'Rabbi Jonathan Sacks') for r in resources):
        raise ValueError('Include a verified resource by Evan or Jonathan Sacks')
    for resource in resources:
        if any(not resource.get(k, '').strip() for k in ('author', 'title', 'display_note', 'verified_on')):
            raise ValueError('Complete and verify the further-reading entries')
    for item in (verse, *readings, teaching, *resources):
        url = urlsplit(item['url'])
        if url.scheme not in ('https', 'http') or not url.netloc:
            raise ValueError('Use direct source URLs')


def build_commentary_study(data, output):
    validate(data)
    for name, filename in [('Garamond', 'EBGaramond[wght].ttf'),
                           ('GaramondItalic', 'EBGaramond-Italic[wght].ttf'),
                           ('Hebrew', 'FrankRuhlLibre[wght].ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(FONTS / filename)))
    pdfmetrics.registerFontFamily('Garamond', normal='Garamond', italic='GaramondItalic')
    output.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(output), pagesize=(612, 792))
    c.setTitle(data['title'] + ' | The Rabbi’s Notes')
    c.setAuthor('Draft prepared for Rabbi Evan Moffic')

    def para(text, x, top, width, size=12, leading=15.5, font='Garamond',
             color=NAVY, align=TA_LEFT, bottom=65):
        style = ParagraphStyle('study', fontName=font, fontSize=size, leading=leading,
                               textColor=color, alignment=align)
        p = Paragraph(text, style)
        _, height = p.wrap(width, 792)
        if top - height < bottom:
            raise ValueError(f'Text exceeds its allotted space ({top-height:.1f} < {bottom}): {text[:90]}')
        p.drawOn(c, x, top-height)
        return top-height

    def link(label, url):
        return '<a href="' + escape(url, {'"': '&quot;'}) + '"><u>' + escape(label) + '</u></a>'

    def hebrew(text, center_x, baseline, size, width):
        shaped = shapeStr(text, 'Hebrew', size, force=True)
        if pdfmetrics.stringWidth(shaped, 'Hebrew', size) > width:
            raise ValueError('Hebrew line exceeds its column; split the line')
        c.setFillColor(NAVY)
        c.setFont('Hebrew', size)
        c.drawCentredString(center_x, baseline, shaped)

    def rule(y, x=44, right=568):
        c.setStrokeColor(RULE)
        c.setLineWidth(.55)
        c.line(x, y, right, y)

    def header(page):
        c.setFillColor(HexColor('#FFFFFF'))
        c.rect(0, 0, 612, 792, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.setFont('Helvetica-Bold', 8.5)
        c.drawString(44, 749, data['series'])
        c.setFont('Helvetica', 8)
        c.drawRightString(568, 749, 'ONE WORD WISER')
        c.setFillColor(GRAY)
        c.setFont('Helvetica', 6.5)
        c.drawString(44, 26, 'RABBI EVAN MOFFIC')
        c.drawCentredString(306, 26, f'{page} / 2')
        c.drawRightString(568, 26, data['status'])

    header(1)
    para(escape(data['title']), 44, 724, 305, 29, 33, bottom=690)
    if data.get('subtitle'):
        para(escape(data['subtitle']), 44, 685, 305,
             11.5, 14, 'GaramondItalic', GRAY, bottom=670)
    hebrew(data['hebrew'], 494, 706, 31, 148)
    para(escape(data['pronunciation']), 345, 691, 223, 10.5, 13,
         'GaramondItalic', GRAY, TA_CENTER)
    rule(661)
    para('FOUR COMMENTARIES ON ONE VERSE', 44, 647, 524, 8, 10, 'Helvetica', GRAY)

    for x in (199, 413):
        c.line(x, 622, x, 105)
    verse = data['verse']
    para(link(verse['reference'], verse['url']), 214, 576, 184,
         10.5, 13, 'Helvetica', GRAY, TA_CENTER)
    for i, line in enumerate(verse['hebrew_lines']):
        hebrew(line, 306, 531-i*28, 20.5, 184)
    verse_bottom = para('“' + escape(verse['english']) + '”', 219, 469, 174,
                        19, 24, 'GaramondItalic', NAVY, TA_CENTER, 280)
    para(escape(verse['translation']), 219, verse_bottom-13, 174,
         8, 10, 'Helvetica', GRAY, TA_CENTER)
    para(escape(data['guiding_question']), 221, 273, 170,
         15, 19, 'GaramondItalic', NAVY, TA_CENTER)

    for reading in data['readings']:
        x, top, limit = POSITIONS[reading['position']]
        para(escape(reading['author']).upper(), x, top, 146,
             8.5, 11, 'Helvetica-Bold', GRAY, bottom=limit)
        y = para(escape(reading['heading']), x, top-19, 146,
                 15, 17, 'GaramondItalic', bottom=limit)
        y = para(escape(reading['text']), x, y-10, 146,
                 12, 15.5, bottom=limit+26)
        para(link(reading['reference'], reading['url']), x, y-10, 146,
             8.5, 10.5, color=GRAY, bottom=limit)
    rule(78)
    para(escape(data['footer']), 44, 63, 524, 8.1, 10.5, color=GRAY, bottom=40)
    c.showPage()

    header(2)
    commentary = data['commentary']
    y = para(escape(commentary['title']), 44, 722, 524, 27, 31)
    rule(y-12)
    y = para(escape(commentary['label']), 44, y-28, 524,
             8.5, 11, 'Helvetica-Bold', GRAY)
    for paragraph in commentary['paragraphs']:
        y = para(paragraph, 44, y-9, 524, 12, 15.5)
    teaching = data['related_teaching']
    y = para(escape(teaching['label']), 44, y-17, 524,
             8.5, 11, 'Helvetica-Bold', GRAY)
    y = para(escape(teaching['title']), 44, y-6, 524, 18, 21, 'GaramondItalic')
    quote_top = y-8
    y = para('“' + escape(teaching['excerpt']) + '”', 57, quote_top, 498,
             12, 15.5, 'GaramondItalic')
    c.setStrokeColor(RULE)
    c.line(44, quote_top, 44, y)
    y = para(escape(teaching['author']) + ' · ' + link(teaching['reference'], teaching['url'])
             + ' · Working translation from Hebrew',
             57, y-5, 498, 8.8, 11, color=GRAY)
    for paragraph in teaching['paragraphs']:
        y = para(paragraph, 44, y-9, 524, 12, 15.5)

    y = para('READ AND DISCUSS', 44, y-19, 524, 8.5, 11, 'Helvetica-Bold', GRAY)
    for i, question in enumerate(data['questions'], 1):
        y = para(str(i) + '.  ' + escape(question), 44, y-5, 524, 11.5, 14.5)
    rule(y-14)
    y = para('FURTHER READING', 44, y-26, 524, 8.5, 11, 'Helvetica-Bold', GRAY)
    for resource in data['further_reading']:
        y = para(escape(resource['author']) + ' · ' + link(resource['title'], resource['url']),
                 44, y-6, 524, 10.5, 13)
        y = para(escape(resource['display_note']), 44, y-2, 524, 9, 11, color=GRAY)
    if y < 58:
        raise ValueError('Second page has insufficient footer clearance')
    c.showPage()
    c.save()
    print(output)
