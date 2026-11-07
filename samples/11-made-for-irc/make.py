#!/usr/bin/env python3
"""Write tutorial 11's samples: python3 -I samples/11-made-for-irc/make.py

Every picture is a steps file played by `blockwright-cli replay --project`
(the CLI is $BLOCKWRIGHT_CLI, else blockwright-cli on PATH): a marquee sign
on an IRC-target canvas, its bulbs half-block pixels painted with the
Half-Block Brush, its letters strokes of the brush through each letter's
pixels, and a ★ either side typed with the Keyboard tool. The canvases the
steps start from are blank .ans files (which carry the SAUCE) packed as
IRC-target projects with `blockwright-cli pack --target irc`. This script
writes the steps files (*.steps.json) and those starts, replays each into a
scratch directory, and copies the captures the page shows beside them. The
pictures of the editor (the row meter, the IRC View and Lint docks) come
from steps played in the window by `blockwright --screenshot` (the editor is
$BLOCKWRIGHT, else blockwright); the full-width IRC views (irc-*.png) from
`blockwright-cli render --irc`; and the byte counts and findings from
`blockwright-cli export --irc` (export-*.txt) and `lint` (lint-*.txt).
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

BLACK = 0
LIGHT_GREEN, LIGHT_CYAN, LIGHT_RED, YELLOW, WHITE = 10, 11, 12, 14, 15
TITLE = "Made for IRC"
DATE = "20261106"
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
GUI = os.environ.get("BLOCKWRIGHT") or "blockwright"
WINDOW = [1280, 1300]

# Letters 10 pixels tall with 2-pixel stems, as tutorial 10 draws them.
FACE = {
    "I": """
######
######
..##..
..##..
..##..
..##..
..##..
..##..
######
######""",
    "R": """
#####.
######
##..##
##..##
#####.
####..
##.##.
##.##.
##..##
##..##""",
    "C": """
.#####
######
##....
##....
##....
##....
##....
##....
######
.#####""",
}


def bitmap(key):
    rows = FACE[key].strip("\n").split("\n")
    return [(x, y) for y, row in enumerate(rows) for x, ch in enumerate(row) if ch == "#"]


def walk(pixels):
    """The pixels in an order a stroke can take: each point beside the last,
    going back over painted pixels where it must, so the stroke joins
    neighbours only and paints nothing else."""
    left = set(pixels)
    start = min(pixels, key=lambda p: (p[1], p[0]))
    path, stack = [start], [start]
    left.discard(start)
    while stack:
        x, y = stack[-1]
        for n in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if n in left:
                left.discard(n)
                stack.append(n)
                path.append(n)
                break
        else:
            stack.pop()
            if stack:
                path.append(stack[-1])
    assert not left, "a letter's pixels must join left, right, up or down"
    return path


def letter(name, key, x, py, **options):
    points = [[x + dx, py + dy] for dx, dy in walk(bitmap(key))]
    return dict({"name": name, "action": "halfBlock"}, **options, points=points)


def start_project(w, h):
    """A blank w x h canvas packed as an IRC-target project."""
    ans = HERE / f"blank-{w}x{h}.ans"
    Canvas(w, h).save(ans, title=TITLE, date=DATE)
    bwp = HERE / f"blank-{w}x{h}.bwp"
    subprocess.run([CLI, "pack", "--target", "irc", str(ans), str(bwp)], check=True, stdout=subprocess.DEVNULL)
    return bwp.name


def write_steps(name, start, steps, window=None):
    path = HERE / f"{name}.steps.json"
    body = {"version": 1, "start": {"file": start}, "steps": steps}
    if window:
        body["window"] = window
    text = json.dumps(body, indent=1, ensure_ascii=False)
    path.write_text(text + "\n", encoding="utf-8")
    return path


