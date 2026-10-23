# Blockwright tutorial — agent rules

A static tutorial site for Blockwright. `PLAN.md` is the curriculum and the build; read it before adding or reordering lessons, and update it in the same commit when a decision changes.

## Ground truth

- Blockwright's own `PLAN.md` (`~/…/blockwright/PLAN.md`) is the source for what every tool does, its shortcut and its limits. A lesson never describes behaviour the app doesn't have yet; a lesson for a planned feature stays a placeholder until the feature is on Blockwright's `main`.
- The craft rules the lessons teach are the maintainer's, written down in the maintainer's private notes along with where to find them. Teach those rules; don't invent new ones.
- Check every step of a lesson against the installed dev build (`blockwright-dev`, `blockwright-cli-dev`) before it ships.

## Samples

- Sample art is funkpower's own: made for the lesson, or cut from funkpower's own pieces (the maintainer's private notes say where they are). Never use pieces from `ircart/`, `polyhurt/` or anyone else's work, and nothing that shows a real person.
- Every picture on the site is rendered from an `.ans` in `samples/` with `blockwright-cli render`, never a hand-edited PNG, so a sample can be re-rendered when the renderer changes.
- A sample that will be shown on IRC states its widest line's byte count from `blockwright-cli export --irc`.

## Site

- Plain HTML and CSS. No JavaScript unless `PLAN.md` records why a lesson needs it.
- Every page reads at phone width.

## Git

- Remote: `https://git.pumpin.online/funkpower/blockwright-tutorial.git`. Push with `GIT_ASKPASS=$PWD/scripts/git-askpass`. Commits are made as funkpower, never as a real name. No Co-Authored-By or "Generated with" trailers.
- Single-author repo: commit and push to `main`.

## Public repo

The repo is meant to go public with Blockwright. Tracked files and commit messages carry no real names, personal host names, home-directory paths (write `~/…`), email addresses, tokens or other secrets. Deploy targets live in the environment, not in the repo.
