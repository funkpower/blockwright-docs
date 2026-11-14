Title: Shading: forms and falloff
Checked: Blockwright 0.1.0 (30e0254)

# Shading: forms and falloff

## Goal

Shade whole forms in one click each, and let light fall off across a scene. You'll shade the pan and the yolk of *This Is Your Brain on IRC*, the egg from Blockwright's samples, 80 columns by 32 rows on eleven layers, with Blockwright's ramp gradient, form brush, soft brush, smudge brush and despeckle brush. Shown at 2×:

![The title "THIS IS YOUR BRAIN ON IRC" in white and yellow over a frying pan on black. The pan is white along the top of its rim and its handle, falling through grey to black underneath. In it an egg: white egg white with a brown frilled edge, and a yolk white at its upper left, through yellow to light red and red at its right, with a brown hash sign on it. A strip of blue glow shows along the inside of the rim behind the egg and in front of it, and the caption "Any questions? /msg me." sits under the pan](../samples/05-shading-forms-and-falloff/final.bwp "2x")

## The idea

Tutorial 04 lit a ball with clicks: rings round the light, the ladder stepping down a rung every cell or two from the lit side to the edge. The rule for a round form asks for more: **a broad lit side, and the whole fall from light to dark crowded at the turn**, the line where the form turns away from the light. Past the turn the shadow side goes down to black. Even bands across the whole form read as stripes, not as a ball.

The same fire disc twice, each on a layer of its own with alpha lock on. On the left, tutorial 04's seven clicks; on the right, one click of the **Form Brush**:

![Two red discs on black with labels under them. The left one, "ramp shade clicks", is light red at its upper left and steps down in rings through shades of light red on red and red on black to red light shade on black along its lower right edge. The right one, "form brush", is white over its upper left, yellow and white shade down its left side, and falls from there through yellow, light red and red to black at its lower right](../samples/05-shading-forms-and-falloff/idea.ans "2x")

On the left, solid light red covers the upper left, and the rungs step down from there in rings, most of them two cells wide or more, to red `░` along the lower right edge. Along row 3, right of the light red, the first ring is one cell wide, the next four are two cells each, and the disc's edge cuts the last to one. On the right, solid white covers the upper left, and down the left side, from row 5 to row 9, each row starts a rung lower than the one above, through white shade on yellow to yellow and yellow `▓` on light red. That is the lit side. Past it each rung takes one cell, every rung in order, through yellow, light red and red, to black at the lower right, except one rung on most rows, which takes two: on rows 4 to 10 the first rung past the lit side, at columns 29 and 30, and on row 1 solid yellow, at columns 34 and 35.

Tutorial 04 gave the rule's fall as three to five cells. That is shorter than a whole ramp's ladder can go without skipping a rung: fire has seventeen rungs, numbered 0 (black) to 16 (white), so sixteen steps from black to white. The form brush keeps every rung in order, as tutorial 04 asked, and gives nearly every one a cell, so its fall is about as short as the ladder allows: four cells for each colour, or five where a rung takes two, where along row 3 the clicks gave most rungs two cells.

The rest of the page is the tools that go round a form: the **ramp gradient** for the light behind or under it, falling off as it goes; the **soft brush** for shadows; the **smudge brush** to drag a tone along; and the **despeckle brush** to clean up after.

### The form brush

The **Form Brush** (**Tools > Form Brush**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd>) shades a whole shape along the ramp in one click: a solid lit side, the fall, and the shadow side down to black. The shape is the selection, or with nothing selected the cells the click covers; with alpha lock on, those are the layer's opaque cells under the brush. Make the brush big enough to cover the whole shape. Either button does the same. Its options add **Light** and **Form**, here set for the pan in step 3 below:

![The Tool Options dock for the Form Brush: a help text, then Size 80 with Tip Square, Pressure None with Strength 100%, Ramp steel, Light NW with Form Cylinder, Form rim light unticked with Glint ticked, Alpha lock ticked, and Symmetry Off](../samples/05-shading-forms-and-falloff/form-options.png)

