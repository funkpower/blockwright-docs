# Blockwright docs — working rules

Static documentation site for Blockwright: tutorials and the manual. `PLAN.md` is the structure and the build; read it before adding or reordering pages, and update it in the same commit when a decision changes.

## Ground truth

- Blockwright's own `PLAN.md` (`~/…/blockwright/PLAN.md`) is the source for what every tool does, its shortcut and its limits. A page never describes behaviour the app doesn't have yet; a page for a planned feature stays a placeholder until the feature is on Blockwright's `main`.
- The craft rules the tutorials teach are the maintainer's, written down in the maintainer's private notes along with where to find them. Teach those rules; don't invent new ones.
- Check every step and every documented option against the installed dev build (`blockwright-dev`, `blockwright-cli-dev`) before it ships, and record the version checked on the page.

## Samples

- Sample art is funkpower's own: made for the tutorial, or cut from funkpower's own pieces (the maintainer's private notes say where they are). Never use pieces from `ircart/`, `polyhurt/` or anyone else's work, and nothing that shows a real person.
- Every picture on the site is rendered from an `.ans` in `samples/` with `blockwright-cli render`, never a hand-edited PNG, so a sample can be re-rendered when the renderer changes.
- A sample that will be shown on IRC states its widest line's byte count from `blockwright-cli export --irc`.

## Site

- Plain HTML and CSS. No JavaScript unless `PLAN.md` records why a page needs it.
- Every page reads at phone width.

## Git

- Remote: `https://git.pumpin.online/funkpower/blockwright-docs.git`. Push with `GIT_ASKPASS=$PWD/scripts/git-askpass`. Commits are made as funkpower, never as a real name. No Co-Authored-By or "Generated with" trailers.
- Single-author repo: commit and push to `main`.

## Public repo

The repo is meant to go public with Blockwright. Tracked files and commit messages carry no real names, personal host names, home-directory paths (write `~/…`), email addresses, tokens or other secrets. Deploy targets live in the environment, not in the repo.
