Title: Drawing for NomadNet: Reticulum and Micron pages
Checked: Blockwright 0.1.1 (c0acea0)

# Drawing for NomadNet: Reticulum and Micron pages

NomadNet hosts and shows pages on the Reticulum network. A page is a Micron file, `.mu`. Blockwright draws a piece for one under the Micron target and writes it with **File > Export Micron...**; NomadNet shows it in a terminal.

![Gas-mask operator: a soldier in a khaki helmet and a dark olive gas mask at an early-nineties desk, two putty towers and a monitor seen from behind on the left, his gloved hand on the mouse, his eyes turned back over his shoulder through the round lenses, all in half blocks against a slate wall](../samples/manual-nomadnet/operator.bwp)

*Gas-mask operator*, one of the samples that come with Blockwright (**Help > Samples**), is a Micron page in twelve-bit colour: the project, [operator.bwp](../samples/manual-nomadnet/operator.bwp), and the page it exports, [operator.mu](../samples/manual-nomadnet/operator.mu).

NomadNet details are as in NomadNet 1.5.0; each names the file in NomadNet's source it comes from.

## Reticulum, NomadNet and Micron

- **Reticulum** (`https://reticulum.network/`, source at `https://github.com/markqvist/Reticulum`) is an encrypted mesh networking stack. It runs over LoRa, packet radio, Wi-Fi, serial lines or the internet, and needs no internet connection.
- **NomadNet** (source at `https://github.com/markqvist/NomadNet`) is a messaging program on Reticulum whose **nodes** host pages and files. Its text UI has a browser for those pages. Its README installs it with `pip install nomadnet` and starts it with `nomadnet`.
- **Micron** is NomadNet's markup for pages: text with codes for colour, bold, italic, underline, alignment, links and more. Its guide is in NomadNet: the **Guide** section of the text UI, topic **Micron Markup** (`nomadnet/ui/textui/Guide.py`).

Blockwright writes the part of Micron a picture needs: colours, bold, italic and underline, and when asked, centring and the cache header. It writes no links or other markup.

## Making a page

1. Choose **Format > Target > Micron (NomadNet)** (no shortcut), or set **Micron (NomadNet)** as the target for new documents ([Preferences](16-preferences.md#documents)). The change is one undo step and changes no cell. Under the Micron target:
    - the Palette dock offers mIRC's 99 colours and the **B**, **I** and **U** toggles, and a click on the pen opens the twelve-bit colour picker ([The Micron colour dialog](09-colour.md#the-micron-colour-dialog));
    - the row meter is hidden, as a page has no byte budget ([The row meter](10-irc.md#the-row-meter));
    - the lint leaves out the checks for what IRC drops or pays for: trailing black, blank edge rows and wasted formatting ([Targets](11-lint.md#targets));
    - the status bar reads `Micron`, and a new document made for it writes its `.ans` in UTF-8.
2. Draw.
3. Choose **File > Export Micron...** ([Micron page](13-file-formats.md#micron-page-mu)), or from the command line:

```
$ blockwright-cli export --micron operator.bwp operator.mu
42 lines, 80 columns
```

A piece drawn under another target exports the same way: the target sets what the editor offers, not what the export writes.

The lint under the Micron target notes what an `.ans` of the piece would lose (`ans-loss`), and what the page doesn't write as drawn (`micron-colour`, `micron-glyph`; [Lint](11-lint.md#micron-colour)). Notes leave the piece clean:

```
$ blockwright-cli lint operator.bwp
0,0 ans-loss - note: 3355 cells are in colours an .ans can't hold, saved as the nearest of the 16 (fine for Micron)
clean, 1 note (1 ans-loss), noise 0.0099, iCE on
```

A flat `.ans` takes the target from the command line: `blockwright-cli pack --target micron piece.ans piece.bwp` makes a Micron project of it ([pack, unpack and snapshot](14-cli.md#pack-unpack-and-snapshot)), and `lint --target micron` lints it as one.

## Putting a page on a node

1. Turn node hosting on: `enable_node = yes` under `[node]` in NomadNet's config file, `~/.nomadnetwork/config` (or `~/.config/nomadnetwork/config`, or `/etc/nomadnetwork/config`, when that one exists) (`nomadnet/NomadNetworkApp.py`).
2. Copy the `.mu` into the node's pages folder: `~/.nomadnetwork/storage/pages` by default, or the folder `pages_path` under `[node]` names. `index.mu` is the page a visitor gets first; subfolders are served too (`nomadnet/ui/textui/Guide.py`, "Hosting a Node").
3. Restart NomadNet. It reads the pages folder when it starts, and again every `page_refresh_interval` minutes when that is set under `[node]` (`nomadnet/NomadNetworkApp.py`).

Keep the page's file not executable: NomadNet runs an executable page as a program and serves what it prints (`nomadnet/Node.py`).

## Viewing it

Start `nomadnet` and open its **Network** section. **Node Info** shows the node's address (`Addr`) and a **Browse** button that opens its `index.mu`. Another page is at `<address>:/page/<file>.mu`: press <kbd>Ctrl</kbd>+<kbd>U</kbd> in **Network**, type it and press **Go** (`nomadnet/ui/textui/Network.py`; `Guide.py`, "Hosting a Node").

## What a page shows

- **Colours.** Blockwright writes a colour as three hex digits when each channel is one digit doubled, else in the six-digit truecolour form, so no colour is rounded ([What a page holds](13-file-formats.md#what-a-page-holds)); the Lint dock notes the cells in the second form (`micron-colour`, [Lint](11-lint.md#micron-colour)), and **Colours > Snap to Micron Colours** moves them to the nearest of the 4096 three digits write ([Keeping a page to three-digit codes](09-colour.md#keeping-a-page-to-three-digit-codes)); every code Blockwright writes is tabled in [Colours on a Micron page](09-colour.md#colours-on-a-micron-page). NomadNet's `colormode` under `[textui]` decides what the reader sees: `24bit`, which the config file NomadNet writes sets, shows both forms as written; `256` and `88` show each as the nearest of the terminal's 256 or 88; `16` maps each to one of the terminal's 16 colours by NomadNet's own rule; `monochrome` drops both, so the page shows in the terminal's default colours, keeping bold, underline and italics (`nomadnet/ui/textui/MicronParser.py`, `make_style`).
- **Bold, italic and underline** are kept. **Blink** isn't: a blinking cell is written on its dark background.
- **Glyphs.** Glyphs NomadNet drops are written as `?`. The Lint dock notes them (`micron-glyph`, [Lint](11-lint.md#micron-glyph)) and the export's warning lists them ([What a page doesn't keep](13-file-formats.md#what-a-page-doesnt-keep)).
- **Size.** A page has no byte budget. Every row and column is written, blank ones and trailing black included.
- **Centring and caching.** **Centre the piece on the page** writes each line centred. **Write a page cache header** sets how long a visitor's NomadNet keeps the page; without it NomadNet keeps a page 12 hours, and it reads the header only from the first line (`nomadnet/ui/textui/Browser.py`; `Guide.py`, "Hosting a Node").
- **One flat picture.** The visible layers are merged; layers, SAUCE, notes and snapshots stay in the project.

## Limits

- Blockwright doesn't open a `.mu` file.
- No view shows the page as NomadNet draws it at 256 or 16 colours; the canvas shows it as the `24bit` mode does.
