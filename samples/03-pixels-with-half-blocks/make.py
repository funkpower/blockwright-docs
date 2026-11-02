#!/usr/bin/env python3
"""Write tutorial 03's samples: python3 -I samples/03-pixels-with-half-blocks/make.py

Every canvas is drawn the way Blockwright's half-block tools draw it
(scripts/ansi.py): each call is one use of a tool, with the same pixels the
tool plots for that drag. Pixel positions are (column, pixel row); a cell row
holds pixel rows 2y and 2y + 1. The step files are the canvas each step of
"Do it" leaves; final.ans is the last of them.
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "scripts"))
from ansi import Canvas  # noqa: E402

BLACK, BLUE, GREEN, CYAN, RED, MAGENTA, BROWN, GREY = range(8)
DARK_GREY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_CYAN, LIGHT_RED, LIGHT_MAGENTA, YELLOW, WHITE = range(8, 16)
W, H = 40, 12
# The smoke's path: up from the chimney, then drifting right. Step 9 draws
# it as one short brush drag between each point and the next.
SMOKE = [(16, 4), (17, 2), (19, 1), (21, 1), (23, 0)]
# Single-pixel stars, each four or more pixels off every shape.
STARS = [(3, 1), (11, 1), (1, 7), (24, 7), (29, 15), (38, 14)]


def save(c, name, title):
    c.save(HERE / name, title=title)


# The idea: how one cell shows two pixels. Each pair is a top and a bottom
# colour, the top plotted first, with a blank cell between pairs.
PAIRS = [(BLUE, BLUE), (YELLOW, YELLOW), (YELLOW, BLUE), (BLUE, YELLOW), (WHITE, YELLOW)]


def halves(c):
    for i, (top, bottom) in enumerate(PAIRS):
        if top == bottom:
            c.plot([(2 * i, 0), (2 * i, 1)], top)
        else:
            c.plot([(2 * i, 0)], top)
            c.plot([(2 * i, 1)], bottom)
    return c


c = halves(Canvas(2 * len(PAIRS) - 1, 1))
save(c, "halves.ans", "Two pixels a cell")

# The same five pairs with iCE colours off: the last cell can't hold two
# bright colours, so the yellow painted under the white comes out brown.
c = halves(Canvas(2 * len(PAIRS) - 1, 1, ice=False))
save(c, "halves-no-ice.ans", "Two pixels a cell, iCE off")


def smoke(c, connected=4):
    for a, b in zip(SMOKE, SMOKE[1:]):
        c.pencil([a, b], GREY, connected=connected)


def scene(stop=None):
    """The night scene, step by step; returns the canvas after step `stop`."""
    c = Canvas(W, H)
    steps = [
        # 1. Fill: the sky.
        lambda: c.fill_pixels(0, 0, BLUE),
        # 2. Rectangle, filled: the ground, on whole cell rows.
        lambda: c.rect(0, 20, W - 1, 2 * H - 1, GREEN, filled=True),
        # 3. Ellipse, filled: the moon, 8 pixels across.
        lambda: c.ellipse(29, 2, 36, 9, YELLOW, filled=True),
        # 4. Rectangle, filled: the walls.
        lambda: c.rect(6, 12, 17, 19, WHITE, filled=True),
        # 5. Line: the roof's three sides.
        lambda: (c.line(5, 11, 11, 5, RED), c.line(12, 5, 18, 11, RED), c.line(5, 11, 18, 11, RED)),
        # 6. Fill: inside the roof.
        lambda: c.fill_pixels(11, 8, RED),
        # 7. Eyedropper on the moon, then the window (filled) and the door.
        lambda: (c.rect(8, 13, 11, 16, c.pick(32, 5), filled=True), c.rect(13, 15, 15, 19, BROWN, filled=True)),
        # 8. Rectangle, filled: the chimney; Half-Block Brush, 4-connected:
        # the smoke, one drag from each point of its path to the next.
        lambda: (c.rect(15, 5, 16, 8, DARK_GREY, filled=True), smoke(c)),
        # 9. Half-Block Brush: stars, a click (one pixel) each.
        lambda: [c.pencil([s], WHITE) for s in STARS],
    ]
    for step in steps[:stop]:
        step()
    return c


for n in range(1, 10):
    save(scene(stop=n), f"step-{n:02}.ans", f"Night house, step {n}")
save(scene(), "final.ans", "Night house")
# The finished scene with View > iCE Colours turned off: the same cells, each
# bright background shown as its dark colour.
c = scene()
c.ice = False
save(c, "no-ice.ans", "Night house, iCE off")

# Check it: a line of smoke drawn 8-connected and 4-connected.
c = Canvas(26, 5, bg=BLUE)
c.pencil([(1, 8), (11, 0)], GREY, connected=8)
c.pencil([(14, 8), (24, 0)], GREY, connected=4)
save(c, "diagonal.ans", "8-connected and 4-connected")

# Check it: a one-pixel line through shade cells leaves the other half of
# each cell it cuts in the shade's background; a line two pixels deep on a
# whole cell row doesn't.
c = Canvas(26, 4)
c.fill(0, 0, 11, 3, "▒", GREY, BLUE)
c.fill(14, 0, 25, 3, "▒", GREY, BLUE)
c.line(0, 3, 11, 3, YELLOW)
c.rect(14, 2, 25, 3, YELLOW, filled=True)
save(c, "speck.ans", "Fallback specks")

# Check it: a word, then a moon drawn over it.
c = Canvas(14, 5, bg=BLUE)
c.text(2, 2, "MOON", WHITE, BLUE)
c.ellipse(5, 1, 11, 7, YELLOW, filled=True)
save(c, "text.ans", "A pixel over a letter")

# Check it: filled ellipses from 3 to 8 pixels across, each over its width.
c = Canvas(40, 6, bg=BLUE)
x = 1
for size in range(3, 9):
    c.ellipse(x, 1, x + size - 1, size, YELLOW, filled=True)
    c.text(x + (size - 1) // 2, 5, str(size), WHITE, BLUE)
    x += size + 1
save(c, "circles.ans", "Small ellipses")

# Check it: a star two pixels off the moon's rim, with one pixel of sky
# between, and one well clear of it.
c = Canvas(32, 5, bg=BLUE)
c.ellipse(2, 1, 9, 8, YELLOW, filled=True)
c.pencil([(11, 2)], WHITE)
c.ellipse(18, 1, 25, 8, YELLOW, filled=True)
c.pencil([(30, 2)], WHITE)
save(c, "star-clear.ans", "Stars off the moon")

# Check it: a roof whose right side stops two pixels short, filled.
c = scene(stop=4)
c.line(5, 11, 11, 5, RED)
c.line(12, 5, 16, 9, RED)
c.line(5, 11, 18, 11, RED)
c.fill_pixels(11, 8, RED)
save(c, "leak.ans", "A fill through a gap")

# Try it: the night house with three faults to find. The smoke is drawn
# 8-connected, the star from 24, 7 sits beside the moon at 27, 5, and the
# bush is a 3-pixel ellipse.
TRY_STARS = [(27, 5) if s == (24, 7) else s for s in STARS]


def try_scene():
    c = scene(stop=7)
    c.rect(15, 5, 16, 8, DARK_GREY, filled=True)
    smoke(c, connected=8)
    for s in TRY_STARS:
        c.pencil([s], WHITE)
    c.ellipse(20, 17, 22, 19, LIGHT_GREEN, filled=True)
    return c


save(try_scene(), "try.ans", "Night house, three faults")
