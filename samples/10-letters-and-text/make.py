#!/usr/bin/env python3
"""Write tutorial 10's samples: python3 -I samples/10-letters-and-text/make.py

Every picture is a steps file played by `blockwright-cli replay --project`
(the CLI is $BLOCKWRIGHT_CLI, else blockwright-cli on PATH): letters drawn
pixel by pixel with the Half-Block Brush on a Pixels layer, labels typed
with the Keyboard tool, rows recoloured with the Rectangle on the layer with
its alpha locked, and letters cleared and moved with selections. The letters
are the bitmaps in FACE below, a pixel a '#'; each letter is one stroke of
the brush, a walk through its pixels from one to the next beside it, so the
stroke paints those pixels and no other. This script writes the steps files
(*.steps.json) and the blank canvases they start from (blank-WxH.ans, which
carry the SAUCE), replays each into a scratch directory, and copies the
captures the page shows beside them. The pictures of the editor's docks come
from the same steps played in the window by `blockwright --screenshot` (the
editor is $BLOCKWRIGHT, else blockwright).
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
DARK_GREY, LIGHT_RED, YELLOW, WHITE = 8, 12, 14, 15
TITLE = "Letters and text"
DATE = "20261105"
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"
WINDOW = [1280, 1300]
DOCK = [0, 0, 310, 205]

# A face 10 pixels tall with 2-pixel stems: five cell rows a letter. The
# letters are 6 columns wide and the 1 is 4. The *_bad ones are the
# misreads: a C with a spur on its lower arm, an R with a shut bowl and no
# leg, and a 0 with square corners.
FACE = {
    "C": """
.#####
######
##....
##....
##....
##....
##....
##....
######
.#####""",
    "C_bad": """
.#####
######
##....
##....
##....
##....
##..##
##..##
######
.#####""",
    "G": """
.#####
######
##....
##....
##.###
##.###
##..##
##..##
######
.#####""",
    "R": """
#####.
######
##..##
##..##
#####.
####..
##.##.
##.##.
##..##
##..##""",
    "R_bad": """
#####.
######
##..##
##..##
######
######
##..##
##..##
##..##
##..##""",
    "A": """
..##..
.####.
##..##
##..##
######
######
##..##
##..##
##..##
##..##""",
    "0": """
.####.
######
##..##
##..##
##..##
##..##
##..##
##..##
######
.####.""",
    "0_bad": """
######
######
##..##
##..##
##..##
##..##
##..##
##..##
######
######""",
    "D": """
#####.
######
##..##
##..##
##..##
##..##
##..##
##..##
######
#####.""",
    "1": """
.##.
###.
.##.
.##.
.##.
.##.
.##.
.##.
####
####""",
}


def bitmap(key):
    rows = FACE[key].strip("\n").split("\n")
    return [(x, y) for y, row in enumerate(rows) for x, ch in enumerate(row) if ch == "#"]


def width(key):
    return len(FACE[key].strip("\n").split("\n")[0])


def walk(pixels):
    """The pixels in an order a stroke can take: each point beside the last
    (left, right, up or down), going back over painted pixels where it must,
    so the stroke joins neighbours only and paints nothing else."""
    left = set(pixels)
    start = min(pixels, key=lambda p: (p[1], p[0]))
    path, stack = [start], [start]
    left.discard(start)
    while stack:
        x, y = stack[-1]
        for n in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if n in left:
                left.discard(n)
                stack.append(n)
                path.append(n)
                break
        else:
            stack.pop()
            if stack:
                path.append(stack[-1])
    assert not left, "a letter's pixels must join left, right, up or down"
    return path


def letter(name, key, x, py, **options):
    """One stroke of the Half-Block Brush through every pixel of the letter,
    its top left at column x, pixel row py."""
    points = [[x + dx, py + dy] for dx, dy in walk(bitmap(key))]
    return dict({"name": name, "action": "halfBlock"}, **options, points=points)


def word(prefix, keys, x, py, gaps=None, **options):
    """The letters left to right, a 1-pixel gap after each unless gaps says
    otherwise; the first takes the options. Returns the steps and the column
    each letter starts at."""
    steps, at = [], []
    for i, key in enumerate(keys):
        at.append(x)
        steps.append(letter(f"{prefix}-{i}", key, x, py, **(options if i == 0 else {})))
        x += width(key) + (gaps or {}).get(i, 1)
    return steps, at


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
    """Writes the steps file and plays it; keep maps a step's name to the file
    its capture becomes (an .ans, or a .bwp for the project after it). shots
    maps a step's name to the PNG its "screenshot" becomes, taken in the
    window."""
    path = write_steps(name, start, steps, window)
    number = {step["name"]: i + 1 for i, step in enumerate(steps)}
    project = any(dest.endswith(".bwp") for dest in keep.values())
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [CLI, "replay", str(path), "-o", tmp] + (["--project"] if project else [])
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
        for step, dest in keep.items():
            capture = f"{number[step]:02d}-{step}{Path(dest).suffix}"
            shutil.copyfile(Path(tmp) / capture, HERE / dest)
    if not shots:
        return
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        for step, dest in shots.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.png", HERE / dest)


