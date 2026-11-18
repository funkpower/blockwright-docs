Title: Frames and canvas size
Checked: Blockwright 0.1.1 (9b263b8)

# Frames and canvas size

## Goal

Give a hi-score board room to breathe with **Format > Canvas Size...**, box its scores with the **Frame** tool, and frame the whole board in a style you make yourself. The board ends 38 columns by 14 rows. Shown at 2×:

![A hi-score board on black. A border of light magenta dots runs round the edge, with a light magenta diamond in each corner. Near the top, MOONLIGHT ARCADE in yellow. Below it a yellow double-line box holds four score lines: a white rank, three light cyan initials, a row of dark grey dots and a light green score, from 1 FNK 98,400 down to 4 ZAP 30,050. Under the box, INSERT COINS in light red](../samples/13-frames-and-canvas-size/final.ans "2x")

## The idea

A frame is drawn, not typed. Pick a style, drag a rectangle, and the **Frame** tool draws the border to fit it.

### How a frame fits any size

Each style is a small box cut nine ways. The four corners are drawn once, as they are. The edges repeat along the sides as far as the drag reaches. The middle of most styles is open: whatever is under it stays.

The Frame tool (**Tools > Frame**, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd>) has eleven styles built in. Here each is drawn 12 columns by 6 rows, in the order of the **Frame** list in **Tool Options**:

![Eleven frames on black in three rows. Top row, all grey lines: single, double, double across with single sides, and single across with double sides. Middle row: a heavy white block frame, a thin light cyan half-block frame, a light cyan frame shaded from dark at the edge to light inside, and a bevel lit white at the top left and dark grey at the bottom right. Bottom row: yellow and black hazard stripes, a grey dashed line, and a grey button with a white raised edge round a grey face](../samples/13-frames-and-canvas-size/styles.ans "2x")

They are **Single line**, **Double line**, **Double across, single down**, **Single across, double down**, **Heavy block**, **Thin half-block**, **Shaded**, **Bevel**, **Hazard stripes**, **Dashed line** and **Double-bevel button**.

### Dragging

Press where one corner goes and let go where the opposite corner goes. Each style has a smallest size, its corners: 2 × 2 for the lines, 4 × 4 for the hazard stripes, 6 × 4 for **Shaded**. A click, or a drag smaller than that, grows to it, toward where you dragged.

The right button erases each cell the frame would draw and leaves the open middle alone. On the bottom layer, as here, an erased cell is a space in grey on black; on a layer above, it is transparent. Right-drag over a frame with the same style and rectangle and the frame is gone, with nothing inside it touched.

### Colours

**Colours** in **Tool Options** is **Style colours** or **Pen colours**. **Style colours** draws the frame in its own colours: grey for the lines, white and dark grey for the bevel. **Pen colours** draws it in the pen's foreground and background. The line, half-block and shaded styles keep the background already under each cell and take only the foreground.

The Frame tool keeps its style and **Colours** between sessions. Check both before you drag.

### Room round the art

A frame drawn on the art itself writes over its edge. Add the room first with **Format > Canvas Size...**. **Width** and **Height** are the new size; the **Anchor** grid says where the old canvas sits in the new one. The summary under it says what each side gains. The anchor starts at top left every time the dialog opens.

### A style of your own

Draw a small box on the canvas: corners, one cell of each edge, a middle. Select it and choose **Selection > Save as Frame Style...**. It joins the end of the **Frame** list and is kept in your library, so the next session has it too.

## Do it

Positions are column then row from `0, 0` at the top left; zoom in (<kbd>Ctrl</kbd>+<kbd>=</kbd>) to count cells.

1. **Open the board.** Download [start.ans](../samples/13-frames-and-canvas-size/start.ans) and **File > Open** (<kbd>Ctrl</kbd>+<kbd>O</kbd>) it:

    ![The board on a black canvas 30 columns by 10 rows: MOONLIGHT ARCADE in yellow on the top row, the four score lines in the middle with a blank row above and below them, and INSERT COINS in light red on the bottom row](../samples/13-frames-and-canvas-size/start.ans "2x")

    The title is on the top row and **INSERT COINS** on the bottom row. A frame round the edge would cover both.

2. **Add room.** **Format > Canvas Size...**. Set **Width** to `38` and **Height** to `14`, and click the centre button of the **Anchor** grid, the dot. The summary reads `4 columns added on the left; 4 columns added on the right; 2 rows added at the top; 2 rows added at the bottom`. Click **OK**:

    ![The same board in the middle of a larger black canvas, with four empty columns on each side and two empty rows above and below](../samples/13-frames-and-canvas-size/grown.ans "2x")

    Everything moved 4 right and 2 down. The title is on row 2, the scores on rows 5 to 8, **INSERT COINS** on row 11.

3. **Box the scores.** Take the **Frame** tool (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd>). In **Tool Options**, set **Frame** to **Double line** and **Colours** to **Style colours**. Drag from `5, 4` to `32, 9`:

    ![The board with a grey double-line box round the four score lines, one empty column between the box and the text on each side](../samples/13-frames-and-canvas-size/box-grey.ans "2x")

    Rows 4 and 9 were the empty rows above and below the scores. Columns 6 and 31 stay empty, a one-column margin each side.

4. **Recolour it.** Left-click yellow in the **Palette** dock for the foreground; leave the background black. Set **Colours** to **Pen colours** and drag from `5, 4` to `32, 9` again:

    ![The board with the double-line box now yellow](../samples/13-frames-and-canvas-size/box-yellow.ans "2x")

    The new frame is drawn over the old one, cell for cell.

