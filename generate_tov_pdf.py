from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT

# ── COLOURS ───────────────────────────────────────────────────────────────────
BLACK   = colors.HexColor('#0d0d0d')
GREY    = colors.HexColor('#777777')
LGREY   = colors.HexColor('#bbbbbb')
RULE    = colors.HexColor('#d8d4ce')
WRONG   = colors.HexColor('#f5ebe8')
RIGHT   = colors.HexColor('#eaf1ea')
WRONG_B = colors.HexColor('#c8a9a0')
RIGHT_B = colors.HexColor('#9ab89a')
SHADE   = colors.HexColor('#f4f2ee')

W, H = A4
ML = 24*mm
MR = 24*mm

# ── STYLES ────────────────────────────────────────────────────────────────────
def S():
    d = {}

    d['cover_label'] = ParagraphStyle('cover_label',
        fontName='Times-Roman', fontSize=9, textColor=GREY,
        letterSpacing=3, leading=14, alignment=TA_LEFT)

    d['cover_title'] = ParagraphStyle('cover_title',
        fontName='Times-Roman', fontSize=52, textColor=BLACK,
        leading=54, alignment=TA_LEFT, spaceAfter=4)

    d['cover_sub'] = ParagraphStyle('cover_sub',
        fontName='Times-Italic', fontSize=22, textColor=GREY,
        leading=28, alignment=TA_LEFT)

    d['cover_body'] = ParagraphStyle('cover_body',
        fontName='Times-Roman', fontSize=10, textColor=GREY,
        leading=16, alignment=TA_LEFT)

    d['toc_head'] = ParagraphStyle('toc_head',
        fontName='Times-Roman', fontSize=8, textColor=GREY,
        letterSpacing=2.5, leading=12, spaceAfter=16, alignment=TA_LEFT)

    d['toc_item'] = ParagraphStyle('toc_item',
        fontName='Times-Roman', fontSize=11, textColor=BLACK,
        leading=22, alignment=TA_LEFT)

    d['section_num'] = ParagraphStyle('section_num',
        fontName='Times-Roman', fontSize=8, textColor=LGREY,
        letterSpacing=2, leading=12, spaceAfter=6, alignment=TA_LEFT)

    d['h1'] = ParagraphStyle('h1',
        fontName='Times-Roman', fontSize=34, textColor=BLACK,
        leading=38, spaceBefore=0, spaceAfter=16, alignment=TA_LEFT)

    d['h2'] = ParagraphStyle('h2',
        fontName='Times-Roman', fontSize=18, textColor=BLACK,
        leading=24, spaceBefore=24, spaceAfter=10, alignment=TA_LEFT)

    d['h3'] = ParagraphStyle('h3',
        fontName='Times-Roman', fontSize=12, textColor=BLACK,
        leading=18, spaceBefore=16, spaceAfter=6, alignment=TA_LEFT)

    d['rule_text'] = ParagraphStyle('rule_text',
        fontName='Times-Bold', fontSize=10.5, textColor=BLACK,
        leading=16, spaceAfter=8, alignment=TA_LEFT)

    d['body'] = ParagraphStyle('body',
        fontName='Times-Roman', fontSize=10.5, textColor=BLACK,
        leading=17, spaceAfter=10, alignment=TA_JUSTIFY)

    d['body_grey'] = ParagraphStyle('body_grey',
        fontName='Times-Roman', fontSize=10.5, textColor=GREY,
        leading=17, spaceAfter=10, alignment=TA_JUSTIFY)

    d['body_sm'] = ParagraphStyle('body_sm',
        fontName='Times-Roman', fontSize=9.5, textColor=GREY,
        leading=15, spaceAfter=8, alignment=TA_LEFT)

    d['list_item'] = ParagraphStyle('list_item',
        fontName='Times-Roman', fontSize=10.5, textColor=BLACK,
        leading=17, spaceAfter=6, leftIndent=12, alignment=TA_LEFT)

    d['ex_label_r'] = ParagraphStyle('ex_label_r',
        fontName='Times-Bold', fontSize=7.5, textColor=colors.HexColor('#3d6e3d'),
        letterSpacing=1.5, leading=12, spaceAfter=6, alignment=TA_LEFT)

    d['ex_label_w'] = ParagraphStyle('ex_label_w',
        fontName='Times-Bold', fontSize=7.5, textColor=colors.HexColor('#7a3e38'),
        letterSpacing=1.5, leading=12, spaceAfter=6, alignment=TA_LEFT)

    d['ex_body'] = ParagraphStyle('ex_body',
        fontName='Times-Italic', fontSize=10, textColor=BLACK,
        leading=16, spaceAfter=0, alignment=TA_LEFT)

    d['ex_note'] = ParagraphStyle('ex_note',
        fontName='Times-Roman', fontSize=8.5, textColor=GREY,
        leading=13, spaceAfter=0, alignment=TA_LEFT, spaceBefore=6)

    d['vocab_term'] = ParagraphStyle('vocab_term',
        fontName='Times-Bold', fontSize=10.5, textColor=BLACK,
        leading=16, spaceAfter=2, alignment=TA_LEFT)

    d['vocab_body'] = ParagraphStyle('vocab_body',
        fontName='Times-Roman', fontSize=10, textColor=colors.HexColor('#444'),
        leading=15, spaceAfter=12, alignment=TA_LEFT)

    d['check_q'] = ParagraphStyle('check_q',
        fontName='Times-Bold', fontSize=10.5, textColor=BLACK,
        leading=16, spaceAfter=3, alignment=TA_LEFT)

    d['check_a'] = ParagraphStyle('check_a',
        fontName='Times-Roman', fontSize=10, textColor=GREY,
        leading=15, spaceAfter=14, leftIndent=0, alignment=TA_LEFT)

    d['footer'] = ParagraphStyle('footer',
        fontName='Times-Roman', fontSize=8, textColor=LGREY,
        leading=12, alignment=TA_LEFT)

    d['footer_r'] = ParagraphStyle('footer_r',
        fontName='Times-Roman', fontSize=8, textColor=LGREY,
        leading=12, alignment=TA_RIGHT)

    return d

