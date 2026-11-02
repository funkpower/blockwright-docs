# Blockwright docs — plan

## 1. What it is

The documentation for Blockwright, in two parts:

- **Tutorials** teach someone who has never made ANSI art and has never heard of CP437. By the end they can draw, shade and light a piece, check it at 1× against the shading and craft rules, and post it to an IRC channel inside the byte budget.
- **The manual** describes everything the app does: every menu, dock, tool and option, the CLI, the file formats, the shortcuts. A reader who knows what they want looks it up here.

Tutorials link to the manual for detail; the manual links to the tutorial that teaches a feature. Neither repeats the other.

Every tutorial has the same shape:

1. **Goal**: one sentence, and the finished sample at 1× and 2×.
2. **The idea**: the concept, with one picture.
3. **Do it**: numbered steps in Blockwright. Each step has the key or click, a picture of the canvas after it, and a window picture of the toolbox, Tool Options and any selection. A step that applies a tool or brush is a before/after pair.
4. **Check it**: what goes wrong and how it looks (a dotted diagonal, a speck, a skipped rung), from the craft rules.
5. **Try it**: a short exercise with a starting `.ans` to download.

Pictures are the point (maintainer, 2026-11-02). Many step-by-step images, before and after every tool and brush, showing what it does and how it is used. For each brush, tutorials 04–07 show:

- its effect on a plain shape;
- each setting run on its own, as a labelled row;
- a 4–8 step worked example on a real subject;
- the common mistake.

