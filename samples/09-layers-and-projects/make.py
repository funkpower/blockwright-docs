#!/usr/bin/env python3
"""Write tutorial 09's samples: python3 -I samples/09-layers-and-projects/make.py

Every picture is a steps file played by `blockwright-cli replay` (the CLI is
$BLOCKWRIGHT_CLI, else blockwright-cli on PATH), starting from tutorial 07's
castle (../07-detail/final.bwp): new layers, strokes on them, their order,
their visibility and a layer moved, one step each. This script writes the
steps files (*.steps.json), replays each into a scratch directory, and
copies the captures the page shows beside them. The snapshots are taken by
`blockwright-cli snapshot`, the same snapshot File > Take Snapshot takes.
The pictures of the Layers dock come from the same steps played in the
window by `blockwright --screenshot` (the editor is $BLOCKWRIGHT, else
blockwright).
"""

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BLACK, BLUE, DARK_GREY = 0, 1, 8
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"
CASTLE = "../07-detail/final.bwp"
WINDOW = [1280, 1300]


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
    window."""
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
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.png", HERE / dest)


def snapshot(project):
    """Takes the project's next snapshot, as File > Take Snapshot and a save."""
    subprocess.run([CLI, "snapshot", str(HERE / project)], check=True, stdout=subprocess.DEVNULL)


def dock(step):
    return dict(step, screenshot={"of": "layers"})


# The idea: the castle's two layers apart. The door hidden leaves the
# Background layer; the Background hidden leaves the door.
steps = [{"name": "door-active", "action": "setActiveLayer", "layer": "door"},
         {"name": "door-hidden", "action": "layerProperties", "visible": False},
         {"name": "door-shown", "action": "layerProperties", "visible": True},
         {"name": "background-active", "action": "setActiveLayer", "layer": "Background"},
         {"name": "background-hidden", "action": "layerProperties", "visible": False}]
replay("apart", CASTLE, steps, {"door-hidden": "background.bwp", "background-hidden": "door.bwp"})

# Banners: a Pixels layer, added with the Background layer active, so over
# it and under the door. Two blue banners under Mirror X and one in the
# middle, filled rectangles; then the layer raised over the door.
ACTIVE = {"name": "background-active", "action": "setActiveLayer", "layer": "Background"}
BANNERS = [ACTIVE, {"name": "banners-layer", "action": "newPixelLayer", "rename": "banners"},
           {"name": "sides", "action": "rectangle", "fg": BLUE, "filled": True, "symmetry": "mirrorX",
            "from": [9, 18], "to": [11, 28]},
           {"name": "middle", "action": "rectangle", "symmetry": "none", "from": [28, 18], "to": [31, 30]},
           {"name": "raise", "action": "raiseLayer"}]
steps = BANNERS[:1] + [dock(BANNERS[1])] + BANNERS[2:4] + [dock(BANNERS[4])]
replay("banners", CASTLE, steps,
       {"sides": "step-01.bwp", "middle": "step-02.bwp", "raise": "banners.bwp"},
       {"banners-layer": "layers-new.png", "raise": "layers-raised.png"}, window=WINDOW)
snapshot("banners.bwp")

# A cloud: another Pixels layer, just above the Background layer and below
# the door and the banners. Two dark grey streaks a pixel deep drawn beside
# the moon, then the layer moved ten cells left, over it.
CLOUD = [ACTIVE, {"name": "cloud-layer", "action": "newPixelLayer", "rename": "cloud"},
         {"name": "cloud-top", "action": "rectangle", "fg": DARK_GREY, "filled": True, "symmetry": "none",
          "from": [14, 5], "to": [24, 5]},
         {"name": "cloud", "action": "rectangle", "from": [19, 8], "to": [29, 8]},
         {"name": "cloud-move", "action": "move", "by": [-10, 0]}]
HIDE = [{"name": "cloud-hidden", "action": "layerProperties", "visible": False}]
steps = CLOUD[:4] + [dock(CLOUD[4])] + [dock(HIDE[0])]
replay("cloud", "banners.bwp", steps,
       {"cloud": "step-03.bwp", "cloud-move": "final.bwp"},
       {"cloud-move": "layers.png", "cloud-hidden": "layers-hidden.png"}, window=WINDOW)
snapshot("final.bwp")

# Save As .ans: the project flattened. Opened again, it is one layer.
subprocess.run([CLI, "convert", str(HERE / "final.bwp"), str(HERE / "final.ans")], check=True,
               stdout=subprocess.DEVNULL)
replay("flat", "final.ans", [dock({"name": "opened", "action": "deselect"})], {}, {"opened": "layers-flat.png"},
       window=WINDOW)

# What goes wrong. The cloud drawn on a Cells layer: each stroke's other
# half is black, over the moon too.
CELLS = [ACTIVE, dict(CLOUD[1], action="newCellsLayer")] + CLOUD[2:]
replay("cloud-cells", "banners.bwp", CELLS, {"cloud-move": "cloud-cells.bwp"})
# The move made with the Background layer still active: the sky and the
# wall go, the door and the banners stay.
WRONG = CLOUD[:4] + [dict(ACTIVE, name="background-clicked"), CLOUD[4]]
replay("wrong-layer", "banners.bwp", WRONG, {"cloud-move": "wrong-layer.bwp"})

# Try it: the castle with its banners, no cloud. The answers: the banners
# lowered under the Background layer, and the door hidden.
shutil.copyfile(HERE / "banners.bwp", HERE / "try.bwp")
steps = [{"name": "banners-active", "action": "setActiveLayer", "layer": "banners"},
         {"name": "lower", "action": "lowerLayer"}, {"name": "lowest", "action": "lowerLayer"}]
replay("try-lower", "try.bwp", steps, {"lowest": "try-lower.bwp"})
steps = [{"name": "door-active", "action": "setActiveLayer", "layer": "door"},
         {"name": "door-hidden", "action": "layerProperties", "visible": False}]
replay("try-hide", "try.bwp", steps, {"door-hidden": "try-hide.bwp"})
