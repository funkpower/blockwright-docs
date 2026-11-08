#!/usr/bin/env python3
"""Write tutorial 12's samples: python3 -I samples/12-scripts-and-generators/make.py

The CLI is $BLOCKWRIGHT_CLI, else blockwright-cli; the editor $BLOCKWRIGHT,
else blockwright. Every command runs in a scratch directory made by
tempfile (under $TMPDIR), with the files it needs copied in, so the
generators' programs run there and nowhere else, and each transcript
(*.txt: the command, what it printed, and the exit status when it isn't 0)
names files only by name. SOURCE_DATE_EPOCH is fixed, and every seed is a
parameter, so a second run writes the same bytes.

start.bwp: the dusk sky, a "sky" Cells layer, from start.steps.json.

ridges-*.bwp: the Ridges generator taken from the bundled sample "Ridges at
dusk" (its scripts/3, as File > Save As Project Directory writes it), added
to start.bwp by `add-generator`, then run again by `run-generators` with
each new set of parameters, as the form in the Layers dock runs it. It
needs a POSIX sh and awk.

baked.bwp: bake.steps.json, the ridges copied onto a Cells layer of their
own with the Select tool and the generator layer hidden, from
`replay --project`.

meteors-*.bwp: the meteors generator in meteors/ (python3) added by
`add-generator` and run again with new parameters.

final.bwp: moon.steps.json, a moon drawn on a Pixels layer by
`replay --project`.

form-*.png and layers.png: the Layers dock and its generator form, from
`blockwright --screenshot`.
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
os.environ["SOURCE_DATE_EPOCH"] = "1793836800"  # 2026-11-04
WINDOW = [1280, 1300]
W, H = 80, 25
RIDGES, BAKED, METEORS = 2, 3, 4  # the layers' ids, as `info` lists them


def write_steps(name, start, steps, window=None):
    body = {"version": 1, "start": start, "steps": steps}
    if window:
        body["window"] = window
    path = HERE / f"{name}.steps.json"
    path.write_text(json.dumps(body, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def replay(name, start, steps, keep=None, shots=None, window=None):
    """Write <name>.steps.json and play it; keep maps a step's name to the
    .bwp its capture becomes, shots a step's name to the PNG its
    "screenshot" becomes."""
    path = write_steps(name, start, steps, window)
    number = {step["name"]: i + 1 for i, step in enumerate(steps)}
    if keep:
        with tempfile.TemporaryDirectory(prefix="t12-") as tmp:
            subprocess.run([CLI, "replay", str(path), "-o", tmp, "--project"], check=True,
                           stdout=subprocess.DEVNULL)
            for step, dest in keep.items():
                shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.bwp", HERE / dest)
    if shots:
        with tempfile.TemporaryDirectory(prefix="t12-") as tmp:
            subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
            for step, dest in shots.items():
                shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.png", HERE / dest)


def run(tmp, args, transcript=None):
    """Run the CLI in tmp; with a transcript, write the command as typed,
    its stdout and stderr, and its exit status when it isn't 0."""
    r = subprocess.run([CLI, *args], cwd=tmp, capture_output=True, text=True)
    if transcript:
        status = f"exit status {r.returncode}\n" if r.returncode else ""
        out = f"$ blockwright-cli {' '.join(args)}\n" + r.stdout + r.stderr + status
        (HERE / transcript).write_text(out, encoding="utf-8")
    elif r.returncode:
        raise SystemExit(f"{args}: exit status {r.returncode}\n{r.stdout}{r.stderr}")
    return r


def rerun(src, dest, layer, params, script=None):
    """Unpack src, write the layer's params.json (and, given script, its
    program's new text), run that layer's generator again and pack the
    project as dest."""
    with tempfile.TemporaryDirectory(prefix="t12-") as tmp:
        shutil.copyfile(HERE / src, Path(tmp) / src)
        run(tmp, ["unpack", src, "project"])
        folder = Path(tmp) / "project" / "scripts" / str(layer)
        text = json.dumps(params, indent=4, sort_keys=True) + "\n"
        (folder / "params.json").write_text(text, encoding="utf-8")
        if script:
            name, body = script
            (folder / name).write_text(body, encoding="utf-8")
        run(tmp, ["run-generators", "--layer", str(layer), "project"])
        run(tmp, ["pack", "project", "out.bwp"])
        shutil.copyfile(Path(tmp) / "out.bwp", HERE / dest)