Each tutorial ends with one piece built through all its brushes in order, every step pictured (blockwright-docs #3; layers, #2). Pictures are 2× with the 1× linked, and every one comes from a steps file, never hand-saved.

Every manual page lists, per feature: where it is (menu, dock, shortcut), what each option does, its limits, and the tutorial that uses it.

## 2. Tutorials

Status is against Blockwright's `main` on 2026-10-23 (`e721809`). Issue and PR numbers are on `funkpower/blockwright`.

### Track A: the tool

| # | Tutorial | Covers | Status |
|---|---|---|---|
| 01 | What ANSI art is | Cells, CP437 glyphs, 16 colours, foreground and background, 80 columns, reading a piece at 1× | Ready to write (concepts; the 1× preview dock is in) |
| 02 | Your first piece | Keyboard mode, F-key glyph sets (Ctrl+, Ctrl+. Ctrl+/), the pen (Ctrl+arrows, Ctrl+D), undo, Save, the SAUCE dialog | Ready to write; screenshots wait for Phase 2c |
| 03 | Pixels with half blocks | Why ▀▄█ make two pixels a cell; half-block brush, 4- vs 8-connected pencil, line, rectangle, ellipse, Filled Shapes, fill, eyedropper; iCE colours and bright backgrounds | Ready to write; screenshots wait for 2c |
| 04 | Shading: the ladder | ░▒▓ as rungs between two colours, ramps (fire, sunset, ice, steel, skin), the shade brush, the ramp shade brush, strength, pressure, alpha lock | Ready to write; screenshots wait for 2c |
| 05 | Shading: forms and falloff | Form shading (dome, cylinder, plane), soft falloff, ramp gradient tool, blend/smudge, despeckle | Form, falloff, despeckle in PR #49; gradient #19; blend #9 |
| 06 | Light | Choosing a light direction, the rim light brush (Ctrl+Shift+L) and its eight compass points, form shading's light, highlights and glints; where the rim light can't help (counters, thin bars, canvas edges) | Rim light merged; form light in PR #49 |
| 07 | Detail | Outline brush, texture stamps, glyph spray, clone stamp, symmetry: mirror X/Y, both, radial 2–8 | Symmetry merged; outline PR #55; stamps, spray, clone #10 |
| 08 | Composing a scene | Selections, move, flip, rotate, paste modes (normal, transparent, under), guides, reference image, Library stamps, Scene Starter | Selections, guides, reference merged; Library is Phase 2c; Scene Starter Phase 5 |
| 09 | Layers and projects | Layer kinds (cells, pixels, text, generator, reference), compositing, the project file, snapshots | Phase 3 (#11, #12, #13) |
| 10 | Letters and text | Lettering by hand, letters that misread at 1× (C/G, R/A, 0/D), TDF text layers | Hand lettering ready to write; TDF #18 |
| 11 | Made for IRC | The 407-byte line budget, trailing black and blank rows, glyphs CP437 can't hold, `export --irc`, the row meter, IRC view, lint panel, publish | CLI export merged; editor side Phase 4 (#14, #15, #16) |
| 12 | Scripts and generators | Generator layers, parameter forms, smart prefabs, the headless CLI | Phase 5 (#17); CLI `render`, `convert`, `export`, `shade` merged |

### Track B: projects

Whole pieces built from the Track A skills: a night scene (sky, moon, stars, tree lines), a face, a figure, a building, an object, an icon, a lettered logo. Written after Track A tutorials 01–08.

## 3. Manual

One page per area, in `manual/`. Each page is written when its feature is on Blockwright's `main`, and updated by the same change that alters the feature (see §5).

| Page | Source in Blockwright's `PLAN.md` | Status |
|---|---|---|
| Install | Phase 6, packaging | Waits for packages (AUR, Debian/Ubuntu, Fedora) |
| The window | §11 workspace layout, §4 renderer (zoom, 1× preview) | Waits for 2c |
| Keyboard mode | §4 keyboard mode | Ready |
| Tools | §4 drawing tools, §10 brushes | Merged tools ready; one section per tool added as each lands |
| Selections | §4 selections | Ready |
| Symmetry | §4 mirror mode, §10 symmetry | Ready |
| Layers | §5 | Phase 3 |
| Library | §12 | 2c (stamps), Phase 5 (prefabs, Scene Starter) |
| Colour | §4 SAUCE/iCE, palette; Phase 8 24-bit | iCE and palette ready |
| IRC | §8 IRC text, §9 | CLI ready; editor side Phase 4 |
| Lint | §10 ladder lint, Phase 4 lint panel | Rules ready; panel Phase 4 |
| Generators | §7 | Phase 5 |
| File formats | §6, §8 | `.ans`/SAUCE/IRC ready; project format Phase 3; XBIN Phase 6 |
| CLI | `blockwright-cli --help` | Ready; generated (§4) |
| Shortcuts | every action | Generated (§4) |
| Preferences | — | Nothing to document yet |

## 4. What the docs need from Blockwright

Findings from reading Blockwright's `PLAN.md` and its CLI on 2026-10-23.

1. **Step-by-step images need a headless stroke runner.** `blockwright-cli` has `render`, `convert`, `export --irc` and `shade` (one ramp pass over a box). A tutorial needs the canvas after each step of a stroke, made the same way every time. The brushes and shape tools are core functions (`brush.h`, `halfblock.h`, `shapes.h`, `brushes/detail.h`), so a `blockwright-cli replay <steps.json>` that applies tool strokes and writes an `.ans` per step is a small wrapper. Without it the step images are hand-saved from the GUI and drift as the tools change.
2. **The shortcuts page and the menu reference need an action dump.** Blockwright already tests that no two actions share a shortcut, so it enumerates them; a `--list-actions` (JSON: menu, name, shortcut, tooltip) lets both pages be generated.
3. **The CLI page is generated** from `blockwright-cli --help` and each command's help.
4. **Window screenshots come from `blockwright --screenshot <steps.json>`** (funkpower/blockwright#295). It replays the same steps file as `replay` in the main window, offscreen, at a fixed size, style, font and screen, and saves the window, a dock or a crop per step. Phase 2c (toolbox, Tool Options, glyph bar) is in, so the layout is the one to picture.
5. **Rendering is ready.** `render --scale 2` gives the 2× view; `export --irc` gives each line's byte count.
6. **Before/after toggles** are the one place JavaScript would help. `<details>` or two images side by side do without it.

## 5. Keeping the manual current

- A Blockwright PR that adds or changes user-visible behaviour names the manual page it affects; the docs change lands in this repo before or with the merge.
- Generated pages (shortcuts, CLI, menus) are rebuilt from the installed dev build on every docs build, so they can't go stale.
- Each page states the Blockwright version it was checked against.

## 6. Build and deploy

- Pages are Markdown in `tutorials/` and `manual/`; a small build script turns them, the generated pages and the rendered samples into `site/`. The script and its Markdown library are chosen when the first page is written.
- Site layout: `/blockwright/` (home: what Blockwright is, install, start here), `/blockwright/tutorials/…`, `/blockwright/manual/…`.
- `scripts/deploy` copies `site/` to `$BW_DOCS_DEST`, the web root behind <https://lrh.pumpin.online/blockwright/>.

## 7. Open questions

- **Search engines:** the host sends `noindex` on every page and answers the configured crawlers with a pointer to the clip mirror. Docs probably want to be found; that needs its own rule on the host.
- **Licence** for the text and samples (CC BY-SA 4.0 would match the bundled font).
- **When to start:** tutorials 01–04 and the ready manual pages could be written now, with screenshots after 2c, or all of it after Phase 5.
- **Versioned docs:** one manual for the latest release, or one per release once packages ship.
