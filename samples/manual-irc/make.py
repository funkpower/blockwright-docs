#!/usr/bin/env python3
"""Write the IRC page's samples: python3 -I samples/manual-irc/make.py

budget.ans has rows that cost a few bytes and rows that cost hundreds;
edges.ans has the black margins and trailing black that IRC trims.
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


def save(c, name, title):
    c.save(HERE / name, title=title)


# budget.ans, 80 columns. Row by row: one colour; fire's nine rungs in long
# bands; the same rungs two cells each, red to yellow and round again; the
# rungs in a scattered order, one a cell; half blocks in four colours on four
# backgrounds, changing every cell; and half blocks in one colour pair.
W = 80
c = Canvas(W, 6)
c.fill(0, 0, W - 1, 0, " ", GREY, BLUE)
fire = [(" ", GREY, RED), (LIGHT, LIGHT_RED, RED), (MEDIUM, LIGHT_RED, RED), (DARK, LIGHT_RED, RED),
        (" ", GREY, LIGHT_RED), (LIGHT, YELLOW, LIGHT_RED), (MEDIUM, YELLOW, LIGHT_RED),
        (DARK, YELLOW, LIGHT_RED), (" ", GREY, YELLOW)]
for i, (ch, fg, bg) in enumerate(fire):
    x0 = i * W // len(fire)
    x1 = (i + 1) * W // len(fire) - 1
    c.fill(x0, 1, x1, 1, ch, fg, bg)
for x in range(W):
    ch, fg, bg = fire[(x // 2) % len(fire)]
    c.put(x, 2, ch, fg, bg)
for x in range(W):
    ch, fg, bg = fire[(x * 5) % len(fire)]
    c.put(x, 3, ch, fg, bg)
for x in range(W):
    c.put(x, 4, UPPER if x % 2 else LOWER, [LIGHT_GREEN, LIGHT_CYAN, YELLOW, LIGHT_MAGENTA][x % 4],
          [BLUE, MAGENTA, RED, GREEN][(x // 3) % 4])
for x in range(W):
    c.put(x, 5, UPPER if x % 2 else LOWER, LIGHT_GREEN, BLUE)
save(c, "budget.ans", "Cheap rows and dear rows")

# edges.ans: a black margin row above and below, a panel whose right edge
# is black, and a row in the middle left black.
c = Canvas(32, 7)
c.fill(2, 1, 29, 5, " ", GREY, BLUE)
c.fill(2, 3, 29, 3, " ", GREY, BLACK)
c.text(4, 2, "funkpower", YELLOW, BLUE)
c.text(4, 4, "on irc", WHITE, BLUE)
save(c, "edges.ans", "Margins and trailing black")
