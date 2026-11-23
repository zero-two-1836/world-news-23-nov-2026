#!/usr/bin/env python3
"""Draw the front page for Monday, 23 November 2026.

A one-image newspaper: a masthead, one hero story and nine short
panels, drawn with Pillow primitives only. Run it and it writes
entry.png next to this file. The drawing is fully deterministic:
same code, same bytes, every run.

Layout budget (1024 px tall): masthead to y=100, dateline band to
156, hero to 428, story grid 444..960 in three 172 px rows, footer
below 968. Every text block is sized to fit its box at these sizes.
"""

from PIL import Image, ImageDraw, ImageFont

W = 1024
H = 1024

PAPER = (248, 244, 233)
INK = (20, 18, 14)
ACCENT = (163, 22, 33)
SOFT = (92, 86, 74)
RULE = (20, 18, 14)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def centered(draw, cx, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


# ---------------------------------------------------------------- icons
# Each icon draws inside a 46x46 box whose top-left corner is (x, y).

def icon_missile(d, x, y):
    d.polygon([(x + 34, y + 4), (x + 42, y + 20), (x + 26, y + 16)], fill=INK)
    d.line([(x + 28, y + 18), (x + 10, y + 36)], fill=ACCENT, width=4)
    d.line([(x + 34, y + 22), (x + 18, y + 38)], fill=ACCENT, width=3)
    d.line([(x + 22, y + 26), (x + 8, y + 40)], fill=ACCENT, width=3)


def icon_building(d, x, y):
    d.rectangle([x + 10, y + 6, x + 36, y + 42], outline=INK, width=3)
    for r in range(3):
        for c in range(2):
            d.rectangle([x + 16 + c * 10, y + 12 + r * 9,
                         x + 21 + c * 10, y + 17 + r * 9], fill=INK)
    d.line([(x + 24, y + 6), (x + 19, y + 20), (x + 27, y + 30),
            (x + 22, y + 42)], fill=ACCENT, width=3)


def icon_ship(d, x, y):
    d.polygon([(x + 4, y + 28), (x + 42, y + 28), (x + 36, y + 40),
               (x + 10, y + 40)], fill=INK)
    d.rectangle([x + 18, y + 16, x + 30, y + 28], fill=INK)
    d.line([(x + 24, y + 6), (x + 24, y + 16)], fill=INK, width=3)
    for i in range(3):
        d.arc([x + 2 + i * 14, y + 38, x + 14 + i * 14, y + 48],
              0, 180, fill=ACCENT, width=3)


def icon_talks(d, x, y):
    d.rounded_rectangle([x + 4, y + 8, x + 26, y + 26], 5, outline=INK, width=3)
    d.polygon([(x + 10, y + 26), (x + 10, y + 34), (x + 18, y + 26)], fill=INK)
    d.rounded_rectangle([x + 20, y + 18, x + 42, y + 36], 5, outline=ACCENT, width=3)
    d.polygon([(x + 36, y + 36), (x + 36, y + 44), (x + 28, y + 36)], fill=ACCENT)


def icon_planet(d, x, y):
    d.ellipse([x + 12, y + 12, x + 36, y + 36], outline=INK, width=3)
    d.ellipse([x + 17, y + 17, x + 23, y + 23], fill=SOFT)
    d.ellipse([x + 26, y + 26, x + 31, y + 31], fill=SOFT)
    d.arc([x + 2, y + 4, x + 44, y + 44], 200, 320, fill=ACCENT, width=3)
    d.ellipse([x + 38, y + 6, x + 43, y + 11], fill=ACCENT)


def icon_ball(d, x, y):
    d.ellipse([x + 6, y + 6, x + 40, y + 40], outline=INK, width=3)
    d.polygon([(x + 23, y + 16), (x + 30, y + 21), (x + 27, y + 29),
               (x + 19, y + 29), (x + 16, y + 21)], fill=INK)
    d.line([(x + 23, y + 16), (x + 23, y + 7)], fill=INK, width=2)
    d.line([(x + 30, y + 21), (x + 38, y + 19)], fill=INK, width=2)
    d.line([(x + 19, y + 29), (x + 13, y + 35)], fill=INK, width=2)


def icon_cricket(d, x, y):
    d.polygon([(x + 26, y + 4), (x + 34, y + 8), (x + 18, y + 34),
               (x + 12, y + 30)], fill=INK)
    d.ellipse([x + 26, y + 32, x + 40, y + 46], fill=ACCENT)


def icon_book(d, x, y):
    d.polygon([(x + 23, y + 12), (x + 6, y + 6), (x + 6, y + 36),
               (x + 23, y + 41)], outline=INK, width=3)
    d.polygon([(x + 23, y + 12), (x + 40, y + 6), (x + 40, y + 36),
               (x + 23, y + 41)], outline=INK, width=3)
    d.line([(x + 23, y + 12), (x + 23, y + 41)], fill=ACCENT, width=3)


def icon_mountains(d, x, y):
    d.polygon([(x + 2, y + 40), (x + 16, y + 14), (x + 26, y + 28),
               (x + 32, y + 18), (x + 44, y + 40)], outline=INK, width=3)
    d.polygon([(x + 13, y + 19), (x + 16, y + 14), (x + 19, y + 19)],
              fill=ACCENT)


ICONS = {
    "missile": icon_missile,
    "building": icon_building,
    "ship": icon_ship,
    "talks": icon_talks,
    "planet": icon_planet,
    "ball": icon_ball,
    "cricket": icon_cricket,
    "book": icon_book,
    "mountains": icon_mountains,
}

PANELS = [
    ("MIDDLE EAST", "HOUTHI MISSILE INTERCEPTED",
     "Coalition downs a missile in the west; Houthis claim a "
     "refinery hit; two hurt in Bahrain.", "missile"),
    ("UKRAINE", "14 MISSING NEAR KYIV",
     "Russian drone flattens a five-storey block in Dymer. Nine "
     "evacuated; rescuers search rubble.", "building"),
    ("LIBYA", "WARSHIP HIT AT BENGHAZI",
     "Suspected Ukrainian sea drones strike a Russian warship; "
     "the UN urges a probe.", "ship"),
    ("ISRAEL", "UNITY TALKS END, NO DEAL",
     "Netanyahu's Likud and Eisenkot's Yashar break off talks on "
     "a joint government.", "talks"),
    ("SPACE", "PROBE ORBITS MERCURY",
     "Europe-Japan BepiColombo arrives after eight years; ESA "
     "checks a thruster glitch.", "planet"),
    ("FOOTBALL", "LIVERPOOL ROUT UNITED",
     "Ten-man Manchester United are hammered in Mauricio "
     "Pochettino's first match.", "ball"),
    ("CRICKET", "INDIA PRESS FOR TEST WIN",
     "New Zealand 157 for 4 at lunch on the final day as India "
     "chase victory.", "cricket"),
    ("SOUTH KOREA", "EDUCATION MINISTER QUITS",
     "Seoul's education chief resigns over the university "
     "entrance-exam row.", "book"),
    ("DIPLOMACY", "NEPAL PM MEETS MODI",
     "Balendra Shah holds talks in Delhi as India and Nepal "
     "prepare new pacts.", "mountains"),
]

HERO_TAG = "CLIMATE  |  ANTALYA, TURKEY"
HERO_HEAD = "COP31 CLIMATE TALKS COLLAPSE"
HERO_BODY = ("The summit ends with no agreement after the EU rejects "
             "a text with no fossil-fuel phase-out. UN chief Guterres "
             "calls himself \"deeply disappointed\".")


def draw_globe(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=INK, width=4)
    d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=INK, width=2)
    d.line([(cx - r, cy), (cx + r, cy)], fill=INK, width=2)
    d.line([(cx - r, cy - r // 2), (cx + r, cy - r // 2)], fill=INK, width=2)
    d.line([(cx - r, cy + r // 2), (cx + r, cy + r // 2)], fill=INK, width=2)
    d.line([(cx + r // 4, cy - r), (cx - r // 5, cy - r // 3),
            (cx + r // 3, cy + r // 4), (cx - r // 4, cy + r)],
           fill=ACCENT, width=5)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    centered(d, W // 2, 22, "THE WORLD TODAY", font(SERIF_BOLD, 60), INK)
    d.line([(36, 100), (W - 36, 100)], fill=RULE, width=3)

    # Dateline band
    d.rectangle([0, 108, W, 156], fill=INK)
    band_f = font(SANS_BOLD, 30)
    d.text((36, 117), "MONDAY, 23 NOVEMBER 2026", font=band_f,
           fill=(255, 255, 255))
    right = "ONE DAY - TEN STORIES"
    rw = d.textlength(right, font=band_f)
    d.text((W - 36 - rw, 117), right, font=band_f, fill=(255, 255, 255))

    # Hero story
    d.text((36, 170), HERO_TAG, font=font(SANS_BOLD, 22), fill=ACCENT)
    text_block(d, 36, 200, HERO_HEAD, font(SERIF_BOLD, 50), INK, 690, 57)
    text_block(d, 36, 322, HERO_BODY, font(SANS, 22), INK, 690, 29)
    draw_globe(d, 866, 282, 95)
    d.line([(36, 428), (W - 36, 428)], fill=RULE, width=3)

    # Story grid: 3 columns x 3 rows of 172 px
    grid_top = 444
    col_w = (W - 72) // 3
    row_h = 172
    for i, (tag, head, body, icon) in enumerate(PANELS):
        col = i % 3
        row = i // 3
        x0 = 36 + col * col_w
        y0 = grid_top + row * row_h
        if col:
            d.line([(x0 - 12, y0 + 4), (x0 - 12, y0 + row_h - 12)],
                   fill=SOFT, width=2)
        if row:
            d.line([(x0 + 2, y0 - 8), (x0 + col_w - 26, y0 - 8)],
                   fill=SOFT, width=2)
        ICONS[icon](d, x0 + 2, y0)
        d.text((x0 + 58, y0 + 10), tag, font=font(SANS_BOLD, 19),
               fill=ACCENT)
        text_block(d, x0 + 2, y0 + 46, head, font(SANS_BOLD, 25), INK,
                   col_w - 30, 30)
        text_block(d, x0 + 2, y0 + 108, body, font(SANS, 16), SOFT,
                   col_w - 30, 20)

    # Footer
    d.line([(36, 968), (W - 36, 968)], fill=RULE, width=3)
    centered(d, W // 2, 978,
             "Compiled from the day's wire reports: The Hindu - AFP - "
             "Reuters - ESA", font(SANS, 18), SOFT)

    return img


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    build().save(out, format="PNG")
    print("wrote", out)
