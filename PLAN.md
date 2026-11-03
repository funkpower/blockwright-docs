# Blockwright docs — plan

## 1. What it is

The documentation for Blockwright, in two parts:

- **Tutorials** teach someone who has never made ANSI art and has never heard of CP437. By the end they can draw, shade and light a piece, check it at 1× against the shading and craft rules, and post it to an IRC channel inside the byte budget.
- **The manual** describes everything the app does: every menu, dock, tool and option, the CLI, the file formats, the shortcuts. A reader who knows what they want looks it up here.

Tutorials link to the manual for detail; the manual links to the tutorial that teaches a feature. Neither repeats the other.

Every tutorial has the same shape:

1. **Goal**: one sentence, and the finished sample at 1× (and at 2× when it is small enough to fit the page at 2×).
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
| 01 | What ANSI art is | Cells, CP437 glyphs, 16 colours, foreground and background, 80 columns, reading a piece at 1× | Written, checked against `c44974c` |
| 02 | Your first piece | Keyboard mode, F-key glyph sets (Ctrl+, Ctrl+. Ctrl+/), the pen (Ctrl+arrows, Ctrl+D), undo, Save, the SAUCE dialog | Written, checked against `c44974c`; no window pictures yet (the app has no `--screenshot` at `c44974c`) |
| 03 | Pixels with half blocks | Why ▀▄█ make two pixels a cell; half-block brush, 4- vs 8-connected pencil, line, rectangle, ellipse, Filled Shapes, fill, eyedropper; iCE colours and bright backgrounds | Written, checked against `c44974c`; window screenshots wait for #295 |
| 04 | Shading: the ladder | ░▒▓ as rungs between two colours, ramps (fire, sunset, ice, steel, skin), the shade brush, the ramp shade brush, strength, pressure, alpha lock | Ready to write; screenshots wait for 2c; step images wait for #208 |
| 05 | Shading: forms and falloff | Form shading (dome, cylinder, plane), soft falloff, ramp gradient tool, blend/smudge, despeckle | Form, falloff, despeckle in PR #49; gradient #19; blend #9; step images wait for #208 |
| 06 | Light | Choosing a light direction, the rim light brush (Ctrl+Shift+L) and its eight compass points, form shading's light, highlights and glints; where the rim light can't help (counters, thin bars, canvas edges) | Rim light merged; form light in PR #49; step images wait for #208 |
| 07 | Detail | Outline brush, texture stamps, glyph spray, clone stamp, symmetry: mirror X/Y, both, radial 2–8 | Symmetry merged; outline PR #55; stamps, spray, clone #10; step images wait for #208 |
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
| The window | §11 workspace layout, §4 renderer (zoom, 1× preview) | Written, checked against `c44974c`; window screenshots wait for `blockwright --screenshot` |
| Keyboard mode | §4 keyboard mode | Written, checked against `c44974c` |
| Tools | §4 drawing tools, §10 brushes | Merged tools ready; one section per tool added as each lands |
| Selections | §4 selections | Ready |
| Symmetry | §4 mirror mode, §10 symmetry | Ready |
| Layers | §5 | Phase 3 |
| Library | §12 | 2c (stamps), Phase 5 (prefabs, Scene Starter) |
| Colour | §4 SAUCE/iCE, palette; Phase 8 24-bit | Written, checked against `c44974c`; 24-bit covers reading only (drawing in 24-bit is Phase 8) |
| IRC | §8 IRC text, §9 | Written, checked against `c44974c` |
| Lint | §10 ladder lint, Phase 4 lint panel | Written, checked against `c44974c` |
| Generators | §7 | Phase 5 |
| File formats | §6, §8 | Written, checked against `c44974c` |
| CLI | `blockwright-cli --help` | Written, checked against `c44974c`; its full help is generated (§4) |
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

