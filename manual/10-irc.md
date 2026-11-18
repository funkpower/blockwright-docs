Title: IRC: byte budget, row meter, IRC view, export
Checked: Blockwright 0.1.1 (716a62e)

# IRC: byte budget, row meter, IRC view, export

A piece goes to IRC as text: one message per row, coloured with mIRC codes. Every row must fit a byte budget, and IRC drops the blank rows and trailing black an `.ans` keeps. The same encoder is in `blockwright-cli export --irc` and `render --irc`.

## The byte budget

IRC carries a message in at most 512 bytes. A server relays a line to the channel as

```
:nick!user@host PRIVMSG #channel :text
```

followed by CR LF. The text gets 498 bytes less the sender's mask (`nick!user@host` as the server shows it) and the channel's name, and bytes past that are lost. The budget is the bytes a row's line may take.

The one preset is **EFnet / WeeChat, 407 bytes**: the room left on EFnet when a line is sent through WeeChat. New documents and opened flat files start with it; a project opens with the budget it was saved with.

Set the budget with **View > IRC > Budget...** (no shortcut):

| Field | What it does |
|---|---|
| Preset | `EFnet / WeeChat (407 bytes)` or `Custom`. Picking the preset sets the bytes to 407 |
| Budget | The bytes a line may take, 1 to 512. A number other than the preset's makes it Custom |
| Mask, Channel | Your `nick!user@host` and the channel. With both filled in, the budget is 498 less their lengths, and the preset becomes Custom. While either is empty, holds a space, or leaves no room for text, the budget stays as it was |

The budget belongs to the document, and changing it is one undo step. A project saves it (its profile, `efnet-weechat` or `custom`, and the bytes). An `.ans` can't keep a changed budget ([File formats](13-file-formats.md#saving-a-project-as-a-flat-file)).

## The row meter

The row meter is a column right of the canvas, one bar beside each row, scrolling and zooming with it. **View > IRC > Row Meter** (no shortcut) turns it off and on; it starts on. Under the Micron target the meter is hidden whatever the setting, as a page has no byte budget; **Row Meter** keeps its tick, and the meter comes back under the ANSI or IRC target. A project keeps its IRC budget under every target.

Each bar's length is the row's share of the budget, full when the row is over it. When the row is tall enough on screen, the bar shows the row's bytes as sent. Its colour gives the row's state:

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

