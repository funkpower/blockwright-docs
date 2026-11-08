Title: The Library: stamps, Save to Library and text styles
Checked: Blockwright 0.1.0 (bb1c676)

# The Library: stamps, Save to Library and text styles

The Library holds **stamps**: parts of a picture kept as files, ready to place on the canvas, and the **text styles** the Text tool and **Layer Style** use. Some come with Blockwright, in the bundled library; the ones you save go in your own, the user library. This page covers the **Library** dock, placing a stamp, frames and bands that resize, **Save to Library**, where the files are kept and the limits.

Tutorial 08, [Composing a scene](../tutorials/08-composing-a-scene.md), places parts with the Select tool and ends with the Library.

Prefabs, parts made of several layers, and the **Scene Starter**, which lays out a scene from the Library in one go, aren't in the app yet.

## Where it is

| Item | Where | Shortcut |
|---|---|---|
| The **Library** dock | The right-hand dock column, below **Layers**; **Window > Library** | none |
| **Save to Library...** | **Selection** | none |
| **Save as Frame Style...** | **Selection** | none |
| **Save as Preset...** | The **Layer Style** dialog (**Layer > Layer Style…**) | none |
| `library list`, `library check` | `blockwright-cli` ([CLI](14-cli.md#library)) | |

The Library dock can be moved and floated but not closed, so its **Window** menu item is always ticked and greyed out ([The Window menu](02-the-window.md#the-window-menu)). **Window > Reset Layout** puts it back.

**File > Publish to Library...** is something else: it publishes the piece to an IRC art library folder, not to this Library.

## The Library dock

![The Library dock: a search box reading "Search names and tags", a category list with All highlighted over buildings, classic and elements, a grid of stamp thumbnails with their names (Barn, Castle keep, Fence, House, Lighthouse, Log cabin, Stone bridge, Windmill, Wall of fire, the four frames, Snowy boulder, Cliff edge, Far mountain range), each name whole, wrapped onto a second line when it is long, and a Refresh button at the bottom](../samples/manual-08-library/dock.png)

From the top:

| Part | What it does |
|---|---|
| Search box | Shows only the items whose name or tags hold every word you type, in any order. A word can be part of a name or tag: `pin` finds `pine`. Upper and lower case are the same for A to Z. The category isn't searched. The **×** in the box clears it. |
| Category list | **All**, then each category once, from the stamps and the text styles, in byte order (so a capitalised category comes before the lower-case ones). Pick one to show only its items; it works together with the search. |
| Thumbnails | Each stamp and text style, its name under it. A thumbnail is the stamp drawn at full size, or shrunk to fit, never enlarged. The bundled stamps come first, then yours, then the bundled text styles, then yours, each group in path order: by category folder, then by file name. |
| Skipped files | Below the grid, when a file in either library can't be read: *1 file skipped*, *3 files skipped*. Its tooltip lists each file and what is wrong with it. |
| **Refresh** | Reads both libraries again. |

Hover over a stamp for its name, size, widest IRC row, category, tags, and which library it is in with its path. The bundled pine:

```
Pine tree
13 x 14 cells, widest IRC row 30 bytes
Category: trees
Tags: tree, pine, conifer, evergreen
Bundled library: …/share/blockwright/library/trees/pine-tree.ans
```

The dock reads the libraries when Blockwright starts, after **Save to Library**, **Save as Frame Style** and **Save as Preset**, and on **Refresh**. A file added, changed or removed some other way shows up on the next **Refresh**. The dock has no way to rename or delete a stamp: do that to its files ([Where stamps are kept](#where-stamps-are-kept)).

A fresh install has 63 stamps and 11 text styles:

| Category | Stamps | Text styles |
|---|---|---|
| buildings | 8 | |
| classic | | 5: Gold 3D, Outline, Rainbow, Shadow, Sunset |
| elements | | 2: Fire, Ice |
| fire | 1 | |
| frames | 4: Bevelled block frame, Double line frame, Hazard stripe frame, Single line frame | |
| land | 7 | |
| metal | | 1: Chrome |
| plants | 3 | |
| signs | | 3: Masthead, Neon, Warning sign |
| sky | 14 | |
| smoke | 3 | |
| symbols | 6 | |
| things | 3 | |
| trees | 11 | |
| water | 3 | |

## Placing a stamp

Double-click a stamp, or select it and press <kbd>Enter</kbd>, and it floats with its top left corner at the cell cursor. Drag it onto the canvas, and it floats with its top left corner on the cell you drop it on. The Select tool is taken in hand, and the cell cursor moves to the corner.

The stamp is now a float, the same as a paste ([Selections](05-selections.md#the-float)): drag it or move it with the arrow keys, flip it or turn it, and put it down with <kbd>Enter</kbd> or a click. <kbd>Esc</kbd> drops it. Nothing is changed until it is put down, and then it is one edit. A float already up when you place a stamp is put down first.

A stamp lands in **Transparent** mode, whatever the **Paste** setting: its blank cells, spaces on black, leave the canvas under them as it was. While it floats, **Selection > Paste Mode** and **Paste** in **Tool Options** show **Transparent**. Pick another mode while it floats and the stamp lands in that one, and that mode becomes the setting ([Paste modes](05-selections.md#paste-modes)).

It lands on the layer that is active when it is put down. Clicking another layer in the Layers dock puts the float down on the old one first. A layer that can't take the stamp, a hidden, locked, Generator, Reference or live Text layer, or a Pixels layer when a cell of the stamp isn't something half blocks can show, takes nothing: the float goes and the canvas is as it was, with no message.

A stamp is placed as the Library last read it, not from its file at that moment: after changing a stamp's files, press **Refresh**.

### Frames and bands

A stamp saved with **Resize** set is a **frame**, which resizes both ways, or a **band**, which resizes in width only. Placed, it floats with handles on its outline: eight on a frame, two on a band, one at each end. Drag a handle to resize it, the side opposite staying put. The **insets**, the cells at each side kept whole, stay as they are, and what is between them is repeated to fill. Each resize starts again from the stamp as it was saved, so shrinking it and growing it back loses nothing; only the stamp you put down is an edit.

The four bundled frames are frames: Bevelled block, Double line and Single line keep one cell at each side, and Hazard stripe keeps 4 at the left, 8 at the right, 2 at the top and 3 at the bottom.

## Save to Library

**Selection > Save to Library...** keeps the selection, or the float, as a stamp in your user library. It is greyed out until there is a selection or a float.

What it saves:

- **A float**, lifted, pasted or a placed stamp: the floating cells as they stand, after any flip or turn. A float lifted from a Pixels layer is saved as the layer shows it.
- **A selection with nothing floating**: the selected cells of the **visible composite**, every visible layer merged, not just the active layer. **Copy** takes the active layer only.

The **Save to Library** dialog:

| Field | What it takes |
|---|---|
| **Name** | The stamp's name, each character one CP437 has a glyph for. The field stops at 35 characters. Spaces at the ends are dropped. |
| **Category** | Type one, or pick one of the categories the Library has. It starts empty. |
| **Tags** | Words to search by, comma-separated (`tree, pine, night`). Empty and repeated tags are dropped. |
| **Resize** | **Fixed size**, **Width only (a band)** or **Width and height (a frame)** |
| **Insets** | **Left**, **Right**, **Top** and **Bottom**, each starting at 1: the cells kept whole at each side when it resizes. **Left** and **Right** are for a band or a frame, **Top** and **Bottom** for a frame only. Saving a placed frame or band again starts from its own. |

Under the fields, the dialog says what is missing, and **OK** stays greyed out until nothing is: *The stamp needs a name.*, *The name holds a character CP437 has no glyph for.*, *The stamp needs a category.*

When the top folder of your user library already has a stamp with the same name, Blockwright asks first: *A stamp named "…" is already in the library (…). Do you want to replace it?*, **No** by default. A bundled stamp is never replaced. Saved, the status bar says *Saved … to the library* with the file's path, and the Library shows the stamp at once.

The cells are written as an `.ans`, with the document's iCE setting. A transparent cell is written as a space on black, a blank cell: it is the see-through part of the stamp, which a placed stamp leaves alone in **Transparent** mode.

If it can't be saved, a box says *Could not save the stamp:* and why, for example:

- the selection is more than 400 columns or 5000 rows;
- every cell is blank, so the stamp would draw nothing;
- a frame or band holds a wide character, or its insets leave no column or row between them to repeat;
- there is no user library directory, or it can't be written.

### Save as Frame Style and Save as Preset

**Selection > Save as Frame Style...** turns a small drawn box into a style for the Frame tool. It is saved at the top of the user library as `<file name>.frame.json`, the file name made from its name as a stamp's is ([Where stamps are kept](#where-stamps-are-kept)); a name already used gets a number on the end, and a frame style is never replaced. It appears in the Frame tool's style list after the built-in ones, not in the Library dock.

**Save as Preset...** in the **Layer Style** dialog saves the layer's style as a text style in the user library, `<file name>.style.json`, named the same way. A name already used gets a number on the end; a preset is never replaced. Text styles show in the dock with the stamps:

- double-click one to apply it to the active layer;
- drag one onto the canvas to start a new text layer in that style where you drop it;
- a style that needs iCE colours is greyed out while iCE colours are off ([iCE colours](09-colour.md#ice-colours)).

## Where stamps are kept

A stamp is two files side by side, with the same name: an `.ans` and a `.json` sidecar. There is no index.

- **`<name>.ans`**: the cells, in CP437 with a SAUCE record whose title is the stamp's name ([File formats](13-file-formats.md)). A stamp holding characters CP437 can't write is saved as UTF-8 instead.
- **`<name>.json`**: the category, the tags, the widest IRC row in bytes, and for a frame or band its insets.

The category comes from the sidecar, not from the folder the files are in.

The file name is the stamp's name in lower case, A to Z and 0 to 9, each run of other characters between them a `-`, at most 48 characters: **Pine (night)** is `pine-night.ans`. A name with no letter or digit is spelt in code points: **♥** is `u2665.ans`. A stamp with a different name that makes the same file name, such as **pine night**, is saved as `pine-night-2.ans`, then `-3`, and so on; only the same name, character for character, replaces. Saved stamps go at the top of the user library, not in a folder per category.

| Library | Where | Written by Blockwright |
|---|---|---|
| Bundled | `share/blockwright/library` beside the installed program, or `$BLOCKWRIGHT_BUNDLED_LIBRARY` | Never |
| User | `$BLOCKWRIGHT_USER_LIBRARY` if it is set; otherwise `Blockwright/library` in the system's data folder: `~/.local/share/Blockwright/library` on Linux (or under `$XDG_DATA_HOME`), `~/Library/Application Support/Blockwright/library` on macOS, `AppData\Local\Blockwright\library` in the user's folder on Windows | **Save to Library**, **Save as Frame Style**, **Save as Preset** |

The user library folder is made the first time something is saved to it. Copy a stamp's two files into it, or out of it to share, and **Refresh**. To delete a stamp, delete both files.

`blockwright-cli library list` prints the stamps and text styles of both libraries, and `library check <dir>` checks a folder's files, including each stamp's IRC row widths ([CLI](14-cli.md#library)).

## Limits

- **Size.** A stamp is at most 400 columns by 5000 rows, and can't be all blank.
- **Name.** 1 to 35 characters, all in CP437.
- **Category and tags.** A category can't be empty; a tag can't hold a comma. Neither can hold a control character.
- **IRC.** **Save to Library** doesn't check a stamp's rows against the IRC budget; `blockwright-cli library check` does.
- **Placing.** The float keeps at least one cell on the canvas; the cells off the canvas are lost when it lands. A layer that refuses the stamp takes nothing, with no message.
- **Managing.** The dock doesn't rename, move or delete stamps; do it to the files and **Refresh**.
- **Steps files.** A steps file has no step that places or saves a stamp, so `replay` and `--screenshot` can't show one being placed.
