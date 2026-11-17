Title: Blockwright
Checked: Blockwright 0.1.1 (609a15c)

# Blockwright {.visually-hidden}

<div class="hero">
<div class="logo"><img src="samples/home/logo-large.ans" alt="####  ##    ###   #### ## ## ##   ## ####  ####  #### ## ## ######
## ## ##   ## ## ##    ####  ## # ## ## ##  ##  ##    ## ##   ##
####  ##   ## ## ##    ###   ## # ## ####   ##  ## ## #####   ##
## ## ##   ## ## ##    ####  ####### ## #   ##  ## ## ## ##   ##
####  ####  ###   #### ## ##  ## ##  ## ## ####  #### ## ##   ##"></div>
<div class="hero-text">
<p class="tagline">An editor for ANSI and IRC art: half-block pixels, shading along colour ramps, lighting, layers, and a live byte meter so every line fits on IRC.</p>
<div class="term">
<p><span class="ps1" aria-hidden="true">$ </span>blockwright --version | head -n 1</p>
<p class="out">blockwright 0.1.1 (bd67fae)</p>
<p aria-hidden="true"><span class="ps1">$ </span><span class="cursor"></span></p>
</div>
<p>For Linux, FreeBSD, macOS and Windows.</p>
<p class="actions"><a class="button" href="#download">Download 0.1.1</a> <a class="button" href="samples/index.md">Samples</a> <a class="button" href="tutorials/index.md">Tutorials</a></p>
</div>
</div>

<div class="rule" aria-hidden="true"><span>█▓▒░</span>░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░</div>

<h2 id="windows"><span class="visually-hidden">The window</span><span aria-hidden="true">blockwright</span></h2>

<div class="shots">
<figure><img src="samples/home/harbour.png" alt="The Blockwright window with Harbour at night open: a city skyline under a full moon over the water, with HARBOUR in yellow block letters. The Half-Block Brush is in Tool Options with a yellow pen, and the moon, a Pixels layer, is selected in the Layers dock." width="1600" height="1000"><figcaption>Harbour at night, a layer of every kind</figcaption></figure>
<figure><img src="samples/home/still-life.png" alt="The Blockwright window with Still life open: a cylinder shaded from white to magenta, a box in yellow, brown and red, and a ball in cyan and blue on a grey table, against a dark grey wall. The Form Brush is in Tool Options, set to a dome lit from the north-west on the sea ramp, with Glint and Alpha lock ticked." width="1600" height="1000"><figcaption>Still life and the Form Brush</figcaption></figure>
<figure><img src="samples/home/battlestation.png" alt="The Blockwright window with Battlestation open: a desk seen from behind the chair, a wide monitor lighting the room blue, and a server rack on the right. The Colorize Brush is in Tool Options, and the glow layer is selected in the Layers dock." width="1600" height="1000"><figcaption>Battlestation and the Colorize Brush</figcaption></figure>
</div>

<div class="rule" aria-hidden="true"><span>█▓▒░</span>░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░</div>

<h2 id="download"><span class="visually-hidden">Download</span><span aria-hidden="true">ls releases/v0.1.1/</span></h2>

<p class="lead">Blockwright 0.1.1, released on 14 November 2026. Every package holds both <code>blockwright</code>, the editor, and <code>blockwright-cli</code>, the command line; each card says where it puts the second. Each file but the <code>PKGBUILD</code> has a <code>.sha256</code> file beside it with its SHA-256 checksum (<a href="manual/01-install.md#checksums">checking it</a>). The <a href="https://git.pumpin.online/funkpower/blockwright/releases/tag/v0.1.1">release page</a> lists every file, and the manual's <a href="manual/01-install.md">install page</a> takes each system in turn.</p>

<div class="downloads">