ST = S()

def rule(space_before=12, space_after=12, thickness=0.5, color=RULE):
    return HRFlowable(width='100%', thickness=thickness, color=color,
                      spaceAfter=space_after, spaceBefore=space_before)

def section_head(num, title):
    return [
        rule(space_before=0, space_after=10),
        Paragraph(num, ST['section_num']),
        Paragraph(title, ST['h1']),
    ]

def ex_block(kind, text, note=None):
    label = ST['ex_label_r'] if kind == 'right' else ST['ex_label_w']
    label_text = '✓  RIGHT' if kind == 'right' else '✗  WRONG'
    bg = RIGHT if kind == 'right' else WRONG
    border = RIGHT_B if kind == 'right' else WRONG_B
    inner = [[Paragraph(label_text, label)],
             [Paragraph(text, ST['ex_body'])]]
    if note:
        inner.append([Paragraph(note, ST['ex_note'])])
    t = Table(inner, colWidths=[W - ML - MR - 48])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('LEFTPADDING',  (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('TOPPADDING',   (0,0), (0,0),  11),
        ('TOPPADDING',   (0,1), (-1,-1), 6),
        ('BOTTOMPADDING',(0,-1),(-1,-1), 12),
        ('LINEBEFORE', (0,0), (-1,-1), 2.5, border),
    ]))
    return t

def wr_table(wrong, right):
    cw = [(W - ML - MR - 2) / 2] * 2
    data = [
        [Paragraph('✗  WRONG', ST['ex_label_w']),
         Paragraph('✓  RIGHT', ST['ex_label_r'])],
        [Paragraph(wrong, ST['ex_body']),
         Paragraph(right, ST['ex_body'])],
    ]
    t = Table(data, colWidths=cw)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), WRONG),
        ('BACKGROUND', (1,0), (1,-1), RIGHT),
        ('LEFTPADDING',  (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING',   (0,0), (-1, 0), 10),
        ('TOPPADDING',   (0,1), (-1,-1), 8),
        ('BOTTOMPADDING',(0,-1),(-1,-1), 12),
        ('LINEAFTER', (0,0), (0,-1), 1, colors.white),
        ('LINEBEFORE', (0,0), (0,-1), 2.5, WRONG_B),
        ('LINEBEFORE', (1,0), (1,-1), 2.5, RIGHT_B),
    ]))
    return t

# ── PAGE FOOTER ───────────────────────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    if doc.page > 2:
        canvas.setFont('Times-Roman', 8)
        canvas.setFillColor(LGREY)
        canvas.drawString(ML, 14*mm, 'RUNO — Writing Manual')
        canvas.drawRightString(W - MR, 14*mm, str(doc.page))
    canvas.restoreState()

