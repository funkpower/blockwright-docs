Title: Shortcuts
Checked: Blockwright 0.1.1 (1347435)

# Shortcuts

Every action in the menus and docks, menu by menu, with its default keys and what it does. Any action can be given a key. **Help > Keyboard Shortcuts** shows the actions that have a key now.

Typing keys and the keys a tool takes while you use it (the select tool's arrows, <kbd>Enter</kbd> and <kbd>Esc</kbd>, the glyph brush's F-keys) aren't actions. [Keyboard mode](03-keyboard-mode.md#keys) lists them.

## Changing a shortcut

Open the **Shortcuts** tab of **Edit > Preferences** ([Preferences](16-preferences.md#shortcuts)). Pick an action (the search box finds one by name or key), then press the new key in **Key**.

- **No Key** removes the action's keys.
- **Default** restores its default keys, except any that another action now has; it names that action under the list.
- **Reset All** restores every action's default keys.

Nothing changes until **OK**.

An action gets one key here, with any modifiers, and not a modifier alone. <kbd>Meta</kbd> is the Windows key. The editor refuses these, and says why under the list:

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
