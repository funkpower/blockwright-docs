Title: Keyboard mode, F-key glyph sets and the pen
Checked: Blockwright 0.1.0 (c44974c)

# Keyboard mode, F-key glyph sets and the pen

Keyboard mode types on the canvas the way a text editor types on a page: a key puts a glyph in the cell under the cursor and moves the cursor on. The F-keys type the block, shade and line glyphs that aren't on a keyboard, from 16 sets you switch between. Everything typed is drawn in the pen's two colours.

[What ANSI art is](../tutorials/01-what-ansi-art-is.md) types its first word this way.

## Keyboard mode

**Tools > Keyboard** (<kbd>Ctrl</kbd>+<kbd>K</kbd>) is the tool Blockwright starts with. Keys type in every other tool too, unless the tool uses the key itself: the select tool takes the arrows, <kbd>Enter</kbd>, <kbd>Esc</kbd> and <kbd>Delete</kbd> while there is a selection, the glyph brush takes the F-keys to pick its glyph, and the text tool types into its own text layer.

Click a cell to put the cursor there. The cursor is a frame around one cell, drawn so it shows on any colour.

### Keys

| Key | What it does |
|---|---|
| A letter, digit or other character | Puts that glyph in the cell, in the pen's colours, and moves the cursor one cell right. |
| <kbd>F1</kbd> to <kbd>F10</kbd> | Puts the current glyph set's glyph for that key in the cell, and moves right (see below). <kbd>Shift</kbd>+<kbd>F2</kbd> to <kbd>Shift</kbd>+<kbd>F10</kbd> do the same. |
| <kbd>←</kbd> <kbd>→</kbd> <kbd>↑</kbd> <kbd>↓</kbd> | Move the cursor one cell. It stops at the canvas's edges. |
| <kbd>Home</kbd> / <kbd>End</kbd> | To the first or the last column of the row. |
| <kbd>Enter</kbd> | To the first column of the next row (it stays on the last row at the bottom). |
| <kbd>Backspace</kbd> | Moves the cursor one cell left and clears that cell. On the first column it does nothing. |
| <kbd>Delete</kbd> | Clears the cell under the cursor; the cursor stays. |

A cleared cell is a space in grey on black on the bottom layer, and transparent on any other layer. A pixels layer is the exception: a cell cleared on one is transparent even when it is the bottom layer.

Typing on the last column leaves the cursor on it, past the glyph just typed. <kbd>Backspace</kbd> then clears that last cell rather than the one to its left. Any move of the cursor ends this.

Each key is one step on the undo stack: **Edit > Undo** takes back one glyph at a time.

### Which keys type

A key types when it gives a printable character, unless <kbd>Ctrl</kbd> (or <kbd>Meta</kbd>) is held without <kbd>Alt</kbd>: those chords are shortcuts, such as <kbd>Ctrl</kbd>+<kbd>↑</kbd> for the pen below. So characters made with <kbd>AltGr</kbd>, or with <kbd>Option</kbd> on a Mac, type, and so does text from an input method.

A cell can hold only a glyph CP437 has. Accented letters made of a letter and a combining accent are joined first, so `e` followed by a combining acute types `é`, which CP437 has. A character with no CP437 glyph, such as `€` or an emoji, is not typed, and the status bar says so for a few seconds: `€ has no CP437 glyph; not typed`. When an input method sends several characters at once and any of them can't be typed, none of them is.

Five CP437 glyphs can't be typed either: `○ ◙ ♪ → ←`. Their bytes, 9, 10, 13, 26 and 27, are tab, line feed, carriage return, end of file and escape, which a reader of an `.ans` file acts on rather than draws, so the file can't hold them as glyphs. The status bar gives them the same message as a character CP437 lacks, `→ has no CP437 glyph; not typed`, though CP437 has them.

### Where the glyphs go

Typing goes into the active layer. On a layer that is hidden or locked, a generator layer, a reference layer or a live text layer, nothing is typed. A pixels layer holds only spaces and the blocks `█ ▀ ▄`, so any other glyph typed on one doesn't land.

With **Edit > Mirror Mode** (<kbd>Ctrl</kbd>+<kbd>M</kbd>) on and **Edit > Symmetry > Mirror X** picked, every glyph typed is also put in the mirrored column across the canvas's centre, flipped left to right, so `┌` on the left gives `┐` on the right. The other symmetry modes don't repeat typing.

## The F-key glyph sets

<kbd>F1</kbd> to <kbd>F10</kbd> type the ten glyphs of the current **glyph set**. There are 16 sets, the ones Moebius and PabloDraw have. Set 6, the shades and half blocks, is the one Blockwright starts on each time it starts:

![The 16 glyph sets, a row each under F1 to F10, set 6 on blue: 1 single box lines, 2 double box lines, 3 and 4 mixed single and double lines, 5 crossings and symbols, 6 shades and half blocks, 7 faces, card suits and notes, 8 arrows, 9 to 16 maths, Greek, accented letters and brackets](../samples/manual-03-keyboard-mode/glyph-sets.ans "2x")

