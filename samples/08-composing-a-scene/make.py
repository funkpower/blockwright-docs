#!/usr/bin/env python3
"""Write tutorial 08's samples: python3 -I samples/08-composing-a-scene/make.py

Every picture is a steps file played by `blockwright-cli replay` (the CLI is
$BLOCKWRIGHT_CLI, else blockwright-cli on PATH): the parts of a scene drawn
on a layer of their own, then picked up, moved, flipped, turned, copied, cut
and pasted with the editor's own selection actions, one step each. This
script writes the steps files (*.steps.json) and the blank canvas they start
from (blank-60x20.ans, which carries the SAUCE), replays each into a scratch
directory, and copies the captures the page shows beside them. The pictures
of the window come from the same steps played by `blockwright --screenshot`
(the editor is $BLOCKWRIGHT, else blockwright), with an empty user library,
so the Library dock shows the bundled stamps only.
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

BLACK, BLUE, GREEN, BROWN, GREY = 0, 1, 2, 6, 7
DARK_GREY, LIGHT_GREEN, WHITE = 8, 10, 15
TITLE = "Composing a scene"
DATE = "20261108"
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"
WINDOW = [1280, 1300]


def blank(w, h):
    name = f"blank-{w}x{h}.ans"
    Canvas(w, h).save(HERE / name, title=TITLE, date=DATE)
    return name


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
    its capture becomes (a .bwp, the project after it). shots maps a step's
    name to the PNG its "screenshot" becomes, taken in the window."""
    path = write_steps(name, start, steps, window)
    number = {step["name"]: i + 1 for i, step in enumerate(steps)}
    if keep:
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([CLI, "replay", str(path), "-o", tmp, "--project"], check=True,
                           stdout=subprocess.DEVNULL)
            for step, dest in keep.items():
                shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.bwp", HERE / dest)
    if not shots:
        return
    with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as library:
        env = dict(os.environ, BLOCKWRIGHT_USER_LIBRARY=library)
        subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL,
                       env=env)
        for step, dest in shots.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.png", HERE / dest)


def shot(step, of, cells=None, pixels=None):
    step = dict(step, screenshot={"of": of})
    if cells:
        step["screenshot"]["crop"] = {"cells": cells}
    if pixels:
        step["screenshot"]["crop"] = {"pixels": pixels}
    return step


def runs(name, fg, test, xs, ys):
    """Half block strokes, one per unbroken run of pixels in a row: the
    points of one stroke are joined by lines, so each run is its own."""
    steps = []
    for y in ys:
        row = [x for x in xs if test(x, y)]
        while row:
            end = 0
            while end + 1 < len(row) and row[end + 1] == row[end] + 1:
                end += 1
            steps.append({"name": f"{name}-{len(steps) + 1}", "action": "halfBlock", "fg": fg,
                          "points": [[row[0], y], [row[end], y]]})
            row = row[end + 1:]
    steps[-1]["name"] = name
    return steps


def star(n, x, y):
    return {"name": f"star-{n}", "action": "glyph", "glyph": "·", "fg": GREY, "bg": BLACK, "points": [[x, y]]}


# The scene's ground, on the Background layer: a shore and a lake, the moon
# at the upper left, its broken reflection under it, and a few stars.
SHINE = {31: (5, 6, 7, 8, 9, 10), 33: (6, 7, 9, 10, 11), 35: (4, 5, 7, 8), 37: (8, 9, 10), 39: (6, 7)}
GROUND = [
    {"name": "shore", "action": "rectangle", "fg": GREEN, "filled": True, "symmetry": "none",
     "from": [0, 26], "to": [59, 27]},
    {"name": "bank", "action": "rectangle", "fg": BROWN, "from": [0, 28], "to": [59, 29]},
    {"name": "lake", "action": "rectangle", "fg": BLUE, "from": [0, 30], "to": [59, 39]},
    {"name": "moon", "action": "ellipse", "fg": WHITE, "from": [4, 2], "to": [11, 9]},
] + runs("moon-shine", WHITE, lambda x, y: x in SHINE.get(y, ()), range(0, 14), range(30, 40)) + \
    [star(n, x, y) for n, (x, y) in enumerate([(17, 1), (27, 6), (35, 2), (58, 5), (15, 9), (57, 11)], 1)]

# The parts, on a Cells layer of their own, laid out in the empty sky: a
# pine nine cells across lit from the right, a dead snag of right half
# blocks, and a far ridge lit from the left. Each canopy row is the same
# width in both its halves, so the pine's cells are whole blocks.
PINE_X, PINE_TIP = 53, 3


def canopy(x, y):
    if y == PINE_TIP:
        return x == PINE_X
    if not PINE_TIP < y <= PINE_TIP + 18:
        return False
    tier, row = divmod(y - PINE_TIP - 1, 6)
    return abs(x - PINE_X) <= 1 + tier + row // 2


def ridge_top(x):
    return min(4 + abs(x - 19), 6 + abs(x - 28))


pine_xs, pine_ys = range(PINE_X - 6, PINE_X + 7), range(0, 24)
ridge_xs, ridge_ys = range(14, 34), range(4, 12)
PARTS = [
    {"name": "parts-layer", "action": "newCellsLayer", "rename": "parts"},
] + runs("pine-dark", GREEN, lambda x, y: canopy(x, y) and x <= PINE_X, pine_xs, pine_ys) + \
    runs("pine-lit", LIGHT_GREEN, lambda x, y: canopy(x, y) and x > PINE_X, pine_xs, pine_ys) + [
    {"name": "pine-trunk", "action": "halfBlock", "fg": BROWN, "points": [[PINE_X, 22], [PINE_X, 23]]},
    {"name": "snag", "action": "glyph", "glyph": "▐", "fg": BROWN, "bg": BLACK,
     "points": [[40, 4], [40, 7]]},
] + runs("ridge-lit", GREY, lambda x, y: y >= ridge_top(x) and (x < 19 or 23 < x < 28), ridge_xs, ridge_ys) + \
    runs("ridge-dark", DARK_GREY, lambda x, y: y >= ridge_top(x) and not (x < 19 or 23 < x < 28), ridge_xs,
         ridge_ys)
