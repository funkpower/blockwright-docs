Title: blockwright-cli
Checked: Blockwright 0.1.0 (f34d296)

# blockwright-cli

`blockwright-cli` is Blockwright without the window. It converts, renders, exports, shades and lints pieces, packs and unpacks projects, and runs generator layers, so scripts can do what the editor does.

```
blockwright-cli [options] command [args...]
```

## What it reads

Every command that reads a piece takes an ANSI file (`.ans`), an XBIN (`.xb`) or a BIN (`.bin`). It also takes a project, a `.bwp` zip or a project directory, and reads it as its flattened composite: the visible layers merged as the editor shows them. Commands that write a piece (`convert`, `shade`) write XBIN to an output named `.xb`, BIN to one named `.bin`, and ANSI otherwise. `convert`, `shade`, `export --irc` and `render` refuse an output named `.bwp` (exit status 1): `pack` writes a project.

An `.ans` is read as UTF-8 when it starts with a byte order mark, or when it is all well-formed UTF-8 with a sequence of three bytes or more (the block and box glyphs terminals draw with); otherwise it is read as CP437. `--encoding auto|cp437|utf-8` says which, for `info`, `convert`, `render`, `export`, `shade`, `lint`, `pack` and `unpack`; `info` prints the one it was read as.

`convert` and `shade` write an `.ans` as CP437 unless `--output-encoding utf-8` is given. The SAUCE record stays CP437, and a UTF-8 `.ans` starts with a byte order mark only when its text has no sequence of three bytes or more, so that a reader still takes it for UTF-8. `snapshot` writes the project's own encoding, or the one `--output-encoding` gives. XBIN and BIN are CP437, so `--output-encoding utf-8` to an `.xb` or `.bin` output is a usage error. Everything else is written as CP437.

An option given to a command that doesn't take it is a usage error.

