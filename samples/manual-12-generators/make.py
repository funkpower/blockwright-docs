#!/usr/bin/env python3
"""Write the Generators page's samples: python3 -I samples/manual-12-generators/make.py

Each steps file starts from the bundled sample "Ridges at dusk" and is played
by `blockwright-cli replay --project` (the CLI is $BLOCKWRIGHT_CLI, else
blockwright-cli); the .bwp captures the page shows are copied beside it.
form.png is the first steps file played by `blockwright --screenshot` (the
editor is $BLOCKWRIGHT, else blockwright), the generator form in the Layers
dock.

ridges.bwp: the sample as it opens, with the ridges layer active.

seed-12.bwp: the sample's "Another seed" variant: the hidden ridges layer at
seed 12, four ridges and sharp peaks shown, the ridges layer hidden.

smooth.bwp: ridges.bwp with the ridges layer's parameters set to two ridges,
roughness 0 and highest row 12 (seed 3, no sharp peaks), run again by
`blockwright-cli run-generators`. That runs the layer's script, which needs
a POSIX sh and awk.
"""

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"
SAMPLE = "04-generator-ridges"
RIDGES = 3  # the ridges layer's id


def replay(name, start, steps, keep, shots=None, window=None):
    """Write <name>.steps.json and play it; keep maps a step's name to the
    .bwp its capture becomes, shots a step's name to the PNG its
    "screenshot" becomes."""
    path = HERE / f"{name}.steps.json"
    body = {"version": 1, "start": start, "steps": steps}
    if window:
        body["window"] = window
    path.write_text(json.dumps(body, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    number = {step["name"]: i + 1 for i, step in enumerate(steps)}
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([CLI, "replay", str(path), "-o", tmp, "--project"], check=True, stdout=subprocess.DEVNULL)
        for step, dest in keep.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.bwp", HERE / dest)
    if not shots:
        return
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        for step, dest in shots.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.png", HERE / dest)


def rerun(src, dest, layer, params):
    """Unpack src, write the layer's params.json, run that layer's generator
    again and pack the project as dest."""
    with tempfile.TemporaryDirectory() as tmp:
        unpacked = Path(tmp) / "project"
        subprocess.run([CLI, "unpack", str(HERE / src), str(unpacked)], check=True, stdout=subprocess.DEVNULL)
        text = json.dumps(params, indent=4, sort_keys=True) + "\n"
        (unpacked / "scripts" / str(layer) / "params.json").write_text(text, encoding="utf-8")
        subprocess.run([CLI, "run-generators", "--layer", str(layer), str(unpacked)], check=True,
                       stdout=subprocess.DEVNULL)
        subprocess.run([CLI, "pack", str(unpacked), str(HERE / dest)], check=True, stdout=subprocess.DEVNULL)


steps = [{"name": "pick", "action": "setActiveLayer", "layer": "ridges", "screenshot": {"of": "generatorForm"}}]
replay("ridges", {"sample": SAMPLE}, steps, {"pick": "ridges.bwp"}, {"pick": "form.png"}, window=[1280, 1300])

steps = [{"name": "pick", "action": "setActiveLayer", "layer": "ridges (seed 12)"}]
replay("seed-12", {"sample": SAMPLE, "variant": "Another seed"}, steps, {"pick": "seed-12.bwp"})

rerun("ridges.bwp", "smooth.bwp", RIDGES, {"ridges": 2, "roughness": 0, "seed": 3, "sharp": False, "top": 12})