**Light** is the compass point the light comes from, **NW** (the upper left) to start with. **Strength** is how far each cell moves toward the tone the form gives it: shade a form at 100%, so every cell gets there. **Form rim light** and **Glint** are about light more than form; leave them as they are until tutorial 06.

A disc of dark grey on a layer of its own, with alpha lock on, before, and after one click at 100% on the steel ramp:

![A flat dark grey disc on black](../samples/05-shading-forms-and-falloff/form-before.ans "2x")

![The disc as a ball: solid white at its upper left, the rows below that a rung lower each down its left side but for the bottom row, two lower, and from there a rung a cell through grey and dark grey to black at its lower right, where it runs into the black round it](../samples/05-shading-forms-and-falloff/form-after.ans "2x")

### Form

**Form** is the shape of the surface: **Dome**, **Cylinder** or **Plane**. A dome is round every way, a cylinder is round across its shorter side and straight along the longer, and a plane is flat and tilts toward the light. Each of these was laid at dark grey on a layer of its own, with alpha lock on, and shaded with one click at 100%:

![Three labelled grey shapes on black. The dome, a disc, is white at its upper left and falls to black at its lower right. The cylinder, an upright bar, is two columns of white at its left, two of white dark shade on grey, then one each of white medium and light shade on grey, grey and dark grey light shade on grey, the same in every row, with its right column black against the black. The plane, a box, is white across its upper left and falls diagonally to black in its lower right corner](../samples/05-shading-forms-and-falloff/form-shapes.ans "2x")

The cylinder is nine cells across, too few for the ladder to come down from white to black a rung a cell. The brush makes its shadow edge, the right column, black all the same, and the lint reads that column as an outline ending the shading, not a skipped rung.

### The ramp gradient

The **Ramp Gradient** (**Tools > Ramp Gradient**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>G</kbd>) fills with a gradient along the ramp: drag from where it starts to where it ends. It fills the selection, or the whole layer with nothing selected, and alpha lock keeps it to the opaque cells, as for the brushes. The left button runs from the **From** rung to the **To** rung; the right runs the other way. Its options, set for the glow in step 2 below:

![The Tool Options dock for the Ramp Gradient: a help text, then Ramp ice, Gradient Radial with Banding Cell-banded, From rung 6 with To rung 0, and Alpha lock unticked](../samples/05-shading-forms-and-falloff/gradient-options.png)

A bar of magenta, selected, before, and after a drag on the violet ramp from its left end to its right, from rung 0 to rung 12:

![A plain magenta bar](../samples/05-shading-forms-and-falloff/gradient-before.ans "2x")

![The same bar black at the left, climbing through magenta shade on black to magenta, light magenta shade on magenta to light magenta, and white shade on light magenta to white at the right](../samples/05-shading-forms-and-falloff/gradient-after.ans "2x")

Every rung between the ends is laid, in order. Each shade block takes two cells along the gradient, and the solid colours share the rest of the length as plateaus: here five cells of black, four of magenta, four of light magenta and five of white. Broad plateaus with the shades squeezed between them: the same terracing as the form's lit side and fall.

**Gradient** is **Linear**, along the drag, or **Radial**, in rings round where you press. **Banding** is **Cell-banded**, each rung in whole cells, or **4×4 Bayer**, which mixes the edge of each band into the next with an ordered dither. The lint doesn't call the dither's cells specks while each sits a rung from its neighbours, and a project keeps them that way; saved as `.ans` and opened again, they are plain cells and the lint calls them specks. **From rung** and **To rung** count up the ramp from 0, its darkest. Each row here is a box on the violet ramp, cell-banded, with a drag across it:

![Three labelled rows on black. "linear": black at the left climbing to white at the right. "radial": white at the middle, a ring of white shade round it, and rings stepping down to magenta at the right end and magenta dark shade on black at the left. "rung 4 to 8": magenta over the left part, three shade blocks, and light magenta over the right part](../samples/05-shading-forms-and-falloff/gradient-settings.ans "2x")

