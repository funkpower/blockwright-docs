Title: File formats: .ans, SAUCE, IRC text, UTF-8, XBIN, project files
Checked: Blockwright 0.1.0 (12ee9ef)

# File formats: .ans, SAUCE, IRC text, UTF-8, XBIN, project files

Blockwright keeps a piece in an ANSI file (`.ans`) with its SAUCE record, an XBIN (`.xb`), a BIN (`.bin`), or a project (`.bwp`, or a project directory). It also writes IRC text (`.txt`), Micron pages (`.mu`) and PNG pictures. Its other inputs are in [Other files Blockwright reads](#other-files-blockwright-reads).

Only a project holds everything the editor has. Before writing any other format, the editor says what it will lose.

| Format | Read | Write | Holds |
|---|---|---|---|
| Project, `.bwp` or a directory | Yes | Yes | Everything: layers, any glyph, mIRC's colours, bold, italic and underline, the target, the IRC budget, notes, snapshots, SAUCE |
| ANSI, `.ans` | Yes | Yes | One flat canvas of CP437 glyphs, or any glyph in a UTF-8 `.ans`, in the 16 colours, iCE or blink, SAUCE |
| XBIN, `.xb` | Yes | Yes | One flat canvas, its own palette and font, iCE, SAUCE without its flags |
| BIN, `.bin` | Yes | Yes | One flat canvas an even number of columns wide, iCE, SAUCE |
| IRC text, `.txt` | No | Yes | The rows as IRC lines, in mIRC colours |
| Micron page, `.mu` | No | Yes | The rows as a NomadNet page, in the document's colours, bold, italic and underline |
| PNG | No | Yes, with `blockwright-cli render` | A picture |

## Opening a file

**File > Open...** lists `Blockwright projects and ANSI art (*.bwp *.ans *.xb *.bin)`, `Blockwright projects (*.bwp)`, `ANSI art (*.ans)`, `ANSI art, CP437 (*.ans)`, `ANSI art, UTF-8 (*.ans)`, `XBIN (*.xb)`, `BIN (*.bin)` and `All files (*)`. The CP437 and UTF-8 filters read an `.ans` in that encoding; the others go by its bytes ([UTF-8 ANSI](#utf-8-ansi)).

**File > Open Project Directory...** opens a project directory. **File > Open Recent** lists recent files.

How a file is read:

- A directory holding a `manifest.json`, a file that starts as a zip (`PK` 0x03 0x04), or any file named `.bwp` is a project.
- A file that starts with the XBIN magic (`XBIN` and 0x1A) is an XBIN, whatever its name.
- Otherwise the extension decides, in any case: `.xb` or `.xbin` is XBIN, `.bin` is BIN, anything else ANSI ([UTF-8 ANSI](#utf-8-ansi)).

A file that can't be read gives "Could not open …" and the reason. `blockwright-cli` reads files the same way, except that it ignores the `.bwp` name, and reads a project as its visible layers merged.

## Saving

**File > Save As...** offers `ANSI art (*.ans)`, `ANSI art, UTF-8 (*.ans)`, `Blockwright project (*.bwp)`, `XBIN (*.xb)`, `BIN (*.bin)` and `All files (*)`, starting on the document's own kind. A name without an extension gets the filter's. The extension picks the format: `.bwp` is a project, `.xb` or `.xbin` XBIN, `.bin` BIN, anything else ANSI.

**File > Save As Project Directory...** asks before replacing a directory that holds a project, and refuses one that holds anything else. On a project directory, **Save As...** picks another directory and the second item reads **Save As File...**.

If the file can't hold everything, a warning lists the losses before writing, under "Before saving as .ans:", "Before saving as XBIN:", "Before saving as BIN:" or "Before saving the project:":

| Line | When |
|---|---|
| N cell(s) hold a glyph with no CP437 code and will be written as '?': … | A CP437 `.ans`, XBIN or BIN, and a glyph CP437 doesn't have; the glyphs are named with where they are, such as `★ at 0,0` |
| N cell(s) hold glyphs CP437 can't hold whole: … | A CP437 `.ans`, XBIN or BIN, and a wide glyph or a glyph with combining marks, each named with what it is written as |
| N cell(s) hold a glyph whose CP437 byte .ans reads as a control code (…) and will be written as '?' (XBIN and BIN keep them) | A CP437 `.ans`, and a glyph whose byte the reader would act on (see [Writing](#writing)) |
| N cell(s) hold control characters a UTF-8 .ans can't hold and will be written as '?': … | A UTF-8 `.ans`, and a control character in a cell; other lines name a wide glyph or a zero-width glyph a terminal wouldn't draw in its cells |
| N cell(s) lost their blink when the file was opened with iCE colours, and this save doesn't put it back | See [iCE colours and blink](#ice-colours-and-blink) |
| the file's own palette is left out (only XBIN keeps one) | Anything but XBIN, from an XBIN with its own palette |
| the file's own font is left out (only XBIN keeps one) | Anything but XBIN, from an XBIN with its own font |
| the 9 px letter spacing is left out (XBIN has none and draws 8 px) | XBIN, with 9 px letter spacing on |
| the legacy aspect ratio is left out (XBIN has none) | XBIN, with SAUCE's aspect ratio set; a square one says `square` |
| the SAUCE font name … is left out (XBIN names no font) | XBIN, with a SAUCE font name other than `IBM VGA` or `IBM VGA 437` |
| N cell(s) are in colours the file can't hold, saved as the nearest of the 16 | An `.ans`, XBIN or BIN, and a cell in a colour past the 16, such as one of mIRC's ([Palette, iCE colours and 24-bit colour](09-colour.md#mircs-99-colours)) |
| N cell(s) have bold, italic or underline, which the file can't hold | An `.ans`, XBIN or BIN, and a cell with bold, italic or underline |

When a UTF-8 `.ans` would keep glyphs a CP437 one loses, the warning says so. **Save** writes it anyway; **Cancel** writes nothing.

The status bar then says "Saved …", or a message from [Saving a project as a flat file](#saving-a-project-as-a-flat-file). An `.ans`, XBIN or BIN is written beside its destination and renamed over it, so a failed save ("Could not save …") leaves the old file intact. A flat file is never written over a project: "… is a project; save it as a project or choose another name".

`blockwright-cli convert` and `pack` warn of the same losses and write nothing without `--allow-lossy` ([From the command line](#from-the-command-line)).

## ANSI (.ans) and SAUCE

An `.ans` is CP437 text with ANSI escape codes. A SAUCE record may follow: 128 bytes after a 0x1A giving size, title, author, group, date, font and flags, with optional comments before it.

![A sky shaded from blue down to light cyan over a green field, a yellow sun at the right, funkpower in yellow on the grass](../samples/manual-file-formats/piece.ans "2x")

```
$ blockwright-cli info piece.ans
file:        piece.ans
encoding:    CP437
size:        32x8
ice:         on
sauce:       yes
title:       A sun over a field
author:      funkpower
group:       
date:        20261102
filesize:    496 (matches content)
datatype:    1
filetype:    1
tinfo:       32 8 0 0
flags:       0x1 (iCE on, letter spacing not set, aspect not set)
font:        IBM VGA
comments:    0
```

### Reading

- The width is SAUCE's TInfo1 when the record says Character (DataType 1) and TInfo1 isn't 0; otherwise 80. The height is the last row drawn on, or a Character record's TInfo2 if that is taller. A width outside 1-400 columns is refused, and so is a file that draws below row 5000.
- Colours set with 256-colour or 24-bit codes (`38;5;n`, `38;2;r;g;b`, PabloDraw's `CSI t`) are taken to the nearest of the 16 palette colours.
- The glyphs are CP437 bytes, or UTF-8 ([UTF-8 ANSI](#utf-8-ansi)).
- iCE colours come from a Character record's flags, and are on for a file without one.
- The art ends at the first 0x1A before the record. SAUCE's FileSize never cuts the art; `info` says whether it matches.

### Writing

The writer writes:

- `ESC[0m` first, then each row without trailing black spaces, with a full colour code at each change, and `ESC[0m` and CR LF at the end. A full-width row wraps on its own and gets no CR LF. An empty row is one space.
- Then SAUCE: the document's own record, or a new one dated today in `IBM VGA`. It is written as Character, `ANSi` (DataType 1, FileType 1), with width, height, FileSize and iCE flag from the document.
- In a CP437 `.ans`, a glyph with no CP437 byte, or whose byte the reader would act on (TAB, LF, CR, SUB, ESC), is written as `?`, a wide glyph as `?` and a space, NUL as a space. A UTF-8 `.ans` writes UTF-8 ([UTF-8 ANSI](#utf-8-ansi)).
- A colour past the 16 becomes the nearest of them. Bold, italic and underline are dropped.

### SAUCE fields

**File > SAUCE...** edits the record:

| Field | Limit |
|---|---|
| Title | 35 characters |
| Author | 20 characters |
| Group | 20 characters |
| Date | Empty or `CCYYMMDD`; **Today** fills it in |
| Comments | Up to 255 lines of 64 characters |

Title, author and group refuse non-CP437 characters and text past the limit. While the date or comments are wrong, the dialog says why and **OK** stays greyed out. A field left as it came from the file isn't checked, so a malformed date in the record doesn't stop the rest being edited.

Two flags are set from the View menu:

| View menu item | SAUCE flag |
|---|---|
| iCE Colours | iCE colours (bit 0): bright backgrounds as 16 colours; off, they blink on the dark colour |
| 9 px Letter Spacing | Letter spacing 9 px (bits 1-2): 9 px cells, the line-drawing glyphs 0xC0-0xDF joined as on VGA; off, 8 px |

The aspect flag (bits 3-4) and the font name are kept as read.

## iCE colours and blink

The bright-background bit is also the blink bit. With **iCE colours** on it gives 16 backgrounds; off, there are 8 dark ones and the bit blinks. Turning iCE colours off changes how cells show and save; the cells stay as drawn.

Saved with iCE colours off, the two lower rows of sky are blue and blink.

![The sun piece with iCE colours off: the lower sky blue instead of light blue](../samples/manual-file-formats/blink.ans "2x")

```
$ blockwright-cli info blink.ans
…
ice:         off
…
flags:       0x0 (iCE off, letter spacing not set, aspect not set)
…
```

A file can't have both. One with iCE colours off that holds a bright background anyway (a 24-bit colour, or `ESC[10xm`) opens with iCE colours on, and its blinking cells lose their blink. `mixed.ans` has nine blinking letters and two cells of bright blue background:

![funkpower in yellow on blue, then two light blue cells](../samples/manual-file-formats/mixed.ans "4x")

```
$ blockwright-cli convert mixed.ans out.ans
blockwright-cli: warning: mixed.ans: 9 blinking cells lose their blink: bright backgrounds need iCE colours, where blink is a bright background
blockwright-cli: out.ans: not written: the conversion loses data (--allow-lossy writes it anyway)
```

Converting to XBIN or BIN says the same. In the editor the blink is lost on open, and every save that still writes those cells without their blink lists them. A blank glyph is never counted, as blink on a space shows nothing.

## XBIN (.xb)

An XBIN is an 11-byte header (width, height, font height, flags), an optional palette and font, then character and attribute pairs, optionally run-compressed. Blockwright refuses one with a 512-character font, a font height outside 1-32, a palette or font cut short, or a size of 0 or over 400 × 5000.

- iCE colours are the header's non-blink flag.
- A palette is 16 colours of 6-bit RGB, a font 256 glyphs 8 pixels wide. Only an XBIN save writes them back; other saves warn. The canvas and PNGs ignore them and use the standard palette and IBM VGA font.
- SAUCE, if any, follows the cells.

The writer compresses each row and writes SAUCE as XBin (DataType 6, FileType 0) with flags and font name cleared; iCE goes in the header. So 9 px letter spacing, the aspect flag and a font name other than `IBM VGA` or `IBM VGA 437` are lost: saving warns, and `convert` needs `--allow-lossy`.

```
$ blockwright-cli convert piece.ans piece.xb
$ blockwright-cli info piece.xb
file:        piece.xb
format:      XBIN, compressed
palette:     none
font:        none
size:        32x8
ice:         on
sauce:       yes
title:       A sun over a field
author:      funkpower
group:       
date:        20261102
filesize:    67 (matches content)
datatype:    6
filetype:    0
tinfo:       32 8 0 0
flags:       0x0 (iCE off, letter spacing not set, aspect not set)
font:        
comments:    0
```

The `ice` line is the header's; the SAUCE flags are 0. The art's 496 bytes are 67 as XBIN; with SAUCE, the files are 625 and 196 bytes.

[palette.xb](../samples/manual-file-formats/palette.xb) is an 8 × 2 XBIN with its own palette, and no SAUCE:

```
$ blockwright-cli info palette.xb
file:        palette.xb
format:      XBIN
palette:     custom
font:        none
size:        8x2
ice:         off
sauce:       none
$ blockwright-cli convert palette.xb palette.ans
blockwright-cli: warning: palette.xb: its palette is left out: only XBIN holds one
blockwright-cli: palette.ans: not written: the conversion loses data (--allow-lossy writes it anyway)
```

A palette the same as the standard one isn't counted as lost.

## BIN (.bin)

A BIN is character and attribute pairs, row after row, then SAUCE. The width is FileType × 2 when SAUCE says BinaryText (DataType 5), with iCE colours from its flags; without such a record it is 160 with iCE on. The last row is padded with blank cells.

SAUCE is written as BinaryText (DataType 5, FileType the width / 2, TInfo1-4 0), keeping the flags (iCE set to the document's) and font name. An odd width gains a blank column on the right. A BIN holds no palette or font.

```
$ blockwright-cli convert piece.ans piece.bin
$ blockwright-cli info piece.bin
…
format:      BIN
…
filesize:    512 (matches content)
datatype:    5
filetype:    16
tinfo:       0 0 0 0
flags:       0x1 (iCE on, letter spacing not set, aspect not set)
font:        IBM VGA
…
```

XBIN and BIN write any glyph with a CP437 byte as that byte, control codes included; others as `?`, a wide glyph as `?` and a space.

## Projects (.bwp)

A project is the whole document: layers, IRC budget, notes, snapshots, SAUCE and any files kept with it. It is a zip file, `.bwp`, or a directory of the same files.

```
manifest.json       format, version, size, palette, iCE, target, .ans encoding, IRC budget, SAUCE, layer order, next layer id
layers/<id>.json    the layer's properties
layers/<id>.cells   its cells (a versioned header, then zstd)
fonts/<sha256>.tdf  a TheDraw font a text layer is set in, named by the sha256 of its bytes
notes.md            notes; absent when empty
snapshots/r<N>.ans  snapshots, each the visible layers flattened to an .ans in the project's encoding
refs/<sha256>.png   a reference layer's picture, .png or .jpg, named by the sha256 of its bytes (from version 1.5)
scripts/<id>/, thumbnail.png and anything else
```

The manifest has `"target": "irc"` only under the IRC target, and `"ansEncoding": "utf-8"` only for a UTF-8 `.ans`. A reference layer's `"reference"` key names its picture, with place, size and opacity; a picture whose bytes don't hash to its name is refused.

`blockwright-cli unpack` writes a project directory. For the sun piece:

```
$ blockwright-cli unpack piece.ans piece/
$ find piece -type f | sort
piece/layers/1.cells
piece/layers/1.json
piece/manifest.json
$ cat piece/manifest.json
{
    "format": "blockwright",
    "height": 8,
    "ice": true,
    "ircBudget": {
        "bytes": 407,
        "profile": "efnet-weechat"
    },
    "layers": [
        1
    ],
    "nextLayerId": 2,
    "palette": "cga",
    "sauce": {
        "aspectRatio": "none",
        "author": "funkpower",
        "comments": [
        ],
        "date": "20261102",
        "font": "IBM VGA",
        "group": "",
        "letterSpacing": null,
        "reservedFlags": 0,
        "tinfo3": 0,
        "tinfo4": 0,
        "title": "A sun over a field"
    },
    "version": "1.3",
    "width": 32
}
```

`pack` writes the zip, and `info` reads either:

```
$ blockwright-cli pack piece.ans piece.bwp
$ blockwright-cli info piece.bwp
file:        piece.bwp
project:     zip
size:        32x8
ice:         on
encoding:    CP437
target:      ansi
irc budget:  407 bytes (efnet-weechat)
layers:      1 (next id 2)
  1  cells  32x8 at 0,0  normal  visible yes, locked no, alpha locked no  Background
notes:       0 bytes
snapshots:   0
files:       0
sauce:       yes
title:       A sun over a field
author:      funkpower
group:       
date:        20261102
letter spacing: not set
aspect:      not set
font:        IBM VGA
comments:    0
```

**Versions.** The version is `major.minor`. A feature an older reader can drop without changing the picture raises the minor version; one it would show wrongly raises the major. A wide glyph or cluster makes a project 4.0, and bold, italic or underline 5.0.

A reader refuses a major version it doesn't know. Within a major version it skips unknown keys, and keeps unknown files and saves them back.

A project doesn't hold an XBIN's palette or font: packing an XBIN that has one needs `--allow-lossy`, and Save warns.

### Saving a project as a flat file

Saving a project as an `.ans`, XBIN or BIN writes its visible layers merged. What happens to the document depends on what it holds:

| The document | After saving as `.ans`, `.xb` or `.bin` | Status bar |
|---|---|---|
| One plain cells layer the size of the canvas, at 0,0, visible, normal, unstyled, with no notes, snapshots or files, the budget unchanged and the ANSI target | The flat file becomes the document's file | Saved … |
| A project with more than that | The file is an export; the document is still the project | Exported … flattened; the document is still … |
| A flat file with more than that (a layer added, say) | The file is written, but the document stays modified, since the file doesn't hold it all | Saved … flattened; only a project keeps the layers |

Closing such a flat document asks first: only a project saves its layers and IRC budget.

**File > Take Snapshot** flattens the visible layers to the next `snapshots/r<N>.ans`, in the document's encoding; the status bar says "Took snapshot rN; saving the project keeps it". If the `.ans` would lose anything it asks first, with the same lines as Save. On a flat document it is greyed out: save as a project first.

## IRC text (.txt)

**File > Export IRC Text...** and `blockwright-cli export --irc` write the canvas as IRC text: UTF-8, one line per row ending in a line feed, colours as mIRC codes. Blockwright doesn't read it back. The encoding, byte budget and options are in [IRC](10-irc.md).

## Micron page (.mu)

**File > Export Micron...** and `blockwright-cli export --micron` write the canvas as a Micron page, NomadNet's page markup: UTF-8, one line per row ending in a line feed. Blockwright doesn't read it back. In the app:

1. Any edit in progress lands. A floating selection that can't land stops the export, and the status bar says "Not exported: the floating selection can't land: …".
2. If any cell would be written as something else ([What a page doesn't keep](#what-a-page-doesnt-keep)), a warning starts "Before exporting a Micron page:", lists them, and asks "Export anyway?". **Save** goes on; **Cancel**, the default, stops.
3. The **Export Micron** dialog offers **Centre the piece on the page** and **Write a page cache header, seconds:** with a number from 0 to 31536000. Both start unticked, the number at 0.
4. A file dialog asks where, starting at the document's name with `.mu`, filtered to `Micron pages (*.mu)` or `All files (*)`.
5. The status bar says "Exported a Micron page to …", or a message says "Could not write …" and why.

### What a page holds

- The visible layers merged, under the document's iCE setting. The 16 colours are written in the document's palette (an XBIN's own, if it has one). Any other colour, such as one of [mIRC's 99 colours](09-colour.md#mircs-99-colours), is written as exact RGB.
- A colour as `` `F `` (foreground) or `` `B `` (background) and three hex digits when each channel is one digit doubled, as in the 16 (`#aa5500` is `a50`), else `T` and six digits (`` `FT001008 ``).
- A colour only where it changes and the cell shows it: no foreground for a space unless underlined, no background behind a `█` unless italic.
- Bold, italic and underline as `` `! ``, `` `* `` and `` `_ ``, toggled where they change.
- `` ` `` and `\` escaped with a `\`, and `!` after `#` too.
- Every row and column, blanks included. Each line starts with its colours and ends with ``` `` ```, which resets them.

The sun piece starts:

```
$ blockwright-cli export --micron piece.ans piece.mu
8 lines, 32 columns
$ head -3 piece.mu
`B00a                                ``
`F55f`B00a░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░``
`F55f`B00a▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`Fff5▄▄▄▄▄`F55f▒▒▒▒▒``
```

`palette.xb` is written in its own palette. Its first line is ``` `F000█`FT001008█`FT002010█`FT003018█`FT004120█`FT005128█`FT006130█`FT007138█`` ```.

No `#!bg=` or `#!fg=` header is written.

### Centre and the cache header

**Centre the piece on the page** (`--centre`) starts each line with `` `c ``. A centred line ends by turning off any bold, italic or underline, then `` `f`b ``.

**Write a page cache header** (`--cache S`) writes `#!c=S` as the first line: the seconds a peer may keep the page, `0` for never.

```
$ blockwright-cli export --micron --centre --cache 3600 piece.ans piece.mu
8 lines, 32 columns, centred
$ head -3 piece.mu
#!c=3600
`c`B00a                                `f`b
`c`F55f`B00a░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░`f`b
```

### What a page doesn't keep

- Blink. A blink cell without iCE colours is written on its dark background.
- Some glyphs, written as IRC text writes them ([How a row is encoded](10-irc.md#how-a-row-is-encoded)): a control code as its CP437 glyph, NUL as a space, and a C1 control, U+2028, U+2029 or a non-scalar code point as `?`.
- Glyphs holding code points NomadNet drops, written as `?` (a wide one as `?` and a space): combining marks, format characters, variation selectors, emoji skin-tone modifiers, and `☝`, which NomadNet draws as a space.
- Layers, SAUCE, the target, the IRC budget, notes, snapshots and files.

The glyphs written as `?` are the ones the warning lists. `blockwright-cli` prints them as warnings and writes the file anyway. See [export --micron](14-cli.md#export-micron) for the options.

## UTF-8 ANSI

A UTF-8 `.ans` holds any glyph: a two-column one such as `日` takes two cells, and a glyph with combining marks stays in one. Escape codes are the same. SAUCE stays CP437; its FileSize counts the UTF-8 bytes.

An `.ans` is read as UTF-8 when it starts with a byte order mark, or is all well-formed UTF-8 with at least one sequence of three bytes or more. Anything else is CP437. The status bar shows `CP437` or `UTF-8`.

To read a file the other way, open it with the `ANSI art, CP437 (*.ans)` or `ANSI art, UTF-8 (*.ans)` filter, or use **File > Reopen with Encoding** (**Auto (as its bytes say)**, **CP437** or **UTF-8**). It asks to save edits first, and works only on an `.ans`.

**File > Save** writes an `.ans` in the encoding it was opened or last saved in. A new document is CP437 under the ANSI target, UTF-8 under the IRC target.

**Save As...** with `ANSI art (*.ans)` writes CP437, with `ANSI art, UTF-8 (*.ans)` UTF-8. A UTF-8 `.ans` with no sequence of three bytes or more gets a byte order mark, so it reads back as UTF-8.

`blockwright-cli` reads an `.ans` the same way, or as `--encoding cp437` or `--encoding utf-8` says. `convert` writes CP437 unless given `--output-encoding utf-8`; the sun piece is 883 bytes that way. XBIN and BIN are CP437 only, so `--output-encoding utf-8` to an `.xb` or `.bin` is refused, exit status 2.

## Other files Blockwright reads

| File | Read by |
|---|---|
| PNG and JPEG pictures | **File > Open Reference Image...** (`Images (*.png *.jpg *.jpeg)`), as a reference layer; a project keeps the picture under `refs/` |
| Python scenes (`.py`) | **File > Open Scene...** and `blockwright-cli import-scene`, which run the scene and open it as a project with a generator layer for each of its layers |
| A generator's directory (`generator.json`, and `params.json` and scripts) | `blockwright-cli add-generator` |
| TheDraw fonts (`.tdf`) | The fonts folder set in Preferences, for text layers, and a `text` step in a `blockwright-cli replay` steps file ([A TheDraw font](14-cli.md#a-thedraw-font)); a project keeps the fonts its text layers use under `fonts/` |
| Library stamps (an `.ans` and its `.json` sidecar) and text styles (`.style.json`) | The Library, from the bundled library and the user's; `blockwright-cli library list` and `library check` |

## What each format keeps

| | Project | `.ans` | XBIN | BIN |
|---|---|---|---|---|
| Layers | Yes | Merged | Merged | Merged |
| Glyphs with no CP437 code | Yes | `?` (CP437), Yes (UTF-8) | `?` | `?` |
| mIRC's colours past 15 | Yes | The nearest of the 16 | The nearest of the 16 | The nearest of the 16 |
| Bold, italic, underline | Yes | No | No | No |
| iCE colours | Yes | Yes | Yes (header) | Yes |
| An XBIN's palette and font | No | No | Yes | No |
| SAUCE title, author, group, date, comments | Yes | Yes | Yes | Yes |
| SAUCE letter spacing and aspect | Yes | Yes | No | Yes |
| SAUCE font name | Yes | Yes | No; a warning unless it is `IBM VGA` or `IBM VGA 437` | Yes |
| Odd width | Yes | Yes | Yes | A blank column added |
| Target, IRC budget, notes, snapshots, files | Yes | No | No | No |

## From the command line

```
blockwright-cli convert [--allow-lossy] [--encoding auto|cp437|utf-8] [--output-encoding cp437|utf-8] <in> <out>
blockwright-cli pack [--allow-lossy] [--encoding auto|cp437|utf-8] [--target ansi|irc] <in> <out.bwp>
blockwright-cli unpack [--allow-lossy] [--encoding auto|cp437|utf-8] [--target ansi|irc] <in> <dir>
```

`convert` writes the format `<out>`'s name gives: XBIN for `.xb` or `.xbin`, BIN for `.bin`, ANSI for anything but `.bwp`, which it refuses with exit status 1: `pack` writes a project. `pack` and `unpack` write a project, its target set by `--target` (default: a project's own, else `ansi`).

A conversion that would lose something prints a warning for each loss and writes nothing, exit status 1. With `--allow-lossy` it prints the warnings and writes the file:

```
$ blockwright-cli convert palette.xb palette.ans
blockwright-cli: warning: palette.xb: its palette is left out: only XBIN holds one
blockwright-cli: palette.ans: not written: the conversion loses data (--allow-lossy writes it anyway)
$ blockwright-cli pack palette.xb palette.bwp
blockwright-cli: warning: palette.xb: its palette is left out: only XBIN holds one
blockwright-cli: palette.bwp: not written: the project loses data (--allow-lossy writes it anyway)
```

`convert` loses blink only where a bright background forces iCE colours on, as with `mixed.ans` above. `pack` warns of lost blink but writes the project anyway. Other options are in [convert](14-cli.md#convert) and [pack, unpack and snapshot](14-cli.md#pack-unpack-and-snapshot).
