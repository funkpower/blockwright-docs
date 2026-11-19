Title: Keyboard mode, F-key glyph sets and the pen
Checked: Blockwright 0.1.1 (1347435)

# Keyboard mode, F-key glyph sets and the pen

In keyboard mode a key puts a glyph in the cell under the cursor and moves the cursor on. The F-keys type block, shade and line glyphs from 21 sets (16 in a CP437 document under the ANSI target). Everything is typed in the pen's two colours.

[What ANSI art is](../tutorials/01-what-ansi-art-is.md) types its first word this way.

## Keyboard mode

Blockwright starts in **Tools > Keyboard** (<kbd>Ctrl</kbd>+<kbd>K</kbd>). Keys type in the other tools too, except keys a tool uses itself:

- the select tool takes the arrows, <kbd>Enter</kbd>, <kbd>Esc</kbd> and <kbd>Delete</kbd> while there is a selection;
- the glyph brush takes the F-keys to pick its glyph;
- the text tool types into its own text layer.

Click a cell to put the cursor there. The cursor is a frame around one cell, or both cells of a wide character.

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

A cleared cell is transparent, except on a bottom Cells layer, where it is a space in grey on black.

Typing on the last column leaves the cursor there. <kbd>Backspace</kbd> then clears that last cell, until the cursor moves.

Each key is one undo step.

### Which keys type

A key types when it gives a printable character, unless <kbd>Ctrl</kbd> (or <kbd>Meta</kbd>) is held without <kbd>Alt</kbd>: those chords are shortcuts. Characters made with <kbd>AltGr</kbd> or <kbd>Option</kbd>, and text from an input method, type.

In a CP437 document under the ANSI target, a cell holds only glyphs CP437 has. A letter and a combining accent are joined first, so `e` and a combining acute type `é`.

A character with no CP437 glyph, such as `€` or an emoji, isn't typed, and the status bar says `€ has no CP437 code; not typed (target: ANSI, CP437)`. If an input method sends several characters and any can't be typed, none is.

Five CP437 glyphs can't be typed there either: `○ ◙ ♪ → ←`. Their bytes, 9, 10, 13, 26 and 27, are control codes an `.ans` reader acts on. The status bar names the byte: `→ is CP437 0x1A, which .ans reads as SUB; not typed (target: ANSI, CP437)`.

