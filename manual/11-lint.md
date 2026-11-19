Title: Lint panel and the checks it runs
Checked: Blockwright 0.1.1 (1347435)

# Lint panel and the checks it runs

The lint reads a piece as it looks at 1× and lists the faults a rule can find. The editor shows the list in the **Lint** dock; `blockwright-cli lint` prints it.

The lint doesn't judge composition, light or legibility. A clean result doesn't mean a piece is finished.

## The Lint dock

Open it from **Window > Lint**. It starts on the right, tabbed with the IRC View dock.

A list at the top picks the ramps the lint checks:

| Choice | What it checks |
|---|---|
| All named ramps | Every named ramp, with the craft pairs allowed ([Ramps and craft pairs](#ramps-and-craft-pairs)). The default |
| A ramp by name (`fire`, `sunset`, `ice`, `grass`, `steel`, `skin`, `sea`, `toxic`, `violet`, `wood`) | That ramp only, without the craft pairs |

Below it is one row per finding:

| Column | Holds |
|---|---|
| Cell | The cell the finding is at, `x,y`, counted from 0 at the top left |
| Kind | The finding's kind, as named in [The checks](#the-checks) |
| Ramp | The ramp it was found under, or `-` for noise and the checks that use no ramp |
| Message | What is wrong. Hover to read a long message |

Click a row, or select it and press Enter, to move the cell cursor to that cell.

Under the list is the same summary line the CLI prints. The dock lists at most 1000 findings; past that the summary adds "The first 1000 are listed."

The dock lints the visible layers merged, with the document's iCE setting and target ([Targets](#targets)). It lints again 250 ms after an edit, an open, or a change of format or target, while it is shown.

The dock never reports [`flat`](#flat), which needs a box that only the CLI takes.

## blockwright-cli lint

```
blockwright-cli lint [--ramp R]... [--box x0,y0,x1,y1] [--target ansi|irc|micron] [--colours 16|99] [--json] <in>
```

`<in>` is an `.ans`, `.xb` or `.bin` file, or a project, linted as its visible layers merged, with the file's own iCE setting. `--encoding` says how an `.ans` is read ([blockwright-cli](14-cli.md#what-it-reads)).

| Option | What it does |
|---|---|
| `--ramp R` | Check this ramp: a name (`fire`, `sunset`, `ice`, `grass`, `steel`, `skin`, `sea`, `toxic`, `violet`, `wood`) or palette indices 0-15 from dark to light, such as `0,8,7,15`. Repeat for several. Without it, every named ramp is checked with the craft pairs allowed |
| `--box x0,y0,x1,y1` | The subject's box, corners inclusive. Only findings touching it are reported, and [`flat`](#flat) runs inside it. A box past the right or bottom edge is cut to the canvas |
| `--target ansi|irc|micron` | Lint for an `.ans`, for IRC or for a Micron page. The default is a project's own target, or ANSI for a flat file ([Targets](#targets)) |
| `--colours 16\|99` | Lint IRC text as sent in 99 or 16 colours. The default is a project's own setting under the IRC target, else 99. `16` turns [`irc-fold`](#irc-fold) on under the IRC target, whether a project's own or `--target irc` |
| `--json` | Print the findings as JSON |

The text output is one line per finding, then a summary:

```
11,2 speckle steel cell 11,2: a speck, lighter than every neighbour
1 finding (1 speckle), noise 0.0000, iCE on
```

Each line holds the cell, kind, ramp (`-` for none) and message, sorted by row, column, then kind; a finding under two ramps is listed once, under the first. The summary counts kinds in the order of [The checks](#the-checks). A piece with nothing to report prints:

```
clean, noise 0.0000, iCE on
```

A note prints like a finding, with `note: ` before its message, but leaves the piece clean. The notes are [`ans-loss`](#ans-loss), under the IRC and Micron targets: what an `.ans` save would lose; [`irc-fold`](#irc-fold), under the IRC target in 16 colours: what the fold changes; and, under the Micron target only, [`micron-colour`](#micron-colour) and [`micron-glyph`](#micron-glyph): what a page doesn't write as the canvas holds it. A snowman under `--target irc`:

```
0,0 ans-loss - note: 1 cell holds a glyph a CP437 .ans saves as '?' (fine for IRC)
clean, 1 note (1 ans-loss), noise 0.0000, iCE on
```

The summary counts findings by kind, then notes. In the Lint dock a note's row is in italics.

With `--json` the same finding reads:

```
{"findings":[{"kind":"speckle","severity":"warning","ramp":"steel","x":11,"y":2,"x2":11,"y2":2,"message":"cell 11,2: a speck, lighter than every neighbour"}],"noise":0.0000,"ice":true}
```

- `x2,y2` is the far corner of what the finding covers (the whole canvas for `one-glyph` and `noise`), or the other cell of a wide rung, a rung skip or a flag ([`width-varies`](#width-varies)). For a single cell it repeats the cell.
- `severity` is `"warning"` for a finding and `"note"` for a note.
- `ramp` is `null` for noise and the checks that use no ramp.

A piece with nothing to report gives `{"findings":[],"noise":0.0000,"ice":true}`. A piece with only notes is clean but still lists them; the snowman under `--target irc` gives:

```
{"findings":[{"kind":"ans-loss","severity":"note","ramp":null,"x":0,"y":0,"x2":0,"y2":0,"message":"1 cell holds a glyph a CP437 .ans saves as '?' (fine for IRC)"}],"noise":0.0000,"ice":true}
```

A clean piece can still list notes; to test for clean, read the exit status or look for `"severity":"warning"`.

The exit status is 0 when the piece is clean, with or without notes, and 4 when there is a finding. A bad `--ramp`, or a `--box` that isn't four numbers from 0, is a usage error, status 2, with the usage text.

```
$ blockwright-cli lint --ramp nope clean.ans
blockwright-cli: --ramp takes a ramp name (fire, sunset, ice, grass, steel, skin, sea, toxic, violet, wood) or palette indices 0-15 dark to light, not 'nope'
usage: blockwright-cli info <file> | convert [--allow-lossy] <in> <out>
…
$ blockwright-cli lint --box -1,0,3,3 clean.ans
blockwright-cli: --box takes x0,y0,x1,y1 (cells from 0, corners included), not '-1,0,3,3'
usage: blockwright-cli info <file> | convert [--allow-lossy] <in> <out>
…
```

A box that starts off the canvas is status 1:

```
$ blockwright-cli lint --box 30,30,40,40 clean.ans
blockwright-cli: the box 30,30,40,40 is off the 24x6 canvas
```

See [blockwright-cli](14-cli.md#lint) for the other commands.

## Ramps and craft pairs

A ramp is a list of palette colours, dark to light:

| Ramp | Colours, dark to light |
|---|---|
| `fire` | black, red, light red, yellow, white |
| `sunset` | black, blue, magenta, light magenta, light red, yellow |
| `ice` | black, blue, light blue, light cyan, white |
| `grass` | black, green, light green, yellow |
| `steel` | black, dark grey, grey, white |
| `skin` | black, red, brown, light red, yellow |
| `sea` | black, blue, cyan, light cyan |
| `toxic` | black, green, light green, light cyan, white |
| `violet` | black, magenta, light magenta, white |
| `wood` | black, red, brown, yellow |

Between two neighbours on a ramp, a dark A and a light B, the shading ladder has five rungs: A, B░A, B▒A, B▓A (the shade in B on A), then B. The lint reads a shade as the rung it shows, so B▓A counts as A░B.

Each solid colour is a rung and each neighbour pair adds three shades: steel runs from black (rung 0) through dark grey (4) and grey (8) to white (12). Only shade rungs are measured for width ([wide-rung](#wide-rung)).

A cell is on a ramp's ladder when it shows one of the ramp's colours flat (a space's background, a full block's foreground, a block or shade in one colour) or a ░▒▓ of two neighbours. Text, half blocks and blinking cells are off the ladder.

This canvas is clean: steel from dark grey to white, no shade rung wider than three cells.

![Steel's ladder from dark grey through grey to white in vertical bands, each shade between the solids](../samples/manual-lint/clean.ans "3x")

```
$ blockwright-cli lint clean.ans
clean, noise 0.0000, iCE on
```

The **craft pairs** are common shading steps between colours that aren't neighbours on any named ramp: black with any colour but white, and these 21 pairs:

blue–light blue, light blue–white, grey–dark grey, grey–white, red–light red, light red–yellow, red–magenta, brown–light red, grey–light red, green–light green, yellow–white, magenta–light blue, cyan–light blue, cyan–grey, magenta–dark grey, cyan–light cyan, red–yellow, brown–yellow, dark grey–light green, red–dark grey, green–dark grey.

Linting with every named ramp allows them. Naming a ramp (`--ramp` or the dock's list) checks that ramp alone, strictly. This canvas shades red to yellow through ▒, a craft pair:

![Three vertical bands: red, a yellow medium shade on red, and yellow](../samples/manual-lint/craft-pair.ans "3x")

```
$ blockwright-cli lint craft-pair.ans
clean, noise 0.0000, iCE on
```

Under fire alone, light red sits between red and yellow, so every shaded cell is a fault:

```
$ blockwright-cli lint --ramp fire craft-pair.ans
…
15,5 non-neighbour-shade fire cell 15,5: ▒ of 14 on 4, colours no ramp linted has as neighbours
48 findings (48 non-neighbour-shade), noise 0.0000, iCE on
```

## The checks

The **ladder checks** read each ramp's ladder and name the ramp; noise is one, but with ramp `-`. The **craft checks** use no ramp. The last six, [`no-cp437`](#no-cp437) to [`wasted-format`](#wasted-format), check glyphs and formatting.

### non-neighbour-shade

A ░▒▓ of two colours on a ramp that aren't neighbours on it, when no linted ramp has them as neighbours and they aren't a craft pair. The message gives the shade and its colours by palette index. A document's own palette changes no finding: the lint reads indices, and its dock runs again when the palette changes.

![A blue field with three cells of yellow medium shade on blue in the middle](../samples/manual-lint/non-neighbour-shade.ans "3x")

```
$ blockwright-cli lint non-neighbour-shade.ans
10,2 non-neighbour-shade sunset cell 10,2: ▒ of 14 on 1, colours no ramp linted has as neighbours
11,2 non-neighbour-shade sunset cell 11,2: ▒ of 14 on 1, colours no ramp linted has as neighbours
12,2 non-neighbour-shade sunset cell 12,2: ▒ of 14 on 1, colours no ramp linted has as neighbours
3 findings (3 non-neighbour-shade), noise 0.0000, iCE on
```

Yellow on blue skips three of sunset's colours. **Fix:** step through the colours between, one neighbour pair at a time (blue to magenta to light magenta …), or use a ramp where the two are neighbours.

### wide-rung

A shade rung (░▒▓) of a gradient more than 3 cells wide. Only a run of one shade with a lower rung at one end and a higher one at the other is measured, and solid rungs never are. A band has to be narrow in one direction only: the width is the run along the gradient or the longest run across it, whichever is shorter.

![Steel's ladder in vertical bands, the first shade six cells wide](../samples/manual-lint/wide-rung.ans "3x")

```
$ blockwright-cli lint wide-rung.ans
2,0 wide-rung steel cell 2,0: a rung 6 cells wide (at most 3)
2,1 wide-rung steel cell 2,1: a rung 6 cells wide (at most 3)
2,2 wide-rung steel cell 2,2: a rung 6 cells wide (at most 3)
2,3 wide-rung steel cell 2,3: a rung 6 cells wide (at most 3)
2,4 wide-rung steel cell 2,4: a rung 6 cells wide (at most 3)
2,5 wide-rung steel cell 2,5: a rung 6 cells wide (at most 3)
6 findings (6 wide-rung), noise 0.0000, iCE on
```

**Fix:** narrow the band, or add rungs so the gradient takes more steps over the same distance.

### rung-skip

A jump of more than one rung where three or more levels climb or fall together: a gradient missing its shades. An outline turning back, two planes meeting, or black against anything isn't a skip.

![Three solid bands: dark grey, grey and white, with no shades between](../samples/manual-lint/rung-skip.ans "3x")

```
$ blockwright-cli lint rung-skip.ans
7,0 rung-skip steel cell 7,0: rung 4 next to rung 8 at cell 8,0 (more than one rung apart)
15,0 rung-skip steel cell 15,0: rung 8 next to rung 12 at cell 16,0 (more than one rung apart)
7,1 rung-skip steel cell 7,1: rung 4 next to rung 8 at cell 8,1 (more than one rung apart)
15,1 rung-skip steel cell 15,1: rung 8 next to rung 12 at cell 16,1 (more than one rung apart)
7,2 rung-skip steel cell 7,2: rung 4 next to rung 8 at cell 8,2 (more than one rung apart)
15,2 rung-skip steel cell 15,2: rung 8 next to rung 12 at cell 16,2 (more than one rung apart)
6 findings (6 rung-skip), noise 0.0000, iCE on
```

**Fix:** put the missing ░▒▓ rungs between the two colours.

### speckle

A cell, with at least three ladder neighbours, lighter or darker than all of them. Black, a ramp's top colour (a glint) and dithered cells are never specks.

![A dark grey field with one grey cell in it](../samples/manual-lint/speckle.ans "3x")

```
$ blockwright-cli lint speckle.ans
11,2 speckle steel cell 11,2: a speck, lighter than every neighbour
1 finding (1 speckle), noise 0.0000, iCE on
```

**Fix:** take the cell back to its neighbours' rung, or grow it into a shape that belongs to the form.

### fallback-speck

A two-colour half block (▀ or ▄) cut into shading, whose half facing the shading is in a colour the shade holds but doesn't show. It appears where a shape cut into shading leaves a cell in the shade's hidden colour.

Each half is judged against the cell it faces, above or below, when that cell is on the ladder and isn't black. The cells just past the two ends of its run of identical half blocks decide which rungs it is judged against:

- When an end is the rung the half faces, that rung alone.
- Otherwise, when both ends are the same rung, that rung alone.
- Otherwise the faced rung and the rungs either side of it, less any more than one rung from an end on the ladder. An end at the canvas's edge (the box's, with `--box`), in black or off the ladder takes nothing away. When nothing is left, the half isn't judged.

A judged half has fallen when it shows none of those rungs' colours and one of them could fall back to it: ░ shows its background, ▓ its foreground and ▒ both, and a solid rung has nothing to fall back to. With iCE off, a shade can also fall back to the dark counterparts of its colours, which count as shown when the half block's other half is bright.

A half that isn't judged has to go on into the cell it faces, as a shape's edge goes on into the shape. The cell is flagged when it has a judged half, every judged half has fallen, and a ladder ░, ▒ or ▓ is at one of the run's ends or in a cell the half block faces.

![A light red shaded field with a light cyan block, its lower edge a row of light cyan over light red half blocks](../samples/manual-lint/fallback-speck.ans "3x")

```
$ blockwright-cli lint fallback-speck.ans
8,2 fallback-speck fire cell 8,2: a fallback speck, a half block in a colour the shading beside it doesn't show but falls back to where a pixel cuts it
9,2 fallback-speck fire cell 9,2: a fallback speck, a half block in a colour the shading beside it doesn't show but falls back to where a pixel cuts it
…
15,2 fallback-speck fire cell 15,2: a fallback speck, a half block in a colour the shading beside it doesn't show but falls back to where a pixel cuts it
8 findings (8 fallback-speck), noise 0.0000, iCE on
```

The light red bottom halves face ░ in light red on red, which shows red, and their run ends against that ░ on both sides. Light red is the colour the shade holds but doesn't show.

**Fix:** give the half facing the shade the colour the shade shows (red here), or carry the shade on into the cell.

### one-glyph

Shading that uses only one of ░▒▓, in four or more shade cells. Reported once, at the canvas's top left.

![A field of grey medium shade on dark grey](../samples/manual-lint/one-glyph.ans "3x")

```
$ blockwright-cli lint one-glyph.ans
0,0 one-glyph steel the shading uses one glyph only
1 finding (1 one-glyph), noise 0.0000, iCE on
```

**Fix:** shade through the ladder's rungs. A single shade reads as texture.

### noise

The canvas's pixel noise is over 0.02. Spaces, full blocks and half blocks are two pixels each; shade cells, text cells and a row's trailing black spaces aren't pixels. Noise is the share of non-black pixels unlike all four neighbours, counted over pixels whose four neighbours are all pixels.

It is reported at the top left; the value is in every summary. Shade specks are [`speckle`](#speckle).

![A light red field scattered with red half blocks](../samples/manual-lint/noise.ans "3x")

```
$ blockwright-cli lint noise.ans
0,0 noise - pixel noise 0.123 is over 0.020: bands, not speckle
1 finding (1 noise), noise 0.1227, iCE on
```

**Fix:** shade in bands that follow the form. Dither should step its density one way over many rows.

A deliberate pattern of single pixels, such as rows of marquee bulbs, can go over 0.02 too. If you meant it, leave it.

### lone-pixel

A single non-black pixel, lighter on a named ramp than the colour of all eight pixels around it: a one-pixel highlight.

![A red field with one light red top half pixel](../samples/manual-lint/lone-pixel.ans "3x")

```
$ blockwright-cli lint lone-pixel.ans
11,2 lone-pixel - a lone glint: one top pixel of 12 on 4 reads as a stray; a highlight wants a 2-5 px cluster
1 finding (1 lone-pixel), noise 0.0045, iCE on
```

**Fix:** make the highlight a cluster of two to five pixels, or take it out.

### gap

A one-cell break in a one-cell-thick line, the gap showing what is on either side; the line has to run at least two cells each side. Dashes (regular breaks) and breaks in a line along the canvas's edge aren't gaps. The message says whether the line runs across a row or down a column.

![A white line across a blue field, one cell missing in its middle](../samples/manual-lint/gap.ans "3x")

```
$ blockwright-cli lint gap.ans
12,2 gap - a one-cell break in a line across row 2
1 finding (1 gap), noise 0.0000, iCE on
```

**Fix:** close the gap, or make the break wide enough to read as two lines.

### merge

A text glyph whose foreground is the colour of the background it shows on, so it can't be seen.

![FUNK in white on blue, the N in blue on blue](../samples/manual-lint/merge.ans "3x")

```
$ blockwright-cli lint merge.ans
10,2 merge - the glyph is in its own background colour 1: it can't be seen
1 finding (1 merge), noise 0.0000, iCE on
```

**Fix:** give the glyph a colour that stands apart from its background.

### dotted-diagonal

A 1-pixel diagonal, at least four pixels long, whose pixels touch only at their corners. At 1× it reads as dots.

![A yellow diagonal line of half blocks stepping down a blue field](../samples/manual-lint/dotted-diagonal.ans "2x")

```
$ blockwright-cli lint dotted-diagonal.ans
4,0 dotted-diagonal - a 1 px diagonal of 10 pixels in colour 14 touching only at corners renders dotted; join it 4-connected
1 finding (1 dotted-diagonal), noise 0.0169, iCE on
```

**Fix:** join each pixel to the next along a side (4-connected), as a staircase, or make the line thicker.

### flat

Only with `--box`. An area inside the box of one look (one glyph in one pair of colours, not black), found in 4×2-cell windows and reported at 48 cells or more. The message gives its size and bounding box.

![A red rectangle in a blue field](../samples/manual-lint/flat.ans "3x")

```
$ blockwright-cli lint flat.ans
clean, noise 0.0000, iCE on
$ blockwright-cli lint --box 0,0,23,5 flat.ans
4,1 flat - a flat area of one look, 64 cells in 16x4: model the form or give it texture
1 finding (1 flat), noise 0.0000, iCE on
```

**Fix:** model the form with a ramp, or texture it. Flat fills are fine in graphic pieces and backgrounds, so give `--box` round the subject only.

### trailing-black

A row whose art ends in black before the right edge, beside a row that reaches it. IRC drops trailing black spaces, so the client's own background shows there, or across a row that is all black. Off under the Micron target ([Targets](#targets)).

![A blue field; row 2 is black from column 14 to the edge, row 3 is black all the way](../samples/manual-lint/trailing-black.ans "3x")

```
$ blockwright-cli lint trailing-black.ans
14,2 trailing-black - cells 14-23 of row 2 are black to the edge, beside rows that reach it: IRC drops them
0,3 trailing-black - row 3 is all black, beside rows that reach the edge: IRC shows it in the client's background
2 findings (2 trailing-black), noise 0.0000, iCE on
```

**Fix:** end the row with something that isn't black, or export with **View > IRC > Pad Lines** (no shortcut) on. It keeps the trailing black and writes a row's last cell, when it is a plain one-code-point glyph that shows black alone, as a `█` with a black foreground, which a client can't trim ([Making rows fit](10-irc.md#making-rows-fit)).

### blank-edge-rows

Blank rows above or below the art. IRC trims them when the piece is pasted. Off under the Micron target ([Targets](#targets)).

![A blue band across the middle of a black canvas, two blank rows above and two below](../samples/manual-lint/blank-edge-rows.ans "3x")

```
$ blockwright-cli lint blank-edge-rows.ans
0,0 blank-edge-rows - rows 0-1 above the art are blank: IRC trims them (a margin needs a black-on-black block)
0,4 blank-edge-rows - rows 4-5 below the art are blank: IRC trims them (a margin needs a black-on-black block)
2 findings (2 blank-edge-rows), noise 0.0000, iCE on
```

**Fix:** crop the canvas to the art, or put a black-on-black block in each margin row. **View > IRC > Pad Lines** (no shortcut) also keeps blank rows on export, the same way ([Making rows fit](10-irc.md#making-rows-fit)).

### no-cp437

Only under the ANSI target. A glyph a CP437 `.ans` can't save as it is. The message names the glyph and its code points, and what an `.ans` saves instead:

| The glyph | The message, for example |
|---|---|
| Has no CP437 code | `U+2603 ☃ has no CP437 code: an .ans saves it as '?'` |
| Has a CP437 code whose byte the ANSI reader acts on: ○ (0x09, TAB), ◙ (0x0A, LF), ♪ (0x0D, CR), → (0x1A, SUB), ← (0x1B, ESC) | `U+25CB ○ is CP437 0x09, which .ans reads as TAB: an .ans saves it as '?' (XBIN and BIN keep it)` |
| Takes two cells | `U+6F22 漢 takes two cells: an .ans saves it as '?' and a space` |
| Is a letter with combining marks that CP437 has no glyph for | `U+0071 U+0301 q U+0301 has no CP437 code: an .ans saves it as q, dropping U+0301` |

A letter and mark that CP437 has as one glyph (e and U+0301 is é) isn't flagged, and nor is a cell holding a control character (below U+0020, or U+007F).

For a UTF-8 `.ans` holding ○◙♪→←:

```
$ blockwright-cli lint arrows.ans
0,0 no-cp437 - U+25CB ○ is CP437 0x09, which .ans reads as TAB: an .ans saves it as '?' (XBIN and BIN keep it)
1,0 no-cp437 - U+25D9 ◙ is CP437 0x0A, which .ans reads as LF: an .ans saves it as '?' (XBIN and BIN keep it)
2,0 no-cp437 - U+266A ♪ is CP437 0x0D, which .ans reads as CR: an .ans saves it as '?' (XBIN and BIN keep it)
3,0 no-cp437 - U+2192 → is CP437 0x1A, which .ans reads as SUB: an .ans saves it as '?' (XBIN and BIN keep it)
4,0 no-cp437 - U+2190 ← is CP437 0x1B, which .ans reads as ESC: an .ans saves it as '?' (XBIN and BIN keep it)
5 findings (5 no-cp437), noise 0.0000, iCE on
```

Each is a `"severity":"warning"` in the JSON, and the exit status is 4. Under the IRC and Micron targets the check is off and the same cells make one [`ans-loss`](#ans-loss) note, so the piece is clean, status 0:

```
$ blockwright-cli lint --target irc arrows.ans
0,0 ans-loss - note: 5 cells hold glyphs a CP437 .ans saves as '?' (fine for IRC)
clean, 1 note (1 ans-loss), noise 0.0000, iCE on
```

See [File formats](13-file-formats.md#writing) for why an `.ans` can't keep those five.

**Fix:** use CP437 glyphs, keep the piece as a project (which holds any glyph), or give an IRC piece the IRC target and a page the Micron target.

### width-varies

Under every target, a glyph whose width clients and terminals count differently, shifting the rest of the line. The message names the glyph and each reason:

- Two columns wide, or zero-width, only since a Unicode version after 9.0.0. An older client draws it in one column, or gives it a column of its own.
- U+200D (zero width joiner): a grapheme-joining terminal draws the glyph and the next as one, narrower than their cells.
- U+FE0F after a one-column glyph: a grapheme-joining terminal draws it two columns wide.
- A skin tone modifier (U+1F3FB to U+1F3FF): a grapheme-joining terminal draws it inside the emoji before it.
- Two regional indicators side by side make a flag, reported once at the first, with `x2,y2` the second.

```
$ blockwright-cli lint --target irc heart.ans
0,0 width-varies - U+2764 U+FE0F ❤ U+FE0F: U+FE0F makes it two columns wide in a terminal that joins graphemes, one more than its cell
0,0 ans-loss - note: 1 cell holds a glyph a CP437 .ans saves as '?' (fine for IRC)
1 finding (1 width-varies), 1 note (1 ans-loss), noise 0.0000, iCE on
```

A newer emoji reads `U+1F970 🥰: it takes two columns here, but only since a Unicode version after 9.0.0: a client on an older table may draw it in one`.

**Fix:** use a glyph whose width doesn't vary, or take out the joiner, the U+FE0F or the modifier.

### lone-mark

Under every target, a zero-width code point, such as a combining mark, alone in a cell: a terminal draws it on the cell before or not at all. Also a two-column glyph with no continuation cell, which a terminal draws over the next cell.

```
U+0301 is zero-width in a cell of its own: a terminal draws it on the cell before it, or not at all
```

**Fix:** put the mark in the cell of the glyph it belongs to, or take it out.

### bidi-control

A bidi control (U+061C, U+200E, U+200F, U+202A to U+202E, U+2066 to U+2069) in a cell, alone or in a cluster, under every target. A UTF-8 `.ans` or IRC text writes it as it is, and a client that applies bidi reorders the rest of the line. A right-to-left override alone in a cell is a bidi control and a lone mark:

```
$ blockwright-cli lint --target irc override.ans
0,0 lone-mark - U+202E is zero-width in a cell of its own: a terminal draws it on the cell before it, or not at all
0,0 bidi-control - U+202E is a bidi control: a UTF-8 .ans or IRC text writes it as it is, and a client that applies bidi (HexChat, mIRC) reorders the rest of the line
0,0 ans-loss - note: 1 cell holds a glyph a CP437 .ans saves as '?' (fine for IRC)
2 findings (1 lone-mark, 1 bidi-control), 1 note (1 ans-loss), noise 0.0000, iCE on
```

The exit status is 4.

**Fix:** take it out.

### ans-loss

Only under the IRC and Micron targets. A note of what an `.ans` save would lose; at most one of each kind, at the first cell it counts. Under the Micron target each message ends `(fine for Micron)`:

| What is lost | The message |
|---|---|
| Glyphs: the cells [`no-cp437`](#no-cp437) would flag under the ANSI target | `5 cells hold glyphs a CP437 .ans saves as '?' (fine for IRC)` |
| Colours: cells in a colour other than the 16 | `1 cell is in a colour an .ans can't hold, saved as the nearest of the 16 (fine for IRC)` |
| Formatting: cells with bold, italic or underline | `5 cells have bold, italic or underline, which an .ans leaves out (fine for IRC)` |

With notes alone the summary starts `clean` and the exit status is 0. If the piece will also be saved as an `.ans`, lint it under the ANSI target.

### irc-fold

Only when IRC text is sent in 16 colours (**Format > Target > IRC in 16 Colours**, or `--target irc --colours 16`; [IRC in 16 colours](09-colour.md#irc-in-16-colours)). A note of what the fold to 0 to 15 changes; at most one of each kind, at the first cell it counts. The piece stays clean and the exit status is 0.

| What changes | The message |
|---|---|
| Colours: cells in an mIRC colour past 15 | `1 cell is in an mIRC colour past 15, sent as the nearest of 0-15 (IRC in 16 colours)` |
| Glyphs: cells whose foreground and background fold to the same colour | `1 cell's glyph is hidden in 16 colours: its foreground and background fold to the same colour` |

For several cells the first reads `N cells are in …` and the second `N cells' glyphs are hidden in 16 colours: their foregrounds and backgrounds fold to the same colour`. A cell in mIRC 77 on black, linted with `--colours 16`, is also an [`ans-loss`](#ans-loss) colour note:

```
0,0 ans-loss - note: 1 cell is in a colour an .ans can't hold, saved as the nearest of the 16 (fine for IRC)
0,0 irc-fold - note: 1 cell is in an mIRC colour past 15, sent as the nearest of 0-15 (IRC in 16 colours)
clean, 2 notes (1 ans-loss, 1 irc-fold), noise 0.0000, iCE on
```

**Fix:** none is needed. To see what is sent, open the IRC View dock; to keep a colour exact, send 99 colours; to avoid the fold, draw in 0 to 15.

### micron-colour

Only under the Micron target. A note of the cells whose colour Export Micron writes in the six-digit truecolour form (`` `FTrrggbb ``, `` `BTrrggbb ``) because three hex digits can't hold it, such as most of mIRC's colours 16 to 98, or an XBIN's own palette entry that isn't twelve-bit. It counts the cells whose colour shows, so a foreground on a blank cell isn't counted, and it reports one note at the first cell. The page keeps such a colour exactly and NomadNet 1.5 reads it; the note is for a page meant to keep to three-digit codes. An XBIN whose palette has a colour that isn't twelve-bit, linted under `--target micron`:

```
0,0 micron-colour - note: 2 cells are in colours three hex digits can't write: the page writes them exactly, as truecolour (`FTrrggbb or `BTrrggbb), not a twelve-bit `Frgb or `Brgb
clean, 1 note (1 micron-colour), noise 0.0000, iCE on
```

**Fix:** none is needed. To keep a page to three-digit codes, choose **Colours > Snap to Micron Colours**, which changes each RGB colour of the selection, or of the active layer when nothing is selected, to the nearest of the 4096 three digits write, as one undo step, **Snap to Micron Colours** (the steps-file action is `snapMicronColours`). It leaves an XBIN's own palette entry that isn't twelve-bit, so the note stays for it. Or redraw those cells in colours the Micron colour dialog offers ([Colours on a Micron page](09-colour.md#colours-on-a-micron-page)).

### micron-glyph

Only under the Micron target. A note of the cells a Micron page writes as `?`: a glyph whose code point NomadNet strips from a page, a wide glyph (written as `?` and a space), and a glyph IRC text can't write. One note, at the first cell. It sits beside [`ans-loss`](#ans-loss), which counts what a CP437 `.ans` would lose. A combining mark and a snowman (`a`, U+0301, `b`, a space, U+2603) under `--target micron --encoding utf-8`:

```
0,0 micron-glyph - note: 1 cell holds a glyph a Micron page writes as '?': NomadNet strips its code point from a page, or IRC text can't write it
3,0 ans-loss - note: 1 cell holds a glyph a CP437 .ans saves as '?' (fine for Micron)
clean, 2 notes (1 ans-loss, 1 micron-glyph), noise 0.0000, iCE on
```

**Fix:** use a glyph NomadNet shows. The export's warning lists the glyphs it wrote as `?` ([What a page doesn't keep](13-file-formats.md#what-a-page-doesnt-keep)).

### wasted-format

Bold, italic or underline that draws nothing, though IRC text spends a byte on each toggle; one finding per cell, under the ANSI and IRC targets ([Targets](#targets)). An attribute is wasted when the cell draws the same pixels without it at both glyph widths, 8 and 9 pixels: bold on a blank, `▀` or `█`, or underline on `█`.

Italic shears a block, so italic on `█` isn't flagged. Only glyphs in the VGA font are judged.

The formatting comes from the Palette dock's **B**, **I** and **U** toggles, which the glyph brush and typing write under the IRC and Micron targets.

For an IRC project whose first five cells are bold on a blank, underline on `█`, bold on `▀`, bold on `A` and italic on `█`:

```
$ blockwright-cli lint formatted.bwp
0,0 ans-loss - note: 5 cells have bold, italic or underline, which an .ans leaves out (fine for IRC)
0,0 wasted-format - bold on a blank draws nothing and costs bytes in IRC text
1,0 wasted-format - underline on a full block draws nothing and costs bytes in IRC text
2,0 wasted-format - bold on ▀ draws nothing and costs bytes in IRC text
3 findings (3 wasted-format), 1 note (1 ans-loss), noise 0.0000, iCE on
```

Each is a `"severity":"warning"`; the exit status is 4.

**Fix:** turn the attribute off on those cells. Export writes it, wasted or not.

## Targets

A document targets an `.ans` (ANSI), IRC, or a Micron page for NomadNet: set it with **Format > Target**. A project keeps it (`pack` and `unpack` take `--target`), `lint --target` overrides it, and a flat file is linted for ANSI unless `--target irc` or `--target micron` is given.

Under the IRC and Micron targets:

- [`no-cp437`](#no-cp437) is off, and [`ans-loss`](#ans-loss) notes say what an `.ans` save would lose instead.
- With **IRC in 16 Colours** on, [`irc-fold`](#irc-fold) notes say what the fold changes.
- A ladder check judges a cell in a colour outside the 16 by the nearest of the 16, and the message ends `(an RGB cell, judged by the nearest of the 16)`.

Under the Micron target, three checks are also off, as a page doesn't drop what IRC drops ([Drawing for NomadNet](17-nomadnet.md)):

- [`trailing-black`](#trailing-black) and [`blank-edge-rows`](#blank-edge-rows): a page keeps every row and column, black and blank ones included.
- [`wasted-format`](#wasted-format): a page has no byte budget, so a toggle that draws nothing costs nothing that matters.

[`width-varies`](#width-varies), [`lone-mark`](#lone-mark) and [`bidi-control`](#bidi-control) stay under every target: NomadNet draws in a terminal. Two notes are added, [`micron-colour`](#micron-colour) and [`micron-glyph`](#micron-glyph), for what a page doesn't write as the canvas holds it. Every other check runs as under ANSI.

The trailing-black sample and the arrows of [`no-cp437`](#no-cp437), linted for a page:

```
$ blockwright-cli lint --target micron trailing-black.ans
clean, noise 0.0000, iCE on
$ blockwright-cli lint --target micron arrows.ans
0,0 ans-loss - note: 5 cells hold glyphs a CP437 .ans saves as '?' (fine for Micron)
clean, 1 note (1 ans-loss), noise 0.0000, iCE on
```

## Where the rules come from

The rules are the ones funkpower's pieces for the IRC library are held to. The ladder rules (rungs one to three cells wide, neighbours stepped through ░ ▒ ▓ in order, no form shaded in one glyph) are the shading rules of tutorials 04 and 05.

The flat check doesn't give the share of the subject that is flat; under 15% is a good bar. `--box` counts canvas rows from the top, blank rows included. The rest (every word read at 1×, one light direction, the squint test, nothing that reads as the wrong thing) needs a reader.
