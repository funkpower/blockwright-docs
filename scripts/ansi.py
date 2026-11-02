"""A small cell canvas that writes .ans files with SAUCE, for the docs samples.

    from ansi import Canvas
    c = Canvas(32, 8)
    c.text(1, 1, "HELLO", fg=7, bg=0)
    c.save("step.ans", title="Hello", ice=True)

Colours are palette indices 0-15 in Blockwright's (and the PC's) order: 0 black,
1 blue, 2 green, 3 cyan, 4 red, 5 magenta, 6 brown, 7 grey, then the bright
eight in the same order. Each sample's make.py builds its canvases
with this and saves them; the site build renders the .ans files.

Half-block pixels draw the way Blockwright's half-block tools do
(core/src/halfblock.cpp and shapes.cpp): a cell is two pixels, its top and
bottom half, so pixel row py is cell row py // 2, the top half when py is
even. One colour is a space on a dark background or a full block in a bright
one; two are ▀ unless only ▄ keeps the background dark. Each call is one
tool use: the halves it plots are worked out per cell from the canvas as it
was, and a cell that isn't pixels (text, a shade) becomes pixels, its other
half the background it showed.

A cell is (glyph, fg, bg, blink). With iCE colours on, blink shows as the
bright version of the background; with them off, a bright background shows
as blink on its dark version (iceCell). A pixel drawn with iCE off keeps the
blink the cell showed, and a cell with blink is written with SGR 5 while iCE
is off.

    c.ellipse(2, 2, 13, 13, YELLOW, filled=True)
    c.line(0, 15, 9, 6, WHITE)
"""

import struct

ESC = "\x1b["

# Glyphs below 0x20 (and 0x7f) that Python's cp437 codec treats as control
# codes. Only those a reader takes as glyphs: not ESC, CR, LF, tab,
# backspace, bell or the SAUCE end-of-file mark.
LOW = {"☺": 0x01, "☻": 0x02, "♥": 0x03, "♦": 0x04, "♣": 0x05, "♠": 0x06,
       "♂": 0x0B, "♀": 0x0C, "♫": 0x0E, "☼": 0x0F, "►": 0x10, "◄": 0x11,
       "↕": 0x12, "‼": 0x13, "¶": 0x14, "§": 0x15, "▬": 0x16, "↨": 0x17,
       "↑": 0x18, "↓": 0x19, "∟": 0x1C, "↔": 0x1D, "▲": 0x1E, "▼": 0x1F,
       "⌂": 0x7F}


# SGR numbers the eight the other way round (1 red, 4 blue).
SGR = [0, 4, 2, 6, 1, 5, 3, 7]


def cp437(ch):
    if ch in LOW:
        return bytes([LOW[ch]])
    b = ch.encode("cp437")  # refuses a glyph CP437 can't hold
    if len(b) != 1 or b[0] < 0x20 or b[0] == 0x7F:
        raise ValueError(f"{ch!r} isn't a glyph this writer can put in an .ans")
    return b


UPPER, LOWER, FULL = "\u2580", "\u2584", "\u2588"
BLANKS = (" ", "\0", "\u00a0")


def shown(cell, ice):
    """The cell as it shows (iceCell): with iCE on blink is a bright background,
    with iCE off a bright background is blink on its dark colour."""
    ch, fg, bg, blink = cell
    if ice and blink:
        return (ch, fg, bg | 8, False)
    if not ice and bg >= 8:
        return (ch, fg, bg & 7, True)
    return cell


def half_pair(cell, ice=True):
    """A pixel cell's (top, bottom) colours as they show, or None."""
    ch, fg, bg, _ = shown(cell, ice)
    if ch in BLANKS:
        return (bg, bg)
    return {FULL: (fg, fg), UPPER: (fg, bg), LOWER: (bg, fg)}.get(ch)


def half_cell(top, bottom, ice=True, blink=False):
    """The cell that shows top over bottom (halfBlockCell)."""
    if not ice and top >= 8 and bottom >= 8 and top != bottom:
        bottom &= 7  # iCE off can't show two bright colours in one cell
    if top == bottom:
        return (" ", 7, top, blink) if top < 8 else (FULL, top, 0, blink)
    if bottom < 8 or top >= 8:
        return (UPPER, top, bottom, blink)
    return (LOWER, bottom, top, blink)