The radial row is a drag from the middle of its box to the right end, from rung 12 down to 0. At two cells a rung, those eighteen cells hold the ladder from white down to magenta and no further: a gradient too short for its rungs carries the ladder on past where the drag ended, outside the box, rather than skip a rung. The last row, from rung 4 to rung 8, has no solid colour between its ends, so the two ends take the rest of the length.

### The soft brush

The **Soft Brush** (**Tools > Soft Brush**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>N</kbd>) is the ramp shade brush with a soft edge: it moves the middle of the tip the most and its edge a rung, in rings that step down a rung at a time. That fade from the middle to the edge is its **falloff**. The left button lightens and the right darkens. Its options add **Hardness**, here set for the shadows in step 5 below:

![The Tool Options dock for the Soft Brush: a help text, then Size 8 with Tip Round, Pressure None with Strength 50%, Ramp ice, Hardness 0%, Alpha lock unticked, and Symmetry Off](../samples/05-shading-forms-and-falloff/soft-options.png)

A field of brown, before, after one click on the wood ramp at 50% with **Size** 11, **Tip** **Round** and **Hardness** 0%, and after the same click with the right button:

![A plain brown field](../samples/05-shading-forms-and-falloff/soft-before.ans "2x")

![The field with a patch of yellow medium shade on brown in the middle, ringed by yellow light shade on brown](../samples/05-shading-forms-and-falloff/soft-after.ans "2x")

![The field with a patch of brown medium shade on red in the middle, ringed by brown dark shade on red](../samples/05-shading-forms-and-falloff/soft-right.ans "2x")

At 50% the middle moved two rungs and the ring round it one.

### Hardness

**Hardness** is how sharp the edge is: 0% spreads the falloff across the whole tip, and 100% moves every cell as much as the middle. The same click at 100% on the brown field, at each hardness:

![Three patches on the brown field, labelled under them. 0%: yellow dark shade on brown in the middle row, ringed by medium shade, then light shade. 50%: a wider patch of yellow medium shade on brown, ringed by light shade. 100%: a disc of solid yellow with a hard edge](../samples/05-shading-forms-and-falloff/hardness.ans "2x")

At 0% the middle climbed three rungs, to `▓`, and the rungs step down a ring at a time to the field. At 50% the middle climbed two, to `▒`, over a wider patch, with one ring of `░` round it. At 100% every cell under the tip climbed the whole four rungs to yellow, with no falloff at all. Soft shadows want 0%.

### The smudge brush

The **Smudge Brush** (**Tools > Smudge Brush**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>M</kbd>) picks up the ramp colours under the tip and drags them along the stroke, like a finger through paint, and snaps what it lays back to the ramp's rungs. Each cell of the tip carries its own value, so a wide tip drags a patch. Either button does the same. Its options, set for the rim's shadow in step 6 below:

![The Tool Options dock for the Smudge Brush: a help text, then Size 2 with Tip Square, Pressure None with Strength 50%, Ramp ice, Alpha lock unticked, and Symmetry Off](../samples/05-shading-forms-and-falloff/smudge-options.png)

A row of brown meeting a row of brown medium shade on red, before, and after one drag on the wood ramp at 50% with **Size** 1, from four cells left of where they meet to ten cells right of it:

![A row, solid brown over its left half and brown medium shade on red over its right half](../samples/05-shading-forms-and-falloff/smudge-before.ans "2x")

![The same row with two cells of brown dark shade on red just right of where the brown ends](../samples/05-shading-forms-and-falloff/smudge-after.ans "2x")

**Strength** is how far it drags: at 100% a cell carries its value unchanged, and lower, it fades into the cells it crosses. The same drag at each strength:

![Four labelled rows. At 25% one cell of brown dark shade follows the brown; at 50%, two; at 75% the brown reaches a cell further and three cells of dark shade follow it; at 100% the brown runs on unchanged to where the drag ended](../samples/05-shading-forms-and-falloff/smudge-strength.ans "2x")

### The despeckle brush

