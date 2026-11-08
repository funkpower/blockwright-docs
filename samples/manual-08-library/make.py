#!/usr/bin/env python3
"""Write the Library page's samples: python3 -I samples/manual-08-library/make.py

dock.png is the Library dock on a blank 80 x 25 canvas, played by
`blockwright --screenshot` (the editor is $BLOCKWRIGHT, else blockwright)
with an empty user library, so it shows the bundled stamps and text styles
only. The window is tall enough for the dock to show several rows.
"""

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"


def play(name, start, steps, pictures, window=None):
    """Write <name>.steps.json, play it, and copy each picture {shot: page name}."""
    path = HERE / f"{name}.steps.json"
    head = {"version": 1, "window": window} if window else {"version": 1}
    path.write_text(json.dumps({**head, "start": start, "steps": steps}, indent=1) + "\n")
    with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as library:
        env = dict(os.environ, BLOCKWRIGHT_USER_LIBRARY=library)
        subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL, env=env)
        for shot, page in pictures.items():
            shutil.copyfile(Path(tmp) / shot, HERE / page)


play("dock", {"blank": [80, 25]}, [
    {"name": "dock", "action": "deselect", "screenshot": {"of": "libraryDock"}},
], {"01-dock.png": "dock.png"}, window=[1280, 2200])