- Pages are Markdown in `tutorials/` and `manual/`, plus the home page `index.md` and an `index.md` per section. `scripts/build` turns them into `site/`: one Python 3 script on [Python-Markdown](https://python-markdown.github.io/) (the distribution's package: `python-markdown` on Arch, `python3-markdown` on Debian and Ubuntu, `python3-markdown` on Fedora), with the `meta`, `extra`, `toc` and `sane_lists` extensions. No site generator, no JavaScript, no network. `site/` is build output and isn't tracked.
- **Why this:** pages stay plain Markdown that reads on the forge as it is; the only dependency is a packaged library; the output is static HTML that works from a web root, a subdirectory or a file browser, which is also what the in-app help (Blockwright #210) needs.
- **Publishing a page:** a page carries a meta block. `Title:` names it in the lists (else its first heading). `Checked: Blockwright 0.1.0 (c44974c)` says which build it was checked against and publishes it; a page without `Checked:` is a stub, listed as "not written yet", and a link to a stub fails the build.
- **Pictures of pieces:** `![alt](../samples/<tutorial>/<file>.ans "2x")` renders the `.ans` with `blockwright-cli render --scale 2` (the title is the scale, `1x` to `8x`; none means 1×), puts the PNG in its place, links it to the `.ans`, and copies the `.ans` into the site. Pictures are never edited by hand.
- **Other files:** any other relative link or image (a `.png`, an `.ans` no page draws) names a file in the repo, which the build copies into the site at the same path.
- **Generated parts:** `<!-- generated: cli-help -->` is replaced by `blockwright-cli --help`; `<!-- list: tutorials -->` and `<!-- list: manual -->` by the section's pages in order. A marker goes at the start of a line of its own, in column 0: not indented, not in a list item or blockquote. It is written exactly as shown: lowercase, single spaces. The build replaces markers inside Python-Markdown, after it has set fenced code aside, so a marker is left as written exactly where Markdown shows it as code (a closed fence, an indented block), and a page can show one. A marker comment that is still in a page's HTML fails the build, so a marker is never dropped silently: one in the wrong place with the column-0 rule in the message, and a misspelled one (any `<!-- generated:` or `<!-- list:` comment, in any case, that isn't one of the three) with the three markers in the message.
- **Checks:** the build fails on a link to a missing page or to a stub, a `#fragment` the target page has no id for, a link or image path that leaves the repo (symlinks included) or resolves into `.git/` or `site/`, a link to a missing file, a missing sample, a sample the CLI refuses or a render that writes no picture, a marker left as a comment, and any relative link or image in the output that doesn't resolve.
- **Tests:** `scripts/test-build` runs the build and `scripts/deploy` against scratch copies of the repo, one scenario each for: the repo as it is; the allow-all `robots.txt` in `site/` and in `--out`, with no robots meta tag; `--out` refused inside the repo, around the repo, on a foreign directory, on a built site with a file added, and on a file, and accepted on an empty directory and after a failed build; a linked `.png` and `.ans` copied; a link to a missing file, to a file outside the repo directly and through a symlink, to `.git/` directly and through a symlink, and an `.ans` image through a symlink into `.git/`; a link to a stub and to a missing page; a missing sample, an `.ans` the CLI rejects, a CLI whose render exits 1, and one that exits 0 without a picture; a missing `#fragment` on another page and on the same page, and good ones; an `.ans` image outside the repo; markers in fenced and indented code shown, a marker after a closed fence, after an unclosed fence, between fences indented two spaces and after a longer closing fence replaced, and a marker inside a paragraph, one indented two spaces and one in a list item refused with the column-0 rule in the message, and misspelled markers in column 0 (spacing, case, an unknown name) refused with the accepted markers in the message; and for `scripts/deploy`, which runs on a stand-in `site/` with a stand-in ssh that logs its arguments and runs the rsync server in a scratch directory (no host is contacted): a local path, `./a:b` and an absolute path holding a colon copied locally with their parents made and no ssh, `host:path` and `user@host:path` sent to the path as written with its missing parent made, `host:` and `user@host:` refused before ssh runs, and the manifest neither copied nor deleted, locally and remotely, while a stale page is deleted. `--deploy FILE` runs those scenarios against another version of the script. Cases it doesn't run include a missing `--cli`, the `--out` symlink and manifest-forging cases, and a real remote host.
- **The output directory:** the build clears it first, so it only builds into a new or empty directory, or one holding exactly what a previous build wrote: each build leaves `.blockwright-docs-manifest` there, listing its files, and `scripts/deploy` doesn't copy it. Any other directory, any output inside the repo but `site/`, and any output that contains the repo are refused.
- **Search engines:** the build writes a `robots.txt` that lets crawlers fetch everything, and pages carry no robots meta tag; `ROBOTS` at the top of `scripts/build` would set one on every page, and is empty (see §7).
- **Which CLI:** `--cli PATH`, else `$BLOCKWRIGHT_CLI`, else `blockwright-cli-dev`, else `blockwright-cli` on `PATH`. The build prints the version it used; a page's `Checked:` should name that version.
- **Reproducible samples:** until `blockwright-cli replay` (Blockwright #208) exists, a tutorial's step files can be written by a `make.py` in its samples folder with `scripts/ansi.py`, a small cell canvas that writes `.ans` with SAUCE. Each step file is the canvas the step leaves, made the same way every time. This is for the concept tutorials only (see §7).
- Links between pages are relative, so the same `site/` works at a domain root and in a subdirectory.
- Site layout: `/` (home: what Blockwright is, install, start here), `/tutorials/…`, `/manual/…`, at the domain root of <https://blockwright-docs.pumpin.online/>.
- **Deploy:** every commit to `main` deploys within a few minutes. The maintainer's deploy timer on the dev machine checks `main` every two minutes, builds it with the installed dev CLI into a directory of its own and copies it to the web root behind <https://blockwright-docs.pumpin.online/>; it also redeploys when the dev CLI changes, so the pictures follow the renderer. By hand: `scripts/build`, then `scripts/deploy`, which copies `site/` to `$BW_DOCS_DEST`, a local directory or an rsync destination on another host (`host:path`; `RSYNC_RSH` sets the ssh command). A remote path means what it means to rsync, relative to the login directory unless it starts with `/`; an empty one (`host:`) is refused, since `--delete` would empty the login directory, and `host:.` says so on purpose. Missing parent directories are made on both sides: `mkdir -p` locally, `--mkpath` remotely, which needs rsync 3.2.3 or later at both ends.

## 7. Decisions

- **Search engines:** the site has its own domain, <https://blockwright-docs.pumpin.online/>, and is indexed (docs#1): `ROBOTS = ""` in `scripts/build`, a `robots.txt` that allows everything, and no `X-Robots-Tag` from the host. Its old address, lrh.pumpin.online/blockwright/, where it was `noindex`, redirects permanently to the same page on the new domain.
- **Licence:** the text and the sample art are funkpower's, under CC BY-SA 4.0 (the licence of the bundled font too), unless a file says otherwise. `LICENSE` holds the legal code; the README and every page's footer credit it.
- **Versions:** one set of docs, for the latest Blockwright. No per-release docs until packages ship; then this is decided again.
- **Reproducible samples:** `make.py` step images are fine for the concept tutorials, 01–03, 10 and 11, where a step is typing or placing cells. The brush tutorials, 04–07, show what a brush does to the canvas, so their step images wait for `blockwright-cli replay` (Blockwright #208) and are never imitated with `scripts/ansi.py`.
