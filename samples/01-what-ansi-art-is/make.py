#!/usr/bin/env python3
"""Write tutorial 01's samples: python3 -I samples/01-what-ansi-art-is/make.py

The step files are the canvas each step of "Do it" leaves (typing in keyboard
mode puts the glyph in the pen's colours and moves the cursor one cell right).
final.ans is funkpower's 0xCAFE, copied from the ascii library, not made here.

The pictures of the editor's docks come from the same words typed as a steps
file (do-it.steps.json), one keyboard step a word, played in the window by
`blockwright --screenshot` (the editor is $BLOCKWRIGHT, else blockwright).
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
from ansi import Canvas  # noqa: E402

BLACK, BLUE, GREEN, CYAN, RED, MAGENTA, BROWN, GREY = range(8)
DARK_GREY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_CYAN, LIGHT_RED, LIGHT_MAGENTA, YELLOW, WHITE = range(8, 16)


def save(c, name, title):
    c.save(HERE / name, title=title)


# The idea: four cells, each one glyph with a foreground and a background.
c = Canvas(4, 1)
c.put(0, 0, "A", WHITE, BLUE)
c.put(1, 0, "▀", YELLOW, RED)
c.put(2, 0, "▒", LIGHT_CYAN, BLUE)
c.put(3, 0, "☺", YELLOW, BLACK)
save(c, "cells.ans", "Four cells")

# The 16 colours, numbered as the palette numbers them.
c = Canvas(32, 6)
for i in range(16):
    x, y = (i % 8) * 4, (i // 8) * 3
    c.fill(x, y, x + 2, y + 1, " ", GREY, i)
    c.text(x, y + 2, str(i), GREY, BLACK)
save(c, "palette.ans", "The 16 colours")

# Some of CP437's 256 glyphs.
c = Canvas(23, 7)
rows = [
    "A B C a b c 0 1 2 ! ? @",
    "░ ▒ ▓ █ ▀ ▄ ▌ ▐ ■ ·",
    "─ │ ┌ ┐ └ ┘ ═ ║ ╔ ╗ ╚ ╝",
    "☺ ☻ ♥ ♦ ♣ ♠ ► ◄ ▲ ▼ ⌂ ≈",
]
for i, row in enumerate(rows):
    c.text(0, i * 2, row, GREY, BLACK)
save(c, "glyphs.ans", "Some CP437 glyphs")

# Do it: a 32 x 8 canvas, typed on.
c = Canvas(32, 8)
c.text(1, 1, "HELLO", GREY, BLACK)
save(c, "step-02.ans", "Step 2")
c.text(1, 3, "ANSI", YELLOW, BLACK)
save(c, "step-03.ans", "Step 3")
c.text(1, 5, " ART ", WHITE, BLUE)
save(c, "step-04.ans", "Step 4")

# Check it: the same word in colours that read at 1x and ones that go soft.
c = Canvas(30, 5)
c.text(1, 1, " CLOSED ", GREY, WHITE)
c.text(11, 1, " CLOSED ", RED, GREY)
c.text(21, 1, " CLOSED ", DARK_GREY, BLACK)
c.text(1, 3, " CLOSED ", WHITE, BLUE)
c.text(11, 3, " CLOSED ", YELLOW, RED)
c.text(21, 3, " CLOSED ", WHITE, BLACK)
save(c, "soft-text.ans", "Text that goes soft")

# Try it: a small sign to read cell by cell.
c = Canvas(24, 5)
c.text(0, 0, "╔" + "═" * 22 + "╗", CYAN, BLACK)
c.put(0, 1, "║", CYAN, BLACK)
c.put(23, 1, "║", CYAN, BLACK)
c.text(0, 2, "║", CYAN, BLACK)
c.put(23, 2, "║", CYAN, BLACK)
c.put(0, 3, "║", CYAN, BLACK)
c.put(23, 3, "║", CYAN, BLACK)
c.text(0, 4, "╚" + "═" * 22 + "╝", CYAN, BLACK)
c.text(2, 1, "░▒▓", LIGHT_RED, RED)
c.text(6, 1, "OPEN", YELLOW, BLACK)
c.text(11, 1, "24/7", WHITE, BLACK)
c.text(16, 1, "▓▒░", LIGHT_RED, RED)
c.text(2, 2, "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀", RED, BLACK)
c.text(2, 3, "♥", LIGHT_RED, BLACK)
c.text(4, 3, "hot coffee", GREY, BLACK)
c.text(15, 3, "♥", LIGHT_RED, BLACK)
save(c, "try.ans", "Open 24/7")



# The docks: the words of "Do it" typed as keyboard steps, and the window
# pictured at the last two. The pen of each step holds for the steps after
# it; the last space of step 4 is a step of its own, so the Palette is
# pictured with the pen white on blue and the Preview with the words whole.
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"


def key(name, at, text, **pen):
    return dict({"name": name, "action": "keyboard", "at": at, "text": text}, **pen)


steps = [
    key("hello", [1, 1], "HELLO", fg=GREY, bg=BLACK),
    key("ansi", [1, 3], "ANSI", fg=YELLOW),
    key("art", [1, 5], " ART", fg=WHITE, bg=BLUE),
    key("space", [5, 5], " "),
]
SHOTS = {
    # Step 4: the pen white on blue.
    "art": ("pen.png", {"of": "palette"}),
    # Step 6: the canvas at 1x.
    "space": ("preview.png", {"of": "preview", "crop": {"pixels": [0, 0, 307, 170]}}),
}
number = {}
for i, step in enumerate(steps):
    number[step["name"]] = i + 1
    if step["name"] in SHOTS:
        step["screenshot"] = SHOTS[step["name"]][1]
# The taller window gives the Preview dock room for the whole canvas.
body = {"version": 1, "start": {"blank": [32, 8]}, "steps": steps, "window": [1280, 1300]}
path = HERE / "do-it.steps.json"
path.write_text(json.dumps(body, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
    for name, (dest, _) in SHOTS.items():
        shutil.copyfile(Path(tmp) / f"{number[name]:02d}-{name}.png", HERE / dest)
