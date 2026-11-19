Title: Detail
Checked: Blockwright 0.1.1 (1347435)

# Detail

## Goal

Make this castle wall under a night sky, 60 columns by 20 rows, on two layers, with the **Texture Stamp**, mirrored battlements, the **Glyph Spray**'s stars and the **Outline Brush**. Shown at 2×:

![A brick wall across the lower half under a black sky: three courses of brown bricks lit yellow at their left ends and falling to red at their right, with black mortar between them. Black notches cut battlements along the wall's top, and a black arch in the middle holds a grey door outlined in dark grey. A white moon is at the upper left, and eight small white stars are scattered over the sky](../samples/07-detail/final.bwp "2x")

## The idea

Detail is **many small forms**, each lit like a big one. A brick has a lit side, a dark side and a dark seam round it, like a boulder a few cells across. Dots on a flat fill read as a speckled mass.

Two walls on wood, each 24 columns by 8 rows:

![Two boxes on black, labelled under them. The left, "dots", is flat brown with nine red dots scattered over it. The right, "lit forms", is two courses of bricks with black seams, lit yellow at their left ends and falling to red at their right](../samples/07-detail/idea.ans "2x")

The left box is brown spaces, wood's rung 8, with nine red `.`. The right box is the **Texture Stamp**'s brick. Each brick starts with yellow `░` on brown, runs brown, falls through brown shades on red at its right end, and has black mortar and joints round it.

The tools here lay many small forms at once. The **Outline Brush** draws the seam round a shape, the **Texture Stamp** lays a field of lit forms, the **Glyph Spray** scatters stars, haze and smoke, the **Clone Stamp** copies a detail, and **symmetry** repeats each stroke mirrored or turned.

### The outline brush

The **Outline Brush** (**Tools > Outline Brush**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd>) draws a line one cell wide on a shape's own edge cells. Each edge cell takes the ramp colour one step darker than the darkest of the shape inside it. Where that colour would add a lint finding, the cell takes a lighter shade or keeps what it had.

It reads the active layer. Either button does the same, and one stroke draws one line however often it passes a cell. Its options add **Outline the selection**, here set for the click over the yellow disc below:

![The Tool Options dock for the Outline Brush: a help text, then Size 20 with Tip Square, Pressure None, Ramp fire, Outline the selection unticked, Alpha lock unticked, and Symmetry Off](../samples/07-detail/outline-options.png)

Two discs on black, yellow on fire and grey on steel, before and after one click over each with **Size** 20 and **Tip** **Square**, the yellow with **Ramp** **fire** and the grey with **Ramp** **steel**:

![A yellow disc and a grey disc on black](../samples/07-detail/outline-before.ans "2x")

![The same discs, each with a one-cell line round its edge: light red round the yellow disc, dark grey round the grey one](../samples/07-detail/outline.ans "2x")

Thirty-six cells round each disc took the line: light red `█` on the yellow disc, dark grey `█` on the grey. The line is inside the shape, so the disc does not grow.

**Seams.** Two touching shapes on the same ramp are one shape to the brush, lined round the outside only. To draw the seam, select one shape and tick **Outline the selection**: the shape is then the ramp's cells inside the selection. Two pairs of boxes on steel, a grey box against a white one:

![Two pairs of boxes on black, each a grey box with a white box against its right side, labelled "one shape" and "two shapes"](../samples/07-detail/seam-before.ans "2x")

![The left pair lined round its outside only, dark grey round the grey box and grey round the white box, with nothing between them. The right pair has a dark grey line down the seam between the boxes as well](../samples/07-detail/seam.ans "2x")

The left pair took one click with the option unticked; columns 11 and 12, where the boxes meet, kept their colours. The right pair took two clicks with the option ticked, inside a selection of the grey box, columns 26 to 35, then of the white box, columns 36 to 45. The grey box is lined all round, and column 36 stayed white, so the seam is one line.

### The texture stamp

The **Texture Stamp** (**Tools > Texture Stamp**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>) lays a field of small lit forms along the ramp: scales, foliage, a coin hoard, brick, or mottled stone. It paints over the cells with either button, so select first to keep it to part of the canvas. Its options add **Light**, **Texture**, **Density** and **Seed**, here set for the scales below:

![The Tool Options dock for the Texture Stamp: a help text, then Size 64 with Tip Square, Pressure None, Ramp sea, Light NW, Texture Scales, Density 1.6 with Seed 1, Alpha lock unticked, and Symmetry Off](../samples/07-detail/texture-options.png)

**Texture** is the kind of form. The five kinds, each one click inside a selected box 24 columns by 8 rows, lit from the north-west at **Density** 1.6 and **Seed** 1:

![Five boxes on black, each labelled under it. "scales": small lumps of light cyan and cyan shades. "foliage": lumps of light green and yellow shades. "hoard": lumps of yellow and white shades with a few cells of light red. "brick": courses of brown bricks lit yellow at their left ends. "noise": flat grey mottled with dark grey shade](../samples/07-detail/textures.ans "2x")

Scales on sea, foliage on grass and the hoard on fire are lumps of the ramp's top colours and shades, with black between them on 103 to 117 of the 192 cells. Brick, on wood, is the courses above. Noise, on steel, is grey mottled with dark grey `▒` and `░`, with no black.

**Light** is the side the light comes from, as in tutorial 06. **Seed**, 0 to 99999, fixes the field to the canvas, so overlapping strokes uncover the same texture with no seam.

**Density** is how closely the forms pack: under 1 the lumps leave gaps, and for brick it sets how small the bricks are. Three boxes of brick on wood, at density 0.3, 1.6 and 2.5:

![Three boxes of brick on black, labelled "density 0.3", "density 1.6" and "density 2.5". The first is one big brick, the second courses of long bricks, the third courses of short ones](../samples/07-detail/density.ans "2x")

At 0.3 one brick fills the box. At 1.6 the courses are three rows tall and the bricks 15 and 16 columns long. At 2.5 the courses are two rows tall and the bricks 10 and 11 columns long.

### The glyph spray

The **Glyph Spray** (**Tools > Glyph Spray**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Y</kbd>) scatters stars, haze or smoke over the cells it passes. Its options add **Spray**, **Density** and **Seed**, here set for the stars below:

![The Tool Options dock for the Glyph Spray: a help text, then Size 64 with Tip Square, Pressure None, Ramp steel, Spray Stars, Density 100% with Seed 1, Alpha lock unticked, and Symmetry Off](../samples/07-detail/spray-options.png)

**Stars** are small glyphs in the pen's foreground: `.`, `·`, `∙`, `+`, `*` and `☼`. A star goes only where no other colour is within four columns and two rows, so stars keep off shapes.

The right button takes stars off. **Density** is how many, 30% to start with, and the **Seed** fixes them to the canvas.

A grey disc on black, before and after one click of white stars over the whole canvas at **Density** 100%, **Size** 64 and **Tip** **Square**:

![A grey disc on black](../samples/07-detail/stars-before.ans "2x")

![The same disc with seven small white stars on the black round it](../samples/07-detail/stars.ans "2x")

Seven white stars, the nearest, `+` at `2, 10`, five columns and two rows from the disc. Even at 100% the stars are sparse.

**Haze** lays long, low bands and **smoke** tall, curling wisps, along the ramp. The left button lifts the cells a rung or two, as `░` and `▒`, and the right button takes them down. A blue ground on sea, with one click of haze inside a selection of columns 0 to 28 and one of smoke inside columns 31 to 59, at **Density** 30% and **Seed** 1:

![A blue ground. On the left, a band of cyan shade on blue from row 2 to row 7, deepest at its left; on the right, tall wisps of cyan shade rising through the blue](../samples/07-detail/haze.ans "2x")

The haze is cyan `░` on blue along row 2 with cyan `▒` below, thickest at the left. The smoke is three wisps of cyan `▒` on blue edged with cyan `░`.

### The clone stamp

The **Clone Stamp** (**Tools > Clone Stamp**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd>) copies cells from one place on the canvas to another. <kbd>Ctrl</kbd>+click, with either button, sets the source cell and shows a marker there. Then paint where the copy goes: each cell the brush passes takes the cell at the same distance from the source.

It copies whole cells, glyph and both colours, so it has no **Ramp** and no **Strength**. **Size**, **Tip**, a selection and **Alpha lock** limit the cells it writes, as for any brush.

**Aligned**, ticked to start with, keeps the distance the first stroke set; untick it and each stroke starts again from the source. The stamp reads the active layer as it was when the stroke began.

Under symmetry each copy reads from the source's mirrored or turned spot and copies those cells unflipped. **File > New** and **File > Open** forget the source.

A steps file's `clone` step sets the source and paints a stroke the same way ([The clone stamp](../manual/14-cli.md#the-clone-stamp)).

### Symmetry

Mirror mode repeats a stroke. **Edit > Mirror Mode** (<kbd>Ctrl</kbd>+<kbd>M</kbd>) turns it on and off.

**Edit > Symmetry** picks **Mirror X**, **Mirror Y**, **Mirror X and Y** or **Radial**, and turns mirror mode on. The same choice is the **Symmetry** list at the foot of the **Tool Options** dock, where **Off** turns it off. The brushes, stamps, spray, rectangle, ellipse, line and fill share it; the **Ramp Gradient** has no **Symmetry**.

The mirrors are about the middle of the canvas. **Mirror X** flips a stroke left to right: column `x` comes back at the width less 1 less `x`. **Mirror Y** flips it top to bottom, and **Mirror X and Y** makes both and the half turn, four images in all.

Each picture is a canvas 21 columns by 7 rows. One stroke of the **Glyph Brush** (**Tools > Glyph Brush**, <kbd>Ctrl</kbd>+<kbd>G</kbd>) lays `▀` along row 1 from column 2 to 7, and one lays `▌` down column 2 from row 2 to 4, yellow on black. With **Symmetry** **Off**:

![A yellow corner on black at the upper left: a line of upper half blocks along the top and a line of left half blocks down its left side](../samples/07-detail/sym-off.ans "2x")

**Mirror X**:

![The corner and its mirror image at the upper right, its side line down the right](../samples/07-detail/sym-x.ans "2x")

**Mirror Y**:

![The corner with a line of lower half blocks along row 5 under it, closing it into a box open on the right](../samples/07-detail/sym-y.ans "2x")

**Mirror X and Y**:

![Two boxes open toward each other: the corner and its three images, top and bottom, left and right](../samples/07-detail/sym-xy.ans "2x")

The glyph flips with its image. Under **Mirror X** the `▌` line comes back as `▐` down column 18. Under **Mirror Y** the `▀` line comes back as `▄` along row 5, and the `▌` line lands on itself.

**Radial** turns a stroke round a centre **Folds** times, 2 to 8, 4 to start with; **Folds** is set only while **Symmetry** is **Radial**. The centre is the middle of the canvas, or tick **Radial centre at** and give a column and row.

The same strokes on a canvas 41 columns by 17 rows, `▀` along row 2 from column 22 to 27 and `▌` down column 22 from row 3 to 5, turned round `20, 8`. At 4 folds:

![The corner and three turned images round the middle of the canvas, a quarter turn apart](../samples/07-detail/radial-4.ans "2x")

At 6 folds:

![The corner, its half turn below the middle, and four images on the slant between them, drawn as steps of upper and left half blocks](../samples/07-detail/radial-6.ans "2x")

The turn is made on screen, where a cell is twice as tall as wide. At 4 folds the glyphs turn too, and the six cells of the top line come back as four down the side. At 6 folds the slanted images keep `▀` and `▌`, since CP437 has no slanted half blocks, and their lines run as steps.

Mirror mode stays on from tool to tool, and under **Mirror X** typing and pasting are mirrored too. Turn it off when the symmetric part is done. The manual's [Mirror mode and symmetry](../manual/06-symmetry.md) covers which tools follow it, the glyph each image takes, and its limits.

## Do it

Positions are column then row from `0, 0` at the top left; zoom in (<kbd>Ctrl</kbd>+<kbd>=</kbd>) to count cells. The **Rectangle** and **Ellipse** take pixel rows, two to a cell row, as in tutorial 03, so cell row 9 holds pixel rows 18 and 19.

Options carry over from tool to tool, so each step gives only the ones it changes. To select a box, take **Select** (<kbd>Ctrl</kbd>+<kbd>E</kbd>) and drag from its top left cell to its bottom right; **Selection > Deselect** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>A</kbd>) drops it.