def written(cell, top, bottom, ice):
    """The pixel cell painted over cell: it keeps the blink cell showed."""
    return half_cell(top, bottom, ice, shown(cell, ice)[3])


def set_half(cell, bottom, colour, ice=True):
    """The cell with one half set to colour (setHalfBlock)."""
    pair = half_pair(cell, ice)
    if pair and pair[bottom] == colour:
        return cell
    if not pair:
        bg = shown(cell, ice)[2]
        pair = (bg, bg)
    other = pair[not bottom]
    if not ice and colour >= 8 and other >= 8 and other != colour:
        colour &= 7  # the half not painted keeps the colour it shows
    pair = (pair[0], colour) if bottom else (colour, pair[1])
    return written(cell, *pair, ice)


def set_halves(cell, colour, ice=True):
    """The cell with both halves set to colour (setHalfBlocks)."""
    if half_pair(cell, ice) == (colour, colour):
        return cell
    return written(cell, colour, colour, ice)


def line4(x0, y0, x1, y1):
    """The 4-connected line, both ends included: a diagonal step goes across first."""
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx, sy = (1 if x0 < x1 else -1), (1 if y0 < y1 else -1)
    i = j = 0
    err = dx - dy
    out = [(x0, y0)]
    while i != dx or j != dy:
        e2 = 2 * err
        step_x, step_y = e2 >= -dy, e2 <= dx
        if step_x and step_y:
            err -= dy
            i += 1
            out.append((x0 + sx * i, y0 + sy * j))
            err += dx
            j += 1
        elif step_x:
            err -= dy
            i += 1
        else:
            err += dx
            j += 1
        out.append((x0 + sx * i, y0 + sy * j))
    return out


def line8(x0, y0, x1, y1):
    """The 8-connected line: one point per step along the longer axis."""
    dx, dy = x1 - x0, y1 - y0
    n = max(abs(dx), abs(dy))
    if n == 0:
        return [(x0, y0)]

    def along(a, d, i):
        q, r = divmod(abs(d) * i, n)
        q += 1 if 2 * r >= n else 0
        return a - q if d < 0 else a + q

    return [(along(x0, dx, i), along(y0, dy, i)) for i in range(n + 1)]


def ellipse_pixels(x0, y0, x1, y1, filled):
    """The ellipse inside the box (ellipseShape)."""
    x0, x1 = min(x0, x1), max(x0, x1)
    y0, y1 = min(y0, y1), max(y0, y1)
    rx, ry = x1 - x0, y1 - y0
    a, b = float(rx) * float(rx + 2), float(ry) * float(ry + 2)

    def inside(x, y):
        X, Y = 2 * x - (x0 + x1), 2 * y - (y0 + y1)
        if abs(X) > rx or abs(Y) > ry:
            return False
        return float(X) * float(X) * b + float(Y) * float(Y) * a <= a * b

    out = []
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if inside(x, y) and (filled or any(not inside(x + i, y + j) for j in (-1, 0, 1) for i in (-1, 0, 1))):
                out.append((x, y))
    return out


def rect_pixels(x0, y0, x1, y1, filled):
    """The rectangle from corner to corner (rectShape)."""
    x0, x1 = min(x0, x1), max(x0, x1)
    y0, y1 = min(y0, y1), max(y0, y1)
    return [(x, y) for y in range(y0, y1 + 1) for x in range(x0, x1 + 1)
            if filled or y in (y0, y1) or x in (x0, x1)]


