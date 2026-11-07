#!/usr/bin/env python3
"""Write tutorial 05's samples: python3 -I samples/05-shading-forms-and-falloff/make.py

Every picture is a steps file played by `blockwright-cli replay` (the CLI is
$BLOCKWRIGHT_CLI, else blockwright-cli on PATH): the editor's own ramp
gradient, form, soft, smudge, ramp shade and despeckle brushes, selections
and layer actions, one step per stroke. This script writes the steps files
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
TITLE = "Shading: forms and falloff"
DATE = "20261105"
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"


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


def shot(step, of, crop=None):
    step = dict(step, screenshot={"of": of})
    if crop:
        step["screenshot"]["crop"] = {"pixels": crop}
    return step


def label(name, x, y, text):
    return {"name": name, "action": "keyboard", "fg": GREY, "bg": BLACK, "at": [x, y], "text": text}


def field(name, ramp, rect, rung):
    """Fills a box with one rung of a ramp: ramp shade clicks on a selection
    of the box with a square tip bigger than it, at 100% for each whole
    colour (four rungs) and then one at the rest."""
    x0, y0, x1, y1 = rect
    middle = [[(x0 + x1) // 2, (y0 + y1) // 2]]
    clicks = [1] * (rung // 4) + ([rung % 4 / 4] if rung % 4 else [])
    steps = [{"name": f"{name}-select", "action": "select", "rect": rect}]
    for i, strength in enumerate(clicks):
        steps.append({"name": name if i == len(clicks) - 1 else f"{name}-{i + 1}", "action": "rampShade",
                      "ramp": ramp, "strength": strength, "size": 64, "tip": "square", "points": middle})
    return steps + [{"name": f"{name}-deselect", "action": "deselect"}]


# The idea: the same fire disc twice, each on a layer of its own with alpha
# lock on. The left is lit as in tutorial 04: seven ramp shade clicks at 25%
# round a point up and to the left of its middle, each four cells smaller
# than the one before (two for the last). The right is shaded by one click
# of the form brush at 100%.
start = blank(44, 13)
steps = [label("label-clicks", 2, 12, "ramp shade clicks"), label("label-form", 29, 12, "form brush")]
for name, x in [("clicks", 11), ("form", 33)]:
    steps += [{"name": f"{name}-layer", "action": "newCellsLayer", "rename": name},
              {"name": f"{name}-disc", "action": "rampShade", "ramp": "fire", "strength": 0.25, "size": 20,
               "tip": "round", "points": [[x, 6]]},
              {"name": f"{name}-lock", "action": "layerProperties", "alphaLocked": True}]
    if name == "clicks":
        steps += [{"name": f"lit-{i + 1}", "action": "rampShade", "size": size, "points": [[x - 5, 3]]}
                  for i, size in enumerate([29, 25, 21, 17, 13, 9, 7])]
steps.append({"name": "form", "action": "form", "strength": 1, "size": 30, "form": {"shape": "dome"},
              "points": [[33, 6]]})
replay("idea", start, steps, {"form": "idea.ans"})

# The ramp gradient on a plain shape: a bar of solid violet (rung 4), then a linear gradient across it
# from rung 0 at the left to the top rung at the right.
start = blank(36, 3)
BAR = [0, 0, 35, 2]
steps = field("bar", "violet", BAR, 4) + [
    {"name": "select", "action": "select", "rect": BAR},
    {"name": "gradient", "action": "gradient", "gradient": {"shape": "linear", "banding": "cells", "from": 0, "to": 12},
     "from": [0, 0], "to": [35, 0]}]
replay("gradient", start, steps, {"bar": "gradient-before.ans", "gradient": "gradient-after.ans"})

# The gradient's settings, a labelled row each, every row a 36 x 3 box on
# the violet ramp, cell-banded: linear from rung 0 to 12; radial from the
# box's middle out to its right end, from the top rung to rung 0; and linear
# from rung 4 to rung 8.
LABEL = 12
ROWS = [("linear", "linear", "cells", 0, 12), ("radial", "radial", "cells", 12, 0),
        ("rung 4 to 8", "linear", "cells", 4, 8)]
start = blank(LABEL + 36, 4 * len(ROWS) - 1)
steps = []
for i, (text, shape, banding, a, b) in enumerate(ROWS):
    y = 4 * i
    x0, x1 = LABEL, LABEL + 35
    steps.append(label(f"label-{i + 1}", 0, y + 1, text))
    steps.append({"name": f"select-{i + 1}", "action": "select", "rect": [x0, y, x1, y + 2]})
    origin = [x0, y + 1] if shape == "linear" else [x0 + 18, y + 1]
    steps.append({"name": f"fill-{i + 1}", "action": "gradient", "ramp": "violet",
                  "gradient": {"shape": shape, "banding": banding, "from": a, "to": b},
                  "from": origin, "to": [x1, y + 1]})
steps.append({"name": "deselect", "action": "deselect"})
replay("gradient-settings", start, steps, {"deselect": "gradient-settings.ans"})

# The form brush on a plain shape: a flat disc of dark grey on a layer of
# its own (one ramp shade click at 100% on the steel ramp lifts the empty
# cells a whole colour),
# then, with alpha lock on, one form brush click at 100% over it, as a dome,
# lit from the north-west.
start = blank(26, 13)
DISC = [{"name": "disc-layer", "action": "newCellsLayer", "rename": "disc"},
        {"name": "disc", "action": "rampShade", "ramp": "steel", "strength": 1, "size": 20, "tip": "round",
         "points": [[12, 6]]},
        {"name": "lock", "action": "layerProperties", "alphaLocked": True}]
steps = DISC + [{"name": "form", "action": "form", "strength": 1, "size": 30, "form": {"shape": "dome"},
                 "points": [[12, 6]]}]
replay("form", start, steps, {"disc": "form-before.ans", "form": "form-after.ans"})

# What goes wrong: the same click at 25%.
steps = DISC + [{"name": "form", "action": "form", "strength": 0.25, "size": 30, "form": {"shape": "dome"},
                 "points": [[12, 6]]}]
replay("form-weak", start, steps, {"form": "form-weak.ans"})

# Form, a labelled shape each, each on a layer of its own with alpha lock on,
# laid at dark grey as above and shaded by one click at 100%: a dome on a
# disc, a cylinder on an upright bar, a plane on a box.
start = blank(56, 13)
SHAPES = [("dome", 9, [[9, 6]], "round", 16, None),
          ("cylinder", 26, [[26, 6]], "square", 30, [22, 1, 30, 11]),
          ("plane", 45, [[45, 6]], "square", 30, [38, 2, 52, 10])]
steps = [label(f"label-{shape}", x - len(shape) // 2, 12, shape) for shape, x, *_ in SHAPES]
for i, (shape, x, points, tip, size, rect) in enumerate(SHAPES):
    steps.append({"name": f"{shape}-layer", "action": "newCellsLayer", "rename": shape})
    if rect:
        steps.append({"name": f"{shape}-select", "action": "select", "rect": rect})
    steps.append({"name": f"{shape}-base", "action": "rampShade", "ramp": "steel", "strength": 1, "size": size,
                  "tip": tip, "points": points})
    if rect:
        steps.append({"name": f"{shape}-deselect", "action": "deselect"})
    steps.append({"name": f"{shape}-lock", "action": "layerProperties", "alphaLocked": True})
    steps.append({"name": shape, "action": "form", "strength": 1, "size": 30, "tip": "square",
                  "form": {"shape": shape}, "points": points})
replay("form-shapes", start, steps, {"plane": "form-shapes.ans"})

# The soft brush on a plain shape: a field of solid brown (wood rung 8),
# one click at 50% with the left button, and on the same field one with the
# right.
start = blank(30, 9)
FIELD = field("field", "wood", [0, 0, 29, 8], 8)
SOFT = {"name": "soft", "action": "soft", "ramp": "wood", "strength": 0.5, "size": 11, "tip": "round",
        "hardness": 0, "points": [[14, 4]]}
replay("soft", start, FIELD + [SOFT], {"field": "soft-before.ans", "soft": "soft-after.ans"})
replay("soft-right", start, FIELD + [dict(SOFT, button="right")], {"soft": "soft-right.ans"})

# Hardness, a labelled row: the same click on the same field at 100%, with
# Hardness at 0%, 50% and 100%.
HARD = [0, 0.5, 1]
start = blank(14 * len(HARD), 10)
steps = field("field", "wood", [0, 0, 14 * len(HARD) - 1, 8], 8)
for i, h in enumerate(HARD):
    x = 14 * i + 6
    steps.append(label(f"label-{i + 1}", x - 1, 9, f"{round(h * 100)}%"))
    steps.append({"name": f"soft-{i + 1}", "action": "soft", "ramp": "wood", "strength": 1, "size": 11,
                  "tip": "round", "hardness": h, "points": [[x, 4]]})
replay("hardness", start, steps, {steps[-1]["name"]: "hardness.ans"})

# The smudge brush on a plain shape: a field of wood rung 8 on the left and
# rung 6 on the right, and one size 1 drag at 50% across the edge, from
# column 16 to column 30.
start = blank(40, 1)
EDGE = field("left", "wood", [0, 0, 19, 0], 8) + field("right", "wood", [20, 0, 39, 0], 6)
DRAG = {"name": "smudge", "action": "smudge", "ramp": "wood", "strength": 0.5, "size": 1, "tip": "square",
        "points": [[16, 0], [30, 0]]}
replay("smudge", start, EDGE + [DRAG], {"right": "smudge-before.ans", "smudge": "smudge-after.ans"})

# Strength, a labelled row: the same drag on the same edge at 25%, 50%, 75%
# and 100%.
STRENGTHS = [0.25, 0.5, 0.75, 1.0]
LABEL = 5
start = blank(LABEL + 40, 2 * len(STRENGTHS) - 1)
steps = []
for i, s in enumerate(STRENGTHS):
    y = 2 * i
    steps.append(label(f"label-{i + 1}", 0, y, f"{round(s * 100)}%"))
    steps += field(f"left-{i + 1}", "wood", [LABEL, y, LABEL + 19, y], 8)
    steps += field(f"right-{i + 1}", "wood", [LABEL + 20, y, LABEL + 39, y], 6)
    steps.append(dict(DRAG, name=f"smudge-{i + 1}", strength=s, points=[[LABEL + 16, y], [LABEL + 30, y]]))
replay("smudge-strength", start, steps, {steps[-1]["name"]: "smudge-strength.ans"})

# The despeckle brush on a plain shape: a field of wood rung 6 with single
# cells moved by size 1 ramp shade clicks: one a rung up, one a rung down,
# one two rungs up, a pair of cells a rung up, one at the top rung and one
# at black. Then one despeckle stroke over the whole field.
start = blank(36, 5)
steps = field("field", "wood", [0, 0, 35, 4], 6) + [
    {"name": "up", "action": "rampShade", "ramp": "wood", "strength": 0.25, "size": 1, "tip": "square",
     "points": [[3, 2]]},
    {"name": "down", "action": "rampShade", "button": "right", "points": [[8, 2]]},
    {"name": "up-2", "action": "rampShade", "strength": 0.5, "points": [[13, 2]]},
    {"name": "pair", "action": "rampShade", "strength": 0.25, "points": [[18, 2], [19, 2]]},
    {"name": "top", "action": "rampShade", "strength": 1, "points": [[25, 2]]},
    {"name": "top-2", "action": "rampShade", "points": [[25, 2]]},
    {"name": "black", "action": "rampShade", "button": "right", "points": [[31, 2]]},
    {"name": "black-2", "action": "rampShade", "button": "right", "points": [[31, 2]]},
    {"name": "despeckle", "action": "despeckle", "ramp": "wood", "size": 5, "tip": "square",
     "points": [[0, 2], [35, 2]]}]
replay("despeckle", start, steps, {"black-2": "despeckle-before.ans", "despeckle": "despeckle-after.ans"})

# The finished piece: a pillar and a ball in front of a wall, on a floor, on
# three layers. The wall and the floor are ramp gradients, each filling a
# selection: the wall radial on the violet ramp, from the top left corner;
# the floor linear on the wood ramp, from left to right. The pillar is a
# selection filled with steel's first rung and shaded as a cylinder; the
# ball a disc of sea's first rung, locked, and shaded as a dome. Back on the
# background, the soft brush's right button lays the shadows, the smudge
# brush drags the pillar's along the floor, and the despeckle brush cleans
# the specks left by a few size 1 clicks of wear. The window shows each
# tool's options, the Layers dock once the ball is locked, and the Lint dock
# before and after the despeckle.
W, H = 52, 18
WALL = [{"name": "wall-select", "action": "select", "rect": [0, 0, W - 1, 11]},
        {"name": "wall", "action": "gradient", "ramp": "violet",
         "gradient": {"shape": "radial", "banding": "cells", "from": 8, "to": 1}, "from": [0, 0], "to": [40, 11]}]
FLOOR = [{"name": "floor-select", "action": "select", "rect": [0, 12, W - 1, H - 1]},
         {"name": "floor", "action": "gradient", "ramp": "wood",
          "gradient": {"shape": "linear", "banding": "cells", "from": 8, "to": 4}, "from": [16, 12], "to": [W - 1, 12]},
         {"name": "deselect", "action": "deselect"}]
PILLAR = [{"name": "pillar-layer", "action": "newCellsLayer", "rename": "pillar"},
          {"name": "pillar-select", "action": "select", "rect": [6, 1, 15, 14]},
          {"name": "pillar-base", "action": "rampShade", "ramp": "steel", "strength": 0.25, "size": 30,
           "tip": "square", "points": [[10, 7]]},
          {"name": "pillar", "action": "form", "strength": 1, "form": {"shape": "cylinder"}, "points": [[10, 7]]},
          {"name": "pillar-deselect", "action": "deselect"}]
BALL = [{"name": "ball-layer", "action": "newCellsLayer", "rename": "ball"},
        {"name": "ball-base", "action": "rampShade", "ramp": "sea", "strength": 0.25, "size": 22, "tip": "round",
         "points": [[35, 10]]},
        {"name": "lock", "action": "layerProperties", "alphaLocked": True},
        {"name": "ball", "action": "form", "strength": 1, "size": 30, "form": {"shape": "dome"}, "points": [[35, 10]]}]
SHADOWS = [{"name": "floor-layer", "action": "setActiveLayer", "layer": "Background"},
           {"name": "shadow-1", "action": "soft", "ramp": "wood", "strength": 0.5, "size": 8, "tip": "round",
            "hardness": 0, "button": "right", "points": [[17, 14], [21, 14]]},
           {"name": "shadow-2", "action": "soft", "button": "right", "points": [[48, 15], [51, 15]]}]
SMUDGE = [{"name": "smudge", "action": "smudge", "strength": 0.5, "size": 2, "tip": "square",
           "points": [[21, 14], [27, 14]]}]
WEAR = [{"name": "wear-1", "action": "rampShade", "strength": 0.25, "size": 1, "tip": "square", "points": [[3, 13]]},
        {"name": "wear-2", "action": "rampShade", "button": "right", "points": [[11, 16]]},
        {"name": "wear-3", "action": "rampShade", "points": [[36, 16], [37, 16]]}]
CLEAN = [{"name": "despeckle", "action": "despeckle", "size": 12, "tip": "square", "points": [[0, 15], [W - 1, 15]]},
         {"name": "check", "action": "deselect"}]

start = blank(W, H)
steps = WALL + FLOOR + PILLAR + BALL + SHADOWS + SMUDGE + WEAR + CLEAN
at = {step["name"]: i for i, step in enumerate(steps)}
for name, args in [("wall", ("toolOptions", [0, 0, 256, 967])), ("pillar", ("toolOptions", [0, 0, 256, 890])),
                   ("lock", ("layers",)), ("shadow-1", ("toolOptions", [0, 0, 256, 756])),
                   ("smudge", ("toolOptions", [0, 0, 256, 701])), ("wear-3", ("lint",)),
                   ("despeckle", ("toolOptions", [0, 0, 256, 632])), ("check", ("lint",))]:
    steps[at[name]] = shot(steps[at[name]], *args)
replay("final", start, steps,
       {"wall": "step-01.ans", "floor": "step-02.ans", "pillar-base": "step-03.ans", "pillar": "step-04.ans",
        "ball-base": "step-05.ans", "ball": "step-06.ans", "shadow-2": "step-07.ans", "smudge": "step-08.ans",
        "wear-3": "step-09.ans", "despeckle": "final.bwp"},
       {"wall": "gradient-options.png", "pillar": "form-options.png", "lock": "layers.png",
        "shadow-1": "soft-options.png", "smudge": "smudge-options.png", "wear-3": "lint-before.png",
        "despeckle": "despeckle-options.png", "check": "lint.png"},
       window=[1280, 1300])

# What goes wrong. The wall's gradient with no selection fills the whole
# layer. The ball's form on its layer with no disc under it: the form brush
# leaves a cell whose tone is black as it was, so the empty cells on its
# shadow side stay empty and show the wall and the floor.
replay("no-selection", start, [dict(WALL[1])], {"wall": "no-selection.ans"})
NO_BASE = [BALL[0], dict(BALL[3], ramp="sea", tip="round", size=22)]
replay("no-base", start, WALL + FLOOR + NO_BASE, {"ball": "no-base.ans"})

# Try it: the wall and the floor, with a log lying on the floor: a box of
# steel's first rung on a layer of its own, locked. The answer shades it as
# a cylinder at 100% and lays its shadow with the soft brush's right button
# on the background.
LOG = [{"name": "log-layer", "action": "newCellsLayer", "rename": "log"},
       {"name": "log-select", "action": "select", "rect": [20, 11, 43, 15]},
       {"name": "log-base", "action": "rampShade", "ramp": "steel", "strength": 0.25, "size": 30, "tip": "square",
        "points": [[31, 13]]},
       {"name": "log-deselect", "action": "deselect"},
       {"name": "lock", "action": "layerProperties", "alphaLocked": True}]
TRY = WALL + FLOOR + LOG
replay("try", start, TRY, {"lock": "try.bwp"})
ANSWER = [{"name": "log", "action": "form", "ramp": "steel", "strength": 1, "size": 30, "tip": "square",
           "form": {"shape": "cylinder"}, "points": [[31, 13]]},
          {"name": "floor-layer", "action": "setActiveLayer", "layer": "Background"},
          {"name": "shadow", "action": "soft", "ramp": "wood", "strength": 0.5, "size": 6, "tip": "round",
           "hardness": 0, "button": "right", "points": [[24, 16], [46, 16]]}]
replay("try-answer", start, TRY + ANSWER, {"shadow": "try-answer.ans"})