start = blank(60, 20)
replay("start", start, GROUND + PARTS, {"ridge-dark": "start.bwp"})

# The scene put together, one tool at a time: the pine moved to the shore
# and flipped to face the moon, the snag turned into a log and moved, the
# ridge cut and pasted Under, so it goes behind the pine, and the pine's top
# copied and pasted Transparent in front of both, a younger tree.
PARTS_ACTIVE = {"name": "parts-active", "action": "setActiveLayer", "layer": "parts"}
SELECT_PINE = {"name": "select-pine", "action": "select", "rect": [48, 1, 58, 11]}
MOVE_PINE = {"name": "move-pine", "action": "moveSelection", "by": [-4, 2]}
FLIP = {"name": "flip-pine", "action": "flipHorizontal"}
STAMP_PINE = {"name": "stamp-pine", "action": "deselect"}
SNAG = [{"name": "select-snag", "action": "select", "rect": [40, 4, 40, 7]},
        {"name": "rotate-snag", "action": "rotateClockwise"},
        {"name": "move-log", "action": "moveSelection", "by": [-26, 8]},
        {"name": "stamp-log", "action": "deselect"}]
RIDGE = [{"name": "select-ridge", "action": "select", "rect": [14, 2, 33, 5]},
         {"name": "cut-ridge", "action": "cut"}]
UNDER = {"name": "paste-ridge", "action": "paste", "at": [27, 9], "pasteMode": "under"}
STAMP_RIDGE = {"name": "stamp-ridge", "action": "deselect"}
COPY = [{"name": "select-top", "action": "select", "rect": [45, 3, 53, 9], "pasteMode": "transparent"},
        {"name": "copy-top", "action": "copy"}]
PASTE = {"name": "paste-pine", "action": "paste", "at": [34, 8]}
STAMP_COPY = {"name": "stamp-copy", "action": "deselect"}

PINE = [PARTS_ACTIVE, SELECT_PINE, MOVE_PINE, FLIP, STAMP_PINE]
steps = PINE + SNAG + RIDGE + [UNDER, STAMP_RIDGE] + [shot(COPY[0], "toolOptions", pixels=[0, 0, 256, 920]), COPY[1], PASTE, STAMP_COPY]
replay("final", "start.bwp", steps,
       {"move-pine": "step-01.bwp", "flip-pine": "step-02.bwp", "rotate-snag": "step-03.bwp",
        "move-log": "step-04.bwp", "cut-ridge": "step-05.bwp", "paste-ridge": "step-06.bwp",
        "paste-pine": "step-07.bwp", "stamp-copy": "final.bwp"},
       {"select-top": "paste-mode.png"}, window=WINDOW)
# The marquee round the pine, in the window: a "view" step scrolls the
# canvas to the pine first (the CLI's replay has no window, so this one is
# played by the editor only).
look = [PARTS_ACTIVE, {"name": "scroll", "action": "view", "scrollTo": [36, 0]},
        shot(SELECT_PINE, "canvasView", [36, 0, 24, 14])]
replay("marquee", "start.bwp", look, {}, {"select-pine": "marquee.png"}, window=WINDOW)

# What goes wrong. The pine left as it came, lit from the side away from
# the moon; and the ridge pasted in Normal mode, its right slope written
# over the pine's lower left edge.
unflipped = [PARTS_ACTIVE, SELECT_PINE, MOVE_PINE, STAMP_PINE] + SNAG + RIDGE + [UNDER, STAMP_RIDGE] + COPY + \
    [PASTE, STAMP_COPY]
replay("unflipped", "start.bwp", unflipped, {"stamp-copy": "unflipped.bwp"})
over = PINE + SNAG + RIDGE + [dict(UNDER, pasteMode="normal"), STAMP_RIDGE]
replay("over", "start.bwp", over, {"stamp-ridge": "over.bwp"})

# The Library dock, with no stamps of your own yet.
replay("library", "start.bwp", [shot({"name": "library", "action": "deselect"}, "libraryDock", pixels=[0, 0, 321, 500])], {},
       {"library": "library.png"}, window=[1280, 2200])

# Try it: the finished scene. The answers: the log stood back up as a snag
# at the end of the shore, and a third pine, the big one's top tier, pasted
# far off on the right.
shutil.copyfile(HERE / "final.bwp", HERE / "try.bwp")
steps = [PARTS_ACTIVE, {"name": "select-log", "action": "select", "rect": [14, 12, 17, 12]},
         {"name": "rotate-log", "action": "rotateCounterClockwise"},
         {"name": "move-snag", "action": "moveSelection", "by": [4, -3]},
         {"name": "stamp-snag", "action": "deselect"}]
replay("try-snag", "try.bwp", steps, {"stamp-snag": "try-snag.bwp"})
steps = [PARTS_ACTIVE, {"name": "select-tier", "action": "select", "rect": [47, 3, 51, 6]},
         {"name": "copy-tier", "action": "copy"},
         {"name": "paste-tier", "action": "paste", "at": [55, 9], "pasteMode": "transparent"},
         {"name": "stamp-tier", "action": "deselect"}]
replay("try-pine", "try.bwp", steps, {"stamp-tier": "try-pine.bwp"})