class Canvas:
    def __init__(self, width, height, fg=7, bg=0, ice=True):
        self.width, self.height = width, height
        self.ice = ice
        self.cells = [[(" ", fg, bg, False) for _ in range(width)] for _ in range(height)]

    def put(self, x, y, ch, fg=7, bg=0, blink=False):
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise ValueError(f"cell {x},{y} is off a {self.width}x{self.height} canvas")
        cp437(ch)
        self.cells[y][x] = (ch, fg, bg, blink)

    def text(self, x, y, s, fg=7, bg=0):
        for i, ch in enumerate(s):
            self.put(x + i, y, ch, fg, bg)

    def fill(self, x0, y0, x1, y1, ch=" ", fg=7, bg=0):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.put(x, y, ch, fg, bg)

    def copy(self):
        c = Canvas(self.width, self.height, ice=self.ice)
        c.cells = [row[:] for row in self.cells]
        return c

    # Half-block pixels: x is the column, py the pixel row (twice the cell
    # row, plus one for a bottom half). Pixels off the canvas are dropped.

    def plot(self, pixels, colour):
        """Plots pixels in one colour as one tool use (plotPixels)."""
        halves = {}
        for x, py in pixels:
            if 0 <= x < self.width and 0 <= py < 2 * self.height:
                halves[(x, py // 2)] = halves.get((x, py // 2), 0) | (2 if py % 2 else 1)
        for (x, y), h in halves.items():
            cell = self.cells[y][x]
            self.cells[y][x] = set_halves(cell, colour, self.ice) if h == 3 else set_half(cell, h == 2, colour, self.ice)

    def pencil(self, points, colour, connected=4):
        """A half-block brush stroke through points, each joined to the last."""
        join = line4 if connected == 4 else line8
        pixels, last = [], None
        for p in points:
            pixels += join(*last, *p) if last and last != p else [p]
            last = p
        self.plot(pixels, colour)

    def line(self, x0, y0, x1, y1, colour):
        """The line tool: 4-connected, walked from the end higher up (then further left)."""
        if (y1, x1) < (y0, x0):
            x0, y0, x1, y1 = x1, y1, x0, y0
        self.plot(line4(x0, y0, x1, y1), colour)

    def rect(self, x0, y0, x1, y1, colour, filled=False):
        self.plot(rect_pixels(x0, y0, x1, y1, filled), colour)

    def ellipse(self, x0, y0, x1, y1, colour, filled=False):
        self.plot(ellipse_pixels(x0, y0, x1, y1, filled), colour)

    def pick(self, x, py, background=False):
        """The eyedropper: the colour of the half under (x, py) on a pixel cell."""
        cell = self.cells[py // 2][x]
        pair = half_pair(cell, self.ice)
        if pair:
            return pair[py % 2]
        return shown(cell, self.ice)[2] if background else cell[1]

    def fill_pixels(self, x, py, colour):
        """The fill tool: the 4-connected pixels of the clicked colour, through pixel cells only."""
        def at(px, ppy):
            if not (0 <= px < self.width and 0 <= ppy < 2 * self.height):
                return None
            pair = half_pair(self.cells[ppy // 2][px], self.ice)
            return pair[ppy % 2] if pair else None

        target = at(x, py)
        if target is None:
            return
        seen, todo, region = {(x, py)}, [(x, py)], []
        while todo:
            px, ppy = todo.pop()
            region.append((px, ppy))
            for n in ((px - 1, ppy), (px + 1, ppy), (px, ppy - 1), (px, ppy + 1)):
                if n not in seen and at(*n) == target:
                    seen.add(n)
                    todo.append(n)
        self.plot(region, colour)

    def ans(self):
        out, last = [], None
        enc = lambda t: t.encode("ascii")
        for y, row in enumerate(self.cells):
            for ch, fg, bg, blink in row:
                blink = bg >= 8 or (blink and not self.ice)
                if (fg, bg, blink) != last:
                    codes = ["0"]
                    if fg >= 8:
                        codes.append("1")
                    if blink:
                        codes.append("5")
                    codes += [str(30 + SGR[fg & 7]), str(40 + SGR[bg & 7])]
                    out.append(enc(ESC + ";".join(codes) + "m"))
                    last = (fg, bg, blink)
                out.append(cp437(ch))
            if self.width < 80 or y == self.height - 1:
                out.append(enc(ESC + "0m\r\n"))
                last = None
        return b"".join(out)

    def save(self, path, title="", author="funkpower", date="20261102", ice=None):
        ice = self.ice if ice is None else ice
        body = self.ans()
        sauce = b"SAUCE00"
        sauce += title.encode("cp437")[:35].ljust(35, b" ")
        sauce += author.encode("cp437")[:20].ljust(20, b" ")
        sauce += b"".ljust(20, b" ")  # group
        sauce += date.encode("ascii")[:8].ljust(8, b" ")
        sauce += struct.pack("<IBBHHHHBB", len(body), 1, 1, self.width, self.height, 0, 0, 0, 1 if ice else 0)
        sauce += b"IBM VGA".ljust(22, b"\0")
        assert len(sauce) == 128
        with open(path, "wb") as f:
            f.write(body + b"\x1a" + sauce)