Under the IRC target, and in a UTF-8 document under either target (the documents that offer [sets 17 to 21](#sets-17-to-21)), any character but a control code types, including `€`, the five glyphs above and wide characters such as `中`.

- A wide character takes two cells and moves the cursor two. On the last column it isn't typed: `中 would start on the last column; dropped`.
- <kbd>Backspace</kbd> and <kbd>Delete</kbd> clear both of its cells.
- A combining accent typed on its own joins the character left of the cursor.

### Where the glyphs go

Typing goes into the active layer. Nothing is typed on a hidden or locked layer, a generator, reference or live text layer. A pixels layer takes only spaces and `█ ▀ ▄`.

With **Edit > Mirror Mode** (<kbd>Ctrl</kbd>+<kbd>M</kbd>) on and **Edit > Symmetry > Mirror X** picked, each glyph is also typed, flipped, in the mirrored column: `┌` on the left gives `┐` on the right. Other symmetry modes don't repeat typing ([Mirror mode and symmetry](06-symmetry.md#typing-and-pasting)).

## The F-key glyph sets

<kbd>F1</kbd> to <kbd>F10</kbd> type the ten glyphs of the current **glyph set**. Sets 1 to 16, as in Moebius and PabloDraw, are offered in every document; sets 17 to 21 hold glyphs CP437 lacks and are offered only in IRC and UTF-8 documents ([Sets 17 to 21](#sets-17-to-21)). Blockwright starts on the set last picked, or on set 6, the shades and half blocks, the first time or when the document doesn't offer the set last picked:

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
| 17 | `▖ ▗ ▘ ▝ ▚ ▞ ▙ ▛ ▜ ▟` |
| 18 | `▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▔ ▕` |
| 19 | `▏ ▎ ▍ ▌ ▋ ▊ ▉ █ ▐ ▕` |
| 20 | `◢ ◣ ◤ ◥ ◆ ◇ ○ ● ★ ☆` |
| 21 | `✦ ✧ ✶ ✷ ✸ ✹ ⋆ ✱ ✺ ❖` |

### Changing the set

| Key or item | What it does |
|---|---|
| **Glyphs > Previous Set**, <kbd>Ctrl</kbd>+<kbd>,</kbd> | The set before; from set 1 it goes round to the last set the document offers, 16, or 21 in an IRC or UTF-8 document. |
| **Glyphs > Next Set**, <kbd>Ctrl</kbd>+<kbd>.</kbd> | The set after; from the last set the document offers it goes round to set 1. |
| **Glyphs > Default Set**, <kbd>Ctrl</kbd>+<kbd>/</kbd> | Back to set 6. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F1</kbd> to <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F10</kbd> | Sets 1 to 10. |
| **Glyphs > Set 1** to **Set 21** | Any set the document offers; each item shows its ten glyphs, and the current one is ticked. Sets 17 to 21 are in the menu only in IRC and UTF-8 documents. |

Sets 11 to 21 have no key; pick them from the **Glyphs** menu or the Glyphs dock, or step to them. To give a set a key, find it under **Glyphs** on the **Shortcuts** tab of **Edit > Preferences...** (on macOS in the application menu).

### Sets 17 to 21

Sets 17 to 21 are offered under the IRC target (**Format > Target > IRC**, no shortcut) and in a UTF-8 document, such as a UTF-8 `.ans`, under either target. A CP437 document under the ANSI target leaves them out of the menu, the dock and stepping. If the set in use stops being offered, the F-keys type set 6.

You can give them a key in any document; in a document that hides the set, the key does nothing.

- The **Shortcuts** tab lists them under **Glyphs**. Where hidden, each row ends "(hidden: offered only in IRC and UTF-8 documents)" in grey.
- A key counts as taken whether or not its set is shown. A key one of these sets has is refused for any other action, with "… is already the key for …", and a key another action has is refused for these sets.
- **Help > Keyboard Shortcuts...** (no shortcut) lists a hidden set that has a key. `blockwright --list-actions` lists all five after set 16, each with `"offeredWhen": "in IRC and UTF-8 documents"`.

Set 21 holds sparkles, stars and asterisks. Unifont draws all but `⋆` 16 pixels wide, so the editor squeezes them into one cell, as it does `★` and `☆`. An IRC client draws each in one column in its own font.

Blockwright doesn't pick sets with <kbd>Alt</kbd>+F-keys as Moebius does, and leaves <kbd>Ctrl</kbd>+F-keys and <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+F-keys alone: the desktop takes many of those keys. On a Mac the <kbd>Ctrl</kbd> keys on this page are <kbd>Cmd</kbd>.

<kbd>Shift</kbd>+<kbd>F1</kbd> is **Help > What's This?**; <kbd>F1</kbd> alone types. <kbd>F11</kbd> and <kbd>F12</kbd> type nothing.

### Seeing the set

- **The status bar** shows the set: `F-keys set 6: ░ ▒ ▓ █ ▀ ▄ ▌ ▐ ■ ·`. Its tooltip lists each F-key's glyph and the keys that change the set.
- **The Glyphs dock**, along the bottom, shows the set as ten cells, beside a list of the sets offered. A cell click does what its F-key does with the active tool. Picking from the list changes the set.

A sign typed in keyboard mode. The frame is set 2 (<kbd>F1</kbd> `╔`, <kbd>F5</kbd> `═`, <kbd>F2</kbd> `╗`, <kbd>F6</kbd> `║`, <kbd>F3</kbd> `╚`, <kbd>F4</kbd> `╝`) in light cyan; the bar is set 6 (<kbd>F1</kbd> `░`, <kbd>F2</kbd> `▒`, <kbd>F3</kbd> `▓`, <kbd>F4</kbd> `█`) in light red; the words are letters in yellow:

![A sign in a light cyan double frame: NOW OPEN in yellow over a light red bar that fades out through the shades at both ends](../samples/manual-03-keyboard-mode/typed.ans "2x")

## The pen

The **pen** is the two colours everything is drawn in: a **foreground** for the glyph and a **background** for the rest of the cell. Blockwright starts with the pen last picked, grey on black the first time.

| Key or item | What it does |
|---|---|
| Left click on a colour in the **Palette** dock | Makes it the foreground. |
| Right click on a colour in the **Palette** dock | Makes it the background. |
| **Colours > Previous Foreground**, <kbd>Ctrl</kbd>+<kbd>↑</kbd> | The colour before the foreground (from 0, black, round to 15, white; under the IRC target, round to 98). |
| **Colours > Next Foreground**, <kbd>Ctrl</kbd>+<kbd>↓</kbd> | The colour after the foreground (from 15 round to 0; under the IRC target, from 15 on to 16 and from 98 round to 0). |
| **Colours > Previous Background**, <kbd>Ctrl</kbd>+<kbd>←</kbd> | The colour before the background. |
| **Colours > Next Background**, <kbd>Ctrl</kbd>+<kbd>→</kbd> | The colour after the background. |
| **Colours > Default Colours**, <kbd>Ctrl</kbd>+<kbd>D</kbd> | Grey on black, with no bold, italic or underline. |
| **Colours > Swap Colours** | Swaps the foreground and the background. No key; set one in **Edit > Preferences... > Shortcuts**. |
| **Tools > Eyedropper**, <kbd>Ctrl</kbd>+<kbd>I</kbd> | Left click takes the foreground, right click the background: on a half-block pixel, the pixel's colour; on any other cell, the cell's foreground or background. |

Under the IRC target the pen also has bold, italic and underline: the **B**, **I** and **U** toggles under the Palette dock's colours. Typing writes them, except on a Pixels layer; **Swap Colours** leaves them alone. Under the ANSI target they are hidden.

The colours are numbered 0 to 15 in the Palette dock's order. Under the IRC target it shows mIRC's 99, 0 to 98, and <kbd>Ctrl</kbd>+arrows step through all of them; with **IRC in 16 Colours** on they step 0 to 15 only. The colours themselves are on [Palette, iCE colours and 24-bit colour](09-colour.md).
