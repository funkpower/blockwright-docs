#!/usr/bin/env python3
"""Write the window page's pictures: python3 -I samples/manual-02-the-window/make.py

window.steps.json opens tutorial 09's finished project
(../09-layers-and-projects/final.bwp) and changes nothing in it: two view
steps set the zoom, and the window and the status bar are pictured there. It is played by
`blockwright --screenshot` (the editor is $BLOCKWRIGHT, else blockwright).

window.png: the whole window, every dock where it starts.
status-bar.png: the right end of the status bar.
"""

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"
WINDOW = [1600, 1000]

SHOTS = {
    "window": ("window.png", {"of": "window"}),
    "status": ("status-bar.png", {"crop": {"pixels": [1110, WINDOW[1] - 24, 490, 24]}}),
}
steps = [
    {"name": "window", "action": "view", "zoom": 2},
    {"name": "status", "action": "view", "zoom": 2},
]
number = {}
for i, s in enumerate(steps):
    number[s["name"]] = i + 1
    s["screenshot"] = SHOTS[s["name"]][1]
body = {"version": 1, "start": {"file": "../09-layers-and-projects/final.bwp"}, "steps": steps, "window": WINDOW}
path = HERE / "window.steps.json"
path.write_text(json.dumps(body, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
    for name, (dest, _) in SHOTS.items():
        shutil.copyfile(Path(tmp) / f"{number[name]:02d}-{name}.png", HERE / dest)
