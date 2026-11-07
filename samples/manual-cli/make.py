#!/usr/bin/env python3
"""Write the CLI page's samples: python3 -I samples/manual-cli/make.py

pointer-before.png and pointer-after.png show "pointer": true: a yellow line
drawn with the Line tool on a blank 16 x 8 canvas, pictured before and after
the step at "scale": 2, the canvas cropped out of the window. The steps file
(pointer.steps.json) is played by `blockwright --screenshot` (the editor is
$BLOCKWRIGHT, else blockwright).
"""

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"
YELLOW = 14
W, H = 16, 8

steps = {
    "version": 1,
    "start": {"blank": [W, H]},
    "steps": [
        {
            "name": "line",
            "action": "line",
            "from": [2, 2],
            "to": [12, 13],
            "fg": YELLOW,
            "screenshot": {"crop": {"cells": [0, 0, W, H]}, "when": "both", "scale": 2, "pointer": True},
        }
    ],
}

path = HERE / "pointer.steps.json"
path.write_text(json.dumps(steps, indent=1) + "\n")
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
    for when in ("before", "after"):
        shutil.copyfile(Path(tmp) / f"01-line-{when}.png", HERE / f"pointer-{when}.png")
