#!/usr/bin/env python3
"""Write tutorial 04's samples: python3 -I samples/04-shading-the-ladder/make.py

Every picture is a steps file played by `blockwright-cli replay` (the CLI is
$BLOCKWRIGHT_CLI, else blockwright-cli on PATH): the editor's own shade and
ramp shade brushes and layer actions, one step per stroke. This script writes
the steps files (*.steps.json) and the blank canvases they start from
(blank-WxH.ans, which carry the SAUCE), replays each into a scratch
directory, and copies the captures the page shows beside them. The pictures
of the editor's docks come from the same steps played in the window by
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
TITLE = "Shading: the ladder"
DATE = "20261105"
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"

# The ramps Blockwright ships (core/src/ramp.cpp), in its order, with how
# many colours each climbs through.
RAMPS = [("fire", 5), ("sunset", 6), ("ice", 5), ("grass", 4), ("steel", 4),
         ("skin", 5), ("sea", 4), ("toxic", 5), ("violet", 4), ("wood", 4)]


def blank(w, h):
    name = f"blank-{w}x{h}.ans"
    Canvas(w, h).save(HERE / name, title=TITLE, date=DATE)
    return name


def rows(x0, x1, y0, y1):
    """A stroke's points that pass over every cell of the box once, a row at a time."""
    pts = []
    for y in range(y0, y1 + 1):
        a, b = (x0, x1) if (y - y0) % 2 == 0 else (x1, x0)
        pts += [[a, y], [b, y]]
    return pts


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
    window (a "-before" or "-after" in the name picks that one)."""
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
            base, _, when = step.partition(":")
            shutil.copyfile(Path(tmp) / f"{number[base]:02d}-{base}{'-' + when if when else ''}.png", HERE / dest)


# The idea: the five steps of a ladder, light blue over blue, a blank cell
# between each. Each cell is clicked with the shade brush once per rung.
start = blank(9, 1)
steps = [{"name": "base", "action": "rectangle", "fg": BLUE, "filled": True, "from": [x, 0], "to": [x, 1]}
         for x in range(0, 9, 2)]
steps.append({"name": "pen", "action": "shade", "fg": LIGHT_BLUE, "bg": BLUE, "size": 1, "tip": "square"})
for rung in range(1, 5):
    for i in range(rung):
        steps.append({"name": f"rung-{rung}-{i + 1}", "action": "shade", "points": [[2 * rung, 0]]})
replay("ladder", start, steps, {"rung-4-4": "ladder.ans"})

# The shade brush on a plain shape: a blue bar, then four passes of light
# blue over blue, each starting three cells further right, so each part of
# the bar keeps the rung it reached. Then one right-button pass back down
# over the whole bar.
start = blank(15, 2)
steps = [{"name": "base", "action": "rectangle", "fg": BLUE, "filled": True, "from": [0, 0], "to": [14, 3]},
         {"name": "pen", "action": "shade", "fg": LIGHT_BLUE, "bg": BLUE, "size": 1, "tip": "square"}]
for i in range(1, 5):
    steps.append({"name": f"pass-{i}", "action": "shade", "points": rows(3 * i, 14, 0, 1)})
steps.append({"name": "back", "action": "shade", "button": "right", "points": rows(0, 14, 0, 1)})
replay("shade", start, steps, {"base": "shade-before.ans", "pass-4": "shade-after.ans", "back": "shade-right.ans"})

# Every ramp Blockwright ships, climbed a rung a cell: the ramp shade brush
# at 25%, one pass per rung, each pass starting a cell further right.
LABEL = 7
width = LABEL + 4 * 5 + 1
start = blank(width, 2 * len(RAMPS) - 1)
steps = []
for r, (ramp, colours) in enumerate(RAMPS):
    y = 2 * r
    steps.append({"name": f"{ramp}-label", "action": "keyboard", "fg": GREY, "bg": BLACK, "at": [0, y], "text": ramp})
    top = 4 * (colours - 1)
    for i in range(1, top + 1):
        steps.append({"name": f"{ramp}-{i}", "action": "rampShade", "ramp": ramp, "strength": 0.25,
                      "size": 1, "tip": "square", "points": [[LABEL + i, y], [LABEL + top, y]]})
replay("ramps", start, steps, {steps[-1]["name"]: "ramps.ans"})

# The ramp shade brush on a plain shape: the same blue bar, wider, with the
# ice ramp at 25%. Left-button passes, each starting two cells further right,
# climb about two thirds of the bar up the ramp; right-button passes, each
# ending two cells further left, take the left end down to black.
start = blank(34, 2)
steps = [{"name": "base", "action": "rectangle", "fg": BLUE, "filled": True, "from": [0, 0], "to": [33, 3]},
         {"name": "pen", "action": "rampShade", "ramp": "ice", "strength": 0.25, "size": 1, "tip": "square"}]
for i in range(1, 13):
    steps.append({"name": f"up-{i}", "action": "rampShade", "points": rows(8 + 2 * i, 33, 0, 1)})
for i in range(1, 5):
    steps.append({"name": f"down-{i}", "action": "rampShade", "button": "right", "points": rows(0, 9 - 2 * i, 0, 1)})
replay("ramp-shade", start, steps, {"base": "ramp-shade-before.ans", "down-4": "ramp-shade-after.ans"})

# Strength as a labelled row: the fire ramp on black, one pass of a 4 x 2
# square at each strength on the top row, two passes on the bottom row.
STRENGTHS = [0.25, 0.5, 0.75, 1.0]
start = blank(9 + 6 * len(STRENGTHS), 5)
steps = []
for i, s in enumerate(STRENGTHS):
    steps.append({"name": f"label-{i + 1}", "action": "keyboard", "fg": GREY, "bg": BLACK,
                  "at": [9 + 6 * i, 0], "text": f"{round(s * 100)}%"})
steps.append({"name": "label-once", "action": "keyboard", "at": [0, 1], "text": "1 pass"})
steps.append({"name": "label-twice", "action": "keyboard", "at": [0, 3], "text": "2 passes"})
for i, s in enumerate(STRENGTHS):
    x = 9 + 6 * i
    steps.append({"name": f"once-{i + 1}", "action": "rampShade", "ramp": "fire", "strength": s,
                  "size": 1, "tip": "square", "points": rows(x, x + 3, 1, 2)})
    for p in (1, 2):
        steps.append({"name": f"twice-{i + 1}-{p}", "action": "rampShade", "points": rows(x, x + 3, 3, 4)})
replay("strength", start, steps, {steps[-1]["name"]: "strength.ans"})

# Alpha lock: two balls on a layer of their own, each clicked once at 50%
# with the brush hanging over its upper left, the first with the layer's
# alpha lock off and the second with it on.
start = blank(34, 9)
steps = [{"name": "label-off", "action": "keyboard", "fg": GREY, "bg": BLACK, "at": [4, 8], "text": "lock off"},
         {"name": "label-on", "action": "keyboard", "at": [22, 8], "text": "lock on"},
         {"name": "ball-layer", "action": "newCellsLayer", "rename": "ball"},
         {"name": "ball-1", "action": "rampShade", "ramp": "fire", "strength": 1, "size": 12, "tip": "round",
          "points": [[8, 4]]},
         {"name": "ball-2", "action": "rampShade", "points": [[25, 4]]},
         {"name": "click-off", "action": "rampShade", "strength": 0.5, "points": [[6, 3]]},
         {"name": "lock", "action": "layerProperties", "alphaLocked": True},
         {"name": "click-on", "action": "rampShade", "points": [[23, 3]]}]
replay("alpha-lock", start, steps, {"click-on": "alpha-lock.ans"})

# The finished piece: a lit ball on a floor, on two layers. The floor is
# the shade brush in blue over black, four drags along the bottom row with a
# smaller brush each time. The ball is the ramp shade brush on the fire
# ramp at 25%, on a layer of its own: one click for a disc on the first rung
# above black, then, with the layer's alpha lock on, seven clicks at one
# point up and to the left of its middle, the brush four cells smaller each
# time (two for the last, so the top colour is wide enough to hold the
# highlight). Each click lifts a smaller disc round the light a rung, and
# the far side, under only the first, keeps the first rung. Then a two-cell
# click for the highlight, and the shade brush's right button lays the
# ball's shadow on the floor. The window shows the shade and ramp shade
# brushes' options, the Layers dock once the ball's layer is locked, and the
# Lint dock before the shadow and at the end.
W, H = 40, 16
FLOOR = [{"name": f"floor-{i + 1}", "action": "shade", **opts, "size": size, "points": [[0, H - 1], [W - 1, H - 1]]}
         for i, (size, opts) in enumerate([(12, {"fg": BLUE, "bg": BLACK, "tip": "square"}), (8, {}), (4, {}), (1, {})])]
BALL = [{"name": "ball-layer", "action": "newCellsLayer", "rename": "ball"},
        {"name": "ball-base", "action": "rampShade", "ramp": "fire", "strength": 0.25, "size": 20, "tip": "round",
         "points": [[19, 7]]}]
LOCK = [{"name": "lock", "action": "layerProperties", "alphaLocked": True}]
LIGHT = (14, 4)


def lit(strength, x=LIGHT[0], y=LIGHT[1]):
    return [{"name": f"lit-{i + 1}", "action": "rampShade", "strength": strength, "size": size, "points": [[x, y]]}
            for i, size in enumerate([29, 25, 21, 17, 13, 9, 7])]


HIGHLIGHT = [{"name": "highlight", "action": "rampShade", "size": 2, "points": [[15, 4]]}]
SHADOW = [{"name": "floor-layer", "action": "setActiveLayer", "layer": "Background"},
          {"name": "shadow-1", "action": "shade", "button": "right", "size": 4, "points": [[17, 13], [26, 13]]},
          {"name": "shadow-2", "action": "shade", "button": "right", "size": 2, "points": [[29, 13], [31, 13]]},
          {"name": "shadow-3", "action": "shade", "button": "right", "size": 2, "points": [[23, 11], [25, 11]]}]


def shot(step, of, crop=None, when=None):
    step = dict(step, screenshot={"of": of})
    if crop:
        step["screenshot"]["crop"] = {"pixels": crop}
    if when:
        step["screenshot"]["when"] = when
    return step


start = blank(W, H)
steps = FLOOR + BALL + LOCK + lit(0.25) + HIGHLIGHT + SHADOW
at = {step["name"]: i for i, step in enumerate(steps)}
for name, args in [("floor-1", ("toolOptions", [0, 0, 256, 603])), ("lock", ("layers",)),
                   ("lit-1", ("toolOptions", [0, 0, 256, 682])), ("highlight", ("lint",)),
                   ("shadow-3", ("lint",))]:
    steps[at[name]] = shot(steps[at[name]], *args)
replay("final", start, steps,
       {"floor-1": "step-01.ans", "floor-4": "step-02.ans", "ball-base": "step-03.ans", "lit-1": "step-04.ans",
        "lit-4": "step-05.ans", "lit-7": "step-06.ans", "highlight": "step-07.ans", "shadow-3": "final.bwp"},
       {"floor-1": "shade-options.png", "lit-1": "ramp-shade-options.png", "lock": "layers.png",
        "highlight": "lint-before.png", "shadow-3": "lint.png"},
       window=[1280, 1300])

# What goes wrong: the ball and its first lit clicks with the strength at
# 100%.
replay("bands", start, FLOOR + [BALL[0], dict(BALL[1], strength=1)] + LOCK + lit(1)[:3], {"lit-3": "bands.ans"})

# Try it: the floor and a flat green disc on the grass ramp, to be lit from
# the upper right. The answer takes the disc down to its first rung above
# black with one right-button click at 75%, then lights it as the finished
# piece is lit, mirrored: the same clicks at the cells across the ball's
# middle (the ball spans columns 9 to 28, so an odd-sized click at x lands
# at 37 - x and the two-cell one at 38 - x), with the shadow to the lower
# left.
TRY = FLOOR + [BALL[0], dict(BALL[1], ramp="grass", strength=1)] + LOCK
replay("try", start, TRY, {"lock": "try.bwp"})
MIRROR = (37 - LIGHT[0], LIGHT[1])
ANSWER = [dict(BALL[1], name="first-rung", button="right", strength=0.75, ramp="grass")]
ANSWER += lit(0.25, *MIRROR) + [dict(HIGHLIGHT[0], points=[[38 - 15, 4]])]
ANSWER += [dict(SHADOW[0]), dict(SHADOW[1], points=[[21, 13], [12, 13]]),
           dict(SHADOW[2], points=[[9, 13], [7, 13]]), dict(SHADOW[3], points=[[15, 11], [13, 11]])]
replay("try-answer", start, TRY + ANSWER, {"shadow-3": "try-answer.ans"})
