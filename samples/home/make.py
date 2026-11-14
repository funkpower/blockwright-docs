#!/usr/bin/env python3
"""Write the home page's window pictures: python3 -I samples/home/make.py

Each picture is a steps file played by `blockwright --screenshot` (the editor
is $BLOCKWRIGHT, else blockwright): one of the samples Blockwright installs,
opened by a {"sample": ...} start, a layer made active, the zoom set to 1, and
a tool's settings set by a step without points, which changes nothing on the
canvas. The window is pictured at that step, so Tool Options shows the tool.

harbour.png: Harbour at night, the moon's Pixels layer and the Half-Block Brush.
still-life.png: Still life, the sphere and the Form Brush, a dome lit from the
north-west on the sea ramp.
battlestation.png: Battlestation, the colours-only glow layer and the Colorize
Brush in light blue.

logo-large.ans is Blockwright's own large logo, copied unchanged from
`branding/logo-large.ans` in Blockwright's source (the same file in 0.1.0); the
home page shows it with Blockwright's `branding/logo.txt` as its alt text.
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
    "harbour": ("01-layers-showcase", "moon", {"action": "halfBlock", "fg": 14, "size": 2}),
    "still-life": ("03-still-life", "sphere", {"action": "form", "ramp": "sea", "size": 6, "light": "NW",
                                               "form": {"shape": "dome", "rim": False, "specular": True}}),
    "battlestation": ("07-battlestation", "glow", {"action": "colorize", "fg": 9, "size": 4, "tip": "round"}),
}

for name, (sample, layer, tool) in SHOTS.items():
    steps = [
        {"name": "layer", "action": "setActiveLayer", "layer": layer},
        {"name": "zoom", "action": "view", "zoom": 1},
        dict(tool, name=name, screenshot={"of": "window"}),
    ]
    body = {"version": 1, "start": {"sample": sample}, "steps": steps, "window": WINDOW}
    path = HERE / f"{name}.steps.json"
    path.write_text(json.dumps(body, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        shutil.copyfile(Path(tmp) / f"03-{name}.png", HERE / f"{name}.png")