The **Despeckle Brush** (**Tools > Despeckle Brush**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>D</kbd>) cleans up specks: a lone cell lighter or darker than every neighbour on the ramp takes the rung most of its neighbours share. Cells off the ramp, black, the ramp's top rung (a glint) and the cells of a Bayer gradient's dither are left alone, and so is any fix that would add a new lint finding. Either button does the same. Its options have no **Strength**; here they are set for the clean-up in step 8 below:

![The Tool Options dock for the Despeckle Brush: a help text, then Size 12 with Tip Square, Pressure None, Ramp ice, Alpha lock unticked, and Symmetry Off](../samples/05-shading-forms-and-falloff/despeckle-options.png)

A field of brown medium shade on red with six specks along its middle row, before, and after one drag of a size 5 brush along that row on the wood ramp. The specks, left to right: a cell a rung up, a cell a rung down, a cell two rungs up, a pair of cells a rung up, a cell of yellow (the top rung) and a cell of black:

![A field of brown medium shade on red with six specks along its middle row: dark shade, light shade, solid brown, two cells of dark shade, yellow and black](../samples/05-shading-forms-and-falloff/despeckle-before.ans "2x")

![The same field with only the pair of dark shade cells, the yellow cell and the black cell left](../samples/05-shading-forms-and-falloff/despeckle-after.ans "2x")

The three lone specks went back to the field. The pair stayed, since each of the two has a neighbour that matches it; the yellow and the black stayed, as the brush leaves them.

## Do it

You'll start from the egg with its pan and yolk still flat, and shade it back to front: a glow under the pan, the pan, the yolk, the shadows on the glow, and a clean-up. The positions are column then row from `0, 0` at the top left, as in tutorial 04; zoom in (<kbd>Ctrl</kbd>+<kbd>=</kbd>) so you can count cells. Set **Size**, **Tip**, **Strength**, **Ramp** and the other options in the **Tool Options** dock; they carry over from tool to tool, so each step gives only the ones it changes. To select a box, take the **Select** tool (<kbd>Ctrl</kbd>+<kbd>E</kbd>) and drag from its top left cell to its bottom right cell; **Selection > Deselect** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>A</kbd>) drops the selection. Tutorial 08 covers selections in full, and tutorial 09 layers.

1. **Open the egg.** Download [start.bwp](../samples/05-shading-forms-and-falloff/start.bwp) and open it (**File > Open**, <kbd>Ctrl</kbd>+<kbd>O</kbd>):

    ![The title "THIS IS YOUR BRAIN ON IRC" over a flat dark grey frying pan on black, with an egg in it: white egg white with a brown frilled edge and a flat yellow yolk with a brown hash sign on it, smoke rising above it, and the caption "Any questions? /msg me." under the pan](../samples/05-shading-forms-and-falloff/start.bwp "2x")

    It is the egg from the samples, with its pan and its yolk flat: the pan all dark grey, the yolk all yellow, each on a layer of its own, `pan` and `yolk`, with alpha lock on. The rest is on the layers round them: `egg white` between the pan and the yolk, `#`, `sizzle` and `smoke` above the yolk, the words on `caption`, `tagline` and `signature` below the pan, and `background`, locked, at the bottom.

2. **The glow.** The hob is on. Click **background** in the **Layers** dock, then **Layer > New Cells Layer**, double-click the new layer's name and type `heat`. Select from `10, 14` to `58, 26`, round the pan. Take the **Ramp Gradient** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>G</kbd>) and set **Ramp** to **ice**, **Gradient** to **Radial**, **Banding** to **Cell-banded**, **From rung** to 6 and **To rung** to 0. Drag from `34, 20`, under the yolk, to `62, 20`. Then **Selection > Deselect**:

    ![The egg in its flat pan with blue light showing between the rim and the egg: a strip along the back of the pan, solid blue in the middle and blue shade at its ends, and a shorter strip at the front](../samples/05-shading-forms-and-falloff/step-01.ans "2x")

    Most of the glow is under the pan and the egg, which is where a glow belongs. What shows is the ring where it falls off: along row 15, behind the egg, blue `▒` at column 24, three cells of blue `▓`, solid blue to column 40 where the egg's edge doesn't cover it, three more of `▓` and a `▒` at 44, and pieces of the same at the front, on row 25. Past the ring, out to the selection's edge, it is black.