<section class="dl" id="dl-macos">
<h3>macOS</h3>
<p><a href="https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/Blockwright-0.1.1.dmg">Blockwright-0.1.1.dmg</a></p>
<p>macOS 12 or later, Apple Silicon and Intel. The command line stays inside the app, at <code>Blockwright.app/Contents/MacOS/blockwright-cli</code>.</p>
<p>Homebrew installs it too, from funkpower's <a href="https://git.pumpin.online/funkpower/homebrew-tap">tap</a>, and links <code>blockwright-cli</code> onto the <code>PATH</code>; the manual's <a href="manual/01-install.md#homebrew">Homebrew section</a> gives the two commands.</p>
<p class="how"><a href="manual/01-install.md#macos">Installing on macOS</a></p>
</section>

<section class="dl" id="dl-windows">
<h3>Windows</h3>
<p><a href="https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-x86_64.msi">blockwright-0.1.1-x86_64.msi</a></p>
<p>Windows 10 or later, x86-64. It installs <code>blockwright.exe</code> and <code>blockwright-cli.exe</code> in the <code>bin</code> folder of <code>Program Files\Blockwright</code>, which it doesn't add to the <code>PATH</code>.</p>
<p class="how"><a href="manual/01-install.md#windows">Installing on Windows</a></p>
</section>

<section class="dl" id="dl-appimage">
<h3>Linux · AppImage</h3>
<p><a href="https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-x86_64.AppImage">blockwright-0.1.1-x86_64.AppImage</a></p>
<p>Any x86-64 distribution with glibc 2.36 or newer. One file holds both programs: it runs the editor, or the command line when <code>--cli</code> comes first or when it's started through a link named <code>blockwright-cli</code>. Where AppImageLauncher is installed, that link starts the editor; use a two-line script that runs the AppImage with <code>--cli</code> first instead, after removing the link.</p>
<p class="how"><a href="manual/01-install.md#linux-appimage">Installing the AppImage</a>, the script included</p>
</section>

<section class="dl" id="dl-deb">
<h3>Debian and Ubuntu</h3>
<ul class="files">
<li>Debian 13: <a href="https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright_0.1.1-1_debian13_amd64.deb">blockwright_0.1.1-1_debian13_amd64.deb</a></li>
<li>Debian testing (forky): <a href="https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright_0.1.1-1_debian-testing_amd64.deb">blockwright_0.1.1-1_debian-testing_amd64.deb</a></li>
<li>Ubuntu 26.04: <a href="https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright_0.1.1-1_ubuntu26.04_amd64.deb">blockwright_0.1.1-1_ubuntu26.04_amd64.deb</a></li>
<li>Ubuntu 26.10: <a href="https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright_0.1.1-1_ubuntu26.10_amd64.deb">blockwright_0.1.1-1_ubuntu26.10_amd64.deb</a></li>
</ul>
<p>Each <code>.deb</code> is for the release named in it only. Both programs go on the <code>PATH</code>.</p>
<p class="how"><a href="manual/01-install.md#debian-and-ubuntu">Installing on Debian and Ubuntu</a></p>
</section>

<section class="dl" id="dl-fedora">
<h3>Fedora 45</h3>
<p><a href="https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-1.fc45.x86_64.rpm">blockwright-0.1.1-1.fc45.x86_64.rpm</a></p>
<p>Both programs go on the <code>PATH</code>.</p>
<p class="how"><a href="manual/01-install.md#fedora">Installing on Fedora</a></p>
</section>

<section class="dl" id="dl-arch">
<h3>Arch Linux</h3>
<p><a href="https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/PKGBUILD">PKGBUILD</a></p>
<p>Built with <code>makepkg -si</code>. Both programs go on the <code>PATH</code>.</p>
<p class="how"><a href="manual/01-install.md#arch-linux">Installing on Arch Linux</a></p>
</section>

<section class="dl" id="dl-freebsd">
<h3>FreeBSD 14</h3>
<p><a href="https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-freebsd-port.tar.gz">blockwright-0.1.1-freebsd-port.tar.gz</a></p>
<p>A port to build. Both programs go on the <code>PATH</code>.</p>
<p class="how"><a href="manual/01-install.md#freebsd">Installing on FreeBSD</a></p>
</section>