| Set | F1 to F10 |
|---|---|
| 1 | `┌ ┐ └ ┘ ─ │ ├ ┤ ┴ ┬` |
| 2 | `╔ ╗ ╚ ╝ ═ ║ ╠ ╣ ╩ ╦` |
| 3 | `╒ ╕ ╘ ╛ ═ │ ╞ ╡ ╧ ╤` |
| 4 | `╓ ╖ ╙ ╜ ─ ║ ╟ ╢ ╨ ╥` |
| 5 | `┼ ╬ ╪ ╫ Φ Φ ¢ £ Ö ∩` |
| 6 | `░ ▒ ▓ █ ▀ ▄ ▌ ▐ ■ ·` |
| 7 | `☺ ☻ ♥ ♦ ♣ ♠ ≡ ♫ ☼`, and a space on F10 |
| 8 | `↑ ↓ ▲ ▼ ► ◄ ↕ ↔ ¶ §` |
| 9 | `« » ≥ ≤ ⌐ ¬ ² ÷ ½ ¼` |
| 10 | `π ± ⌠ ⌡ Ω ¥ Σ ° √ ⁿ` |
| 11 | `α ß Γ σ µ τ δ ∞ φ ε` |
| 12 | `Ç ç Ñ ñ ÿ ƒ ≈ ∙ ¡ ¿` |
| 13 | `â ä à á ª å Ä Å æ Æ` |
| 14 | `ê ë è é É î ï ì í ₧` |
| 15 | `ô ö ò ó º û ü ù ú Ü` |
| 16 | ``/ \ ( ) { } [ ] ` '`` |

### Changing the set

| Key or item | What it does |
|---|---|
| **Glyphs > Previous Set**, <kbd>Ctrl</kbd>+<kbd>,</kbd> | The set before; from set 1 it goes round to set 16. |
| **Glyphs > Next Set**, <kbd>Ctrl</kbd>+<kbd>.</kbd> | The set after; from set 16 it goes round to set 1. |
| **Glyphs > Default Set**, <kbd>Ctrl</kbd>+<kbd>/</kbd> | Back to set 6. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F1</kbd> to <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F10</kbd> | Sets 1 to 10. |
| **Glyphs > Set 1** to **Set 16** | Any set; each item shows its ten glyphs, and the current one is ticked. |

Sets 11 to 16 have no key of their own: pick them from the **Glyphs** menu or the Glyphs dock, or step to them.

Moebius picks sets with <kbd>Alt</kbd>+F-keys. Blockwright doesn't, because the desktop takes many of those keys before an editor sees them (<kbd>Alt</kbd>+<kbd>F4</kbd> closes the window), and leaves <kbd>Ctrl</kbd>+F-keys and <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+F-keys alone for the same reason. On a Mac the <kbd>Ctrl</kbd> keys on this page are <kbd>Cmd</kbd>.

<kbd>Shift</kbd>+<kbd>F1</kbd> is **Help > What's This?**, not a glyph; <kbd>F1</kbd> on its own types. <kbd>F11</kbd> and <kbd>F12</kbd> type nothing.

### Seeing the set

- **The status bar** shows the current set and its glyphs: `F-keys set 6: ░ ▒ ▓ █ ▀ ▄ ▌ ▐ ■ ·`. Its tooltip lists each F-key with its glyph and the keys that change the set.
- **The Glyphs dock**, along the bottom of the window, shows the set as ten cells, with a list of all 16 sets beside them. Clicking a cell does what its F-key does with the active tool: in keyboard mode it types the glyph, with the glyph brush it picks the brush's glyph. Picking a set from the list changes the set.

Here is a sign typed in keyboard mode. The frame is set 2 (<kbd>F1</kbd> `╔`, <kbd>F5</kbd> `═`, <kbd>F2</kbd> `╗`, <kbd>F6</kbd> `║`, <kbd>F3</kbd> `╚`, <kbd>F4</kbd> `╝`) in light cyan; the bar is set 6 (<kbd>F1</kbd> `░`, <kbd>F2</kbd> `▒`, <kbd>F3</kbd> `▓`, <kbd>F4</kbd> `█`) in light red; the words are letters in yellow:

![A sign in a light cyan double frame: NOW OPEN in yellow over a light red bar that fades out through the shades at both ends](../samples/manual-03-keyboard-mode/typed.ans "2x")

## The pen

The **pen** is the two colours everything is drawn in: a **foreground** for the glyph and a **background** for the rest of the cell. Keyboard mode types in both, and the drawing tools use them too. Blockwright starts with grey on black each time it starts.

| Key or item | What it does |
|---|---|
| Left click on a colour in the **Palette** dock | Makes it the foreground. |
| Right click on a colour in the **Palette** dock | Makes it the background. |
| **Colours > Previous Foreground**, <kbd>Ctrl</kbd>+<kbd>↑</kbd> | The colour before the foreground (from 0, black, round to 15, white). |
| **Colours > Next Foreground**, <kbd>Ctrl</kbd>+<kbd>↓</kbd> | The colour after the foreground (from 15 round to 0). |
| **Colours > Previous Background**, <kbd>Ctrl</kbd>+<kbd>←</kbd> | The colour before the background. |
| **Colours > Next Background**, <kbd>Ctrl</kbd>+<kbd>→</kbd> | The colour after the background. |
| **Colours > Default Colours**, <kbd>Ctrl</kbd>+<kbd>D</kbd> | Grey on black. |
| **Colours > Swap Colours** | Swaps the foreground and the background. It has no key; give it one in **Edit > Preferences... > Shortcuts**. |
| **Tools > Eyedropper**, <kbd>Ctrl</kbd>+<kbd>I</kbd> | On a half-block pixel, a left click makes the pixel's colour the foreground and a right click makes it the background. On any other cell, a left click takes the cell's foreground and a right click its background. |

The colours are numbered 0 to 15, in the order the Palette dock shows them. The Palette dock, its pen swatches and what the colours look like are on [Palette, iCE colours and 24-bit colour](09-colour.md).
