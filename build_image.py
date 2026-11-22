#!/usr/bin/env python3
"""Build entry.png for news-image-20261122: Sunday 22 November 2026 world news in one image.

Deterministic: fixed layout, fixed fonts, no randomness, no network.
Run: python3 build_image.py  -> writes entry.png beside this file (1024x1024).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = Path(__file__).resolve().parent / "entry.png"

BG = (250, 247, 240)
INK = (26, 26, 26)
NAVY = (31, 58, 95)
TEAL = (14, 107, 122)
RED = (192, 57, 43)
GOLD = (201, 162, 39)
LIGHT = (255, 255, 255)
GREY = (90, 90, 90)
PALE = (238, 233, 221)
PALE_TEAL = (222, 238, 240)
PALE_GOLD = (246, 238, 210)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.22)
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def pin(draw, cx, cy, num, fill=RED):
    r = 13
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill, outline=LIGHT, width=2)
    f = font(15, bold=True)
    tw = draw.textlength(str(num), font=f)
    draw.text((cx - tw / 2, cy - 8), str(num), font=f, fill=LIGHT)


def card(draw, box, fill=LIGHT, outline=(200, 195, 180)):
    draw.rounded_rectangle(box, radius=10, fill=fill, outline=outline, width=1)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---------- Masthead ----------
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.text((24, 10), "THE WORLD IN ONE IMAGE  •  WORLD NEWS OF THE DAY", font=font(15, bold=True), fill=(180, 205, 230))
    d.text((24, 32), "Sunday 22 November 2026", font=font(52, bold=True), fill=LIGHT)
    d.text((24, 92), "Reported by early Sunday + scheduled today  •  Times GMT unless stated  •  Saturday events labelled SAT", font=font(13), fill=(210, 222, 238))
    d.rectangle([0, 118, W, 124], fill=GOLD)

    # ---------- Lead cards ----------
    leads = [
        ("1  WORLD — ANTALYA, TURKEY", "COP31 talks run into Sunday with new deal text",
         "Negotiators passed Friday's deadline and worked through Saturday. Objections by 03:00 GMT; approval session 06:00 GMT today. Nearly 200 delegations; fossil-fuel wording + adaptation finance still at issue. [Reuters]"),
        ("2  ASIA — HONG KONG", "Hong Kong votes for Election Committee",
         "Polls 09:00–18:00 today: 856 candidates for 723 seats in 31 subsectors. Ballots form the 1,500-member committee (term from 1 Feb 2027) that elects the Chief Executive. [HK REO; China Daily Asia]"),
        ("3  AMERICAS — LAS VEGAS, USA", "Las Vegas Grand Prix overnight",
         "Formula 1 Round 21: Sat 20:00 PST = Sun 04:00 GMT, 50 laps on the Strip Circuit. Both championships already decided. No winner claimed — race runs overnight. [Formula1.com]"),
    ]
    x0, y0, cw, ch, gap = 16, 136, 320, 250, 12
    for i, (kicker, head, body) in enumerate(leads):
        x = x0 + i * (cw + gap)
        card(d, [x, y0, x + cw, y0 + ch])
        # illustration strip
        ix0, iy0, ix1, iy1 = x + 10, y0 + 10, x + cw - 10, y0 + 96
        if i == 0:
            d.rounded_rectangle([ix0, iy0, ix1, iy1], radius=8, fill=(30, 80, 110))
            # globe
            cx, cy, r = ix0 + 70, (iy0 + iy1) // 2, 32
            d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(90, 170, 220), outline=LIGHT, width=2)
            d.arc([cx - r, cy - r, cx + r, cy + r], 0, 360, fill=LIGHT, width=1)
            d.line([cx - r, cy, cx + r, cy], fill=LIGHT, width=1)
            d.ellipse([cx - 12, cy - r, cx + 12, cy + r], outline=LIGHT, width=1)
            # leaf + thermometer bar
            d.ellipse([cx + 55, cy - 18, cx + 95, cy + 12], fill=(70, 170, 90))
            d.rectangle([cx + 55, cy + 20, cx + 200, cy + 30], fill=(240, 120, 60))
            d.text((cx + 55, cy - 34), "COP31", font=font(22, bold=True), fill=LIGHT)
            d.text((cx + 110, cy - 8), "ANTALYA", font=font(13, bold=True), fill=LIGHT)
        elif i == 1:
            d.rounded_rectangle([ix0, iy0, ix1, iy1], radius=8, fill=(120, 30, 40))
            # skyline
            for j, (bw, bh) in enumerate([(34, 52), (26, 66), (40, 44), (28, 60), (36, 50)]):
                bx = ix0 + 18 + j * 46
                d.rectangle([bx, iy1 - 8 - bh, bx + bw, iy1 - 8], fill=(230, 220, 200))
                for wy in range(iy1 - 8 - bh + 6, iy1 - 16, 12):
                    d.rectangle([bx + 5, wy, bx + 11, wy + 6], fill=(90, 90, 90))
                    d.rectangle([bx + 17, wy, bx + 23, wy + 6], fill=(90, 90, 90))
            # ballot box
            d.rectangle([ix1 - 62, iy0 + 18, ix1 - 14, iy1 - 14], fill=LIGHT, outline=INK, width=2)
            d.rectangle([ix1 - 52, iy0 + 26, ix1 - 24, iy0 + 32], fill=INK)
            d.text((ix1 - 58, iy0 + 40), "VOTE", font=font(13, bold=True), fill=RED)
        else:
            d.rounded_rectangle([ix0, iy0, ix1, iy1], radius=8, fill=(25, 25, 35))
            # chequered strip
            for r in range(2):
                for c in range(14):
                    col = LIGHT if (r + c) % 2 == 0 else (25, 25, 35)
                    d.rectangle([ix0 + c * 21, iy0 + r * 10, ix0 + c * 21 + 21, iy0 + r * 10 + 10], fill=col)
            # simple F1 car
            cy = iy1 - 30
            d.polygon([(ix0 + 40, cy), (ix0 + 110, cy - 16), (ix0 + 190, cy - 16), (ix0 + 240, cy)], fill=RED)
            d.rectangle([ix0 + 120, cy - 28, ix0 + 170, cy - 16], fill=(60, 60, 80))
            d.rectangle([ix0 + 232, cy - 30, ix0 + 248, cy], fill=RED)
            for wx in (ix0 + 70, ix0 + 200):
                d.ellipse([wx - 14, cy - 6, wx + 14, cy + 22], fill=(15, 15, 15), outline=LIGHT, width=2)
            d.text((ix0 + 120, iy0 + 30), "F1  •  50 LAPS", font=font(15, bold=True), fill=LIGHT)
        d.text((x + 12, y0 + 104), kicker, font=font(11, bold=True), fill=TEAL)
        yy = text_block(d, x + 12, y0 + 122, head, font(19, bold=True), INK, cw - 24, leading=23)
        text_block(d, x + 12, yy + 4, body, font(12), (45, 45, 45), cw - 24, leading=16)

    # ---------- World map + numbers ----------
    my0 = 398
    card(d, [16, my0, 640, my0 + 168])
    d.text((28, my0 + 8), "WHERE — numbered stories on the map", font=font(13, bold=True), fill=NAVY)
    # simplified continents (polygons in map box)
    ox, oy = 28, my0 + 32
    land = (170, 195, 165)
    # North America
    d.polygon([(ox+8,oy+18),(ox+70,oy+6),(ox+120,oy+14),(ox+130,oy+34),(ox+105,oy+52),(ox+80,oy+48),(ox+60,oy+62),(ox+30,oy+52),(ox+10,oy+36)], fill=land)
    # South America
    d.polygon([(ox+95,oy+68),(ox+125,oy+64),(ox+138,oy+82),(ox+125,oy+112),(ox+108,oy+118),(ox+98,oy+92)], fill=land)
    # Europe
    d.polygon([(ox+215,oy+12),(ox+255,oy+8),(ox+268,oy+24),(ox+250,oy+38),(ox+225,oy+36),(ox+212,oy+24)], fill=land)
    # Africa
    d.polygon([(ox+218,oy+44),(ox+262,oy+42),(ox+275,oy+64),(ox+262,oy+100),(ox+238,oy+108),(ox+222,oy+78)], fill=land)
    # Asia
    d.polygon([(ox+268,oy+10),(ox+360,oy+6),(ox+400,oy+20),(ox+390,oy+44),(ox+350,oy+52),(ox+330,oy+72),(ox+305,oy+60),(ox+285,oy+36)], fill=land)
    # SE Asia islands + Australia
    d.polygon([(ox+335,oy+78),(ox+365,oy+76),(ox+368,oy+88),(ox+340,oy+90)], fill=land)
    d.polygon([(ox+380,oy+88),(ox+425,oy+84),(ox+432,oy+104),(ox+400,oy+112),(ox+382,oy+102)], fill=land)
    # pins: 1 Antalya, 2 Hong Kong, 3 Las Vegas, 4 Canberra, 5 Brussels, 6 Paris, 7 Peru, 8 Mexico, 9 Washington
    pin(d, ox + 278, oy + 30, 1)
    pin(d, ox + 372, oy + 48, 2)
    pin(d, ox + 52, oy + 34, 3)
    pin(d, ox + 414, oy + 102, 4, fill=TEAL)
    pin(d, ox + 244, oy + 16, 5, fill=TEAL)
    pin(d, ox + 222, oy + 34, 6, fill=TEAL)
    pin(d, ox + 108, oy + 84, 7, fill=(120, 80, 20))
    pin(d, ox + 62, oy + 50, 8, fill=(120, 80, 20))
    pin(d, ox + 100, oy + 30, 9, fill=(120, 80, 20))
    d.text((ox, oy + 122), "1 Antalya  2 Hong Kong  3 Las Vegas  4 Canberra  5 Brussels  6 Paris  7 Junín (Peru)  8 Sinaloa  9 Washington", font=font(10), fill=GREY)

    # numbers panel
    card(d, [652, my0, 1008, my0 + 168], fill=PALE_GOLD)
    d.text((664, my0 + 8), "DAY IN NUMBERS", font=font(13, bold=True), fill=NAVY)
    nums = [
        ("856 / 723", "Hong Kong candidates / seats today"),
        ("03:00 → 06:00 GMT", "COP31 objection deadline → approval session"),
        ("50 laps", "Las Vegas GP, Sun 04:00 GMT"),
        ("152 homes", "uninhabitable after Peru M6.7 (INDECI, Sat)"),
        ("−5.28%", "Nasdaq Friday close; markets shut Sunday"),
    ]
    yy = my0 + 30
    for big, small in nums:
        d.text((664, yy), big, font=font(14, bold=True), fill=RED)
        d.text((664, yy + 16), small, font=font(10), fill=INK)
        yy += 27

    # ---------- Region strip ----------
    ry = 578
    regions = [
        ("AMERICAS", "F1 overnight; Mexico + Peru fallout"),
        ("EUROPE", "France protests (Sat); EU trade; football"),
        ("AFRICA", "No new verified event by 02:30 GMT"),
        ("MIDDLE EAST", "No new verified event by 02:30 GMT"),
        ("ASIA-PACIFIC", "HK vote; 3 small quakes Sun local"),
        ("OCEANIA", "AUKUS reply Sun; Shield starts"),
        ("WORLD", "COP31 overtime into Sunday"),
    ]
    rw = (W - 32) / 7
    for i, (name, desc) in enumerate(regions):
        x = 16 + i * rw
        d.rounded_rectangle([x + 2, ry, x + rw - 2, ry + 62], radius=8, fill=PALE_TEAL if i % 2 == 0 else PALE, outline=(180, 190, 185), width=1)
        d.text((x + 8, ry + 6), name, font=font(10, bold=True), fill=NAVY)
        text_block(d, x + 8, ry + 22, desc, font(10), INK, rw - 16, leading=13)

    # ---------- Mid cards + briefs (continuous numbering 4-15) ----------
    by = 652
    d.text((16, by), "MORE OF THE DAY — numbered to the map where pinned", font=font(13, bold=True), fill=NAVY)
    items_left = [
        ("4  OCEANIA — CANBERRA", "Marles: AUKUS critics 'wrong'",
         "Defence Minister Marles Sunday rejected US CBO warning on Virginia-class sales. A$368bn over 30 years. [Reuters, Sun]"),
        ("5  EUROPE–ASIA — BRUSSELS (SAT)", "EU–Indonesia trade deal signed",
         "CEPA + Investment deal signed Saturday after 10 years. 98.5% of tariffs to go; in force targeted 2027. [EC; Reuters]"),
        ("6  EUROPE — FRANCE (SAT)", "Fourth weekend of protests",
         "Cost-of-living marches Saturday: Interior ~146,000; unions 250,000. Counts reported Sunday."),
    ]
    items_mid = [
        ("7  AMERICAS — PERU (AFTERMATH)", "M6.7 toll: 152 homes uninhabitable",
         "Friday quake near Carhuamayo. INDECI Sat: 1 dead, 16 injured, 152 uninhabitable. [INDECI; USGS]"),
        ("8  AMERICAS — MEXICO (FRI/SAT)", "'Chapo Isidro' captured",
         "FBI Ten Most Wanted Meza Flores seized in Guasave Fri night. Officials: 4 soldiers, 7 gunmen killed. [Reuters]"),
        ("9  AMERICAS — USA (REPORTED SAT)", "FBI probes apparent NCIC hack",
         "Apparent NCIC breach reported Fri, confirmed to AP Sat. Scope unclear. [AP; CNN]"),
    ]
    briefs = [
        "10  MYANMAR M4.1 Sun 02:35 IST [NCS].  11  PHILIPPINES M4.6 Sarangani Sun 08:23, no damage expected [PHIVOLCS].  12  INDONESIA M4.6 near Abepura Sun local [USGS].",
        "13  FOOTBALL TODAY (GMT): Juventus–Venezia 11:30 • Barcelona–Villarreal 13:00 • Hull–Brighton 14:00 • Liverpool–Man Utd 16:30 • Atalanta–Inter 19:45. Scheduled — no scores yet.",
        "14  MARKETS shut Sunday. Friday: Dow 48,147 (−1.93%), S&P 6,910 (−3.70%), Nasdaq 22,618 (−5.28%).  15  CRICKET: NSW v Queensland starts today, SCG.",
    ]
    colw = 320
    for col, items in enumerate([items_left, items_mid]):
        x = 16 + col * (colw + 12)
        yy = by + 22
        for kicker, head, body in items:
            card(d, [x, yy, x + colw, yy + 74])
            d.text((x + 10, yy + 5), kicker, font=font(10, bold=True), fill=TEAL)
            y2 = text_block(d, x + 10, yy + 20, head, font(13, bold=True), INK, colw - 20, leading=16)
            text_block(d, x + 10, y2 + 1, body, font(10), (45, 45, 45), colw - 20, leading=13)
            yy += 80
    # briefs column (right)
    x = 16 + 2 * (colw + 12)
    card(d, [x, by + 22, x + colw, by + 22 + 234], fill=(255, 255, 255))
    d.text((x + 10, by + 28), "BRIEFS 10–15", font=font(11, bold=True), fill=TEAL)
    yy = by + 48
    for b in briefs:
        yy = text_block(d, x + 10, yy, b, font(10), INK, colw - 20, leading=14)
        yy += 7

    # ---------- Date check + footer ----------
    fy = 964
    d.rounded_rectangle([16, fy - 52, 1008, fy + 18], radius=8, fill=(240, 230, 225), outline=(200, 170, 160), width=1)
    d.text((26, fy - 46), "DATE CHECK — big stories deliberately NOT dated today:", font=font(11, bold=True), fill=RED)
    d.text((26, fy - 30), "Nvidia CEO exit 11 Nov • Lagarde exit announced 29 Oct • Gaza aid statement 15–16 Nov • Norway oil ruling 13 Nov • Ghana notes unveiled 12 Nov", font=font(10), fill=INK)
    d.text((26, fy - 16), "Eisenkot mandate 7–8 Nov • Kyiv bridges barrage 20 Nov • Al-Shabaab ambush 26 Oct • Kenya Ebola discharge 11 Nov • Timor-Leste M6.8 21 Nov", font=font(10), fill=INK)
    d.text((16, 992), "Sources: Reuters • AP • HK Registration & Electoral Office • China Daily Asia • European Commission • Formula1.com • USGS • PHIVOLCS • NCS • INDECI  |  Made for make.fun news-image-20261122", font=font(10), fill=GREY)

    img.save(OUT, format="PNG", optimize=False)
    print(f"wrote {OUT} {OUT.stat().st_size} bytes")


if __name__ == "__main__":
    main()
