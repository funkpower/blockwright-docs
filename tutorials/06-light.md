Title: Light
Checked: Blockwright 0.1.0 (6cb21c1)

# Light

## Goal

Light a whole scene from one direction. You'll make this boulder and standing stone on two hills under a sky, 60 columns by 20 rows, on four layers, with the form brush's **Light**, **Glint** and **Form rim light** and with the **Rim Light Brush**. Shown at 2×:

![A grey boulder on the right and a smaller stone on the left, standing on two green hills under a sky that is light cyan in the top right corner, cyan over the right, and blue over the left. The boulder is grey over its upper right with a small white spot near its right side, and falls through dark grey to dark grey shades at its lower left. The stone is white at its upper right and falls through grey and dark grey to dark grey shades at its lower left. The hills are a rung lighter along their edges that face the upper right](../samples/06-light/final.bwp "2x")

## The idea

A scene has **one light**. Every form in it is lit from the same side, so every lit side faces the same way and every shadow falls away from it. Two forms lit from different sides read as two suns.

Four domes the same size on steel, each a disc on a layer of its own shaded with one click of the **Form Brush**. The two on the left are both lit from the north-west; of the two on the right, the third is lit from the north-west and the fourth from the north-east:

![Four grey domes in a row on black, labelled under them. The left two, "one light", and the third are white at the upper left and fall through grey to dark grey shades at the lower right. The fourth is lit from the other side: white at the upper right, falling through grey to dark grey at the lower left. "two lights" is under the third and fourth](../samples/06-light/idea.ans "2x")

Each of the first three is solid white on its upper left: three cells on row 1 and four on rows 2 and 3. From there it steps down a rung at a time to dark grey `█` and on to dark grey `▓`, `▒` and `░` on black at its lower right. The fourth is lit from the north-east instead. It is white on its upper right, 24 cells across rows 1 to 4, and its lower left goes down only to dark grey `█` and dark grey `▓` on black, with no `▒` or `░`. Side by side, the third and fourth look lit by two lights.

Which side to light from is up to you. The upper left is the usual choice and Blockwright's default, which tutorial 05 used. Choose it once, at the start, and give it to every form and every edge in the piece. Anything glowing in the picture (a lamp, a fire, the sun itself) is the light and can set the side: light the forms from where it is.

### The form brush's light

The **Form Brush**'s options, set for the stone's form in step 7 below:

![The Tool Options dock for the Form Brush: a help text, then Size 26 with Tip Square, Pressure None with Strength 100%, Ramp steel, Light NE with Form Dome, Form rim light ticked with Glint unticked, Alpha lock ticked, and Symmetry Off](../samples/06-light/form-options.png)

Tutorial 05 left **Light** at **NW**; the stone is lit from **NE**. **Light** is a point of the compass: **N**, **NE**, **E**, **SE**, **S**, **SW**, **W** or **NW**, the side the light comes from, with north at the top of the canvas. Eight domes, each lit from the point it stands at round the rose:

![Eight grey domes in a ring on black round the words "light from", each labelled with a point of the compass: NW, N and NE across the top, W and E at the sides, SW, S and SE across the bottom. Each dome is white on the side of the point it stands at and falls to dark grey on the side away from it](../samples/06-light/light-rose.ans "2x")

The N dome's white is at its top and the S dome's at its bottom, the E dome's at its right end and the W dome's at its left; the four diagonals have theirs at the corner they stand at. The brush and the **Rim Light Brush** share **Light**: set it in either one's options and both take it.

### The rim light brush

The **Rim Light Brush** (**Tools > Rim Light Brush**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>L</kbd>) lights a shape's edge. Under the brush, the cells on the shape's edge that face the light go one rung lighter. The shape is the active layer's cells on the ramp, other than black. One stroke lights only one cell deep, however often it passes over a cell. Either button does the same. Its options add **Light** and **Keep the lint clean**, here set for the hills' rim in step 4 below:

![The Tool Options dock for the Rim Light Brush: a help text, then Size 64 with Tip Square, Pressure None, Ramp grass, Light NE, Keep the lint clean ticked, Alpha lock ticked, and Symmetry Off](../samples/06-light/rim-options.png)

A disc of grey, steel's rung 8, on a layer of its own, before, and after one click from the north-west with **Size** 64 and **Tip** **Square**, big enough to cover it:

![A flat grey disc on black](../samples/06-light/rim-before.ans "2x")

![The same disc with a line of white light shade on grey along its upper left edge](../samples/06-light/rim-after.ans "2x")

