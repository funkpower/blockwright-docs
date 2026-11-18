#!/usr/bin/env python3
"""Write tutorial 13's samples: python3 -I samples/13-frames-and-canvas-size/make.py

The hi-score board starts as a flat .ans (start.ans). The rest is a steps
file played by `blockwright-cli replay` (the CLI is $BLOCKWRIGHT_CLI, else
blockwright-cli on PATH): the Canvas Size step, the typed source of a frame
style and its Delete are the editor's own actions. A steps file has no Frame
tool action, so each frame is laid as the cells the Frame tool writes: the
style's source cut nine ways and stretched to the drag (frame.py, a copy of
the editor's drawFrame), one glyph stroke per unbroken run of a cell. The
sheet of built-in styles and the frame on the uncut board are drawn the
same way straight into an .ans.
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE.parent.parent / "scripts"))
sys.path.insert(0, str(HERE))
from ansi import Canvas  # noqa: E402
from frame import BUILT_IN, draw_frame, style_from_cells  # noqa: E402

BLACK, GREY, DARK_GREY = 0, 7, 8
LIGHT_GREEN, LIGHT_CYAN, LIGHT_RED, LIGHT_MAGENTA, YELLOW, WHITE = 10, 11, 12, 13, 14, 15
TITLE = "Frames and canvas size"
DATE = "20261118"
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"

SCORES = [("1", "FNK", "98,400"), ("2", "BWR", "76,250"), ("3", "ACE", "51,900"), ("4", "ZAP", "30,050")]


def board():
    """The board as it starts: 30 x 10, a blank row above and below the
    scores where a box will go."""
    c = Canvas(30, 10)
    c.text(7, 0, "MOONLIGHT ARCADE", YELLOW)
    for i, (rank, name, score) in enumerate(SCORES):
        y = 3 + i
        c.text(3, y, rank, WHITE)
        c.text(6, y, name, LIGHT_CYAN)
        c.text(11, y, "........", DARK_GREY)
        c.text(21, y, score, LIGHT_GREEN)
    c.text(9, 9, "INSERT COINS", LIGHT_RED)
    return c


def frame_cells(style, x0, y0, x1, y1, pen=None):
    """The cells a left-button drag from x0, y0 to x1, y1 writes, as the
    Frame tool writes them: Pen colours recolour every drawn cell."""
    cells = draw_frame(style, x1 - x0 + 1, y1 - y0 + 1)
    out = []
    for (x, y), (ch, fg, bg) in sorted(cells.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        if pen:
            fg, bg = pen
        out.append((x0 + x, y0 + y, ch, fg, bg))
    return out


def frame_steps(name, cells):
    """Glyph strokes laying the cells: one per unbroken run along a row of
    one glyph in one pair of colours (a stroke's points are joined by lines)."""
    steps, run = [], []

    def flush():
        if run:
            x, y, ch, fg, bg = run[0]
            steps.append({"name": f"{name}-{len(steps) + 1}", "action": "glyph", "glyph": ch, "fg": fg,
                          "bg": bg, "points": [[x, y], [run[-1][0], y]]})
            run.clear()

    for cell in cells:
        if run and (cell[1] != run[-1][1] or cell[0] != run[-1][0] + 1 or cell[2:] != run[-1][2:]):
            flush()
        run.append(cell)
    flush()
    steps[0]["size"], steps[0]["tip"], steps[0]["symmetry"] = 1, "square", "none"
    steps[-1]["name"] = name
    return steps


def lay(canvas, cells):
    for x, y, ch, fg, bg in cells:
        canvas.put(x, y, ch, fg, bg)


def write_steps(name, start, steps):
    path = HERE / f"{name}.steps.json"
    body = {"version": 1, "start": {"file": start}, "steps": steps}
    path.write_text(json.dumps(body, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def replay(name, start, steps, keep):
    """Writes the steps file and plays it; keep maps a step's name to the
    .ans its capture becomes."""
    path = write_steps(name, start, steps)
    number = {step["name"]: i + 1 for i, step in enumerate(steps)}
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([CLI, "replay", str(path), "-o", tmp], check=True, stdout=subprocess.DEVNULL)
        for step, dest in keep.items():
            shutil.copyfile(Path(tmp) / f"{number[step]:02d}-{step}.ans", HERE / dest)


def styles_sheet():
    """Every built-in style at 12 x 6, four to a row, in the list's order."""
    c = Canvas(56, 24)
    for i, style in enumerate(BUILT_IN):
        x, y = 1 + (i % 4) * 14, 1 + (i // 4) * 8
        lay(c, frame_cells(style, x, y, x + 11, y + 5))
    c.save(HERE / "styles.ans", title=TITLE, date=DATE)


# The board grown to 38 x 14 with the old canvas in the centre: 4 columns
# each side, 2 rows top and bottom. Then a Double line box round the scores
# in its own grey, the same drag again in a yellow pen, the source of a
# frame style typed in the free corner at 1, 10, and, once it is saved and
# deleted, that style round the whole board.
DOUBLE, SINGLE = BUILT_IN[1], BUILT_IN[0]
BOX = (5, 4, 32, 9)
OUTER = (0, 0, 37, 13)
SOURCE_AT = (1, 10)
SOURCE = ["♦·♦", "· ·", "♦·♦"]
PEN = (YELLOW, BLACK)


def diamond():
    """The style Save as Frame Style makes of the source: corner columns
    and rows 1, Draw the middle off."""
    rows = [[(ch, LIGHT_MAGENTA, BLACK) for ch in r] for r in SOURCE]
    return style_from_cells(rows, inset=1, fill=False)


def main():
    board().save(HERE / "start.ans", title=TITLE, date=DATE)
    styles_sheet()

    grow = {"name": "grown", "action": "canvasSize", "size": [38, 14], "anchor": "centre"}
    source = [{"name": f"source-{i + 1}", "action": "keyboard", "at": [SOURCE_AT[0], SOURCE_AT[1] + i],
               "text": row, "fg": LIGHT_MAGENTA, "bg": BLACK} for i, row in enumerate(SOURCE)]
    source[-1]["name"] = "source"
    sx, sy = SOURCE_AT
    clear = [{"name": "select-source", "action": "select", "rect": [sx, sy, sx + 2, sy + 2]},
             {"name": "deleted", "action": "deleteSelection"},
             {"name": "deselect", "action": "deselect"}]
    grey_box = frame_steps("box-grey", frame_cells(DOUBLE, *BOX))
    yellow_box = frame_steps("box-yellow", frame_cells(DOUBLE, *BOX, pen=PEN))
    outer = frame_steps("final", frame_cells(diamond(), *OUTER))
    replay("do-it", "start.ans", [grow] + grey_box + yellow_box + source + clear + outer,
           {"grown": "grown.ans", "box-grey": "box-grey.ans", "box-yellow": "box-yellow.ans",
            "source": "source.ans", "final": "final.ans"})

    # What goes wrong: a frame on the board before it grows writes over the
    # title and the last line; the anchor left at top left puts every new
    # cell on the right and below; the source left on the canvas; the
    # outer frame drawn with Pen colours still on.
    tight = board()
    lay(tight, frame_cells(DOUBLE, 0, 0, 29, 9))
    tight.save(HERE / "too-tight.ans", title=TITLE, date=DATE)
    replay("top-left", "start.ans", [dict(grow, name="top-left", anchor="top-left")],
           {"top-left": "top-left.ans"})
    replay("left-over", "start.ans", [grow] + grey_box + yellow_box + source +
           frame_steps("left-over", frame_cells(diamond(), *OUTER)), {"left-over": "left-over.ans"})
    replay("pen-left-on", "start.ans", [grow] + grey_box + yellow_box + source + clear +
           frame_steps("pen-left-on", frame_cells(diamond(), *OUTER, pen=PEN)), {"pen-left-on": "pen-left-on.ans"})

    # Try it: on the finished board, the box's title set as a tab in its
    # top rule; and the box erased with the right button (a blank, a space in
    # grey on black, where each of its cells was) and drawn again in Single
    # line with a light cyan pen.
    tab = [{"name": "tab", "action": "keyboard", "at": [13, 4], "text": " TOP SCORES ", "fg": WHITE,
            "bg": BLACK}]
    replay("try-tab", "final.ans", tab, {"tab": "try-tab.ans"})
    erase = frame_steps("erased", [(x, y, " ", GREY, BLACK) for x, y, *_ in frame_cells(DOUBLE, *BOX)])
    single = frame_steps("single", frame_cells(SINGLE, *BOX, pen=(LIGHT_CYAN, BLACK)))
    replay("try-single", "final.ans", erase + single, {"erased": "try-erased.ans", "single": "try-single.ans"})

if __name__ == "__main__":
    main()
