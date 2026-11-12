Title: Preferences
Checked: Blockwright 0.1.0 (6cb21c1)

# Preferences

**Edit > Preferences...** holds the settings that belong to you rather than to a piece: where TheDraw fonts are read from, the target a new document takes, and the keyboard shortcuts. On macOS it is in the application menu. It has no shortcut by default: <kbd>Ctrl</kbd>+<kbd>,</kbd>, the usual key for it, is **Glyphs > Previous Set** in Blockwright. The **Shortcuts** tab can give it a key. On a Mac the <kbd>Ctrl</kbd> keys on this page are <kbd>Cmd</kbd>.

The dialog has three tabs, **Fonts**, **Documents** and **Shortcuts**, and one **OK** and **Cancel** for all of them. **OK** keeps what every tab shows; **Cancel** keeps nothing, from any tab. Nothing a tab changes takes effect before **OK**.

## Fonts

The **Fonts** tab sets the fonts folder: the folder the **Text** tool's face picker offers TheDraw fonts (`.tdf`) from. Blockwright ships no TheDraw fonts; with no folder, text layers can use the three bundled faces and the fonts a project already holds. Using the fonts on a text layer is in [Letters and text](../tutorials/10-letters-and-text.md#text-layers-and-thedraw-fonts).

| Part | What it does |
|---|---|
| **Fonts folder** | The folder's path. Type one and leave the field, or use **Browse...**. Empty, the field reads `None` |
| **Browse...** | Picks the folder in a folder dialog |
| **Clear** | Sets no folder |
| `Default: ~/tdfiglet/fonts` | Shown under the field while the folder is the default (below) |
| The summary | How many fonts the folder holds and how many files couldn't be read: `1 TheDraw font; 1 file not read` |
| The list | One line per font, its name and then its file, relative to the folder; then a line per file that couldn't be read, with the reason: `Not read: broken.tdf: TheDraw font, byte 0: no TheDraw font signature` |

**The default.** Until you set a folder, Blockwright uses `tdfiglet/fonts` in your home folder if that folder exists, and none if it doesn't. **OK** with the field as it opened leaves it that way, so the default follows the folder: make `~/tdfiglet/fonts` later and Blockwright reads it at the next start. **Clear** is different: it keeps "no folder" as your choice, and `~/tdfiglet/fonts` isn't read again, even if it is there, until you pick a folder.

**What is read.** Every file under the folder whose name ends `.tdf`, in any case, subfolders included. A link to a folder isn't followed. A file that holds several fonts lists each of them; a file that is a byte-for-byte copy of one already read adds nothing. A file that isn't a TheDraw font, or is broken, is listed as not read and the rest are still offered. While the folder is read the summary says `Scanning fonts…`; with no folder it says `No fonts folder: text layers can use the bundled faces and the fonts a project holds.`

