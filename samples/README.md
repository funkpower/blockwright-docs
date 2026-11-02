# Samples

One folder per tutorial, named as the tutorial (`03-pixels-with-half-blocks/`). In it: the `.ans` for each step (`step-01.ans`, `step-02.ans`, …, `final.ans`), the exercise's starting file (`try.ans`), and whatever made them: a `make.py` that writes them with `scripts/ansi.py` (run it as `python3 -I samples/<tutorial>/make.py`), later a `steps.json` for `blockwright-cli replay`, or a note saying where a file came from. PNGs are build output, not tracked; `scripts/build` renders them.

The samples are funkpower's art, under the repo's licence, CC BY-SA 4.0 (`LICENSE`), unless a file says otherwise.
