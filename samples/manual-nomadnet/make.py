#!/usr/bin/env python3
"""Write the NomadNet page's samples: python3 -I samples/manual-nomadnet/make.py

operator.bwp is Blockwright's sample 10, Gas-mask operator, a Micron-target
project, taken whole by a one-step `blockwright-cli replay --project` from
its {"sample": ...} start (the CLI is $BLOCKWRIGHT_CLI, else blockwright-cli
on PATH). replay's flat .ans capture can't hold the page's colours, so it is
written with --allow-lossy into a scratch folder and dropped. operator.mu is
`export --micron` of the project.
"""

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLI = os.environ.get("BLOCKWRIGHT_CLI") or "blockwright-cli"
SAMPLE = "10-gas-mask-operator"


def main():
    with tempfile.TemporaryDirectory() as tmp:
        steps = Path(tmp) / "operator.steps.json"
        steps.write_text(json.dumps({"version": 1, "start": {"sample": SAMPLE},
                                     "steps": [{"name": "operator", "action": "deselect"}]}) + "\n")
        out = Path(tmp) / "out"
        subprocess.run([CLI, "replay", "--project", "--allow-lossy", str(steps), "-o", str(out)],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        shutil.copyfile(out / "01-operator.bwp", HERE / "operator.bwp")
    subprocess.run([CLI, "export", "--micron", str(HERE / "operator.bwp"), str(HERE / "operator.mu")],
                   check=True, stdout=subprocess.DEVNULL)


if __name__ == "__main__":
    main()
