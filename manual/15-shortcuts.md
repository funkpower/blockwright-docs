Title: Shortcuts
Checked: Blockwright 0.1.0 (6cb21c1)

# Shortcuts

Every action in Blockwright's menus and docks, menu by menu, with the keys it starts with and what it does. Any of them can be given a key. **Help > Keyboard Shortcuts** shows the actions that have a key, with the keys they have now.

Typing keys aren't actions, and nor are the keys a tool takes while you use it (the select tool's arrows, <kbd>Enter</kbd> and <kbd>Esc</kbd>, the glyph brush's F-keys). [Keyboard mode](03-keyboard-mode.md#keys) lists the typing keys and the F-key glyph sets.

## Changing a shortcut

Open **Edit > Preferences** and its **Shortcuts** tab ([Preferences](16-preferences.md#shortcuts)). Pick an action in the list (the search box finds an action by its name or its key), then press the new key in **Key**. **No Key** takes the action's keys away. **Default** gives it its default keys back, but for any of them another action has now: it leaves that key off and names the action that has it under the list. **Reset All** gives every action its default keys back. Nothing changes until you press **OK**.

An action gets one key here: a single key, with any modifiers it needs, and not a modifier on its own. <kbd>Meta</kbd> is the Windows key. The editor refuses these, and says why under the list:

- a key keyboard mode types or edits with:
    - any key but an F-key, unless <kbd>Ctrl</kbd> or <kbd>Meta</kbd> is held;
    - <kbd>F1</kbd> to <kbd>F10</kbd> alone or with <kbd>Shift</kbd>, but for <kbd>Shift</kbd>+<kbd>F1</kbd>;
    - <kbd>Ctrl</kbd> or <kbd>Meta</kbd> with <kbd>Alt</kbd> and a character, as <kbd>Ctrl</kbd>+<kbd>Alt</kbd> is AltGr on Windows;
- a key the desktop takes:
    - <kbd>Alt</kbd> with an F-key;
    - <kbd>Ctrl</kbd> with an F-key, unless <kbd>Shift</kbd> or <kbd>Meta</kbd> is held too;
    - <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd> and <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Backspace</kbd>;
- a key another action already has.

## Every action

<!-- generated: shortcuts -->