Fourteen cells went from grey to white `░` on grey, rung 9: on row 2 the seven from column 8 to 14, on row 3 columns 6 to 8, on row 4 columns 5 and 6, and column 5 on rows 5 and 6. The rest of the disc stays grey, `15, 2` too, just right of the lit cells on the top row.

The same disc eight times, each lit from the point it stands at:

![Eight flat grey discs in a ring on black round the words "light from", each labelled with a point of the compass, each with a line of white light shade on grey along the stretch of its edge that faces its point: the top of the N disc, the right end of the E disc, the lower left of the SW disc, and so on round the ring](../samples/06-light/rim-rose.ans "2x")

The rim light brush doesn't shade the form: the disc is as flat after it as before, with a lit edge. It is for shapes that are flat, a layer of hills or a wall of one tone, and for edges the form brush didn't reach.

### Keep the lint clean

On a form that is already shaded, a rung more on its lit edge can skip the ladder. **Keep the lint clean**, unticked at first, leaves a cell unlit where lighting it would add a lint finding. Two domes laid at **Size** 20 and lit from the north-west, then each rimmed from the north-west, the left with the option unticked and the right with it ticked:

![Two grey domes on black, white at the upper left falling to dark grey shades at the lower right, labelled "lint not kept" and "lint kept clean"](../samples/06-light/rim-lint-before.ans "2x")

![The same domes after the rim light. The left one is a rung lighter along most of its top row and down its left edge; the right one only down its left edge](../samples/06-light/rim-lint.ans "2x")

On the left dome the rim lit 13 cells: seven along row 1 from column 9 to 15, `4, 3`, `3, 4` and `4, 4`, and column 3 on rows 5 to 7. The **Lint** dock lists two rung skips there. `15, 1` went from dark grey `▓` on grey to dark grey `▒` on grey, rung 6, beside the dark grey of `16, 1`, rung 4. `4, 4` went from white `▒` on grey to white `▓` on grey, rung 11, above the white `░` on grey of `4, 5`, rung 9. On the right dome the rim lit only column 33 on rows 4 to 7, each a rung, and the Lint dock lists nothing more. Tick **Keep the lint clean** for shaded shapes.

### Glint

A highlight is the lit side of a form. A **glint** is more: a spot of the brightest colour where the light shines back off a hard or wet surface, small, inside the lit side and off its edge. The **Form Brush** lays one where its **Glint** box is ticked, which is how it starts. Two domes laid at **Size** 28 and lit from the north-east, the left with **Glint** unticked and the right with it ticked:

![Two domes on black, labelled "Glint off" and "Glint on". The left is solid white over its upper right and falls through grey and dark grey to black at its lower left, where its edge is lost in the black round it. The right is solid grey over its upper right with a small white spot near its right side, ringed by white shade on grey, and falls to dark grey shades on black at its lower left](../samples/06-light/glint.ans "2x")

With **Glint** unticked, the lit side is solid white, 31 cells across rows 1 to 5, and the shadow side goes down to black: 84 cells of the disc on its lower left are black, the same as the canvas round them. With it ticked, the lit plane goes down to grey, the highest solid colour below white, and the white is two cells, `58, 5` and `59, 5`. The ladder climbs to them a rung a cell: white `░`, `▒` and `▓` on grey from the left along row 5, and down again on the right, with a ring of white shades on grey round them on rows 2 to 4 and 6 to 8. That doesn't lower the rest of the dome: where the dome without the glint is grey or darker, the glinted one is the same or lighter, by up to five rungs. `8, 1` on the left is dark grey `▒` on black, rung 2, and `42, 1`, the same place on the right, is dark grey `▒` on grey, rung 6. Its shadow side ends in dark grey shades on black, with no black.

The glint needs room: a lit side big enough to hold the spot and its ring. The domes above, laid at **Size** 14 and 20, were all shaded with **Glint** ticked and have none; on those the lit side is white.

### Form rim light

Light bounces back off the ground and anything near, so a form's shadow side can carry a thin rim of reflected light along its edge, just inside the black. **Form rim light**, unticked at first, does that: it lifts the edge facing away from the light a rung. Two domes laid at **Size** 20 and lit from the north-east, the left with **Form rim light** unticked and the right with it ticked:

![Two domes on black, white at the upper right and falling to dark grey at the lower left, labelled "Form rim light off" and "Form rim light on". The right one has a thin line of dark grey light shade on black along its lower left edge, a black cell in from it](../samples/06-light/form-rim.ans "2x")

