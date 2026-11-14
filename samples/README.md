# Samples

One folder per tutorial, named as the tutorial (`03-pixels-with-half-blocks/`). In it: the picture for each step (`step-01.ans`, `step-02.ans`, …, `final.ans`), the exercise's starting file (`try.ans`), and whatever made them: a `make.py` that writes them with `scripts/ansi.py` (run it as `python3 -I samples/<tutorial>/make.py`), later a `steps.json` for `blockwright-cli replay`, or a note saying where a file came from.

A sample is a flat `.ans` only while it is one simple picture. Anything more complicated is a Blockwright project, `final.bwp` or `try.bwp`, with each part on its own cells layer, from a layer script written with `scripts/ansi.py`'s `scene()` (`PLAN.md` §6, "Layered samples"). A script reproduces its `.ans` and `.bwp` files byte for byte.

Two folders aren't a tutorial's: `gallery/` holds the Samples page's files, one folder per sample Blockwright installs, written with the page itself (`samples/index.md`) by `gallery/make.py`; `home/` holds the home page's window pictures, written by `home/make.py`, and Blockwright's large logo, `logo-large.ans`, copied unchanged from Blockwright's `branding/` (the same file in 0.1.0).

PNGs are build output, not tracked; `scripts/build` renders them, a `.bwp` as its composite.

The samples are funkpower's art, under the repo's licence, CC BY-SA 4.0 (`LICENSE`), unless a file or the section below says otherwise.

## Generator scripts from Blockwright

The generators packed inside some of the `.bwp` projects come from Blockwright's own samples (the ridges and stars from **Ridges at dusk**, the fog from **Harbour at night**), and are under Blockwright's licence, the [GNU General Public License, version 3](https://www.gnu.org/licenses/gpl-3.0.html) or (at your option) any later version (GPL-3.0-or-later; Blockwright's [`LICENSE`](https://git.pumpin.online/funkpower/blockwright/src/branch/main/LICENSE)). Each generator is a `scripts/<n>/` directory inside the project, a zip: its `generator.json`, the `.sh` and `.awk` it runs, and its `params.json` where it has one (the ridges do, the stars don't). They are:

| Projects | Generators under the GPL |
|---|---|
| `manual-12-generators/`: `ridges.bwp`, `seed-12.bwp`, `smooth.bwp` | `scripts/2/` (stars: `stars.sh`, `stars.awk`), `scripts/3/` and `scripts/4/` (ridges: `ridges.sh`, `ridges.awk`) |
| `gallery/01-layers-showcase/`: `harbour-at-night.bwp` | `scripts/10/` (fog: `fog.py`) |
| `gallery/04-generator-ridges/`: `ridges-at-dusk.bwp` | `scripts/2/` (stars: `stars.sh`, `stars.awk`), `scripts/3/` and `scripts/4/` (ridges: `ridges.sh`, `ridges.awk`) |
| `12-scripts-and-generators/`: `baked.bwp`, `final.bwp`, `low.bwp`, `meteors-1.bwp` to `meteors-3.bwp`, `ridges-1.bwp` to `ridges-6.bwp`, `seed-5.bwp`, `try.bwp`, `try-right.bwp`, `try-tail.bwp` | `scripts/2/` (ridges: `ridges.sh`, `ridges.awk`) |

Everything else in the docs is under CC BY-SA 4.0, including the meteors generator of tutorial 12: `12-scripts-and-generators/meteors/`, and `scripts/4/` (`meteors.py`) in that tutorial's projects.
