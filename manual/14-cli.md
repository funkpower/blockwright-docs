Title: blockwright-cli
Checked: Blockwright 0.1.0 (c44974c)

# blockwright-cli

`blockwright-cli` is Blockwright without the window. It converts, renders, exports, shades and lints pieces, packs and unpacks projects, and runs generator layers, so scripts can do what the editor does.

```
blockwright-cli [options] command [args...]
```

## What it reads

Every command that reads a piece takes an ANSI file (`.ans`), an XBIN (`.xb`) or a BIN (`.bin`). It also takes a project, a `.bwp` zip or a project directory, and reads it as its flattened composite: the visible layers merged as the editor shows them. Commands that write a piece (`convert`, `shade`) write XBIN to an output named `.xb`, BIN to one named `.bin`, and ANSI otherwise.

## Commands

### info

```
blockwright-cli info <file>
```

Prints the piece's size, whether it uses iCE colours, and its SAUCE fields (title, author, group, date, font, letter spacing). For a project it also prints the layers (id, kind, size, position, mode, visibility and locks, name), the IRC byte budget, the size of the notes in bytes, and the snapshots.

### convert

```
blockwright-cli convert [--allow-lossy] <in> <out>
```

Reads a piece and writes it as ANSI, XBIN or BIN, chosen by `<out>`'s extension. `<out>` may be `<in>`: the file is rewritten in place, which normalises it. When something can't be represented in the output, nothing is written unless `--allow-lossy` is given.

### render

```
blockwright-cli render [--scale N] [--font-width 8|9] <in> <out.png>
blockwright-cli render --irc [--budget N] [--scale N] [--font-width 8|9] <in> <out.png>
```

Draws the piece as a PNG with the IBM VGA font.

| Option | What it does |
|---|---|
| `--scale N` | Integer zoom, nearest neighbour, 1 to 8 (default 1) |
| `--font-width 8\|9` | Glyph width in pixels (default: the SAUCE letter spacing, else 8) |
| `--irc` | Draw the IRC view instead: the mIRC palette, without what IRC drops, each line cut at the budget. Prints how many rows were cut |
| `--budget N` | With `--irc`: the bytes a line may take (default 407) |

`render` refuses to write over its input.

### export --irc

```
blockwright-cli export --irc [--budget N] [--fit] [--pad] [--swap-shades] [--allow-over-budget] <in> <out>
```

Writes the piece as IRC text with mIRC colour codes, one line per row, and prints a table of each line's size in bytes, then a summary:

```
40 lines, longest 256 bytes, budget 407: 0 over
```

| Option | What it does |
|---|---|
| `--budget N` | The bytes a line may take. Default: a project's own budget, else 407 (EFnet through WeeChat) |
| `--fit` | Fit lines over the budget by merging their least visible colours, and report how many cells were merged in how many lines |
| `--pad` | Keep trailing black cells and blank rows at the top and bottom, ending each row on a black block |
| `--swap-shades` | Let the encoder draw a shade as its opposite with the colours reversed when that is shorter |
| `--allow-over-budget` | Write the file even when lines are over the budget |

A line over the budget is reported with how far over it is. Without `--allow-over-budget` the output isn't written and the exit status is 3.

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
| `--form dome\|cylinder\|plane` | Shade the selection as that form |
| `--glint` | With `--form`: a glint of the ramp's top rung at the brightest point |
| `--despeckle` | Clear the selection's specks |
| `--rim` | Light the selection's edge cells that face the light |
| `--light P` | With `--form` or `--rim`: where the light comes from, `N`, `NE`, `E`, `SE`, `S`, `SW`, `W` or `NW` (default `NW`) |
| `--ice` | Turn iCE colours on. Without it, a piece without iCE colours keeps them off, and no shade that needs a bright background is used |

`--form`, `--despeckle` and `--rim` need a selection: `--box`, `--mask` or both. Only one mode can be given.

### lint

```
blockwright-cli lint [--ramp R]... [--box x0,y0,x1,y1] [--json] <in>
```

Checks the shading ladders under each ramp, the pixel noise, and the craft rules. It prints one line per finding (cell, kind, ramp, message) and a summary:

```
62 findings (5 wide-rung, 47 rung-skip, 2 speckle, 2 fallback-speck, 1 one-glyph, 5 trailing-black), noise 0.0013, iCE on
```

`--ramp` can be given more than once; without it every named ramp is checked, and the craft pairs. `--json` prints the findings as JSON instead. The exit status is 4 when there are findings.

### library

```
blockwright-cli library list [dir]
blockwright-cli library check <dir>
```

`list` prints the stamps and text styles in a library, by default the bundled library and the user's, one per line, tab-separated: kind, category, name, size, widest IRC row in bytes, `ice` when a text style needs iCE colours (else `-`), tags, path. A text style's size and bytes are those of its thumbnail sample.

`check` checks every stamp, sidecar and text style in a library directory, drawing each text style's sample.

### pack, unpack and snapshot

```
blockwright-cli pack [--allow-lossy] <in> <out.bwp>
blockwright-cli unpack [--allow-lossy] <in> <dir>
blockwright-cli snapshot [--allow-lossy] <project>
```

`pack` writes a piece or a project as a project zip. `unpack` writes one as a project directory; `<dir>` must be empty or a project already. A project can't hold an XBIN's own palette or font, so `pack` and `unpack` drop them only with `--allow-lossy`.

`snapshot` saves the project's flattened composite as its next round, `snapshots/rN.ans`, and prints `rN`.

### Generators

```
blockwright-cli add-generator [--name NAME] [--timeout S] <project> <dir>
blockwright-cli run-generators [--layer ID]... [--timeout S] <project>
blockwright-cli import-scene [--timeout S] <scene.py> <out>
```

These run programs: a generator layer's output comes from the program its `generator.json` names.

- `add-generator` adds a generator layer on top of the project, from a directory with a `generator.json` (and a `params.json` and scripts), runs it once and saves the project. `--name` names the layer (default: the directory's name).
- `run-generators` runs the project's generator layers again, bottom first, and saves their output. `--layer` picks one layer by id (as `info` lists them); give it more than once for several.
- `import-scene` opens a Python scene as a new project with a generator layer for each of the scene's layers, run once. `<out>` is a `.bwp`, or a directory that doesn't exist or is empty. It runs the scene with `python3` (on Windows, the first of `py -3`, `python` and `python3` that is Python 3).

`--timeout` is the seconds a generator may run, 1 to 3600 (default 30). If any run fails, nothing is written.

## Exit status

| Status | Meaning |
|---|---|
| 0 | Success |
| 1 | An input that can't be read or an output that can't be written; a `convert`, `shade`, `pack`, `unpack` or `snapshot` that would lose data, without `--allow-lossy`; a `library check` that found a problem; a generator or scene that failed. Nothing is written |
| 2 | A usage error: an unknown command or option, a missing argument, a value out of range |
| 3 | `export --irc` found a line over the budget, without `--allow-over-budget`. Nothing is written |
| 4 | `lint` found something |

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
