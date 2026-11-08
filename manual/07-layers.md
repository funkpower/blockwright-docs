Title: Layers: the five kinds, the dock and the menu
Checked: Blockwright 0.1.0 (07846f9)

# Layers: the five kinds, the dock and the menu

A piece in Blockwright is a stack of layers, composited bottom first into the canvas you see. Each layer has a kind, which decides what it holds, which tools can paint it, how it covers the layers below and how it exports. This page covers the five kinds, which to pick for what, the **Layers** dock and the **Layer** menu.

A flat `.ans` opens as one Cells layer named `Background`. Only a project (`.bwp`, or a project directory) keeps the layers; any other file holds the visible layers merged ([Saving a project as a flat file](13-file-formats.md#saving-a-project-as-a-flat-file)).

## The five kinds

The **Kind** column of the Layers dock names each layer's kind; hover over it for a short explanation of the kind, the same text as the kind's section in **Help > Manual...**. The sections below say the same in more detail.

| Kind | Holds | Painted by | Made by |
|---|---|---|---|
| **Cells** | A glyph and a foreground and background colour in each cell | Typing, the Glyph Brush, the shade and ramp brushes, the detail brushes, the pixel tools and the Frame tool | **+ Cells**, **Layer > New Cells Layer** |
| **Pixels** | Two half-block colours a cell, top and bottom, each a palette colour or transparent | The Half-Block Brush, Line, Rectangle, Ellipse and Fill | **+ Pixels**, **Layer > New Pixels Layer** |
| **Text** | Live text in a font, drawn as glyph cells | The Text tool and Tool Options; painting tools can't change it | The Text tool |
| **Generator** | A program's cached output, as glyph cells | Its parameters and **Run** in the Layers dock; painting tools can't edit it | **File > Open Scene...** (as a new project), `blockwright-cli add-generator` and `import-scene` |
| **Reference** | A picture to trace | Nothing paints it; it is moved and resized | **File > Open Reference Image...** |

### Cells

A Cells layer holds a glyph plus foreground and background colours in each cell. Use keyboard mode (typing), the Glyph Brush, the shade and ramp brushes, the detail brushes, the pixel tools or the Frame tool.

Opaque cells normally replace the cells below; transparent cells show through. Exports flatten the visible layers into character cells.

A new Cells layer is all transparent. Erasing on it (<kbd>Backspace</kbd>, <kbd>Delete</kbd>, the Glyph Brush's and the Frame tool's right button, clearing a selection) leaves a transparent cell, so the layer below shows; on the bottom layer it leaves a blank cell instead, a space in grey on black, so a flat `.ans` stays opaque.

### Pixels

A Pixels layer holds two half-block colours per cell (top and bottom), each either a palette colour or transparent.

Paint with the Half-Block Brush, Line, Rectangle, Ellipse or Fill. Other tools can only write a space, `█`, `▀` or `▄`; shade-producing tools and other glyphs are refused, and nothing is written.

Set halves cover what is below; transparent halves show through, except on a layer with a layer style switched on ([How the layers combine](#how-the-layers-combine)). Where a half is transparent, the cell picks `▀` or `▄` and its colours so the free half shows what is under it: a pixel's own half, or the colour a shade cell shows (`░` its background, `▓` its foreground, `▒` its darker colour in a free top half and its lighter colour in a free bottom half), so a shape drawn over a shaded field doesn't leave specks at its edges. With iCE colours off a cell shows only one bright colour, and the pixel keeps its own: where the pixel is bright and the free half would show a different bright colour, the free half goes dark, to that colour's dark version under `█`, `▀` or `▄` (yellow to brown, dark grey to black) and to the shade's background in its dark version under `▓` or `▒`. A blinking free half (iCE off, a half showing the cell's foreground) keeps its blink only where the pixel is dark and a different colour from it. A text cell stays in front of pixels ([Text](#text)). Exports flatten these pixels into half-block glyphs and colours in the visible composite.

A cell erased on a Pixels layer is transparent, even when the layer is the bottom one.

### Text

A Text layer holds text rendered as glyph cells with foreground and background colours.

Edit live text with the Text tool and Tool Options; painting tools cannot change it. Clicking a Text layer with the Text tool edits it; clicking anywhere else and typing starts a new Text layer there, named `Text N`, just above the active layer; a `text` step in a `replay` steps file does the same ([The text tool](14-cli.md#the-text-tool)). Without a live text source, the cells can be painted like a Cells layer.

Opaque text cells normally replace cells below and cannot be covered by Pixels layers, whichever is on top; transparent cells show through. A Cells or Generator layer above that writes its own glyph over a text cell makes it plain cells again ([How the layers combine](#how-the-layers-combine)). Exports flatten the visible rendered text into character cells.

### Generator

A Generator layer holds a program's cached output as glyph cells with foreground and background colours.

Change its parameters and press **Run** in the Layers dock; painting tools cannot edit the output. The cached cells composite like a Cells layer and export in the visible composite. Opening or exporting does not run the generator, so a project with generator layers shows and exports the same on a machine that doesn't have the program.

**File > Open Scene...** opens a Python scene as a new project, one Generator layer per scene layer, after asking to run it. Running a generator runs a program on your computer with your permissions, so Blockwright asks before a project's generators first run in a session, with **No** the default; a run that is refused or fails leaves the layer's cells as they were and says why in the status bar. The commands that add and run generator layers outside the window are in [the CLI](14-cli.md). The generators the samples carry, the form, running and writing a generator are in [Generator layers and scripts](12-generators.md).

### Reference

A Reference layer holds a picture to trace, saved with the project with its place, size and opacity. **File > Open Reference Image...** takes a picture and adds it as a Reference layer named `Reference N` at the top of the stack, as wide as the canvas, at 50% opacity, and makes it the active layer; adding it is one undo step. The project keeps a PNG or JPEG as it is, and a picture in another format the app reads (BMP, GIF, WebP and TIFF among them) as a PNG.

It shows in its place in the stack: over the art layers below it and under the art layers above it, so raise it to see the picture over your art or lower it to draw over the picture. Painting tools cannot edit it. <kbd>Alt</kbd>+drag or the Move/Transform tool moves it by canvas pixels, and the Move/Transform tool's corner handles and Tool Options (**X**, **Y**, **Width**, **Height**, **Keep aspect**, **Scale**) resize it. **Layer > Reference Opacity** sets how strongly it shows: **25%**, **50%**, **75%** or **100%**.

It is skipped by the compositor and never exported.

## Which kind to pick

The dock's own hint, under the list, puts it in one line: `Cells: glyphs and shades. Pixels: half-block drawing.`

- **Cells** for anything drawn with glyphs: shading with `░▒▓`, line drawing, typed text, detail. It is the kind every tool paints.
- **Pixels** for shapes drawn in half-block pixels that sit over other work: a figure, a moon, a line of hills. The halves the layer leaves transparent show the layer below in the same cell (until it has a layer style switched on), so the shape can be moved or redrawn without repainting the background, and its edges over a shaded field stay clean.
- **Text** for lettering you still want to edit: a title in a TheDraw font or big whole-cell letters. Bake it (below) when you want to paint over the letters.
- **Generator** for art a program makes from parameters, such as a Python scene opened with **File > Open Scene...**, when you want to change the parameters and run it again. Bake it (below) when you want to keep its cells and paint over them.
- **Reference** for a photo or sketch to trace. It never reaches the export.

## The Layers dock

The **Layers** dock is on the right of the window ([Docks](02-the-window.md#docks)). It lists the layers top first; the current row is the active layer, the one the tools edit. Which layer is active is not an undo step.

| Column | What it does |
|---|---|
| **Layer** | The box shows or hides the layer; double-click the name to rename it. An empty name is refused and the row goes back. |
| **Alpha Lock** | Ticked, the tools paint only the layer's opaque cells (on a Pixels layer, its opaque pixels). It is the same setting as the alpha lock in Tool Options, which follows the active layer. |
| **Kind** | Cells, Pixels, Text, Generator or Reference. Its tooltip explains the kind. |
| **Style** | `fx` when the layer has a layer style; double-click to edit it, or to add one. Only Cells, Pixels and live Text layers can have one. |

A hidden layer still saves, but it isn't in the composite, the export or the lint, and the tools don't edit it: a stroke or typing on a hidden layer is refused.

Under the list are the hint and the buttons:

| Button | Layer menu item | What it does |
|---|---|---|
| **+ Cells** | **New Cells Layer** | Adds a Cells layer above the active layer. |
| **+ Pixels** | **New Pixels Layer** | Adds a Pixels layer above the active layer. |
| **Delete** | **Delete Layer** | Deletes the active layer. The layer below becomes active (the new bottom, when the bottom one goes). Greyed out when the stack has one layer. |
| ▲ | **Raise Layer** | Moves the active layer up one. Greyed out on the top layer. |
| ▼ | **Lower Layer** | Moves the active layer down one. Greyed out on the bottom layer. |

A new layer is the canvas's size, all transparent, named `Layer N` with the lowest free N, and becomes the active layer. The tooltips of **+ Cells** and **+ Pixels** and of their menu items explain the kind they add, and the status bar says `Add a Cells layer above the active layer: glyphs and shades` or `Add a Pixels layer above the active layer: half-block drawing` while the pointer is on the menu item.

Each change in the dock is one undo step: undoing an add or a delete makes the layer that was active active again. Before any change in the dock, the tool lands what it holds (a drag, a floating selection) on the layer it was editing.

When the active layer is a Generator layer, its form is under the buttons: a field for each parameter the generator declares, with its value, and **Run**, which runs the generator again as it is. A field commits when it is let go or stepped: a slider released, a spin box stepped by its arrows, the mouse wheel or the arrow keys, a box ticked or cleared, an entry picked, or a typed value ended with <kbd>Enter</kbd> or by focus leaving it; each commit is one undo step, and the generator runs again shortly after. Undo and redo put back both the parameters and the cells, and run nothing.

## The Layer menu

The **Layer** menu has the dock's actions and the ones that change a layer's content. None has a shortcut; give one in **Edit > Preferences... > Shortcuts**.

| Item | What it does |
|---|---|
| **New Cells Layer** | As **+ Cells**. |
| **New Pixels Layer** | As **+ Pixels**. |
| **Delete Layer** | As **Delete**. |
| **Raise Layer** | As ▲. |
| **Lower Layer** | As ▼. |
| **Layer Style…** | Opens the **Layer Style** dialog for the active layer: its effects, in the order they draw, each with a box to switch it on or off (plate, glow, shadow, outline, fill, shade and bevel), and **Preset**, which starts from a text style in the Library. Greyed out unless the active layer is a Cells, Pixels or live Text layer. |
| **Bake Layer** | Makes the active layer a Cells layer of what it shows: a live Text layer keeps its cells and drops its text, a Generator layer keeps the cells its last run left, with its name, offset, visibility, mode and locks, and drops its program and form, and a styled Cells or Pixels layer keeps its styled cells and drops its style. A style with every effect switched off draws nothing, so baking it only drops the style, and a Pixels layer stays a Pixels layer. The text, form or style can't be edited after, except by undoing the bake, which is one step. Greyed out unless the active layer is a live Text layer, a Generator layer, or a Cells or Pixels layer with a style: a plain Cells or Pixels layer, a Text layer without a live text source and a Reference layer can't be baked. |
| **Reference Opacity** | **25%**, **50%**, **75%** or **100%** for the active Reference layer; greyed out on any other kind. |

## Moving a layer

With any tool, <kbd>Alt</kbd> and a left-drag on the canvas moves the active layer; the Move/Transform tool does the same without <kbd>Alt</kbd>. An art layer moves by whole cells, a Reference layer by canvas pixels. The canvas and the 1× preview show the move as you drag, and the status bar shows how far it has gone and where the layer will be. Releasing is one undo step; <kbd>Esc</kbd> drops the move. A hidden layer doesn't move, and a layer moved partly off the canvas keeps its cells there.

## How the layers combine

Each cell of the canvas starts blank: a space, grey on black, with no bold, italic, underline or blink. It then takes each visible layer over it in turn, bottom first. A cell no visible layer adds anything to stays as it started. A hidden layer adds nothing, and a Reference layer never adds anything.

On a Cells, Text or Generator layer, a transparent cell adds nothing. What an opaque cell writes depends on the layer's mode:

| Mode | An opaque cell |
|---|---|
| **normal** | Replaces the cell: glyph, colours, bold, italic, underline and blink. |
| **chars-only** | Writes its glyph, and keeps the colours, bold, italic, underline and blink under it, except where a wide glyph shows whole over two cells coloured differently (below). |
| **colours-only** | Writes its foreground, background, bold, italic, underline and blink, and keeps the glyph under it. |

There is no blending: a cell is opaque or transparent, and the mode decides which of its parts it writes.

- A Pixels layer adds the halves it sets, whatever its mode, and leaves the others showing what is under them:
  - A cell with both halves set is stored opaque. It replaces the cell under it, and has no bold, italic, underline or blink.
  - A cell with one half set is stored as a transparent `▀` (the top half) or `▄` (the bottom half), its foreground the half's colour. It adds that half, and the other half shows what is under it. The cell keeps the bold, italic and underline of the cell under it, and that cell's blink only as [Pixels](#pixels) says. A transparent `▀` light red over `A` white on blue gives `▀` light red on blue.
  - Any other transparent cell adds nothing.
  - With iCE colours off, a free half that would be a second bright colour in the cell shows dark ([Pixels](#pixels)).
- A Cells or Pixels layer with a layer style that has any effect switched on composites its styled cells instead of its own. A cell the style draws in is opaque, and one it draws nothing in is transparent and adds nothing. So the layer can add cells where its own are transparent, such as an outline round what it holds.
  - A Cells layer's styled cells combine by its mode, as in the table.
  - A Pixels layer's combine as whole cells in the normal mode, whatever its own mode. Where the layer sets only one half of a cell, the other half shows what the style draws there (black where no other effect draws), not what is under it. Like its pixels, its styled cells never cover a text cell.
- A cell that a Text layer writes its glyph to (normal or chars-only) is text, and stays in front of any Pixels layer, above or below it: a Pixels layer adds nothing to it. A Cells or Generator layer that then writes its glyph there (normal or chars-only) makes it plain cells again; a colours-only one recolours it and leaves it text.
- A wide glyph, such as `日`, takes two cells of one layer: the glyph, and its continuation in the cell to its right. The continuation has the same colours and formatting as the glyph. `日` shows whole only while no layer above it writes a glyph to either of the two cells:
  - A layer above that writes a glyph to one of the two cells (a normal or chars-only cell, or a Pixels layer's half) leaves the other one a space, in the colours it has there. `日` white on blue, with `B` light red on green over its right half, gives a space white on blue, then `B`.
  - A colours-only layer above one or both cells, or a cell above that adds nothing (such as a transparent cell of a Cells layer), writes no glyph, so `日` still shows whole.
  - Where `日` shows whole but its two cells were coloured differently, both take the colours, bold, italic, underline and blink written last: those of the highest layer to colour either cell, the left cell's when that layer coloured both. This holds in every mode: a chars-only `日` over `A` white on blue and `B` light red on green shows white on blue in both cells.

A new layer is in the normal mode, and the app has no control for the mode: neither the Layers dock nor the Layer menu shows or sets it. A project keeps it, as `"mode"` (`"normal"`, `"chars-only"` or `"colours-only"`) in each `layers/<id>.json` ([Projects](13-file-formats.md#projects-bwp)), so opening and saving a project in the app leaves each layer's mode as it was. To change it, unpack the project, set the key and pack it again:

```
$ blockwright-cli unpack piece.bwp piece/
$ # set "mode" in piece/layers/<id>.json
$ blockwright-cli pack piece/ piece.bwp
```

Blockwright's own sample project, `samples/01-layers-showcase`, uses both: its `stars` layer is chars-only, star glyphs that take their colours from the sky under them, and its `reflection` layer is colours-only, the moon's yellow laid on the water's own ripple glyphs.

Saving to an `.ans`, an XBIN or a BIN, exporting IRC text, taking a snapshot, the lint and every `blockwright-cli` command that reads a project as a picture (`convert`, `render`, `export --irc`, `lint`, `shade`, `snapshot`, `replay`) use this composite of the visible layers. `blockwright-cli info` lists a project's layers with their ids, kinds, sizes, places, modes and visibility, as in `3  cells  80x7 at 0,0  chars-only  visible yes, locked no, alpha locked no  stars` ([CLI](14-cli.md)).
