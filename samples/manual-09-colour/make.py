#!/usr/bin/env python3
"""Write the colour page's samples: python3 -I samples/manual-09-colour/make.py

palette.ans is the 16 colours as the Palette dock lays them out, two rows of
eight, each bright colour under its dark one. ice-on.ans and ice-off.ans are
the same cells saved with iCE colours on and off: a background from 8 to 15
shows as itself with iCE on; with it off the cell blinks and shows the dark
colour (the background minus 8) in its visible phase.
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "scripts"))
from ansi import Canvas  # noqa: E402

BLACK, BLUE, GREEN, CYAN, RED, MAGENTA, BROWN, GREY = range(8)
DARK_GREY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_CYAN, LIGHT_RED, LIGHT_MAGENTA, YELLOW, WHITE = range(8, 16)

# The palette: a swatch and its number for each colour.
c = Canvas(40, 6)
for i in range(16):
    x, y = (i % 8) * 5, (i // 8) * 3
    c.fill(x, y, x + 3, y + 1, " ", GREY, i)
    c.text(x, y + 2, f"{i:>2}", GREY, BLACK)
c.save(HERE / "palette.ans", title="The 16 colours")

# The bright backgrounds, each with a glyph on it, and a line of text on a
# bright background.
c = Canvas(40, 6)
for i in range(8):
    x = i * 5
    c.fill(x, 0, x + 3, 1, " ", GREY, 8 + i)
    c.put(x + 1, 0, "♥", BLACK if i else WHITE, 8 + i)
    c.text(x, 2, f"{8 + i:>2}", GREY, BLACK)
c.text(0, 4, " BLACK ON YELLOW ", BLACK, YELLOW)
c.text(19, 4, " WHITE ON LIGHT RED ", WHITE, LIGHT_RED)
c.save(HERE / "ice-on.ans", title="Bright backgrounds, iCE on", ice=True)
c.save(HERE / "ice-off.ans", title="Bright backgrounds, iCE off", ice=False)
