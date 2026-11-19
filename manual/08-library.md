Title: The Library: stamps, Save to Library and text styles
Checked: Blockwright 0.1.1 (1347435)

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
| **New Collection...**, **Rename Collection...**, **Delete Collection...**, **Add Files to Collection...**, **Add Folder to Collection...**, **Add to Collection...**, **Edit Stamp...**, **Remove Stamp...** | The Library dock's **Collections** button, and right-click on the category list or the thumbnails | none; <kbd>Delete</kbd> on a stamp of yours is **Remove Stamp...** |
| `library list`, `library check`, `library new`, `rename`, `delete`, `add`, `edit`, `remove` | `blockwright-cli` ([CLI](14-cli.md#library)) | |

The Library dock can be moved and floated but not closed ([The Window menu](02-the-window.md#the-window-menu)). **Window > Reset Layout** puts it back.

## The Library dock

![The Library dock: a search box reading "Search names and tags", a category list with All highlighted over buildings, classic and elements, a grid of stamp thumbnails with their names (Barn, Castle keep, Fence, House, Lighthouse, Log cabin, Stone bridge, Windmill, Wall of fire, the four frames, Snowy boulder, Cliff edge, Far mountain range), each name whole, wrapped onto a second line when it is long, and the Collections and Refresh buttons at the bottom](../samples/manual-08-library/dock.png)

From the top:

| Part | What it does |
|---|---|
| Search box | Shows only the items whose name or tags hold every word you type, in any order. A word can be part of a name or tag: `pin` finds `pine`. Case doesn't matter for A to Z. The category isn't searched. The **×** clears the box. |
| Category list | **All**, then each category of the stamps and text styles once, in byte order (capitalised categories first). Pick one to show only its items; it combines with the search. |
| Thumbnails | Each stamp and text style with its name under it, drawn at full size or shrunk to fit, never enlarged. Bundled stamps first, then yours, then bundled text styles, then yours, each group by category folder, then file name. |
| Skipped files | Below the grid, when a file in either library can't be read: *1 file skipped*, *3 files skipped*. Its tooltip lists each file and what is wrong with it. |
| **Collections** | A menu of the collection commands ([Your own stamps and collections](#your-own-stamps-and-collections)). |
| **Refresh** | Reads both libraries again. |

Hover over a stamp for its details. The bundled pine:

```
Pine tree
13 x 14 cells, widest IRC row 30 bytes
Category: trees
Tags: tree, pine, conifer, evergreen
Bundled library: …/share/blockwright/library/trees/pine-tree.ans
```

The dock reads the libraries at startup, after **Save to Library**, **Save as Frame Style**, **Save as Preset** and every collection command, and on **Refresh**, keeping the search and the category picked. To rename or remove a stamp of yours, see [Your own stamps and collections](#your-own-stamps-and-collections).

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
| **Category** | Type one, or pick one the Library has, a collection of yours included. It starts empty. A collection's name files the stamp in that collection's folder ([Collections](#collections)). |
| **Tags** | Words to search by, comma-separated (`tree, pine, night`). Empty and repeated tags are dropped. |
| **Resize** | **Fixed size**, **Width only (a band)** or **Width and height (a frame)** |
| **Insets** | **Left**, **Right**, **Top** and **Bottom**, each starting at 1: the cells kept whole at each side when it resizes. **Left** and **Right** are for a band or a frame, **Top** and **Bottom** for a frame only. A placed frame or band saved again starts from its own. |

**OK** stays greyed out while the dialog says something is missing: *The stamp needs a name.*, *The name holds a character CP437 has no glyph for.*, *The stamp needs a category.*

If the place the stamp goes already has one of the same name, Blockwright asks before replacing it, **No** by default: `A stamp named "Pine" is already in the library (…/pine.ans). Do you want to replace it?` The place is the top folder of your user library, or for a collection anywhere in its folder. A bundled stamp is never replaced.

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

## Your own stamps and collections

Your stamps live in your user library. A **collection** is a named set of them, which you make, rename and delete from the dock. A category is a name in a stamp's sidecar; a collection's stamps have its name as their category, so the category list shows each collection with the categories.

![The Library dock holding one collection of your own, Night sky, with its four stamps (Crescent moon, Full moon, Small star, Star field), listed in the category list under All; the Collections and Refresh buttons at the bottom. The bundled stamps are left out of this picture](../samples/manual-08-library/collection.png)

A category or collection of yours with a bundled one's name, such as `trees`, is one entry showing both sets.

The collection commands are on the dock's **Collections** button. Right-click the category list for the collection commands, or a thumbnail for the stamp commands and **New Collection...**, **Add Files to Collection...** and **Add Folder to Collection...**. None has a shortcut; they are listed under **Library** in [Shortcuts](15-shortcuts.md#every-action), where one can be set.

What a command did, or why it did nothing, shows in the status bar: `Made the collection "Night sky"`, `"trees" is a bundled category, not one of your collections; nothing renamed`. A bundled stamp, a text style and a bundled category can't be changed; a command on one is refused there, with no dialog.

### Collections

- **New Collection...** asks for a name and makes an empty collection, listed at once. A name already in use is refused, as is one whose folder name another folder already has ([Where stamps are kept](#where-stamps-are-kept)): `No collection made: a collection named "Night sky" already exists`.
- **Rename Collection...** renames the collection picked in the category list, and its stamps' category with it. The collection stays picked under its new name.
- **Delete Collection...** deletes the collection picked in the category list and every stamp in it, after asking, **No** by default: `Delete the collection "Night sky" and the 4 stamps in it? They go to the trash.`, or for an empty one `Delete the empty collection "Night sky"? It goes to the trash.` When a bundled category has the same name, the box adds that its bundled stamps stay.

Pick the collection in the category list first; with **All** or a bundled category picked, the status bar says so and nothing changes.

### Adding stamps to a collection

- **From the canvas.** Select the part, or have it floating, and choose **Selection > Save to Library...** with the collection's name as the category ([Save to Library](#save-to-library)).
- **From a stamp in the Library**, bundled or yours. Pick it and choose **Add to Collection...**. A box asks which collection; type a new name to make one first. The stamp is copied byte for byte, with the collection as its category.
- **From `.ans` files.** **Add Files to Collection...** takes the files picked in a file dialog, and **Add Folder to Collection...** a folder's own `.ans` files (not its subfolders', nor hidden ones whose names start with `.`). Both then ask for the collection, as **Add to Collection...** does. A file with a sidecar beside it is copied as a stamp; a plain `.ans` is named from its SAUCE title, else its file name, and trimmed of blank columns on the right and blank rows below.

A collection holds one stamp of each name: a name it has already is refused, and the stamp isn't added. A batch adds what it can; the status bar says how many were added and refused, `Added 3 stamps to the collection "Night sky"; 1 file refused`, and a box lists each refused file with its reason. A batch that takes more than half a second shows its progress, and **Cancel** stops it between files.

### Changing a stamp's name, category or tags

Pick a stamp of yours and choose **Edit Stamp...**: the **Save to Library** dialog's **Name**, **Category** and **Tags**, filled in from the stamp. **OK** changes them.

- A new name changes the stamp's SAUCE title; the files keep their names.
- A collection's name as the category moves the stamp into that collection's folder. Any other category takes a stamp out of its collection, to the top of the user library; a stamp already at the top stays there.
- A moved stamp's files take the new name's file name.

To change the art, place the stamp, change it, and save it again with **Save to Library...** under the same name and category, which asks to replace it. The art is the float as it stands: a resize, flip or turn is saved too.

### Removing a stamp

Pick a stamp of yours and choose **Remove Stamp...**, or press <kbd>Delete</kbd>. It asks, **No** by default: `Remove the stamp Pine (…/pine.ans)? It goes to the trash.`

### The trash

Removed stamps and deleted collections go to the system's trash. Where the trash can't take them, nothing is removed, and a second box asks whether to delete them permanently, **No** by default; only **Yes** deletes them, and that can't be undone.

### Stamps outside a collection

Stamps saved with a category that names no collection go at the top of the user library, as they always have. They show in the category list by their category, and **Edit Stamp...** and **Remove Stamp...** work on them; the collection commands don't, as their category isn't a collection.

### Folders and sharing

The user library is read with every folder in it, a collection's or not. A symbolic link to a folder isn't followed (*symbolic link to a folder, not followed* under **Skipped files**); copy the folder in.

To share a collection, copy its folder into someone else's user library and press **Refresh**, or give them the files to add with **Add Folder to Collection...**. Check them first with `blockwright-cli library check <dir>` ([CLI](14-cli.md#library)).

Copying a stamp's `.ans` and `.json` into the user library by hand works too. An `.ans` without a sidecar isn't a stamp there; the **Skipped files** tooltip says *no sidecar*, or *.ans has no SAUCE record (the title is the stamp's name)* when it has no SAUCE record. A hand-written sidecar has to give the widest row's IRC bytes exactly. `blockwright-cli library check <dir>` says what is wrong with each file, such as *sidecar says the widest row is 0 IRC bytes; the art's is 52*.

## Where stamps are kept

A stamp is two files side by side with the same name:

- **`<name>.ans`**: the cells, in CP437 with a SAUCE record whose title is the stamp's name ([File formats](13-file-formats.md)). A stamp with characters CP437 can't write is saved as UTF-8.
- **`<name>.json`**: the category, the tags, the widest IRC row in bytes, and a frame's or band's insets.

The category comes from the sidecar, not the folder.

**A collection is a folder** in the user library, named from the collection's name as a stamp's file is (below): **Night sky** is `night-sky/`. A name Windows keeps for a device (`con`, `prn`, `aux`, `nul`, `com1` to `com9`, `lpt1` to `lpt9`) gets a `-` after it: `con-/`. The folder holds the collection's stamps and a `.collection` file with its name, one line, so an empty collection keeps its name. A folder copied in without one is named after the category its stamps share, else after the folder.

The file name is the stamp's name in lower case, A to Z and 0 to 9, each run of other characters a `-`, at most 48 characters: **Pine (night)** is `pine-night.ans`. A name with no letter or digit is spelt in code points: **♥** is `u2665.ans`. A different name that makes the same file name, such as **pine night**, is saved as `pine-night-2.ans`, then `-3`.

| Library | Where | Written by Blockwright |
|---|---|---|
| Bundled | `share/blockwright/library` beside the installed program, or `$BLOCKWRIGHT_BUNDLED_LIBRARY` | Never |
| User | `$BLOCKWRIGHT_USER_LIBRARY` if it is set; otherwise `Blockwright/library` in the system's data folder: `~/.local/share/Blockwright/library` on Linux (or under `$XDG_DATA_HOME`), `~/Library/Application Support/Blockwright/library` on macOS, `AppData\Local\Blockwright\library` in the user's folder on Windows | **Save to Library**, **Save as Frame Style**, **Save as Preset**, and the collection commands |

The user library folder is made the first time something is saved to it.

`blockwright-cli library list` prints both libraries, your collections first; `library check <dir>` checks a folder's files and IRC row widths; `library new`, `rename`, `delete`, `add`, `edit` and `remove` do what the collection commands do ([CLI](14-cli.md#library)).

## Limits

- **Size.** A stamp is at most 400 columns by 5000 rows, and can't be all blank.
- **Name.** 1 to 35 characters, all in CP437.
- **Category and tags.** A category can't be empty; a tag can't hold a comma. Neither can hold a control character.
- **Collection name.** Not empty, no control character, at most 128 bytes in UTF-8.
- **IRC.** **Save to Library** doesn't check a stamp's rows against the IRC budget; `blockwright-cli library check` does.
- **Placing.** The float keeps at least one cell on the canvas; cells off the canvas are lost when it lands.
- **Managing.** Files and folders dropped on the dock aren't added; use **Add Files to Collection...** or **Add Folder to Collection...**. There is no export command for a collection; copy its folder ([Folders and sharing](#folders-and-sharing)).
- **Steps files.** A steps file's `placeStamp` and `saveToLibrary` steps place and save a stamp ([replay](14-cli.md#replay)), but none runs a collection command.
