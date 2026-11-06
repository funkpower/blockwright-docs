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
5. **Try it**: a short exercise with a starting file to download (an `.ans`, or a `.bwp` when it has layers).

Pictures are the point (maintainer, 2026-11-02). Many step-by-step images, before and after every tool and brush, showing what it does and how it is used. For each brush, tutorials 04–07 show:

- its effect on a plain shape;
- each setting run on its own, as a labelled row;
- a 4–8 step worked example on a real subject;
- the common mistake.

Each tutorial ends with one piece built through all its brushes in order, every step pictured (blockwright-docs #3; layers, #2). Pictures are 2× with the 1× linked, and every one comes from a steps file, never hand-saved.

Samples are flat `.ans` only while they are one simple picture, as in tutorials 01 and 03 (maintainer, 2026-11-02). Anything more complicated is a Blockwright project (`.bwp`, Blockwright `PLAN.md` §6), with each part on its own layer the way the reader would build it, so a reader who downloads it can hide a layer and see what it adds. The page shows the composite. How layered samples are made and drawn is in §6 ("Layered samples").

Every manual page lists, per feature: where it is (menu, dock, shortcut), what each option does, its limits, and the tutorial that uses it.

## 2. Tutorials

Status is against Blockwright's `main` on 2026-11-05 (`06fbac5`). Issue and PR numbers are on `funkpower/blockwright`.

### Track A: the tool

| # | Tutorial | Covers | Status |
|---|---|---|---|
| 01 | What ANSI art is | Cells, CP437 glyphs, 16 colours, foreground and background, 80 columns, reading a piece at 1× | Written, checked against `c44974c` |
| 02 | Your first piece | Keyboard mode, F-key glyph sets (Ctrl+, Ctrl+. Ctrl+/), the pen (Ctrl+arrows, Ctrl+D), undo, Save, the SAUCE dialog | Written, checked against `c44974c`; no window pictures yet (`--screenshot`, #374, can take them now) |
| 03 | Pixels with half blocks | Why ▀▄█ make two pixels a cell; half-block brush, 4- vs 8-connected pencil, line, rectangle, ellipse, Filled Shapes, fill, eyedropper; iCE colours and bright backgrounds | Written, checked against `c44974c`; no window pictures yet (`--screenshot`, #374, can take them now) |
| 04 | Shading: the ladder | ░▒▓ as rungs between two colours, the ten shipped ramps, the shade brush, the ramp shade brush, strength, pressure, alpha lock | Written, checked against `48592c8`: step pictures from `replay` steps files, dock pictures from `--screenshot`, final piece and Try-it file `.bwp` from `replay --project`; pressure is described, not pictured (§4) |
| 05 | Shading: forms and falloff | Form shading (dome, cylinder, plane), soft falloff, ramp gradient tool, blend/smudge, despeckle | Written, checked against `749832e`: step pictures from `replay` steps files, dock pictures from `--screenshot` (they show each tool's default settings), final piece and Try-it file `.bwp` from `replay --project`; 4×4 Bayer banding is described, not pictured |
| 06 | Light | Choosing a light direction, the rim light brush (Ctrl+Shift+L) and its eight compass points, form shading's light, highlights and glints; where the rim light can't help (counters, thin bars, canvas edges) | Ready to write, as 04: rim light and form brushes merged (#49) |
| 07 | Detail | Outline brush, texture stamps, glyph spray, clone stamp, symmetry: mirror X/Y, both, radial 2–8 | Ready to write, as 04: symmetry, outline brush (#55), texture stamp, glyph spray and clone stamp (#10) merged |
| 08 | Composing a scene | Selections, move, flip, rotate, paste modes (normal, transparent, under), guides, reference image, Library stamps, Scene Starter | Selections, move/transform, flip, rotate, paste modes, guides, reference image and the Library (dock, Save to Library) merged; the Scene Starter isn't on `main`; samples and Try-it file are `.bwp` (§6) |
| 09 | Layers and projects | Layer kinds (cells, pixels, text, generator, reference), compositing, the project file, snapshots | Ready to write: the five layer kinds, the project file and snapshots merged (#11, #12, #13); samples and Try-it file are `.bwp` (§6) |
| 10 | Letters and text | Lettering by hand, letters that misread at 1× (C/G, R/A, 0/D), TDF text layers | Ready to write: the Text tool and TDF fonts merged (#18) |
| 11 | Made for IRC | The 407-byte line budget, trailing black and blank rows, glyphs CP437 can't hold, `export --irc`, the row meter, IRC view, lint panel, publish | Ready to write: `export --irc`, the row meter, IRC view, lint panel and publish merged (#14, #15, #16) |
| 12 | Scripts and generators | Generator layers, parameter forms, smart prefabs, the headless CLI | Generator layers and their parameter forms merged (#17); smart prefabs aren't on `main`; CLI `render`, `convert`, `export`, `shade`, `lint`, `replay` merged; samples are `.bwp` (§6) |

Which samples are `.bwp` (§1): the final piece of 04–07, and the samples and Try-it files of 08, 09 and 12, and of every Track B project. 01, 02, 03, 10 (hand lettering) and 11 stay flat `.ans`; 10's TDF text layers, when written, are a `.bwp`.

### Track B: projects

Whole pieces built from the Track A skills: a night scene (sky, moon, stars, tree lines), a face, a figure, a building, an object, an icon, a lettered logo. Written after Track A tutorials 01–08.

## 3. Manual

One page per area, in `manual/`. Each page is written when its feature is on Blockwright's `main`, and updated by the same change that alters the feature (see §5).

| Page | Source in Blockwright's `PLAN.md` | Status |
|---|---|---|
| Install | Phase 6, packaging | Waits for packages (AUR, Debian/Ubuntu, Fedora) |
| The window | §11 workspace layout, §4 renderer (zoom, 1× preview) | Written, checked against `c44974c`; no window pictures yet (`--screenshot`, #374, can take them now) |
| Keyboard mode | §4 keyboard mode | Written, checked against `c44974c` |
| Tools | §4 drawing tools, §10 brushes | Merged tools ready; one section per tool added as each lands |
| Selections | §4 selections | Ready |
| Symmetry | §4 mirror mode, §10 symmetry | Ready |
| Layers | §5, §15 (layer styles) | Written, checked against `0162e63` |
| Library | §12 | Ready for stamps (the Library dock, Save to Library); prefabs and the Scene Starter aren't on `main` |
| Colour | §4 SAUCE/iCE, palette; Phase 8 24-bit | Written, checked against `c44974c`; 24-bit covers reading only (drawing in 24-bit is Phase 8) |
| IRC | §8 IRC text, §9 | Written, checked against `c44974c` |
| Lint | §10 ladder lint, Phase 4 lint panel | Written, checked against `f34d296` |
| Generators | §7 | Ready (#17) |
| File formats | §6, §8 | Written, checked against `c44974c` |
| CLI | `blockwright-cli --help` | Written, checked against `f34d296`; its full help is generated (§4) |
| Shortcuts | every action | Generated (§4) |
| Preferences | — | Nothing to document yet |

## 4. What the docs need from Blockwright

Findings from reading Blockwright's `PLAN.md` and its CLI on 2026-10-23, brought up to `06fbac5` on 2026-11-05.

1. **Step-by-step images come from `blockwright-cli replay <steps.json> -o <dir>`** (#346; #208 stays open as the umbrella). It applies each step through the editor's tools and writes the canvas after each step as `NN-<name>.ans`, and with `--project` as a `.bwp` too, layers and all, so a layered final piece (04–07) comes from the same steps file. A tutorial's `make.py` writes the steps files, runs `replay` and keeps the captures it shows (04's is the model). At `06fbac5` a step's points take a pressure (`[x, y, p]`), but `replay`'s brush maps pressure to nothing (`core/include/blockwright/brush.h:71`) and no step key changes that, so pressure can't be pictured; 04 describes it.
2. **Pictures with a layer hidden.** No command renders a project with a layer left out, but `render` honours each layer's `visible` flag in a project directory: `blockwright-cli unpack final.bwp dir`, set `"visible": false` in `dir/layers/<id>.json`, then `blockwright-cli render dir out.png`. Checked against `c44974c` on a three-layer project: hiding the middle layer leaves the other two. Until Blockwright has a flag for it, a "with this layer hidden" picture is made that way, by the build or a sample script, never saved by hand.
3. **The shortcuts page and the menu reference come from `blockwright --list-actions`** (#209): every menu and dock action as JSON, with its id, menu path, text, shortcuts and tooltip. The build doesn't read it yet; 04's menu paths and shortcuts were checked against it.
4. **The CLI page is generated** from `blockwright-cli --help` and each command's help.
5. **Window screenshots come from `blockwright --screenshot <steps.json> -o <dir>`** (#374, the first slice of #295, which stays open). It plays the same steps file as `replay` in the main window, offscreen, and saves the window, a dock or a crop per step. At `06fbac5` the Tool Options widgets and the palette show the app's defaults, not a step's brush options: only the selected tool, the layers, alpha lock and the lint follow the steps. So a tutorial pictures the docks that follow (Tool Options for which settings a tool has, the Layers and Lint docks), not the window after every step.
6. **Rendering is ready.** `render --scale 2` gives the 2× view; `export --irc` gives each line's byte count.
7. **Before/after toggles** are the one place JavaScript would help. `<details>` or two images side by side do without it.

## 5. Keeping the manual current

- A Blockwright PR that adds or changes user-visible behaviour names the manual page it affects; the docs change lands in this repo before or with the merge.
- Generated pages (shortcuts, CLI, menus) are rebuilt from the installed dev build on every docs build, so they can't go stale.
- Each page states the Blockwright version it was checked against.

## 6. Build and deploy

- Pages are Markdown in `tutorials/` and `manual/`, plus the home page `index.md` and an `index.md` per section. `scripts/build` turns them into `site/`: one Python 3 script on [Python-Markdown](https://python-markdown.github.io/) (the distribution's package: `python-markdown` on Arch, `python3-markdown` on Debian and Ubuntu, `python3-markdown` on Fedora), with the `meta`, `extra`, `toc` and `sane_lists` extensions. No site generator, no JavaScript, no network. `site/` is build output and isn't tracked.
- **Why this:** pages stay plain Markdown that reads on the forge as it is; the only dependency is a packaged library; the output is static HTML that works from a web root, a subdirectory or a file browser, which is also what the in-app help (Blockwright #210) needs.
- **Publishing a page:** a page carries a meta block. `Title:` names it in the lists (else its first heading). `Checked: Blockwright 0.1.0 (c44974c)` says which build it was checked against and publishes it; a page without `Checked:` is a stub, listed as "not written yet", and a link to a stub fails the build.
- **Pictures of pieces:** `![alt](../samples/<tutorial>/<file>.ans "2x")` renders the `.ans` with `blockwright-cli render --scale 2` (the title is the scale, `1x` to `8x`; none means 1×), puts the PNG in its place, links it to the `.ans`, and copies the `.ans` into the site. A `.bwp` is drawn the same way, as its composite, and links to the `.bwp`. The PNG keeps the sample's whole name (`final.ans-2x.png`, `final.bwp-2x.png`), so a flat `.ans` and a project of the same name can sit in one folder, as the flat export beside its project will; failing the build on the clash instead would forbid that pairing. Any other image is a `.png`, copied as it is; an image of any other kind fails the build, an unpacked project directory included, since a picture links to one file the reader downloads. Pictures are never edited by hand.
- **Other files:** any other relative link (a `.bwp` or an `.ans` no page draws, a Try-it file) names a file in the repo, which the build copies into the site at the same path.
- **Generated parts:** `<!-- generated: cli-help -->` is replaced by `blockwright-cli --help`; `<!-- list: tutorials -->` and `<!-- list: manual -->` by the section's pages in order. A marker goes at the start of a line of its own, in column 0: not indented, not in a list item or blockquote. It is written exactly as shown: lowercase, single spaces. The build replaces markers inside Python-Markdown, after it has set fenced code aside, so a marker is left as written exactly where Markdown shows it as code (a closed fence, an indented block), and a page can show one. A marker comment that is still in a page's HTML fails the build, so a marker is never dropped silently: one in the wrong place with the column-0 rule in the message, and a misspelled one (any `<!-- generated:` or `<!-- list:` comment, in any case, that isn't one of the three) with the three markers in the message.
- **Checks:** the build fails on a link to a missing page or to a stub, a `#fragment` the target page has no id for, a link or image path that leaves the repo (symlinks included) or resolves into `.git/` or `site/`, a link to a missing file, a missing sample, a sample the CLI refuses or a render that writes no picture, an image that is neither a sample (`.ans`, `.bwp`) nor a `.png`, a marker left as a comment, and any relative link or image in the output that doesn't resolve.
- **Tests:** `scripts/test-build` runs the build and `scripts/deploy` against scratch copies of the repo, one scenario each for: the repo as it is; the site menu on every page exactly once, linking every built page, listing each section in its index's order with a stub unlinked, and marking the page itself `aria-current="page"` exactly once and its section `here`; the allow-all `robots.txt` in `site/` and in `--out`, with no robots meta tag; `--out` refused inside the repo, around the repo, on a foreign directory, on a built site with a file added, and on a file, and accepted on an empty directory and after a failed build; a linked `.png` and `.ans` copied; a link to a missing file, to a file outside the repo directly and through a symlink, to `.git/` directly and through a symlink, and an `.ans` image through a symlink into `.git/`; a link to a stub and to a missing page; a missing sample, an `.ans` the CLI rejects, a CLI whose render exits 1, and one that exits 0 without a picture; a three-layer `.bwp` made by `import-scene` from an `ansi.py` scene, drawn as its composite (equal to the scene's flat render) and linked, `final.ans` and `final.bwp` in one folder each drawn to its own PNG, and a `.gif` image and an unpacked project directory refused; a scene title SAUCE can't hold (empty, 36 characters, not CP437) refused by `scene()` with a message before it lists its layers, and a 35-character one imported with SAUCE; a scene with a layer that leaves iCE off refused by `scene()` with a message in every mode (`--list-layers`, `--layer-ans`, flat) and by `import-scene`, with nothing written; a missing `#fragment` on another page and on the same page, and good ones; an `.ans` image outside the repo; markers in fenced and indented code shown, a marker after a closed fence, after an unclosed fence, between fences indented two spaces and after a longer closing fence replaced, and a marker inside a paragraph, one indented two spaces and one in a list item refused with the column-0 rule in the message, and misspelled markers in column 0 (spacing, case, an unknown name) refused with the accepted markers in the message; and for `scripts/deploy`, which runs on a stand-in `site/` with a stand-in ssh that logs its arguments and runs the rsync server in a scratch directory (no host is contacted): a local path, `./a:b` and an absolute path holding a colon copied locally with their parents made and no ssh, `host:path` and `user@host:path` sent to the path as written with its missing parent made, `host:` and `user@host:` refused before ssh runs, and the manifest neither copied nor deleted, locally and remotely, while a stale page is deleted. `--deploy FILE` runs those scenarios against another version of the script. Cases it doesn't run include a missing `--cli`, the `--out` symlink and manifest-forging cases, and a real remote host.
- **The output directory:** the build clears it first, so it only builds into a new or empty directory, or one holding exactly what a previous build wrote: each build leaves `.blockwright-docs-manifest` there, listing its files, and `scripts/deploy` doesn't copy it. Any other directory, any output inside the repo but `site/`, and any output that contains the repo are refused.
- **Search engines:** the build writes a `robots.txt` that lets crawlers fetch everything, and pages carry no robots meta tag; `ROBOTS` at the top of `scripts/build` would set one on every page, and is empty (see §7).
- **Which CLI:** `--cli PATH`, else `$BLOCKWRIGHT_CLI`, else `blockwright-cli-dev`, else `blockwright-cli` on `PATH`. The build prints the version it used; a page's `Checked:` should name that version.
- **Reproducible samples:** a tutorial's step files are written by a `make.py` in its samples folder, the same way every time. Where a step is typing or placing cells (01–03, 10, 11), `make.py` draws them with `scripts/ansi.py`, a small cell canvas that writes `.ans` with SAUCE. Where a step is a tool or brush (04–07), `make.py` writes steps files and runs `replay` (§4, §7).
- **Layered samples:** a layered `.bwp` comes from a layer script written with `scripts/ansi.py`'s `scene()`, a layer per part. Blockwright's CLI writes the project from it, so no project writer lives in this repo.
  - **How `import-scene` reads it:** `import-scene` (Blockwright `core/src/scene_import.cpp`, `cli/main.cpp`) imports nothing from the scene; it runs it. It runs `python3 -B <scene.py> --list-layers` and reads one JSON object from stdout, `{"width", "rows", "title", "layers": [{"name"}, {"name", "key"}, …]}` (the bottom layer without a key, every other with a key colour 0–15). Then, once per layer, it runs `python3 -B <scene.py> --layer-ans=NAME [--key=K]` in a scratch directory, with a JSON object on stdin, and reads an `.ans` from stdout: the cells the layer changed, every other cell a blank on colour K, which becomes transparent. Any script that answers those two calls will do; `scene()` is one. Checked against `c44974c` with a 16×4 scene of three layers (sky, hill, sun): three layers, and the composite renders byte for byte as the scene's own flat `.ans`.
  - **Deterministic:** `import-scene --bake --author funkpower --date <CCYYMMDD>` (#308) writes cells layers and no `scripts/`, so the project names no path and has nothing to run on a reader's machine, with SAUCE's author and date fixed. Checked against `06fbac5` with the 16×4 three-layer scene: cells layers, no `scripts/`, and the same bytes imported from two directories.
  - **Layered samples are iCE on:** `scene()` refuses a layer that leaves the canvas with iCE off, because `import-scene` used to make every project iCE on. At `06fbac5` it reads an `ice` key from the layer listing (`core/src/scene_import.cpp`), so `scene()` can pass it and drop the refusal; until it does, the rule stands.
  - Sample scripts reproduce committed `.bwp` files byte for byte, as they do `.ans`. A layered sample whose steps come from a steps file (04–07) is written by `replay --project` instead (§4).
- **Dock pictures depend on the host:** a `.png` from `--screenshot` (§4) is drawn with the host's fonts and Qt style, so `make.py` run on another machine can change only those PNGs while every `.ans` and `.bwp` comes out the same. Regenerate them on the machine that made the committed ones, or commit the new PNGs on their own after looking at them.
- Links between pages are relative, so the same `site/` works at a domain root and in a subdirectory.
- Site layout: `/` (home: what Blockwright is, install, start here), `/tutorials/…`, `/manual/…`, at the domain root of <https://blockwright-docs.pumpin.online/>.
- **Page layout:** the site menu on the left, the page on the right at a 44rem measure. The menu is the home link, then Tutorials and Manual, each section's index and its pages in the order the index lists them (one page list in `scripts/build` feeds the indexes, the menu and the pager); a stub is dimmed and unlinked, as in the index. The current page is marked `aria-current="page"` and highlighted, its section heading yellow. The menu is sticky and scrolls on its own when it is taller than the window. Under 50rem it folds into a `<details>` "Menu" above the page, no JavaScript: beside the page `::details-content` keeps it open and hides the toggle, and a browser that can't style `::details-content` keeps the toggle. Wide pictures and tables scroll inside the page column.
- **Deploy:** every commit to `main` deploys within a few minutes. The maintainer's deploy timer on the dev machine checks `main` every two minutes, builds it with the installed dev CLI into a directory of its own and copies it to the web root behind <https://blockwright-docs.pumpin.online/>; it also redeploys when the dev CLI changes, so the pictures follow the renderer. By hand: `scripts/build`, then `scripts/deploy`, which copies `site/` to `$BW_DOCS_DEST`, a local directory or an rsync destination on another host (`host:path`; `RSYNC_RSH` sets the ssh command). A remote path means what it means to rsync, relative to the login directory unless it starts with `/`; an empty one (`host:`) is refused, since `--delete` would empty the login directory, and `host:.` says so on purpose. Missing parent directories are made on both sides: `mkdir -p` locally, `--mkpath` remotely, which needs rsync 3.2.3 or later at both ends.

## 7. Decisions

- **Search engines:** the site has its own domain, <https://blockwright-docs.pumpin.online/>, and is indexed (docs#1): `ROBOTS = ""` in `scripts/build`, a `robots.txt` that allows everything, and no `X-Robots-Tag` from the host. Its old address, lrh.pumpin.online/blockwright/, where it was `noindex`, redirects permanently to the same page on the new domain.
- **Licence:** the text and the sample art are funkpower's, under CC BY-SA 4.0 (the licence of the bundled font too), unless a file says otherwise. `LICENSE` holds the legal code; the README and every page's footer credit it.
- **Versions:** one set of docs, for the latest Blockwright. No per-release docs until packages ship; then this is decided again.
- **Reproducible samples:** `scripts/ansi.py` step images are fine for the concept tutorials, 01–03, 10 and 11, where a step is typing or placing cells. The brush tutorials, 04–07, show what a brush does to the canvas, so their step images come from `blockwright-cli replay` steps files and are never imitated with `scripts/ansi.py`.