On the left dome, the cells along the lower left edge are black, the same as the canvas: `3, 5` to `3, 7`, `4, 8`, `5, 8`, `6, 9` and `7, 9`. On the right dome the same seven cells, `29, 5` to `29, 7`, `30, 8`, `31, 8`, `32, 9` and `33, 9`, are dark grey `░` on black, rung 1, and the black stays one cell in from them, as at `30, 6`, `30, 7` and `31, 7`. Along the bottom row the right dome is also a rung lighter, from `35, 10` to `42, 10`, and a few cells near its right edge are too. Neither dome has a glint, with **Glint** ticked on both: they are too small.

### Where the rim light can't help

The rim light reads each cell's edge from the shape round it, and some shapes give it too little to read.

**Thin shapes.** Four grey shapes on one layer: a stem a column wide and one two wide, a bar a row tall and one two tall, each rimmed from the north-west inside a selection of its own:

![Four grey shapes on black: two upright stems on the left, labelled "stems", and two flat bars on the right, labelled "bars"](../samples/06-light/thin-before.ans "2x")

![The same shapes after the rim light: only the top cell of the thin stem lit, most of the left column and the top cell of the wide stem, the first three cells of the thin bar, and most of the top row of the wide bar](../samples/06-light/thin.ans "2x")

A shape a cell thin has no inside for an edge to face out from. On the stem a column wide, only its top cell, `5, 1`, went to white `░` on grey. On the bar a row tall, only `18, 2` to `20, 2`, at its left end. At two cells thick the rim reads: the two-column stem lit its left column from row 1 to row 7, and `12, 1` at its top; the two-row bar lit its top row from column 18 to 29, not `30, 6` and `31, 6` at its right end. Light a one-cell stem or bar by hand, with the **Ramp Shade Brush**.

**Counters.** A counter is the hole in a shape, like the middle of an O. The rim light takes the hole as outside, so the walls round it that face the light through the hole light up. A grey box with a one-cell hole at `9, 4`, before, and after the rim light from the north-west:

![A grey box on black with a black hole of one cell in its middle](../samples/06-light/counter-before.ans "2x")

![The box with most of its top row and left column lit, and four cells lit round the hole: the one to its right and three under it](../samples/06-light/counter.ans "2x")

Along the box's outside edge the rim lit the top row from column 3 to 14 and the left column from row 1 to row 7. Round the hole it lit `10, 4`, right of the hole, and `8, 5`, `9, 5` and `10, 5`, under it. Where the hole is a hole, that is right. Where it is a dark mark on a flat face, a knot or a crack, the lit ring makes it read as a dent: take those cells back down with the **Ramp Shade Brush**'s right button.

**Canvas edges.** Past the canvas is not outside. A shape with cells on the canvas's first or last three columns, or on its first or last row, can light differently from the same shape further in. The same grey box twice, the left one on the canvas's first column, each rimmed from the east:

![Two grey boxes on black, each lit down its right column, the left one also on its top left and bottom left corner cells, which are on the canvas's first column](../samples/06-light/edge.ans "2x")

The box further in lit its right column, rows 2 to 7, and `18, 2` and `18, 7`, the cells next to its top and bottom right corners. The box on the edge lit the same cells, column 5 and `4, 2` and `4, 7`, and also `0, 2` and `0, 7`, at the corners on the canvas's first column, which the other box doesn't light. Keep a shape you rim three columns or more in from the canvas's sides and off its first and last rows, or check its edge cells after.

## Do it

You'll build the piece back to front: the sky, the hills, the boulder and the stone, all lit from the north-east, the upper right. The positions are column then row from `0, 0` at the top left; zoom in (<kbd>Ctrl</kbd>+<kbd>=</kbd>) so you can count cells. Set the options in the **Tool Options** dock; they carry over from tool to tool, so each step gives only the ones it changes. **Selection > Deselect** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>A</kbd>) drops a selection.

1. **A new canvas.** On the start screen, set **Width** to 60 and **Height** to 20, leave **iCE colours** ticked, and press **New**.

2. **The sky.** The light comes from the upper right, so the sky is brightest in the top right corner. **Selection > Select All** (<kbd>Ctrl</kbd>+<kbd>A</kbd>). Take the **Ramp Gradient** (**Tools > Ramp Gradient**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>G</kbd>) and set **Ramp** to **sea**, **Gradient** to **Radial**, **Banding** to **Cell-banded**, **From rung** to 10 and **To rung** to 2. Drag from `59, 0` to `0, 19`. Then **Selection > Deselect**:

    ![The canvas filled with sky: light cyan shade on cyan in the top right corner, cyan over the right part, three shade blocks running from the top edge down to the bottom right, blue over the left, and blue shade on black in the bottom left corner](../samples/06-light/step-01.ans "2x")

    Light cyan `░` and `▒` on cyan, rungs 9 and 10, take the four cells in each of rows 0 and 1 at the right end. Cyan, rung 8, covers the upper right. Cyan `▓`, `▒` and `░` on blue, rungs 7 to 5, run down from columns 22 to 27 on row 0 to the right end of rows 16 to 18. Blue, rung 4, covers the rest, but for the bottom left corner, which goes down to blue `▓` and `▒` on black.

3. **The hills.** **Layer > New Cells Layer**. In the **Layers** dock, double-click the new layer's name and type `hills`. Take the **Ramp Shade Brush** (**Tools > Ramp Shade Brush**, <kbd>Ctrl</kbd>+<kbd>T</kbd>) and set **Ramp** to **grass**, **Strength** to 100%, **Tip** to **Round** and **Size** to 36. Click once at `14, 19`; set **Size** to 44 and click once at `48, 19`. Each click lays a whole colour, green, on the empty cells. Tick **Alpha lock**. Take the **Ramp Gradient**, set **Gradient** to **Linear**, **From rung** to 3 and **To rung** to 6, and drag from `0, 19` to `0, 10`. With nothing selected the gradient fills the whole layer, and alpha lock keeps it to the hills:

    ![Two green hills over the bottom of the sky, the left lower than the right, a notch of sky between them; light green shade on green along their tops, green below, and a row of green dark shade on black along the bottom](../samples/06-light/step-02.ans "2x")

    Rows 8 to 11 are light green `▒` on green, rung 6, row 12 light green `░` on green, rows 13 to 18 green, and row 19 green `▓` on black, rung 3.

4. **The hills' rim.** Take the **Rim Light Brush** (**Tools > Rim Light Brush**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>L</kbd>). **Ramp** is still **grass**. Set **Light** to **NE**, tick **Keep the lint clean**, and set **Size** to 64 and **Tip** to **Square**. Click once at `30, 12`; the brush covers the whole canvas:

    ![The hills a rung lighter along the edges that face the upper right](../samples/06-light/step-03.ans "2x")

    Thirty-nine cells go a rung lighter. Light green `▒` on green goes to light green `▓` on green along the hilltops: row 8 from column 42 to 54 and row 9 from 54 to 58 on the right hill, row 10 from 9 to 19 on the left, and `58, 10` and `59, 10`. Green goes to light green `░` on green down the left hill's right slope, `25, 13` to `27, 13` and `27, 14` to `29, 14`, and at `0, 13` and `1, 13`, on the canvas's first columns. The Lint dock is clean.

5. **The boulder.** **Layer > New Cells Layer**, and name it `boulder`. Take the **Ramp Shade Brush**, set **Ramp** to **steel**, **Strength** to 25%, **Tip** to **Round** and **Size** to 28, and click once at `42, 12`: a disc of dark grey `░` on black, steel's first rung. Tick **Alpha lock**. Take the **Form Brush** (**Tools > Form Brush**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd>) and set **Strength** to 100%, **Form** to **Dome**, **Size** to 38 and **Tip** to **Square**. **Light** is already **NE**: the two brushes share it. Leave **Glint** ticked and **Form rim light** unticked, and click once at `42, 12`:

    ![The boulder shaded on the right hill: grey over its upper right with a small white spot ringed by white shade on grey, falling through dark grey to dark grey shades on black at its lower left](../samples/06-light/step-04.ans "2x")

    The lit side is grey, the glint white at `49, 10` and `50, 10`, with white `▓`, `▒` and `░` on grey each side of it along row 10. The fall runs down to dark grey at the lower left, then to dark grey `▓`, `▒` and `░` on black at the edge.

6. **The stone.** **Layer > New Cells Layer**, and name it `stone`. Take the **Ramp Shade Brush**, set **Strength** to 25%, **Tip** to **Round** and **Size** to 16, and click once at `14, 14`. Tick **Alpha lock**:

    ![The Layers dock: stone, active, above boulder, hills and Background; stone, boulder and hills have Alpha Lock ticked, Background doesn't](../samples/06-light/layers.png)

7. **The stone's form.** Take the **Form Brush**, set **Strength** to 100%, **Tip** to **Square** and **Size** to 26, untick **Glint** and tick **Form rim light**, and click once at `14, 14`. With **Glint** unticked the stone's lit side is white: `15, 10` to `17, 10`, `15, 11` to `19, 11`, `16, 12` to `20, 12`, and `19, 13` and `20, 13`. Its shadow side ends in dark grey shades on black, with no black. **Form rim light** lifts its lower left edge a rung, so `6, 14`, `7, 15`, `8, 16` and `10, 17` are dark grey `▒` on black, not `░`:

    ![The finished piece: the boulder and the stone on the hills under the sky, all lit from the upper right](../samples/06-light/final.bwp "2x")

    The **Lint** dock is clean:

    ![The Lint dock with no findings: clean, noise 0.0000, iCE on](../samples/06-light/lint.png)

8. **Save it.** **File > Save As** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>), with a name ending `.bwp`, so the four layers are kept.

## Check it

**One light for every form.** **Light** is shared, but nothing stops you changing it between forms. The stone shaded from the north-west, in the scene lit from the north-east:

![The scene with the stone white at its upper left and dark grey at its lower right, while the boulder's glint and the hills' lit edges face the upper right](../samples/06-light/two-lights.ans "2x")

The stone's white is now on its upper left, `10, 10` to `12, 10` and `8, 11` to `12, 11`, and its dark grey on its right, while the boulder's glint and the hills' rim face the upper right. Undo (<kbd>Ctrl</kbd>+<kbd>Z</kbd>), set **Light** back to **NE**, and click again.

**Rim flat shapes, not formed ones.** The form brush has already lit a form's side that faces the light. The rim light brush over the boulder and the stone as well, from the north-east, with **Keep the lint clean** unticked:

![The scene with a line of white light shade on grey round the top and right edge of the boulder, and the stone's top and right edge a rung lighter](../samples/06-light/stickers.ans "2x")

The boulder gets a line of white `░` on grey along its top, row 5 from column 38 to 46, and on down its right side to `55, 13`, and the stone's edge goes a rung lighter at `11, 10` to `14, 10`, `21, 13`, `21, 14` and `20, 15`. An outline lighter than the form inside it reads as a cut-out, not a lit edge. The Lint dock lists a speck at `34, 6` and a rung skip at `10, 10`. Undo, and leave the light on a shaded form to the form brush: **Glint** for the lit side, **Form rim light** for the shadow side.

## Try it

Download [try.bwp](../samples/06-light/try.bwp) and open it (**File > Open**, <kbd>Ctrl</kbd>+<kbd>O</kbd>):

![The sky light cyan in the top left corner and blue on the right, the two hills shaded but not rimmed, and the boulder and the stone as flat discs of dark grey light shade on black](../samples/06-light/try.bwp "2x")

It is the scene again under a sky brightest at the top left. The hills are shaded but not rimmed, and the boulder and the stone are laid and locked, each on its own layer, but not shaded.

1. Light the scene from the upper left: the boulder with a glint, the stone with a rim of reflected light, and the hills' lit edges, with the lint kept clean.
2. Which is the light's side on this sky, and why?

<details markdown="1">
<summary>Answers</summary>

1. Click **boulder** in the **Layers** dock. Take the **Form Brush**, **Ramp** **steel**, **Strength** 100%, **Form** **Dome**, **Light** **NW**, **Glint** ticked, **Form rim light** unticked, **Size** 38, **Tip** **Square**, and click once at `42, 12`. Click **stone**, untick **Glint**, tick **Form rim light**, set **Size** to 26 and click once at `14, 14`. Click **hills**, take the **Rim Light Brush**, set **Ramp** to **grass**, tick **Keep the lint clean**, set **Size** to 64, and click once at `30, 12`. Set the ramp first: the brush lights only cells on its ramp, so with **steel** still set from the stones, the click leaves the hills as they are. The Lint dock is clean:

    ![The scene lit from the upper left: the boulder grey at its upper left with a white glint, falling to dark grey shades at its lower right; the stone white at its upper left, falling to dark grey at its lower right; the hills a few cells lighter on their edges](../samples/06-light/try-answer.ans "2x")

    The boulder's glint is at `33, 10` and `34, 10`, with white `▓`, `▒` and `░` on grey each side of it along row 10. The stone's white is at its upper left. The rim lifts 13 cells of the hills a rung: `8, 10`, `9, 10` and `18, 10` on the left hill's top; `0, 13` to `2, 13`, on the canvas's first columns; `27, 13`, `27, 14` and `28, 14`, at the bottom of the notch between the hills; and `57, 9`, `58, 9`, `58, 10` and `59, 10`, where the right hill runs off the canvas.

2. The upper left. The sky is brightest there, light cyan in the top left corner, and the light has to come from where the sky is brightest, or the forms look lit by a second sun.

</details>

Tutorial 07, *Detail*, goes on from here: the outline brush, texture stamps, glyph spray, the clone stamp and symmetry.