3. **The pan's form.** Click **pan** in the **Layers** dock; its **Alpha Lock** is already ticked, so the shape is the pan. Take the **Form Brush** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd>), set **Ramp** to **steel**, **Strength** to 100%, **Size** to 80, **Tip** to **Square** and **Form** to **Cylinder**, leave **Light** at **NW**, and click once at `41, 20`. Size 80 covers the whole pan, handle and all:

    ![The pan shaded: white along the top of the rim and the handle, stepping down through white shade on grey to a black lower edge, behind the egg and in front of it alike](../samples/05-shading-forms-and-falloff/step-02.ans "2x")

    The pan is wider than it is tall, so the cylinder lies on its side and is round from top to bottom. Down the left end of the rim, column 8, it is white, then white `▓`, `▒`, `▒` and `░` on grey, then black.

4. **The yolk's form.** Click **yolk** in the **Layers** dock. Its alpha lock is on too:

    ![The Layers dock: yolk, active, with Alpha Lock ticked, then egg white, unticked, pan, ticked, and signature, tagline and caption, unticked](../samples/05-shading-forms-and-falloff/layers.png)

    Take the **Form Brush** again, set **Ramp** to **fire**, **Size** to 30 and **Form** to **Dome**, and click once at `32, 19`:

    ![The yolk shaded: white at its upper left, falling through yellow and light red to red at its lower right, the brown hash sign unchanged on top of it](../samples/05-shading-forms-and-falloff/step-03.ans "2x")

    Across row 17 the yolk is four cells of white, then a cell for each rung down: white `▓`, `▒` and `░` on yellow, yellow, yellow `▓`, `▒` and `░` on light red, light red, two cells of light red `▓` on red and one of `▒`, where the egg white cuts it off. The broad lit side, and the fall crowded after it.

    The `#` is on its own layer above the yolk, so the click left it alone. That is the way to keep it: the form brush's output stays on the form's layer, and anything drawn over the form goes on a layer above, the yolk's highlight included (tutorial 06). Click the form again later and it shades the yolk, not the `#`; after step 9, though, it also paints over that step's one-cell fixes, which then need making again. The sample's own yolk is gentler, skin at 65%; the rule here still holds, since a form you mean to soften is easier to soften from 100% than to find from 25%.

5. **The shadows.** Click **heat** in the **Layers** dock. Take the **Soft Brush** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>N</kbd>) and set **Ramp** to **ice**, **Strength** to 50%, **Size** to 8, **Tip** to **Round** and **Hardness** to 0%. With the right button, drag from `38, 26` to `44, 26`, under the front of the egg, and from `20, 15` to `26, 15`, where the rim at the back left stands between the light and the glow:

    ![The glow darker in two places: at the front, under the egg, the blue shade a rung darker and its end gone to black; at the back left, the end of the strip gone to black and the shade a rung darker up to the solid blue](../samples/05-shading-forms-and-falloff/step-04.ans "2x")

    At the front, columns 41 to 43 of row 25 go from `▓` to `▒` and 44 to black. At the back, 24 goes to black, 25 to 27 from `▓` to `▒`, and 28 from solid blue to `▓`.

6. **Drag the rim's shadow.** The light comes from the left, so the shadow can run further right along the back. Take the **Smudge Brush** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>M</kbd>), set **Size** to 2 and **Tip** to **Square**, leave **Strength** at 50%, and drag from `26, 15` to `32, 15`. Column 28 drops another rung, to `▒`, and 30 and 31 from solid blue to `▓`:

    ![The back strip of the glow with its shade carried three cells further right](../samples/05-shading-forms-and-falloff/step-05.ans "2x")

