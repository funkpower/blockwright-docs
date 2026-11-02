# Blockwright docs — working rules

Static documentation site for Blockwright: tutorials and the manual. `PLAN.md` is the structure and the build; read it before adding or reordering pages, and update it in the same PR when a decision changes.

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

## Build and test

- `scripts/build` must pass, and `scripts/test-build` (the build's own checks, run against scratch copies of the repo) must pass, before a PR opens. A change to `scripts/build` that adds behaviour adds a scenario to `scripts/test-build`.
- Sample scripts (`samples/*/make.py`) must reproduce the committed `.ans` files byte for byte.

## Git and the forge

- Remote: `https://git.pumpin.online/funkpower/blockwright-docs.git`. Push with `GIT_ASKPASS=$PWD/scripts/git-askpass`. Commits are made as funkpower (picked up from the remote URL), never as a real name.
- Work on a branch, open a PR with `scripts/forge pr-create <branch> <title> <body-file>`; the PR body is the report. Never push to `main`; PRs are squash-merged through `scripts/forge pr-merge`.
- No Co-Authored-By or "Generated with" trailers. Never force-push except `--force-with-lease` on your own branch.
- Never print the forge token or any `pass` entry.

## Review

Every PR gets an adversarial Codex review before it merges. When Codex is unavailable (out of credits or its session limit), a Claude reviewer stands in for it, one that didn't write the change, and says in its comment that it is the fallback. A later pass may go back to Codex once it is available; either the stand-in or Codex may then re-check the stand-in's findings. Findings need a failing test or an exact repro; the author fixes, the same reviewer re-checks. Codex can't run the build, so the PR body states what was built and tested and how.

## Public repo

The repo, its history, issues and PRs are public. Tracked files, commit messages and PR or issue text carry no real names, personal host names, home-directory paths (write `~/…`), email addresses, tokens or other secrets, and nothing about anyone's employer or private infrastructure. Pages and tests may use placeholder addresses at reserved example domains (`example.org`, `example.com`, `.invalid`, `.test`), which belong to nobody. People are "funkpower" or "the maintainer"; machines are "the dev machine". Deploy targets live in the environment, not in the repo. PRs are squash-merged, so the PR title and the first paragraph of its body become the commit on `main`.

## Licence

The text and the sample art are funkpower's, under CC BY-SA 4.0 (`LICENSE`), unless a file says otherwise. Don't add anything that can't be shared under it.
