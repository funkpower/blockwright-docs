Title: IRC: byte budget, row meter, IRC view, export
Checked: Blockwright 0.1.0 (4916cd6)

# IRC: byte budget, row meter, IRC view, export

A piece goes to an IRC channel as text: one message per row, its colours as mIRC colour codes. A message has a fixed size, so every row has to fit in a byte budget, and IRC drops the blank rows and trailing black that an `.ans` keeps. This page covers the budget, the row meter beside the canvas that measures each row against it, the three ways to make rows fit or keep their shape (Fit, Pad, Swap Shades), the IRC View dock that shows the piece as a client will, and **File > Export IRC Text...**, which writes the lines. The same encoder is in `blockwright-cli export --irc` and `render --irc`.

## The byte budget

IRC carries a message in at most 512 bytes. A server relays a line to the channel as

```
:nick!user@host PRIVMSG #channel :text
```

followed by CR LF, so the text gets 512 bytes less the rest: 498 bytes less the sender's mask (`nick!user@host` as the server shows it) and the channel's name. Bytes past that are lost. The budget is the bytes a row's line may take.

The one preset is **EFnet / WeeChat, 407 bytes**: the room left on EFnet when a line is sent through WeeChat. A new document starts with it, and so does a flat file when it is opened; a project opens with the budget it was saved with.

Set the budget with **View > IRC > Budget...** (no shortcut). The IRC Budget dialog has:

| Field | What it does |
|---|---|
| Preset | `EFnet / WeeChat (407 bytes)` or `Custom`. Picking the preset sets the bytes to 407 |
| Budget | The bytes a line may take, 1 to 512. A number other than the preset's makes it Custom |
| Mask, Channel | Your `nick!user@host` and the channel. With both filled in the budget is worked out as 498 less their lengths, and the preset becomes Custom. While either is empty, holds a space, or leaves no room for text, the budget isn't worked out and stays as it was, with no message |

The budget belongs to the document. Changing it is a step on the undo stack, and a project saves it (its profile, `efnet-weechat` or `custom`, and the bytes). An `.ans` has nowhere to keep it: a document whose budget has been changed is one an `.ans` doesn't hold whole (see [File formats](13-file-formats.md#saving-a-project-as-a-flat-file)).

## The row meter

The row meter is a column right of the canvas, one bar beside each row. It scrolls and zooms with the canvas. Turn it off and on with **View > IRC > Row Meter** (no shortcut); it starts on.

Each bar is as long as the row's share of the budget, full when the row is over it, and shows the row's size in bytes as sent (see below) when the row is tall enough on screen to hold the number. Its colour gives the row's state:

| Colour | The row |
|---|---|
| Grey | Fits the budget |
| Amber | Fits because Fit merged some of its colours |
| Red | Is over the budget |

Hover over a bar for the row's figures, counted from row 0:

```
Row 3: 602 of 407 bytes as WeeChat's ascii script sends it, 476 as written, over by 195
Row 3: 407 of 407 bytes as WeeChat's ascii script sends it, 340 as written, 31 cells merged to fit
```