In a project format before 5.0 (the project's `manifest.json` gives the version), a cell's attributes hold only blink: bold, italic and underline came with 5.0. If any cell of a project in such a format has another attribute bit set, which no earlier build wrote, every command that reads the project clears those bits as it reads and says so on stderr, naming the file and the number of cells (`1 cell` when there is one):

```
blockwright-cli: note: old.bwp: cleared attribute bits no earlier build wrote from 2 cells
```

The command goes on as usual: its output on stdout and its exit status are the same as without the note. `replay` prints it for a project it starts from, after the steps file's name (`blockwright-cli: note: steps.json: start: old.bwp: ...`), and so does `blockwright --screenshot` (`blockwright: note: steps.json: start: old.bwp: ...`). A newer project with an attribute bit Blockwright doesn't know is refused instead (`...: cell 0 has an unknown attribute`, exit status 1).

## Commands

### info

```
blockwright-cli info <file>
```

Prints the piece's size and whether it uses iCE colours. For an `.ans` it prints the encoding it was read as (CP437 or UTF-8); for an XBIN, that it is one (and whether it is compressed), its palette (none, standard or custom) and its font; for a BIN, that it is one. Then the SAUCE record, or `none`: title, author, group, date, the file size it records and whether that matches the content, data type, file type, the four TInfo fields, the flags (iCE colours, letter spacing, aspect ratio), font and comments.

For a project it prints whether it is a zip or a directory, its size, iCE colours, encoding and target, the IRC byte budget, the layers (id, kind, size, position, mode, visibility and locks, name), the size of the notes in bytes, the snapshots, the files it carries, and its SAUCE title, author, group, date, letter spacing, aspect ratio, font and comments.

### convert

```
blockwright-cli convert [--allow-lossy] [--output-encoding cp437|utf-8] <in> <out>
```

Reads a piece and writes it as ANSI, XBIN or BIN, chosen by `<out>`'s extension. `<out>` may be `<in>`: the file is rewritten in place, which normalises it. When something can't be represented in the output, nothing is written unless `--allow-lossy` is given. `--output-encoding` writes an `.ans` as CP437 (the default) or UTF-8 (see [What it reads](#what-it-reads)).

### render

```
blockwright-cli render [--scale N] [--font-width 8|9] <in> <out.png>
blockwright-cli render --irc [--budget N] [--fit] [--pad] [--swap-shades] [--scale N] [--font-width 8|9] <in> <out.png>
```

Draws the piece as a PNG with the IBM VGA font.

| Option | What it does |
|---|---|
| `--scale N` | Integer zoom, nearest neighbour, 1 to 8 (default 1) |
| `--font-width 8|9` | Glyph width in pixels (default: the SAUCE letter spacing, else 8) |
| `--irc` | Draw the IRC view instead: the mIRC palette, without what IRC drops, each line cut at the budget. Prints how many rows were cut, as `IRC view: 0 rows cut at 407 bytes` |
| `--budget N` | With `--irc`: the bytes a line may take, 1 to 512. Default: a project's own budget, else 407 |
| `--fit`, `--pad`, `--swap-shades` | With `--irc`: as for [export --irc](#export-irc) |

`--budget`, `--fit`, `--pad` and `--swap-shades` without `--irc` are usage errors.

`render` refuses to write over its input.

### export --irc

```
blockwright-cli export --irc [--budget N] [--fit] [--pad] [--swap-shades] [--allow-over-budget] <in> <out>
```

Writes the piece as IRC text with mIRC colour codes, one line per row, and prints a table of each line's size in bytes (headed `line  bytes`), then a summary:

```
40 lines, longest 256 bytes, budget 407: 0 over
```

| Option | What it does |
|---|---|
| `--budget N` | The bytes a line may take, 1 to 512. Default: a project's own budget, else 407 (EFnet through WeeChat) |
| `--fit` | Fit lines over the budget by merging their least visible colours, and report how many cells were merged in how many lines |
| `--pad` | Keep trailing black cells and blank rows at the top and bottom, ending each row on a black block |
| `--swap-shades` | Let the encoder draw a shade as its opposite with the colours reversed when that is shorter |
| `--allow-over-budget` | Write the file even when lines are over the budget |

A line over the budget, measured as WeeChat's ascii script sends it, is reported with how far over it is. Without `--allow-over-budget` the output isn't written and the exit status is 3. Cells IRC text can't hold, such as a control character, are written as `?`, with a warning that counts them and names the first. `export --irc` refuses to write over its input.

### shade

```
blockwright-cli shade --ramp R [--darken] [--steps N] [--box x0,y0,x1,y1] [--mask <mask>] [--ice] [--allow-lossy] <in> <out>
blockwright-cli shade --form dome|cylinder|plane [--glint] --ramp R [--light P] (--box ... and/or --mask ...) <in> <out>
blockwright-cli shade --despeckle --ramp R (--box ... and/or --mask ...) <in> <out>
blockwright-cli shade --rim --ramp R [--light P] (--box ... and/or --mask ...) <in> <out>
```

Runs one pass of a shading brush over part of the piece. Without a mode it is the rung step: each cell on the ramp moves one rung lighter (or darker), and the ladder is checked afterwards. `<out>` may be `<in>`.

| Option | What it does |
|---|---|
| `--ramp R` | A named ramp (`fire`, `sunset`, `ice`, `grass`, `steel`, `skin`, `sea`, `toxic`, `violet`, `wood`) or palette indices from dark to light, such as `0,8,7,15` |
| `--darken` | Darken instead of lighten |
| `--steps N` | Rungs to move each cell, 1 to 64 (default 1) |
| `--box x0,y0,x1,y1` | The cells to work on, counted from 0, corners included (default: the whole piece) |
| `--mask <mask>` | A piece the size of the input whose non-blank cells are the selection; with `--box`, those of them inside the box |
| `--form dome|cylinder|plane` | Shade the selection as that form |
| `--glint` | With `--form`: a glint of the ramp's top rung at the brightest point |
| `--despeckle` | Clear the selection's specks |
| `--rim` | Light the selection's edge cells that face the light |
| `--light P` | With `--form` or `--rim`: where the light comes from, `N`, `NE`, `E`, `SE`, `S`, `SW`, `W` or `NW` (default `NW`) |
| `--ice` | Turn iCE colours on. Without it, a piece without iCE colours keeps them off, and no shade that needs a bright background is used |

`--form`, `--despeckle` and `--rim` need a selection: `--box`, `--mask` or both. Only one mode can be given.

### lint

```
blockwright-cli lint [--ramp R]... [--box x0,y0,x1,y1] [--target ansi|irc] [--json] <in>
```

Checks the shading ladders under each ramp, the pixel noise, and the craft rules. It prints one line per finding (cell, kind, ramp, message) and a summary:

```
62 findings (5 wide-rung, 47 rung-skip, 2 speckle, 2 fallback-speck, 1 one-glyph, 5 trailing-black), noise 0.0013, iCE on
```

`--ramp` can be given more than once; without it every named ramp is checked, and the craft pairs. `--target ansi|irc` lints for an `.ans` or for IRC (default: a project's own target, else ANSI). `--json` prints the findings as JSON instead, each with a `severity`, `"warning"` or `"note"`; a piece with only notes still lists them. A note (`ans-loss`, under the IRC target) is printed with `note: ` before its message but leaves the piece clean, so the exit status is 4 only when there is a finding other than a note. See [Lint](11-lint.md#blockwright-cli-lint).

### library

```
blockwright-cli library list [dir]
blockwright-cli library check <dir>
```

`list` prints the stamps and text styles in a library, by default the bundled library and the user's, one per line, tab-separated: kind, category, name, size, widest IRC row in bytes, `ice` when a text style needs iCE colours (else `-`), tags, path. A text style's size and bytes are those of its thumbnail sample.

`check` checks every stamp, sidecar and text style in a library directory, drawing each text style's sample.

### pack, unpack and snapshot

```
blockwright-cli pack [--allow-lossy] [--target ansi|irc] <in> <out.bwp>
blockwright-cli unpack [--allow-lossy] [--target ansi|irc] <in> <dir>
blockwright-cli snapshot [--allow-lossy] [--output-encoding cp437|utf-8] <project>
```

`pack` writes a piece or a project as a project zip. `unpack` writes one as a project directory; `<dir>` must be empty or a project already. A project can't hold an XBIN's own palette or font, so `pack` and `unpack` drop them only with `--allow-lossy`. `--target` sets the project's target, ANSI or IRC (default: a project's own, else ANSI); see [Lint](11-lint.md#the-irc-target).

`snapshot` saves the project's flattened composite as its next snapshot, `snapshots/rN.ans`, and prints `rN`. It is written in the project's own encoding unless `--output-encoding` gives one.

### Generators

```
blockwright-cli add-generator [--name NAME] [--timeout S] <project> <dir>
blockwright-cli run-generators [--layer ID]... [--timeout S] <project>
blockwright-cli import-scene [--timeout S] [--bake] [--author NAME] [--date CCYYMMDD] <scene.py> <out>
```

These run programs: a generator layer's output comes from the program its `generator.json` names.

- `add-generator` adds a generator layer on top of the project, from a directory with a `generator.json` (and a `params.json` and scripts), runs it once and saves the project. `--name` names the layer (default: the directory's name).
- `run-generators` runs the project's generator layers again, bottom first, and saves their output. `--layer` picks one layer by id (as `info` lists them); give it more than once for several.
- `import-scene` opens a Python scene as a new project with a generator layer for each of the scene's layers, run once. `<out>` is a `.bwp`, or a directory that doesn't exist or is empty. It runs the scene with `python3` (on Windows, the first of `py -3`, `python` and `python3` that is Python 3). To rebuild a project byte for byte, `--bake` writes each layer as the cells it made, without its script, so the project doesn't name the scene's path (its layers can't be run again); `--author` sets the SAUCE author (1 to 20 CP437 characters) and `--date` the SAUCE date (default: the day in UTC of `SOURCE_DATE_EPOCH` when it is set, else today).

`--timeout` is the seconds a generator may run, 1 to 3600 (default 30). If any run fails, nothing is written.

### replay

```
blockwright-cli replay [options] <steps.json> -o <dir>
```

`replay` plays a steps file: a start and a list of edits, each made through the editor's own brushes, shapes, selection and layer operations. After each step it writes the canvas, flattened and with its SAUCE, to `<dir>` as `NN-<name>.ans`, where `NN` is the step's number from `01` (with more digits in a file of 100 steps or more: `001`); a step with `"capture": "before-after"` writes `NN-<name>-before.ans` and `NN-<name>-after.ans`. `<dir>` is made if it isn't there. Nothing is written unless every step applies, and the same file writes the same bytes every run. Files already in `<dir>` stay unless this run writes one of the same name.

| Option | What it does |
|---|---|
| `-o`, `--output <dir>` | Where the files go. Required |
| `--project` | Also write each capture as `NN-<name>.bwp` |
| `--render` | Also write each capture as `NN-<name>.png` |
| `--scale N` | With `--render`: zoom 1 to 8 (default 1) |
| `--font-width 8|9` | With `--render`: glyph width (default: the SAUCE's, else 8) |
| `--allow-lossy` | Write an `.ans` that loses something; a warning says what |
| `--output-encoding cp437|utf-8` | The `.ans` files' text (default CP437) |

A steps file is JSON. In brief:

```
{"version": 1,
 "start": {"blank": [80, 25]},
 "steps": [{"name": "word", "action": "keyboard", "at": [1, 1], "text": "Hi", "fg": 14},
           {"name": "box", "action": "rectangle", "from": [0, 0], "to": [7, 5], "fg": 4}]}
```

- `"start"` is `{"file": ...}` (an `.ans`, `.xb`, `.bin` or project, relative to the steps file), `{"sample": ...}` or `{"blank": [w, h]}`. `"ice"` sets a blank start's iCE colours (default on).
- Each step has a `"name"` (1 to 64 of `a-z`, `0-9`, `-` and `_`, starting with a letter or a digit) and an `"action"`, the editor's name for it: a tool (`shade`, `halfBlock`, `line`, `keyboard`, …), a selection command (`select`, `copy`, `paste`, …) or a layer command (`newCellsLayer`, `setActiveLayer`, …). Points are cells, or, for the half-block tools (`halfBlock`, `line`, `rectangle`, `ellipse`, `fill` and `eyedropper`), pixels, two to a cell row: the example's rectangle from pixel `[0, 0]` to `[7, 5]` covers cell rows 0 to 2.
- Any step but a `view` step may also set Tool Options (`"fg"` and `"bg"` 0 to 15, `"size"`, `"ramp"`, `"symmetry"` and more), which hold for the steps after it.

`blockwright-cli replay --help` gives the whole format: every action, its keys, and every Tool Option with its range and default. A step that can't be applied (an unknown action or key, a value out of range, a point off the canvas, nothing selected to transform) stops the replay with exit status 1 and a message naming the step, such as `blockwright-cli: bad.json: step 2 (off): cell (20, 1) is off the 8 x 3 canvas`.

A steps file can also carry what only the editor's window uses ([Pictures of the window](#pictures-of-the-window)). `replay` passes over a step's `"screenshot"` and the file's `"window"`, but it has no window to set a view in, so it refuses a file with a `view` step before it reads the start or writes anything, with exit status 1:

```
blockwright-cli: v.json: step 2 (zoomed): view sets the window's zoom, scroll and IRC options, and blockwright-cli replay has no window; replay this file with blockwright --screenshot
```

### Pictures of the window

```
blockwright --screenshot <steps.json> -o <dir>
```

`--screenshot` is an option of the editor, `blockwright`, not of `blockwright-cli`. It plays the same steps file in the editor's window, offscreen, and writes a PNG for each step that has a `"screenshot"`, as `NN-<name>.png`, `NN` numbered as for `replay`. A picture taken before the step is `NN-<name>-before.png`; the one taken after is `NN-<name>-after.png` when `"when"` is `"both"` or the step has `"capture": "before-after"`. A `"screenshot"` is:

```
{"of": "window" | a dock or widget's object name,
 "crop": {"cells": [x, y, w, h]} | {"pixels": [x, y, w, h]},
 "when": "before" | "after" | "both"}
```

`"of"` is `"window"` when left out, and `"when"` is `"after"`. A crop of `"cells"` needs `"of"` to hold the canvas, with the cells in view. The file's top-level `"window": [w, h]` sizes the window, 1280 × 800 without one. A file with no step that asks for a screenshot writes no picture and exits with status 0, saying `blockwright: ok.json: no step asks for a screenshot`.

A `view` step sets what the window shows, for the pictures after it:

```
{"name": "fit-on", "action": "view", "ircFit": true}
```

| Key | Value | What it sets |
|---|---|---|
| `"zoom"` | 1 to 8 | The canvas's zoom, as **View > Zoom In** (<kbd>Ctrl</kbd>+<kbd>=</kbd>) and **View > Zoom Out** (<kbd>Ctrl</kbd>+<kbd>-</kbd>) set it ([Views](02-the-window.md#views)) |
| `"scrollTo"` | `[x, y]`, a cell | Scrolls so that cell is at the canvas view's top left, as far as the scroll bars go: at the canvas's right or bottom edge they stop short |
| `"ircFit"` | `true` or `false` | **View > IRC > Fit Lines to the Budget** (no shortcut) on or off |
| `"ircPad"` | `true` or `false` | **View > IRC > Pad Lines** (no shortcut) on or off |
| `"ircSwapShades"` | `true` or `false` | **View > IRC > Swap Shades** (no shortcut) on or off |

The three IRC settings are the ones in [Making rows fit](10-irc.md#making-rows-fit), and the row meter and the IRC View dock follow them as they do the menu. Every key is optional, but a view step needs at least one; an empty one is refused (`step 1 (empty): view needs at least one of "zoom", "scrollTo", "ircFit", "ircPad" or "ircSwapShades"`). A key left out leaves that setting as it was. A view step takes a `"screenshot"` but no Tool Options: `"fg"` on one is refused with `step 1 (v): view takes no "fg"`. A `"scrollTo"` cell must be on the canvas as it stands at that step; one off it is refused (`step 2 (far): scrollTo cell (20, 0) is off the 20 x 10 canvas`). Every refusal exits with status 1.

A view step takes effect where it stands and holds until a later view step changes it. A screenshot taken `"before"` a view step shows the view the steps before it left. Until the first view step the window has a new window's view: zoom 2, scrolled to the top left, Fit, Pad and Swap Shades off. Within one step the zoom is set before the scroll. A view step changes the window, not the piece: it makes no undo step and doesn't mark the document modified.

On a screen whose scale isn't a whole number (150%, say), the cell before the one scrolled to can show up to one of the window's own pixels at the view's edge (one and a half screen pixels at 150%), and the IRC View can start a column or a row early.

### The editor's action list

`blockwright --list-actions` is an option of the editor, `blockwright`, not of `blockwright-cli`. It prints every menu and dock action as a JSON list and exits: each action's `id`, menu, text, default `shortcuts`, tips and more. It lists every action, including ones the open document doesn't offer. Glyph sets 17 to 21 (`glyphSet17` to `glyphSet21`), which are offered only under the IRC target or in a UTF-8 document ([Sets 17 to 21](03-keyboard-mode.md#sets-17-to-21)), carry `"offeredWhen": "in IRC and UTF-8 documents"`; no other action has `offeredWhen`.

## Exit status

| Status | Meaning |
|---|---|
| 0 | Success |
| 1 | An input that can't be read or an output that can't be written; a `convert`, `shade`, `pack`, `unpack` or `snapshot` that would lose data, without `--allow-lossy`; a `library check` that found a problem; a generator or scene that failed; a `replay` step that can't be applied, or any `view` step in a file given to `replay`. Nothing is written. Also an error the command didn't expect, such as one from the file system: it prints `blockwright-cli: <command>: ` and the error's message, and ends the run |
| 2 | A usage error: an unknown command or option, an option the command doesn't take, a missing argument, a value out of range |
| 3 | `export --irc` found a line over the budget, without `--allow-over-budget`. Nothing is written |
| 4 | `lint` found something other than a note |

## Examples

Draw a piece at 2× for a web page:

```
blockwright-cli render --scale 2 piece.ans piece.png
```

Check that every line fits an IRC message, and write the IRC text:

```
blockwright-cli export --irc piece.ans piece.irc
```

Lint a piece and fail a script when it has findings:

```
blockwright-cli lint piece.ans || echo "lint found something"
```

Turn a piece into a project directory, and save its first snapshot:

```
blockwright-cli unpack piece.ans piece/
blockwright-cli snapshot piece/
```

## Every option

The command's own help, `blockwright-cli --help`:

<!-- generated: cli-help -->
