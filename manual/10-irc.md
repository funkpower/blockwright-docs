Title: IRC: byte budget, row meter, IRC view, export
Checked: Blockwright 0.1.0 (c44974c)

# IRC: byte budget, row meter, IRC view, export

A piece goes to an IRC channel as text: one message per row, its colours as mIRC colour codes. A message has a fixed size, so every row has to fit in a byte budget, and IRC drops the blank rows and trailing black that an `.ans` keeps. This page covers the budget, the row meter beside the canvas that measures each row against it, the three ways to make rows fit or keep their shape (Fit, Pad, Swap Shades), the IRC View dock that shows the piece as a client will, and **File > Export IRC Text...**, which writes the lines. The same encoder is in `blockwright-cli export --irc` and `render --irc`.

## The byte budget

IRC carries a message in at most 512 bytes. A server relays a line to the channel as

```
:nick!user@host PRIVMSG #channel :text
```

followed by CR LF, so the text gets 512 bytes less the rest: 498 bytes less the sender's mask (`nick!user@host` as the server shows it) and the channel's name. Bytes past that are lost. The budget is the bytes a row's line may take.

The one preset is **EFnet / WeeChat, 407 bytes**: the room left on EFnet when a line is sent through WeeChat. It is every document's budget until it is changed.

Set the budget with **View > IRC > Budget...**. The IRC Budget dialog has:

| Field | What it does |
|---|---|
| Preset | `EFnet / WeeChat (407 bytes)` or `Custom`. Picking the preset sets the bytes to 407 |
| Budget | The bytes a line may take, 1 to 512. A number other than the preset's makes it Custom |
| Mask, Channel | Your `nick!user@host` and the channel. With both filled in the budget is worked out as 498 less their lengths, and the preset becomes Custom. While either is empty or holds a space, the budget isn't worked out and stays as it was, with no message |

The budget belongs to the document. Changing it is a step on the undo stack, and a project saves it (its profile, `efnet-weechat` or `custom`, and the bytes). An `.ans` has nowhere to keep it: a document whose budget has been changed is one an `.ans` doesn't hold whole (see [File formats](13-file-formats.md#saving-a-project-as-a-flat-file)).

## The row meter

The row meter is a column right of the canvas, one bar beside each row. It scrolls and zooms with the canvas. Turn it off and on with **View > IRC > Row Meter**; it starts on.

Each bar is as long as the row's share of the budget, full when the row is over it, and shows the row's size in bytes when the row is tall enough on screen to hold the number. Its colour gives the row's state:

| Colour | The row |
|---|---|
| Grey | Fits the budget |
| Amber | Fits because Fit merged some of its colours |
| Red | Is over the budget |

Hover over a bar for the row's figures, counted from row 0:

```
Row 4: 476 of 407 bytes, over by 69
Row 4: 404 of 407 bytes, 18 cell(s) merged to fit
```

The meter measures each row as the export writes it, with the window's Fit, Pad and Swap Shades settings and the document's iCE colours (with iCE off a bright background is saved as blink on the dark colour, which IRC shows dark). It counts what the canvas shows, every visible layer, and a tool's edit still in progress: a floating selection or a drag shows in the meter before it lands.

## Making rows fit

Three settings in **View > IRC** change how rows are encoded. They are the window's, start off each time Blockwright starts, and aren't saved with a document. The meter and Export IRC Text use them; the IRC View dock doesn't (see [The IRC View dock](#the-irc-view-dock)).

| Setting | What it does |
|---|---|
| Fit Lines to the Budget | Merge the least visible colours in a line over the budget until it fits |
| Pad Lines | Keep blank rows and trailing black, so clients that trim spaces keep the shape |
| Swap Shades | Draw ░ as ▓ with the colours swapped, and ▓ as ░, where it saves bytes |

**Fit** works on a row over the budget, one cell at a time. A solid cell takes its left neighbour's colour; a half block or shade takes one of its own two colours or one of its neighbour's. The cheapest change goes first, by how far the colour moves times the area that changes, until the row fits. Then every change the row can do without is put back, the most visible first. A cell fit changes only ever shows colours it showed before or colours its left neighbour shows. Letters, digits and other glyphs that aren't a blank, a block, a half block or a shade are never changed. A row that fits is left alone, and so is one no merging can make fit.

**Pad** keeps what IRC would drop. Without it the encoder leaves off the black spaces at the end of each row (a client shows its own background there), and the export leaves off the blank rows above and below the art. With it each row keeps its trailing black and ends on a black-on-black █, which a client can't trim, and the blank rows are kept too.

**Swap Shades** lets the encoder draw a shade as its opposite with the colours reversed (░ as ▓, ▓ as ░, ▒ as ▒) when that is shorter. The patterns of the two differ a little, so it is a choice, not the default.

## The IRC View dock