7. **Specks.** Slips of a one-cell brush leave specks, and the glow is easy to slip on. Make three on purpose: take the **Ramp Shade Brush** (<kbd>Ctrl</kbd>+<kbd>T</kbd>), set **Strength** to 25% and **Size** to 1, and click `47, 16`; set **Strength** to 50%, right-click `34, 15` and click `37, 15`. The **Lint** dock lists six findings (if it is hidden, **Window > Lint**):

    ![The glow with a cell a rung lighter at the right end of the back strip, a cell two rungs darker and a cell of light blue in the solid blue](../samples/05-shading-forms-and-falloff/step-06.ans "2x")

    ![The Lint dock: six findings. speckle at 47,16 and fallback-speck at 47,17 on the sunset ramp, rung-skip at 33,18 on the skin ramp, speckle at 56,19 and 23,23 on the fire ramp and at 11,22 on the steel ramp](../samples/05-shading-forms-and-falloff/lint-before.png)

    `47, 16` is listed as a speck, and `47, 17` under it, a half block of the egg's brown edge, as a [fallback speck](../manual/11-lint.md#fallback-speck); the lint names the ramp it reads them on, sunset, and both go when `47, 16` does. `34, 15` and `37, 15` aren't listed: the lint judges a cell only when three of its four neighbours are on the ladder, and each of these has the rim above and the egg below. The other four were there before the specks. With the dock open from step 1, the count runs 1, 4, 5, 4: `start.bwp` arrives with a speck at `31, 18`, a cell of the `#` against the flat yolk, which goes with the yolk's form; the pan's form brings `56, 19`, `11, 22` and `44, 25`, a speck in the glow at the front, which goes with the shadow under the egg in step 5; and the yolk's form brings `33, 18` and `23, 23`. Step 9 comes to the four left.

8. **Clean up.** Take the **Despeckle Brush** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>D</kbd>), **Ramp** still **ice**, set **Size** to 12 and **Tip** to **Square**, and drag from `10, 15` to `58, 15`. All three go back: the brush reads the active layer alone, where every neighbour is glow, so it fixes the two the lint can't see as well as the one it can:

    ![The glow as it was before the specks](../samples/05-shading-forms-and-falloff/step-07.ans "2x")

    ![The Lint dock: four findings, rung-skip at 33,18 on the skin ramp, speckle at 56,19 on the fire ramp, at 11,22 on the steel ramp and at 23,23 on the fire ramp](../samples/05-shading-forms-and-falloff/lint-forms.png)

9. **Where the forms meet the layers.** The four left are where a form meets a layer above it, and the despeckle brush on `heat` doesn't reach them. Each is one cell; fix them with a one-cell **Ramp Shade Brush**, **Tip** **Square**, on the form's own layer:

    - Click **yolk** in the **Layers** dock and set **Ramp** to **fire**. `23, 23`, the tip of the yolk's tail, is a cell of light red between egg white and yellow `░` on light red: at **Strength** 25%, click it once, and it matches `24, 23` beside it. `33, 18` is yellow `▒` on light red against the `#`'s brown, which the lint reads on the skin ramp as more than a rung away: click it once, still at 25%, to yellow `▓` on light red, like `32, 18` beside it and `33, 17` above it. That clears the finding because the lint counts a jump as a skip only when it carries on a fall: at `▒` the row fell from `32, 18` to `33, 18` and on to the brown, and at `▓` the two cells are one level with the `#`'s brown on either side, which is an edge.
    - Click **pan** and set **Ramp** to **steel**. `11, 22`, at the left of the pan's inner rim, is a `▓` among `▒`: at 25%, click `11, 21` above it, and the two make a pair. `56, 19` is a spark of the sizzle in the black at the rim's inner edge: at 100%, click `56, 18`, the black cell above it, back to dark grey.

    ![The finished piece: the shaded pan and yolk, the glow with its shadows, and no specks](../samples/05-shading-forms-and-falloff/final.bwp "2x")

    The **Lint** dock is clean:

    ![The Lint dock with no findings: clean, noise 0.0140, iCE on](../samples/05-shading-forms-and-falloff/lint.png)

10. **Save it.** **File > Save As** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>), with a name ending `.bwp`, so the eleven layers are kept.

## Check it

**Shade a form at 100%.** At 25% each cell moves only part of the way to its tone. The disc from *The form brush* after the same click at 25%:

