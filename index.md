Title: Blockwright

<div class="hero">
<div class="hero-text">
<h1 class="wordmark"><span class="shade" aria-hidden="true">░▒▓█</span>BLOCKWRIGHT<span class="shade" aria-hidden="true">█▓▒░</span></h1>
<p class="tagline">An editor for ANSI and IRC art.</p>
<p>Half-block pixels, shading along colour ramps, lighting, layers, and a live byte meter so every line fits on IRC. It opens and saves <code>.ans</code> with SAUCE, XBIN and BIN, and exports IRC text and Micron pages.</p>
<div class="term">
<p><span class="ps1" aria-hidden="true">$ </span>blockwright --version</p>
<p class="out">Blockwright {{version}}</p>
<p class="out dim">Linux · FreeBSD · macOS · Windows</p>
<p aria-hidden="true"><span class="ps1">$ </span><span class="cursor"></span></p>
</div>
<p class="actions"><a class="button" href="#download">Download {{version}}</a> <a class="button" href="docs/index.md">Read the docs</a></p>
</div>
<figure class="hero-art">
<img src="samples/01-what-ansi-art-is/final.ans" alt="0xCAFE: a coffee mug in blue, magenta and white with grey steam rising, the word 0xCAFE in white block letters across its blue band, on a saucer, with a pink arrow pointing at it from the top right corner.">
<figcaption><cite>0xCAFE</cite> by funkpower, 80 × 40, from <a href="tutorials/01-what-ansi-art-is.md">tutorial 1</a>.</figcaption>
</figure>
</div>

<div class="rule" aria-hidden="true"><span>█▓▒░</span>░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░</div>

<h2 id="download"><span class="visually-hidden">Download</span><span aria-hidden="true"><span class="ps1">$ </span>ls releases/v{{version}}/</span></h2>

<p class="lead">Blockwright {{version}}. Every package installs the editor, <code>blockwright</code>, and the command-line tool, <code>blockwright-cli</code>. Each file but the <code>PKGBUILD</code> has a <code>.sha256</code> file beside it with its checksum. The <a class="pending" href="manual/01-install.md">install guide</a> has the full steps for each system, and the <a href="{{release}}">release page</a> lists every file.</p>

<div class="downloads">

<section class="dl" aria-labelledby="dl-appimage">
<h3 id="dl-appimage">Linux · AppImage</h3>
<p><a href="{{download}}/{{appimage}}">{{appimage}}</a></p>
<p>Any x86-64 distribution with glibc 2.36 or newer. Make it executable and run it:</p>
<pre><code>chmod +x {{appimage}}
./{{appimage}}</code></pre>
<p>It needs <code>fusermount3</code> or <code>fusermount</code> on the <code>PATH</code>. Without either, run it with <code>APPIMAGE_EXTRACT_AND_RUN=1</code>:</p>
<pre><code>APPIMAGE_EXTRACT_AND_RUN=1 ./{{appimage}}</code></pre>
</section>

<section class="dl" aria-labelledby="dl-deb">
<h3 id="dl-deb">Debian and Ubuntu</h3>
<ul class="files">
<li>Debian 13: <a href="{{download}}/{{deb-debian13}}">{{deb-debian13}}</a></li>
<li>Debian testing: <a href="{{download}}/{{deb-debian-testing}}">{{deb-debian-testing}}</a></li>
<li>Ubuntu 26.04: <a href="{{download}}/{{deb-ubuntu2604}}">{{deb-ubuntu2604}}</a></li>
<li>Ubuntu 26.10: <a href="{{download}}/{{deb-ubuntu2610}}">{{deb-ubuntu2610}}</a></li>
</ul>
<p>Each <code>.deb</code> is for its own release only. Install the one for yours:</p>
<pre><code>sudo apt install ./{{deb-debian13}}</code></pre>
</section>

<section class="dl" aria-labelledby="dl-fedora">
<h3 id="dl-fedora">Fedora 45</h3>
<p><a href="{{download}}/{{rpm-fedora45}}">{{rpm-fedora45}}</a></p>
<pre><code>sudo dnf install ./{{rpm-fedora45}}</code></pre>
</section>

<section class="dl" aria-labelledby="dl-arch">
<h3 id="dl-arch">Arch Linux</h3>
<p>The AUR package isn't up yet. Build the package from the release's <a href="{{download}}/{{pkgbuild}}">PKGBUILD</a>, as a user who isn't root:</p>
<pre><code>mkdir blockwright &amp;&amp; cd blockwright
curl -LO {{download}}/{{pkgbuild}}
makepkg -si</code></pre>
</section>

<section class="dl" aria-labelledby="dl-freebsd">
<h3 id="dl-freebsd">FreeBSD 14</h3>
<p><a href="{{download}}/{{freebsd-port}}">{{freebsd-port}}</a></p>
<p>A port. It needs a ports tree in <code>/usr/ports</code>. As root, install the build dependencies, unpack the port and build it:</p>
<pre><code>pkg install cmake ninja qt6-base qt6-svg libzip zstd
tar xzf {{freebsd-port}}
cd blockwright
make install clean</code></pre>
</section>

<section class="dl" aria-labelledby="dl-macos">
<h3 id="dl-macos">macOS 12 or later</h3>
<p><a href="{{download}}/{{dmg}}">{{dmg}}</a></p>
<p>Apple Silicon and Intel. Open the dmg and drag Blockwright to Applications, or install it with Homebrew:</p>
<pre><code>brew tap funkpower/tap {{forge}}/funkpower/homebrew-tap.git
brew install --cask funkpower/tap/blockwright</code></pre>
<p>The app is signed ad hoc and isn't notarized, so macOS blocks it the first time. Before you open it, run:</p>
<pre><code>xattr -dr com.apple.quarantine /Applications/Blockwright.app</code></pre>
</section>

<section class="dl" aria-labelledby="dl-windows">
<h3 id="dl-windows">Windows 10 or later</h3>
<p><a href="{{download}}/{{msi}}">{{msi}}</a></p>
<p>x86-64. Run the MSI: it installs Blockwright in Program Files with a Start menu shortcut.</p>
<p>The MSI isn't signed, so Microsoft Defender SmartScreen stops it with "Windows protected your PC" and gives the publisher as unknown. Click <b>More info</b>, then <b>Run anyway</b>. Windows then asks for administrator rights for an installer from an unknown publisher.</p>
</section>

<section class="dl" aria-labelledby="dl-source">
<h3 id="dl-source">Source</h3>
<p><a href="{{download}}/{{source}}">{{source}}</a></p>
<p>Needs a C++20 compiler, CMake, Ninja and Qt 6.7 or newer. <code>packaging/README.md</code> in the tarball has the steps for each system. The code is on <a href="{{repo}}">the forge</a>, under the GPL, version 3 or later.</p>
</section>

</div>

<div class="rule" aria-hidden="true"><span>█▓▒░</span>░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░</div>

<h2 id="docs"><span class="visually-hidden">Documentation</span><span aria-hidden="true"><span class="ps1">$ </span>man blockwright</span></h2>

<ul class="docs-links">
<li><a href="tutorials/index.md">Tutorials</a> <span>From nothing to a finished piece on IRC, one skill at a time.</span></li>
<li><a href="manual/index.md">Manual</a> <span>Every tool, menu, file format and command.</span></li>
<li><a href="docs/index.md">Docs</a> <span>Both, page by page.</span></li>
</ul>