The first is row 3 of the canvas under [How a row is encoded](#how-a-row-is-encoded), the second the same row with Fit on. A row over the budget whose size as sent depends on the Unicode version of the script's Python adds a clause starting "where the script's Python has".

The meter measures each row as Export IRC Text writes it, with the window's Fit, Pad and Swap Shades settings and the document's iCE colours (with iCE off a bright background is saved as blink on the dark colour, which IRC shows dark; under the IRC target a cell whose background is an RGB colour, an mIRC colour past 15 say, is sent as it is). What counts against the budget is the line as WeeChat's ascii script sends it, which writes the line again its own way, so a line can be longer sent than written, and a line over the budget can be shorter (see [The IRC View dock](#the-irc-view-dock)). It counts what the canvas shows, every visible layer, and a tool's edit still in progress: a floating selection or a drag shows in the meter before it lands.

## Making rows fit

Three settings in **View > IRC** change how rows are encoded. No **View > IRC** action, these three included, has a shortcut by default; give one a key on the **Shortcuts** tab of **Edit > Preferences...** (which has no shortcut by default; on macOS it is in the application menu), where they are listed under **View > IRC**. They are the window's, start off each time Blockwright starts, and aren't saved with a document. The meter, the IRC View dock and Export IRC Text use them; **File > Publish to Library...** and **File > Send to WeeChat...** don't.

| Setting | What it does |
|---|---|
| Fit Lines to the Budget | Merge the least visible colours in a line over the budget so that it fits; a line merging can't fit is left as it was |
| Pad Lines | Keep blank rows and trailing black, so clients that trim spaces keep the shape |
| Swap Shades | Draw ░ as ▓ with the colours swapped, and ▓ as ░, where it saves bytes |

Fit, Pad and the trimming of a row's end work on the canvas as its visible layers combine it ([How the layers combine](07-layers.md#how-the-layers-combine)), not on any one layer's stored cells, and see each cell of it as IRC text writes it. A cell no visible layer adds anything to (a Reference layer never does) stays as it started, an uncovered cell: a space, grey on black, with no bold, italic or underline. A NUL is a space, and a control code on its own (0x01–0x1F, 0x7F) is its CP437 glyph, each in the cell's own colours and formatting. A cell written as `?` (see [How a row is encoded](#how-a-row-is-encoded)) is a `?`, and a wide glyph written as `?` and a space is those two cells. A wide glyph with no continuation after it is one cell like any other: `日` alone is a glyph of one code point, as a letter is.

**Fit** works on a row over the budget as sent, one cell at a time. The cells it may change hold a glyph of one code point, taken as above: a space (so a NUL or an uncovered cell too) or a no-break space, a `█`, any glyph whose foreground and background are the same (a control code's glyph among them), and the half blocks and shades `▀▄▌▐░▒▓`. A solid cell takes its left neighbour's colour; a half block or shade takes one of its own two colours or one of its neighbour's. The cheapest change goes first, by how far the colour moves times the area that changes, until the row fits; a cell can change up to three times, never in the same round as its neighbour. Then every change the row can do without is put back, the most visible first. A cell fit changes only ever shows colours it showed before or colours its left neighbour shows. Fit never changes:

- any other glyph in two colours, such as a letter, or a `★` light red on black;
- a cell with bold, italic or underline;
- a letter with a combining mark (`q` + U+0301), even one red on red;
- either cell of a wide glyph followed by its continuation and written whole, such as `日`.

A `日` with no continuation after it changes only when its colours are the same, as a letter does. A row that fits is left alone. A row that merging can't bring within the budget is given back as it was and stays over: a row of 80 `★` on black, light red and red by turns, is 402 bytes written and 483 sent, and Fit can change none of its cells.

**Pad** keeps what IRC would drop. Without it the encoder leaves off the cells at the end of each row that, taken as above, are a space on black and not underlined (a NUL on black and every uncovered cell among them, but not a no-break space), and a client shows its own background there; the export leaves off the rows left empty above and below the art.

With Pad those rows are kept, and each row keeps those cells. If a row's last cell, taken as above, shows black alone, Pad writes it as a `█` with a black foreground (mIRC 1) and no background code of its own, which a client can't trim; its background is whatever the row set before it, or the client's own if the row set none. `A` white on blue and then a black `█` on blue, say, are `^C0,2A^C1█`: the `█` sits on the blue set before it. A cell shows black alone when it has no bold, italic or underline and is one of these:

- a space, a NUL or a no-break space on black;
- a black `█` on any background;
- any other glyph of one code point, black on black, a control code's glyph among them.

Every uncovered cell shows black alone.

Any other last cell gets no `█` from Pad and is encoded as any cell is: a coloured `█` can still be written as a space in its colour (`A` grey on red, then a red `█` on red, is `^C15,5A ^O`), and a letter with a combining mark (`q` + U+0301), even black on black, or a wide glyph followed by its continuation and written whole, such as `日`, is written as itself. A row that ends on a wide glyph written as `?` and a space ends on that space, which takes the `█` when it shows black alone.

At the end of a row, a space underlined, light red on black, is kept with or without Pad, as `^C4,1^_ ^O` (7 bytes written, 9 sent). In a transparent cell of a Cells layer it adds nothing, and the row ends on what the other visible layers make of that cell. If none of them adds anything (the cell is uncovered), or what they make is a plain space, grey on black, the cell is left off without Pad and is `^C1█` with Pad (5 written, 6 sent).

**Swap Shades** lets the encoder draw a shade as its opposite with the colours reversed (░ as ▓, ▓ as ░, ▒ as ▒) when that is shorter. The patterns of the two differ a little, so it is a choice, not the default.

## The IRC View dock

The IRC View dock shows the piece much as a client shows it once it is sent: each row encoded as Export IRC Text writes it, with the window's Fit, Pad and Swap Shades and the document's iCE setting, read back the way a client reads mIRC codes, and cut at the budget. Open it with **View > IRC > IRC View** or **Window > IRC View** (neither has a shortcut). It starts on the right, tabbed with the Lint dock, and has its own scroll bars.

What it shows:

- the colours in the mIRC palette, the 16 palette colours as the mIRC colours of the same name;
- what IRC drops (the cells left off a row's end and the empty rows above and below the art, as [Making rows fit](#making-rows-fit) says) in the client's own background, a dark grey (`#262626`), so it stands apart from the art's black;
- on a row over the budget, the cells past the cut in the client's background, with a red bar at the cut.

Under the picture a line counts the rows cut:

```
Every line fits 407 bytes
1 row cut at 407 bytes
2 rows cut at 407 bytes
```

The cut is the one WeeChat's ascii script makes. The script reads each line back into cells and writes them again with every colour number in two digits, so a line written with a one-digit number can be longer as sent: the first row of the canvas under [How a row is encoded](#how-a-row-is-encoded) is 85 bytes written and 87 sent. A line that fits that way is sent whole. A longer one the script encodes again more tightly (a space or a full block for a solid cell, whichever is shorter), unless a cell in it is bold, italic or underlined, or it reads back as more than 2,000 cells (one per code point, less each zero-width one, such as a combining mark, that joins the one before): then the script keeps its first writing, and the tighter one isn't tried. If what it has fits it is sent whole, and otherwise the cells whose glyph ends within the budget less one byte are kept, the last byte left for a reset, and the rest are lost. The tighter encoding can be shorter than the line as written. With Pad on and a budget of 9, a row of `1` and then a space, both grey on black, is written in 12 bytes, ending on Pad's `█` in `^C1`; the script's first writing is 13 bytes, over the budget, so it encodes the line again, draws the `█` as a space on the black already set, and sends 9 bytes, counting the reset after the space. Make the `1` bold and the row is 13 bytes written and 15 sent, at any budget, and a budget of 9 cuts it.

The dock redraws 250 ms after an edit, a file opened, a change of iCE colours or a change of target, and at once when the budget changes or **View > IRC > Fit Lines to the Budget**, **Pad Lines** or **Swap Shades** is switched (none has a shortcut). Switching **View > IRC > Row Meter** doesn't redraw it. It redraws only while it is shown; a dock hidden behind the Lint tab redraws when it is brought forward. "Updating…" shows when it has been out of date for half a second. Unlike the row meter, it draws only what has landed on the canvas: a tool's edit still in progress shows once it lands.

The dock scrolls with the canvas on both axes, with no setting to turn that off: when the canvas scrolls, zooms or changes size, the dock's top row and left column become those of the cell at the top-left corner of the canvas's view (row 0 while the canvas's whole height is in view, column 0 while its whole width is), matched by cell, not by pixel, since the canvas may be zoomed and the dock is drawn at 1×, and only as far as the dock's own scroll bars go, so near the right or bottom edge it stops short. It matches cell numbers, not what they show: a wide glyph with no continuation after it, such as `日` alone, gets a continuation in the dock and pushes the rest of its row a column right, unless it is drawn as a space or a █ in its own colour or the canvas is one column wide (where it shows as `�`), so what shows at a column there can be the canvas's column to its left. Scroll the dock by hand, with its scroll bars or their right-click menu, the mouse wheel, or, after a click on the picture, the arrow keys, Page Up and Page Down, and it stays there, as far as the dock's scroll range allows, until the canvas next scrolls by any amount, zooms or changes size, when it lines up again. An edit, a redraw, and resizing, hiding or showing the dock don't line it up again, though an edit that changes the canvas's size does.

## Export IRC Text

**File > Export IRC Text...** (no shortcut) writes the lines the row meter measures to a text file: the canvas as IRC lines, one message each. It is above **File > Publish to Library...** and **File > Send to WeeChat...** (no shortcut either), which write their own lines, without Fit, Pad or Swap Shades, and hold them to the 407-byte budget whatever the document's budget is (Send to WeeChat holds only the IRC text it sends, which it sends under the IRC target or for a UTF-8 document).

1. Any tool's edit in progress lands first.
2. If any line is over the budget as sent, a warning says how many and how long the longest is: "2 lines are over the 407-byte budget, the longest 602 bytes as WeeChat's ascii script sends them: the script cuts them short. Export anyway?" (for one line, "1 line is over the 407-byte budget, at … bytes as WeeChat's ascii script sends it: the script cuts it short."). **Save** goes on, **Cancel**, the default, stops.
3. If any cell would be written as `?` (see [How a row is encoded](#how-a-row-is-encoded)), a second warning starts "Before exporting IRC text:", lists them, and asks "Export anyway?" with the same buttons. Those cells are a C1 control, U+2028, U+2029 or a code point that isn't a Unicode scalar value, a cluster holding one of them or a control code other than NUL, and a wide glyph written as `?` and a space. The encoder's other substitutions, listed there, don't warn: a cell drawn another way, NUL written as a space, and a control code on its own written as its CP437 glyph.
4. A file dialog asks where, starting (for a document with a file) at its name with `.txt` in its folder, filtered to `IRC text (*.txt)` or `All files (*)`.
5. The file is written, and the status bar says "Exported 6 IRC lines to …" ("1 IRC line" for one) for three seconds. If it can't be written, a message says "Could not write …" and why.

The file is UTF-8, each line ended by a line feed, the blank lines above and below the art left out (kept with Pad).

## How a row is encoded

The encoder searches the ways each cell can be drawn and writes the shortest line of those it tries:

- A colour is set with `^C` (byte 0x03) only when it changes: `^Cfg,bg` when the background changes, `^Cfg` alone when only the foreground does, unless the next glyph is a comma, which a client would read as the start of a background. Before a comma the encoder writes the background again (`^Cfg,bg`) or follows the number with `^B^B` (0x02 twice, bold on and off again), whichever is shorter, and the background when the two are the same length. `A` in white and then `,5` in light red, all on black, is `^C0,1A^C4,1,5`: `,1` and `^B^B` are both two bytes, so the background is written. On light blue, mIRC's 12, the same cells are `^C0,12A^C4^B^B,5`, as `,12` is a byte longer than `^B^B`. A colour number under 10 takes one digit unless the character after it is a digit. The palette colours map onto mIRC's numbers as below; a 24-bit colour is drawn as the nearest of mIRC's 99, so under the IRC target a swatch from mIRC 16 to 98 is written as its own number, except six whose colour is also a lower number's and which are written as that one: 52 as 4, 54 as 8, 58 as 11, 62 as 13, 88 as 1 and 98 as 0.
- A cell that can be drawn more than one way is drawn whichever way gives the shortest line the encoder tries: a solid cell as a space in its colour or a █; ▀ as ▄ with the colours swapped, and ▄ as ▀ (▌ and ▐ the same); a glyph in its own background as a solid cell. Shades are drawn as they are unless Swap Shades is on. A cell with bold, italic or underline, a wide glyph followed by its continuation and a cluster are drawn only as themselves; a `日` with no continuation after it is drawn as a letter is, so in its own background it can be a space or a █. Not every line is tried. Where a solid cell drawn as a space changes the background, its code has to set a foreground too, and the encoder tries only these foregrounds for that code: the one already set, the background's own number, and 1 when the one already set is 10 to 98. Until a row sets a foreground, the one already set counts as 99, the client's own colour: with iCE colours on, a space grey on light blue and then `A` white on light blue are `^C99,12 ^C0A` (10 bytes). The next cell's foreground is never tried: `A` white on black, then a space grey on blue and `B` yellow on blue, are `^C0,1A^C0,2 ^C8B` (13 bytes), though `^C0,1A^C8,2 B` (11) draws the same cells. Nor does the code in front of a `█` ever change the background, unless the cell is bold, italic or underlined or the `█` has a combining mark: a `█` light red on black, then a space grey on blue, are `^C4█^C2█` (10 bytes), though `^C4,2█ ^O` (9) draws the same cells.
- Bold, italic and underline are switched on and off with `^B`, `^]` and `^_` (0x02, 0x1D, 0x1F), after any colour code.
- A row whose last glyph written is a space ends with `^O` (0x0F), which resets the colours, so the client doesn't carry the background on past it.
- Spaces on black at the start of a row are kept, and encoded as any cell is: a space, grey on black, and then `A`, white on black, are `^C1,1 ^C0A`, and an underlined space keeps its line (one light red on black, then `A`, grey on black, is `^C4,1^_ ^C15^_A`). The cells at the end that are a space on black and not underlined are left off, each taken as [Making rows fit](#making-rows-fit) says (a NUL as a space, an uncovered cell as a grey-on-black space, a control code as its glyph). Pad keeps them, and writes a row's last cell, when it shows black alone, as a `█` with a black foreground and no background code of its own.
- A glyph is written as UTF-8. NUL is written as a space, another control code (0x01-0x1F, 0x7F) as its CP437 glyph, and a C1 control (U+0080-U+009F), U+2028, U+2029 or a code point that isn't a Unicode scalar value as `?`. A cluster is written whole, with any NUL in it as a space, unless it holds one of those or another control code, when it is written as `?` (and a space, when its continuation follows). A wide glyph followed by its continuation is written whole where a UTF-8 `.ans` would write it whole, and otherwise as `?` and a space, so the row keeps its columns. One with no continuation after it is a cell like any other: `日` alone is written whole, where a UTF-8 `.ans` writes `?`.
- A cell is written as the visible layers combine it ([How the layers combine](07-layers.md#how-the-layers-combine)); an uncovered cell, one no visible layer adds anything to, as a space, grey on black, with no bold, italic or underline.

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

A row in one colour is cheap: the first row of the canvas below, 80 blue spaces, is `^C2,2`, 80 spaces and `^O`, 85 bytes, and 87 as sent, as `^C02,02`. Every change of colour costs a code, so the cost is in rows that change colour often.

![Six rows 80 columns wide: blue; fire's ladder from red to yellow in long bands; the same ladder two cells a rung; the ladder in a scattered order; half blocks in four colours on four changing backgrounds; light green half blocks on blue](../samples/manual-irc/budget.ans "1x")

```
$ blockwright-cli export --irc budget.ans budget.txt
line  bytes   sent
   1     85     87
   2    205    213
   3    258    293
   4    476    602  over by 195
   5    494    561  over by 154
   6    244    246
6 lines, longest 494 bytes, 602 sent, budget 407: 2 over
blockwright-cli: budget.ans: line 4 is 602 bytes as WeeChat's ascii script sends it, over the 407-byte budget by 195
blockwright-cli: budget.ans: line 5 is 561 bytes as WeeChat's ascii script sends it, over the 407-byte budget by 154
blockwright-cli: budget.txt: not written: lines over the budget (--allow-over-budget writes it anyway)
```

Nothing is written and the exit status is 3. Rows 2 and 3 hold the same nine rungs; row 3, which changes rung every two cells, takes 53 more bytes as written and 80 more as sent. Row 4 takes the rungs in a scattered order and row 5 is half blocks in four colours on four backgrounds, so both change colour at almost every cell. Row 6, light green ▄▀ on blue, comes out as `^C2,9` and ▀▄▀▄…: the same picture, drawn as blue on light green with the halves swapped.

With `--fit`:

```
$ blockwright-cli export --irc --fit budget.ans budget.txt
line  bytes   sent
   1     85     87
   2    205    213
   3    258    293
   4    340    407  fit: 31 cells merged
   5    351    406  fit: 48 cells merged
   6    244    246
6 lines, longest 351 bytes, 407 sent, budget 407: 0 over
fit: 79 cells merged in 2 lines
```

A smaller budget merges more:

```
$ blockwright-cli export --irc --budget 300 --fit budget.ans budget.txt
…
   4    252    298  fit: 42 cells merged
   5    253    299  fit: 63 cells merged
   6    244    246
6 lines, longest 258 bytes, 299 sent, budget 300: 0 over
fit: 105 cells merged in 2 lines
```

Swap Shades saves bytes in the shaded rows and leaves the rest:

```
$ blockwright-cli export --irc --swap-shades budget.ans budget.txt
line  bytes   sent
   1     85     87
   2    201    207
   3    240    266
   4    370    443  over by 36
   5    494    561  over by 154
   6    244    246
6 lines, longest 494 bytes, 561 sent, budget 407: 2 over
blockwright-cli: budget.ans: line 4 is 443 bytes as WeeChat's ascii script sends it, over the 407-byte budget by 36
blockwright-cli: budget.ans: line 5 is 561 bytes as WeeChat's ascii script sends it, over the 407-byte budget by 154
blockwright-cli: budget.txt: not written: lines over the budget (--allow-over-budget writes it anyway)
```

Rows 4 and 5 are still over, so again nothing is written and the exit status is 3.

## Trailing black and blank rows

This canvas has a black margin round a blue panel and a black stripe across it:

![A blue panel with funkpower in yellow and on irc in white, a black stripe across its middle, in a black margin](../samples/manual-irc/edges.ans "2x")

Without Pad, the blank rows above and below are left off, each row loses the black after the panel, and the stripe, all black, is an empty line. Seven rows become five lines:

```
$ blockwright-cli export --irc edges.ans edges.txt
line  bytes   sent
   1     39     43
   2     41     46
   3      0      0
   4     41     46
   5     39     43
5 lines, longest 41 bytes, 46 sent, budget 407: 0 over
```

The first line is `^C1,1` and two spaces (the left margin, kept), then `^C1,2` and the panel's spaces, then `^O`. A client shows the stripe and the right margin in its own background. With `--pad` every row is kept, and as each ends in black, each ends on a █ with a black foreground: rows 1, 3, 4, 5 and 7 on the black the row set, and rows 2 and 6, which are `^C1,1`, two spaces, `^C1,2`, the panel's spaces and `██`, on the panel's blue:

```
$ blockwright-cli export --irc --pad edges.ans edges.txt
line  bytes   sent
   1     38     40
   2     44     48
   3     48     55
   4     38     40
   5     48     55
   6     44     48
   7     38     40
7 lines, longest 48 bytes, 55 sent, budget 407: 0 over
```

The lint reports both as [trailing-black](11-lint.md#trailing-black) and [blank-edge-rows](11-lint.md#blank-edge-rows).

## From the command line

```
blockwright-cli export --irc [--budget N] [--fit] [--pad] [--swap-shades] [--allow-over-budget] <in> <out>
blockwright-cli render --irc [--budget N] [--fit] [--pad] [--swap-shades] [--scale N] [--font-width 8|9] <in> <out.png>
```

`export --irc` is Export IRC Text: `--fit`, `--pad` and `--swap-shades` are the three settings, `--budget` the budget (by default a project's own, else 407; 1 to 512, and any other number is refused: "blockwright-cli: --budget takes 1 to 512 bytes", exit status 2), and `--allow-over-budget` writes the file even with lines over the budget, still listing them, with exit status 0. Without it, a line over the budget as sent leaves the file unwritten and the exit status is 3. Its table gives each line's bytes as written and as sent, and counts lines from 1, after the blank rows above the art are left off; the meter counts canvas rows from 0. An `.ans` read in can be CP437 or UTF-8: it is read as UTF-8 when it has a byte order mark or is all well-formed UTF-8 with a sequence of three bytes or more, else as CP437, and `--encoding cp437` or `utf-8` says which.

`render --irc` draws the IRC View as a PNG and prints its status line:

```
$ blockwright-cli render --irc budget.ans view.png
IRC view: 2 rows cut at 407 bytes
$ blockwright-cli render --irc edges.ans view.png
IRC view: 0 rows cut at 407 bytes
```

`--fit`, `--pad` and `--swap-shades` encode the rows as in `export --irc`: `render --irc --fit budget.ans view.png` prints "IRC view: 0 rows cut at 407 bytes". The cut is measured as the script sends a line, not as it is written: at `--budget 500` both the 476- and 494-byte rows are still cut ("IRC view: 2 rows cut at 500 bytes"), as they are 602 and 561 bytes sent.

See [blockwright-cli](14-cli.md#export-irc) for every option.
