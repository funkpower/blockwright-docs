# Blockwright tutorial — plan

## 1. Who it is for

Someone who has never made ANSI art and has never heard of CP437. By the end they can draw, shade and light a piece in Blockwright, check it at 1× against the shading and craft rules, and post it to an IRC channel inside the byte budget.

Every lesson has the same shape:

1. **Goal**: one sentence, and the finished sample at 1× and 2×.
2. **The idea**: the concept, with one picture.
3. **Do it**: numbered steps in Blockwright, each with the key or click and a picture of the canvas after it.
4. **Check it**: what goes wrong and how it looks (a dotted diagonal, a speck, a skipped rung), from the craft rules.
5. **Try it**: a short exercise with a starting `.ans` to download.

## 2. Curriculum

Status is against Blockwright's `main` on 2026-10-23 (`e721809`). Issue and PR numbers are on `funkpower/blockwright`.

### Track A: the tool

| # | Lesson | Covers | Status |
|---|---|---|---|
| 01 | What ANSI art is | Cells, CP437 glyphs, 16 colours, foreground and background, 80 columns, reading a piece at 1× | Ready to write (concepts; the 1× preview dock is in) |
| 02 | Your first piece | Keyboard mode, F-key glyph sets (Ctrl+, Ctrl+. Ctrl+/), the pen (Ctrl+arrows, Ctrl+D), undo, Save, the SAUCE dialog | Ready to write; screenshots wait for Phase 2c |
| 03 | Pixels with half blocks | Why ▀▄█ make two pixels a cell; half-block brush, 4- vs 8-connected pencil, line, rectangle, ellipse, Filled Shapes, fill, eyedropper; iCE colours and bright backgrounds | Ready to write; screenshots wait for 2c |
| 04 | Shading: the ladder | ░▒▓ as rungs between two colours, ramps (fire, sunset, ice, steel, skin), the shade brush, the ramp shade brush, strength, pressure, alpha lock | Ready to write; screenshots wait for 2c |
| 05 | Shading: forms and falloff | Form shading (dome, cylinder, plane), soft falloff, ramp gradient tool, blend/smudge, despeckle | Form, falloff, despeckle in PR #49; gradient #19; blend #9 |
| 06 | Light | Choosing a light direction, the rim light brush (Ctrl+Shift+L) and its eight compass points, form shading's light, highlights and glints; where the rim light can't help (counters, thin bars, canvas edges) | Rim light merged; form light in PR #49 |
| 07 | Detail | Outline brush, texture stamps, glyph spray, clone stamp, symmetry: mirror X/Y, both, radial 2–8 | Symmetry merged; outline PR #55; stamps, spray, clone #10 |
| 08 | Composing a scene | Selections, move, flip, rotate, paste modes (normal, transparent, under), guides, reference image, Library stamps, Scene Starter | Selections, guides, reference merged; Library is Phase 2c (not yet filed); Scene Starter Phase 5 |
| 09 | Layers and projects | Layer kinds (cells, pixels, text, generator, reference), compositing, the project file, snapshots | Phase 3 (#11, #12, #13) |
| 10 | Letters and text | Lettering by hand, letters that misread at 1× (C/G, R/A, 0/D), TDF text layers | Hand lettering ready to write; TDF #18 |
| 11 | Made for IRC | The 407-byte line budget, trailing black and blank rows, glyphs CP437 can't hold, `export --irc`, the row meter, IRC view, lint panel, publish | CLI export merged; editor side Phase 4 (#14, #15, #16) |
| 12 | Scripts and generators | Generator layers, parameter forms, smart prefabs, the headless CLI | Phase 5 (#17); CLI `render`, `convert`, `export`, `shade` merged |

### Track B: projects

Whole pieces built from the Track A skills: a night scene (sky, moon, stars, tree lines), a face, a figure, a building, an object, an icon, a lettered logo. Written after Track A lessons 01–08.

### Reference pages

- **Shortcuts:** every action and its key, generated from the app (see §3), not typed by hand.
- **Is it done?** The craft rules as a page a beginner can run against their own piece.
- **Install:** per platform, after Blockwright's Phase 6.

## 3. What the samples need from Blockwright

Findings from reading Blockwright's `PLAN.md` and its CLI on 2026-10-23.

1. **Step-by-step images need a headless stroke runner.** `blockwright-cli` has `render`, `convert`, `export --irc` and `shade` (one ramp pass over a box). A lesson needs the canvas after each step of a stroke, made the same way every time. The brushes and shape tools are core functions (`brush.h`, `halfblock.h`, `shapes.h`, `brushes/detail.h`), so a `blockwright-cli replay <steps.json>` that applies tool strokes and writes an `.ans` per step is a small wrapper. Without it the step images are hand-saved from the GUI and drift as the tools change.
2. **Screenshots of the window wait for Phase 2c.** 2c replaces the Brush dock with a toolbox, Tool Options and a glyph bar, so any screenshot taken before it is redone. Grabbing widgets under `QT_QPA_PLATFORM=offscreen` would make them reproducible.
3. **The shortcut page needs a dump.** Blockwright already tests that no two actions share a shortcut, so it enumerates them; a `--list-actions` (JSON: menu, name, shortcut) would let the page be generated.
4. **Rendering is ready.** `render --scale 2` gives the 2× view; `export --irc` gives each line's byte count.
5. **Before/after toggles** are the one place JavaScript would help. `<details>` or two images side by side do without it.

## 4. Build and deploy

- Lessons are Markdown in `lessons/`; a small build script turns them and the rendered samples into `site/`. The script and its Markdown library are chosen when lesson 01 is written.
- `scripts/deploy` copies `site/` to `$BW_TUTORIAL_DEST`, the web root behind <https://lrh.pumpin.online/blockwright/>.

## 5. Open questions

- **Search engines:** the host sends `noindex` on every page and answers the configured crawlers with a pointer to the clip mirror. A tutorial probably wants to be found; that needs its own rule on the host.
- **Licence** for the lesson text and samples (CC BY-SA 4.0 would match the bundled font).
- **When to start:** lessons 01–04 could be written now against the merged tools, with screenshots after 2c, or all of Track A after Phase 5.
