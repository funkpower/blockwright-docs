#!/usr/bin/env python3
"""Write the Library page's samples: python3 -I samples/manual-08-library/make.py

dock.png is the Library dock on a blank 80 x 25 canvas, played by
`blockwright --screenshot` (the editor is $BLOCKWRIGHT, else blockwright)
with an empty user library, so it shows the bundled stamps and text styles
only. The window is tall enough for the dock to show several rows.

collection.png is the same dock with an empty bundled library and a user
library holding one collection, Night sky, made with `blockwright-cli
library new` and `library add` (the CLI is $BLOCKWRIGHT_CLI, else
blockwright-cli) from four of the bundled sky stamps.
"""

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
NIGHT_SKY = ["crescent-moon", "full-moon", "small-star", "star-field"]


def play(name, start, steps, pictures, window=None, library=None, env=None):
    """Write <name>.steps.json, play it, and copy each picture {shot: page name}."""
    path = HERE / f"{name}.steps.json"
    head = {"version": 1, "window": window} if window else {"version": 1}
    path.write_text(json.dumps({**head, "start": start, "steps": steps}, indent=1) + "\n")
    with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as scratch:
        env = dict(os.environ, **(env or {}))
        env.setdefault("BLOCKWRIGHT_USER_LIBRARY", scratch)
        args = [GUI, "--screenshot", str(path), "-o", tmp] + (["--user-library", library] if library else [])
        subprocess.run(args, check=True, stdout=subprocess.DEVNULL, env=env)
        for shot, page in pictures.items():
            shutil.copyfile(Path(tmp) / shot, HERE / page)


def bundled_library():
    """The bundled library beside the CLI: <prefix>/share/blockwright/library."""
    if os.environ.get("BLOCKWRIGHT_BUNDLED_LIBRARY"):
        return Path(os.environ["BLOCKWRIGHT_BUNDLED_LIBRARY"])
    cli = Path(shutil.which(CLI)).resolve()
    return cli.parent.parent / "share" / "blockwright" / "library"


play("dock", {"blank": [80, 25]}, [
    {"name": "dock", "action": "deselect", "screenshot": {"of": "libraryDock"}},
], {"01-dock.png": "dock.png"}, window=[1280, 2200])

with tempfile.TemporaryDirectory() as user, tempfile.TemporaryDirectory() as empty:
    sky = bundled_library() / "sky"
    subprocess.run([CLI, "library", "new", "--dir", user, "Night sky"], check=True, stdout=subprocess.DEVNULL)
    subprocess.run([CLI, "library", "add", "--dir", user, "Night sky"] + [str(sky / f"{n}.ans") for n in NIGHT_SKY],
                   check=True, stdout=subprocess.DEVNULL)
    play("collection", {"blank": [80, 25]}, [
        {"name": "collection", "action": "deselect", "screenshot": {"of": "libraryDock"}},
    ], {"01-collection.png": "collection.png"}, window=[1280, 2200], library=user,
        env={"BLOCKWRIGHT_BUNDLED_LIBRARY": empty})
