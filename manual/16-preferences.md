Title: Preferences
Checked: Blockwright 0.1.0 (12ee9ef)

# Preferences

**Edit > Preferences...** holds your own settings: the TheDraw fonts folder, the target for new documents, and the keyboard shortcuts. On macOS it is in the application menu.

It has no shortcut by default, because <kbd>Ctrl</kbd>+<kbd>,</kbd> is **Glyphs > Previous Set**; the **Shortcuts** tab can give it one. On a Mac the <kbd>Ctrl</kbd> keys on this page are <kbd>Cmd</kbd>.

**OK** keeps every tab's changes; **Cancel** drops them all. Nothing takes effect before **OK**.

## Fonts

The **Fonts** tab sets the folder the **Text** tool's face picker offers TheDraw fonts (`.tdf`) from. Blockwright ships none; with no folder, text layers can use the three bundled faces and the fonts a project already holds. [Letters and text](../tutorials/10-letters-and-text.md#text-layers-and-thedraw-fonts) uses them.

| Part | What it does |
|---|---|
| **Fonts folder** | The folder's path. Type one and leave the field, or use **Browse...**. Empty, the field reads `None` |
| **Browse...** | Picks the folder in a folder dialog |
| **Clear** | Sets no folder |
| `Default: ~/tdfiglet/fonts` | Shown under the field while the folder is the default (below) |
| The summary | How many fonts the folder holds and how many files couldn't be read: `1 TheDraw font; 1 file not read` |
| The list | One line per font, its name and then its file, relative to the folder; then a line per file that couldn't be read, with the reason: `Not read: broken.tdf: TheDraw font, byte 0: no TheDraw font signature` |

**The default.** Until you set a folder, Blockwright uses `~/tdfiglet/fonts` if it exists. Make it later and Blockwright reads it at the next start. **Clear** stores "no folder" as your choice: `~/tdfiglet/fonts` isn't read again until you pick a folder.

**What is read.** Every file ending `.tdf`, in any case, in the folder and its subfolders. Links to folders aren't followed. A file with several fonts lists each; an exact copy of a file already read adds nothing.

A broken file is listed as not read. While reading, the summary says `Scanning fonts…`; with no folder, `No fonts folder: text layers can use the bundled faces and the fonts a project holds.`

**When it takes effect.** The tab reads the folder in the background when the dialog opens, when you leave a changed field, and after **Browse...** or **Clear**. **OK** saves the folder and reads it again, so fonts copied in since are offered once that read ends. Blockwright also reads it at each start.

A text layer already in a TheDraw font keeps a copy of the font in its project ([Projects (.bwp)](13-file-formats.md#projects-bwp)), so moving or clearing the folder doesn't change it.

## Documents

The **Documents** tab has one setting, **Target for new documents**:

| Choice | A new document is made for |
|---|---|
| **ANSI (.ans)** (the default) | The 16 colours an `.ans` holds |
| **IRC** | mIRC's 99 colours |

**When it takes effect.** At the next new document: **File > New**, the start screen's **New**, the canvas left when the start screen closes without a pick (from startup or **File > Start Screen...**), and the first canvas when Blockwright starts without the start screen. A new IRC document starts in UTF-8: the status bar reads `IRC UTF-8` where an ANSI one reads `ANSI CP437`.

For the open document, use **Format > Target**; it is part of the document and **Edit > Undo** takes it back. What each target means is in [IRC](10-irc.md) and [Palette, iCE colours and 24-bit colour](09-colour.md).

## Shortcuts

The **Shortcuts** tab lists every action under its menu or dock, with its key, and a **Search by action or key** field. Click an action, then press the new key in **Key**.

**No Key**, **Default** and **Reset All** work as in [Changing a shortcut](15-shortcuts.md#changing-a-shortcut). An action whose key you changed shows in italics.

A key keyboard mode types or edits with is refused, as is one another action has. The reason shows under the field: `W can't be a shortcut: Keyboard mode types or edits with it; add Ctrl.` or `Ctrl+Shift+Y can't be a shortcut: Ctrl+Shift+Y is already the key for Glyph Spray.`

New keys work when **OK** closes the dialog; an open **Help > Keyboard Shortcuts** sheet shows them at once. The default keys are on the [Shortcuts](15-shortcuts.md#every-action) page.

## Where the settings are kept

These settings, and everything else Blockwright remembers between runs, are in one settings store:

| System | Where |
|---|---|
| Linux | `~/.config/Blockwright/Blockwright.conf`, or `Blockwright/Blockwright.conf` under `$XDG_CONFIG_HOME` when that is set |
| macOS | `~/Library/Preferences/com.blockwright.Blockwright.plist` |
| Windows | The registry key `HKEY_CURRENT_USER\Software\Blockwright\Blockwright` |

On Linux the file is plain text. **OK** with nothing changed leaves it alone, unless it was edited by hand. While IRC is the target or any action has an entry, **OK** rewrites the whole file, and comments and blank lines added by hand are lost.

The **Preferences** entries:

```ini
[document]
defaultTarget=irc

[fonts]
folder=

[shortcuts]
swapColours=Ctrl+Shift+U
```

- `document/defaultTarget` is there only while the target is IRC, as `irc`. Case doesn't matter; missing or any value but `irc` or `ansi` means ANSI. **OK** normalises a hand-edited value even with nothing changed: `IRC` becomes `irc`, and `ansi` or an unknown value is removed.
- `fonts/folder` is the folder's path, or empty after **Clear**. **OK** writes it only after you change the field or use **Browse...** or **Clear**, and it stays from then on. Missing means the default, `~/tdfiglet/fonts` if it exists.
- `shortcuts/<action>` holds the keys of an action you changed, by its id (`swapColours` is **Colours > Swap Colours**). Setting an action back to its default removes the entry.

At start, Blockwright ignores a key the tab would refuse and a key an earlier entry already has. An action loses any default key an entry gives another action. **OK** then writes what every action has, even with nothing changed: with `swapColours=Ctrl+Shift+Y`, **Tools > Glyph Spray**'s default key, it adds `sprayTool=`.

The same store holds the window's size and dock layout, the recent files, whether the start screen shows, the pen, the glyph set, the tools' last settings and your favourite faces. Nothing resets all of it; **Reset All** on the **Shortcuts** tab resets the keys only.
