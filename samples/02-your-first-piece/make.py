#!/usr/bin/env python3
"""Write tutorial 02's samples: python3 -I samples/02-your-first-piece/make.py

The step files are the canvas each step of "Do it" leaves, typed in keyboard
mode: a glyph goes in the pen's colours and the cursor moves one cell right,
staying on the last column, where the next glyph overwrites the cell.

The pictures of the editor's docks come from the same card typed as a steps
file (do-it.steps.json), one keyboard step a row or a word, played in the
window by `blockwright --screenshot` (the editor is $BLOCKWRIGHT, else
blockwright).
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "scripts"))
from ansi import LOW, Canvas  # noqa: E402

BLACK, BLUE, GREEN, CYAN, RED, MAGENTA, BROWN, GREY = range(8)
DARK_GREY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_CYAN, LIGHT_RED, LIGHT_MAGENTA, YELLOW, WHITE = range(8, 16)

# Blockwright's sixteen F-key sets as CP437 codes (core/src/glyph_sets.cpp).
SETS = [
    [218, 191, 192, 217, 196, 179, 195, 180, 193, 194],
    [201, 187, 200, 188, 205, 186, 204, 185, 202, 203],
    [213, 184, 212, 190, 205, 179, 198, 181, 207, 209],
    [214, 183, 211, 189, 196, 186, 199, 182, 208, 210],
    [197, 206, 216, 215, 232, 232, 155, 156, 153, 239],
    [176, 177, 178, 219, 223, 220, 221, 222, 254, 250],
    [1, 2, 3, 4, 5, 6, 240, 14, 15, 32],
    [24, 25, 30, 31, 16, 17, 18, 29, 20, 21],
    [174, 175, 242, 243, 169, 170, 253, 246, 171, 172],
    [227, 241, 244, 245, 234, 157, 228, 248, 251, 252],
    [224, 225, 226, 229, 230, 231, 235, 236, 237, 238],
    [128, 135, 165, 164, 152, 159, 247, 249, 173, 168],
    [131, 132, 133, 160, 166, 134, 142, 143, 145, 146],
    [136, 137, 138, 130, 144, 140, 139, 141, 161, 158],
    [147, 148, 149, 162, 167, 150, 129, 151, 163, 154],
    [47, 92, 40, 41, 123, 125, 91, 93, 96, 39],
]
UNLOW = {v: k for k, v in LOW.items()}


def glyph(code):
    return UNLOW.get(code) or bytes([code]).decode("cp437")


def save(c, name, title):
    c.save(HERE / name, title=title)


class Pen:
    """Keyboard mode: a cursor, a pen and the current F-key set."""

    def __init__(self, canvas):
        self.c = canvas
        self.x = self.y = 0
        self.fg, self.bg = GREY, BLACK
        self.set = 6  # numbered from 1, as the Glyphs menu numbers them

    def at(self, x, y):
        self.x, self.y = x, y

    def type(self, s):
        for ch in s:
            self.c.put(self.x, self.y, ch, self.fg, self.bg)
            self.x = min(self.x + 1, self.c.width - 1)

    def fkey(self, n, times=1):
        for _ in range(times):
            self.type(glyph(SETS[self.set - 1][n - 1]))

    def hold(self, n=None):
        """Hold F<n> (or Space) until the cursor reaches the last column."""
        while self.x < self.c.width - 1:
            self.fkey(n) if n else self.type(" ")
        self.fkey(n) if n else self.type(" ")

    def enter(self):
        self.x, self.y = 0, min(self.y + 1, self.c.height - 1)


# The idea: the sixteen sets, F1 to F10 across.
c = Canvas(44, 33)
for k in range(10):
    c.text(4 + k * 4, 0, f"F{k + 1}", DARK_GREY, BLACK)
for s, codes in enumerate(SETS):
    y = 2 + s * 2
    c.text(0, y, f"{s + 1:>2}", YELLOW if s == 5 else DARK_GREY, BLACK)
    for k, code in enumerate(codes):
        c.put(4 + k * 4, y, glyph(code), WHITE if s == 5 else GREY, BLACK)
save(c, "sets.ans", "The F-key sets")

# Do it: an ace of hearts, 11 x 11.
c = Canvas(11, 11)
p = Pen(c)

# 2. The pen black on white, set 1, the top edge.
p.bg = WHITE
p.fg = BLACK
p.set = 1
p.at(0, 0)
p.fkey(1)
p.hold(5)
p.fkey(2)
save(c, "step-02.ans", "Step 2")

# 3. The sides, seven rows of them.
for _ in range(7):
    p.enter()
    p.fkey(6)
    p.hold()
    p.fkey(6)
save(c, "step-03.ans", "Step 3")

# 4. The bottom edge.
p.enter()
p.fkey(3)
p.hold(5)
p.fkey(4)
save(c, "step-04.ans", "Step 4")

# 5. The corners: A and a heart, top left and bottom right, in red.
p.fg = RED
p.at(1, 1)
p.type("A")
p.set = 7
p.at(1, 2)
p.fkey(3)
p.at(9, 6)
p.fkey(3)
p.at(9, 7)
p.type("A")
save(c, "step-05.ans", "Step 5")

# 6. The big heart, its first two rows, in the default set.
p.set = 6
p.at(2, 3)
p.fkey(6); p.fkey(4); p.fkey(6); p.type(" "); p.fkey(6); p.fkey(4); p.fkey(6)
p.at(2, 4)
p.fkey(4, 7)
save(c, "step-06.ans", "Step 6")

# 7. A slip (F6 where F5 was meant), undone, and the last two rows.
slip = c.copy()
s = Pen(slip)
s.fg, s.bg, s.set = RED, WHITE, 6
s.at(2, 5)
s.fkey(6)
save(slip, "slip.ans", "A slip")
p.at(2, 5)
p.fkey(5); p.fkey(4, 5); p.fkey(5)
p.at(4, 6)
p.fkey(5); p.fkey(4); p.fkey(5)
save(c, "step-07.ans", "Step 7")

# 8. Signed, in the default colours.
p.fg, p.bg = GREY, BLACK
p.at(2, 10)
p.type("funkpower")
save(c, "step-08.ans", "Step 8")

# 10. Saved, with its SAUCE title.
save(c, "final.ans", "Ace of hearts")
ace = c


# Check it: a corner short of the edge, a heart off centre, and the card as it should be.
def card():
    k = Canvas(11, 9)
    for y in range(9):
        for x in range(11):
            k.put(x, y, *ace.cells[y][x])
    return k


short = card()
short.put(9, 0, glyph(SETS[0][1]), BLACK, WHITE)
short.put(10, 0, " ", GREY, BLACK)
off = card()
for y in range(3, 7):
    for x in range(8, 1, -1):
        off.put(x + 1, y, *off.cells[y][x])
    off.put(2, y, " ", RED, WHITE)
off.put(9, 6, glyph(SETS[6][2]), RED, WHITE)

c = Canvas(39, 9)
for i, k in enumerate([short, off, card()]):
    for y in range(9):
        for x in range(11):
            c.put(i * 14 + x, y, *k.cells[y][x])
save(c, "check.ans", "Three cards")

# Try it: an empty card to make the ace of spades on.
c = Canvas(11, 11)
for y in range(9):
    for x in range(11):
        ch, fg, bg, blink = ace.cells[y][x]
        if 1 <= x <= 9 and 1 <= y <= 7:
            ch, fg = " ", BLACK
        c.put(x, y, ch, fg, bg, blink)
save(c, "try.ans", "An empty card")

# The answer: one way to draw it.
p = Pen(c)
p.fg, p.bg = BLACK, WHITE
p.at(1, 1)
p.type("A")
p.set = 7
p.at(1, 2)
p.fkey(6)
p.at(9, 6)
p.fkey(6)
p.at(9, 7)
p.type("A")
p.set = 6
p.at(2, 3)
p.type("  "); p.fkey(6); p.fkey(4); p.fkey(6)
p.at(2, 4)
p.fkey(6); p.fkey(4, 5); p.fkey(6)
p.at(2, 5)
p.fkey(5); p.fkey(4, 5); p.fkey(5)
p.at(4, 6)
p.fkey(6); p.fkey(4); p.fkey(6)
p.fg, p.bg = GREY, BLACK
p.at(2, 10)
p.type("funkpower")
save(c, "try-answer.ans", "Ace of spades")


# The docks: the card typed as keyboard steps, each string what the keys of
# "Do it" type, and the window pictured at three of them. A row typed past
# the last column overwrites it, as holding F5 to the edge and pressing F2
# does. The Glyphs dock shows set 6 throughout: no step changes the set.
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"


def key(name, at, text, **pen):
    return dict({"name": name, "action": "keyboard", "at": at, "text": text}, **pen)


def row(left, fill, right):
    return left + fill * 10 + right


steps = [key("top", [0, 0], row("┌", "─", "┐"), fg=BLACK, bg=WHITE)]
steps += [key(f"side-{y}", [0, y], row("│", " ", "│")) for y in range(1, 8)]
steps += [
    key("bottom", [0, 8], row("└", "─", "┘")),
    key("a-top", [1, 1], "A", fg=RED),
    key("heart-top", [1, 2], "♥"),
    key("heart-bottom", [9, 6], "♥"),
    key("a-bottom", [9, 7], "A"),
    key("humps", [2, 3], "▄█▄ ▄█▄"),
    key("row-4", [2, 4], "█" * 7),
    key("row-5", [2, 5], "▀█████▀"),
    key("point", [4, 6], "▀█▀"),
    key("sign", [2, 10], "funkpower", fg=GREY, bg=BLACK),
]
SHOTS = {
    # Step 2: the pen black on white.
    "top": ("pen.png", {"of": "palette"}),
    # The idea: the Glyphs dock's buttons and set list.
    "side-1": ("glyphs.png", {"of": "glyphBar", "crop": {"pixels": [0, 0, 512, 85]}}),
    # Check it: the finished card at 1x.
    "sign": ("preview.png", {"of": "preview", "crop": {"pixels": [0, 0, 307, 206]}}),
}
number = {}
for i, step in enumerate(steps):
    number[step["name"]] = i + 1
    if step["name"] in SHOTS:
        step["screenshot"] = SHOTS[step["name"]][1]
# The taller window gives the Preview dock room for the whole card.
body = {"version": 1, "start": {"blank": [11, 11]}, "steps": steps, "window": [1280, 1300]}
path = HERE / "do-it.steps.json"
path.write_text(json.dumps(body, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
    for name, (dest, _) in SHOTS.items():
        shutil.copyfile(Path(tmp) / f"{number[name]:02d}-{name}.png", HERE / dest)
