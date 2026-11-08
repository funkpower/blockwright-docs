# Meteors falling down to the left: a white * head, then a tail of / up to
# the right, the first half in the Tail colour and the rest dark grey dots.
# Every other cell is a black space, which the key colour makes transparent.
import json
import sys

job = json.loads(sys.stdin.readline())
w, h = job["layer"]["width"], job["layer"]["height"]
p = job["params"]
state = p["seed"]


def below(n):
    """A whole number from 0 to n - 1, from the seed: the same every run."""
    global state
    state = (state * 1664525 + 1013904223) % 2**32
    return state * n // 2**32


cells = {}
placed = 0
bottom = min(p["bottom"], h - 1)
for _ in range(1000):
    if placed == p["count"]:
        break
    x, y = below(w), below(bottom + 1)
    trail = [(x + i, y - i) for i in range(p["length"])]
    if any(not (0 <= cx < w and 0 <= cy) for cx, cy in trail):
        continue
    if any((cx + dx, cy + dy) in cells for cx, cy in trail for dx in (-1, 0, 1) for dy in (-1, 0, 1)):
        continue
    for i, cell in enumerate(trail):
        if i == 0:
            cells[cell] = ("*", 15)
        elif i <= p["length"] // 2:
            cells[cell] = ("/", p["colour"])
        else:
            cells[cell] = ("\xfa", 8)
    placed += 1

SGR = [30, 34, 32, 36, 31, 35, 33, 37]  # the PC's colour order to ANSI's
out = sys.stdout.buffer
for y in range(h):
    for x in range(w):
        glyph, fg = cells.get((x, y), (" ", 7))
        bold = "1;" if fg > 7 else ""
        out.write(f"\x1b[0;{bold}{SGR[fg % 8]};40m".encode() + glyph.encode("latin-1"))
    out.write(b"\x1b[0m\r\n")
