#!/usr/bin/env python3
"""Write the Samples page and its files: python3 -I samples/gallery/make.py

Every sample is one of the projects Blockwright installs (Help > Samples),
opened by a steps file's {"sample": ...} start and played by
`blockwright-cli replay` (the CLI is $BLOCKWRIGHT_CLI, else blockwright-cli on
PATH). For each sample, in a folder named after it:

- `<name>.bwp` and `<name>.ans`: the project as it opens, and flattened. One
  step that changes nothing (a Shade step without points) captures both.
- `layer-NN.ans`: the layer stack built up one layer at a time. The steps hide
  every visible layer but the bottom one, then show them again from the bottom
  up, one step each; the capture after each step that shows a layer is kept.
  Layers the project keeps hidden stay hidden, as they do when it opens.
- `variant-NN.ans`: each variant in its notes, the sample opened as that
  variant (the start's "variant") and captured with the same empty step.

The steps files are kept beside them (*.steps.json). The page,
`samples/index.md`, is written from the projects' notes (the description,
the Layers and Variants tables), the captures, and the summary line of
`blockwright-cli export --irc` on each project, under the project's own
budget.
"""

import json
import os
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAGE = HERE.parent / "index.md"
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
# Blockwright's samples, in the order the app lists them; the layers showcase
# leads the page.
SAMPLES = ["01-layers-showcase", "02-ddos-king", "03-still-life", "04-generator-ridges", "05-character",
           "06-blockwright-logo", "07-battlestation", "08-brain-on-irc", "09-wtc-0903"]
# Samples that pack generators of Blockwright's own, which stay under its
# licence: the scripts/<n>/ directories and what each one is.
GENERATORS = {
    "01-layers-showcase": "`scripts/10/` (the fog, `fog.py`)",
    "04-generator-ridges": "`scripts/2/` (the stars, `stars.sh` and `stars.awk`), `scripts/3/` and `scripts/4/` "
                           "(the ridges, `ridges.sh` and `ridges.awk`)",
}
BLOCKWRIGHT_LICENSE = "https://git.pumpin.online/funkpower/blockwright/src/branch/main/LICENSE"
# A step that changes nothing: a tool step without points only sets Tool Options.
NOTHING = {"action": "shade"}
SUMMARY_RE = re.compile(r"^(\d+) lines, longest (\d+) bytes, (\d+) sent, budget (\d+): (\d+) over$", re.M)


def run(*args):
    return subprocess.run([CLI, *map(str, args)], check=True, capture_output=True, text=True).stdout


