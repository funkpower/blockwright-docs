#!/usr/bin/env python3
"""Write tutorial 07's samples: python3 -I samples/07-detail/make.py

Every picture is a steps file played by `blockwright-cli replay` (the CLI is
$BLOCKWRIGHT_CLI, else blockwright-cli on PATH): the editor's own outline
brush, texture stamp, glyph spray, glyph brush, ramp shade brush, shape
tools, selections and layer actions, with the symmetry a step sets, one step
per stroke. This script writes the steps files (*.steps.json) and the blank
canvases they start from (blank-WxH.ans, which carry the SAUCE), replays
each into a scratch directory, and copies the captures the page shows
beside them. The pictures of the editor's docks come from the same steps
played in the window by `blockwright --screenshot` (the editor is
$BLOCKWRIGHT, else blockwright). The texture stamp and the glyph spray take
a fixed seed from their steps, so they paint the same cells every run.
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
DARK_GREY, YELLOW, WHITE = 8, 14, 15
TITLE = "Detail"
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
    """Grey text on black, typed with the Keyboard tool. Typing is mirrored
    under Mirror X, so a label goes in with the symmetry off."""
    return {"name": name, "action": "keyboard", "fg": GREY, "bg": BLACK, "symmetry": "none", "at": [x, y],
            "text": text}


def flat(name, rect, ramp, clicks, tip="square", size=64):
    """Lays a box (or, with a round tip, the disc of that size at its
    middle) in a whole colour of the ramp: ramp shade clicks at 100%, each a
    whole colour, inside a selection of the box."""
    x0, y0, x1, y1 = rect
    middle = [[(x0 + x1) // 2, (y0 + y1) // 2]]
    steps = [{"name": f"{name}-select", "action": "select", "rect": rect}]
    for i in range(clicks):
        step = {"name": name if i == clicks - 1 else f"{name}-{i + 1}", "action": "rampShade", "points": middle}
        if i == 0:
            step.update(ramp=ramp, strength=1, size=size, tip=tip)
        steps.append(step)
    return steps + [{"name": f"{name}-deselect", "action": "deselect"}]


def stamp(name, rect, kind, ramp, density=1.6, seed=1, light="NW"):
    """One texture stamp click, square tip, inside a selection of the box,
    so it stamps the box and nothing round it."""
    x0, y0, x1, y1 = rect
    return [{"name": f"{name}-select", "action": "select", "rect": rect},
            {"name": name, "action": "texture", "ramp": ramp, "light": light, "size": 64, "tip": "square",
             "texture": {"kind": kind, "density": density, "seed": seed},
             "points": [[(x0 + x1) // 2, (y0 + y1) // 2]]},
            {"name": f"{name}-deselect", "action": "deselect"}]


# The idea: a wall as a flat brown box sprinkled with dots, and as the
# texture stamp's brick, many small lit forms.
start = blank(54, 11)
steps = [label("label-dots", 10, 10, "dots"), label("label-forms", 36, 10, "lit forms")]
steps += flat("mass", [1, 1, 24, 8], "wood", 2)
for i, (x, y) in enumerate([(4, 2), (11, 3), (19, 2), (7, 5), (15, 6), (22, 5), (3, 7), (12, 8), (20, 8)]):
    steps.append({"name": f"dot-{i}", "action": "keyboard", "fg": RED, "bg": BROWN, "at": [x, y], "text": "."})
steps += stamp("bricks", [29, 1, 52, 8], "brick", "wood")
replay("idea", start, steps, {"bricks": "idea.ans"})

# The outline brush on two flat discs, yellow on fire and grey on steel,
# one click over each; the window shows its options.
start = blank(40, 12)
steps = flat("yellow", [3, 2, 16, 8], "fire", 3, "round", 14) + flat("grey", [23, 2, 36, 8], "steel", 2, "round", 14)
steps += [{"name": "line-yellow", "action": "outline", "ramp": "fire", "size": 20, "tip": "square", "points": [[9, 5]]},
          {"name": "line-grey", "action": "outline", "ramp": "steel", "points": [[29, 5]]}]
steps[-2] = shot(steps[-2], "toolOptions", [0, 0, 256, 920])
replay("outline", start, steps, {"grey": "outline-before.ans", "line-grey": "outline.ans"},
       {"line-yellow": "outline-options.png"}, window=[1280, 1300])

# Seams: a grey box and a white box touching, twice. The left pair is
# outlined as it is; the right pair with Outline the selection, a selection
# round each box in turn.
start = blank(48, 11)
steps = [label("label-plain", 5, 10, "one shape"), label("label-selection", 28, 10, "two shapes")]
for side, x in [("left", 2), ("right", 26)]:
    steps += flat(f"{side}-grey", [x, 1, x + 9, 8], "steel", 2) + flat(f"{side}-white", [x + 10, 1, x + 19, 8], "steel", 3)
steps += [{"name": "line-left", "action": "outline", "ramp": "steel", "size": 22, "tip": "square", "points": [[11, 4]]},
          {"name": "grey-select", "action": "select", "rect": [26, 1, 35, 8]},
          {"name": "line-grey", "action": "outline", "outline": "selection", "points": [[30, 4]]},
          {"name": "white-select", "action": "select", "rect": [36, 1, 45, 8]},
          {"name": "line-white", "action": "outline", "points": [[40, 4]]},
          {"name": "line-deselect", "action": "deselect"}]
replay("seam", start, steps, {"right-white": "seam-before.ans", "line-deselect": "seam.ans"})

# The texture stamp's five kinds, each in a box of its own, lit from the
# north-west at the default density and seed; the window shows its options.
start = blank(76, 20)
KINDS = [("scales", "sea", 0, 0), ("foliage", "grass", 26, 0), ("hoard", "fire", 52, 0),
         ("brick", "wood", 0, 10), ("noise", "steel", 26, 10)]
steps = []
for kind, ramp, x, y in KINDS:
    steps.append(label(f"label-{kind}", x + 12 - len(kind) // 2, y + 9, kind))
for kind, ramp, x, y in KINDS:
    steps += stamp(kind, [x, y, x + 23, y + 7], kind, ramp)
at = {step["name"]: i for i, step in enumerate(steps)}
steps[at["scales"]] = shot(steps[at["scales"]], "toolOptions", [0, 0, 256, 912])
replay("textures", start, steps, {"noise": "textures.ans"}, {"scales": "texture-options.png"}, window=[1280, 1300])

# Density sets a brick's size: 0.3, 1.6 and 2.5.
start = blank(76, 9)
steps = []
for i, d in enumerate([0.3, 1.6, 2.5]):
    steps.append(label(f"label-{i}", 26 * i + 7, 8, f"density {d}"))
for i, d in enumerate([0.3, 1.6, 2.5]):
    steps += stamp(f"brick-{i}", [26 * i, 0, 26 * i + 23, 6], "brick", "wood", density=d)
replay("density", start, steps, {"brick-2": "density.ans"})

# The glyph spray's stars: a grey disc on black, then one click of white
# stars over the whole canvas; the window shows its options.
start = blank(40, 12)
steps = flat("moon", [5, 2, 18, 8], "steel", 2, "round", 14)
steps += [shot({"name": "stars", "action": "spray", "fg": WHITE, "bg": BLACK, "size": 64, "tip": "square",
                "spray": {"kind": "stars", "density": 100, "seed": 1}, "points": [[20, 6]]},
               "toolOptions", [0, 0, 256, 900])]
replay("stars", start, steps, {"moon": "stars-before.ans", "stars": "stars.ans"}, {"stars": "spray-options.png"},
       window=[1280, 1300])

# Haze and smoke on a blue ground, sea ramp, each in a selection of its own.
start = blank(60, 10)
steps = flat("ground", [0, 0, 59, 9], "sea", 1)
steps += [{"name": "haze-select", "action": "select", "rect": [0, 0, 28, 9]},
          {"name": "haze", "action": "spray", "ramp": "sea", "size": 64, "tip": "square",
           "spray": {"kind": "haze", "density": 30, "seed": 1}, "points": [[14, 5]]},
          {"name": "smoke-select", "action": "select", "rect": [31, 0, 59, 9]},
          {"name": "smoke", "action": "spray", "spray": {"kind": "smoke", "density": 30, "seed": 1}, "points": [[45, 5]]},
          {"name": "smoke-deselect", "action": "deselect"}]
replay("haze", start, steps, {"smoke-deselect": "haze.ans"})

# Symmetry: one stroke of the glyph brush's ▀ along row 1 and one of its ▌
# down column 2, yellow, under each mode in turn.
STROKE = [{"name": "top", "action": "glyph", "glyph": "▀", "fg": YELLOW, "bg": BLACK, "size": 1, "tip": "square",
           "points": [[2, 1], [7, 1]]},
          {"name": "side", "action": "glyph", "glyph": "▌", "points": [[2, 2], [2, 4]]}]
start = blank(21, 7)
for mode, dest in [("none", "sym-off"), ("mirrorX", "sym-x"), ("mirrorY", "sym-y"), ("mirrorXY", "sym-xy")]:
    steps = [dict(STROKE[0], symmetry=mode), STROKE[1]]
    replay(dest, start, steps, {"side": f"{dest}.ans"})
RADIAL = [{"name": "top", "action": "glyph", "glyph": "▀", "fg": YELLOW, "bg": BLACK, "size": 1, "tip": "square",
           "points": [[22, 2], [27, 2]]},
          {"name": "side", "action": "glyph", "glyph": "▌", "points": [[22, 3], [22, 5]]}]
start = blank(41, 17)
for folds in [4, 6]:
    steps = [dict(RADIAL[0], symmetry={"mode": "radial", "folds": folds}), RADIAL[1]]
    replay(f"radial-{folds}", start, steps, {"side": f"radial-{folds}.ans"})

# The finished piece: a brick wall with battlements and a gate under a moon
# and stars, lit from the north-west, on two layers. The wall is the texture
# stamp's brick on wood; the battlements black notches cut with the
# Rectangle under Mirror X; the gate a black arch; the moon a white disc on
# steel; the stars the glyph spray's; the door, on a layer of its own, a
# grey arch outlined by the outline brush.
W, H = 60, 20
WALL = stamp("wall", [0, 9, W - 1, H - 1], "brick", "wood", seed=69)
NOTCHES = [{"name": "notch-1", "action": "rectangle", "fg": BLACK, "filled": True, "symmetry": "mirrorX",
            "from": [3, 18], "to": [6, 23]},
           {"name": "notch-2", "action": "rectangle", "from": [13, 18], "to": [16, 23]},
           {"name": "notch-3", "action": "rectangle", "from": [23, 18], "to": [26, 23]}]
GATE = [{"name": "gate-arch", "action": "ellipse", "fg": BLACK, "filled": True, "symmetry": "none",
         "from": [25, 25], "to": [34, 37]},
        {"name": "gate", "action": "rectangle", "from": [25, 31], "to": [34, 39]}]
MOON = flat("moon", [4, 1, 11, 5], "steel", 3, "round", 7)
STARS = [{"name": "stars", "action": "spray", "fg": WHITE, "bg": BLACK, "size": 64, "tip": "square",
          "spray": {"kind": "stars", "density": 60, "seed": 1}, "points": [[30, 4]]}]
DOOR = [{"name": "door-layer", "action": "newCellsLayer", "rename": "door"},
        {"name": "door-arch", "action": "ellipse", "fg": GREY, "filled": True, "from": [26, 28], "to": [33, 36]},
        {"name": "door", "action": "rectangle", "from": [26, 32], "to": [33, 39]}]
LINE = [{"name": "door-line", "action": "outline", "ramp": "steel", "size": 20, "tip": "square", "points": [[29, 16]]}]
CHECK = [{"name": "check", "action": "deselect"}]

start = blank(W, H)
steps = WALL + NOTCHES + GATE + MOON + STARS + DOOR + LINE + CHECK
at = {step["name"]: i for i, step in enumerate(steps)}
for name, args in [("door-line", ("layers", [0, 0, 310, 205])), ("check", ("lint",))]:
    steps[at[name]] = shot(steps[at[name]], *args)
replay("final", start, steps,
       {"wall-deselect": "step-01.ans", "notch-3": "step-02.ans", "gate": "step-03.ans", "moon": "step-04.ans",
        "stars": "step-05.ans", "door": "step-06.ans", "door-line": "final.bwp"},
       {"door-line": "layers.png", "check": "lint.png"},
       window=[1280, 1300])

# What goes wrong. The wall stamped under Mirror X: the right half is lit
# from the north-east. And the outline brush run over the wall too.
MIRRORED = [dict(WALL[0]), dict(WALL[1], symmetry="mirrorX"), dict(WALL[2])]
replay("mirror-light", start, MIRRORED, {"wall": "mirror-light.ans"})
STICKERS = [{"name": "wall-active", "action": "setActiveLayer", "layer": "Background"},
            {"name": "wall-line", "action": "outline", "ramp": "wood", "size": 64, "tip": "square",
             "points": [[30, 14]]}]
replay("stickers", start, WALL + NOTCHES + GATE + STICKERS, {"wall-line": "stickers.ans"})
# The stars sprayed with Mirror X still on from the battlements.
replay("stars-mirrored", start, WALL + NOTCHES + GATE + MOON + [dict(STARS[0], symmetry="mirrorX")],
       {"stars": "stars-mirrored.ans"})

# Try it: the wall, the gate and the moon, no battlements and no stars. The
# answer cuts two notches a side under Mirror X and sprays stars with the
# symmetry off, seed 2.
TRY = WALL + GATE + MOON
replay("try", start, TRY, {"moon": "try.bwp"})
ANSWER = [dict(NOTCHES[0], **{"from": [5, 18], "to": [8, 23]}),
          dict(NOTCHES[1], **{"from": [15, 18], "to": [18, 23]}),
          dict(STARS[0], symmetry="none", spray={"kind": "stars", "density": 60, "seed": 2})]
replay("try-answer", start, TRY + ANSWER, {"stars": "try-answer.ans"})
