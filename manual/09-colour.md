Title: Palette, iCE colours and 24-bit colour
Checked: Blockwright 0.1.1 (716a62e)

# Palette, iCE colours and 24-bit colour

A cell has a foreground and a background, each one of 16 colours or an exact RGB: one of mIRC's 16 to 98 under the IRC and Micron targets, and under the Micron target any of the 4096 colours a Micron page's three-digit codes write. iCE colours decide whether the bright eight work as backgrounds.

[What ANSI art is](../tutorials/01-what-ansi-art-is.md) introduces the 16 colours and iCE colours.

## The 16 colours

The 16 colours are those of the PC's VGA text mode, numbered 0 to 15. 8 to 15 are the bright versions of 0 to 7:

![The 16 colours in two rows of eight, numbered: 0 to 7 black, blue, green, cyan, red, magenta, brown, grey; under them 8 to 15 dark grey, light blue, light green, light cyan, light red, light magenta, yellow, white](../samples/manual-09-colour/palette.ans "2x")

| Number | Colour | RGB | Number | Colour | RGB |
|---|---|---|---|---|---|
| 0 | black | `#000000` | 8 | dark grey | `#555555` |
| 1 | blue | `#0000aa` | 9 | light blue | `#5555ff` |
| 2 | green | `#00aa00` | 10 | light green | `#55ff55` |
| 3 | cyan | `#00aaaa` | 11 | light cyan | `#55ffff` |
| 4 | red | `#aa0000` | 12 | light red | `#ff5555` |
| 5 | magenta | `#aa00aa` | 13 | light magenta | `#ff55ff` |
| 6 | brown | `#aa5500` | 14 | yellow | `#ffff55` |
| 7 | grey | `#aaaaaa` | 15 | white | `#ffffff` |

The Palette dock, the **Colours** menu and `blockwright-cli` use the PC's order. ANSI escape codes number the first eight differently (`31` is red, `34` is blue); Blockwright converts when it reads and writes `.ans` files.

## What each target does with colour

The target ([Format > Target](10-irc.md)) decides how many colours the document is sent in. The cells themselves hold the same colours under every target.

