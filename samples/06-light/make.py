#!/usr/bin/env python3
"""Write tutorial 06's samples: python3 -I samples/06-light/make.py

Every picture is a steps file played by `blockwright-cli replay` (the CLI is
$BLOCKWRIGHT_CLI, else blockwright-cli on PATH): the editor's own ramp
gradient, ramp shade, form and rim light brushes, selections and layer
actions, one step per stroke. This script writes the steps files
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
TITLE = "Light"
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


def dome(name, x, y, size, light, rim=False, glint=True):
    """A disc of steel's first rung on a layer of its own, locked, and one
    form brush click at 100% over it, as a dome lit from light."""
    return [{"name": f"{name}-layer", "action": "newCellsLayer", "rename": name},
            {"name": f"{name}-base", "action": "rampShade", "ramp": "steel", "strength": 0.25, "size": size,
             "tip": "round", "points": [[x, y]]},
            {"name": f"{name}-lock", "action": "layerProperties", "alphaLocked": True},
            {"name": name, "action": "form", "light": light, "strength": 1, "size": size + 10, "tip": "square",
             "form": {"shape": "dome", "rim": rim, "specular": glint}, "points": [[x, y]]}]


def grey(name, rect, tip="square", size=64):
    """Fills a box (or, with a round tip, the disc of that size at its middle)
    with solid grey, steel rung 8: two ramp shade clicks at 100%, each a whole
    colour, inside a selection of the box."""
    x0, y0, x1, y1 = rect
    middle = [[(x0 + x1) // 2, (y0 + y1) // 2]]
    return [{"name": f"{name}-select", "action": "select", "rect": rect},
            {"name": f"{name}-1", "action": "rampShade", "ramp": "steel", "strength": 1, "size": size, "tip": tip,
             "points": middle},
            {"name": name, "action": "rampShade", "points": middle},
            {"name": f"{name}-deselect", "action": "deselect"}]


def rim(name, rect, light, keep_lint=False):
    """One rim light brush click, square tip, inside a selection of the box,
    so it reaches only the shape laid in it."""
    x0, y0, x1, y1 = rect
    return [{"name": f"{name}-select", "action": "select", "rect": rect},
            {"name": name, "action": "rimLight", "ramp": "steel", "light": light, "size": 64, "tip": "square",
             "keepLint": keep_lint, "points": [[(x0 + x1) // 2, (y0 + y1) // 2]]},
            {"name": f"{name}-deselect", "action": "deselect"}]


# The idea: four domes the same size, two pairs. The left pair are both lit
# from the north-west; in the right pair one is lit from the north-west and
# one from the north-east.
start = blank(72, 10)
steps = [label("label-one", 13, 9, "one light"), label("label-two", 49, 9, "two lights")]
for name, x, light in [("a", 9, "NW"), ("b", 27, "NW"), ("c", 45, "NW"), ("d", 63, "NE")]:
    steps += dome(name, x, 4, 14, light)
replay("idea", start, steps, {"d": "idea.ans"})

# The form brush's Light, a compass rose: eight domes, each lit from the
# point of the compass it stands at.
ROSE = [["NW", "N", "NE"], ["W", None, "E"], ["SW", "S", "SE"]]
start = blank(54, 28)
labels, bodies = [], []
for r, row in enumerate(ROSE):
    for c, light in enumerate(row):
        x, y = 10 + 18 * c, 4 + 9 * r
        if light is None:
            labels.append(label("label-middle", x - 4, y, "light from"))
            continue
        labels.append(label(f"label-{light.lower()}", x - len(light) // 2, y + 5, light))
        bodies += dome(light.lower(), x, y, 14, light)
replay("light-rose", start, labels + bodies, {bodies[-1]["name"]: "light-rose.ans"})

# The rim light brush on a plain shape: a flat grey disc on a layer of its
# own, and one click lit from the north-west.
start = blank(25, 11)
DISC = [{"name": "disc-layer", "action": "newCellsLayer", "rename": "disc"}] + grey("disc", [5, 1, 19, 9], "round", 14)
replay("rim", start, DISC + rim("rim", [5, 1, 19, 9], "NW"), {"disc": "rim-before.ans", "rim": "rim-after.ans"})

# The rim light's Light, a compass rose: eight flat grey discs on one layer,
# each lit, inside a selection of its own, from the point it stands at.
start = blank(54, 28)
labels, bodies = [], [{"name": "discs-layer", "action": "newCellsLayer", "rename": "discs"}]
for r, row in enumerate(ROSE):
    for c, light in enumerate(row):
        x, y = 10 + 18 * c, 4 + 9 * r
        if light is None:
            labels.append(label("label-middle", x - 4, y, "light from"))
            continue
        labels.append(label(f"label-{light.lower()}", x - len(light) // 2, y + 5, light))
        box = [x - 7, y - 3, x + 7, y + 3]
        bodies += grey(f"disc-{light.lower()}", box, "round", 14) + rim(f"rim-{light.lower()}", box, light)
replay("rim-rose", start, labels + bodies, {bodies[-1]["name"]: "rim-rose.ans"})

# Keep the lint clean: two domes lit from the north-west by the form brush,
# then both rimmed from the north-west, the left with the option off and
# the right with it on.
start = blank(56, 14)
steps = [label("label-off", 7, 13, "lint not kept"), label("label-on", 37, 13, "lint kept clean")]
SIDES = [("off", 13, False), ("on", 43, True)]
for name, x, keep in SIDES:
    steps += dome(name, x, 6, 20, "NW")
for name, x, keep in SIDES:
    steps += [{"name": f"{name}-active", "action": "setActiveLayer", "layer": name}]
    steps += rim(f"rim-{name}", [x - 10, 1, x + 10, 11], "NW", keep)
replay("rim-lint", start, steps, {"on": "rim-lint-before.ans", "rim-on": "rim-lint.ans"})

# The form brush's glint: two domes 28 across lit from the north-east, the
# left with Glint off and the right with it on.
start = blank(68, 16)
steps = [label("label-off", 12, 15, "Glint off"), label("label-on", 46, 15, "Glint on")]
steps += dome("off", 17, 7, 28, "NE", glint=False)
steps += dome("on", 51, 7, 28, "NE", glint=True)
replay("glint", start, steps, {"on": "glint.ans"})

# The form brush's rim light: two domes 20 across lit from the north-east,
# the left with Form rim light off and the right with it on.
start = blank(52, 13)
steps = [label("label-off", 4, 12, "Form rim light off"), label("label-on", 31, 12, "Form rim light on")]
steps += dome("off", 13, 6, 20, "NE", rim=False)
steps += dome("on", 39, 6, 20, "NE", rim=True)
replay("form-rim", start, steps, {"on": "form-rim.ans"})

# Where the rim light can't help: thin bars. A stem a column wide and one
# two wide, a bar a row tall and one two tall, all grey on one layer, each
# rimmed from the north-west inside a selection of its own.
start = blank(36, 12)
THIN = {"stem-1": [5, 1, 5, 8], "stem-2": [11, 1, 12, 8], "bar-1": [18, 2, 31, 2], "bar-2": [18, 6, 31, 7]}
steps = [label("label-stems", 4, 10, "stems"), label("label-bars", 22, 10, "bars"),
         {"name": "thin-layer", "action": "newCellsLayer", "rename": "thin"}]
for name, rect in THIN.items():
    steps += grey(name, rect)
lit = []
for name, rect in THIN.items():
    lit += rim(f"rim-{name}", rect, "NW")
replay("thin", start, steps + lit, {"bar-2": "thin-before.ans", lit[-2]["name"]: "thin.ans"})

# Counters: a grey box with a one-cell hole, the hole's cells taken back to
# empty by two ramp shade clicks at 100% with the right button, then rimmed
# from the north-west.
start = blank(20, 10)
BOX = [3, 1, 16, 8]
steps = ([{"name": "box-layer", "action": "newCellsLayer", "rename": "box"}] + grey("box", BOX) +
         [{"name": "hole-select", "action": "select", "rect": [9, 4, 9, 4]},
          {"name": "hole-1", "action": "rampShade", "ramp": "steel", "button": "right", "strength": 1, "size": 1,
           "tip": "square", "points": [[9, 4]]},
          {"name": "hole", "action": "rampShade", "button": "right", "points": [[9, 4]]},
          {"name": "hole-deselect", "action": "deselect"}] + rim("rim", BOX, "NW"))
replay("counter", start, steps, {"hole": "counter-before.ans", "rim": "counter.ans"})

# Canvas edges: the same grey box twice on one layer, the left on the
# canvas's first column and the right further in, both rimmed from the east.
start = blank(30, 10)
EDGE = {"edge": [0, 2, 5, 7], "inside": [14, 2, 19, 7]}
steps = [{"name": "boxes-layer", "action": "newCellsLayer", "rename": "boxes"}]
for name, rect in EDGE.items():
    steps += grey(name, rect)
for name, rect in EDGE.items():
    steps += rim(f"rim-{name}", rect, "E")
replay("edge", start, steps, {"rim-inside": "edge.ans"})

# The finished piece: a boulder and a standing stone on two hills under a
# sky, lit from the north-east, on four layers. The sky is a radial ramp
# gradient on the sea ramp, brightest at the top right corner; the hills two
# grass discs on a layer of their own, locked, shaded by a linear gradient
# and rimmed from the north-east with the lint kept clean. The boulder and
# the stone are discs of steel's first rung, each on its own layer, locked
# and shaded as domes lit from the north-east: the boulder with Glint, the
# stone with Form rim light. The window shows the rim light's and the form
# brush's options, the Layers dock and the Lint dock at the end.
W, H = 60, 20
SKY = [{"name": "sky-select", "action": "select", "rect": [0, 0, W - 1, H - 1]},
       {"name": "sky", "action": "gradient", "ramp": "sea",
        "gradient": {"shape": "radial", "banding": "cells", "from": 10, "to": 2}, "from": [W - 1, 0], "to": [0, H - 1]},
       {"name": "sky-deselect", "action": "deselect"}]
HILLS = [{"name": "hills-layer", "action": "newCellsLayer", "rename": "hills"},
         {"name": "hill-1", "action": "rampShade", "ramp": "grass", "strength": 1, "size": 36, "tip": "round",
          "points": [[14, 19]]},
         {"name": "hill-2", "action": "rampShade", "size": 44, "points": [[48, 19]]},
         {"name": "hills-lock", "action": "layerProperties", "alphaLocked": True},
         {"name": "hills", "action": "gradient", "gradient": {"shape": "linear", "banding": "cells", "from": 3, "to": 6},
          "from": [0, 19], "to": [0, 10]}]
HILLS_RIM = [{"name": "hills-rim", "action": "rimLight", "light": "NE", "size": 64, "tip": "square",
              "keepLint": True, "points": [[30, 12]]}]
BOULDER = dome("boulder", 42, 12, 28, "NE", rim=False, glint=True)
STONE = dome("stone", 14, 14, 16, "NE", rim=True, glint=False)
CHECK = [{"name": "check", "action": "deselect"}]

start = blank(W, H)
steps = SKY + HILLS + HILLS_RIM + BOULDER + STONE + CHECK
at = {step["name"]: i for i, step in enumerate(steps)}
for name, args in [("hills-rim", ("toolOptions", [0, 0, 256, 750])), ("stone", ("toolOptions", [0, 0, 256, 812])),
                   ("stone-lock", ("layers", [0, 0, 310, 205])), ("check", ("lint",))]:
    steps[at[name]] = shot(steps[at[name]], *args)
replay("final", start, steps,
       {"sky": "step-01.ans", "hills": "step-02.ans", "hills-rim": "step-03.ans", "boulder": "step-04.ans",
        "stone": "final.bwp"},
       {"hills-rim": "rim-options.png", "stone": "form-options.png", "stone-lock": "layers.png",
        "check": "lint.png"},
       window=[1280, 1300])

# What goes wrong. The stone lit from the north-west in a scene lit from
# the north-east; and the rim light brush, from the north-east, run over the
# boulder and the stone as well as the hills.
replay("two-lights", start, SKY + HILLS + HILLS_RIM + BOULDER + dome("stone", 14, 14, 16, "NW", rim=True, glint=False),
       {"stone": "two-lights.ans"})
STICKERS = [{"name": "boulder-rim", "action": "setActiveLayer", "layer": "boulder"},
            dict(HILLS_RIM[0], name="boulder-rimmed", keepLint=False),
            {"name": "stone-rim", "action": "setActiveLayer", "layer": "stone"},
            dict(HILLS_RIM[0], name="stone-rimmed", keepLint=False)]
replay("stickers", start, SKY + HILLS + HILLS_RIM + BOULDER + STONE + STICKERS, {"stone-rimmed": "stickers.ans"})

# Try it: the same hills and shapes under a sky brightest at the top left,
# the hills shaded but not rimmed, the boulder and the stone laid and locked
# but not shaded. The answer lights them all from the north-west.
TRY_SKY = [SKY[0], dict(SKY[1], **{"from": [0, 0], "to": [W - 1, H - 1]}), SKY[2]]
TRY = TRY_SKY + HILLS + BOULDER[:3] + STONE[:3]
replay("try", start, TRY, {"stone-lock": "try.bwp"})
ANSWER = [{"name": "boulder-active", "action": "setActiveLayer", "layer": "boulder"},
          dict(BOULDER[3], light="NW"),
          dict(STONE[3], light="NW"),
          {"name": "hills-active", "action": "setActiveLayer", "layer": "hills"},
          dict(HILLS_RIM[0], ramp="grass", light="NW")]
ANSWER.insert(2, {"name": "stone-active", "action": "setActiveLayer", "layer": "stone"})
replay("try-answer", start, TRY + ANSWER, {"hills-rim": "try-answer.ans"})