<section class="dl" id="dl-source">
<h3>Source</h3>
<p><a href="https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1.tar.gz">blockwright-0.1.1.tar.gz</a></p>
<p>Needs a C++20 compiler, CMake 3.24 or newer, Qt 6.7 or newer (Core, Gui, Widgets, Concurrent and Svg), libzip 1.7 or newer and zstd.</p>
<p class="how"><a href="manual/01-install.md#building-from-source">Building from source</a></p>
<p>The source is on <a href="https://git.pumpin.online/funkpower/blockwright">the forge</a>, under the GPL version 3 or later. Older releases, 0.1.0 among them, are on its <a href="https://git.pumpin.online/funkpower/blockwright/releases">releases page</a>.</p>
</section>

</div>

<div class="rule" aria-hidden="true"><span>█▓▒░</span>░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░</div>

<h2 id="samples"><span class="visually-hidden">Samples</span><span aria-hidden="true">ls samples/</span></h2>

<p><a href="samples/index.md">All samples</a></p>

<div class="carousel">
<figure><a href="samples/index.md#harbour-at-night"><img src="samples/gallery/01-layers-showcase/harbour-at-night.ans" alt="Harbour at night, the finished piece"></a><figcaption><a href="samples/index.md#harbour-at-night">Harbour at night</a></figcaption></figure>
<figure><a href="samples/index.md#ddos-king"><img src="samples/gallery/02-ddos-king/ddos-king.ans" alt="DDOS KING, the finished piece"></a><figcaption><a href="samples/index.md#ddos-king">DDOS KING</a></figcaption></figure>
<figure><a href="samples/index.md#still-life"><img src="samples/gallery/03-still-life/still-life.ans" alt="Still life, the finished piece"></a><figcaption><a href="samples/index.md#still-life">Still life</a></figcaption></figure>
<figure><a href="samples/index.md#ridges-at-dusk"><img src="samples/gallery/04-generator-ridges/ridges-at-dusk.ans" alt="Ridges at dusk, the finished piece"></a><figcaption><a href="samples/index.md#ridges-at-dusk">Ridges at dusk</a></figcaption></figure>
<figure><a href="samples/index.md#traveller"><img src="samples/gallery/05-character/traveller.ans" alt="Traveller, the finished piece"></a><figcaption><a href="samples/index.md#traveller">Traveller</a></figcaption></figure>
<figure><a href="samples/index.md#blockwright-logo"><img src="samples/gallery/06-blockwright-logo/blockwright-logo.ans" alt="Blockwright logo, the finished piece"></a><figcaption><a href="samples/index.md#blockwright-logo">Blockwright logo</a></figcaption></figure>
<figure><a href="samples/index.md#battlestation"><img src="samples/gallery/07-battlestation/battlestation.ans" alt="Battlestation, the finished piece"></a><figcaption><a href="samples/index.md#battlestation">Battlestation</a></figcaption></figure>
<figure><a href="samples/index.md#this-is-your-brain-on-irc"><img src="samples/gallery/08-brain-on-irc/this-is-your-brain-on-irc.ans" alt="This Is Your Brain on IRC, the finished piece"></a><figcaption><a href="samples/index.md#this-is-your-brain-on-irc">This Is Your Brain on IRC</a></figcaption></figure>
<figure><a href="samples/index.md#wtc-0903"><img src="samples/gallery/09-wtc-0903/wtc-0903.ans" alt="wtc-0903, the finished piece"></a><figcaption><a href="samples/index.md#wtc-0903">wtc-0903</a></figcaption></figure>
</div>

<div class="rule" aria-hidden="true"><span>█▓▒░</span>░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░</div>

<div class="docs">
<section>
<h2 id="tutorials"><span class="visually-hidden">Tutorials</span><span aria-hidden="true">ls tutorials/</span></h2>
<p><a href="tutorials/index.md">All tutorials</a></p>
<!-- list: tutorials -->
</section>
<section>
<h2 id="manual"><span class="visually-hidden">Manual</span><span aria-hidden="true">man blockwright</span></h2>
<p><a href="manual/index.md">Every tool, menu, file format and command</a>.</p>
<!-- list: manual -->
</section>
</div>