The IRC View dock shows the piece much as a client shows it once it is sent: each row encoded, read back the way a client reads mIRC codes, and cut at the budget. It reads the canvas as drawn, without the window's Fit, Pad and Swap Shades and without the document's iCE setting (see below). Open it with **View > IRC > IRC View** or **Window > IRC View**. It starts on the right, tabbed with the Lint dock.

What it shows:

- the colours in the mIRC palette, the 16 palette colours as the mIRC colours of the same name;
- what IRC drops (trailing black spaces, blank rows above and below the art) in the client's own background, a dark grey (`#262626`), so it stands apart from the art's black;
- on a row over the budget, the cells past the cut in the client's background, with a red bar at the cut.

Under the picture a line counts the rows cut:

```
Every line fits 407 bytes
1 row cut at 407 bytes
2 rows cut at 407 bytes
```

The cut is the one a sending script makes. A line that fits is sent whole. A longer one the script encodes again its own way (two-digit colour codes, a space or a full block for a solid cell, whichever is shorter); if that fits it is sent whole, and otherwise the cells whose glyph ends within the budget less one byte are kept, the last byte left for a reset, and the rest are lost.

The dock redraws 250 ms after an edit, at once when the budget changes, and only while it is shown; "Updating…" shows when it has been out of date for half a second. It encodes the rows without Fit, Pad or Swap Shades, whatever the View > IRC settings are. It also ignores the document's iCE setting: with iCE colours off, a cell on a bright background shows in the dock in the bright colour (light blue as mIRC 12, say), while the row meter and Export IRC Text write it in the dark one (mIRC 2), as the saved file has it.

## Export IRC Text

**File > Export IRC Text...** writes the lines the row meter measures to a text file: the canvas as IRC lines, one message each. It is above **File > Publish to Library...**, which writes its own lines (without Fit or Pad, against the 407-byte budget).

1. Any tool's edit in progress lands first.
2. If any line is over the budget, a warning says how many and how long the longest is: "2 line(s) are over the 407-byte budget, the longest 494 bytes: a client cuts them short or drops them. Export anyway?" **Save** goes on, **Cancel** stops.
3. A file dialog asks where, starting (for a document with a file) at its name with `.txt` in its folder, filtered to `IRC text (*.txt)` or `All files (*)`.
4. The file is written, and the status bar says "Exported 6 IRC line(s) to …" for three seconds. If it can't be written, a message says "Could not write …" and why.

The file is UTF-8, each line ended by a line feed, the blank lines above and below the art left out (kept with Pad).

## How a row is encoded

The encoder writes the shortest line that draws the row:

- A colour is set with `^C` (byte 0x03) only when it changes: `^Cfg,bg` when the background changes, `^Cfg` alone when only the foreground does, unless the next glyph is a comma, which a client would read as the start of a background. Before a comma the encoder writes the background again (`^Cfg,bg`) or follows the number with `^B^B` (0x02 twice, bold on and off again), whichever is shorter, and the background when the two are the same length. `A` in white and then `,5` in light red, all on black, is `^C0,1A^C4,1,5`: `,1` and `^B^B` are both two bytes, so the background is written. On light blue, mIRC's 12, the same cells are `^C0,12A^C4^B^B,5`, as `,12` is a byte longer than `^B^B`. A colour number under 10 takes one digit unless the character after it is a digit. The palette colours map onto mIRC's numbers as below; a 24-bit colour is drawn as the nearest of mIRC's 99.
- A cell that can be drawn more than one way is drawn whichever way makes the line shortest: a solid cell as a space in its colour or a █; ▀ as ▄ with the colours swapped, and ▄ as ▀ (▌ and ▐ the same); a glyph in its own background as a solid cell. Shades are drawn as they are unless Swap Shades is on.
- A row whose last glyph is a coloured space ends with `^O` (0x0F), which resets the colours, so the client doesn't carry the background on past it.
- Black spaces at the start of a row are kept, as spaces in `^C1,1`; black spaces at the end are left off (kept with Pad, which ends the row on a black █ instead).
- A glyph is written as UTF-8. A control code (0x00-0x1F, 0x7F) is written as its CP437 glyph, a C1 control (U+0080-U+009F) as `?`.
- A transparent cell is drawn blank.

| Palette | mIRC | Palette | mIRC |
|---|---|---|---|
| 0 black | 1 | 8 dark grey | 14 |
| 1 blue | 2 | 9 light blue | 12 |
| 2 green | 3 | 10 light green | 9 |
| 3 cyan | 10 | 11 light cyan | 11 |
| 4 red | 5 | 12 light red | 4 |
| 5 magenta | 6 | 13 light magenta | 13 |
| 6 brown | 7 | 14 yellow | 8 |
| 7 grey | 15 | 15 white | 0 |

A row in one colour is cheap: the first row of the canvas below, 80 blue spaces, is `^C2,2`, 80 spaces and `^O`, 85 bytes. Every change of colour costs a code, so the cost is in rows that change colour often.

