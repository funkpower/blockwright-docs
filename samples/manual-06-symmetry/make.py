#!/usr/bin/env python3
"""Write the Symmetry page's samples: python3 -I samples/manual-06-symmetry/make.py

Each steps file starts from a blank canvas this script writes (it carries the
SAUCE) and is played by `blockwright-cli replay` (the CLI is $BLOCKWRIGHT_CLI,
else blockwright-cli); the .ans captures the page shows are copied beside it.
options.png is the first steps file played by `blockwright --screenshot` (the
editor is $BLOCKWRIGHT, else blockwright), the Tool Options dock cropped to
its rows from Glyph down.

centre.ans: four arrows laid along row 2 from column 12 to 15 by the Glyph
Brush under Radial, 4 folds, turned about the cell 10, 6.

folds-8.ans: the corner of tutorial 07 (upper half blocks along row 2 from
column 22 to 27, left half blocks down column 22 from row 3 to 5) under
Radial, 8 folds, about the middle of a canvas 41 by 17.

typing.ans: /<(▌Ab typed at 1, 1 under Mirror X on a canvas 21 by 3.

pixels.ans: a Pixels layer over the blank one, and one Line on it from pixel
22, 4 to pixel 34, 10 under Radial, 5 folds.
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

BLACK, GREY, YELLOW = 0, 7, 14
TITLE = "Symmetry"
DATE = "20261108"
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"


def blank(w, h):
    name = f"blank-{w}x{h}.ans"
    Canvas(w, h).save(HERE / name, title=TITLE, date=DATE)
    return name


def replay(name, start, steps, keep, shots=None, window=None):
    """Write <name>.steps.json and play it; keep maps a step's name to the
    .ans its capture becomes, shots a step's name to the PNG its
    "screenshot" becomes."""
    path = HERE / f"{name}.steps.json"
    body = {"version": 1, "start": {"file": start}, "steps": steps}
    if window:
        body["window"] = window
    path.write_text(json.dumps(body, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    number = {step["name"]: i + 1 for i, step in enumerate(steps)}
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([CLI, "replay", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        for step, dest in keep.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.ans", HERE / dest)
    if not shots:
        return
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        for step, dest in shots.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.png", HERE / dest)


def glyph(name, g, points, symmetry=None):
    step = {"name": name, "action": "glyph", "glyph": g, "fg": YELLOW, "bg": BLACK, "size": 1, "tip": "square",
            "points": points}
    if symmetry is not None:
        step["symmetry"] = symmetry
    return step


steps = [glyph("arrows", "►", [[12, 2], [15, 2]], {"mode": "radial", "folds": 4, "centre": [10, 6]})]
steps[0]["screenshot"] = {"of": "toolOptions", "crop": {"pixels": [0, 440, 256, 215]}}
replay("centre", blank(41, 17), steps, {"arrows": "centre.ans"}, {"arrows": "options.png"}, window=[1280, 1300])

steps = [glyph("top", "▀", [[22, 2], [27, 2]], {"mode": "radial", "folds": 8}), glyph("side", "▌", [[22, 3], [22, 5]])]
replay("folds-8", blank(41, 17), steps, {"side": "folds-8.ans"})

steps = [{"name": "type", "action": "keyboard", "fg": GREY, "bg": BLACK, "symmetry": "mirrorX", "at": [1, 1],
          "text": "/<(▌Ab"}]
replay("typing", blank(21, 3), steps, {"type": "typing.ans"})

steps = [{"name": "layer", "action": "newPixelLayer", "rename": "pixels"},
         {"name": "line", "action": "line", "fg": YELLOW, "from": [22, 4], "to": [34, 10],
          "symmetry": {"mode": "radial", "folds": 5}}]
replay("pixels", blank(41, 17), steps, {"line": "pixels.ans"})