def add(src, dest, folder, name=None, transcript=None, files=None):
    """Copy src and the generator's folder into a scratch directory and run
    add-generator there; the project it saves becomes dest. files names
    other folders to copy in (as name: source path)."""
    with tempfile.TemporaryDirectory(prefix="t12-") as tmp:
        shutil.copyfile(HERE / src, Path(tmp) / "night.bwp")
        for target, source in (files or {}).items():
            shutil.copytree(source, Path(tmp) / target)
        args = ["add-generator"] + (["--name", name] if name else []) + ["night.bwp", folder]
        r = run(tmp, args, transcript)
        if dest:
            shutil.copyfile(Path(tmp) / "night.bwp", HERE / dest)
        return r


# The start: a dusk sky, black over the top rows, then a rung a row up the
# sunset ramp (blue, magenta, light magenta, light red), the light, medium and
# dark shade between each colour and the next.
steps = [{"name": "rename", "action": "layerProperties", "rename": "sky"},
         {"name": "margin", "action": "keyboard", "at": [W - 1, 0], "fg": 0, "bg": 0, "text": "█"}]
for row in range(1, 8):  # a black block ends each black row, so IRC keeps it
    steps.append({"name": "margin-%d" % row, "action": "keyboard", "at": [W - 1, row], "text": "█"})
row = 8
for dark, light in [(0, 1), (1, 5), (5, 13), (13, 12)]:
    for glyph in "░▒▓":
        steps.append({"name": "row-%d" % row, "action": "keyboard", "at": [0, row], "fg": light, "bg": dark,
                      "text": glyph * W})
        row += 1
    if light != 12:
        steps.append({"name": "row-%d" % row, "action": "keyboard", "at": [0, row], "fg": light, "bg": 0,
                      "text": "█" * W})
        row += 1
steps.append({"name": "glow", "action": "rectangle", "from": [0, 2 * row], "to": [W - 1, 2 * H - 1], "fg": 12,
              "filled": True})
replay("start", {"blank": [W, H]}, steps, {"glow": "start.bwp"})

# The Ridges generator as File > Save As Project Directory writes it from the
# bundled sample: scripts/3 of the saved directory.
with tempfile.TemporaryDirectory(prefix="t12-") as tmp:
    path = Path(tmp) / "open.steps.json"
    body = {"version": 1, "start": {"sample": "04-generator-ridges"}, "steps": [{"name": "open", "action": "deselect"}]}
    path.write_text(json.dumps(body))
    subprocess.run([CLI, "replay", str(path), "-o", tmp, "--project"], check=True, stdout=subprocess.DEVNULL)
    run(tmp, ["unpack", "01-open.bwp", "ridges-at-dusk"])
    SAMPLE = Path(tmp) / "ridges-at-dusk"
    add("start.bwp", "ridges-1.bwp", "ridges-at-dusk/scripts/3", name="ridges", transcript="add-ridges.txt",
        files={"ridges-at-dusk": SAMPLE})

# The form, read as the layer is added; then a parameter at a time.
replay("form-ridges", {"file": "ridges-1.bwp"},
       [{"name": "pick", "action": "setActiveLayer", "layer": "ridges", "screenshot": {"of": "generatorForm"}}],
       shots={"pick": "form-ridges.png"}, window=WINDOW)
ridges = {"ridges": 3, "roughness": 0.3, "seed": 3, "sharp": False, "top": 18}
for dest, change in [("ridges-2.bwp", {"top": 13}), ("ridges-3.bwp", {"ridges": 4}),
                     ("ridges-4.bwp", {"sharp": True}), ("ridges-5.bwp", {"seed": 41}),
                     ("ridges-6.bwp", {"seed": 2026})]:
    ridges.update(change)
    rerun("ridges-1.bwp", dest, RIDGES, ridges)

# Bake: the ridges copied onto a Cells layer, the generator layer hidden.
steps = [{"name": "pick", "action": "setActiveLayer", "layer": "ridges"},
         {"name": "all", "action": "selectAll"},
         {"name": "copy", "action": "copy"},
         {"name": "new", "action": "newCellsLayer", "rename": "ridges (baked)"},
         {"name": "paste", "action": "paste", "at": [0, 0]},
         {"name": "drop", "action": "deselect"},
         {"name": "pick-again", "action": "setActiveLayer", "layer": "ridges"},
         {"name": "hide", "action": "layerProperties", "visible": False},
         {"name": "back", "action": "setActiveLayer", "layer": "ridges (baked)", "screenshot": {"of": "layers"}}]
