"""A small cell canvas that writes .ans files with SAUCE, for the docs samples.

    from ansi import Canvas
    c = Canvas(32, 8)
    c.text(1, 1, "HELLO", fg=7, bg=0)
    c.save("step.ans", title="Hello", ice=True)

Colours are palette indices 0-15 in Blockwright's (and the PC's) order: 0 black,
1 blue, 2 green, 3 cyan, 4 red, 5 magenta, 6 brown, 7 grey, then the bright
eight in the same order. Each sample's make.py builds its canvases
with this and saves them; the site build renders the .ans files.
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


class Canvas:
    def __init__(self, width, height, fg=7, bg=0):
        self.width, self.height = width, height
        self.cells = [[(" ", fg, bg) for _ in range(width)] for _ in range(height)]

    def put(self, x, y, ch, fg=7, bg=0):
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise ValueError(f"cell {x},{y} is off a {self.width}x{self.height} canvas")
        cp437(ch)
        self.cells[y][x] = (ch, fg, bg)

    def text(self, x, y, s, fg=7, bg=0):
        for i, ch in enumerate(s):
            self.put(x + i, y, ch, fg, bg)

    def fill(self, x0, y0, x1, y1, ch=" ", fg=7, bg=0):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.put(x, y, ch, fg, bg)

    def copy(self):
        c = Canvas(self.width, self.height)
        c.cells = [row[:] for row in self.cells]
        return c

    def ans(self):
        out, last = [], None
        enc = lambda t: t.encode("ascii")
        for y, row in enumerate(self.cells):
            for ch, fg, bg in row:
                if (fg, bg) != last:
                    codes = ["0"]
                    if fg >= 8:
                        codes.append("1")
                    if bg >= 8:
                        codes.append("5")
                    codes += [str(30 + SGR[fg & 7]), str(40 + SGR[bg & 7])]
                    out.append(enc(ESC + ";".join(codes) + "m"))
                    last = (fg, bg)
                out.append(cp437(ch))
            if self.width < 80 or y == self.height - 1:
                out.append(enc(ESC + "0m\r\n"))
                last = None
        return b"".join(out)

    def save(self, path, title="", author="funkpower", date="20261102", ice=True):
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
