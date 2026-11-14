Title: Samples
Checked: Blockwright 0.1.1 (bd67fae)

# Samples

The sample projects that come with Blockwright, taken apart. Each one is built from layers, and each is shown here a layer at a time from the bottom up, with what every layer does, the variants it keeps, the finished piece and what it costs on IRC. Download a project and open it to turn its layers on and off yourself; the start screen and **Help > Samples** open the ones your Blockwright installed.

Blockwright 0.1.0 installs five of them, Harbour at night, Still life, Ridges at dusk, Traveller and Blockwright logo, and Ember Kiln, a text-style logo DDOS KING has since replaced. DDOS KING, Battlestation, This Is Your Brain on IRC and wtc-0903 come with 0.1.1; 0.1.0 opens their projects too.

- [Harbour at night](#harbour-at-night)
- [DDOS KING](#ddos-king)
- [Still life](#still-life)
- [Ridges at dusk](#ridges-at-dusk)
- [Traveller](#traveller)
- [Blockwright logo](#blockwright-logo)
- [Battlestation](#battlestation)
- [This Is Your Brain on IRC](#this-is-your-brain-on-irc)
- [wtc-0903](#wtc-0903)

## Harbour at night {#harbour-at-night}

A city on the water under a full moon, built from thirteen layers: every layer kind, both blend modes, the locks, a generator, a text layer and its baked copy, and a reference sketch.

80 × 40 cells, 13 layers.

### Layer by layer

The visible layers from the bottom up, each picture adding one to the ones before it: sky, stars, moon, cloud, skyline, quay, water, reflection, fog and title. The hidden layers, day sky, title (baked) and reference sketch, stay hidden, as they are when the project opens.

<div class="strip">
<figure><img src="gallery/01-layers-showcase/layer-01.ans" alt="Harbour at night, its bottom layer, sky, alone"><figcaption>sky</figcaption></figure>
<figure><img src="gallery/01-layers-showcase/layer-02.ans" alt="Harbour at night with its bottom 2 visible layers: sky and stars"><figcaption>+ stars</figcaption></figure>
<figure><img src="gallery/01-layers-showcase/layer-03.ans" alt="Harbour at night with its bottom 3 visible layers: sky, stars and moon"><figcaption>+ moon</figcaption></figure>
<figure><img src="gallery/01-layers-showcase/layer-04.ans" alt="Harbour at night with its bottom 4 visible layers: sky, stars, moon and cloud"><figcaption>+ cloud</figcaption></figure>
<figure><img src="gallery/01-layers-showcase/layer-05.ans" alt="Harbour at night with its bottom 5 visible layers: sky, stars, moon, cloud and skyline"><figcaption>+ skyline</figcaption></figure>
<figure><img src="gallery/01-layers-showcase/layer-06.ans" alt="Harbour at night with its bottom 6 visible layers: sky, stars, moon, cloud, skyline and quay"><figcaption>+ quay</figcaption></figure>
<figure><img src="gallery/01-layers-showcase/layer-07.ans" alt="Harbour at night with its bottom 7 visible layers: sky, stars, moon, cloud, skyline, quay and water"><figcaption>+ water</figcaption></figure>
<figure><img src="gallery/01-layers-showcase/layer-08.ans" alt="Harbour at night with its bottom 8 visible layers: sky, stars, moon, cloud, skyline, quay, water and reflection"><figcaption>+ reflection</figcaption></figure>
<figure><img src="gallery/01-layers-showcase/layer-09.ans" alt="Harbour at night with its bottom 9 visible layers: sky, stars, moon, cloud, skyline, quay, water, reflection and fog"><figcaption>+ fog</figcaption></figure>
<figure><img src="gallery/01-layers-showcase/layer-10.ans" alt="Harbour at night with its bottom 10 visible layers: sky, stars, moon, cloud, skyline, quay, water, reflection, fog and title"><figcaption>+ title</figcaption></figure>
</div>

Each layer, as its notes describe it, from the top down:

| Layer | Kind | Mode | Locks | What it does |
|---|---|---|---|---|
| reference sketch | reference | normal | - | The rough the piece was drawn over, hidden; show it and set Layer > Reference Opacity to trace it. |
| title | text | normal | - | HARBOUR in the block face, a flat yellow fill with a brown drop shadow to the south-west. Click it with the Text tool to change the words; the style follows. |
| title (baked) | cells | normal | - | The same title baked to cells (Layer > Bake Layer), hidden: what the text layer becomes when it has to be edited cell by cell. |
| fog | generator | normal | - | Wisps of mist over the near water, made by fog.py. Its parameters are in the Layers dock: change the seed or the rows and press Run. Black is its key colour, so the cells off a wisp are clear. |
| reflection | cells | colours-only | - | The moon's path on the water. Colours only: it paints yellow onto the water's own ripple glyphs and keeps them. |
| water | cells | normal | - | The harbour, a band a rung down the sea ramp, with ripple dashes a rung lighter. |
| quay | cells | normal | - | The stone edge of the shore. Wider than the canvas at both ends, so move it and nothing runs out. |
| skyline | cells | normal | alpha | The towers, on a strip smaller than the canvas. Alpha-locked: shade over it and only the towers take the paint, which is how their roofs caught the glow. |
| cloud | pixels | normal | - | A thin grey cloud across the moon, half a cell high. iCE is off, so a cell shows only one bright colour, and the upper layer keeps its own: the grey stays and the moon's yellow under it shows as brown. The Moon in front variant turns that round. |
| moon | pixels | normal | - | A pixel layer, two pixels to a cell, drawn with the Half-Block Brush. Smaller than the canvas and placed by its offset: Alt+drag it along the sky. |
| stars | cells | chars-only | - | Star glyphs only. Each one takes its colour from the sky cell under it. |
| day sky | cells | normal | - | A daylight sky down the sea ramp, hidden; the Day variant shows it. |
| sky | cells | normal | locked | The night sky, a band a rung up the sunset ramp to the city's glow. Locked so a stray stroke can't touch it. |

### Variants

The variants the project offers in the Layers dock, each a few layers shown, hidden or moved:

<div class="strip">
<figure><img src="gallery/01-layers-showcase/variant-01.ans" alt="Harbour at night, the Day variant: show day sky; hide stars; hide moon; hide reflection"><figcaption>Day<br><small>show day sky; hide stars; hide moon; hide reflection</small></figcaption></figure>
<figure><img src="gallery/01-layers-showcase/variant-02.ans" alt="Harbour at night, the Moon set variant: lower moon below sky"><figcaption>Moon set<br><small>lower moon below sky</small></figcaption></figure>
<figure><img src="gallery/01-layers-showcase/variant-03.ans" alt="Harbour at night, the Moon in front variant: raise moon above cloud"><figcaption>Moon in front<br><small>raise moon above cloud</small></figcaption></figure>
<figure><img src="gallery/01-layers-showcase/variant-04.ans" alt="Harbour at night, the No fog variant: hide fog"><figcaption>No fog<br><small>hide fog</small></figcaption></figure>
<figure><img src="gallery/01-layers-showcase/variant-05.ans" alt="Harbour at night, the Baked title variant: hide title; show title (baked)"><figcaption>Baked title<br><small>hide title; show title (baked)</small></figcaption></figure>
</div>

### The finished piece

![Harbour at night, the finished piece at 1×](gallery/01-layers-showcase/harbour-at-night.ans)

<details><summary>At 2×</summary>
<img src="gallery/01-layers-showcase/harbour-at-night.ans" alt="Harbour at night, the finished piece at 2×" title="2x">
</details>

Its widest IRC row is 271 bytes as `blockwright-cli export --irc` writes it; as WeeChat's ascii script sends it, the widest is 294. The project's budget is 407 bytes, and no row is over it.

Download: [harbour-at-night.bwp](gallery/01-layers-showcase/harbour-at-night.bwp), the project, layers, notes and all; [harbour-at-night.ans](gallery/01-layers-showcase/harbour-at-night.ans), the piece flattened.

The generators packed in harbour-at-night.bwp, `scripts/10/` (the fog, `fog.py`), are Blockwright's own and stay under its licence, the GPL version 3 or later ([Blockwright's `LICENSE`](https://git.pumpin.online/funkpower/blockwright/src/branch/main/LICENSE)); the rest is under this site's licence.

## DDOS KING {#ddos-king}

A king on a throne of server racks, crowned and in shades, holding up an ethernet cable for a sceptre while packet lightning arcs over him, with his name in gold across the top in case the lightning left any doubt. Fourteen layers: a locked backdrop, eleven layers of throne, figure, lightning and lettering on it, and two hidden layers the variants use.

80 × 64 cells, 14 layers.

### Layer by layer

The visible layers from the bottom up, each picture adding one to the ones before it: backdrop, throne, cables, king, sceptre, head, lightning, finials, packets, title, border and signature. The hidden layers, margins and cable tips, stay hidden, as they are when the project opens.

<div class="strip">
<figure><img src="gallery/02-ddos-king/layer-01.ans" alt="DDOS KING, its bottom layer, backdrop, alone"><figcaption>backdrop</figcaption></figure>
<figure><img src="gallery/02-ddos-king/layer-02.ans" alt="DDOS KING with its bottom 2 visible layers: backdrop and throne"><figcaption>+ throne</figcaption></figure>
<figure><img src="gallery/02-ddos-king/layer-03.ans" alt="DDOS KING with its bottom 3 visible layers: backdrop, throne and cables"><figcaption>+ cables</figcaption></figure>
<figure><img src="gallery/02-ddos-king/layer-04.ans" alt="DDOS KING with its bottom 4 visible layers: backdrop, throne, cables and king"><figcaption>+ king</figcaption></figure>
<figure><img src="gallery/02-ddos-king/layer-05.ans" alt="DDOS KING with its bottom 5 visible layers: backdrop, throne, cables, king and sceptre"><figcaption>+ sceptre</figcaption></figure>
<figure><img src="gallery/02-ddos-king/layer-06.ans" alt="DDOS KING with its bottom 6 visible layers: backdrop, throne, cables, king, sceptre and head"><figcaption>+ head</figcaption></figure>
<figure><img src="gallery/02-ddos-king/layer-07.ans" alt="DDOS KING with its bottom 7 visible layers: backdrop, throne, cables, king, sceptre, head and lightning"><figcaption>+ lightning</figcaption></figure>
<figure><img src="gallery/02-ddos-king/layer-08.ans" alt="DDOS KING with its bottom 8 visible layers: backdrop, throne, cables, king, sceptre, head, lightning and finials"><figcaption>+ finials</figcaption></figure>
<figure><img src="gallery/02-ddos-king/layer-09.ans" alt="DDOS KING with its bottom 9 visible layers: backdrop, throne, cables, king, sceptre, head, lightning, finials and packets"><figcaption>+ packets</figcaption></figure>
<figure><img src="gallery/02-ddos-king/layer-10.ans" alt="DDOS KING with its bottom 10 visible layers: backdrop, throne, cables, king, sceptre, head, lightning, finials, packets and title"><figcaption>+ title</figcaption></figure>
<figure><img src="gallery/02-ddos-king/layer-11.ans" alt="DDOS KING with its bottom 11 visible layers: backdrop, throne, cables, king, sceptre, head, lightning, finials, packets, title and border"><figcaption>+ border</figcaption></figure>
<figure><img src="gallery/02-ddos-king/layer-12.ans" alt="DDOS KING with its bottom 12 visible layers: backdrop, throne, cables, king, sceptre, head, lightning, finials, packets, title, border and signature"><figcaption>+ signature</figcaption></figure>
</div>

Each layer, as its notes describe it, from the top down:

| Layer | Kind | Mode | Locks | What it does |
|---|---|---|---|---|
| signature | cells | normal | - | The tag in grey in the lower right corner, inside the frame. |
| border | cells | normal | - | The frame: DDOS KING repeated between rising and falling block waves along the top and bottom, the chant stacked a letter a row down the sides, in the lightning's colours. |
| title | cells | normal | - | DDOS KING in square capitals 12 pixels high, strokes two pixels thick, gold by pixel row: a white top edge, yellow to the middle, brown below. The round corners of D and O are cut by a two-pixel stair, those of S and G by a single pixel; K, I and N are square. |
| packets | cells | normal | - | Green packet blocks riding the bolts. |
| finials | cells | normal | - | Gold balls on the rack corners. They sit above the lightning, so no bolt crosses them. |
| lightning | cells | normal | - | White bolt cores a pixel wide in a light cyan glow, from the sceptre's plug out over the throne. |
| head | cells | normal | - | The face, the black shades, the grin and the gold crown with its jewels. |
| sceptre | cells | normal | - | A yellow ethernet cable topped by an RJ45 plug, held up in the king's right hand. |
| king | cells | normal | - | The body: a purple robe lit from the left, the ermine collar and hem, the gold belt, the sleeves, the hand on the armrest and red boots. |
| cable tips | cells | normal | - | Hidden: half a cell more yellow on top of four cable runs, where they stop against the blue. The No lightning variant shows it. |
| cables | cells | normal | - | Bundles of yellow cables curving out of each armrest into the raised floor, with black ties. |
| throne | cells | normal | - | The tall back rack, the flanking and armrest racks with their LEDs, the dais, the panel behind the head and the raised floor. |
| margins | cells | normal | - | Hidden: black blocks over the frame's rows and its last column. The variants without the border show it. |
| backdrop | cells | normal | locked | The black and the blue the piece stands on, with the shaded fade at the top of the blue. Locked, so painting the throne or the lightning never touches it. |

### Variants

The variants the project offers in the Layers dock, each a few layers shown, hidden or moved:

<div class="strip">
<figure><img src="gallery/02-ddos-king/variant-01.ans" alt="DDOS KING, the No lightning variant: hide lightning; hide packets; show cable tips"><figcaption>No lightning<br><small>hide lightning; hide packets; show cable tips</small></figcaption></figure>
<figure><img src="gallery/02-ddos-king/variant-02.ans" alt="DDOS KING, the No border variant: hide border; show margins"><figcaption>No border<br><small>hide border; show margins</small></figcaption></figure>
<figure><img src="gallery/02-ddos-king/variant-03.ans" alt="DDOS KING, the Title only variant: hide backdrop; hide throne; hide cables; hide king; hide sceptre; hide head; hide lightning; hide finials; hide packets; hide border; hide signature; show margins"><figcaption>Title only<br><small>hide backdrop; hide throne; hide cables; hide king; hide sceptre; hide head; hide lightning; hide finials; hide packets; hide border; hide signature; show margins</small></figcaption></figure>
</div>

### The finished piece

![DDOS KING, the finished piece at 1×](gallery/02-ddos-king/ddos-king.ans)

<details><summary>At 2×</summary>
<img src="gallery/02-ddos-king/ddos-king.ans" alt="DDOS KING, the finished piece at 2×" title="2x">
</details>

Its widest IRC row is 308 bytes as `blockwright-cli export --irc` writes it; as WeeChat's ascii script sends it, the widest is 342. The project's budget is 407 bytes, and no row is over it.

Download: [ddos-king.bwp](gallery/02-ddos-king/ddos-king.bwp), the project, layers, notes and all; [ddos-king.ans](gallery/02-ddos-king/ddos-king.ans), the piece flattened.

## Still life {#still-life}

A cylinder, a box and a ball on a table, each object on its own layer, shaded inside its own shape under an alpha lock with the light from the upper left. The shadows they cast and a rim light from the right sit on two layers of their own, so turning layers off shows how the light was built. The brushes tutorials' showcase.

80 × 30 cells, 7 layers.

### Layer by layer

The visible layers from the bottom up, each picture adding one to the ones before it: wall, table, shadows, cylinder, box, sphere and rim light.

<div class="strip">
<figure><img src="gallery/03-still-life/layer-01.ans" alt="Still life, its bottom layer, wall, alone"><figcaption>wall</figcaption></figure>
<figure><img src="gallery/03-still-life/layer-02.ans" alt="Still life with its bottom 2 visible layers: wall and table"><figcaption>+ table</figcaption></figure>
<figure><img src="gallery/03-still-life/layer-03.ans" alt="Still life with its bottom 3 visible layers: wall, table and shadows"><figcaption>+ shadows</figcaption></figure>
<figure><img src="gallery/03-still-life/layer-04.ans" alt="Still life with its bottom 4 visible layers: wall, table, shadows and cylinder"><figcaption>+ cylinder</figcaption></figure>
<figure><img src="gallery/03-still-life/layer-05.ans" alt="Still life with its bottom 5 visible layers: wall, table, shadows, cylinder and box"><figcaption>+ box</figcaption></figure>
<figure><img src="gallery/03-still-life/layer-06.ans" alt="Still life with its bottom 6 visible layers: wall, table, shadows, cylinder, box and sphere"><figcaption>+ sphere</figcaption></figure>
<figure><img src="gallery/03-still-life/layer-07.ans" alt="Still life with its bottom 7 visible layers: wall, table, shadows, cylinder, box, sphere and rim light"><figcaption>+ rim light</figcaption></figure>
</div>

Each layer, as its notes describe it, from the top down:

| Layer | Kind | Mode | Locks | What it does |
|---|---|---|---|---|
| rim light | cells | normal | - | A back light from the east: a band along each object's right edge, brightest at the edge and a rung dimmer each cell in, on each object's own ramp. It only holds the cells it lights, so hiding it puts the dark sides back. |
| sphere | cells | normal | alpha | The ball, shaded as a dome on the sea ramp, lit from the north-west with a specular highlight. Smaller than the canvas, placed by its offset. |
| box | cells | normal | alpha | The box in three faces on the wood ramp without its black: a yellow top where the light falls, a brown front and a red side turned away, each edge stepping a rung at a time. |
| cylinder | cells | normal | alpha | The pillar on its round foot, shaded as a cylinder on the violet ramp, white down the lit side and dark down the far one. |
| shadows | cells | normal | - | The shadows the objects cast to the right on the table: the table's own grey rungs taken down, deepest at each foot and lifting back to the table a rung at a time. |
| table | cells | normal | locked | The table top, grey shading lighter toward the front, locked. |
| wall | cells | normal | locked | A flat dark grey wall, locked: dark enough to set the lit sides off, light enough that the black on the ball's far side still reads with the rim light off. |

### Variants

The variants the project offers in the Layers dock, each a few layers shown, hidden or moved:

<div class="strip">
<figure><img src="gallery/03-still-life/variant-01.ans" alt="Still life, the No rim light variant: hide rim light"><figcaption>No rim light<br><small>hide rim light</small></figcaption></figure>
<figure><img src="gallery/03-still-life/variant-02.ans" alt="Still life, the No shadows variant: hide shadows"><figcaption>No shadows<br><small>hide shadows</small></figcaption></figure>
<figure><img src="gallery/03-still-life/variant-03.ans" alt="Still life, the Form only variant: hide rim light; hide shadows"><figcaption>Form only<br><small>hide rim light; hide shadows</small></figcaption></figure>
</div>

### The finished piece

![Still life, the finished piece at 1×](gallery/03-still-life/still-life.ans)

<details><summary>At 2×</summary>
<img src="gallery/03-still-life/still-life.ans" alt="Still life, the finished piece at 2×" title="2x">
</details>

Its widest IRC row is 262 bytes as `blockwright-cli export --irc` writes it; as WeeChat's ascii script sends it, the widest is 268. The project's budget is 407 bytes, and no row is over it.

Download: [still-life.bwp](gallery/03-still-life/still-life.bwp), the project, layers, notes and all; [still-life.ans](gallery/03-still-life/still-life.ans), the piece flattened.

## Ridges at dusk {#ridges-at-dusk}

Mountain ridges and stars made by two generator layers, programs that ship inside the project with their parameters, under a lake, a shore, pines and a cabin on layers of their own.

80 × 34 cells, 9 layers.

### Layer by layer

The visible layers from the bottom up, each picture adding one to the ones before it: sky, stars, ridges, lake, shore, pines and cabin. The hidden layers, ridges (seed 12) and ridges (baked), stay hidden, as they are when the project opens.

<div class="strip">
<figure><img src="gallery/04-generator-ridges/layer-01.ans" alt="Ridges at dusk, its bottom layer, sky, alone"><figcaption>sky</figcaption></figure>
<figure><img src="gallery/04-generator-ridges/layer-02.ans" alt="Ridges at dusk with its bottom 2 visible layers: sky and stars"><figcaption>+ stars</figcaption></figure>
<figure><img src="gallery/04-generator-ridges/layer-03.ans" alt="Ridges at dusk with its bottom 3 visible layers: sky, stars and ridges"><figcaption>+ ridges</figcaption></figure>
<figure><img src="gallery/04-generator-ridges/layer-04.ans" alt="Ridges at dusk with its bottom 4 visible layers: sky, stars, ridges and lake"><figcaption>+ lake</figcaption></figure>
<figure><img src="gallery/04-generator-ridges/layer-05.ans" alt="Ridges at dusk with its bottom 5 visible layers: sky, stars, ridges, lake and shore"><figcaption>+ shore</figcaption></figure>
<figure><img src="gallery/04-generator-ridges/layer-06.ans" alt="Ridges at dusk with its bottom 6 visible layers: sky, stars, ridges, lake, shore and pines"><figcaption>+ pines</figcaption></figure>
<figure><img src="gallery/04-generator-ridges/layer-07.ans" alt="Ridges at dusk with its bottom 7 visible layers: sky, stars, ridges, lake, shore, pines and cabin"><figcaption>+ cabin</figcaption></figure>
</div>

Each layer, as its notes describe it, from the top down:

| Layer | Kind | Mode | Locks | What it does |
|---|---|---|---|---|
| cabin | pixels | normal | - | A cabin on the shore in half-block pixels, its window lit |
| pines | pixels | normal | - | Six pines in half-block pixels, standing over the lake and the ridges, green where the light from the right falls and dark in the shade of each bough |
| shore | cells | normal | locked | A strip of grass along the bottom |
| lake | cells | normal | locked | The water under the ridges, on the sea ramp, with ripples a rung up on every other row |
| ridges (baked) | cells | normal | - | Hidden: the ridges layer baked, its cells as they are, with no generator behind them |
| ridges (seed 12) | generator | normal | - | Hidden: the same ridges generator with other parameters (seed 12, four ridges, sharp peaks) |
| ridges | generator | normal | - | `ridges.sh`: three ridges from value noise, far to near, each darker than the one behind it as haze makes them (light blue, then dark grey, then slate) and all darker than the glow; its form has Seed, Ridges, Roughness, Sharp peaks and Highest row |
| stars | generator | chars-only | - | `stars.sh`: stars in the black rows from a seed; chars only, so each takes the sky's colours under it |
| sky | cells | normal | locked | Black at the top, then a rung a row up the sunset ramp to a light red glow behind the ridges |

### Variants

The variants the project offers in the Layers dock, each a few layers shown, hidden or moved:

<div class="strip">
<figure><img src="gallery/04-generator-ridges/variant-01.ans" alt="Ridges at dusk, the Another seed variant: show ridges (seed 12); hide ridges"><figcaption>Another seed<br><small>show ridges (seed 12); hide ridges</small></figcaption></figure>
<figure><img src="gallery/04-generator-ridges/variant-02.ans" alt="Ridges at dusk, the Baked variant: show ridges (baked); hide ridges"><figcaption>Baked<br><small>show ridges (baked); hide ridges</small></figcaption></figure>
<figure><img src="gallery/04-generator-ridges/variant-03.ans" alt="Ridges at dusk, the No stars variant: hide stars"><figcaption>No stars<br><small>hide stars</small></figcaption></figure>
<figure><img src="gallery/04-generator-ridges/variant-04.ans" alt="Ridges at dusk, the Generated only variant: hide lake; hide shore; hide pines; hide cabin"><figcaption>Generated only<br><small>hide lake; hide shore; hide pines; hide cabin</small></figcaption></figure>
</div>

### The finished piece

![Ridges at dusk, the finished piece at 1×](gallery/04-generator-ridges/ridges-at-dusk.ans)

<details><summary>At 2×</summary>
<img src="gallery/04-generator-ridges/ridges-at-dusk.ans" alt="Ridges at dusk, the finished piece at 2×" title="2x">
</details>

Its widest IRC row is 260 bytes as `blockwright-cli export --irc` writes it; as WeeChat's ascii script sends it, the widest is 278. The project's budget is 407 bytes, and no row is over it.

Download: [ridges-at-dusk.bwp](gallery/04-generator-ridges/ridges-at-dusk.bwp), the project, layers, notes and all; [ridges-at-dusk.ans](gallery/04-generator-ridges/ridges-at-dusk.ans), the piece flattened.

The generators packed in ridges-at-dusk.bwp, `scripts/2/` (the stars, `stars.sh` and `stars.awk`), `scripts/3/` and `scripts/4/` (the ridges, `ridges.sh` and `ridges.awk`), are Blockwright's own and stay under its licence, the GPL version 3 or later ([Blockwright's `LICENSE`](https://git.pumpin.online/funkpower/blockwright/src/branch/main/LICENSE)); the rest is under this site's licence.

## Traveller {#traveller}

A traveller with a staff and a pack, looking out over a meadow toward the hills, drawn in half-block pixels on layers of their own: an outline, the body, the face, the highlights and the shadow on the grass, all one size and in one place over a locked scene, with a hidden copy of the whole figure merged onto one layer to move with a single Alt+drag.

80 × 30 cells, 9 layers.

### Layer by layer

The visible layers from the bottom up, each picture adding one to the ones before it: sky, hills, meadow, shadow, outline, body, face detail and highlights. The one hidden layer, figure (merged), stays hidden, as it is when the project opens.

<div class="strip">
<figure><img src="gallery/05-character/layer-01.ans" alt="Traveller, its bottom layer, sky, alone"><figcaption>sky</figcaption></figure>
<figure><img src="gallery/05-character/layer-02.ans" alt="Traveller with its bottom 2 visible layers: sky and hills"><figcaption>+ hills</figcaption></figure>
<figure><img src="gallery/05-character/layer-03.ans" alt="Traveller with its bottom 3 visible layers: sky, hills and meadow"><figcaption>+ meadow</figcaption></figure>
<figure><img src="gallery/05-character/layer-04.ans" alt="Traveller with its bottom 4 visible layers: sky, hills, meadow and shadow"><figcaption>+ shadow</figcaption></figure>
<figure><img src="gallery/05-character/layer-05.ans" alt="Traveller with its bottom 5 visible layers: sky, hills, meadow, shadow and outline"><figcaption>+ outline</figcaption></figure>
<figure><img src="gallery/05-character/layer-06.ans" alt="Traveller with its bottom 6 visible layers: sky, hills, meadow, shadow, outline and body"><figcaption>+ body</figcaption></figure>
<figure><img src="gallery/05-character/layer-07.ans" alt="Traveller with its bottom 7 visible layers: sky, hills, meadow, shadow, outline, body and face detail"><figcaption>+ face detail</figcaption></figure>
<figure><img src="gallery/05-character/layer-08.ans" alt="Traveller with its bottom 8 visible layers: sky, hills, meadow, shadow, outline, body, face detail and highlights"><figcaption>+ highlights</figcaption></figure>
</div>

Each layer, as its notes describe it, from the top down:

| Layer | Kind | Mode | Locks | What it does |
|---|---|---|---|---|
| figure (merged) | pixels | normal | - | Hidden: the five layers below merged onto one, the same size and in the same place, so a single Alt+drag moves the whole figure |
| highlights | pixels | normal | - | Small clusters of light where the sun from the upper left catches the crown of the hat, the upper arm and the tip of the staff |
| face detail | pixels | normal | - | The eye and the mouth, over the skin |
| body | pixels | normal | alpha | The figure in flat colours, a colour a part: hat and band, grey hair, skin, scarf, a red coat lit down its front edges, a green pack lit along its top, trousers, boots, glove and staff. Alpha-locked, so paint stays inside the figure |
| outline | pixels | normal | - | The whole silhouette grown a pixel all round, in black, under the body: it parts the figure from the sky and the grass and fills the shade under the arm |
| shadow | pixels | normal | - | The shadow the figure casts on the grass, away from the light: a strip of darker green out from the back boot |
| meadow | cells | normal | locked | Light green grass, a brown path coming out of the hills toward the front, and tufts of darker grass in the near rows |
| hills | cells | normal | locked | Far hills in the haze, cyan against the light cyan sky, their tops in half-block steps |
| sky | cells | normal | locked | The ice ramp a rung a row: blue at the top, light blue, then light cyan down to the hills |

### Variants

The variants the project offers in the Layers dock, each a few layers shown, hidden or moved:

<div class="strip">
<figure><img src="gallery/05-character/variant-01.ans" alt="Traveller, the No outline variant: hide outline"><figcaption>No outline<br><small>hide outline</small></figcaption></figure>
<figure><img src="gallery/05-character/variant-02.ans" alt="Traveller, the No highlights variant: hide highlights"><figcaption>No highlights<br><small>hide highlights</small></figcaption></figure>
<figure><img src="gallery/05-character/variant-03.ans" alt="Traveller, the Silhouette variant: raise outline above highlights"><figcaption>Silhouette<br><small>raise outline above highlights</small></figcaption></figure>
<figure><img src="gallery/05-character/variant-04.ans" alt="Traveller, the One layer variant: show figure (merged); hide highlights; hide face detail; hide body; hide outline; hide shadow"><figcaption>One layer<br><small>show figure (merged); hide highlights; hide face detail; hide body; hide outline; hide shadow</small></figcaption></figure>
<figure><img src="gallery/05-character/variant-05.ans" alt="Traveller, the Scene only variant: hide highlights; hide face detail; hide body; hide outline; hide shadow"><figcaption>Scene only<br><small>hide highlights; hide face detail; hide body; hide outline; hide shadow</small></figcaption></figure>
</div>

### The finished piece

![Traveller, the finished piece at 1×](gallery/05-character/traveller.ans)

<details><summary>At 2×</summary>
<img src="gallery/05-character/traveller.ans" alt="Traveller, the finished piece at 2×" title="2x">
</details>

Its widest IRC row is 268 bytes as `blockwright-cli export --irc` writes it; as WeeChat's ascii script sends it, the widest is 277. The project's budget is 407 bytes, and no row is over it.

Download: [traveller.bwp](gallery/05-character/traveller.bwp), the project, layers, notes and all; [traveller.ans](gallery/05-character/traveller.ans), the piece flattened.

## Blockwright logo {#blockwright-logo}

The program's own logo taken apart into the layers a block-letter logo is made of: the mark's four blocks, the BLOCK and WRIGHT lettering in half-block pixels, a blue drop under the letters, and the shade cells that take each stroke from light cyan down to cyan, all over a locked black backdrop. Shown together they make the logo exactly as it ships with Blockwright.

80 × 18 cells, 6 layers.

### Layer by layer

The visible layers from the bottom up, each picture adding one to the ones before it: backdrop, white blocks, gold block, drop, letters and shading.

<div class="strip">
<figure><img src="gallery/06-blockwright-logo/layer-01.ans" alt="Blockwright logo, its bottom layer, backdrop, alone"><figcaption>backdrop</figcaption></figure>
<figure><img src="gallery/06-blockwright-logo/layer-02.ans" alt="Blockwright logo with its bottom 2 visible layers: backdrop and white blocks"><figcaption>+ white blocks</figcaption></figure>
<figure><img src="gallery/06-blockwright-logo/layer-03.ans" alt="Blockwright logo with its bottom 3 visible layers: backdrop, white blocks and gold block"><figcaption>+ gold block</figcaption></figure>
<figure><img src="gallery/06-blockwright-logo/layer-04.ans" alt="Blockwright logo with its bottom 4 visible layers: backdrop, white blocks, gold block and drop"><figcaption>+ drop</figcaption></figure>
<figure><img src="gallery/06-blockwright-logo/layer-05.ans" alt="Blockwright logo with its bottom 5 visible layers: backdrop, white blocks, gold block, drop and letters"><figcaption>+ letters</figcaption></figure>
<figure><img src="gallery/06-blockwright-logo/layer-06.ans" alt="Blockwright logo with its bottom 6 visible layers: backdrop, white blocks, gold block, drop, letters and shading"><figcaption>+ shading</figcaption></figure>
</div>

Each layer, as its notes describe it, from the top down:

| Layer | Kind | Mode | Locks | What it does |
|---|---|---|---|---|
| shading | cells | normal | - | ▓ ▒ ░ in light cyan on cyan, a rung a row down each stroke, with a stem's left column a rung lighter where the light from the upper left falls |
| letters | pixels | normal | alpha | BLOCK over WRIGHT in half-block pixels, two pixels to a stroke with rounded corners: light cyan, and cyan at the foot. Alpha-locked, so paint stays inside the letters |
| drop | pixels | normal | - | The letters moved one column right and one pixel down, in blue, under them: a rim along their right and lower edges that lifts them off the black. It stays out of the counters of the B, O and R |
| gold block | cells | normal | - | The mark's top block, yellow going through ▓ ▒ ░ to brown, with a white top edge and a brown side and foot |
| white blocks | cells | normal | - | The mark's three white blocks in an L, white on grey going from ▓ to ░, with a dark grey side and foot |
| backdrop | cells | normal | locked | Black |

### Variants

The variants the project offers in the Layers dock, each a few layers shown, hidden or moved:

<div class="strip">
<figure><img src="gallery/06-blockwright-logo/variant-01.ans" alt="Blockwright logo, the No shading variant: hide shading"><figcaption>No shading<br><small>hide shading</small></figcaption></figure>
<figure><img src="gallery/06-blockwright-logo/variant-02.ans" alt="Blockwright logo, the No drop variant: hide drop"><figcaption>No drop<br><small>hide drop</small></figcaption></figure>
<figure><img src="gallery/06-blockwright-logo/variant-03.ans" alt="Blockwright logo, the Wordmark only variant: hide gold block; hide white blocks"><figcaption>Wordmark only<br><small>hide gold block; hide white blocks</small></figcaption></figure>
<figure><img src="gallery/06-blockwright-logo/variant-04.ans" alt="Blockwright logo, the Mark only variant: hide shading; hide letters; hide drop"><figcaption>Mark only<br><small>hide shading; hide letters; hide drop</small></figcaption></figure>
</div>

### The finished piece

![Blockwright logo, the finished piece at 1×](gallery/06-blockwright-logo/blockwright-logo.ans)

<details><summary>At 2×</summary>
<img src="gallery/06-blockwright-logo/blockwright-logo.ans" alt="Blockwright logo, the finished piece at 2×" title="2x">
</details>

Its widest IRC row is 324 bytes as `blockwright-cli export --irc` writes it; as WeeChat's ascii script sends it, the widest is 350. The project's budget is 407 bytes, and no row is over it.

Download: [blockwright-logo.bwp](gallery/06-blockwright-logo/blockwright-logo.bwp), the project, layers, notes and all; [blockwright-logo.ans](gallery/06-blockwright-logo/blockwright-logo.ans), the piece flattened.

## Battlestation {#battlestation}

A night desk seen from behind the chair. A wide monitor running a tiling layout is the only light in the room, and the blue it throws on the wall, the desk and the rack sits on a colours-only layer of its own, so the light can go out without a glyph moving. Eleven layers: a locked wall, nine layers of desk, hardware, light and chair on it, and one hidden layer a variant uses.

80 × 40 cells, 11 layers.

### Layer by layer

The visible layers from the bottom up, each picture adding one to the ones before it: wall, desk, monitor frame, screen, keyboard, mug and mouse, rack, glow, chair and signature. The one hidden layer, margins, stays hidden, as it is when the project opens.

<div class="strip">
<figure><img src="gallery/07-battlestation/layer-01.ans" alt="Battlestation, its bottom layer, wall, alone"><figcaption>wall</figcaption></figure>
<figure><img src="gallery/07-battlestation/layer-02.ans" alt="Battlestation with its bottom 2 visible layers: wall and desk"><figcaption>+ desk</figcaption></figure>
<figure><img src="gallery/07-battlestation/layer-03.ans" alt="Battlestation with its bottom 3 visible layers: wall, desk and monitor frame"><figcaption>+ monitor frame</figcaption></figure>
<figure><img src="gallery/07-battlestation/layer-04.ans" alt="Battlestation with its bottom 4 visible layers: wall, desk, monitor frame and screen"><figcaption>+ screen</figcaption></figure>
<figure><img src="gallery/07-battlestation/layer-05.ans" alt="Battlestation with its bottom 5 visible layers: wall, desk, monitor frame, screen and keyboard"><figcaption>+ keyboard</figcaption></figure>
<figure><img src="gallery/07-battlestation/layer-06.ans" alt="Battlestation with its bottom 6 visible layers: wall, desk, monitor frame, screen, keyboard and mug and mouse"><figcaption>+ mug and mouse</figcaption></figure>
<figure><img src="gallery/07-battlestation/layer-07.ans" alt="Battlestation with its bottom 7 visible layers: wall, desk, monitor frame, screen, keyboard, mug and mouse and rack"><figcaption>+ rack</figcaption></figure>
<figure><img src="gallery/07-battlestation/layer-08.ans" alt="Battlestation with its bottom 8 visible layers: wall, desk, monitor frame, screen, keyboard, mug and mouse, rack and glow"><figcaption>+ glow</figcaption></figure>
<figure><img src="gallery/07-battlestation/layer-09.ans" alt="Battlestation with its bottom 9 visible layers: wall, desk, monitor frame, screen, keyboard, mug and mouse, rack, glow and chair"><figcaption>+ chair</figcaption></figure>
<figure><img src="gallery/07-battlestation/layer-10.ans" alt="Battlestation with its bottom 10 visible layers: wall, desk, monitor frame, screen, keyboard, mug and mouse, rack, glow, chair and signature"><figcaption>+ signature</figcaption></figure>
</div>

Each layer, as its notes describe it, from the top down:

| Layer | Kind | Mode | Locks | What it does |
|---|---|---|---|---|
| signature | cells | normal | - | The tag in dark grey in the lower left corner. |
| chair | cells | normal | - | The racing chair from behind: a dark grey back under a grey headrest with a light cyan top, its sides trimmed in light blue and blue, the armrests and the base. |
| glow | cells | colours-only | - | The blue the screen throws: the rings on the wall round the monitor, the desk top and the rack's side and top edge toward the screen. In its colours-only mode it gives colours and no shapes; the glyphs are the layers' under it, so with it hidden the same cells show in the dark colours those layers have. |
| rack | cells | normal | - | The home-lab rack on the right: a dark grey cabinet with a grey post down its left side, units with light green, yellow, light red and light cyan lights, and a light green display at the foot. Its side and top edge toward the screen are dark grey here, and the side black toward the foot; the glow lights it. |
| mug and mouse | cells | normal | - | A dark grey mug of coffee left of the keyboard, its rim and right side catching light blue and light cyan, and a mouse with a light blue top on a pad to the right. |
| keyboard | cells | normal | - | Grey keys on a dark grey board edged in light blue, a light magenta key at the top left and a light cyan one on the right, and an underglow strip along the front in light cyan, light blue and light magenta. |
| screen | cells | normal | alpha | The tiling layout: a top bar with workspace markers, a title and a status block; a wallpaper banded from magenta down to blue, a row of magenta and then three rows a band; a code pane in a light cyan border, with dark grey line numbers, a bar of colour for each word and a highlighted line; a terminal pane with its cursor; and a pane of light green bars with yellow and light red peaks. No word on it can be read. Alpha-locked, so paint stays on the screen's own cells. |
| monitor frame | cells | normal | - | The bezel in dark grey with a light blue top edge, a light cyan power light at the lower right, and the neck of the stand. |
| desk | cells | normal | - | The desk with the screen off: a dark grey back edge, three rows of dark grey shading thinning toward the front, black from there to the front edge, and two dark grey legs. The glow puts the blue under the shading and on the front half. |
| margins | cells | normal | - | Hidden: a black block in the bottom left corner. The Screen only variant shows it. |
| wall | cells | normal | locked | The wall, black, with the shading of the rings round the monitor already in place in black on black, and a black block in the top left corner. Locked, so painting the desk or the screen never touches it. |

### Variants

The variants the project offers in the Layers dock, each a few layers shown, hidden or moved:

<div class="strip">
<figure><img src="gallery/07-battlestation/variant-01.ans" alt="Battlestation, the No glow variant: hide glow"><figcaption>No glow<br><small>hide glow</small></figcaption></figure>
<figure><img src="gallery/07-battlestation/variant-02.ans" alt="Battlestation, the Lights off variant: hide glow; hide screen"><figcaption>Lights off<br><small>hide glow; hide screen</small></figcaption></figure>
<figure><img src="gallery/07-battlestation/variant-03.ans" alt="Battlestation, the Screen only variant: hide desk; hide keyboard; hide mug and mouse; hide rack; hide glow; hide chair; hide signature; show margins"><figcaption>Screen only<br><small>hide desk; hide keyboard; hide mug and mouse; hide rack; hide glow; hide chair; hide signature; show margins</small></figcaption></figure>
</div>

### The finished piece

![Battlestation, the finished piece at 1×](gallery/07-battlestation/battlestation.ans)

<details><summary>At 2×</summary>
<img src="gallery/07-battlestation/battlestation.ans" alt="Battlestation, the finished piece at 2×" title="2x">
</details>

Its widest IRC row is 285 bytes as `blockwright-cli export --irc` writes it; as WeeChat's ascii script sends it, the widest is 295. The project's budget is 407 bytes, and no row is over it.

Download: [battlestation.bwp](gallery/07-battlestation/battlestation.bwp), the project, layers, notes and all; [battlestation.ans](gallery/07-battlestation/battlestation.ans), the piece flattened.

## This Is Your Brain on IRC {#this-is-your-brain-on-irc}

One egg frying in a pan, seen from above, under the caption THIS IS YOUR BRAIN ON IRC. The yolk is a speech bubble with a # pressed into it. The yolk is a dome and the pan a cylinder, two of the three forms the Form brush knows, and each is one pass of that brush over a flat copy kept hidden beneath it. Fourteen layers: a locked black background, three of lettering, the pan twice, the egg white, the yolk twice, the # and the highlight, two of heat, and one hidden layer a variant uses.

80 × 32 cells, 14 layers.

### Layer by layer

The visible layers from the bottom up, each picture adding one to the ones before it: background, caption, tagline, signature, pan, egg white, yolk, #, highlight, sizzle and smoke. The hidden layers, margins, pan (flat) and yolk (flat), stay hidden, as they are when the project opens.

<div class="strip">
<figure><img src="gallery/08-brain-on-irc/layer-01.ans" alt="This Is Your Brain on IRC, its bottom layer, background, alone"><figcaption>background</figcaption></figure>
<figure><img src="gallery/08-brain-on-irc/layer-02.ans" alt="This Is Your Brain on IRC with its bottom 2 visible layers: background and caption"><figcaption>+ caption</figcaption></figure>
<figure><img src="gallery/08-brain-on-irc/layer-03.ans" alt="This Is Your Brain on IRC with its bottom 3 visible layers: background, caption and tagline"><figcaption>+ tagline</figcaption></figure>
<figure><img src="gallery/08-brain-on-irc/layer-04.ans" alt="This Is Your Brain on IRC with its bottom 4 visible layers: background, caption, tagline and signature"><figcaption>+ signature</figcaption></figure>
<figure><img src="gallery/08-brain-on-irc/layer-05.ans" alt="This Is Your Brain on IRC with its bottom 5 visible layers: background, caption, tagline, signature and pan"><figcaption>+ pan</figcaption></figure>
<figure><img src="gallery/08-brain-on-irc/layer-06.ans" alt="This Is Your Brain on IRC with its bottom 6 visible layers: background, caption, tagline, signature, pan and egg white"><figcaption>+ egg white</figcaption></figure>
<figure><img src="gallery/08-brain-on-irc/layer-07.ans" alt="This Is Your Brain on IRC with its bottom 7 visible layers: background, caption, tagline, signature, pan, egg white and yolk"><figcaption>+ yolk</figcaption></figure>
<figure><img src="gallery/08-brain-on-irc/layer-08.ans" alt="This Is Your Brain on IRC with its bottom 8 visible layers: background, caption, tagline, signature, pan, egg white, yolk and #"><figcaption>+ #</figcaption></figure>
<figure><img src="gallery/08-brain-on-irc/layer-09.ans" alt="This Is Your Brain on IRC with its bottom 9 visible layers: background, caption, tagline, signature, pan, egg white, yolk, # and highlight"><figcaption>+ highlight</figcaption></figure>
<figure><img src="gallery/08-brain-on-irc/layer-10.ans" alt="This Is Your Brain on IRC with its bottom 10 visible layers: background, caption, tagline, signature, pan, egg white, yolk, #, highlight and sizzle"><figcaption>+ sizzle</figcaption></figure>
<figure><img src="gallery/08-brain-on-irc/layer-11.ans" alt="This Is Your Brain on IRC with its bottom 11 visible layers: background, caption, tagline, signature, pan, egg white, yolk, #, highlight, sizzle and smoke"><figcaption>+ smoke</figcaption></figure>
</div>

Each layer, as its notes describe it, from the top down:

| Layer | Kind | Mode | Locks | What it does |
|---|---|---|---|---|
| smoke | cells | normal | - | Three wisps of grey and dark grey shade rising off the pan. The outer two rise from a single cell to three across at the top; the middle one is three cells across on each of its three rows. |
| sizzle | pixels | normal | - | The fat spitting at the white's edge: two yellow arcs on each side of the egg and two white spits. At three of the places where an arc steps a pixel diagonally, a pixel joins the step, since the lint counts a lone pixel as noise. |
| highlight | pixels | normal | - | The light on the yolk from the upper left: a white crescent along its upper left, a glint two pixels wide at its lower left and one pixel at its upper right. |
| # | pixels | normal | - | The # pressed into the yolk in brown: two bars across and two strokes down, leaning right. |
| yolk | cells | normal | alpha | The yolk after one pass of the Form brush: a dome on the skin ramp at 65%: yellow over most of it, light red and brown along its top edge, and brown over red down its right side, the side away from the light. One cell at its tail is set to the shade of the cell above it. Alpha-locked, so a brush keeps to the yolk's own cells. |
| yolk (flat) | cells | normal | alpha | Hidden: the yolk as a speech bubble in flat yellow, its tail at the lower left. The Raw egg variant shows it. |
| egg white | cells | normal | - | The white: white in the middle, thinning to grey at its edge, a fringe of browned lace with the pan showing through it, four grey blisters, and the yolk's grey shadow down and to the right. |
| pan | cells | normal | alpha | The pan after one pass of the Form brush: a cylinder on the steel ramp at 100%. The ring, the lip on the left and the handle on the right, with a hole at its end, are white along most of their upper edges and black along most of their lower ones. Eleven cells along the upper and lower edges keep the flat dark grey, where the brush took back a change the lint would have reported: four on the inner edge at the top of the ring, four under the handle and three more on the ring's sides. One cell beside the sizzle is set to the shade of its neighbour. Alpha-locked, so a brush keeps to the pan's own cells. |
| pan (flat) | cells | normal | alpha | Hidden: the pan in flat dark grey. The Raw egg variant shows it. |
| signature | cells | normal | - | The tag in dark grey in the lower right corner. |
| tagline | cells | normal | - | Any questions? in white and /msg me. in yellow, under the pan. |
| caption | cells | normal | - | THIS IS YOUR BRAIN ON IRC in two rows of block letters, white with a grey foot and IRC in yellow with a brown foot. |
| margins | cells | normal | - | Hidden: a black block in the top left corner. The No caption variant shows it. |
| background | cells | normal | locked | Black, the whole canvas, which is also the floor of the pan. Locked, so painting the egg never touches it. |

### Variants

The variants the project offers in the Layers dock, each a few layers shown, hidden or moved:

<div class="strip">
<figure><img src="gallery/08-brain-on-irc/variant-01.ans" alt="This Is Your Brain on IRC, the Raw egg variant: hide pan; show pan (flat); hide yolk; show yolk (flat); hide #; hide highlight; hide sizzle; hide smoke"><figcaption>Raw egg<br><small>hide pan; show pan (flat); hide yolk; show yolk (flat); hide #; hide highlight; hide sizzle; hide smoke</small></figcaption></figure>
<figure><img src="gallery/08-brain-on-irc/variant-02.ans" alt="This Is Your Brain on IRC, the No caption variant: hide caption; hide tagline; show margins"><figcaption>No caption<br><small>hide caption; hide tagline; show margins</small></figcaption></figure>
</div>

### The finished piece

![This Is Your Brain on IRC, the finished piece at 1×](gallery/08-brain-on-irc/this-is-your-brain-on-irc.ans)

<details><summary>At 2×</summary>
<img src="gallery/08-brain-on-irc/this-is-your-brain-on-irc.ans" alt="This Is Your Brain on IRC, the finished piece at 2×" title="2x">
</details>

Its widest IRC row is 273 bytes as `blockwright-cli export --irc` writes it; as WeeChat's ascii script sends it, the widest is 301. The project's budget is 407 bytes, and no row is over it.

Download: [this-is-your-brain-on-irc.bwp](gallery/08-brain-on-irc/this-is-your-brain-on-irc.bwp), the project, layers, notes and all; [this-is-your-brain-on-irc.ans](gallery/08-brain-on-irc/this-is-your-brain-on-irc.ans), the piece flattened.

## wtc-0903 {#wtc-0903}

Lower Manhattan at 9:03 on the morning of 11 September 2001, seen from across the East River: United Airlines Flight 175 going into the South Tower, the fireball breaking out of the tower's east face, and the North Tower burning behind it, its smoke carried left across the sky. A hundred columns wide, twenty more than a terminal opens at, and every row still fits one IRC line. Twelve layers: a locked sky, ten layers of towers, smoke, fire, light, city and water on it, and the tag.

100 × 48 cells, 12 layers.

### Layer by layer

The visible layers from the bottom up, each picture adding one to the ones before it: sky, North Tower, plume, fire, South Tower, sunlight, fireball, plane, skyline, water, reflections and tag.

<div class="strip">
<figure><img src="gallery/09-wtc-0903/layer-01.ans" alt="wtc-0903, its bottom layer, sky, alone"><figcaption>sky</figcaption></figure>
<figure><img src="gallery/09-wtc-0903/layer-02.ans" alt="wtc-0903 with its bottom 2 visible layers: sky and North Tower"><figcaption>+ North Tower</figcaption></figure>
<figure><img src="gallery/09-wtc-0903/layer-03.ans" alt="wtc-0903 with its bottom 3 visible layers: sky, North Tower and plume"><figcaption>+ plume</figcaption></figure>
<figure><img src="gallery/09-wtc-0903/layer-04.ans" alt="wtc-0903 with its bottom 4 visible layers: sky, North Tower, plume and fire"><figcaption>+ fire</figcaption></figure>
<figure><img src="gallery/09-wtc-0903/layer-05.ans" alt="wtc-0903 with its bottom 5 visible layers: sky, North Tower, plume, fire and South Tower"><figcaption>+ South Tower</figcaption></figure>
<figure><img src="gallery/09-wtc-0903/layer-06.ans" alt="wtc-0903 with its bottom 6 visible layers: sky, North Tower, plume, fire, South Tower and sunlight"><figcaption>+ sunlight</figcaption></figure>
<figure><img src="gallery/09-wtc-0903/layer-07.ans" alt="wtc-0903 with its bottom 7 visible layers: sky, North Tower, plume, fire, South Tower, sunlight and fireball"><figcaption>+ fireball</figcaption></figure>
<figure><img src="gallery/09-wtc-0903/layer-08.ans" alt="wtc-0903 with its bottom 8 visible layers: sky, North Tower, plume, fire, South Tower, sunlight, fireball and plane"><figcaption>+ plane</figcaption></figure>
<figure><img src="gallery/09-wtc-0903/layer-09.ans" alt="wtc-0903 with its bottom 9 visible layers: sky, North Tower, plume, fire, South Tower, sunlight, fireball, plane and skyline"><figcaption>+ skyline</figcaption></figure>
<figure><img src="gallery/09-wtc-0903/layer-10.ans" alt="wtc-0903 with its bottom 10 visible layers: sky, North Tower, plume, fire, South Tower, sunlight, fireball, plane, skyline and water"><figcaption>+ water</figcaption></figure>
<figure><img src="gallery/09-wtc-0903/layer-11.ans" alt="wtc-0903 with its bottom 11 visible layers: sky, North Tower, plume, fire, South Tower, sunlight, fireball, plane, skyline, water and reflections"><figcaption>+ reflections</figcaption></figure>
<figure><img src="gallery/09-wtc-0903/layer-12.ans" alt="wtc-0903 with its bottom 12 visible layers: sky, North Tower, plume, fire, South Tower, sunlight, fireball, plane, skyline, water, reflections and tag"><figcaption>+ tag</figcaption></figure>
</div>

Each layer, as its notes describe it, from the top down:

| Layer | Kind | Mode | Locks | What it does |
|---|---|---|---|---|
| tag | cells | normal | - | funkpower in grey in the lower right corner, row 47. |
| reflections | cells | colours-only | - | The shore buildings in the water along row 43, all in dark grey, with two columns of every five left out where the ripples break them. It holds colours and no shapes; the glyphs are the water's, so with it hidden row 43 is plain light blue. |
| water | cells | normal | - | The river from row 43 down: light blue along the shore, then blue, with short ripples in light cyan near the shore and in light blue further out. |
| skyline | cells | normal | - | Downtown in front of the towers' feet, from row 25 down: grey, white, dark grey and black buildings with bands of windows and plant rooms on some roofs, 40 Wall Street's cyan pyramid under a dark grey spire at column 79, rows 25 to 27, alone above the other roofs, and the shore along row 42, a black drive with dark grey piers. |
| plane | cells | normal | - | United 175, banked left wing down: the near wing and the top of the fuselage in grey, the rest of the fuselage, the far wing and the tail fin in dark grey. Its nose is already inside the South Tower's south face, where a black hole is cut at column 44, rows 18 and 19. |
| fireball | cells | normal | - | The fireball out of the South Tower's east face and across in front of the North Tower: a white and yellow core, brown and red around it, and a dark grey rim on the right. |
| sunlight | cells | normal | - | The morning sun on both east faces: white pinstripes on grey where the shade has grey on dark grey, and the crowns white over grey. It lights only the cells the plume and the fire left showing, so the shapes of both are cut out of it. |
| South Tower | cells | normal | alpha | The South Tower in shade, columns 42 to 55 from row 9 down: the south face, 42 to 45, and the east face, 46 to 55, both grey pinstripes on dark grey, under a grey roof line. It is nearer than the North Tower and the smoke, so it sits above them. Alpha-locked, so paint stays on the tower's own cells. |
| fire | cells | normal | - | The North Tower's fire, rows 13 to 15 across columns 60 to 73: a black gash along row 13, red and brown flames under it on the east face with yellow along their foot, and red and black on the south face. |
| plume | cells | normal | - | The smoke from the North Tower's fire, carried left behind the South Tower and out at the left edge: lobes of dark grey with grey crowns on the side toward the sun, black underneath and black where it leaves the tower, thinning to dark grey shade over the sky at the far end. The fire covers it at one cell, column 62 on row 13. |
| North Tower | cells | normal | alpha | The North Tower in shade, columns 60 to 73 from row 10 down, faces like the South Tower's, and the mast on its roof in grey up to row 2. The east-face cells the plume and the fire cover are drawn in the sun already. Alpha-locked, so paint stays on the tower's own cells. |
| sky | cells | normal | locked | The morning sky: blue at the top, light blue from row 13, light cyan from row 27, with three rows of shade at each change, rows 10 to 12 and 24 to 26. Locked, so painting the towers never touches it. |

### Variants

The variants the project offers in the Layers dock, each a few layers shown, hidden or moved:

<div class="strip">
<figure><img src="gallery/09-wtc-0903/variant-01.ans" alt="wtc-0903, the Before 8:46 variant: hide plume; hide fire; hide fireball; hide plane"><figcaption>Before 8:46<br><small>hide plume; hide fire; hide fireball; hide plane</small></figcaption></figure>
<figure><img src="gallery/09-wtc-0903/variant-02.ans" alt="wtc-0903, the Sunlight off variant: hide sunlight"><figcaption>Sunlight off<br><small>hide sunlight</small></figcaption></figure>
<figure><img src="gallery/09-wtc-0903/variant-03.ans" alt="wtc-0903, the Fire only variant: hide North Tower; hide plume; hide South Tower; hide sunlight; hide plane; hide skyline; hide water; hide reflections; hide tag"><figcaption>Fire only<br><small>hide North Tower; hide plume; hide South Tower; hide sunlight; hide plane; hide skyline; hide water; hide reflections; hide tag</small></figcaption></figure>
<figure><img src="gallery/09-wtc-0903/variant-04.ans" alt="wtc-0903, the Smoke in front variant: raise plume above sunlight"><figcaption>Smoke in front<br><small>raise plume above sunlight</small></figcaption></figure>
</div>

### The finished piece

![wtc-0903, the finished piece at 1×](gallery/09-wtc-0903/wtc-0903.ans)

<details><summary>At 2×</summary>
<img src="gallery/09-wtc-0903/wtc-0903.ans" alt="wtc-0903, the finished piece at 2×" title="2x">
</details>

Its widest IRC row is 344 bytes as `blockwright-cli export --irc` writes it; as WeeChat's ascii script sends it, the widest is 347. The project's budget is 407 bytes, and no row is over it.

Download: [wtc-0903.bwp](gallery/09-wtc-0903/wtc-0903.bwp), the project, layers, notes and all; [wtc-0903.ans](gallery/09-wtc-0903/wtc-0903.ans), the piece flattened.