**When it takes effect.** The tab reads the folder when the dialog opens, when you leave the field after changing it, and after **Browse...** or **Clear**, in the background, so the dialog stays usable. **OK** saves the folder and reads it again, even when it hasn't changed, so fonts copied in since are offered; the face picker has them once that read ends. Blockwright also reads the folder each time it starts. A text layer already set in a TheDraw font doesn't depend on the folder: its project keeps a copy of the font file ([Projects (.bwp)](13-file-formats.md#projects-bwp)), so moving or clearing the folder leaves it as it was.

## Documents

The **Documents** tab has one setting, **Target for new documents**:

| Choice | A new document is made for |
|---|---|
| **ANSI (.ans)** (the default) | The 16 colours an `.ans` holds |
| **IRC** | mIRC's 99 colours |

Its tooltip says the same: "What File > New and a new canvas offer: the 16 colours an .ans holds, or IRC's 99".

**When it takes effect.** At the next new document, not the one that is open: **File > New**, the start screen's **New**, the canvas the start screen makes when you close it without a pick (with <kbd>Esc</kbd>, say), whether it showed at startup or from **File > Start Screen...**, and the first canvas when Blockwright starts without the start screen. A new IRC document starts in UTF-8, so the status bar reads `IRC UTF-8` where an ANSI one reads `ANSI CP437`. To change the target of the open document, use **Format > Target**, which is part of the document and is undone with **Edit > Undo**. What each target means for colours, glyphs and saving is in [IRC](10-irc.md) and [Palette, iCE colours and 24-bit colour](09-colour.md).

## Shortcuts

The **Shortcuts** tab gives any action of the window a different key, or none. It lists every action under its menu or dock, with its key, and a **Search by action or key** field. Click an action, then press the new key in **Key**. **No Key** takes the action's keys away. **Default** gives it its default keys back, but for any of them another action has now: it leaves that key off and names the action that has it under the list. **Reset All** gives every action its default keys back. An action whose key you changed is shown in italics.

A key that keyboard mode types or edits with is refused, and so is one another action already has; the reason is shown under the field: `W can't be a shortcut: Keyboard mode types or edits with it; add Ctrl.`, `Ctrl+Shift+Y can't be a shortcut: Ctrl+Shift+Y is already the key for Glyph Spray.` The new keys work as soon as **OK** closes the dialog, and an open **Help > Keyboard Shortcuts** sheet shows them at once.

Every action's default keys are listed on the [Shortcuts](15-shortcuts.md#every-action) page, and the full rules for which keys can be given are under [Changing a shortcut](15-shortcuts.md#changing-a-shortcut).

## Where the settings are kept

Blockwright keeps these settings, and the other things it remembers between runs, in one settings store of its own:

| System | Where |
|---|---|
| Linux | `~/.config/Blockwright/Blockwright.conf`, or `Blockwright/Blockwright.conf` under `$XDG_CONFIG_HOME` when that is set |
| macOS | `~/Library/Preferences/com.blockwright.Blockwright.plist` |
| Windows | The registry key `HKEY_CURRENT_USER\Software\Blockwright\Blockwright` |

On Linux the file is plain text. **OK** writes each **Preferences** entry by its own rule, below, so **OK** with nothing changed on any tab changes nothing in the file, unless it was edited by hand. While IRC is the target or any action has an entry, though, **OK** writes the whole file again with its entries only, so comments and blank lines added by hand are lost.

The **Preferences** settings are these entries:

```ini
[document]
defaultTarget=irc

[fonts]
folder=

[shortcuts]
swapColours=Ctrl+Shift+U
```

- `document/defaultTarget` is there only while the target is IRC, as `irc`; **OK** with ANSI chosen removes it. The value is read without regard to case, so `IRC` also means IRC; missing, or any value other than `irc` or `ansi`, means ANSI. So **OK** changes a hand-edited value even with nothing changed: `IRC` becomes `irc`, and `ansi` or a value it doesn't know is removed.
- `fonts/folder` is the folder's path, or empty after **Clear**. **OK** writes it only when you changed the field or used **Browse...** or **Clear**, and it stays from then on, even when it names `~/tdfiglet/fonts` or is empty with no such folder. Missing means the default, `~/tdfiglet/fonts` if it exists.
- `shortcuts/<action>` holds the keys of an action you changed, by the action's id (`swapColours` is **Colours > Swap Colours**). An action with no entry has its default keys; setting an action back to its default removes its entry. When Blockwright starts it ignores a kept key the tab would refuse (in an entry edited by hand, say) and a key an earlier entry already has, and an action with no entry goes without any default key an entry has given another action. **OK** writes the keys every action has then, so after such an edit it rewrites, adds or removes entries even with nothing changed: with `swapColours=Ctrl+Shift+Y`, **Tools > Glyph Spray**'s default key, **OK** adds `sprayTool=`; with `swapColours=W`, it removes the entry, because `W` is ignored and **Colours > Swap Colours** has no default key.

The same store holds what Blockwright remembers without asking: the window's size and dock layout, the recent files, whether the start screen shows at startup, the pen's colours, the glyph set, the tools' last settings, your favourite faces, and what was last entered in **Publish to Library** and **Send to WeeChat**. There is no button that resets all of it; **Reset All** on the **Shortcuts** tab resets the keys only.