1. **A new canvas.** On the start screen, set **Width** to 60 and **Height** to 20, leave **iCE colours** ticked, and press **New**.

2. **The wall.** Select the box from `0, 9` to `59, 19`. Take the **Texture Stamp** (**Tools > Texture Stamp**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>) and set **Ramp** to **wood**, **Light** to **NW**, **Texture** to **Brick**, **Density** to 1.6, **Seed** to 69, **Size** to 64 and **Tip** to **Square**, with **Symmetry** **Off**. Click once at `29, 14`. Then **Selection > Deselect**:

    ![Three courses of brown bricks across the bottom of a black canvas, lit yellow at their left ends and falling to red at their right, with black mortar and joints](../samples/07-detail/step-01.ans "2x")

    The courses are rows 9 to 11, 13 to 15 and 17 to 19, with black mortar on rows 12 and 16.

3. **The battlements.** Take the **Rectangle** (**Tools > Rectangle**, <kbd>Ctrl</kbd>+<kbd>U</kbd>) and tick **Filled**. Left-click black, the first swatch. Choose **Edit > Symmetry > Mirror X**. Drag from `3, 18` to `6, 23`, from `13, 18` to `16, 23`, and from `23, 18` to `26, 23`:

    ![The wall with black notches cut into its top course, leaving seven merlons](../samples/07-detail/step-02.ans "2x")

    **Mirror X** cuts the other three notches, at columns 33 to 36, 43 to 46 and 53 to 56. Set **Symmetry** to **Off**.