![Six rows 80 columns wide: blue; fire's ladder from red to yellow in long bands; the same ladder two cells a rung; the ladder in a scattered order; half blocks in four colours on four changing backgrounds; light green half blocks on blue](../samples/manual-irc/budget.ans "1x")

```
$ blockwright-cli export --irc budget.ans budget.txt
line  bytes
   1     85
   2    205
   3    258
   4    476  over by 69
   5    494  over by 87
   6    244
6 lines, longest 494 bytes, budget 407: 2 over
blockwright-cli: budget.ans: line 4 is 476 bytes, over the 407-byte budget by 69
blockwright-cli: budget.ans: line 5 is 494 bytes, over the 407-byte budget by 87
blockwright-cli: budget.txt: not written: lines over the budget (--allow-over-budget writes it anyway)
```

Nothing is written and the exit status is 3. Rows 2 and 3 hold the same nine rungs; row 3, which changes rung every two cells, takes 53 more bytes. Row 4 takes the rungs in a scattered order and row 5 is half blocks in four colours on four backgrounds, so both change colour at almost every cell. Row 6, light green ▄▀ on blue, comes out as `^C2,9` and ▀▄▀▄…: the same picture, drawn as blue on light green with the halves swapped.

With `--fit`:

```
$ blockwright-cli export --irc --fit budget.ans budget.txt
line  bytes
   1     85
   2    205
   3    258
   4    404  fit: 18 cells merged
   5    405  fit: 27 cells merged
   6    244
6 lines, longest 405 bytes, budget 407: 0 over
fit: 45 cells merged in 2 lines
```

A smaller budget merges more:

```
$ blockwright-cli export --irc --budget 300 --fit budget.ans budget.txt
…
   4    298  fit: 31 cells merged
   5    300  fit: 58 cells merged
   6    244
6 lines, longest 300 bytes, budget 300: 0 over
fit: 89 cells merged in 2 lines
```

Swap Shades saves bytes in the shaded rows and leaves the rest:

```
$ blockwright-cli export --irc --swap-shades budget.ans budget.txt
line  bytes
   1     85
   2    201
   3    240
   4    370
   5    494  over by 87
   6    244
6 lines, longest 494 bytes, budget 407: 1 over
blockwright-cli: budget.ans: line 5 is 494 bytes, over the 407-byte budget by 87
blockwright-cli: budget.txt: not written: lines over the budget (--allow-over-budget writes it anyway)
```

Row 5 is still over, so again nothing is written and the exit status is 3.

## Trailing black and blank rows

This canvas has a black margin round a blue panel and a black stripe across it:

![A blue panel with funkpower in yellow and on irc in white, a black stripe across its middle, in a black margin](../samples/manual-irc/edges.ans "2x")

Without Pad, the blank rows above and below are left off, each row loses the black after the panel, and the stripe, all black, is an empty line. Seven rows become five lines:

```
$ blockwright-cli export --irc edges.ans edges.txt
line  bytes
   1     39
   2     41
   3      0
   4     41
   5     39
5 lines, longest 41 bytes, budget 407: 0 over
```

The first line is `^C1,1` and two spaces (the left margin, kept), then `^C1,2` and the panel's spaces, then `^O`. A client shows the stripe and the right margin in its own background. With `--pad` every row is kept and ends on a black █:

```
$ blockwright-cli export --irc --pad edges.ans edges.txt
line  bytes
   1     38
   2     44
   3     48
   4     38
   5     48
   6     44
   7     38
7 lines, longest 48 bytes, budget 407: 0 over
```

The lint reports both as [trailing-black](11-lint.md#trailing-black) and [blank-edge-rows](11-lint.md#blank-edge-rows).

## From the command line

```
blockwright-cli export --irc [--budget N] [--fit] [--pad] [--swap-shades] [--allow-over-budget] <in> <out>
blockwright-cli render --irc [--budget N] [--scale N] [--font-width 8|9] <in> <out.png>
```

`export --irc` is Export IRC Text: `--fit`, `--pad` and `--swap-shades` are the three settings, `--budget` the budget (by default a project's own, else 407; any positive number), and `--allow-over-budget` writes the file even with lines over the budget, still listing them, with exit status 0. Without it, a line over the budget leaves the file unwritten and the exit status is 3. Its table counts lines from 1, after the blank rows above the art are left off; the meter counts canvas rows from 0.

`render --irc` draws the IRC View as a PNG and prints its status line:

```
$ blockwright-cli render --irc budget.ans view.png
IRC view: 2 rows cut at 407 bytes
$ blockwright-cli render --irc edges.ans view.png
IRC view: 0 rows cut at 407 bytes
```

As in the dock, the rows are encoded without fit, pad or swapped shades, so the rows a fit would save still show cut. And because the sending script's own encoding differs, the cut isn't simply the byte count: at `--budget 450` both of the 476- and 494-byte rows are still cut ("IRC view: 2 rows cut at 450 bytes").

See [blockwright-cli](14-cli.md#export-irc) for every option.
