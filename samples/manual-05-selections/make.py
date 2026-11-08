#!/usr/bin/env python3
"""Write the Selections page's samples: python3 -I samples/manual-05-selections/make.py

Each steps file starts from a blank canvas this script writes (it carries the
SAUCE) and is played by `blockwright-cli replay --project` (the CLI is
$BLOCKWRIGHT_CLI, else blockwright-cli); the .bwp captures the page shows are
copied beside it. float.png is the same steps played by `blockwright
--screenshot` (the editor is $BLOCKWRIGHT, else blockwright), the canvas
cropped out of the window.

transforms.bwp: a flag drawn once at the left, then copied and pasted four
times, each float flipped or turned before it is put down: Flip
Horizontally, Flip Vertically, Rotate Clockwise, Rotate Counterclockwise.

paste-modes.bwp: three green hills on the bottom layer, and a sun of yellow
full blocks whose corners are spaces on black, copied and pasted over each
hill's top, Normal, Transparent and Under from left to right. The sun is
drawn at the top left, copied, and cleared before the pastes.

float.png: the Under paste still floating, before it is put down.
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

BLACK, RED, GREEN, BROWN, WHITE, YELLOW = 0, 4, 2, 6, 15, 14
TITLE = "Selections"
DATE = "20261108"
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"


def blank(w, h):
    name = f"blank-{w}x{h}.ans"
    Canvas(w, h).save(HERE / name, title=TITLE, date=DATE)
    return name


def replay(name, start, steps, keep, shots=None, window=None):
    """Write <name>.steps.json and play it; keep maps a step's name to the
    .bwp its capture becomes, shots a step's name to the PNG its
    "screenshot" becomes."""
    path = HERE / f"{name}.steps.json"
    body = {"version": 1, "start": {"file": start}, "steps": steps}
    if window:
        body["window"] = window
    path.write_text(json.dumps(body, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    number = {step["name"]: i + 1 for i, step in enumerate(steps)}
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([CLI, "replay", str(path), "-o", tmp, "--project"], check=True, stdout=subprocess.DEVNULL)
        for step, dest in keep.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.bwp", HERE / dest)
    if not shots:
        return
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        for step, dest in shots.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.png", HERE / dest)


def glyph(name, g, fg, points, bg=BLACK):
    return {"name": name, "action": "glyph", "glyph": g, "fg": fg, "bg": bg, "points": points}


# The flag: a white pole of right half blocks on a foot, a red pennant of
# upper half blocks, and a yellow arrow at its tip. 5 columns by 4 rows.
FLAG = [
    glyph("pole", "▐", WHITE, [[0, 0], [0, 1], [0, 2]]),
    glyph("foot", "┴", WHITE, [[0, 3]]),
    glyph("pennant", "▀", RED, [[1, 0], [2, 0], [3, 0], [1, 1], [2, 1]]),
    glyph("tip", "►", YELLOW, [[4, 0]]),
    {"name": "select-flag", "action": "select", "rect": [0, 0, 4, 3]},
    {"name": "copy-flag", "action": "copy"},
]
steps = list(FLAG)
for n, action in enumerate(["flipHorizontal", "flipVertical", "rotateClockwise", "rotateCounterClockwise"], 1):
    steps += [{"name": f"paste-{n}", "action": "paste", "at": [n * 8, 0]},
              {"name": f"turn-{n}", "action": action},
              {"name": f"stamp-{n}", "action": "deselect"}]
replay("transforms", blank(37, 5), steps, {"stamp-4": "transforms.bwp"})

# The sun: yellow full blocks, 6 by 3, its four corners left as they are,
# spaces on black.
SUN = [[x, 0] for x in range(1, 5)] + [[x, 1] for x in range(6)] + [[x, 2] for x in range(1, 5)]
steps = [{"name": f"hill-{n}", "action": "ellipse", "fg": GREEN, "filled": True,
          "from": [x - 1, 6], "to": [x + 12, 15]} for n, x in enumerate((1, 15, 29), 1)]
steps += [{"name": "ground", "action": "rectangle", "fg": GREEN, "filled": True, "symmetry": "none",
           "from": [0, 12], "to": [41, 15]}]
steps += [glyph("sun", "█", YELLOW, SUN),
          {"name": "select-sun", "action": "select", "rect": [0, 0, 5, 2]},
          {"name": "copy-sun", "action": "copy"},
          {"name": "clear-sun", "action": "deleteSelection"}]
for n, (x, mode) in enumerate([(4, "normal"), (18, "transparent"), (32, "under")], 1):
    steps += [{"name": f"paste-{mode}", "action": "paste", "at": [x, 2], "pasteMode": mode},
              {"name": f"stamp-{mode}", "action": "deselect"}]
steps[-2]["screenshot"] = {"of": "canvasView", "crop": {"cells": [28, 0, 14, 8]}, "scale": 2}
replay("paste-modes", blank(42, 8), steps, {"stamp-under": "paste-modes.bwp"}, {"paste-under": "float.png"},
       window=[1600, 1000])
