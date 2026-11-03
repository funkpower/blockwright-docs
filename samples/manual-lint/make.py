#!/usr/bin/env python3
"""Write the lint page's samples: python3 -I samples/manual-lint/make.py

One small canvas per finding the lint reports, each drawn so that the lint
finds that fault in it, and a clean one to compare.
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "scripts"))
from ansi import Canvas  # noqa: E402

BLACK, BLUE, GREEN, CYAN, RED, MAGENTA, BROWN, GREY = range(8)
DARK_GREY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_CYAN, LIGHT_RED, LIGHT_MAGENTA, YELLOW, WHITE = range(8, 16)
UPPER, LOWER, FULL = "▀", "▄", "█"
LIGHT, MEDIUM, DARK = "░", "▒", "▓"
W, H = 24, 6


def save(c, name, title):
    c.save(HERE / name, title=title)


def field(bg, w=W, h=H):
    c = Canvas(w, h)
    c.fill(0, 0, w - 1, h - 1, " ", GREY, bg)
    return c


# A steel gradient, dark grey to white, every rung two cells wide.
STEEL = [(" ", GREY, DARK_GREY), (LIGHT, GREY, DARK_GREY), (MEDIUM, GREY, DARK_GREY),
         (DARK, GREY, DARK_GREY), (" ", GREY, GREY), (LIGHT, WHITE, GREY),
         (MEDIUM, WHITE, GREY), (DARK, WHITE, GREY), (" ", GREY, WHITE)]


def bands(c, rungs, widths, x=0, y0=0, y1=H - 1):
    for (ch, fg, bg), n in zip(rungs, widths):
        c.fill(x, y0, x + n - 1, y1, ch, fg, bg)
        x += n
    return x


# Clean: a steel gradient, each rung two or three cells wide.
c = field(DARK_GREY)
bands(c, STEEL, [3, 3, 2, 3, 2, 3, 2, 3, 3])
save(c, "clean.ans", "A clean steel gradient")

# wide-rung: the same gradient with its first ░ rung six cells wide.
c = field(DARK_GREY)
bands(c, STEEL, [2, 6, 2, 2, 2, 2, 2, 2, 4])
save(c, "wide-rung.ans", "A rung six cells wide")

# rung-skip: dark grey, grey and white side by side, no shades between.
c = field(DARK_GREY, W, 3)
bands(c, [STEEL[0], STEEL[4], STEEL[8]], [8, 8, 8], y1=2)
save(c, "rung-skip.ans", "Three solid rungs, no shades")

# non-neighbour-shade: a ▒ of yellow on blue, which no ramp steps between.
c = field(BLUE)
c.fill(10, 2, 12, 2, MEDIUM, YELLOW, BLUE)
save(c, "non-neighbour-shade.ans", "Yellow shaded straight onto blue")

# speckle: one grey cell in a dark grey field.
c = field(DARK_GREY)
c.put(11, 2, " ", GREY, GREY)
save(c, "speckle.ans", "A speck of grey")

# fallback-speck: a light cyan shape cut into fire's ░ (light red on red);
# its edge cells keep the shade's light red underneath.
c = Canvas(W, H)
c.fill(0, 0, W - 1, H - 1, LIGHT, LIGHT_RED, RED)
c.fill(8, 0, 15, 1, FULL, LIGHT_CYAN, BLACK)
c.fill(8, 2, 15, 2, UPPER, LIGHT_CYAN, LIGHT_RED)
c.fill(0, 4, W - 1, 5, MEDIUM, LIGHT_RED, RED)
save(c, "fallback-speck.ans", "A shape cut into a shade")

# A craft pair: fire's red shaded straight to yellow.
c = field(RED)
c.fill(8, 0, 15, H - 1, MEDIUM, YELLOW, RED)
c.fill(16, 0, W - 1, H - 1, " ", GREY, YELLOW)
save(c, "craft-pair.ans", "Red shaded to yellow")

# one-glyph: a whole field shaded in ▒ alone.
c = field(DARK_GREY)
c.fill(0, 0, W - 1, H - 1, MEDIUM, GREY, DARK_GREY)
save(c, "one-glyph.ans", "Shaded in one glyph")

# noise: a light red field with a quarter of its pixels scattered red.
c = field(LIGHT_RED)
for y in range(H):
    for x in range(W):
        if (x * 7 + y * 3) % 4 == 0:
            c.put(x, y, UPPER if (x + y) % 2 else LOWER, RED, LIGHT_RED)
save(c, "noise.ans", "Scattered pixels")

# lone-pixel: one light red pixel in a red field.
c = field(RED)
c.put(11, 2, UPPER, LIGHT_RED, RED)
save(c, "lone-pixel.ans", "A lone glint")

# gap: a white line across a blue field, broken at one cell.
c = field(BLUE)
c.fill(2, 2, 21, 2, FULL, WHITE, BLUE)
c.put(12, 2, " ", GREY, BLUE)
save(c, "gap.ans", "A broken line")

# merge: a word with one letter in its own background colour.
c = field(BLUE)
c.text(8, 2, "FUNK", WHITE, BLUE)
c.put(10, 2, "N", BLUE, BLUE)
save(c, "merge.ans", "A letter that can't be seen")

# dotted-diagonal: a 1 px yellow diagonal, its pixels touching at corners.
c = field(BLUE, 40, 8)
for x in range(4, 14):
    py = x - 4
    c.put(x, py // 2, UPPER if py % 2 == 0 else LOWER, YELLOW, BLUE)
save(c, "dotted-diagonal.ans", "A dotted diagonal")

# flat: a plain red block (the rule runs only with a box).
c = field(BLUE)
c.fill(4, 1, 19, 4, " ", GREY, RED)
save(c, "flat.ans", "A flat block")

# trailing-black: a blue panel whose third row stops short, and a fourth
# row left all black.
c = field(BLUE)
c.fill(14, 2, W - 1, 2, " ", GREY, BLACK)
c.fill(0, 3, W - 1, 3, " ", GREY, BLACK)
save(c, "trailing-black.ans", "Black to the edge")

# blank-edge-rows: a blue panel with black rows above and below it.
c = Canvas(W, H)
c.fill(0, 2, W - 1, 3, " ", GREY, BLUE)
save(c, "blank-edge-rows.ans", "Blank rows above and below")
