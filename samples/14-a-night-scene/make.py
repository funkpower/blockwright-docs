#!/usr/bin/env python3
"""Write tutorial 14's samples: python3 -I samples/14-a-night-scene/make.py

Every picture is a steps file played by `blockwright-cli replay --project`
(the CLI is $BLOCKWRIGHT_CLI, else blockwright-cli on PATH) from a blank
60 x 24 canvas (blank.ans, which carries the SAUCE record): the sky's two ramp gradients, the stars sprayed inside a
selection, then a Pixels layer each for the moon, the far trees and the
near trees, drawn with the Ellipse, Rectangle, Line and Fill tools. This
script writes the steps files (*.steps.json), replays each into a scratch
directory, and copies the projects the page shows beside them. The picture
of the Layers dock comes from the same steps played in the window by
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
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE.parent.parent / "scripts"))
from ansi import Canvas  # noqa: E402

BLACK, BLUE, GREY, DARK_GREY, WHITE = 0, 1, 7, 8, 15
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"
TITLE = "A night scene"
DATE = "20261118"
START = {"file": "blank.ans"}
WINDOW = [1280, 1300]


def write_steps(name, steps, window=None):
    path = HERE / f"{name}.steps.json"
    body = {"version": 1, "start": START, "steps": steps}
    if window:
        body["window"] = window
    path.write_text(json.dumps(body, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def replay(name, steps, keep, shots=None, window=None):
    """Writes the steps file and plays it; keep maps a step's name to the
    project after it, shots a step's name to the PNG its "screenshot"
    becomes, taken in the window."""
    path = write_steps(name, steps, window)
    number = {step["name"]: i + 1 for i, step in enumerate(steps)}
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([CLI, "replay", "--project", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        for step, dest in keep.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.bwp", HERE / dest)
    if not shots:
        return
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        for step, dest in shots.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.png", HERE / dest)


def gradient(name, rungs, frm, to, banding="cells"):
    return {"name": name, "action": "gradient", "ramp": "ice",
            "gradient": {"shape": "linear", "banding": banding, "from": rungs[0], "to": rungs[1]},
            "from": frm, "to": to}


# The sky: black at the top, one row each of light, medium and dark shade
# into blue, three rows of blue, the same three rows into light blue, and
# light blue down to the bottom. The first gradient fills the whole layer;
# the second only the selection under the blue rows.
SKY = [{"name": "sky-layer", "action": "layerProperties", "rename": "sky"},
       gradient("sky-top", (0, 4), [30, 6], [30, 10]),
       {"name": "sky-lower", "action": "select", "rect": [0, 12, 59, 23]},
       gradient("sky-bottom", (4, 8), [30, 12], [30, 16]),
       {"name": "sky", "action": "deselect"}]

# Stars in grey, sprayed inside a selection of the black rows that stops
# well short of where the moon goes.
STAR_FIELD = {"name": "star-field", "action": "select", "rect": [0, 0, 39, 6]}
SPRAY = {"name": "stars-sprayed", "action": "spray", "fg": GREY, "size": 64, "tip": "square",
         "pressure": "none", "symmetry": "none", "spray": {"kind": "stars", "density": 100, "seed": 1},
         "points": [[20, 3]]}
STARS = [STAR_FIELD, SPRAY, {"name": "stars", "action": "deselect"}]

# The moon, a white disc in the open black at the top right.
MOON = [{"name": "moon-layer", "action": "newPixelLayer", "rename": "moon"},
        {"name": "moon", "action": "ellipse", "fg": WHITE, "filled": True, "from": [44, 2], "to": [53, 11]}]

# The far trees: a blue band along the bottom and a row of rounded crowns of
# different sizes, overlapping, their tops on the flat light blue.
CROWNS = [(0, 36, 8, 44), (6, 34, 16, 44), (16, 36, 25, 44), (22, 35, 29, 44), (28, 33, 38, 44),
          (34, 36, 41, 44), (38, 34, 48, 44), (47, 36, 57, 44), (54, 34, 59, 44)]


def far_trees(colour):
    steps = [{"name": "far-layer", "action": "newPixelLayer", "rename": "far trees"},
             {"name": "far-band", "action": "rectangle", "fg": colour, "filled": True, "from": [0, 40],
              "to": [59, 47]}]
    for i, (x0, y0, x1, y1) in enumerate(CROWNS):
        steps.append({"name": f"crown-{i + 1}", "action": "ellipse", "from": [x0, y0], "to": [x1, y1]})
    steps[-1]["name"] = "far-trees"
    return steps


# The near trees: black ground along the bottom and six pines, each two
# lines from its tip to its feet on the ground and a fill inside; tall ones
# with their tips on the flat blue, short ones on the flat light blue.
PINES = [(5, 22, 4), (17, 33, 3), (27, 24, 5), (38, 34, 3), (48, 23, 4), (56, 33, 3)]


def near_trees():
    steps = [{"name": "near-layer", "action": "newPixelLayer", "rename": "near trees"},
             {"name": "ground", "action": "rectangle", "fg": BLACK, "filled": True, "from": [0, 43],
              "to": [59, 47]}]
    for i, (x, y, w) in enumerate(PINES):
        steps += [{"name": f"pine-{i + 1}-left", "action": "line", "from": [x, y], "to": [x - w, 43]},
                  {"name": f"pine-{i + 1}-right", "action": "line", "from": [x, y], "to": [x + w, 43]},
                  {"name": f"pine-{i + 1}", "action": "fill", "at": [x, y + 3]}]
    steps[-1]["name"] = "near-trees"
    return steps


def dock(step):
    return dict(step, screenshot={"of": "layers"})


def main():
    Canvas(60, 24).save(HERE / "blank.ans", title=TITLE, date=DATE)
    near = near_trees()
    steps = SKY + STARS + MOON + far_trees(BLUE) + near[:-1] + [dock(near[-1])]
    replay("do-it", steps,
           {"sky-top": "step-01.bwp", "sky": "step-02.bwp", "stars": "step-03.bwp", "moon": "step-04.bwp",
            "far-trees": "step-05.bwp", "near-trees": "final.bwp"},
           {"near-trees": "layers.png"}, window=WINDOW)

    # What goes wrong: the sky in one long gradient, black to light blue
    # down the whole canvas; the stars sprayed with no selection, up to the
    # moon; the far trees in black, the colour of the near ones.
    one_ramp = [SKY[0], gradient("sky", (0, 8), [30, 0], [30, 23], "bayer")]
    replay("one-ramp", one_ramp + STARS + MOON + far_trees(BLUE) + near, {"near-trees": "one-ramp.bwp"})
    replay("stars-everywhere", SKY + [dict(SPRAY, name="stars")] + MOON + far_trees(BLUE) + near,
           {"near-trees": "stars-everywhere.bwp"})
    replay("far-black", SKY + STARS + MOON + far_trees(BLACK) + near, {"near-trees": "far-black.bwp"})

    # Try it: the far trees recoloured dark grey with one fill, and the far
    # trees hidden.
    replay("try-recolour", steps + [{"name": "far-active", "action": "setActiveLayer", "layer": "far trees"},
                                    {"name": "recoloured", "action": "fill", "fg": DARK_GREY, "at": [37, 40]}],
           {"recoloured": "try-recolour.bwp"})
    replay("try-hidden", steps + [{"name": "far-active", "action": "setActiveLayer", "layer": "far trees"},
                                  {"name": "far-hidden", "action": "layerProperties", "visible": False}],
           {"far-hidden": "try-hidden.bwp"})


if __name__ == "__main__":
    main()