def replay(folder, name, start, steps, keep):
    """Writes <name>.steps.json in folder and plays it; keep lists (step's name,
    file) pairs, the capture after that step and the file it becomes (an .ans,
    or a .bwp for the project)."""
    path = folder / f"{name}.steps.json"
    body = {"version": 1, "start": start, "steps": steps}
    path.write_text(json.dumps(body, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    width = max(2, len(str(len(steps))))
    number = {step["name"]: f"{i + 1:0{width}d}" for i, step in enumerate(steps)}
    project = any(dest.endswith(".bwp") for _, dest in keep)
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([CLI, "replay", str(path), "-o", tmp] + (["--project"] if project else []), check=True,
                       stdout=subprocess.DEVNULL)
        for step, dest in keep:
            shutil.copyfile(Path(tmp) / f"{number[step]}-{step}{Path(dest).suffix}", folder / dest)


def table(notes, heading):
    """The Markdown table under `## heading` in notes, as its lines."""
    m = re.search(rf"^## {re.escape(heading)}\n\n((?:\|.*\n)+)", notes, re.M)
    if not m:
        raise SystemExit(f"no {heading} table in the notes")
    return m.group(1).rstrip("\n").split("\n")


def rows(lines):
    """A Markdown table's body rows as lists of cells."""
    return [[c.strip() for c in line.strip().strip("|").split("|")] for line in lines[2:]]


def alt(text):
    return text.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def figure(src, alt_text, caption):
    return (f'<figure><img src="{src}" alt="{alt(alt_text)}"><figcaption>{caption}</figcaption></figure>')


def listing(names):
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]


def sample(sid):
    folder = HERE / sid
    shutil.rmtree(folder, ignore_errors=True)
    folder.mkdir()
    start = {"sample": sid}

    # The project as it opens, and flattened, named after its title.
    replay(folder, "final", start, [dict(NOTHING, name="final")], [("final", "piece.bwp"), ("final", "piece.ans")])
    with zipfile.ZipFile(folder / "piece.bwp") as z:
        manifest = json.loads(z.read("manifest.json"))
        layers = [json.loads(z.read(f"layers/{i}.json")) for i in manifest["layers"]]
        notes = z.read("notes.md").decode("utf-8")
    names = [layer["name"] for layer in layers]
    if len(set(names)) != len(names):
        raise SystemExit(f"{sid}: two layers share a name")
    title = re.search(r"^# (.+)$", notes, re.M).group(1).strip()
    short = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    for kind in (".bwp", ".ans"):
        (folder / f"piece{kind}").rename(folder / f"{short}{kind}")
    description = re.search(r"^# [^\n]+\n\n(.+?)\n\n", notes, re.M | re.S).group(1).strip()

    # The layer stack, one layer at a time.
    shown = [layer["name"] for layer in layers if layer["visible"]]
    steps = []
    for name in reversed(shown[1:]):
        steps += [{"name": f"pick-{len(steps) + 1}", "action": "setActiveLayer", "layer": name},
                  {"name": f"hide-{len(steps) + 2}", "action": "layerProperties", "visible": False}]
    steps.append(dict(NOTHING, name="layer-01"))
    keep = [("layer-01", "layer-01.ans")]
    for n, name in enumerate(shown[1:], 2):
        steps += [{"name": f"pick-{len(steps) + 1}", "action": "setActiveLayer", "layer": name},
                  {"name": f"layer-{n:02d}", "action": "layerProperties", "visible": True}]
        keep.append((f"layer-{n:02d}", f"layer-{n:02d}.ans"))
    replay(folder, "layers", start, steps, keep)
    for _, f in keep:
        if (folder / f).read_bytes() == b"":
            raise SystemExit(f"{sid}: {f} is empty")
    if (folder / f"layer-{len(shown):02d}.ans").read_bytes() != (folder / f"{short}.ans").read_bytes():
        raise SystemExit(f"{sid}: the last layer picture isn't the flattened piece")

    # The variants.
    variants = rows(table(notes, "Variants"))
    for n, (variant, _) in enumerate(variants, 1):
        replay(folder, f"variant-{n:02d}", dict(start, variant=variant), [dict(NOTHING, name="variant")],
               [("variant", f"variant-{n:02d}.ans")])

    # The widest IRC row, under the project's own budget.
    with tempfile.TemporaryDirectory() as tmp:
        out = run("export", "--irc", folder / f"{short}.bwp", Path(tmp) / "irc.txt")
    m = SUMMARY_RE.search(out)
    if not m:
        raise SystemExit(f"{sid}: export --irc printed no summary: {out[-200:]}")
    lines, longest, sent, budget, over = m.groups()

    # The page's section.
    rel = f"gallery/{sid}"
    hidden = [layer["name"] for layer in layers if not layer["visible"]]
    w, h = manifest["width"], manifest["height"]
    md = [f"## {title} {{#{short}}}", "", description, "",
          f"{w} × {h} cells, {len(layers)} layers.", "",
          "### Layer by layer", ""]
    lead = (f"The visible layers from the bottom up, each picture adding one to the ones before it: "
            f"{listing(shown)}.")
    if hidden:
        lead += (f" {'The' if len(hidden) > 1 else 'The one'} hidden {'layers' if len(hidden) > 1 else 'layer'}, "
                 f"{listing(hidden)}, {'stay' if len(hidden) > 1 else 'stays'} hidden, as {'they are' if len(hidden) > 1 else 'it is'} "
                 "when the project opens.")
    md += [lead, "", '<div class="strip">']
    for n, name in enumerate(shown, 1):
        upto = shown[:n]
        what = (f"{title}, its bottom layer, {name}, alone" if n == 1 else
                f"{title} with its bottom {n} visible layers: {listing(upto)}")
        md.append(figure(f"{rel}/layer-{n:02d}.ans", what, f"{'' if n == 1 else '+ '}{name}"))
    md += ["</div>", "", "Each layer, as its notes describe it, from the top down:", ""]
    md += table(notes, "Layers") + ["", "### Variants", "",
                                    "The variants the project offers in the Layers dock, each a few layers "
                                    "shown, hidden or moved:", "", '<div class="strip">']
    for n, (variant, changes) in enumerate(variants, 1):
        md.append(figure(f"{rel}/variant-{n:02d}.ans", f"{title}, the {variant} variant: {changes}",
                         f"{variant}<br><small>{changes}</small>"))
    md += ["</div>", "", "### The finished piece", "",
           f"![{alt(title)}, the finished piece at 1×]({rel}/{short}.ans)", "",
           f'<details><summary>At 2×</summary>\n<img src="{rel}/{short}.ans" alt="{alt(title)}, the finished '
           f'piece at 2×" title="2x">\n</details>', "",
           f"Its widest IRC row is {longest} bytes as `blockwright-cli export --irc` writes it; as WeeChat's "
           f"ascii script sends it, the widest is {sent}. The project's budget is {budget} bytes, and "
           f"{'no row is over it' if over == '0' else f'{over} rows are over it'}.", "",
           f"Download: [{short}.bwp]({rel}/{short}.bwp), the project, layers, notes and all; "
           f"[{short}.ans]({rel}/{short}.ans), the piece flattened."]
    if sid in GENERATORS:
        md += ["", f"The generators packed in {short}.bwp, {GENERATORS[sid]}, are Blockwright's own and stay "
               f"under its licence, the GPL version 3 or later ([Blockwright's `LICENSE`]({BLOCKWRIGHT_LICENSE})); "
               "the rest is under this site's licence."]
    return title, short, "\n".join(md)


def main():
    version = run("--version").splitlines()[0]
    checked = re.sub(r"^\S+", "Blockwright", version.strip(), count=1)
    sections = [sample(sid) for sid in SAMPLES]
    page = ["Title: Samples", f"Checked: {checked}", "", "# Samples", "",
            "The sample projects that come with Blockwright, taken apart. Each one is built from layers, and "
            "each is shown here a layer at a time from the bottom up, with what every layer does, the variants "
            "it keeps, the finished piece and what it costs on IRC. Download a project and open it to turn its "
            "layers on and off yourself; the start screen and **Help > Samples** open the ones your Blockwright installed.", "",
            "Blockwright 0.1.1 installs all nine. 0.1.0 installed five of them, Harbour at night, Still life, "
            "Ridges at dusk, Traveller and Blockwright logo, and Ember Kiln, a text-style logo DDOS KING has since "
            "replaced; it opens the other four projects too.", ""]
    page += [f"- [{title}](#{short})" for title, short, _ in sections]
    for _, _, md in sections:
        page += ["", md]
    PAGE.write_text("\n".join(page) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