def replay(name, start, steps, keep, shots=None, window=None):
    """Writes the steps file and plays it; keep maps a step's name to the
    .bwp its capture becomes. shots maps a step's name to the PNG its
    "screenshot" becomes, taken in the window. The .ans captures are written
    as UTF-8, which holds the ★."""
    path = write_steps(name, start, steps, window)
    number = {step["name"]: i + 1 for i, step in enumerate(steps)}
    if keep:  # the CLI's replay has no window, so it refuses a "view" step
        with tempfile.TemporaryDirectory() as tmp:
            cmd = [CLI, "replay", str(path), "-o", tmp, "--project", "--output-encoding", "utf-8"]
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
            for step, dest in keep.items():
                shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.bwp", HERE / dest)
    if not shots:
        return
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([GUI, "--screenshot", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        for step, dest in shots.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.png", HERE / dest)


def shot(step, of, crop=None):
    step = dict(step, screenshot={"of": of})
    if crop:
        step["screenshot"]["crop"] = {"pixels": crop}
    return step


def export(piece, report, *options, text=None):
    """`export --irc` of the piece, run in a scratch directory with the piece
    copied in, so the report names files only by name; its report (stdout,
    then stderr, and the exit status when it isn't 0) goes in `report`, and
    the IRC text, when it is written, in `text`."""
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copyfile(HERE / piece, Path(tmp) / piece)
        out = Path(piece).stem + ".txt"
        r = subprocess.run([CLI, "export", "--irc", *options, piece, out], cwd=tmp, capture_output=True, text=True)
        if text:
            shutil.copyfile(Path(tmp) / out, HERE / text)
    status = f"exit status {r.returncode}\n" if r.returncode else ""
    (HERE / report).write_text(r.stdout + r.stderr + status, encoding="utf-8")


def lint(piece, report):
    """`lint` of the piece: its findings and summary, and the exit status
    when it isn't 0, in `report`."""
    r = subprocess.run([CLI, "lint", piece], cwd=HERE, capture_output=True, text=True)
    status = f"exit status {r.returncode}\n" if r.returncode else ""
    (HERE / report).write_text(r.stdout + r.stderr + status, encoding="utf-8")


def irc_view(piece, png, *options):
    """The IRC view of the piece as `render --irc` draws it, at 2x."""
    subprocess.run([CLI, "render", "--irc", "--scale", "2", *options, piece, png], cwd=HERE, check=True,
                   stdout=subprocess.DEVNULL)


def look(name, start, shots):
    """Pictures of the editor with `start` open, a step each: shots is a list
    of (step name, "of", crop) or (step name, "of", crop, view), the PNG
    named after the step. Each step is a Deselect, which changes nothing, or,
    given a view (the "view" step's fields, such as {"ircFit": True}), a
    "view" step, which changes the window and not the piece. A first step
    takes the IRC View, which brings its tab to the front of the dock it
    shares with Lint; that picture isn't kept."""
    steps = [shot({"name": "irc-view", "action": "deselect"}, "ircView")]
    for n, of, crop, *view in shots:
        step = {"name": n, "action": "view", **view[0]} if view else {"name": n, "action": "deselect"}
        steps.append(shot(step, of, crop))
    replay(name, start, steps, {}, {s[0]: f"{s[0]}.png" for s in shots}, window=WINDOW)


W, H = 80, 9
BULBS = [LIGHT_RED, YELLOW, LIGHT_GREEN, LIGHT_CYAN]
TOP, BOTTOM = 1, 2 * H - 1  # the bulbs' pixel rows: the bottom halves of rows 0 and 8


def bulb(name, x, py, colour):
    return {"name": name, "action": "halfBlock", "fg": colour, "points": [[x, py]]}


def bulb_row(prefix, py, columns):
    return [bulb(f"{prefix}-{x}", x, py, BULBS[x % len(BULBS)]) for x in columns]


def sign(row_offset=0):
    """The sign as first drawn: bulbs in every cell of the top and bottom
    rows, IRC in white, a ★ either side."""
    top, bottom = TOP + 2 * row_offset, BOTTOM + 2 * row_offset
    steps = bulb_row("top", top, range(W)) + bulb_row("bottom", bottom, range(W))
    x = 28
    for i, key in enumerate("IRC"):
        steps.append(letter(f"letter-{i}", key, x, 4 + 2 * row_offset, **({"fg": WHITE} if i == 0 else {})))
        x += 8
    for side, x in [("left", 24), ("right", 53)]:
        steps.append({"name": f"star-{side}", "action": "keyboard", "fg": YELLOW, "bg": BLACK,
                      "at": [x, 4 + row_offset], "text": "★"})
    return steps


def fix(row_offset=0):
    """Each pair of bulbs painted again in one colour, two cells a bulb,
    then a bulb filling the first and last cell of each row between."""
    top, bottom = TOP + 2 * row_offset, BOTTOM + 2 * row_offset
    steps = []
    for name, py in [("top", top), ("bottom", bottom)]:
        steps += [{"name": f"pair-{name}-{k}", "action": "halfBlock", "fg": BULBS[k % len(BULBS)],
                   "points": [[2 * k, py], [2 * k + 1, py]]} for k in range(W // 2)]
    for y in range(1 + row_offset, H - 1 + row_offset):
        k = y - row_offset
        for side, x in [("left", 0), ("right", W - 1)]:
            steps.append({"name": f"{side}-{k}", "action": "halfBlock", "fg": BULBS[(k + 2 * (x > 0)) % len(BULBS)],
                          "points": [[x, 2 * y], [x, 2 * y + 1]]})
    return steps


start = start_project(W, H)
drawn = sign()
replay("sign", start, drawn, {drawn[-1]["name"]: "over.bwp"})
fixed = fix()
replay("fix", "over.bwp", fixed, {fixed[-1]["name"]: "final.bwp"})
export("over.bwp", "export-over.txt")
export("over.bwp", "export-fit.txt", "--fit")
export("final.bwp", "export-final.txt", text="final.txt")
irc_view("over.bwp", "irc-over.png")
irc_view("over.bwp", "irc-fit.png", "--fit")
irc_view("final.bwp", "irc-final.png")
METER = [263, 446, 702, 304]   # the canvas's columns 0-40 and the row meter
BESIDE = [263, 446, 1017, 690]  # the same, and the IRC View under them
look("look-over", "over.bwp", [("meter-over", "window", METER), ("beside-over", "window", BESIDE), ("lint-over", "lint", None),
                               ("meter-fit", "window", METER, {"ircFit": True})])
look("look-final", "final.bwp", [("meter-final", "window", METER), ("lint-final", "lint", None)])

# Try it: the finished sign on a canvas a row taller at the top and the
# bottom. The answer keeps the margin with a black-on-black █ at the end
# of each blank row.
start = start_project(W, H + 2)
steps = sign(row_offset=1) + fix(row_offset=1)
replay("try", start, steps, {steps[-1]["name"]: "try.bwp"})
lint("try.bwp", "lint-try.txt")
export("try.bwp", "export-try.txt")
export("try.bwp", "export-try-pad.txt", "--pad")
margin = [{"name": f"margin-{y}", "action": "keyboard", "fg": BLACK, "bg": BLACK, "at": [W - 1, y], "text": "█"}
          for y in (0, H + 1)]
replay("try-answer", "try.bwp", margin, {margin[-1]["name"]: "try-answer.bwp"})
lint("try-answer.bwp", "lint-try-answer.txt")
export("try-answer.bwp", "export-try-answer.txt")
