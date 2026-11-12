#!/usr/bin/env python3
"""Write the Tools page's samples: python3 -I samples/manual-04-tools/make.py

Each steps file starts from a blank canvas this script writes (it carries the
SAUCE) and is played by `blockwright-cli replay` (the CLI is $BLOCKWRIGHT_CLI,
else blockwright-cli on PATH): one tool's strokes, through the editor's own
brushes and shapes, and the captures the page shows are copied beside it. The
pictures of the Tool Options dock come from options.steps.json played in the
window by `blockwright --screenshot` (the editor is $BLOCKWRIGHT, else
blockwright): a step for each tool, with the options a fresh editor starts
with, cropped to the options below the tool's help.
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
TITLE = "Tools"
DATE = "20261112"
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"
W, H = 24, 8


def blank(w, h):
    name = f"blank-{w}x{h}.ans"
    Canvas(w, h).save(HERE / name, title=TITLE, date=DATE)
    return name


def write_steps(name, start, steps, window=None):
    path = HERE / f"{name}.steps.json"
    body = {"version": 1, "start": {"file": start}, "steps": steps}
    if window:
        body["window"] = window
    text = json.dumps(body, indent=1, ensure_ascii=False)
    path.write_text(text + "\n", encoding="utf-8")
    return path


def replay(name, start, steps, keep, shots=None, window=None):
    """Writes the steps file and plays it; keep maps a capture's name (a
    step's, with -before or -after for a before-after step) to the file it
    becomes. shots maps a step's name to the PNG its "screenshot" becomes,
    taken in the window."""
    path = write_steps(name, start, steps, window)
    number = {step["name"]: i + 1 for i, step in enumerate(steps)}
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([CLI, "replay", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        for capture, dest in keep.items():
            step = capture.removesuffix("-before").removesuffix("-after")
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{capture}.ans", HERE / dest)
    if not shots:
        return
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        for step, dest in shots.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.png", HERE / dest)


def row(x0, x1, y):
    return [[x0, y], [x1, y]]


def cover(x0, x1, y0, y1):
    """A stroke that passes over every cell of the box once, a row at a time."""
    pts = []
    for y in range(y0, y1 + 1):
        a, b = (x0, x1) if (y - y0) % 2 == 0 else (x1, x0)
        pts += [[a, y], [b, y]]
    return pts


def before_after(step):
    return dict(step, capture="before-after")


start = blank(W, H)

# The shape most brushes work on: a dark grey disc on black, two rungs up the
# steel ramp (black, dark grey, grey, white).
DISC = {"name": "disc", "action": "ellipse", "fg": DARK_GREY, "filled": True, "from": [2, 1], "to": [21, 14]}
# The options a fresh editor starts with, where replay's differ.
EDITOR = {"strength": 0.25, "pressure": "size", "ramp": "steel"}

# Half-block brush: the same diagonal drag with Pencil 4-connected on, then off.
replay("half-block", start,
       [{"name": "four", "action": "halfBlock", "fg": YELLOW, "pencil": 4, "points": [[1, 1], [10, 14]]},
        {"name": "eight", "action": "halfBlock", "pencil": 8, "points": [[13, 1], [22, 14]]}],
       {"eight": "half-block.ans"})

# Shade brush: a row each of one, two, three and four passes, then a row
# built to four and taken back one with the right button.
steps = [{"name": "pen", "action": "shade", "fg": LIGHT_BLUE, "bg": BLUE}]
for y in range(4):
    steps += [{"name": f"row{y + 1}-{i + 1}", "action": "shade", "points": row(2, 21, y + 1)} for i in range(y + 1)]
steps += [{"name": f"back-{i + 1}", "action": "shade", "points": row(2, 21, 6)} for i in range(4)]
steps.append({"name": "back", "action": "shade", "button": "right", "points": row(2, 21, 6)})
replay("shade", start, steps, {"back": "shade.ans"})

# Glyph brush: a round tip of hearts dragged across, then the right button
# erasing a line through them.
replay("glyph", start,
       [{"name": "hearts", "action": "glyph", "glyph": "♥", "fg": LIGHT_RED, "size": 5, "tip": "round",
         "points": row(4, 19, 3)},
        {"name": "erase", "action": "glyph", "button": "right", "size": 1, "points": row(0, 23, 3)}],
       {"erase": "glyph.ans"})

# Colorize brush: red over the disc, keeping its glyphs.
replay("colorize", start,
       [DISC, before_after({"name": "red", "action": "colorize", "fg": RED, "size": 3, "points": row(0, 23, 3)})],
       {"red-before": "disc.ans", "red-after": "colorize.ans"})

# Ramp shade brush at the editor's 25%: three clicks of shrinking size
# lighten the disc's upper left.
replay("ramp-shade", start,
       [DISC, dict(EDITOR, name="opts", action="rampShade", tip="round")]
       + [{"name": f"lit-{i + 1}", "action": "rampShade", "size": size, "points": [[9, 2]]}
          for i, size in enumerate([13, 9, 5])],
       {"lit-3": "ramp-shade.ans"})

# Form brush: two dark grey blocks, each selected and stroked over at 100%,
# lit from the north-west: a dome on the left, a cylinder on the right.
BLOCKS = [{"name": "left", "action": "rectangle", "fg": DARK_GREY, "filled": True, "from": [1, 2], "to": [10, 13]},
          {"name": "right", "action": "rectangle", "fg": DARK_GREY, "filled": True, "from": [13, 2], "to": [22, 13]}]
replay("form", start,
       BLOCKS + [dict(EDITOR, name="opts", action="form", strength=1),
                 {"name": "sel-dome", "action": "select", "rect": [1, 1, 10, 6]},
                 {"name": "dome", "action": "form", "size": 3, "points": cover(1, 10, 1, 6)},
                 {"name": "sel-cyl", "action": "select", "rect": [13, 1, 22, 6]},
                 {"name": "cylinder", "action": "form", "form": {"shape": "cylinder", "rim": False, "specular": True},
                  "size": 3, "points": cover(13, 22, 1, 6)}],
       {"cylinder": "form.ans"})

# Soft brush: one click at 100% in the middle of the disc, hardness 0%.
replay("soft", start,
       [DISC, dict(EDITOR, name="opts", action="soft", hardness=0, tip="round"),
        {"name": "soft", "action": "soft", "strength": 1, "size": 12, "points": [[11, 3]]}],
       {"soft": "soft.ans"})

# Despeckle brush: grey specks in the disc, then one stroke over it.
SPECKS = [{"name": f"speck-{i + 1}", "action": "halfBlock", "fg": GREY, "points": [[x, 2 * y], [x, 2 * y + 1]]}
          for i, (x, y) in enumerate([(6, 2), (11, 4), (16, 3)])]
replay("despeckle", start,
       [DISC] + SPECKS
       + [dict(EDITOR, name="opts", action="despeckle"),
          before_after({"name": "clean", "action": "despeckle", "size": 3, "points": cover(2, 21, 1, 6)})],
       {"clean-before": "despeckle-before.ans", "clean-after": "despeckle.ans"})

# Smudge brush: a grey bar on dark grey, dragged right at 100% and at 50%.
# Black stops a smear, so the ground is dark grey.
GROUND = {"name": "ground", "action": "rectangle", "fg": DARK_GREY, "filled": True, "from": [0, 0], "to": [23, 15]}
BAR = {"name": "bar", "action": "rectangle", "fg": GREY, "filled": True, "from": [2, 2], "to": [7, 13]}
replay("smudge", start,
       [GROUND, BAR, dict(EDITOR, name="opts", action="smudge"),
        {"name": "full", "action": "smudge", "strength": 1, "size": 2, "points": row(4, 21, 2)},
        {"name": "half", "action": "smudge", "strength": 0.5, "size": 2, "points": row(4, 21, 5)}],
       {"half": "smudge.ans"})

# Outline brush: a grey disc, one stroke over it.
replay("outline", start,
       [dict(DISC, fg=GREY), dict(EDITOR, name="opts", action="outline"),
        before_after({"name": "line", "action": "outline", "size": 3, "points": cover(1, 22, 0, 7)})],
       {"line-before": "outline-before.ans", "line-after": "outline.ans"})

# Rim light brush: the disc lit from the north-west, one stroke over it.
replay("rim-light", start,
       [DISC, dict(EDITOR, name="opts", action="rimLight"),
        {"name": "rim", "action": "rimLight", "size": 3, "points": cover(1, 22, 0, 7)}],
       {"rim": "rim-light.ans"})

# Texture stamp: scales at the defaults, then brick, each a band across.
replay("texture", start,
       [dict(EDITOR, name="opts", action="texture"),
        {"name": "scales", "action": "texture", "size": 4, "points": cover(0, 11, 0, 7)},
        {"name": "brick", "action": "texture", "texture": {"kind": "brick", "density": 1.6, "seed": 1},
         "points": cover(12, 23, 0, 7)}],
       {"brick": "texture.ans"})

# Clone stamp: a small disc at the left, its middle Ctrl+clicked, and a
# stroke at the right copying it.
SMALL = {"name": "small", "action": "ellipse", "fg": LIGHT_CYAN, "filled": True, "from": [1, 2], "to": [8, 13]}
replay("clone", start,
       [SMALL, {"name": "source", "action": "clone", "source": [4, 3]},
        before_after({"name": "copy", "action": "clone", "size": 3, "points": [[17, 3]] + cover(14, 21, 0, 7)})],
       {"copy-before": "clone-before.ans", "copy-after": "clone.ans"})

# Glyph spray: stars on the left half, haze on the right, at the defaults.
replay("spray", start,
       [dict(EDITOR, name="opts", action="spray", fg=WHITE),
        {"name": "stars", "action": "spray", "size": 4, "points": cover(0, 11, 0, 7)},
        {"name": "haze", "action": "spray", "spray": {"kind": "haze", "density": 30, "seed": 1},
         "points": cover(12, 23, 0, 7)}],
       {"haze": "spray.ans"})

# Line, Rectangle and Ellipse, the ellipse with Filled ticked.
replay("shapes", start,
       [{"name": "line", "action": "line", "fg": LIGHT_GREEN, "from": [0, 14], "to": [6, 1]},
        {"name": "rect", "action": "rectangle", "fg": YELLOW, "filled": False, "from": [8, 2], "to": [14, 13]},
        {"name": "oval", "action": "ellipse", "fg": LIGHT_MAGENTA, "filled": True, "from": [16, 2], "to": [23, 13]}],
       {"oval": "shapes.ans"})

# Fill: a grey ring, filled inside with red.
replay("fill", start,
       [dict(DISC, fg=GREY, filled=False),
        before_after({"name": "fill", "action": "fill", "fg": RED, "at": [11, 7]})],
       {"fill-before": "fill-before.ans", "fill-after": "fill.ans"})

# Ramp gradient: linear across the canvas on the steel ramp, rung 0 to 12,
# then radial from the middle, each with nothing selected.
replay("gradient-linear", start,
       [{"name": "linear", "action": "gradient", "ramp": "steel",
         "gradient": {"shape": "linear", "banding": "cells", "from": 0, "to": 12}, "from": [0, 0], "to": [23, 0]}],
       {"linear": "gradient-linear.ans"})
replay("gradient-radial", start,
       [{"name": "radial", "action": "gradient", "ramp": "steel",
         "gradient": {"shape": "radial", "banding": "bayer", "from": 12, "to": 0}, "from": [11, 3], "to": [22, 3]}],
       {"radial": "gradient-radial.ans"})

# Text: a word in the bundled block face.
replay("text", start,
       [{"name": "word", "action": "text", "at": [1, 1], "text": "Hi",
         "textOptions": {"face": "block", "colour": YELLOW}}],
       {"word": "text.ans"})

# The Tool Options dock for each tool, in the toolbox's order. A step that
# only picks the tool has no points; select and move need a rectangle and a
# distance, so they get the smallest.
TOOLS = ["keyboard", "select", "move", "halfBlock", "shade", "glyph", "colorize", "rampShade", "form", "soft",
         "despeckle", "smudge", "outline", "rimLight", "texture", "clone", "spray", "line", "rectangle", "ellipse",
         "fill", "gradient", "eyedropper", "text"]
NEEDS = {"keyboard": EDITOR, "select": {"rect": [0, 0, 0, 0]}, "move": {"by": [0, 0]}}
# Each crop: the dock's options, below the help and the shortcuts link.
CROPS = {
    "clone": [0, 499, 256, 212],
    "colorize": [0, 385, 256, 185],
    "despeckle": [0, 481, 256, 215],
    "eyedropper": [0, 295, 256, 28],
    "fill": [0, 499, 256, 124],
    "form": [0, 649, 256, 305],
    "glyph": [0, 445, 256, 207],
    "gradient": [0, 817, 256, 151],
    "halfblock": [0, 631, 256, 151],
    "line": [0, 367, 256, 124],
    "move": [0, 649, 256, 237],
    "outline": [0, 757, 256, 215],
    "rampshade": [0, 541, 256, 248],
    "rectangle": [0, 427, 256, 151],
    "rimlight": [0, 523, 256, 272],
    "select": [0, 895, 256, 34],
    "shade": [0, 541, 256, 185],
    "smudge": [0, 517, 256, 248],
    "soft": [0, 541, 256, 279],
    "spray": [0, 697, 256, 276],
    "text": [0, 655, 256, 809],
    "texture": [0, 661, 256, 306],
}
steps = []
for tool in TOOLS:
    step = dict({"name": tool.lower(), "action": tool}, **NEEDS.get(tool, {}))
    if step["name"] in CROPS:  # the keyboard has no options to show
        step["screenshot"] = {"of": "toolOptions", "crop": {"pixels": CROPS[step["name"]]}}
    steps.append(step)
replay("options", start, steps, {}, {s["name"]: f"options-{s['name']}.png" for s in steps if "screenshot" in s},
       window=[1280, 1700])
