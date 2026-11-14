# Blockwright docs

Documentation for [Blockwright](https://git.pumpin.online/funkpower/blockwright), the ANSI and IRC art editor: tutorials that start from nothing (what a cell is, how half blocks become pixels, how a shade ladder works, how to light a shape, how to get a piece onto IRC inside the byte budget) and a manual that covers every tool, menu, file format and command.

Published at <https://blockwright.pumpin.online/>. Every commit to `main` is live there within a few minutes.

## Layout

| Path | What |
|---|---|
| `tutorials/` | One Markdown file per tutorial, in reading order |
| `manual/` | One Markdown file per area of the app |
| `samples/<tutorial>/` | The `.ans` files a tutorial shows, step by step, and what makes them |
| `index.md` | The home page: what Blockwright is, the downloads and links into the docs |
| `docs/index.md` | The Docs page: every tutorial and manual page, at `/docs/` |
| `release.json` | The current release: its version and file names, for the home page's downloads. A new release changes `version` here |
| `release-checklist.md` | The maintainer's release checklist: which pages are behind the dev build, at `/release-checklist.html`, linked from no other page |
| `theme/` | The page template and stylesheet |
| `scripts/build` | Builds the site into `site/` (not tracked) |
| `scripts/test-build` | Checks the build against scratch copies of the repo |
| `scripts/ansi.py` | Writes the samples' `.ans` files |
| `scripts/deploy` | Copies `site/` to the web root: a directory, or `host:path` on another machine |
| `scripts/forge` | Opens and merges PRs on the forge |

## Build

Needs Python 3, Python-Markdown (`python-markdown` on Arch, `python3-markdown` on Debian, Ubuntu and Fedora) and `blockwright-cli`, with the Blockwright app beside it or on `PATH` for the shortcuts page:

```
scripts/build                      # into site/
scripts/build --out /some/dir      # elsewhere, outside the repo
scripts/build --cli path/to/blockwright-cli
scripts/build --app path/to/blockwright  # the app the shortcuts page runs (from the CLI's commit)
scripts/test-build                 # the build's own checks
```

Open `site/index.html` in a browser.

The build clears its output directory first, so it only builds into an empty or new directory or one it built before (it leaves a `.blockwright-docs-manifest` there listing what it wrote). It refuses a directory holding anything else.

`PLAN.md` is the structure, the status of each page and how the site gets built.

## Licence

The text and the sample art are funkpower's, licensed under [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0), unless a file says otherwise. The full licence is in `LICENSE`.

The exception is the ridges and stars generator scripts packed inside some sample projects (`.bwp`): they come from Blockwright's own samples and are under the GNU General Public License, version 3 or later, as Blockwright is. `samples/README.md` lists them.