![The disc with dark grey light shade on grey over its upper left, stepping down through dark grey to dark grey light shade on black over its lower right: no white and no black](../samples/05-shading-forms-and-falloff/form-weak.ans "2x")

The lit side stops at dark grey `░` on grey and the shadow side at dark grey `░` on black, so the form is dim and flat. Undo (<kbd>Ctrl</kbd>+<kbd>Z</kbd>), set **Strength** to 100%, and click again.

**Lay the shape before the form.** An empty cell counts as black, so where the form's tone is black the brush has nothing to change, and the cell stays empty. The yolk's click on a new, empty layer, with a round tip of size 14 and the flat yolk hidden:

![The yolk cut off: its lit side and fall are there, white, yellow and light red, but where it should go on down to red at its right the egg white shows through](../samples/05-shading-forms-and-falloff/no-base.ans "2x")

Undo, and shade the layer that holds the flat shape, locked, as in step 4.

**Select before a gradient.** With nothing selected the gradient fills the whole layer. A radial drag on a new canvas, from the top left corner, with no selection:

![A radial gradient over the whole canvas, light magenta in the top left corner falling off in rings through magenta to magenta shade on black in the bottom right corner](../samples/05-shading-forms-and-falloff/no-selection.ans "2x")

Undo, select the box, and drag again.

**Smudge below 100%.** At 100% the smudge carries a value unchanged to where the drag ends, as in the 100% row under *The smudge brush*, and the shadow ends in a hard edge. Drag at 50% or less, so it fades into the glow. Keep the drag on the shading, too: dragged off its end into empty cells, it lays nothing there.

**Despeckle doesn't fix everything.** It leaves pairs, black and the ramp's top rung, as in the picture under *The despeckle brush*, and it reads only the active layer, so a cell that is a speck only against another layer's cells, like the four in step 9, stays. Fix those with a one-cell **Ramp Shade Brush**: at 25%, left button to lift a cell a rung and right to drop it; a black cell, like `56, 18`, takes 100% to come back.

## Try it

Download [try.bwp](../samples/05-shading-forms-and-falloff/try.bwp) and open it (**File > Open**, <kbd>Ctrl</kbd>+<kbd>O</kbd>):

![The wall and the floor with a long box of dark grey light shade on black lying across the floor](../samples/05-shading-forms-and-falloff/try.bwp "2x")

It is a wall and a floor, with a log lying on the floor: a box of steel's first rung on a layer of its own, `log`, with alpha lock on. Click **log** in the **Layers** dock to make it the active layer.

1. Shade the log as a cylinder lying on its side, lit from the upper left, and lay its shadow on the floor under it. Check the Lint dock until it is clean.
2. The log's top four rows climb down from white only as far as white `░` on grey, but its bottom row is black. Why is that no skipped rung?

<details markdown="1">
<summary>Answers</summary>

1. Take the **Form Brush**, **Ramp** **steel**, **Strength** 100%, **Form** **Cylinder**, **Light** **NW**, **Size** 30, **Tip** **Square**, and click once at `31, 13`. A cylinder is round across its shorter side, so a log wider than it is tall is round from top to bottom: a row of white, then white `▓`, `▒` and `░` on grey, a row each, and a black bottom row. For the shadow, make **Background** active, take the **Soft Brush**, **Ramp** **wood**, **Strength** 50%, **Size** 6, **Tip** **Round**, **Hardness** 0%, and drag with the right button from `24, 16` to `46, 16`. Your strokes needn't match these; what matters is the light along the top, the ladder stepping down a rung a row, and the floor darker under the log:

    ![The log shaded: white along its top row, then white shade on grey a row at each rung, and a black bottom row; under it the floor is two rungs darker along the two bottom rows, a rung at each end](../samples/05-shading-forms-and-falloff/try-answer.ans "2x")

2. The log is five rows deep, too few for the ladder to come down from white to black a rung a row. The form brush makes a thin cylinder's shadow edge black all the same, and the lint reads that edge as an outline ending the shading, not as a skipped rung.

</details>

Tutorial 06, *Light*, goes on from here: choosing where the light comes from, the rim light brush, and the form brush's rim light and glint.
