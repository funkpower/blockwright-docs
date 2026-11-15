Title: The Library: stamps, Save to Library and text styles
Checked: Blockwright 0.1.0 (12ee9ef)

# The Library: stamps, Save to Library and text styles

The Library holds **stamps**, parts of a picture to place on the canvas, and the **text styles** the Text tool and **Layer Style** use. Some come in the bundled library; the ones you save go in your user library.

Tutorial 08, [Composing a scene](../tutorials/08-composing-a-scene.md), places parts with the Select tool and ends with the Library.

Prefabs (parts made of several layers) and the **Scene Starter**, which lays out a scene from the Library in one go, aren't in the app yet.

## Where it is

| Item | Where | Shortcut |
|---|---|---|
| The **Library** dock | The right-hand dock column, below **Layers**; **Window > Library** | none |
| **Save to Library...** | **Selection** | none |
| **Save as Frame Style...** | **Selection** | none |
| **Save as Preset...** | The **Layer Style** dialog (**Layer > Layer Style…**) | none |
| `library list`, `library check` | `blockwright-cli` ([CLI](14-cli.md#library)) | |

The Library dock can be moved and floated but not closed ([The Window menu](02-the-window.md#the-window-menu)). **Window > Reset Layout** puts it back.

## The Library dock

![The Library dock: a search box reading "Search names and tags", a category list with All highlighted over buildings, classic and elements, a grid of stamp thumbnails with their names (Barn, Castle keep, Fence, House, Lighthouse, Log cabin, Stone bridge, Windmill, Wall of fire, the four frames, Snowy boulder, Cliff edge, Far mountain range), each name whole, wrapped onto a second line when it is long, and a Refresh button at the bottom](../samples/manual-08-library/dock.png)

From the top:

| Part | What it does |
|---|---|
| Search box | Shows only the items whose name or tags hold every word you type, in any order. A word can be part of a name or tag: `pin` finds `pine`. Case doesn't matter for A to Z. The category isn't searched. The **×** clears the box. |
| Category list | **All**, then each category of the stamps and text styles once, in byte order (capitalised categories first). Pick one to show only its items; it combines with the search. |
| Thumbnails | Each stamp and text style with its name under it, drawn at full size or shrunk to fit, never enlarged. Bundled stamps first, then yours, then bundled text styles, then yours, each group by category folder, then file name. |
| Skipped files | Below the grid, when a file in either library can't be read: *1 file skipped*, *3 files skipped*. Its tooltip lists each file and what is wrong with it. |
| **Refresh** | Reads both libraries again. |

Hover over a stamp for its details. The bundled pine:

```
Pine tree
13 x 14 cells, widest IRC row 30 bytes
Category: trees
Tags: tree, pine, conifer, evergreen
Bundled library: …/share/blockwright/library/trees/pine-tree.ans
```

The dock reads the libraries at startup, after **Save to Library**, **Save as Frame Style** and **Save as Preset**, and on **Refresh**. To rename or delete a stamp, see [Your own stamps and categories](#your-own-stamps-and-categories).

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

Double-click a stamp, or select it and press <kbd>Enter</kbd>, to float it at the cell cursor. Or drag it onto the canvas and drop it; its top left corner lands on the cell you drop it on. Either way the Select tool is taken in hand.

The stamp is now a float ([Selections](05-selections.md#the-float)): move, flip or turn it, put it down with <kbd>Enter</kbd> or a click, or drop it with <kbd>Esc</kbd>. A float already up is put down first; if it can't land, the new stamp isn't placed.

A stamp lands in **Transparent** mode, whatever the **Paste** setting. A mode picked while it floats is used instead and becomes the setting ([Paste modes](05-selections.md#paste-modes)).

It lands on the active layer. Clicking another layer in the Layers dock lands it on the old one first, or drops it if it can't land there.

A layer that can't take the stamp refuses it before it floats. The status bar says *Could not place* and why, such as *the layer is locked*, *the layer is hidden*, *a live Text layer is drawn from its text* or *a Pixels layer holds no ░▒*.

- A stamp whose only glyphs a Pixels layer can't hold are `▌` and `▐` floats on a Pixels layer ([A float that can't land](05-selections.md#a-float-that-cant-land)), but lands only after **Selection > Rotate Clockwise** or **Rotate Counterclockwise** turns them into `▀` and `▄`. Until then <kbd>Enter</kbd> or a click says *a Pixels layer holds no ▌▐; rotate it (Selection > Rotate) or press Esc to drop it*.
- One that also holds `▀` or `▄` never lands.
- An **Undo** that hides or locks the layer leaves a floating stamp up; <kbd>Enter</kbd> then says *the layer is hidden; press Esc to drop it* or *the layer is locked; press Esc to drop it*.

A stamp is placed as the Library last read it, so press **Refresh** after changing its files.

### Frames and bands

A stamp saved with **Resize** set is a **frame**, which resizes both ways, or a **band**, which resizes in width only. Placed, it floats with handles: eight on a frame, one at each end of a band. Drag one to resize; the opposite side stays put.

The **insets**, the cells kept whole at each side, stay as they are; what is between them repeats to fill. Shrinking and growing it back loses nothing.

The four bundled frames are frames. Bevelled block, Double line and Single line keep one cell at each side. Hazard stripe keeps 4 at the left, 8 at the right, 2 at the top and 3 at the bottom.

## Save to Library

**Selection > Save to Library...** keeps the selection, or the float, as a stamp in your user library. It is greyed out until there is a selection or a float. It saves:

- **A float** (lifted, pasted or a placed stamp): the floating cells as they stand, after any flip or turn. A float lifted from a Pixels layer is saved as the layer shows it.
- **A selection with nothing floating**: the selected cells of the **visible composite**, every visible layer merged (where **Copy** takes the active layer only).

The **Save to Library** dialog:

| Field | What it takes |
|---|---|
| **Name** | The stamp's name, each character one CP437 has a glyph for. At most 35 characters; spaces at the ends are dropped. |
| **Category** | Type one, or pick one the Library has. It starts empty. |
| **Tags** | Words to search by, comma-separated (`tree, pine, night`). Empty and repeated tags are dropped. |
| **Resize** | **Fixed size**, **Width only (a band)** or **Width and height (a frame)** |
| **Insets** | **Left**, **Right**, **Top** and **Bottom**, each starting at 1: the cells kept whole at each side when it resizes. **Left** and **Right** are for a band or a frame, **Top** and **Bottom** for a frame only. A placed frame or band saved again starts from its own. |

**OK** stays greyed out while the dialog says something is missing: *The stamp needs a name.*, *The name holds a character CP437 has no glyph for.*, *The stamp needs a category.*

If the top folder of your user library has a stamp with the same name, Blockwright asks before replacing it, **No** by default. A bundled stamp is never replaced.

The cells are written as an `.ans` with the document's iCE setting. A transparent cell is written as a space on black, which **Transparent** mode leaves see-through.

If it can't be saved, a box says *Could not save the stamp:* and why, for example:

- the selection is more than 400 columns or 5000 rows;
- every cell is blank, so the stamp would draw nothing;
- a frame or band holds a wide character, or its insets leave no column or row between them to repeat;
- there is no user library directory, or it can't be written.

### Save as Frame Style and Save as Preset

**Selection > Save as Frame Style...** turns a small drawn box into a Frame tool style, saved at the top of the user library as `<file name>.frame.json` ([Where stamps are kept](#where-stamps-are-kept)). A name already used gets a number on the end; a frame style is never replaced. It appears in the Frame tool's style list, not in the Library dock.

**Save as Preset...** in the **Layer Style** dialog saves the layer's style as a text style, `<file name>.style.json`, named the same way and never replaced. Text styles show in the dock with the stamps:

- double-click one to apply it to the active layer;
- drag one onto the canvas to start a new text layer in that style where you drop it;
- a style that needs iCE colours is greyed out while iCE colours are off ([iCE colours](09-colour.md#ice-colours)).

## Your own stamps and categories

A category is a name in a stamp's sidecar. **Make a category** by typing a new name in **Category** when you save a stamp; a category can't exist without stamps.

A category of yours with a bundled one's name, such as `trees`, is one entry showing both sets.

### Adding a stamp to a category

- **From the canvas.** Select the part, or have it floating, and choose **Selection > Save to Library...** with that category ([Save to Library](#save-to-library)).
- **From a stamp already in the Library**, bundled or yours. Place it, choose **Selection > Save to Library...** while it floats, give it a name and your category, then press <kbd>Esc</kbd>: saving doesn't put the float down. The copy goes in your user library, and one saved under a bundled stamp's own name shows twice, once from each library.
- **From an `.ans` file.** Open it with **File > Open...**, select the part (or **Selection > Select All**, <kbd>Ctrl</kbd>+<kbd>A</kbd>), and save it to the Library.
- **By hand.** Copy a stamp's `.ans` and `.json` into the user library and press **Refresh**. An `.ans` without a sidecar isn't a stamp; the **Skipped files** tooltip says *no sidecar*, or *.ans has no SAUCE record (the title is the stamp's name)* when it has no SAUCE record.

    A hand-written sidecar has to give the widest row's IRC bytes exactly. `blockwright-cli library check <dir>` says what is wrong with each file, such as *sidecar says the widest row is 0 IRC bytes; the art's is 52*.

### Changing a stamp's name, category or tags

**To change only the category or the tags**, edit the stamp's `.json` in a text editor ([Where stamps are kept](#where-stamps-are-kept)) and press **Refresh**. `blockwright-cli library check <dir>` says whether the edited sidecar still reads.

**To change the name**, place the stamp and save it again ([Adding a stamp to a category](#adding-a-stamp-to-a-category)); the name is the `.ans` file's SAUCE title. That writes both files afresh, with two traps:

- **The dialog starts empty.** Empty Tags saves no tags. Hover over the stamp in the dock first to see its category and tags.
- **The art is the float as it is now.** A resize, flip or turn before saving is saved too. Save straight after placing it.

The **same name**, character for character, asks to replace the stamp. A **new name** makes a new stamp and leaves the old one to delete.

Only a stamp at the top of the user library is replaced; one you moved into a folder gets a second copy at the top.

A bundled stamp can't be changed. Save a copy to your library and change that.

### Removing a stamp, or a category

To remove a stamp, delete its `.ans` and `.json` from the user library and press **Refresh**.

A category leaves the list once no stamp or text style is in it. To remove one of yours, delete its stamps and presets, or change the `category` in their `.json` or `.style.json`. Bundled categories stay.

### Folders and sharing

The user library is read with every folder in it. **Save to Library** always writes to the top. A symbolic link to a folder isn't followed (*symbolic link to a folder, not followed* under **Skipped files**); copy the folder in.

To share stamps, copy their files into someone else's user library and press **Refresh**. Check them first with `blockwright-cli library check <dir>` ([CLI](14-cli.md#library)).

## Where stamps are kept

A stamp is two files side by side with the same name:

- **`<name>.ans`**: the cells, in CP437 with a SAUCE record whose title is the stamp's name ([File formats](13-file-formats.md)). A stamp with characters CP437 can't write is saved as UTF-8.
- **`<name>.json`**: the category, the tags, the widest IRC row in bytes, and a frame's or band's insets.

The category comes from the sidecar, not the folder.

The file name is the stamp's name in lower case, A to Z and 0 to 9, each run of other characters a `-`, at most 48 characters: **Pine (night)** is `pine-night.ans`. A name with no letter or digit is spelt in code points: **♥** is `u2665.ans`. A different name that makes the same file name, such as **pine night**, is saved as `pine-night-2.ans`, then `-3`.

| Library | Where | Written by Blockwright |
|---|---|---|
| Bundled | `share/blockwright/library` beside the installed program, or `$BLOCKWRIGHT_BUNDLED_LIBRARY` | Never |
| User | `$BLOCKWRIGHT_USER_LIBRARY` if it is set; otherwise `Blockwright/library` in the system's data folder: `~/.local/share/Blockwright/library` on Linux (or under `$XDG_DATA_HOME`), `~/Library/Application Support/Blockwright/library` on macOS, `AppData\Local\Blockwright\library` in the user's folder on Windows | **Save to Library**, **Save as Frame Style**, **Save as Preset** |

The user library folder is made the first time something is saved to it.

`blockwright-cli library list` prints both libraries; `library check <dir>` checks a folder's files and IRC row widths ([CLI](14-cli.md#library)).

## Limits

- **Size.** A stamp is at most 400 columns by 5000 rows, and can't be all blank.
- **Name.** 1 to 35 characters, all in CP437.
- **Category and tags.** A category can't be empty; a tag can't hold a comma. Neither can hold a control character.
- **IRC.** **Save to Library** doesn't check a stamp's rows against the IRC budget; `blockwright-cli library check` does.
- **Placing.** The float keeps at least one cell on the canvas; cells off the canvas are lost when it lands.
- **Managing.** The dock doesn't rename, move or delete stamps, or make categories or folders: save a stamp again, or change its files and **Refresh** ([Your own stamps and categories](#your-own-stamps-and-categories)). There is no import or export command for a set of stamps; copy the files.
- **Steps files.** No step places or saves a stamp, so `replay` and `--screenshot` can't show one being placed.
