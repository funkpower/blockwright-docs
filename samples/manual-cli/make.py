#!/usr/bin/env python3
"""Write the CLI page's samples: python3 -I samples/manual-cli/make.py

Each steps file is played by `blockwright --screenshot` (the editor is
$BLOCKWRIGHT, else blockwright), and the pictures the page shows are copied
beside it.

pointer-before.png and pointer-after.png show "pointer": true: a yellow line
drawn with the Line tool on a blank 16 x 8 canvas, pictured before and after
the step at "scale": 2, the canvas cropped out of the window.

canvas-size-before.png and canvas-size-after.png show a canvasSize step: a
12 x 4 sun over grass grown to 16 x 6 about the centre, the canvas cropped
out of the window before and after it.

sample-merged-off.png and sample-merged-on.png show "sampleMerged": a red
frame on the bottom layer and a fill inside it on a clear layer above, off
and then on; sample-merged-options.png is Tool Options with the box ticked.

clone-source.png, clone-head.png and clone-aligned.png show clone steps on
funkpower's Spruce Island (spruce-island.ans, a copy of the piece): the
source set on the fox's face with the pointer on it, then two strokes of a
4 x 4 brush on the snow, the second carrying on below the first.
clone-unaligned.png is the second stroke with "aligned": false, copying the
head again, and clone-options.png is Tool Options with Aligned unticked. Both
files set a window large enough for the crop to be in view.
"""

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"
BLUE, GREEN, RED, YELLOW = 1, 2, 4, 14


def crop(w, h, **more):
    return {"crop": {"cells": [0, 0, w, h]}, **more}


def play(name, start, steps, pictures, window=None):
    """Write <name>.steps.json, play it, and copy each picture {shot: page name}."""
    path = HERE / f"{name}.steps.json"
    head = {"version": 1, "window": window} if window else {"version": 1}
    path.write_text(json.dumps({**head, "start": start, "steps": steps}, indent=1) + "\n")
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        for shot, page in pictures.items():
            shutil.copyfile(Path(tmp) / shot, HERE / page)


W, H = 16, 8
play("pointer", {"blank": [W, H]}, [
    {"name": "line", "action": "line", "from": [2, 2], "to": [12, 13], "fg": YELLOW,
     "screenshot": crop(W, H, when="both", scale=2, pointer=True)},
], {"01-line-before.png": "pointer-before.png", "01-line-after.png": "pointer-after.png"})

W, H = 12, 4
play("canvas-size", {"blank": [W, H]}, [
    {"name": "sky", "action": "fill", "at": [0, 0], "fg": BLUE},
    {"name": "sun", "action": "ellipse", "from": [2, 1], "to": [6, 5], "fg": YELLOW, "filled": True},
    {"name": "grass", "action": "rectangle", "from": [0, 6], "to": [W - 1, 7], "fg": GREEN,
     "screenshot": crop(W, H, scale=2)},
    {"name": "grow", "action": "canvasSize", "size": [16, 6], "anchor": "centre",
     "screenshot": crop(16, 6, scale=2)},
], {"03-grass.png": "canvas-size-before.png", "04-grow.png": "canvas-size-after.png"})

play("sample-merged", {"blank": [W, H]}, [
    {"name": "frame", "action": "rectangle", "from": [3, 0], "to": [8, 7], "fg": RED},
    {"name": "paint", "action": "newCellsLayer", "rename": "paint"},
    {"name": "off", "action": "fill", "at": [5, 3], "fg": YELLOW, "screenshot": crop(W, H, scale=2)},
    {"name": "again", "action": "deleteLayer"},
    {"name": "paint-again", "action": "newCellsLayer", "rename": "paint"},
    {"name": "on", "action": "fill", "at": [5, 3], "sampleMerged": True, "screenshot": crop(W, H, scale=2)},
    {"name": "options", "action": "fill", "screenshot": {"of": "toolOptions", "crop": {"pixels": [0, 0, 256, 544]}}},
], {"03-off.png": "sample-merged-off.png", "06-on.png": "sample-merged-on.png",
    "07-options.png": "sample-merged-options.png"})

FOX = {"crop": {"cells": [58, 32, 48, 18]}}
SOURCE = [
    {"name": "source", "action": "clone", "source": [93, 36], "screenshot": {**FOX, "pointer": True}},
    {"name": "head", "action": "clone", "size": 4, "points": [[62, 44], [72, 44]], "screenshot": FOX},
]
play("clone-aligned", {"file": "spruce-island.ans"}, SOURCE + [
    {"name": "body", "action": "clone", "points": [[62, 48], [72, 48]], "screenshot": FOX},
], {"01-source.png": "clone-source.png", "02-head.png": "clone-head.png", "03-body.png": "clone-aligned.png"},
    window=[2800, 2100])
play("clone-unaligned", {"file": "spruce-island.ans"}, SOURCE + [
    {"name": "body", "action": "clone", "points": [[62, 48], [72, 48]], "aligned": False, "screenshot": FOX},
    {"name": "options", "action": "clone", "screenshot": {"of": "toolOptions", "crop": {"pixels": [0, 0, 360, 535]}}},
], {"03-body.png": "clone-unaligned.png", "04-options.png": "clone-options.png"}, window=[2800, 2100])