replay("bake", {"file": "ridges-6.bwp"}, steps, {"hide": "baked.bwp"}, {"back": "layers.png"}, window=WINDOW)

# Meteors, a generator of your own.
FOLDER = HERE / "meteors"
add("baked.bwp", "meteors-1.bwp", "meteors", transcript="add-meteors.txt", files={"meteors": FOLDER})
replay("form-meteors", {"file": "meteors-1.bwp"},
       [{"name": "pick", "action": "setActiveLayer", "layer": "meteors", "screenshot": {"of": "generatorForm"}}],
       shots={"pick": "form-meteors.png"}, window=WINDOW)
meteors = {"seed": 1, "count": 3, "length": 5, "bottom": 7, "colour": 11}
for dest, change in [("meteors-2.bwp", {"count": 5, "length": 7}), ("meteors-3.bwp", {"seed": 17})]:
    meteors.update(change)
    rerun("meteors-1.bwp", dest, METEORS, meteors)

# The command line: a moon by a steps file, then render, export, lint and
# run-generators on the piece.
moon = [{"name": "moon", "action": "newPixelLayer", "rename": "moon"},
        {"name": "disc", "action": "ellipse", "from": [50, 3], "to": [57, 10], "fg": 15, "filled": True},
        {"name": "shadow", "action": "ellipse", "from": [52, 2], "to": [59, 9], "fg": 0, "filled": True}]
with tempfile.TemporaryDirectory(prefix="t12-") as tmp:
    shutil.copyfile(HERE / "meteors-3.bwp", Path(tmp) / "night.bwp")
    path = write_steps("moon", {"file": "night.bwp"}, moon)
    shutil.copyfile(path, Path(tmp) / "moon.steps.json")
    run(tmp, ["replay", "moon.steps.json", "-o", "moon", "--project"], "replay.txt")
    shutil.copyfile(Path(tmp) / "moon" / "03-shadow.bwp", HERE / "final.bwp")
    shutil.copyfile(HERE / "final.bwp", Path(tmp) / "night.bwp")
    (HERE / "replay-files.txt").write_text("\n".join(sorted(p.name for p in (Path(tmp) / "moon").iterdir())) + "\n",
                                          encoding="utf-8")
    run(tmp, ["render", "--scale", "2", "night.bwp", "night.png"], "render.txt")
    run(tmp, ["export", "--irc", "night.bwp", "night.txt"], "export.txt")
    run(tmp, ["lint", "night.bwp"], "lint.txt")
    run(tmp, ["info", "night.bwp"], "info.txt")
    run(tmp, ["unpack", "night.bwp", "night"])
    folder = Path(tmp) / "night" / "scripts" / str(METEORS)
    (folder / "params.json").write_text(json.dumps(dict(meteors, seed=5), indent=4, sort_keys=True) + "\n",
                                        encoding="utf-8")
    run(tmp, ["run-generators", "night"], "run-generators.txt")
    run(tmp, ["pack", "night", "night-5.bwp"])
    shutil.copyfile(Path(tmp) / "night-5.bwp", HERE / "seed-5.bwp")

# The mistakes: meteors below the black rows, and a program that fails.
rerun("final.bwp", "low.bwp", METEORS, dict(meteors, bottom=20))
with tempfile.TemporaryDirectory(prefix="t12-") as tmp:
    broken = Path(tmp) / "meteors"
    shutil.copytree(FOLDER, broken)
    script = broken / "meteors.py"
    script.write_text(script.read_text(encoding="utf-8").replace('p["colour"]', 'p["color"]'), encoding="utf-8")
    add("final.bwp", None, "meteors", transcript="add-broken.txt", files={"meteors": broken})

# Try it: the piece as it ends, and the answers.
shutil.copyfile(HERE / "final.bwp", HERE / "try.bwp")
rerun("try.bwp", "try-tail.bwp", METEORS, dict(meteors, colour=12, length=4))
text = (FOLDER / "meteors.py").read_text(encoding="utf-8")
right = text.replace("(x + i, y - i)", "(x - i, y - i)").replace('("/", p["colour"])', '("\\\\", p["colour"])')
assert right != text and right.count("x - i") == 1 and '"\\\\"' in right
rerun("try.bwp", "try-right.bwp", METEORS, meteors, script=("meteors.py", right))