# ── STORY ─────────────────────────────────────────────────────────────────────
def build():
    story = []

    # ─── COVER ────────────────────────────────────────────────────────────────
    story.append(Spacer(1, 44*mm))
    story.append(Paragraph('RUNO', ST['cover_label']))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph('Writing Manual', ST['cover_title']))
    story.append(Paragraph('How we write — and why.', ST['cover_sub']))
    story.append(Spacer(1, 14*mm))
    story.append(rule(space_before=0, space_after=12))
    story.append(Paragraph(
        'This document is for anyone who writes as RUNO — '
        'social posts, pitch documents, emails, event copy. '
        'It is a practical guide, not a philosophy paper.',
        ST['cover_body']))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph('Tbilisi · 2025', ST['cover_body']))
    story.append(PageBreak())

    # ─── CONTENTS ─────────────────────────────────────────────────────────────
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph('CONTENTS', ST['toc_head']))
    story.append(rule(space_before=0, space_after=14))
    toc = [
        ('01', 'What RUNO Is'),
        ('02', 'The Core Principle'),
        ('03', 'Four Writing Rules'),
        ('04', 'Words We Never Use'),
        ('05', 'Our Vocabulary'),
        ('06', 'By Channel'),
        ('07', 'Checklist'),
    ]
    for num, title in toc:
        story.append(Paragraph(
            f'<font color="#aaaaaa">{num}&nbsp;&nbsp;&nbsp;</font>{title}',
            ST['toc_item']))
    story.append(PageBreak())

    # ─── 01 WHAT RUNO IS ──────────────────────────────────────────────────────
    story += section_head('01', 'What RUNO Is')

    story.append(Paragraph(
        'RUNO is a cultural production agency based in Tbilisi. '
        'We produce events that change something — in how a brand is understood, '
        'in how a team sees itself, in what a guest carries out of the room.',
        ST['body']))
    story.append(Paragraph(
        'We apply the logic of cultural programming to commercial briefs. '
        'Most production companies start from logistics. We start from a '
        'different question: what should this guest feel or understand a year '
        'from now? Every production decision follows from the answer.',
        ST['body']))
    story.append(Paragraph(
        'We do not subcontract what we can build. FORGE is our in-house '
        'fabrication workshop — custom tables, installations, set elements. '
        'It exists because the work requires a level of physical specificity '
        'that the events market cannot supply.',
        ST['body']))

    story.append(Spacer(1, 4*mm))
    story.append(Paragraph('Clients', ST['h3']))
    story.append(Paragraph(
        'Chanel · Bentley · Porsche · Armani · Toyota WRC · Ford Arctic · '
        'Kia · State of Qatar · Bank of Georgia · Gorky Park',
        ST['body']))
    story.append(Paragraph(
        'Marketing directors at luxury brands. Corporate clients from MENA. '
        'HR leaders at distributed technology companies. '
        'Organisers of diplomatic and state-level events.',
        ST['body_grey']))

    story.append(PageBreak())

    # ─── 02 THE CORE PRINCIPLE ────────────────────────────────────────────────
    story += section_head('02', 'The Core Principle')
    story.append(Paragraph('The Language of After', ST['h2']))

    story.append(Paragraph(
        'RUNO speaks from the position of someone who has already done '
        'what they are describing. The work happened. The details are real. '
        'We do not promise — we recount. We do not anticipate — we report.',
        ST['body']))
    story.append(Paragraph(
        'This is not a stylistic choice. It is the only honest position '
        'for an agency with a biography. The silence after the Chanel Tbilisi '
        'show already happened. The Ambassador\'s entrance at 23:17 already '
        'happened. Our voice begins from that fact — and stays there.',
        ST['body']))
    story.append(Paragraph(
        'Everything in this manual follows from this position: '
        'past tense, specific detail, no claims that cannot be proven, '
        'and no selling.',
        ST['body']))

    story.append(PageBreak())

    # ─── 03 FOUR WRITING RULES ────────────────────────────────────────────────
    story += section_head('03', 'Four Writing Rules')
    story.append(Spacer(1, 2*mm))

    # Rule 1
    story.append(Paragraph('Rule 1', ST['section_num']))
    story.append(Paragraph('Use past tense and facts. Not promises.', ST['h2']))
    story.append(Paragraph(
        'Future tense is forbidden unless there is a signed contract '
        'and a confirmed date. "The Bentley Tbilisi Gala Dinner takes '
        'place May 1, 2026" is acceptable — it is a fact. '
        '"We will create an unforgettable experience" is not — '
        'it is a claim about something that has not happened.',
        ST['body']))
    story.append(Paragraph(
        'When writing about a forthcoming project, write about '
        'the production decisions already made — not about the '
        'outcomes you hope they produce.',
        ST['body']))
    story.append(Spacer(1, 3*mm))
    story.append(wr_table(
        'We will deliver a world-class experience your guests will remember for years.',
        'The production timeline is set. The table brief is at FORGE. '
        'The programme arc runs 3.5 hours with a single interval.'
    ))

    story.append(rule(space_before=20, space_after=0))

    # Rule 2
    story.append(Paragraph('Rule 2', ST['section_num']))
    story.append(Paragraph('Be specific. Names, numbers, materials, places.', ST['h2']))
    story.append(Paragraph(
        '"A large-scale event" means nothing. '
        '"500 guests, UN-level protocol, St. Petersburg, '
        'the Ambassador\'s entrance at 23:17" means everything. '
        'Specificity is evidence. It also tells the reader '
        'we were paying attention.',
        ST['body']))
    story.append(Paragraph(
        'Every abstraction can be replaced with the particular thing. '
        'The table has a material. The room has a count. '
        'The moment has a time. Use them.',
        ST['body']))
    story.append(Spacer(1, 3*mm))
    story.append(wr_table(
        'We organised a large-scale event for a major luxury automotive brand.',
        'Bentley Tbilisi Gala Dinner, May 2026. 150 UHNWI guests. '
        'Ten Georgian artists commissioned. Centrepiece table built at FORGE — '
        'oak and steel, 3.4 metres.'
    ))

    story.append(rule(space_before=20, space_after=0))

    # Rule 3
    story.append(Paragraph('Rule 3', ST['section_num']))
    story.append(Paragraph("Don't explain what you just said.", ST['h2']))
    story.append(Paragraph(
        'Every sentence that explains what the previous sentence '
        'already communicated tells the reader they missed it. '
        'Don\'t. Trust the gap.',
        ST['body']))
    story.append(Paragraph(
        'Cultural references, names, numbers — they stand without '
        'explanation. "Pina Bausch" does not need a bracket. '
        '"1,024,000 visitors" does not need a line saying this is impressive. '
        'Remove the parenthetical. Remove the clause. Move on.',
        ST['body']))
    story.append(Spacer(1, 3*mm))
    story.append(wr_table(
        'Like Punchdrunk (the acclaimed immersive theatre company founded by Felix Barrett), '
        'we believe the space itself should be part of the narrative.',
        'The logic is Punchdrunk\'s: the space is the narrative.'
    ))

    story.append(rule(space_before=20, space_after=0))

    # Rule 4
    story.append(Paragraph('Rule 4', ST['section_num']))
    story.append(Paragraph('Present the work. Step back.', ST['h2']))
    story.append(Paragraph(
        'We do not persuade. We do not use the word "offer." '
        'We do not say "we would be delighted." '
        'We place the biography in front of the reader '
        'and remove ourselves from the frame.',
        ST['body']))
    story.append(Paragraph(
        'The sales instinct — the urge to follow a case study '
        'with "and that\'s why you should work with us" — '
        'is the thing we resist most. '
        'The work speaks. Our job is to get out of its way.',
        ST['body']))
    story.append(Spacer(1, 3*mm))
    story.append(wr_table(
        'We are passionate about creating transformative experiences '
        'and we would be delighted to bring our expertise to your next event.',
        'The portfolio includes the Gorky Park 90th anniversary festival, '
        'the State of Qatar reception in St. Petersburg, the Chanel Tbilisi show, '
        'and the Bentley Tbilisi Gala Dinner. '
        'That is the context for the conversation.'
    ))

    story.append(PageBreak())

    # ─── 04 WORDS WE NEVER USE ────────────────────────────────────────────────
    story += section_head('04', 'Words We Never Use')
    story.append(Paragraph(
        'Each of these words has been overused to the point of '
        'carrying no information. When tempted to use one, '
        'ask what specifically you mean — then write that instead.',
        ST['body']))
    story.append(Spacer(1, 4*mm))

    forbidden = [
        ('Unique',
         'Applied to everything, it now means nothing. Write what is specifically different.'),
        ('Unforgettable',
         'A claim about someone else\'s memory. You cannot guarantee it. '
         'Describe the thing — "three seconds of silence after the show" — not the fact that it was unforgettable.'),
        ('Breathtaking',
         'Same problem. Only the person who was there can make this claim.'),
        ('Immersive atmosphere',
         'Both words are exhausted. "Immersive" now means any event with more than a screen and a stage.'),
        ('We create magic',
         'A surrender. RUNO\'s work has a mechanism. Name it.'),
        ('Premium / Luxury event',
         'Price-tier vocabulary. Our clients — who are, in fact, luxury brands — '
         'find these words either presumptuous or inaccurate.'),
        ('Curated journey',
         '"Curated" now means "we made choices." All events involve choices. '
         '"Journey" is equally depleted in experience design.'),
        ('Elevated / Bespoke',
         'Both have been adopted by the entire events industry and now identify nothing.'),
        ('We are pleased to offer',
         'The most common phrase in agency pitch writing. It is not a position. Do not use it.'),
        ('Innovative approach',
         'Self-applied. Innovation is demonstrated, not claimed.'),
        ('World-class / Synergy',
         'Corporate vocabulary that belongs to a different kind of company.'),
        ('"Hope this email finds you well"',
         'Wastes the first sentence of an email. Begin with the point.'),
    ]

    for term, reason in forbidden:
        story.append(KeepTogether([
            Paragraph(term, ST['vocab_term']),
            Paragraph(reason, ST['vocab_body']),
        ]))

    story.append(rule(space_before=8, space_after=12))
    story.append(Paragraph('What we never do structurally', ST['h3']))
    story.append(Paragraph(
        'Staccato dramatic fragments. '
        '"No crowd. No shared programme. No rush." '
        'This is a copywriting technique — sentence fragments as punchy line breaks. '
        'It reads as performed, not real. '
        'If something needs to be said about absence, say it in full sentences.',
        ST['body']))
    story.append(Spacer(1, 3*mm))
    story.append(wr_table(
        '"No crowd. No shared programme. No rush."',
        '"Each guest arrived with a private time slot and a curator '
        'who had been briefed on them specifically. '
        'The experience was not shared because it was not designed to be."'
    ))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph(
        'Rule of thumb: if it would look good on a billboard, '
        'it does not belong in RUNO copy.',
        ST['body_grey']))

    story.append(PageBreak())

    # ─── 05 VOCABULARY ────────────────────────────────────────────────────────
    story += section_head('05', 'Our Vocabulary')
    story.append(Spacer(1, 2*mm))

    story.append(Paragraph('Preferred terms', ST['h3']))
    terms = [
        ('Production', 'not "organisation," "delivery," or "execution." '
                       'We produce events the way a filmmaker produces a film.'),
        ('Precision',  'not "quality" or "excellence." '
                       'Precision implies a specific target was hit.'),
        ('Partner',    'not "vendor" or "supplier." '
                       'A partner has a stake in the outcome. We have a stake.'),
        ('Experience', 'not "event." An event is a scheduled occurrence. '
                       'An experience is what it produces in the people attending.'),
        ('Fabricated / built / made',
                       'not "sourced" or "procured." '
                       'When FORGE makes something, it is made.'),
        ('Commission', 'not "project" or "job." '
                       'A commission implies authorship on both sides.'),
    ]
    for term, body in terms:
        story.append(Paragraph(term, ST['vocab_term']))
        story.append(Paragraph(body, ST['vocab_body']))

    story.append(Paragraph('Preferred verbs', ST['h3']))
    story.append(Paragraph(
        '<b>fabricate</b> — physical making at FORGE'
        '&nbsp;&nbsp;·&nbsp;&nbsp;'
        '<b>calibrate</b> — fine adjustment toward a specific outcome'
        '&nbsp;&nbsp;·&nbsp;&nbsp;'
        '<b>engineer</b> — structural problem-solving'
        '&nbsp;&nbsp;·&nbsp;&nbsp;'
        '<b>choreograph</b> — intentional sequencing'
        '&nbsp;&nbsp;·&nbsp;&nbsp;'
        '<b>hold</b> — structural capacity (the park held; the production held)'
        '&nbsp;&nbsp;·&nbsp;&nbsp;'
        '<b>frame</b> — establish context'
        '&nbsp;&nbsp;·&nbsp;&nbsp;'
        '<b>carry</b> — bear weight (narrative, emotional, logistical)',
        ST['body']))

    story.append(Paragraph('Avoid', ST['h3']))
    story.append(Paragraph(
        'deliver · leverage · utilise · execute · showcase · highlight',
        ST['body_grey']))

    story.append(Spacer(1, 5*mm))
    story.append(Paragraph('Georgian words', ST['h3']))
    geo = [
        ('Supra', 'The Georgian feast. Not "dinner" or "reception." '
                  'A supra has a specific structure: led by a tamada, '
                  'governed by toasts that follow a ritual sequence. '
                  'Use when the event actually draws on this logic.'),
        ('Tamada', 'The toastmaster of a supra — not a master of ceremonies. '
                   'The tamada controls the emotional arc of the table. '
                   'The role is a form of dramaturgy.'),
        ('Okros Runo', 'The Golden Fleece. Our name in Georgian. '
                       'Use only in origin/brand storytelling contexts, '
                       'not in event copy.'),
    ]
    for term, body in geo:
        story.append(Paragraph(term, ST['vocab_term']))
        story.append(Paragraph(body, ST['vocab_body']))

    story.append(PageBreak())

    # ─── 06 BY CHANNEL ────────────────────────────────────────────────────────
    story += section_head('06', 'By Channel')
    story.append(Spacer(1, 2*mm))

    # LinkedIn
    story.append(Paragraph('LinkedIn', ST['h2']))
    story.append(Paragraph(
        'Anna\'s voice. First person. One post = one idea. '
        'These are observations, not announcements.',
        ST['body']))

    story.append(Paragraph('Rules', ST['rule_text']))
    for r in [
        'First line: no preamble — opens mid-thought or with a declarative statement',
        'One idea per post. If a second idea appears, it is its own post.',
        'No hashtags in body copy. If used at all — one line at the end, separately.',
        'No emoji in body.',
        'Paragraphs of 1–3 sentences.',
        'No generic call to action at the end.',
    ]:
        story.append(Paragraph(f'— {r}', ST['list_item']))

    story.append(Spacer(1, 5*mm))
    story.append(ex_block('right', (
        'The hardest part of the Qatar reception was not the protocol — not the 500 guests, '
        'the UN-level security, or the diplomatic placement with margins of minutes rather '
        'than hours. All of that is logistics, and logistics is solvable.\n\n'
        'The hard part was the third hall.\n\n'
        'We had designed the flow so that the main gathering space was approached through '
        'two rooms that progressively quieted — fewer people, less light, lower ceiling. '
        'The idea was that arrival should function as decompression rather than entrance.\n\n'
        'The Ambassador stopped in that third hall for forty seconds. Nobody had told him to. '
        'He stood near the window and looked at the arrangement. Then he walked through.\n\n'
        'That stop was not in the brief. It was in the design.'
    )))
    story.append(Spacer(1, 4*mm))
    story.append(ex_block('wrong', (
        '🌟 Thrilled to share that RUNO has been working on some truly incredible projects! '
        'Our team has been creating unforgettable luxury experiences for world-class brands — '
        'we couldn\'t be more excited about the journey ahead! '
        'Interested in working with us? Drop us a message! 💫\n\n'
        '#luxuryevents #tbilisi #innovation #eventproduction'
    ), 'Fails: "incredible / unforgettable / luxury / world-class / excited / journey" · '
       'emoji · no specific detail · generic CTA · hashtags in body'))

    story.append(rule(space_before=20, space_after=0))

    # Instagram
    story.append(Paragraph('Instagram', ST['h2']))
    story.append(Paragraph(
        'Visual diary of production. Captions in two registers only: '
        'very short (1–2 sentences that extend the image, not describe it) '
        'or long narrative (10+ lines using the image as the entry point). '
        '3–9 lines is the dead zone — it satisfies nothing.',
        ST['body']))

    story.append(Paragraph('Rules', ST['rule_text']))
    for r in [
        'Short captions: one sentence or two. No hashtag in caption body.',
        'Long captions: begin with the image as a portal, not as a label.',
        'No question-ending captions ("What do you think?")',
        'No engagement prompts ("Double tap," "Save this post")',
        'Production credits: one line at the end of long captions if needed',
    ]:
        story.append(Paragraph(f'— {r}', ST['list_item']))

    story.append(Spacer(1, 5*mm))
    story.append(ex_block('right',
        '[Short · FORGE workshop, table mid-fabrication]\n\n'
        'Steel finds its temperature at 1,400°C. We find ours at about the third design revision.'))
    story.append(Spacer(1, 4*mm))
    story.append(ex_block('right',
        '[Long · Empty venue space, Tbilisi, 11pm]\n\n'
        'An hour before a Porsche event, the most important work has already been done.\n\n'
        'The chairs are placed. Each position was calculated not for sight lines to a stage '
        '— there is no stage — but for the conversation that will happen between the person '
        'in that chair and the car three metres to their left.\n\n'
        'Distance is a design decision. 3 metres is close enough to see the stitching on the seat. '
        'Far enough that you choose to approach. We spent forty minutes on the distance.\n\n'
        'In Tbilisi, this Porsche evening ran forty minutes longer than planned. '
        'Nobody left early. That is the only metric that matters.'))
    story.append(Spacer(1, 4*mm))
    story.append(ex_block('wrong',
        'We are SO excited to share a sneak peek of what\'s happening at FORGE! 🔥 '
        'Working tirelessly on some truly stunning pieces for upcoming events. '
        'Every detail matters when it comes to delivering world-class luxury experiences! '
        'Stay tuned! 🙌✨\n\n'
        '#forge #luxuryevents #behindthescenes #eventdesign #tbilisi #bespoke',
        '"sneak peek / working tirelessly / stunning / world-class luxury" · '
        '"Stay tuned" contradicts Language of After · caption describes what the image already shows · '
        'six hashtags'))

    story.append(rule(space_before=20, space_after=0))

    # Email
    story.append(Paragraph('Email', ST['h2']))
    story.append(Paragraph(
        'Context in one sentence maximum, then the substance. '
        'End with a specific next step — not options, one step.',
        ST['body']))

    story.append(Paragraph('Rules', ST['rule_text']))
    for r in [
        'Subject line: specific. "Bentley Tbilisi — production timeline for your review" not "A thought on your event."',
        'No "Hope this email finds you well." No "Just wanted to follow up."',
        'Three paragraphs maximum. One idea per paragraph.',
        'Close: name the one action needed, with a date or time if relevant.',
        'Sign-off: Anna. No "Kind regards" unless it fits the relationship.',
    ]:
        story.append(Paragraph(f'— {r}', ST['list_item']))

    story.append(Spacer(1, 5*mm))
    story.append(ex_block('right',
        'Subject: Porsche Tbilisi Festival — venue decision and revised timeline\n\n'
        'The Georgian National Museum site was approved by Porsche DE on Tuesday. '
        'This changes the production timeline by eleven days.\n\n'
        'Attached is the revised schedule. Three items need your decision by April 22: '
        'secondary entrance placement, catering format (plated or supra-style — '
        'this affects the FORGE brief), and programme close time.\n\n'
        'Can we speak Thursday at 14:00 Tbilisi time?\n\nAnna'))
    story.append(Spacer(1, 4*mm))
    story.append(ex_block('wrong',
        'Subject: Following up :)\n\n'
        'Hi [Name],\n\nHope this email finds you well! Just wanted to touch base about '
        'the exciting Porsche event. We are passionate about creating unforgettable luxury '
        'experiences and truly believe we could bring something really special. '
        'Our innovative approach would be a perfect fit!\n\n'
        'Would love to find a time that works for you. Warm wishes, Anna ✨',
        '"Hope this email finds you well" · "just wanted to touch base" · '
        '"exciting / unforgettable / luxury / innovative / passionate / special" · '
        'no specific detail or timeline · no clear ask · emoji'))

    story.append(rule(space_before=20, space_after=0))

    # Pitch Documents
    story.append(Paragraph('Pitch Documents', ST['h2']))
    story.append(Paragraph(
        'Narrative structure, not bullet points. '
        'Each section is a chapter — a frame established, '
        'evidence developed, a single point landed. '
        'The pitch is an argument, not a menu.',
        ST['body']))

    story.append(Paragraph('Rules', ST['rule_text']))
    for r in [
        'No executive summary bullet list. Begin with the frame.',
        'Name the client specifically: not "luxury automotive client" but "Bentley."',
        'Section headings are statements: not "Our Approach" but "We do not start with a brief. We start with a question."',
        'Biographies appear as narrative — the sequence of decisions, not a CV.',
        'FORGE is introduced as a structural argument: it changes what we can propose.',
        'No summary conclusion. Land the single most important point and stop.',
    ]:
        story.append(Paragraph(f'— {r}', ST['list_item']))

    story.append(Spacer(1, 5*mm))
    story.append(ex_block('right',
        'The Question Before the Brief\n\n'
        'Every pitch document you have received before this one began with an answer. '
        'Capability, process, team, portfolio.\n\nWe begin earlier.\n\n'
        'The Bentley Tbilisi Gala Dinner on May 1 will be attended by 150 guests who '
        'have attended events of this calibre before. '
        'The question is not whether RUNO can organise a dinner. '
        'The question is what 150 people considering a Bentley should feel when they leave '
        '— and whether that feeling serves the brand\'s positioning in Georgia over the next three years.\n\n'
        'We have been asking this since the first production meeting. '
        'The answers changed the venue, the FORGE brief, the programme arc, and the decision not to have a stage.\n\n'
        'This document is the record of those answers.'))
    story.append(Spacer(1, 4*mm))
    story.append(ex_block('wrong',
        'Executive Summary\n'
        '• RUNO is a leading luxury event production agency in Tbilisi\n'
        '• We specialise in bespoke, immersive experiences for premium brands\n'
        '• Our innovative approach combines creativity with world-class execution\n'
        '• We are pleased to offer our services for the Bentley Tbilisi Gala Dinner\n\n'
        'We believe every event is an opportunity to create something truly unforgettable. '
        'Our passionate team will ensure your event exceeds all expectations.',
        'Bullet structure · nine forbidden words in two sections · '
        '"We are pleased to offer" · no specific: no count, date, material, or decision'))

    story.append(PageBreak())

    # ─── 07 CHECKLIST ─────────────────────────────────────────────────────────
    story += section_head('07', 'Checklist')
    story.append(Paragraph(
        'Before publishing anything written as RUNO. '
        'Every "no" requires a revision.',
        ST['body']))
    story.append(Spacer(1, 5*mm))

    checks = [
        ('Is there a word from the forbidden list?',
         'unique · unforgettable · breathtaking · immersive atmosphere · magic · premium · '
         'luxury event · curated · journey · elevated · bespoke · "pleased to offer" · '
         'innovative · synergy · world-class · "hope this email finds you"'),
        ('Does every sentence carry a specific: name, number, place, material, or decision?',
         'If a sentence contains only adjectives and abstractions, add the specific or cut the sentence.'),
        ('Is there a future-tense promise not backed by a signed contract?',
         'Replace with past-tense evidence or a present-tense principle.'),
        ('Does the text explain a reference that should stand alone?',
         'Remove the bracket or clause. Trust the reader.'),
        ('Is there an exclamation mark, reader-addressed question, or emoji in body copy?',
         'Remove all three.'),
        ('Does the opening sentence begin with a greeting or wellbeing wish?',
         'Delete it. Begin with the next sentence.'),
        ('Is the call to action generic?',
         '"Feel free to reach out" / "Let\'s connect" — replace with the specific action requested, or remove.'),
        ('Does the text describe RUNO in general, or demonstrate through specific cases?',
         'General description is not evidence. Add the case or reconsider whether the text is needed.'),
        ('Is the word "we" carrying something real?',
         '"We are passionate" — the "we" is empty. "We built the table" — the "we" is accountable.'),
        ('Could this text have been written by any other agency?',
         'If yes: go back through checks 1–9. The fix is usually one specific detail.'),
    ]

    for i, (q, a) in enumerate(checks):
        story.append(KeepTogether([
            Paragraph(f'<b>{i+1:02d}&nbsp;&nbsp;</b>{q}', ST['check_q']),
            Paragraph(a, ST['check_a']),
        ]))

    story.append(rule(space_before=8, space_after=14))
    story.append(Paragraph(
        'RUNO copy rarely fails at scale. It fails at the word level. '
        'The revision is usually small: remove a word, add a number, '
        'cut the last sentence.',
        ST['body_grey']))

    # back cover space
    story.append(Spacer(1, 20*mm))
    story.append(rule(space_before=0, space_after=12))
    story.append(Paragraph('RUNO', ST['cover_label']))
    story.append(Paragraph('Okros Runo LLC · Tbilisi, Georgia · 2025',
                            ST['cover_body']))

    return story


def main():
    path = '/Users/admin/RUNO_Tone_of_Voice.pdf'
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=ML, rightMargin=MR,
        topMargin=22*mm, bottomMargin=22*mm,
    )
    doc.build(build(), onFirstPage=on_page, onLaterPages=on_page)
    print(f'Saved: {path}')

if __name__ == '__main__':
    main()
