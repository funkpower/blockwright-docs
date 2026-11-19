#!/usr/bin/env python3
"""Write the Micron colour table's sample: python3 -I samples/manual-09-colour/micron.py

micron-colours.bwp is a Micron-target project of one layer, 16 cells wide:
row 1 the 16 colours as foregrounds on a full block, row 2 as backgrounds on
a space, row 3 and 4 the colours from mIRC's 99 that the table names (RGB
cells, as a piece drawn under the IRC target holds them), as foregrounds and
backgrounds, row 5 a twelve-bit colour from the Micron colour dialog as a
foreground and as a background, and row 6 an ordinary cell in the pen's
starting colours. micron-colours.mu is
`blockwright-cli export --micron` of it, and the page's table is copied from
that file. The project is built here as a project directory (PLAN.md §6 of
Blockwright: manifest, a layer's JSON and its .cells) and packed with
`blockwright-cli pack --target micron`; the CLI is $BLOCKWRIGHT_CLI, else
blockwright-cli on PATH.
"""

import json
import os
import struct
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"

WIDTH = 16
FULL, SPACE, X = 0x2588, 0x20, ord("x")


def idx(i):
    return bytes([0, i, 0, 0])


def rgb(v):
    return bytes([1, v >> 16, (v >> 8) & 255, v & 255])


def cell(cp, fg, bg):
    return struct.pack("<I", cp) + fg + bg + bytes([0, 0])


# mIRC 16, 63 and 77 are not twelve-bit; 52 happens to be; 0x3366cc is a
# colour the dialog's digits write (36c).
MIRC = [(16, 0x470000), (52, 0xFF0000), (63, 0xFF0098), (77, 0xFFD39C)]
PICKED = 0x3366CC

rows = []
rows.append([cell(FULL, idx(i), idx(0)) for i in range(16)])
rows.append([cell(SPACE, idx(7), idx(i)) for i in range(16)])
rows.append([cell(FULL, rgb(v), idx(0)) for _, v in MIRC] + [cell(SPACE, idx(7), idx(0))] * (WIDTH - len(MIRC)))
rows.append([cell(SPACE, idx(7), rgb(v)) for _, v in MIRC] + [cell(SPACE, idx(7), idx(0))] * (WIDTH - len(MIRC)))
rows.append([cell(FULL, rgb(PICKED), idx(0)), cell(SPACE, idx(7), rgb(PICKED))]
            + [cell(SPACE, idx(7), idx(0))] * (WIDTH - 2))
rows.append([cell(X, idx(7), idx(0))] + [cell(SPACE, idx(7), idx(0))] * (WIDTH - 1))
HEIGHT = len(rows)


def main():
    with tempfile.TemporaryDirectory() as tmp:
        proj = Path(tmp) / "proj"
        (proj / "layers").mkdir(parents=True)
        (proj / "manifest.json").write_text(json.dumps({
            "format": "blockwright", "height": HEIGHT, "ice": True,
            "ircBudget": {"bytes": 407, "profile": "efnet-weechat"},
            "layers": [1], "nextLayerId": 2, "palette": "cga", "sauce": None,
            "version": "1.3", "width": WIDTH}, indent=4) + "\n")
        (proj / "layers" / "1.json").write_text(json.dumps({
            "alphaLocked": False, "height": HEIGHT, "id": 1, "kind": "cells",
            "locked": False, "mode": "normal", "name": "Background",
            "visible": True, "width": WIDTH, "x": 0, "y": 0}, indent=4) + "\n")
        raw = Path(tmp) / "cells.raw"
        raw.write_bytes(b"".join(c for row in rows for c in row))
        frame = subprocess.run(["zstd", "-q", "-3", "-c", str(raw)], check=True, capture_output=True).stdout
        (proj / "layers" / "1.cells").write_bytes(
            b"BWCL" + struct.pack("<HHII", 1, 0, WIDTH, HEIGHT) + frame)
        bwp = HERE / "micron-colours.bwp"
        subprocess.run([CLI, "pack", "--target", "micron", str(proj), str(bwp)],
                       check=True, stdout=subprocess.DEVNULL)
    subprocess.run([CLI, "export", "--micron", str(HERE / "micron-colours.bwp"), str(HERE / "micron-colours.mu")],
                   check=True, stdout=subprocess.DEVNULL)


if __name__ == "__main__":
    main()