| Target | Sent as |
|---|---|
| ANSI | The 16. A cell in another colour is saved as the nearest of the 16. |
| IRC | mIRC's 99 by default: 0 to 15 as the palette, 16 to 98 as exact RGB. **IRC in 16 Colours** (below) sends only 0 to 15. |
| Micron | The RGB of each cell ([Export for NomadNet](10-irc.md#export-for-nomadnet)). |

A cell holds a colour as one of the 16, or as an exact RGB, which includes mIRC's 16 to 98 (under the IRC and Micron targets) and a Micron page's 4096. mIRC's 99 is no colour of a cell: it means the client's own colour, and the encoder writes it only for a row's foreground that nothing has set ([IRC](10-irc.md#how-a-row-is-encoded)). Cells keep their mIRC colours under the ANSI target.

Changing the target is one undo step, `Target`, and changes no cell: cells keep their colours under any target.

### IRC in 16 colours

**Format > Target > IRC in 16 Colours** is a checkbox, enabled only under the IRC target. It makes IRC text carry only mIRC's 0 to 15. Each colour past 15 is sent as the nearest of 0 to 15, by squared RGB distance, a tie going to the lower number. The six of 16 to 98 that share an RGB with one of 0 to 15 (52, 54, 58, 62, 88 and 98) fold to 4, 8, 11, 13, 1 and 0. A cell in 0 to 15 is sent unchanged, so a document that uses only those exports the same bytes in both modes.

The mode is a setting of the document, stored with it ([The project file](13-file-formats.md#projects-bwp)). It rewrites no cell: switch it off again and the 99-colour text is back. Under the ANSI and Micron targets it does nothing, and the setting is kept. Switching it is one undo step, **IRC Colours**. The status bar's target label reads `IRC 16` while it is on ([The window](02-the-window.md)).

Export IRC Text, the row meter, the IRC View dock, `export --irc` and `render --irc` all send the folded colours, so they agree. [Lint](11-lint.md#irc-fold) counts what the fold changes.

Which mode to pick, and what clients show for 16 to 98, is on [IRC](10-irc.md#99-colours-or-16).

### Saving to a file

An `.ans`, XBIN or BIN file holds only the 16. Saving another colour to one, under any target, writes the nearest of the 16 and warns: `3 cells are in colours the file can't hold, saved as the nearest of the 16` (`1 cell is in a colour …` for one). A project keeps them.

## The Palette dock

The **Palette** dock is on the right of the window and can't be closed. It shows the pen on the left and the 16 colours in two rows of eight, 0 to 7 on top.

Under the IRC and Micron targets, mIRC's 16 to 98 follow under the pen in smaller swatches, in rows of 12; the greys 88 to 98 make their own row. Under IRC with **IRC in 16 Colours** on they are left out: the dock shows the 16 only, and an RGB pen shows as the swatch it is sent as. Below them, **B**, **I** and **U** turn bold, italic and underline on and off for the pen (the glyph brush writes them as `^B`, `^]` and `^_`).

- **Left click** a colour for the pen's foreground, **right click** for the background.
- **Under the Micron target, left click** the pen's foreground or background square to open the [Micron colour dialog](#the-micron-colour-dialog) for it. Its tooltip names the colour: `The foreground colour #aaaaaa: click to pick another` for the starting pen.
- **The pen** is two overlapping squares: the foreground top-left over the background bottom-right.
- **The bent arrow** at the pen's top-right swaps the foreground and the background (**Colours > Swap Colours**).
- **The small grey-over-black squares** at the pen's bottom-left set the pen back to grey on black (**Colours > Default Colours**, <kbd>Ctrl</kbd>+<kbd>D</kbd>).

An mIRC swatch's tooltip names it and its RGB, such as `mIRC 16 (#470000)`.

The pen's keys and the eyedropper are on [Keyboard mode, F-key glyph sets and the pen](03-keyboard-mode.md#the-pen).

## The Micron colour dialog

Under the Micron target, **Colours > Pick Foreground Colour...** and **Colours > Pick Background Colour...** (no shortcuts), or a left click on the pen's foreground or background square, open a dialog titled **Foreground Colour** or **Background Colour**. The two menu items are greyed out under the other targets.

| Part | What it does |
|---|---|
| **Red**, **Green**, **Blue** | A slider and a box for each channel, one hex digit, `0` to `F` |
| **Code** | The three digits together, such as `a50`; type three to set all the channels |
| The swatch | The colour |

A digit stands for itself doubled, so `a50` is `#aa5500`: the dialog offers the 4096 colours a three-digit code writes, and only those. It opens on the pen's colour, each channel at its nearest digit; one of the 16 is read as the document's palette has it.

**OK** sets the pen to the colour, as a swatch does; it adds no undo step. **OK** on the digits it opened with, or **Cancel**, leaves the pen as it was. The Palette dock marks no swatch for a colour none of them holds; **Colours > Next Foreground** and the other three step from it to the first or last swatch.

How the page writes a colour is in [What a page holds](13-file-formats.md#what-a-page-holds).

## iCE colours

Without iCE colours, a background is one of the first eight colours, and the bit that would make it bright makes the cell blink. With **iCE colours** on, that bit is a bright background: all 16 colours work as backgrounds and nothing blinks.

The eight bright backgrounds and two lines of text, with iCE colours on:

![Eight swatches numbered 8 to 15, dark grey to white, each with a heart on it, and BLACK ON YELLOW and WHITE ON LIGHT RED on bright bars](../samples/manual-09-colour/ice-on.ans "2x")

With iCE colours off, each bright background shows as its dark colour: dark grey becomes black, yellow brown, white grey. The cells blink in a viewer that blinks; Blockwright draws them without animating the blink:

![The same picture with iCE off: swatches 8 to 15 now black, blue, green, cyan, red, magenta, brown and grey, the text on brown and red bars](../samples/manual-09-colour/ice-off.ans "2x")

### Turning it on and off

- **On the start screen**, **iCE colours (16 background colours, no blink)** starts ticked.
- **File > New** makes a canvas with iCE on.
- **View > iCE Colours** turns it on or off for the open canvas, as one undo step (**iCE Colours On**, **iCE Colours Off**).

Turning iCE off changes only how the canvas shows. A bright background stays in the cell and shows dark until iCE is on again, even one picked with iCE off.

Live text layers are redrawn for the new setting in the same undo step. A text style in the Library that needs iCE colours can't be used while they are off.

### In the file

The setting is saved in the SAUCE record of every `.ans` Blockwright saves.

- **Saving with iCE on**, a bright background is written as the blink bit, which iCE viewers read as bright.
- **Saving with iCE off**, a bright background is written as its dark colour with the blink bit set, as the canvas showed it.
- **Opening a file**, Blockwright reads the setting from SAUCE. A file with no SAUCE record opens with iCE on.
- **Opening a file whose SAUCE says iCE off** but which has bright backgrounds (codes `100` to `107`, or a 256-colour or 24-bit background read as bright, below), Blockwright turns iCE on so they show. Cells that blinked lose their blink. When a cell with a glyph lost it, saving warns: `N cell(s) lost their blink when the file was opened with iCE colours, and this save doesn't put it back`, and `blockwright-cli convert` won't write the file without `--allow-lossy` ([blockwright-cli](14-cli.md)).

For an iCE-off file with one blinking `X` and a bright background, `blockwright-cli convert in.ans out.ans` prints this and exits with status 1:

```
blockwright-cli: warning: in.ans: 1 blinking cell loses its blink: bright backgrounds need iCE colours, where blink is a bright background
blockwright-cli: out.ans: not written: the conversion loses data (--allow-lossy writes it anyway)
```

A file with bright backgrounds and no blinking glyph converts without a warning, and the new file's SAUCE says iCE on.

## 24-bit and 256 colours

Files that use more than the 16 colours are read with each colour fitted to the nearest of the 16, under either target:

| In the file | Read as |
|---|---|
| `ESC[38;2;R;G;Bm`, `ESC[48;2;R;G;Bm` | A 24-bit foreground or background. |
| `ESC[1;R;G;Bt`, `ESC[0;R;G;Bt` | PabloDraw's 24-bit foreground (`1`) or background (`0`). Black, `0;0;0`, means no 24-bit colour: the colour the other codes set shows again. |
| `ESC[38;5;Nm`, `ESC[48;5;Nm` | One of xterm's 256 colours: 0 to 15 the 16 colours, 16 to 231 a 6 × 6 × 6 colour cube, 232 to 255 a ramp of greys. |
| `ESC[90m` to `ESC[97m`, `ESC[100m` to `ESC[107m` | A bright foreground or background. |

Nearest is the least squared distance in red, green and blue; a tie goes to the lower number. `ESC[38;2;200;30;30m` reads as red (4), and `ESC[48;5;21m`, xterm's pure blue, as blue (1).

An XBIN file can carry its own palette. Saving as XBIN keeps it; any other format leaves it out and warns: `the file's own palette is left out (only XBIN keeps one)`. The editor shows such a piece in the standard 16 colours.