5. **Draw a style's source.** In the free corner at the bottom left, draw a three by three box in light magenta: a diamond at each corner, a dot on each side, the middle empty. Take keyboard mode (<kbd>Ctrl</kbd>+<kbd>K</kbd>) and left-click light magenta for the foreground. Press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F7</kbd> for set 7 and type `♦` (<kbd>F4</kbd>) at `1, 10`, `3, 10`, `1, 12` and `3, 12`: click each cell, then press the key. Press <kbd>Ctrl</kbd>+<kbd>/</kbd> for set 6 and type `·` (<kbd>F10</kbd>) at `2, 10`, `1, 11`, `3, 11` and `2, 12`:

    ![The board with a small light magenta box at the bottom left: diamonds at its four corners and a dot in the middle of each side](../samples/13-frames-and-canvas-size/source.ans "2x")

6. **Save it as a style.** Take the **Select** tool (<kbd>Ctrl</kbd>+<kbd>E</kbd>) and drag from `1, 10` to `3, 12`. Choose **Selection > Save as Frame Style...**. In the dialog:

    - **Name:** `Dotted diamond`. **OK** stays greyed out until the style has a name.
    - **Corner columns:** **left** `1`, **right** `1`; **Corner rows:** **top** `1`, **bottom** `1`, as the dialog starts. The corners are one cell, so the edges are the dots between them.
    - **Draw the middle** off, as it starts: the frame leaves the board inside it alone.
    - Tick **Keep the background under it**, so the dots and diamonds take the colour of whatever they are drawn on. On this black board it makes no difference.

    The preview shows the style stretched. Click **OK**. The status bar says the style was saved to the library and that the Frame tool lists it.

7. **Clear the source.** With the box still selected, press <kbd>Delete</kbd>, then **Selection > Deselect** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>A</kbd>). The corner is empty again.

8. **Frame the board.** Take the **Frame** tool. Set **Frame** to **Dotted diamond**, at the end of the list, and **Colours** back to **Style colours**. Drag from `0, 0` to `37, 13`:

    ![The finished board: the light magenta dotted border with diamond corners round the whole canvas](../samples/13-frames-and-canvas-size/final.ans "2x")

    Between the border and the yellow box there are four empty columns each side and one empty row above the title and below **INSERT COINS**. Save it with **File > Save As...** (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>S</kbd>) under a new name.

## Check it

**Make room first.** The double line dragged round the board as it came, from `0, 0` to `29, 9`:

![The board on its original 30 by 10 canvas with a grey double-line frame round its edge. The top rule has replaced the title and the bottom rule has replaced INSERT COINS; only the score lines are left inside](../samples/13-frames-and-canvas-size/too-tight.ans "2x")

The frame's rules took the title's row and the last line's. Undo (<kbd>Ctrl</kbd>+<kbd>Z</kbd>), make the canvas bigger, then draw.

**Pick the anchor.** **Canvas Size** with the anchor left at top left:

![The board in the top left corner of the larger canvas, its title touching the top edge, with eight empty columns on the right and four empty rows at the bottom](../samples/13-frames-and-canvas-size/top-left.ans "2x")

All the new room went to the right and the bottom. The board is still against the top and left edges, and the margins round it won't match. Undo and click the centre of the **Anchor** grid. If the room to add is odd, the centre puts the extra column on the right and the extra row at the bottom.

**Delete the source.** The border drawn with the source still in its corner:

![The finished board, but the small light magenta box of diamonds and dots is still in the bottom left corner, just inside the border](../samples/13-frames-and-canvas-size/left-over.ans "2x")

Saving a frame style leaves its source on the canvas. Next to the border it reads as a stray piece of it. Select it and press <kbd>Delete</kbd>.

**Set the colours back.** The border drawn with **Colours** still on **Pen colours** and the pen still yellow:

![The finished board with the dotted border and its diamonds in yellow, the same colour as the box and the title](../samples/13-frames-and-canvas-size/pen-left-on.ans "2x")

**Pen colours** recolours every style, your own too. The Frame tool also remembers it for the next session. Undo, set **Colours** to **Style colours**, and drag again.

## Try it

![The finished board](../samples/13-frames-and-canvas-size/final.ans "2x")

[final.ans](../samples/13-frames-and-canvas-size/final.ans) is the board after step 8.

1. Give the box a heading, `TOP SCORES`, without adding a row. Where does it go?
2. Swap the yellow double-line box for a light cyan single-line one. How do you get rid of the old box without touching the scores?

<details markdown="1">
<summary>Answers</summary>

1. Set it as a tab in the box's top rule: a space each side, so the rule stops short of the words. Take keyboard mode, left-click white for the foreground, click `13, 4` and type <code> TOP SCORES </code>, a space first and last:

    ![The finished board with TOP SCORES in white set into the middle of the yellow box's top rule, a gap each side of it](../samples/13-frames-and-canvas-size/try-tab.ans "2x")

    It is columns 13 to 24, twelve cells, with the corner and seven cells of rule each side. A heading under the rule would need another row in the box.

2. Erase it with the right button. Take the **Frame** tool, set **Frame** to **Double line**, and right-drag from `5, 4` to `32, 9`, the rectangle you drew it with:

    ![The finished board with the yellow box gone; the score lines are untouched](../samples/13-frames-and-canvas-size/try-erased.ans "2x")

    Only the frame's own cells are blanked; the open middle, with the scores, is left alone. Then set **Frame** to **Single line** and **Colours** to **Pen colours**, left-click light cyan, and drag the same rectangle with the left button:

    ![The finished board with a light cyan single-line box round the scores](../samples/13-frames-and-canvas-size/try-single.ans "2x")

</details>

The manual has the rest: [Frame](../manual/04-tools.md#frame), [Canvas Size](../manual/02-the-window.md#canvas-size) and [Save as Frame Style](../manual/08-library.md#save-as-frame-style-and-save-as-preset).
