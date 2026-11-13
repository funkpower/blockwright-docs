#!/usr/bin/env python3
"""Write the keyboard mode page's samples: python3 -I samples/manual-03-keyboard-mode/make.py

glyph-sets.ans is the 16 F-key sets as Blockwright has them (core/src/glyph_sets.cpp
at 30c37b9), set 6, the default, on blue. typed.ans is a sign typed in keyboard
mode: the frame with set 2's F-keys, the bar with set 6's, the word as letters.
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "scripts"))
from ansi import Canvas  # noqa: E402

BLACK, BLUE, GREEN, CYAN, RED, MAGENTA, BROWN, GREY = range(8)
DARK_GREY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_CYAN, LIGHT_RED, LIGHT_MAGENTA, YELLOW, WHITE = range(8, 16)

# F1 to F10 of each set.
SETS = [
    "┌┐└┘─│├┤┴┬",
    "╔╗╚╝═║╠╣╩╦",
    "╒╕╘╛═│╞╡╧╤",
    "╓╖╙╜─║╟╢╨╥",
    "┼╬╪╫ΦΦ¢£Ö∩",
    "░▒▓█▀▄▌▐■·",
    "☺☻♥♦♣♠≡♫☼ ",
    "↑↓▲▼►◄↕↔¶§",
    "«»≥≤⌐¬²÷½¼",
    "π±⌠⌡Ω¥Σ°√ⁿ",
    "αßΓσµτδ∞φε",
    "ÇçÑñÿƒ≈∙¡¿",
    "âäàáªåÄÅæÆ",
    "êëèéÉîïìí₧",
    "ôöòóºûüùúÜ",
    "/\\(){}[]`'",
]
DEFAULT = 6

# The sets: a row each under the F-key names, three columns a key so the
# picture fits the page at 2x, and a blank row between, so the box-drawing
# glyphs of one set don't join the next.
c = Canvas(36, 33)
c.text(0, 0, "Set", GREY, BLACK)
for k in range(10):
    c.text(6 + k * 3, 0, f"F{k + 1}", DARK_GREY, BLACK)
for i, glyphs in enumerate(SETS):
    y = i * 2 + 2
    bg = BLUE if i + 1 == DEFAULT else BLACK
    c.fill(0, y, 35, y, " ", GREY, bg)
    c.text(0, y, f"{i + 1:>3}", GREY, bg)
    for k, ch in enumerate(glyphs):
        c.put(6 + k * 3, y, ch, WHITE, bg)
c.save(HERE / "glyph-sets.ans", title="The F-key glyph sets")

# A sign typed in keyboard mode.
c = Canvas(20, 4)
c.text(0, 0, "╔" + "═" * 18 + "╗", LIGHT_CYAN, BLACK)
c.put(0, 1, "║", LIGHT_CYAN, BLACK)
c.text(1, 1, "    NOW  OPEN     ", YELLOW, BLACK)
c.put(19, 1, "║", LIGHT_CYAN, BLACK)
c.put(0, 2, "║", LIGHT_CYAN, BLACK)
c.text(1, 2, "░▒▓" + "█" * 12 + "▓▒░", LIGHT_RED, BLACK)
c.put(19, 2, "║", LIGHT_CYAN, BLACK)
c.text(0, 3, "╚" + "═" * 18 + "╝", LIGHT_CYAN, BLACK)
c.save(HERE / "typed.ans", title="A sign typed with the F-keys")