4. **The gate.** Take the **Ellipse** (**Tools > Ellipse**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>O</kbd>); black and **Filled** carry over. Drag from `25, 25` to `34, 37`. Take the **Rectangle** and drag from `25, 31` to `34, 39`:

    ![The wall with a black arch cut in the middle of its two lower courses](../samples/07-detail/step-03.ans "2x")

    The gate is black from column 25 to 34, with its round top on rows 13 and 14.

5. **The moon.** Take the **Ramp Shade Brush** (**Tools > Ramp Shade Brush**, <kbd>Ctrl</kbd>+<kbd>T</kbd>) and set **Ramp** to **steel**, **Strength** to 100%, **Tip** to **Round** and **Size** to 7. Click three times at `7, 3` to take the black up steel to white:

    ![The wall under a white moon at the upper left](../samples/07-detail/step-04.ans "2x")

    The moon is 17 cells of white `█`.

6. **The stars.** Take the **Glyph Spray** (**Tools > Glyph Spray**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Y</kbd>) and left-click white, the last swatch. Set **Spray** to **Stars**, **Density** to 60%, **Seed** to 1, **Size** to 64 and **Tip** to **Square**. **Symmetry** is **Off**. Click once at `30, 4`:

    ![The wall and the moon under eight small white stars](../samples/07-detail/step-05.ans "2x")

    Eight stars, white on black: `·` at `27, 1`, `+` at `44, 1`, `∙` at `19, 2`, `*` at `34, 2`, `·` at `20, 5`, `.` at `27, 5`, `∙` at `42, 5` and `.` at `52, 6`. None is within four columns and two rows of the wall or the moon.