def shot(step, of, crop=None):
    step = dict(step, screenshot={"of": of})
    if crop:
        step["screenshot"]["crop"] = {"pixels": crop}
    return step


def label(name, x, y, text):
    """Grey text on black, typed with the Keyboard tool."""
    return {"name": name, "action": "keyboard", "fg": GREY, "bg": BLACK, "at": [x, y], "text": text}


def title_layer():
    return {"name": "title-layer", "action": "newPixelLayer", "rename": "title"}


PEN = {"fg": YELLOW, "bg": BLACK, "symmetry": "none"}

# The idea: the three misreads, each as a group of three: the bad letter,
# the letter it reads as, and the fix, a label under each.
GROUPS = [("C_bad", "G", "C"), ("R_bad", "A", "R"), ("0_bad", "D", "0")]
start = blank(80, 7)
steps, x = [], 2
for g, keys in enumerate(GROUPS):
    for i, key in enumerate(keys):
        steps.append(label(f"label-{g}-{i}", x + 2, 6, key[0]))
        x += 8
    x += 3
steps.append(title_layer())
x = 2
for g, keys in enumerate(GROUPS):
    for i, key in enumerate(keys):
        steps.append(letter(f"letter-{g}-{i}", key, x, 2, **(PEN if not g and not i else {})))
        x += 8
    x += 3
replay("misreads", start, steps, {steps[-1]["name"]: "misreads.bwp"})

# Do it: CRAG 10 in yellow on a Pixels layer, two letters a step, a 4-pixel
# word gap, then cell rows 1, 4 and 5 recoloured white, light red and red on
# the layer with its alpha locked.
W, H = 46, 7
TITLE_WORD = ["C", "R", "A", "G", "1", "0"]
letters, at = word("letter", TITLE_WORD, 2, 2, gaps={3: 4}, **PEN)
ROWS = [(1, WHITE), (4, LIGHT_RED), (5, RED)]
LOCK = [{"name": "lock", "action": "layerProperties", "alphaLocked": True}]
BANDS = [{"name": f"row-{y}", "action": "rectangle", "fg": c, "filled": True, "from": [0, 2 * y], "to": [W - 1, 2 * y + 1]}
         for y, c in ROWS]
start = blank(W, H)
steps = [title_layer()] + letters + LOCK + BANDS
steps[0] = shot(steps[0], "layers", DOCK)
steps[1] = shot(steps[1], "toolOptions", [0, 0, 256, 640])
steps[-1] = shot(steps[-1], "preview")
replay("final", start, steps,
       {"letter-1": "step-01.bwp", "letter-3": "step-02.bwp", "letter-5": "step-03.bwp", "row-5": "final.bwp"},
       {"title-layer": "layers.png", "letter-0": "brush-options.png", "row-5": "preview.png"}, window=WINDOW)

# Check it: the word gap as tight as the letter gaps.
tight, _ = word("tight", TITLE_WORD, 2, 2, **PEN)
replay("tight", start, [title_layer()] + tight, {"tight-5": "tight.bwp"})

# Check it: the rows painted with the layer's alpha unlocked.
replay("no-lock", start, [title_layer()] + letters + BANDS, {"row-5": "no-lock.bwp"})

# Try it: ARC 10 drawn with the three misreads and a 1-pixel word gap. The
# answer clears the bad R and the bad 0 and draws them again, clears the C's
# spur, and moves the 10 three columns right.
TRY_WORD = ["A", "R_bad", "C_bad", "1", "0_bad"]
bad, at = word("letter", TRY_WORD, 2, 2, **PEN)
start = blank(39, 7)
replay("try", start, [title_layer()] + bad, {"letter-4": "try.bwp"})
r, c, one, zero = at[1], at[2], at[3], at[4]
answer = [{"name": "title", "action": "setActiveLayer", "layer": "title"},
          {"name": "r-select", "action": "select", "rect": [r, 1, r + 5, 5]},
          {"name": "r-clear", "action": "deleteSelection"},
          {"name": "zero-select", "action": "select", "rect": [zero, 1, zero + 5, 5]},
          {"name": "zero-clear", "action": "deleteSelection"},
          {"name": "spur-select", "action": "select", "rect": [c + 4, 4, c + 5, 4]},
          {"name": "spur-clear", "action": "deleteSelection"},
          {"name": "deselect", "action": "deselect"},
          letter("r", "R", r, 2, **PEN),
          letter("zero", "0", zero, 2),
          {"name": "gap-select", "action": "select", "rect": [one, 1, zero + 5, 5]},
          {"name": "gap", "action": "moveSelection", "by": [3, 0]},
          {"name": "gap-deselect", "action": "deselect"}]
replay("try-answer", "try.bwp", answer, {"gap-deselect": "try-answer.bwp"})
