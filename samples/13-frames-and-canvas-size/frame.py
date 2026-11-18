"""The editor's frame styles and drawFrame, for tutorial 13's pictures.

A style is a small source box cut nine ways by its insets: the corners are
copied once, the edges repeated along the sides, the middle repeated to
fill only when the style draws it. A source cell marked transparent ('.' in
the background row) is never written. Colours are palette indices 0-15.
"""

HEX = "0123456789abcdef"


class Style:
    def __init__(self, name, rows, fg, bg, inset=1, top=None, fill=False):
        self.name = name
        self.left = self.right = inset
        self.top = self.bottom = inset if top is None else top
        self.fill = fill
        # source[y][x]: (glyph, fg, bg), or None for a transparent cell
        self.source = [[None if bg[y][x] == "." else (rows[y][x], HEX.index(fg[y][x]), HEX.index(bg[y][x]))
                        for x in range(len(rows[0]))] for y in range(len(rows))]

    def minimum(self):
        return self.left + self.right, self.top + self.bottom


def _index(i, length, lead, middle, trail):
    if i < lead:
        return i
    if i >= length - trail:
        return lead + middle + (i - (length - trail))
    return lead + (i - lead) % middle


def draw_frame(style, width, height):
    """The style drawn width x height: {(x, y): (glyph, fg, bg)} for every
    cell it writes. Below the minimum it draws nothing (the Frame tool grows
    the drag to the minimum first)."""
    mw, mh = style.minimum()
    if width < mw or height < mh:
        return {}
    sw, sh = len(style.source[0]), len(style.source)
    mid_w, mid_h = sw - style.left - style.right, sh - style.top - style.bottom
    out = {}
    for y in range(height):
        sy = _index(y, height, style.top, mid_h, style.bottom)
        mid_row = style.top <= y < height - style.bottom
        for x in range(width):
            if mid_row and style.left <= x < width - style.right and not style.fill:
                continue
            cell = style.source[sy][_index(x, width, style.left, mid_w, style.right)]
            if cell is not None:
                out[(x, y)] = cell
    return out


def style_from_cells(rows, inset=1, fill=False):
    """A style from drawn cells, as Save as Frame Style makes one: a space
    on black is a hole."""
    glyphs = ["".join(ch for ch, _, _ in r) for r in rows]
    fg = ["".join(HEX[f] for _, f, _ in r) for r in rows]
    bg = ["".join("." if ch == " " and b == 0 else HEX[b] for ch, _, b in r) for r in rows]
    return Style("", glyphs, fg, bg, inset, fill=fill)


def _line(name, top, mid, bottom, fg):
    w = len(top)
    return Style(name, [top, mid, bottom], [fg * w] * 3, ["0" * w, "0" + "." * (w - 2) + "0", "0" * w])


def _hazard():
    rows, fg, bg = [], [], []
    w, h = 12, 8
    for y in range(h):
        r = f = b = ""
        for x in range(w):
            across, down = x < 2 or x >= w - 2, y < 2 or y >= h - 2
            yellow = (across and down) or (x + 2 * y) % 8 < 4
            r += "█" if (across or down) and not yellow else " "
            f += "0"
            b += "e" if across or down else "."
        rows.append(r)
        fg.append(f)
        bg.append(b)
    return Style("Hazard stripes", rows, fg, bg, 2)


def _shaded():
    rows, bg = [], []
    step = "▓▒░"
    row_depth = [0, 1, 3, 1, 0]
    for y in range(5):
        r = b = ""
        for x in range(7):
            depth = min(x, 6 - x, row_depth[y])
            r += step[depth] if depth < 3 else " "
            b += "0" if depth < 3 else "."
        rows.append(r)
        bg.append(b)
    return Style("Shaded", rows, ["bbbbbbb"] * 5, bg, 3, top=2)


# In the order the Frame tool's list gives them.
BUILT_IN = [
    _line("Single line", "┌─┐", "│ │", "└─┘", "7"),
    _line("Double line", "╔═╗", "║ ║", "╚═╝", "7"),
    _line("Double across, single down", "╒═╕", "│ │", "╘═╛", "7"),
    _line("Single across, double down", "╓─╖", "║ ║", "╙─╜", "7"),
    _line("Heavy block", "███", "█ █", "███", "f"),
    _line("Thin half-block", "▄▄▄", "▌ ▐", "▀▀▀", "b"),
    _shaded(),
    Style("Bevel", ["██▀", "█ █", "▀██"], ["fff", "f78", "f88"], ["008", "0.0", "800"]),
    _hazard(),
    _line("Dashed line", "┌── ┐", "│   │", "└── ┘", "7"),
    Style("Double-bevel button", ["▀▀▀", "▌ ▌", "▀▀▀"], ["fff", "f7f", "fff"], ["888", "878", "888"], fill=True),
]