7. **The door.** **Layer > New Cells Layer**. In the **Layers** dock, double-click the new layer's name and type `door`. Take the **Ellipse** and left-click grey, the eighth swatch. Drag from `26, 28` to `33, 36`. Take the **Rectangle** and drag from `26, 32` to `33, 39`:

    ![The wall with a grey door in the gate, a strip of black left round it](../samples/07-detail/step-06.ans "2x")

    The gate's black shows round the door. On its own layer, the door can be moved or redrawn without touching the wall:

    ![The Layers dock: door, highlighted as the active layer, above Background, both with their visibility boxes ticked; Alpha Lock unticked and Kind Cells](../samples/07-detail/layers.png)

8. **The door's outline.** Take the **Outline Brush** (**Tools > Outline Brush**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd>). **Ramp** is still **steel**; leave **Outline the selection** unticked. Set **Size** to 20 and **Tip** to **Square**, and click once at `29, 16`. The brush reads the door layer, so it lines the door only:

    ![The finished piece: the wall with its battlements and gate, the grey door outlined in dark grey, under the moon and the stars](../samples/07-detail/final.bwp "2x")

    Eighteen cells of the door's edge went to dark grey `█`. Row 19 runs off the canvas and has no line across it. The **Lint** dock lists eight findings; scroll for the last:

    ![The Lint dock reading All named ramps: seven of the eight findings in view, blank-edge-rows at 0,0, trailing-black at 0,8, 0,12 and 34,16, and speckle at 6,13 and 25,13 on fire and at 38,13 on skin, with the list's scroll bar beside them; under the list, 8 findings (4 speckle, 3 trailing-black, 1 blank-edge-rows), noise 0.0000, iCE on](../samples/07-detail/lint.png)

    The four specks are spaces near brick ends, read along **fire** and **skin** because the list starts at **All named ramps**. Pick **wood** and they go.

    The other four are about IRC: a blank top row, rows 8 and 12 all black, and the black at the end of row 16. Tutorial 11, *Made for IRC*, deals with them.

9. **Save it.** **File > Save As** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>), with a name ending `.bwp`, so the two layers are kept.

