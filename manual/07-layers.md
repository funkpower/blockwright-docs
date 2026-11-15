Title: Layers: the five kinds, the dock and the menu
Checked: Blockwright 0.1.0 (12ee9ef)

# Layers: the five kinds, the dock and the menu

A piece is a stack of layers, composited bottom first. A layer's kind decides what it holds, which tools paint it and how it covers the layers below.

A flat `.ans` opens as one Cells layer named `Background`. Only a project (`.bwp`, or a project directory) keeps the layers. Any other file holds the visible layers merged ([Saving a project as a flat file](13-file-formats.md#saving-a-project-as-a-flat-file)).

## The five kinds

The **Kind** column of the Layers dock names each layer's kind; its tooltip is the kind's section in **Help > Manual...**.

| Kind | Holds | Painted by | Made by |
|---|---|---|---|
| **Cells** | A glyph and a foreground and background colour in each cell | Typing, the Glyph Brush, the shade and ramp brushes, the detail brushes, the pixel tools and the Frame tool | **+ Cells**, **Layer > New Cells Layer** |
| **Pixels** | Two half-block colours a cell, top and bottom, each a palette colour or transparent | The Half-Block Brush, Line, Rectangle, Ellipse and Fill | **+ Pixels**, **Layer > New Pixels Layer** |
| **Text** | Live text in a font, drawn as glyph cells | The Text tool and Tool Options; painting tools can't change it | The Text tool |
| **Generator** | A program's cached output, as glyph cells | Its parameters and **Run** in the Layers dock; painting tools can't edit it | **File > Open Scene...** (as a new project), `blockwright-cli add-generator` and `import-scene` |
| **Reference** | A picture to trace | Nothing paints it; it is moved and resized | **File > Open Reference Image...** |

### Cells

A Cells layer holds a glyph, a foreground and a background colour in each cell. Every painting tool paints it. In the normal mode, opaque cells replace the cells below and transparent cells show through.

A new Cells layer is all transparent. Erasing on it leaves a transparent cell, so the layer below shows; on the bottom layer it leaves a blank cell instead, a space in grey on black, so a flat `.ans` stays opaque. Erasing means <kbd>Backspace</kbd>, <kbd>Delete</kbd>, the right button of the Glyph Brush or the Frame tool, or clearing a selection.

### Pixels

A Pixels layer holds two half-block colours per cell, top and bottom, each a palette colour or transparent. Paint it with the Half-Block Brush, Line, Rectangle, Ellipse or Fill. Other tools can write only a space, `█`, `▀` or `▄`; anything else is refused.

Set halves cover what is below. Transparent halves show through, unless the layer has a layer style switched on ([How the layers combine](#how-the-layers-combine)). A cell erased on a Pixels layer is transparent, even on the bottom layer.

Where one half is transparent, the cell picks `▀` or `▄` and its colours so the free half shows what is under it. Over a shade cell the free half shows `░`'s background, `▓`'s foreground, and `▒`'s darker colour in a free top half or its lighter colour in a free bottom half, so a shape over a shaded field gets no specks.

- With iCE colours off, a cell shows one bright colour, and the pixel keeps its own. A free half that would show a different bright colour goes dark: under `█`, `▀` or `▄` to that colour's dark version (yellow to brown, dark grey to black), under `▓` or `▒` to the shade's background in its dark version.
- With iCE colours off, a free half showing the cell's foreground keeps its blink only where the pixel is dark and a different colour from it.
- A text cell stays in front of pixels ([Text](#text)).

### Text

A Text layer holds text rendered as glyph cells. Edit it with the Text tool and Tool Options; painting tools can't change it.

- Click a Text layer with the Text tool to edit it.
- Click anywhere else and type to start a new Text layer, `Text N`, above the active layer. A `text` step in a `replay` steps file does the same ([The text tool](14-cli.md#the-text-tool)).
- A Text layer without a live text source can be painted like a Cells layer.

No Pixels layer covers a text cell, above or below. A Cells or Generator layer above that writes its own glyph there makes it a plain cell again ([How the layers combine](#how-the-layers-combine)).

### Generator

A Generator layer holds a program's cached output as glyph cells. Change its parameters and press **Run** in the Layers dock; painting tools can't edit the output.

The cached cells composite like a Cells layer. Opening or exporting doesn't run the generator, so the project shows and exports the same on a machine without the program.

**File > Open Scene...** opens a Python scene as a new project, one Generator layer per scene layer, after asking to run it.

A generator is a program that runs with your permissions. Blockwright asks before a project's generators first run in a session, with **No** the default. A refused or failed run leaves the cells as they were and says why in the status bar.

The commands that add and run generator layers are in [the CLI](14-cli.md). Writing and running generators is in [Generator layers and scripts](12-generators.md).

### Reference

A Reference layer holds a picture to trace. The project saves it with its place, size and opacity.

**File > Open Reference Image...** adds a picture as the active layer, `Reference N`, at the top of the stack, as wide as the canvas and at 50% opacity. It is one undo step. The project keeps a PNG or JPEG as it is, and other formats (such as BMP, GIF, WebP or TIFF) as a PNG.

Raise it to see the picture over your art; lower it to draw over the picture. Painting tools can't edit it.

- <kbd>Alt</kbd>+drag or the Move/Transform tool moves it by canvas pixels.
- The Move/Transform tool's corner handles and Tool Options (**X**, **Y**, **Width**, **Height**, **Keep aspect**, **Scale**) resize it.
- **Layer > Reference Opacity** sets how strongly it shows: **25%**, **50%**, **75%** or **100%**.

The compositor skips it, and it is never exported.

## Which kind to pick

The dock's hint, under the list: `Cells: glyphs and shades. Pixels: half-block drawing.`

- **Cells** for anything drawn with glyphs: shading with `░▒▓`, line drawing, typed text, detail.
- **Pixels** for half-block shapes over other work: a figure, a moon, a line of hills. You can move or redraw the shape without repainting the background.
- **Text** for lettering you still want to edit: a title in a TheDraw font or big whole-cell letters. Bake it (below) to paint over the letters.
- **Generator** for art a program makes from parameters, such as a Python scene opened with **File > Open Scene...**. Bake it (below) to keep its cells and paint over them.
- **Reference** for a photo or sketch to trace.

## The Layers dock

The **Layers** dock is on the right of the window ([Docks](02-the-window.md#docks)). It lists the layers top first. The current row is the active layer, the one the tools edit; picking it is not an undo step.

| Column | What it does |
|---|---|
| **Layer** | The box shows or hides the layer. Double-click the name to rename it; an empty name is refused. |
| **Alpha Lock** | Ticked, the tools paint only the layer's opaque cells (on a Pixels layer, its opaque pixels). The same setting as the alpha lock in Tool Options. |
| **Kind** | Cells, Pixels, Text, Generator or Reference. Its tooltip explains the kind. |
| **Style** | `fx` when the layer has a layer style. Double-click to edit or add one. Only Cells, Pixels and live Text layers can have one. |

A hidden layer still saves, but it isn't in the composite, the export or the lint. A stroke or typing on a hidden layer is refused.

| Button | Layer menu item | What it does |
|---|---|---|
| **+ Cells** | **New Cells Layer** | Adds a Cells layer above the active layer. |
| **+ Pixels** | **New Pixels Layer** | Adds a Pixels layer above the active layer. |
| **Delete** | **Delete Layer** | Deletes the active layer. The layer below becomes active (the new bottom, when the bottom one goes). Greyed out when the stack has one layer. |
| ▲ | **Raise Layer** | Moves the active layer up one. Greyed out on the top layer. |
| ▼ | **Lower Layer** | Moves the active layer down one. Greyed out on the bottom layer. |

A new layer is the canvas's size, all transparent, named `Layer N` with the lowest free N, and becomes the active layer.

Each change in the dock is one undo step. Undoing an add or a delete makes the layer that was active active again.

Before a change in the dock, other than a rename or the alpha lock, the tool lands what it holds (a drag, a floating selection) on the layer it was editing. A floating selection that can't land there is dropped ([A float that can't land](05-selections.md#a-float-that-cant-land)).

An **Undo** or **Redo** of one of these changes lands nothing first. It keeps a floating selection when it leaves the active layer and the active layer's cells and offset as they were, as undoing a hide, a lock, a raise or a lower does. Otherwise it drops the float ([The float](05-selections.md#the-float)).

When the active layer is a Generator layer, its form is under the buttons: a field per parameter, and **Run**. A field commits, as one undo step, when you:

- release a slider;
- step a spin box with its arrows, the mouse wheel or the arrow keys;
- tick or clear a box, or pick an entry;
- end a typed value with <kbd>Enter</kbd> or by leaving the field.

The generator runs again shortly after a commit. Undo and redo put back both the parameters and the cells, and run nothing.

## The Layer menu

The **Layer** menu has the dock's actions and the ones that change a layer's content. None has a shortcut; set one in **Edit > Preferences... > Shortcuts**.

| Item | What it does |
|---|---|
| **New Cells Layer** | As **+ Cells**. |
| **New Pixels Layer** | As **+ Pixels**. |
| **Delete Layer** | As **Delete**. |
| **Raise Layer** | As ▲. |
| **Lower Layer** | As ▼. |
| **Layer Style…** | Opens the **Layer Style** dialog for the active layer. It lists the effects in drawing order, each with a box to switch it on or off: plate, glow, shadow, outline, fill, shade and bevel. **Preset** starts from a text style in the Library. Greyed out unless the active layer is a Cells, Pixels or live Text layer. |
| **Bake Layer** | Makes the active layer a Cells layer of what it shows. A live Text layer keeps its cells and drops its text. A Generator layer keeps its last run's cells, name, offset, visibility, mode and locks, and drops its program and form. A styled Cells or Pixels layer keeps its styled cells and drops its style; if every effect is off, baking only drops the style, and a Pixels layer stays a Pixels layer. Only undoing the bake (one step) brings the text, form or style back. Greyed out unless the active layer is a live Text layer, a Generator layer, or a Cells or Pixels layer with a style. |
| **Reference Opacity** | **25%**, **50%**, **75%** or **100%** for the active Reference layer; greyed out on any other kind. |

## Moving a layer

With any tool, <kbd>Alt</kbd> and a left-drag on the canvas moves the active layer; the Move/Transform tool does it without <kbd>Alt</kbd>. An art layer moves by whole cells, a Reference layer by canvas pixels. The status bar shows where it will land.

Releasing is one undo step; <kbd>Esc</kbd> drops the move. A hidden layer doesn't move. A layer moved partly off the canvas keeps its cells there.

## How the layers combine

Each cell starts blank: a space, grey on black, with no bold, italic, underline or blink. Each visible layer then adds to it, bottom first. Hidden layers and Reference layers add nothing.

On a Cells, Text or Generator layer, a transparent cell adds nothing. What an opaque cell writes depends on the layer's mode:

| Mode | An opaque cell |
|---|---|
| **normal** | Replaces the cell: glyph, colours, bold, italic, underline and blink. |
| **chars-only** | Writes its glyph, and keeps the colours, bold, italic, underline and blink under it, except where a wide glyph shows whole over two cells coloured differently (below). |
| **colours-only** | Writes its foreground, background, bold, italic, underline and blink, and keeps the glyph under it. |

There is no blending: a cell is opaque or transparent.

- A Pixels layer adds the halves it sets, whatever its mode:
  - A cell with both halves set is stored opaque. It replaces the cell under it, with no bold, italic, underline or blink.
  - A cell with one half set is stored as a transparent `▀` (top half) or `▄` (bottom half) in the half's colour, and the other half shows what is under it. The cell keeps the bold, italic and underline of the cell under it, and its blink only as [Pixels](#pixels) says. A transparent `▀` light red over `A` white on blue gives `▀` light red on blue.
  - Any other transparent cell adds nothing.
  - With iCE colours off, a free half that would be a second bright colour in the cell shows dark ([Pixels](#pixels)).
- A Cells or Pixels layer whose style has an effect switched on composites its styled cells in place of its own. A cell the style draws in is opaque; the rest are transparent. So a style can add cells where the layer is transparent, such as an outline.
  - A Cells layer's styled cells combine by its mode, as in the table.
  - A Pixels layer's styled cells combine as whole cells in the normal mode, whatever its own mode. Where the layer sets one half, the other half shows what the style draws there (black where no other effect draws) and hides what is under it. Its styled cells never cover a text cell.
- A cell that a Text layer writes its glyph to (normal or chars-only) is text. No Pixels layer, above or below, adds anything to it. A Cells or Generator layer that then writes its glyph there (normal or chars-only) makes it plain cells again; a colours-only one recolours it and leaves it text.
- A wide glyph such as `日` takes two cells of one layer, both with its colours and formatting. It shows whole while no layer above writes a glyph to either cell:
  - A layer above that writes a glyph to one of the two cells (a normal or chars-only cell, or a Pixels layer's half) leaves the other a space, in the colours it has there. `日` white on blue, with `B` light red on green over its right half, gives a space white on blue, then `B`.
  - Where `日` shows whole over two cells coloured differently, both take the colours, bold, italic, underline and blink of the highest layer to colour either cell (the left cell's, when that layer coloured both). This holds in every mode: a chars-only `日` over `A` white on blue and `B` light red on green shows white on blue in both cells.

A new layer is in the normal mode, and the app has no control for the mode. A project keeps it as `"mode"` (`"normal"`, `"chars-only"` or `"colours-only"`) in each `layers/<id>.json` ([Projects](13-file-formats.md#projects-bwp)), and opening and saving in the app leaves it as it was. To change it, unpack the project, set the key and pack it again:

```
$ blockwright-cli unpack piece.bwp piece/
$ # set "mode" in piece/layers/<id>.json
$ blockwright-cli pack piece/ piece.bwp
```

In the sample project `samples/01-layers-showcase`, the `stars` layer is chars-only (star glyphs coloured by the sky under them) and the `reflection` layer is colours-only (the moon's yellow on the water's ripple glyphs).

Everything that reads a project as a picture uses this composite of the visible layers: saving to an `.ans`, an XBIN or a BIN, exporting IRC text or a Micron page, taking a snapshot, the lint, and the `blockwright-cli` commands `convert`, `render`, `export --irc`, `export --micron`, `lint`, `shade`, `snapshot` and `replay`. `blockwright-cli info` lists a project's layers with their ids, kinds, sizes, places, modes and visibility, as in `3  cells  80x7 at 0,0  chars-only  visible yes, locked no, alpha locked no  stars` ([CLI](14-cli.md)).