The first is row 3 of the canvas under [How a row is encoded](#how-a-row-is-encoded), the second the same row with Fit on.

The meter measures each row as Export IRC Text writes it, with the window's Fit, Pad and Swap Shades and the document's iCE colours. With iCE off, a bright background is saved as blink on the dark colour, which IRC shows dark. Under the IRC target, an RGB background (an mIRC colour past 15) is sent as it is.

What counts against the budget is the line as WeeChat's ascii script sends it. The script writes the line again its own way, so a line can be longer sent than written, and a line over the budget can be shorter ([The IRC View dock](#the-irc-view-dock)). The meter counts every visible layer and a tool's edit still in progress, such as a floating selection or a drag.

## Making rows fit

Three settings in **View > IRC** change how rows are encoded. They belong to the window, start off each time Blockwright starts, and aren't saved with a document. The meter, the IRC View dock and Export IRC Text use them.

No **View > IRC** action has a shortcut by default. Set one on the **Shortcuts** tab of **Edit > Preferences...** (on macOS, in the application menu).

| Setting | What it does |
|---|---|
| Fit Lines to the Budget | Merge the least visible colours in a line over the budget so that it fits; a line merging can't fit is left as it was |
| Pad Lines | Keep blank rows and trailing black, so clients that trim spaces keep the shape |
| Swap Shades | Draw ░ as ▓ with the colours swapped, and ▓ as ░, where it saves bytes |

Fit, Pad and trimming work on the visible layers combined ([How the layers combine](07-layers.md#how-the-layers-combine)), each cell as IRC text writes it:

- An uncovered cell is a space, grey on black, with no bold, italic or underline.
- A NUL is a space; a lone control code (0x01–0x1F, 0x7F) is its CP437 glyph.
- A cell written as `?` ([How a row is encoded](#how-a-row-is-encoded)) is a `?`; a wide glyph written as `?` and a space is those two cells.
- A wide glyph with no continuation, such as `日` alone, is one cell.

**Fit** works on a row over the budget as sent. It changes only cells with a glyph of one code point that is a space or no-break space, a `█`, a glyph whose foreground and background are the same, or one of `▀▄▌▐░▒▓`.

A solid cell takes its left neighbour's colour; a half block or shade takes one of its own two colours or one of its neighbour's. A cell only ever shows colours it or its left neighbour showed before.

Fit makes the least visible changes first until the row fits, then undoes any it can do without. A row that fits is left alone, and so is one merging can't bring within the budget: a row of 80 `★` on black, light red and red by turns, is 402 bytes written and 483 sent, and Fit can change none of its cells. Fit never changes:

- any other glyph in two colours, such as a letter, or a `★` light red on black;
- a cell with bold, italic or underline;
- a letter with a combining mark (`q` + U+0301), even one red on red;
- either cell of a wide glyph followed by its continuation and written whole, such as `日`.

**Pad** keeps what IRC would drop. Without it, the encoder leaves off the spaces on black, not underlined, at the end of each row (NULs and uncovered cells too, but not a no-break space), and a client shows its own background there. The export also leaves off the empty rows above and below the art.

With Pad, those rows and cells are kept. If a row's last cell shows black alone, Pad writes it as a `█` with a black foreground (mIRC 1) and no background code, which a client can't trim; its background is whatever the row set before it, or the client's own. `A` white on blue and then a black `█` on blue are `^C0,2A^C1█`.

A cell shows black alone when it has no bold, italic or underline and is one of these:

- a space, a NUL or a no-break space on black;
- a black `█` on any background;
- any other glyph of one code point, black on black, a control code's glyph among them;
- an uncovered cell.

Any other last cell is encoded as usual. A coloured `█` can still be a space in its colour (`A` grey on red, then a red `█` on red, is `^C15,5A ^O`).

An underlined space at the end of a row, light red on black, is kept with or without Pad, as `^C4,1^_ ^O` (7 bytes written, 9 sent). A transparent cell of a Cells layer there adds nothing: if the other layers leave the cell uncovered or a plain space, grey on black, it is left off without Pad and is `^C1█` with Pad (5 written, 6 sent).

**Swap Shades** draws a shade as its opposite with the colours reversed (░ as ▓, ▓ as ░, ▒ as ▒) when that is shorter.

## The IRC View dock

The IRC View dock shows the piece as a client shows it once sent: each row encoded as Export IRC Text writes it, read back as a client reads mIRC codes, and cut at the budget. Open it with **View > IRC > IRC View** or **Window > IRC View** (no shortcut). It starts on the right, tabbed with the Lint dock.

It shows:

- the colours in the mIRC palette, the 16 palette colours as the mIRC colours of the same name;
- what IRC drops ([Making rows fit](#making-rows-fit)) in the client's own background, a dark grey (`#262626`);
- on a row over the budget, the cells past the cut in the client's background, with a red bar at the cut.

Under the picture a line counts the rows cut:

```
Every line fits 407 bytes
1 row cut at 407 bytes
2 rows cut at 407 bytes
```

The cut is the one WeeChat's ascii script makes. The script reads each line back into cells and rewrites it with every colour number in two digits, so a line can be longer sent than written. The first row of the canvas under [How a row is encoded](#how-a-row-is-encoded) is 85 bytes written and 87 sent.

A line that fits as sent is sent whole. A longer one the script encodes again more tightly (a space or a full block for a solid cell, whichever is shorter) and sends whole if that fits. Otherwise it keeps the cells whose glyph ends within the budget less one byte, the last byte left for a reset, and the rest are lost.

- The script skips the tighter encoding when a cell is bold, italic or underlined, or the line reads back as more than 2,000 cells.
- The tighter encoding can be shorter than the line as written. With Pad on and a budget of 9, a row of `1` and a space, both grey on black, is 12 bytes written; the script's first writing is 13, so it encodes again and sends 9. Make the `1` bold and the row is 13 bytes written and 15 sent, at any budget, and a budget of 9 cuts it.

The dock redraws 250 ms after an edit, an open, or a change of iCE colours or target, and at once when the budget or **View > IRC > Fit Lines to the Budget**, **Pad Lines** or **Swap Shades** changes. It shows "Updating…" when it has been out of date for half a second. Unlike the row meter, it shows a tool's edit only once it lands.

The dock follows the canvas when it scrolls, zooms or changes size. Scrolled by hand, it stays put until the canvas next moves. A lone wide glyph such as `日` takes two columns in the dock, so the rest of its row there is one column off from the canvas.

## Export IRC Text

**File > Export IRC Text...** (no shortcut) writes the lines the row meter measures to a text file, one message each.

1. Any tool's edit in progress lands first. A floating selection that can't land ([A float that can't land](05-selections.md#a-float-that-cant-land)) stops the export, and the status bar says "Not exported: the floating selection can't land: …" for five seconds.
2. If any line is over the budget as sent, a warning says how many and how long the longest is: "2 lines are over the 407-byte budget, the longest 602 bytes as WeeChat's ascii script sends them: the script cuts them short. Export anyway?" (for one line, "1 line is over the 407-byte budget, at … bytes as WeeChat's ascii script sends it: the script cuts it short."). **Save** goes on; **Cancel**, the default, stops.
3. If any cell would be written as `?` ([How a row is encoded](#how-a-row-is-encoded)), a second warning starts "Before exporting IRC text:", lists them, and asks "Export anyway?" with the same buttons. The encoder's other substitutions don't warn.
4. A file dialog asks where, starting (for a document with a file) at its name with `.txt` in its folder, filtered to `IRC text (*.txt)` or `All files (*)`.
5. The status bar says "Exported 6 IRC lines to …" for three seconds. If the file can't be written, a message says "Could not write …" and why.

The file is UTF-8, each line ended by a line feed. The blank lines above and below the art are left out unless Pad is on.

## 99 colours or 16

IRC text can name 99 colours with `^C` and a number. The IRC formatting spec (the page `modern.ircdocs.horse/formatting`) gives 0 to 15 as the colours every client knows and 16 to 98 as extended colours with fixed RGB values, and says 99 means the client's default foreground or background and is not universally supported. It adds that the RGB a client shows for 16 to 98 depends on its author, and that terminal clients often take it from the terminal's colour scheme.

Blockwright sends mIRC 0 to 98 by default. **Format > Target > IRC in 16 Colours** ([what the mode does](09-colour.md#irc-in-16-colours)) sends only 0 to 15, each other colour as the nearest of them. Nothing is lost for a document in 0 to 15: both modes write the same bytes.

What a client shows for 16 to 98, as read from each client's source at the version named. None of these clients was run for this page.

| Client | Version | 0 to 15 | 16 to 98 | 99 | Source |
|---|---|---|---|---|---|
| WeeChat | 4.10.4 | its colour names for the 16, which `irc.color.mirc_remap` can change | the nearest terminal 256-colour number (16 is 52, 98 is 231), so near mIRC's RGB, not exact; the remap setting doesn't apply to them | the default colour | `src/plugins/irc/irc-color.c`, table `irc_color_to_weechat`; its user guide, `weechat.org/files/doc/weechat/stable/weechat_user.en.html` |
| irssi | 1.4.5 | the terminal's 16 colours | the nearest terminal 256-colour number; with the setting `colors_ansi_24bit` on, the exact RGB | ignored, as a reset | `src/fe-text/gui-printtext.c`, tables `mirc_colors` and `mirc_colors24` |
| HexChat | 2.16.2 | its palette entries 0 to 15 | not mIRC's RGB: 16 to 31 repeat the colours 0 to 15, and numbers 32 to 41 reach palette entries that are not mIRC colours (the text mark, foreground, background and marker-line colours among them), and numbers past 41 wrap modulo 32 | its foreground | `src/fe-gtk/xtext.c` and `xtext.h` (`XTEXT_MIRC_COLS`, `XTEXT_MAX_COLOR`), `src/fe-gtk/palette.c` |
| mIRC | | not checked | not checked | not checked | |

Two client settings also change what arrives: WeeChat's `irc.network.colors_receive` set to `off` drops every colour.

So 16 to 98 show as mIRC's RGB only in a client that maps them, and then as a near colour unless it has a 24-bit mode. To be read the same everywhere, draw in 0 to 15 and switch **IRC in 16 Colours** on. [Lint](11-lint.md#irc-fold) lists the cells the fold changes.

## How a row is encoded

The encoder tries the ways each cell can be drawn and writes the line shortest as WeeChat's ascii script sends it ([The IRC View dock](#the-irc-view-dock)), then shortest as written. The script writes every colour number in two digits and no colour code in front of a plain space on a background already set, so the shortest line written can be longer sent.

Two kinds of row are written shortest as written instead:

- a row with a cluster (a glyph of more than one code point), a lone code point the script may join to the cell before it, or a control character, which the encoder measures once written;
- a row whose line shortest as sent could send more than the line shortest as written at some other budget.

In every row:

- A colour is set with `^C` (byte 0x03) only when it changes: `^Cfg,bg` when the background changes, `^Cfg` when only the foreground does.
- Before a comma, which a client would read as a background, the encoder writes the background again or follows the number with `^B^B` (0x02 twice), whichever is shorter, and the background on a tie. `A` white and `,5` light red, on black, is `^C0,1A^C4,1,5`. On light blue, mIRC's 12, it is `^C0,12A^C4^B^B,5`.
- A colour number under 10 takes one digit unless a digit follows it. The palette colours map onto mIRC's numbers as below, by index: a document's own palette (an XBIN's, say) changes no code, and the IRC view draws mIRC's colours. A 24-bit colour is drawn as the nearest of mIRC's 99, so under the IRC target mIRC 16 to 98 are written as their own numbers, except 52 as 4, 54 as 8, 58 as 11, 62 as 13, 88 as 1 and 98 as 0 (the same colours). With **IRC in 16 Colours** on, a colour past 15 is written as the nearest of 0 to 15 ([IRC in 16 colours](09-colour.md#irc-in-16-colours)).
- A cell that can be drawn more than one way is drawn whichever way gives the shortest line: a solid cell as a space in its colour or a █; ▀ as ▄ with the colours swapped, and ▄ as ▀ (▌ and ▐ the same); a glyph in its own background as a solid cell. Shades are drawn as they are unless Swap Shades is on. A cell with bold, italic or underline, a wide glyph followed by its continuation and a cluster are drawn only as themselves.
- A colour code can set a colour its glyph doesn't show, such as a foreground in front of a space, when the next cell needs it. Until a row sets a foreground, the client's own is written as 99. `A` white on black, then a space grey on blue and `B` yellow on blue, are `^C0,1A^C8,2 B` (11 bytes written, 15 sent), and `A` white on black, then a █ light red on black and `B` light red on blue, are `^C0,1A^C4,2█B` (13 written, 17 sent).
- Bold, italic and underline are switched on and off with `^B`, `^]` and `^_` (0x02, 0x1D, 0x1F), after any colour code.
- A row whose last glyph written is a space ends with `^O` (0x0F), which resets the colours, so the client doesn't carry the background on past it.
- Spaces on black at the start of a row are kept: a space, grey on black, and then `A`, white on black, are `^C0,1 A` (6 bytes written, 8 sent). An underlined space keeps its line: one light red on black, then `A` grey on black, is `^C4,1^_ ^C15^_A`. Spaces on black at the end are left off unless Pad is on ([Making rows fit](#making-rows-fit)).
- A glyph is written as UTF-8. NUL is written as a space, another control code (0x01-0x1F, 0x7F) as its CP437 glyph. A C1 control (U+0080-U+009F), U+2028, U+2029 or a code point that isn't a Unicode scalar value is written as `?`, and so is a cluster holding one of them or a control code other than NUL.
- A wide glyph followed by its continuation is written whole where a UTF-8 `.ans` would write it whole, and otherwise as `?` and a space, so the row keeps its columns. `日` alone, with no continuation, is written whole, where a UTF-8 `.ans` writes `?`.
- A cell is written as the visible layers combine it ([How the layers combine](07-layers.md#how-the-layers-combine)).

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

A row in one colour is cheap: the first row below, 80 blue spaces, is `^C2,2`, 80 spaces and `^O`, 85 bytes (87 sent, as `^C02,02`). Every change of colour costs a code.

![Six rows 80 columns wide: blue; fire's ladder from red to yellow in long bands; the same ladder two cells a rung; the ladder in a scattered order; half blocks in four colours on four changing backgrounds; light green half blocks on blue](../samples/manual-irc/budget.ans "1x")

```
$ blockwright-cli export --irc budget.ans budget.txt
line  bytes   sent
   1     85     87
   2    201    207
   3    240    258
   4    476    602  over by 195
   5    494    561  over by 154
   6    244    246
6 lines, longest 494 bytes, 602 sent, budget 407: 2 over
blockwright-cli: budget.ans: line 4 is 602 bytes as WeeChat's ascii script sends it, over the 407-byte budget by 195
blockwright-cli: budget.ans: line 5 is 561 bytes as WeeChat's ascii script sends it, over the 407-byte budget by 154
blockwright-cli: budget.txt: not written: lines over the budget (--allow-over-budget writes it anyway)
```

Nothing is written and the exit status is 3.

Rows 2 and 3 hold the same nine rungs, but row 3 changes rung every two cells and takes 39 more bytes as written and 51 more as sent. Rows 4 and 5 change colour at almost every cell. Row 6, light green ▄▀ on blue, comes out as `^C2,9` and ▀▄▀▄…: blue on light green with the halves swapped.

With `--fit`:

```
$ blockwright-cli export --irc --fit budget.ans budget.txt
line  bytes   sent
   1     85     87
   2    201    207
   3    240    258
   4    340    407  fit: 31 cells merged
   5    355    407  fit: 44 cells merged
   6    244    246
6 lines, longest 355 bytes, 407 sent, budget 407: 0 over
fit: 75 cells merged in 2 lines
```

A smaller budget merges more:

```
$ blockwright-cli export --irc --budget 300 --fit budget.ans budget.txt
…
   4    252    297  fit: 42 cells merged
   5    270    300  fit: 66 cells merged
   6    244    246
6 lines, longest 270 bytes, 300 sent, budget 300: 0 over
fit: 108 cells merged in 2 lines
```

Swap Shades saves bytes in rows 3 and 4 and leaves the rest as they were:

```
$ blockwright-cli export --irc --swap-shades budget.ans budget.txt
line  bytes   sent
   1     85     87
   2    201    207
   3    238    251
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

Without Pad, the blank rows above and below are left off, each row loses the black after the panel, and the stripe is an empty line. Seven rows become five lines:

```
$ blockwright-cli export --irc edges.ans edges.txt
line  bytes   sent
   1     39     41
   2     39     43
   3      0      0
   4     39     43
   5     39     41
5 lines, longest 39 bytes, 43 sent, budget 407: 0 over
```

The first line is `^C1,2`, two black █ on the blue for the left margin, the panel's 28 spaces, then `^O`. Lines 2 and 4 start `^C1,1` and two spaces. A client shows the stripe and the right margin in its own background.

With `--pad` every row is kept, and each ends on a █ with a black foreground: rows 1, 4 and 7 on the black the row set, the others on the panel's blue:

```
$ blockwright-cli export --irc --pad edges.ans edges.txt
line  bytes   sent
   1     38     40
   2     44     46
   3     46     51
   4     38     40
   5     46     51
   6     44     46
   7     38     40
7 lines, longest 46 bytes, 51 sent, budget 407: 0 over
```

The lint reports both as [trailing-black](11-lint.md#trailing-black) and [blank-edge-rows](11-lint.md#blank-edge-rows).

## Export for NomadNet

**File > Export Micron...** (no shortcut) writes the piece as a Micron page for NomadNet ([Micron page](13-file-formats.md#micron-page-mu)). Colours keep their exact RGB: mIRC's 16 to 98 as stored ([What each target does with colour](09-colour.md#what-each-target-does-with-colour)), so mIRC 16, `#470000`, is `` `FT470000 `` and mIRC 52 is `` `Ff00 ``. The 16 are written as the editor draws them, light blue as `55f`.

Bold, italic and underline are kept, and glyphs are written as IRC text writes them; a code point NomadNet drops from a page, such as a combining mark, is written as `?`. A page has no byte budget, so Fit, Pad and Swap Shades don't apply, and blank rows and trailing black stay. `blockwright-cli export --micron` writes the same page ([export --micron](14-cli.md#export-micron)). To draw for a page from the start, use the Micron target ([Drawing for NomadNet](17-nomadnet.md)).

## From the command line

```
blockwright-cli export --irc [--budget N] [--fit] [--pad] [--swap-shades] [--colours 16|99] [--allow-over-budget] <in> <out>
blockwright-cli render --irc [--budget N] [--fit] [--pad] [--swap-shades] [--colours 16|99] [--scale N] [--font-width 8|9] <in> <out.png>
```

`export --irc` is Export IRC Text:

- `--fit`, `--pad` and `--swap-shades` are the three settings.
- `--colours 16` or `99` is the colour mode: a project's own under the IRC target by default, else 99. `--colours 16` folds even a project set to the ANSI target. Anything else is refused (`--colours takes 16 or 99, not '17'`).
- `--budget` is the budget: a project's own by default, else 407. Outside 1 to 512 it is refused ("blockwright-cli: --budget takes 1 to 512 bytes", exit status 2).
- Without `--allow-over-budget`, a line over the budget as sent leaves the file unwritten, exit status 3. With it, the file is written, the lines are still listed, and the exit status is 0.

Its table gives each line's bytes as written and as sent, counting lines from 1 after the blank rows above the art; the meter counts canvas rows from 0. An `.ans` read in is UTF-8 when it has a byte order mark or is all well-formed UTF-8 with a sequence of three bytes or more, else CP437; `--encoding cp437` or `utf-8` says which.

`render --irc` draws the IRC View as a PNG and prints its status line:

```
$ blockwright-cli render --irc budget.ans view.png
IRC view: 2 rows cut at 407 bytes
$ blockwright-cli render --irc edges.ans view.png
IRC view: 0 rows cut at 407 bytes
```

`--fit`, `--pad` and `--swap-shades` work as in `export --irc`: `render --irc --fit budget.ans view.png` prints "IRC view: 0 rows cut at 407 bytes". The cut is measured as sent: at `--budget 500` the 476- and 494-byte rows are still cut ("IRC view: 2 rows cut at 500 bytes"), as they are 602 and 561 bytes sent.

See [blockwright-cli](14-cli.md#export-irc) for every option.