## Check it

**Turn the symmetry off before the texture.** Under a mirror, the texture stamp folds its field and its light about the middle of the canvas. The wall stamped with **Mirror X** still on:

![The wall with the bricks on its right half lit at their right ends and falling to the left, and a long brick across the middle lit at both ends](../samples/07-detail/mirror-light.ans "2x")

Right of the middle the bricks are lit from the north-east, and the brick across the middle is lit at both ends. Undo (<kbd>Ctrl</kbd>+<kbd>Z</kbd>), set **Symmetry** to **Off**, and stamp again.

**Outline shapes, not textures.** Each brick is a shape to the outline brush. The brush clicked over the wall on the **Background** layer, with **Ramp** **wood** and **Size** 64:

![The wall with most of its bricks ringed in red, their brown left mostly in a strip through the middle of each course](../samples/07-detail/stickers.ans "2x")

Most brick edges went to red spaces, wood's rung 4, and the bricks turn into cut-outs. Undo, and outline only the shapes you draw on their own layer.

**Spray stars with the symmetry off.** The stars sprayed with **Mirror X** still on from the battlements:

![The sky with stars in pairs mirrored about the middle, and four more on the right with no partner](../samples/07-detail/stars-mirrored.ans "2x")

Eight of the twelve stars are mirror pairs. The other four have no partner, because theirs would land beside the moon.

A sky in pairs reads as a pattern. Undo, set **Symmetry** to **Off**, and spray again.

## Try it

Download [try.bwp](../samples/07-detail/try.bwp) and open it (**File > Open**, <kbd>Ctrl</kbd>+<kbd>O</kbd>):

![The brick wall with its black gate under the white moon, with no battlements and no stars](../samples/07-detail/try.bwp "2x")

It is the wall, gate and moon on one layer.

1. Cut battlements with two notches a side, four columns wide and three rows deep, the left two at columns 5 to 8 and 15 to 18, mirrored on the right.
2. Scatter stars over the sky with **Seed** 2 and **Density** 60%, none of them mirrored.
3. The gate was cut with **Symmetry** **Off**. Would **Mirror X** have changed it?

<details markdown="1">
<summary>Answers</summary>

1. Take the **Rectangle**, tick **Filled**, left-click black, the first swatch, and choose **Edit > Symmetry > Mirror X**. Drag from `5, 18` to `8, 23` and from `15, 18` to `18, 23`. **Mirror X** cuts columns 41 to 44 and 51 to 54. Then set **Symmetry** to **Off**.

2. Take the **Glyph Spray**, left-click white, the last swatch, and set **Spray** to **Stars**, **Density** to 60%, **Seed** to 2, **Size** to 64 and **Tip** to **Square**. With **Symmetry** **Off**, click once at `30, 4`:

    ![The wall with four notches along its top and six small white stars over the sky](../samples/07-detail/try-answer.ans "2x")

    Six stars, white on black: `.` at `18, 1`, `∙` at `52, 1`, `·` at `28, 2`, `∙` at `37, 5`, `*` at `43, 5` and `.` at `59, 6`. No two are mirror images.

3. No. The gate runs from column 25 to 34, and on a canvas 60 columns wide **Mirror X** repeats column 25 at 34 and 34 at 25, so the gate's mirror image is the gate.

</details>

Tutorial 08, *Composing a scene*, goes on to selections, moving, flipping and turning what you've drawn, paste modes, guides, a reference image and the Library.
