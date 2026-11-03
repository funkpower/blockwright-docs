#!/usr/bin/env python3
"""Write the file formats page's samples: python3 -I samples/manual-file-formats/make.py

piece.ans uses bright backgrounds (iCE colours); blink.ans is the same cells
in a file with iCE colours off, where those backgrounds blink instead.
palette.xb is an XBIN with a palette of its own, written byte by byte here.
"""

import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "scripts"))
from ansi import Canvas  # noqa: E402

BLACK, BLUE, GREEN, CYAN, RED, MAGENTA, BROWN, GREY = range(8)
DARK_GREY, LIGHT_BLUE, LIGHT_GREEN, LIGHT_CYAN, LIGHT_RED, LIGHT_MAGENTA, YELLOW, WHITE = range(8, 16)
UPPER, LOWER, FULL = "▀", "▄", "█"
LIGHT, MEDIUM, DARK = "░", "▒", "▓"

W, H = 32, 8


def piece():
    c = Canvas(W, H)
    # a sky from blue down to light cyan, the light rows on bright backgrounds
    sky = [(" ", GREY, BLUE), (LIGHT, LIGHT_BLUE, BLUE), (MEDIUM, LIGHT_BLUE, BLUE),
           (" ", GREY, LIGHT_BLUE), (LIGHT, LIGHT_CYAN, LIGHT_BLUE)]
    for y, (ch, fg, bg) in enumerate(sky):
        c.fill(0, y, W - 1, y, ch, fg, bg)
    # a yellow sun on the light rows
    c.fill(22, 2, 26, 2, LOWER, YELLOW, BLUE)
    c.fill(21, 3, 27, 3, FULL, YELLOW, LIGHT_BLUE)
    c.fill(22, 4, 26, 4, UPPER, YELLOW, LIGHT_BLUE)
    # green ground and the signature
    c.fill(0, 5, W - 1, 5, UPPER, LIGHT_CYAN, GREEN)
    c.fill(0, 6, W - 1, 7, " ", GREY, GREEN)
    c.text(2, 6, "funkpower", YELLOW, GREEN)
    return c


c = piece()
c.save(HERE / "piece.ans", title="A sun over a field", ice=True)
c.save(HERE / "blink.ans", title="A sun over a field, blinking", ice=False)

# palette.xb: an 8x2 XBIN with its own palette (each index a different grey
# to green), uncompressed, with no font and no SAUCE.
pal = b"".join(bytes([0, i * 4, i * 2]) for i in range(16))
cells = b"".join(bytes([0xDB, i]) for i in range(16))
xb = b"XBIN\x1a" + struct.pack("<HHBB", 8, 2, 16, 0x01) + pal + cells
(HERE / "palette.xb").write_bytes(xb)

# mixed.ans: iCE colours off, a word that blinks, and two cells after it on
# a bright background (SGR 104, which a file without iCE colours can still
# name). Written byte by byte: Canvas can't put both in one file.
E = "\x1b["
body = (E + "0m" + E + "0;1;5;33;44mfunkpower" + E + "0;104m  " + E + "0m\r\n").encode("ascii")
sauce = (b"SAUCE00" + b"Blink and a bright background".ljust(35, b" ") + b"funkpower".ljust(20, b" ")
         + b"".ljust(20, b" ") + b"20261102"
         + struct.pack("<IBBHHHHBB", len(body), 1, 1, 11, 1, 0, 0, 0, 0) + b"IBM VGA".ljust(22, b"\0"))
assert len(sauce) == 128
(HERE / "mixed.ans").write_bytes(body + b"\x1a" + sauce)
