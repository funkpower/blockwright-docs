Title: Detail
Checked: Blockwright 0.1.0 (fd10778)

# Detail

## Goal

Put detail on a piece with the tools that make many small things at once. You'll make this castle wall under a night sky, 60 columns by 20 rows, on two layers, with the **Texture Stamp**, mirrored battlements, the **Glyph Spray**'s stars and the **Outline Brush**. Shown at 2×:

![A brick wall across the lower half under a black sky: three courses of brown bricks lit yellow at their left ends and falling to red at their right, with black mortar between them. Black notches cut battlements along the wall's top, and a black arch in the middle holds a grey door outlined in dark grey. A white moon is at the upper left, and eight small white stars are scattered over the sky](../samples/07-detail/final.bwp "2x")

## The idea

Detail is **many small forms**, each lit like a big one. A brick, a scale or a coin is a form with a lit side, a dark side and a dark seam round it, the same as a boulder, only a few cells across. A flat fill sprinkled with dots doesn't read as bricks or scales: it reads as a speckled mass.

Two walls on wood, each 24 columns by 8 rows:

![Two boxes on black, labelled under them. The left, "dots", is flat brown with nine red dots scattered over it. The right, "lit forms", is two courses of bricks with black seams, lit yellow at their left ends and falling to red at their right](../samples/07-detail/idea.ans "2x")

The left box is brown spaces, wood's rung 8, with nine red `.` on brown in it. The right box is the **Texture Stamp**'s brick: two courses of bricks, rows 1 to 3 and 5 to 7, black mortar on rows 4 and 8, and black joints between the bricks. The brick on row 1 from column 34 to 49 starts with two cells of yellow `░` on brown, rung 9, runs brown, and falls through brown `▓`, `▒` and `░` on red at its right end; rows 2 and 3 of it are a rung and two rungs darker. A brick has a lit end, a fall and a seam round it; the dots are nine marks on one flat colour.

Drawing a hundred small forms by hand is slow. The tools in this tutorial lay them for you: the **Outline Brush** draws the seam round a shape, the **Texture Stamp** lays a field of small lit forms, the **Glyph Spray** scatters stars, haze and smoke, the **Clone Stamp** copies a detail you've drawn, and **symmetry** repeats each stroke as its mirror image or turned round a centre.

### The outline brush

The **Outline Brush** (**Tools > Outline Brush**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd>) draws a line one cell wide round a shape, on the shape's own edge cells. Each edge cell under the brush aims for the ramp colour one step darker than the darkest of the shape just inside it, so the line is the shape's own colour, a step down. Where that colour would add a lint finding, the cell takes a lighter shade instead, or keeps what it had. It reads the active layer. Either button does the same, and one stroke draws one line, however often it passes over a cell. Its options add **Outline the selection**, here set for the click over the yellow disc below:

![The Tool Options dock for the Outline Brush: a help text, then Size 20 with Tip Square, Pressure None, Ramp fire, Outline the selection unticked, Alpha lock unticked, and Symmetry Off](../samples/07-detail/outline-options.png)

Two discs on black, yellow on the fire ramp and grey on steel, before, and after one click over each with **Size** 20 and **Tip** **Square**, the yellow with **Ramp** **fire** and the grey with **Ramp** **steel**:

![A yellow disc and a grey disc on black](../samples/07-detail/outline-before.ans "2x")

![The same discs, each with a one-cell line round its edge: light red round the yellow disc, dark grey round the grey one](../samples/07-detail/outline.ans "2x")

Thirty-six cells round each disc took the line. On the yellow disc, yellow `█` went to light red `█`, the colour below yellow on fire: row 2 from column 5 to 12, row 8 the same, and the cells down each side between. On the grey disc, grey went to dark grey `█`, the colour below grey on steel, in the same places 20 columns to the right. The line is inside the shape, so the disc is no bigger than before.

**Seams.** Two shapes on the same ramp that touch are one shape to the brush: it lines them round the outside and draws nothing between them. To draw the seam, select one shape and tick **Outline the selection**: the shape is then the ramp's cells inside the selection, and the cells outside it are outside, the shape beside it too. Two pairs of boxes on steel, a grey box against a white one:

![Two pairs of boxes on black, each a grey box with a white box against its right side, labelled "one shape" and "two shapes"](../samples/07-detail/seam-before.ans "2x")

![The left pair lined round its outside only, dark grey round the grey box and grey round the white box, with nothing between them. The right pair has a dark grey line down the seam between the boxes as well](../samples/07-detail/seam.ans "2x")

The left pair took one click with the option unticked. The grey box's edge cells went to dark grey `█`, column 2 and rows 1 and 8, and the white box's to grey, rows 1 and 8 and column 21; from row 2 to 7, columns 11 and 12, where the boxes meet, kept their colours. The right pair took two clicks with the option ticked: one inside a selection of the grey box, columns 26 to 35, and one inside a selection of the white box, columns 36 to 45. The grey box is lined all round, column 35 too, and the white box on its top, bottom and right. Column 36, the white box's left column, stayed white: the seam is one line, the grey box's.

### The texture stamp

The **Texture Stamp** (**Tools > Texture Stamp**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>) lays a field of small lit forms along the ramp: scales, foliage, a coin hoard, brick, or mottled stone. It paints over whatever the cells held, with either button, so make a selection first to keep it to a part of the canvas. Its options add **Light**, **Texture**, **Density** and **Seed**, here set for the scales below:

![The Tool Options dock for the Texture Stamp: a help text, then Size 64 with Tip Square, Pressure None, Ramp sea, Light NW, Texture Scales, Density 1.6 with Seed 1, Alpha lock unticked, and Symmetry Off](../samples/07-detail/texture-options.png)

**Texture** is the kind of form. The five kinds, each stamped with one click inside a selection of a box 24 columns by 8 rows, lit from the north-west at **Density** 1.6 and **Seed** 1:

![Five boxes on black, each labelled under it. "scales": small lumps of light cyan and cyan shades. "foliage": lumps of light green and yellow shades. "hoard": lumps of yellow and white shades with a few cells of light red. "brick": courses of brown bricks lit yellow at their left ends. "noise": flat grey mottled with dark grey shade](../samples/07-detail/textures.ans "2x")

Scales, on sea, are lumps of light cyan `▓`, `▒` and `░` on cyan, light cyan `█`, cyan spaces and three cells of cyan `▓` on blue: 117 of the box's 192 cells are black, between the lumps. Foliage, on grass, is lumps of yellow `▒`, `░` and `▓` on light green, light green `█`, light green `▓` and `▒` on green and one cell of yellow `█`, and 112 cells of black. The hoard, on fire, is lumps of white `░`, `▓` and `▒` on yellow, yellow `█`, and yellow `▓`, `▒` and `░` on light red, with two cells of white `█` and two of light red `█`, and 103 cells of black. Brick, on wood, is courses of bricks like the ones above. Noise, on steel, is 176 cells of dark grey `▒` on grey and 16 of dark grey `░` on grey, with no black: stone with a grain, not forms.

**Light** is the side the light comes from, as in tutorial 06, and the forms are lit from it. **Seed** picks the texture, from 0 to 99999: the field is fixed to the canvas by its seed, so a second click or a drag over the same cells uncovers the same texture, with no seam where strokes overlap, and the same seed paints the same cells every time. **Density** is how closely the forms pack: under 1, the lumps leave gaps between them; for brick, it is how small the bricks are. Three boxes of brick on wood, at density 0.3, 1.6 and 2.5:

![Three boxes of brick on black, labelled "density 0.3", "density 1.6" and "density 2.5". The first is one big brick, the second courses of long bricks, the third courses of short ones](../samples/07-detail/density.ans "2x")

At 0.3 one brick fills the box from column 2 to its right edge and from row 1 to its bottom, with the end of another at column 0. At 1.6 the top course is three rows tall, rows 1 to 3, and the whole bricks are 15 and 16 columns long. At 2.5 the courses are two rows tall, rows 1 and 2 and rows 4 and 5, and the whole bricks are 10 and 11 columns long.

### The glyph spray

The **Glyph Spray** (**Tools > Glyph Spray**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Y</kbd>) scatters stars, haze or smoke over the cells it passes. Its options add **Spray**, **Density** and **Seed**, here set for the stars below:

![The Tool Options dock for the Glyph Spray: a help text, then Size 64 with Tip Square, Pressure None, Ramp steel, Spray Stars, Density 100% with Seed 1, Alpha lock unticked, and Symmetry Off](../samples/07-detail/spray-options.png)

**Stars** are small glyphs in the pen's foreground: `.`, `·`, `∙`, `+`, `*` and `☼`. A star goes only on open ground: no other colour within four columns and two rows of it, so stars keep off shapes. The right button takes stars off again. **Density** is how many stars, as a percentage, 30% to start with. Like the texture, the stars are fixed to the canvas by their **Seed**. A grey disc on black, before, and after one click of white stars over the whole canvas at **Density** 100%, with **Size** 64 and **Tip** **Square**:

![A grey disc on black](../samples/07-detail/stars-before.ans "2x")

![The same disc with seven small white stars on the black round it](../samples/07-detail/stars.ans "2x")

Seven stars, white on black: `·` at `27, 1`, `*` at `34, 2`, `.` at `27, 5`, `·` at `36, 5`, `∙` at `27, 9`, `·` at `34, 9` and `+` at `2, 10`. The nearest to the disc, `2, 10`, is five columns and two rows from its nearest cell. Even at 100% the stars are sparse.

**Haze** lays long, low bands and **smoke** tall, curling wisps, along the ramp: the left button lifts the cells a rung or two, as `░` and `▒`, and the right button takes them down. A blue ground on sea, then one click of haze inside a selection of columns 0 to 28 and one of smoke inside a selection of columns 31 to 59, at **Density** 30% and **Seed** 1:

![A blue ground. On the left, a band of cyan shade on blue from row 2 to row 7, deepest at its left; on the right, tall wisps of cyan shade rising through the blue](../samples/07-detail/haze.ans "2x")

The haze is cyan `░` on blue along row 2 from column 0 to 27, and cyan `▒` on blue below it, thickest at the left: on row 3 from column 0 to 25, on row 6 from 0 to 8, then `░` on row 7. The smoke rises in three wisps of cyan `▒` on blue edged with cyan `░` on blue: from top to bottom round columns 32 to 38 and 53 to 59, and from row 6 down round columns 42 to 47. A cell of haze is two rungs up from blue in the middle of a band and one at its edge.

### The clone stamp

The **Clone Stamp** (**Tools > Clone Stamp**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd>) copies cells from one place on the canvas to another: a window you've drawn to the next bay, a knot to another plank. <kbd>Ctrl</kbd>+click, with either button, sets the source cell; it paints nothing, and a marker shows where it is. Then paint where the copy goes: the cell you press on takes the source cell, and each cell the brush passes takes the cell at the same distance from the source. It copies whole cells, glyph, both colours and all, so its options have no **Ramp** and no **Strength**, and **Size**, **Tip**, a selection and **Alpha lock** limit the cells it writes, as for any brush.

**Aligned**, in its options, is ticked to start with: a second stroke keeps the distance the first one set, so it goes on copying the same stretch. Untick it and each stroke starts again from the source. The stamp reads the canvas as it was when the stroke began, so a copy that runs over its own source copies what was there before. It copies within the active layer. Under symmetry each mirrored or turned copy reads from the source's mirrored or turned spot, not from the source itself, and the cells it finds there are copied as they are, not flipped. **File > New** and **File > Open** forget the source: <kbd>Ctrl</kbd>+click again before you paint.

A steps file's `clone` step sets the source and paints a stroke the same way ([The clone stamp](../manual/14-cli.md#the-clone-stamp)).

### Symmetry

Mirror mode repeats a stroke. **Edit > Mirror Mode** (<kbd>Ctrl</kbd>+<kbd>M</kbd>) turns it on and off. **Edit > Symmetry** picks what it repeats a stroke as, **Mirror X**, **Mirror Y**, **Mirror X and Y** or **Radial**, and picking one turns mirror mode on. The same choice is the **Symmetry** list at the foot of the **Tool Options** dock, where **Off** turns mirror mode off. It is one setting, shared by the brushes, the stamps, the spray, the rectangle, the ellipse, the line and the fill. The **Ramp Gradient** has no **Symmetry**.

The mirrors are about the middle of the canvas. **Mirror X** repeats a stroke flipped left to right: column `x` comes back at the canvas's width less 1 less `x`. **Mirror Y** flips it top to bottom the same way, and **Mirror X and Y** makes both and the half turn as well, four images in all. On a canvas an odd number of cells across, the middle column is its own mirror. Each picture here is a canvas 21 columns by 7 rows with one stroke of the **Glyph Brush** (**Tools > Glyph Brush**, <kbd>Ctrl</kbd>+<kbd>G</kbd>) laying `▀` along row 1 from column 2 to 7 and one laying `▌` down column 2 from row 2 to 4, yellow on black. With **Symmetry** **Off**:

![A yellow corner on black at the upper left: a line of upper half blocks along the top and a line of left half blocks down its left side](../samples/07-detail/sym-off.ans "2x")

**Mirror X**:

![The corner and its mirror image at the upper right, its side line down the right](../samples/07-detail/sym-x.ans "2x")

**Mirror Y**:

![The corner with a line of lower half blocks along row 5 under it, closing it into a box open on the right](../samples/07-detail/sym-y.ans "2x")

**Mirror X and Y**:

![Two boxes open toward each other: the corner and its three images, top and bottom, left and right](../samples/07-detail/sym-xy.ans "2x")

The glyph flips with its image. Under **Mirror X** the `▀` line comes back along row 1 from column 13 to 18, and the `▌` line as `▐` down column 18, rows 2 to 4. Under **Mirror Y** the `▀` line comes back as `▄` along row 5, columns 2 to 7, and the `▌` line, on rows 2 to 4 of a canvas 7 rows tall, lands on itself. **Mirror X and Y** has all of those and `▄` along row 5 from column 13 to 18, the half turn.

**Radial** turns a stroke round a centre, **Folds** times: 2 to 8, 4 to start with. **Folds** can be set only while **Symmetry** is **Radial**. The centre is the middle of the canvas; tick **Radial centre at** and give a column and row to turn round that cell instead. The same strokes on a canvas 41 columns by 17 rows, `▀` along row 2 from column 22 to 27 and `▌` down column 22 from row 3 to 5, turned round `20, 8`. At 4 folds:

![The corner and three turned images round the middle of the canvas, a quarter turn apart](../samples/07-detail/radial-4.ans "2x")

At 6 folds:

![The corner, its half turn below the middle, and four images on the slant between them, drawn as steps of upper and left half blocks](../samples/07-detail/radial-6.ans "2x")

The turn is made on screen, where a cell is twice as tall as it is wide, and each image is rounded to the nearest cell. At 4 folds the quarter turn clockwise is `▀` along row 9 from column 26 to 30 and `▐` down column 32 from row 9 to 12: the glyphs are turned a quarter too, and the six cells of the top line come back as four down the side. The half turn is `▄` along row 14 from column 13 to 18 and `▐` down column 18 from row 11 to 13, the exact flip both ways. The three-quarter turn is `▌` down column 8 from row 5 to 7 and `▄` along row 7 from column 10 to 14. At 6 folds the half turn is the same, and the four images a sixth and a third of a turn either way keep `▀` and `▌` as they are, since CP437 has no half blocks on the slant. Their lines run as steps of whole cells: at the upper left, `▀` at `12, 2` and `13, 2`, at `11, 3` and `12, 3`, and at `11, 4`.

Mirror mode stays on, from tool to tool, until you turn it off. Under **Mirror X**, typing and pasting are mirrored too. Turn it off as soon as the symmetric part is done: **Symmetry** **Off**, or <kbd>Ctrl</kbd>+<kbd>M</kbd>.

## Do it

You'll build the piece back to front: the wall, its battlements and gate, the moon and the stars, then the door on a layer of its own. The positions are column then row from `0, 0` at the top left; zoom in (<kbd>Ctrl</kbd>+<kbd>=</kbd>) so you can count cells. The **Rectangle** and the **Ellipse** take pixel positions, as in tutorial 03: the column, then the pixel row, two to a cell row, so cell row 9 holds pixel rows 18 and 19. Set the options in the **Tool Options** dock; they carry over from tool to tool, so each step gives only the ones it changes. To select a box, take the **Select** tool (<kbd>Ctrl</kbd>+<kbd>E</kbd>) and drag from its top left cell to its bottom right cell; **Selection > Deselect** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>A</kbd>) drops it.

1. **A new canvas.** On the start screen, set **Width** to 60 and **Height** to 20, leave **iCE colours** ticked, and press **New**.

2. **The wall.** Select the box from `0, 9` to `59, 19`. Take the **Texture Stamp** (**Tools > Texture Stamp**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>) and set **Ramp** to **wood**, **Light** to **NW**, **Texture** to **Brick**, **Density** to 1.6, **Seed** to 69, **Size** to 64 and **Tip** to **Square**, with **Symmetry** **Off**. Click once at `29, 14`; the brush covers the selection. Then **Selection > Deselect**:

    ![Three courses of brown bricks across the bottom of a black canvas, lit yellow at their left ends and falling to red at their right, with black mortar and joints](../samples/07-detail/step-01.ans "2x")

    The courses are rows 9 to 11, 13 to 15 and 17 to 19, with black mortar on rows 12 and 16 and black joints between the bricks. The brick on row 9 from column 17 to 33 starts with two cells of yellow `░` on brown and falls to brown `░` on red at its right end; its rows 10 and 11 are a rung and two rungs darker. The seed fixes where the joints fall; 69 is the one in the pictures.

3. **The battlements.** Take the **Rectangle** (**Tools > Rectangle**, <kbd>Ctrl</kbd>+<kbd>U</kbd>) and tick **Filled**. Left-click black, the first swatch. Choose **Edit > Symmetry > Mirror X**. Drag from `3, 18` to `6, 23`, from `13, 18` to `16, 23`, and from `23, 18` to `26, 23`:

    ![The wall with black notches cut into its top course, leaving seven merlons](../samples/07-detail/step-02.ans "2x")

    Each drag cuts a notch four columns wide through rows 9 to 11, and **Mirror X** cuts its mirror image: columns 3 to 6, 13 to 16 and 23 to 26, and 33 to 36, 43 to 46 and 53 to 56. Seven merlons stand between them, the middle one from column 27 to 32. The battlements are done, so set **Symmetry** to **Off**.

4. **The gate.** Take the **Ellipse** (**Tools > Ellipse**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>O</kbd>); black is still the foreground and **Filled** still ticked. Drag from `25, 25` to `34, 37`. Take the **Rectangle** and drag from `25, 31` to `34, 39`:

    ![The wall with a black arch cut in the middle of its two lower courses](../samples/07-detail/step-03.ans "2x")

    The gate is black from column 25 to 34 on rows 15 to 19, with its round top on rows 13 and 14. Two cells on the arch's right edge are half cells, `▀` brown on black: `33, 13` and `34, 14`.

5. **The moon.** Take the **Ramp Shade Brush** (**Tools > Ramp Shade Brush**, <kbd>Ctrl</kbd>+<kbd>T</kbd>) and set **Ramp** to **steel**, **Strength** to 100%, **Tip** to **Round** and **Size** to 7. Click three times at `7, 3`. Each click at 100% lays a whole colour, so three take the black up steel to white:

    ![The wall under a white moon at the upper left](../samples/07-detail/step-04.ans "2x")

    The moon is 17 cells of white `█`: columns 5 to 9 on rows 2 and 4, and 4 to 10 on row 3.

6. **The stars.** Take the **Glyph Spray** (**Tools > Glyph Spray**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Y</kbd>) and left-click white, the last swatch. Set **Spray** to **Stars**, **Density** to 60%, **Seed** to 1, **Size** to 64 and **Tip** to **Square**. **Symmetry** is **Off**. Click once at `30, 4`:

    ![The wall and the moon under eight small white stars](../samples/07-detail/step-05.ans "2x")

    Eight stars, white on black: `·` at `27, 1`, `+` at `44, 1`, `∙` at `19, 2`, `*` at `34, 2`, `·` at `20, 5`, `.` at `27, 5`, `∙` at `42, 5` and `.` at `52, 6`. None is within four columns and two rows of the wall or the moon: the spray found the open sky.

7. **The door.** **Layer > New Cells Layer**. In the **Layers** dock, double-click the new layer's name and type `door`. Take the **Ellipse** and left-click grey, the eighth swatch. Drag from `26, 28` to `33, 36`. Take the **Rectangle** and drag from `26, 32` to `33, 39`:

    ![The wall with a grey door in the gate, a strip of black left round it](../samples/07-detail/step-06.ans "2x")

    The door is grey from column 26 to 33 on rows 15 to 19, and from 28 to 31 on row 14; `27, 14` and `32, 14` are half cells, black over grey. The gate's black shows round it. On a layer of its own, the door can be moved or redrawn without touching the wall:

    ![The Layers dock: door, highlighted as the active layer, above Background, both with their visibility boxes ticked; Alpha Lock unticked and Kind Cells](../samples/07-detail/layers.png)

8. **The door's outline.** Take the **Outline Brush** (**Tools > Outline Brush**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd>). **Ramp** is still **steel**; leave **Outline the selection** unticked. Set **Size** to 20 and **Tip** to **Square**, and click once at `29, 16`. The brush reads the door layer's cells, so it lines the door and not the wall:

    ![The finished piece: the wall with its battlements and gate, the grey door outlined in dark grey, under the moon and the stars](../samples/07-detail/final.bwp "2x")

    Eighteen cells of the door's edge went to dark grey `█`: row 14 from column 27 to 32, `26, 15`, `27, 15`, `32, 15` and `33, 15`, and columns 26 and 33 from row 16 to 19. Row 19, where the door runs off the bottom of the canvas, has no line across it. The **Lint** dock lists eight findings; scroll its list for the last:

    ![The Lint dock reading All named ramps: seven of the eight findings in view, blank-edge-rows at 0,0, trailing-black at 0,8, 0,12 and 34,16, and speckle at 6,13 and 25,13 on fire and at 38,13 on skin, with the list's scroll bar beside them; under the list, 8 findings (4 speckle, 3 trailing-black, 1 blank-edge-rows), noise 0.0000, iCE on](../samples/07-detail/lint.png)

    The four specks are spaces near brick ends, red at `6, 13` and `25, 13` and brown at `38, 13` and `14, 17`, read along **fire** and **skin**, ramps that run through red too: the list at the top of the dock starts at **All named ramps**. Pick **wood**, the ramp the wall is on, and the specks go. The other four are about IRC: a blank top row, rows 8 and 12 all black, and the black at the end of row 16. Black sky and black mortar raise them; tutorial 11, *Made for IRC*, deals with them.

9. **Save it.** **File > Save As** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>), with a name ending `.bwp`, so the two layers are kept.

## Check it

**Turn the symmetry off before the texture.** Under a mirror, the texture stamp folds its field about the middle of the canvas, light and all. The wall stamped with **Mirror X** still on:

![The wall with the bricks on its right half lit at their right ends and falling to the left, and a long brick across the middle lit at both ends](../samples/07-detail/mirror-light.ans "2x")

The left half is the wall of step 2. Right of the middle the light comes from the north-east: the brick on row 9 from column 44 to 59 runs from brown `▒` on red at its left end up to yellow `▒` on brown at columns 58 and 59, and the brick on row 9 from column 17 to 42, across the middle, is lit at both ends. Two lights on one wall. Undo (<kbd>Ctrl</kbd>+<kbd>Z</kbd>), set **Symmetry** to **Off**, and stamp again.

**Outline shapes, not textures.** Each brick is a shape to the outline brush. The brush clicked over the wall on the **Background** layer, with **Ramp** **wood** and **Size** 64:

![The wall with most of its bricks ringed in red, their brown left mostly in a strip through the middle of each course](../samples/07-detail/stickers.ans "2x")

Most of the brick edges went to red spaces, wood's rung 4, or were red already; the rest went darker but stopped short of red, or kept what they had. Rows 9, 11, 13 and 15 are nearly all red, and the bricks keep their brown and its shades mostly along rows 10, 14, 18 and 19, between red ends. The texture is lit already; the outline turns its bricks into cut-outs. Undo, and outline the shapes you draw, a door or a sign, on their own layer.

**Spray stars with the symmetry off.** The stars sprayed with **Mirror X** still on from the battlements:

![The sky with stars in pairs mirrored about the middle, and four more on the right with no partner](../samples/07-detail/stars-mirrored.ans "2x")

Eight of the twelve stars are mirror pairs: `·` at `27, 1` and `32, 1`, `∙` at `19, 2` and `40, 2`, `·` at `20, 5` and `39, 5`, and `.` at `27, 5` and `32, 5`. The other four, at `57, 1`, `49, 2`, `57, 5` and `47, 6`, have no partner: theirs would land beside the moon, off open ground. A sky in pairs reads as a pattern. Undo, set **Symmetry** to **Off**, and spray again.

## Try it

Download [try.bwp](../samples/07-detail/try.bwp) and open it (**File > Open**, <kbd>Ctrl</kbd>+<kbd>O</kbd>):

![The brick wall with its black gate under the white moon, with no battlements and no stars](../samples/07-detail/try.bwp "2x")

It is the wall with its gate and the moon, on one layer: no battlements, no stars, no door.

1. Cut battlements with two notches a side, four columns wide and three rows deep, the left two at columns 5 to 8 and 15 to 18, mirrored on the right.
2. Scatter stars over the sky with **Seed** 2 and **Density** 60%, none of them mirrored.
3. The gate was cut with **Symmetry** **Off**. Would **Mirror X** have changed it?

<details markdown="1">
<summary>Answers</summary>

1. Take the **Rectangle**, tick **Filled**, left-click black, the first swatch, and choose **Edit > Symmetry > Mirror X**. Drag from `5, 18` to `8, 23` and from `15, 18` to `18, 23`. **Mirror X** cuts columns 41 to 44 and 51 to 54. Then set **Symmetry** to **Off**.

2. Take the **Glyph Spray**, left-click white, the last swatch, and set **Spray** to **Stars**, **Density** to 60%, **Seed** to 2, **Size** to 64 and **Tip** to **Square**. With **Symmetry** **Off**, click once at `30, 4`:

    ![The wall with four notches along its top and six small white stars over the sky](../samples/07-detail/try-answer.ans "2x")

    The notches are black on rows 9 to 11 at columns 5 to 8, 15 to 18, 41 to 44 and 51 to 54. Six stars, white on black: `.` at `18, 1`, `∙` at `52, 1`, `·` at `28, 2`, `∙` at `37, 5`, `*` at `43, 5` and `.` at `59, 6`. No two of them are mirror images.

3. No. The gate runs from column 25 to 34, and on a canvas 60 columns wide **Mirror X** repeats column 25 at 34 and 34 at 25: the gate's mirror image is the gate. A shape centred on the canvas comes out the same with the mirror on or off.

</details>

Tutorial 08, *Composing a scene*, goes on from here: selections, moving, flipping and turning what you've drawn, paste modes, guides, a reference image and the Library.
