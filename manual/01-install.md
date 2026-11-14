Title: Installing Blockwright
Checked: Blockwright 0.1.1 (609a15c)

# Installing Blockwright

Blockwright 0.1.1 was released on 14 November 2026. Its files are on the [release page](https://git.pumpin.online/funkpower/blockwright/releases/tag/v0.1.1), with the release notes. Every package installs two programs: `blockwright`, the editor, and `blockwright-cli`, the command line, which renders, converts and checks pieces without a display.

This page has a section per system: what the file needs, the commands that install it, and how to check that it worked. Then come checksums, building from source and uninstalling.

## Downloads

| System | File | Checksum |
|---|---|---|
| Linux, x86-64, any distribution with glibc 2.36 or newer | [blockwright-0.1.1-x86_64.AppImage](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-x86_64.AppImage) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-x86_64.AppImage.sha256) |
| Debian 13 | [blockwright_0.1.1-1_debian13_amd64.deb](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright_0.1.1-1_debian13_amd64.deb) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright_0.1.1-1_debian13_amd64.deb.sha256) |
| Debian testing (forky) | [blockwright_0.1.1-1_debian-testing_amd64.deb](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright_0.1.1-1_debian-testing_amd64.deb) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright_0.1.1-1_debian-testing_amd64.deb.sha256) |
| Ubuntu 26.04 | [blockwright_0.1.1-1_ubuntu26.04_amd64.deb](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright_0.1.1-1_ubuntu26.04_amd64.deb) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright_0.1.1-1_ubuntu26.04_amd64.deb.sha256) |
| Ubuntu 26.10 | [blockwright_0.1.1-1_ubuntu26.10_amd64.deb](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright_0.1.1-1_ubuntu26.10_amd64.deb) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright_0.1.1-1_ubuntu26.10_amd64.deb.sha256) |
| Fedora 45 | [blockwright-0.1.1-1.fc45.x86_64.rpm](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-1.fc45.x86_64.rpm) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-1.fc45.x86_64.rpm.sha256) |
| Arch Linux | [PKGBUILD](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/PKGBUILD) | none; makepkg checks the source |
| FreeBSD 14 | [blockwright-0.1.1-freebsd-port.tar.gz](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-freebsd-port.tar.gz) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-freebsd-port.tar.gz.sha256) |
| macOS 12 (Monterey) or later, Apple Silicon and Intel | [Blockwright-0.1.1.dmg](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/Blockwright-0.1.1.dmg) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/Blockwright-0.1.1.dmg.sha256) |
| Windows 10 or later, x86-64 | [blockwright-0.1.1-x86_64.msi](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-x86_64.msi) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-x86_64.msi.sha256) |
| Source | [blockwright-0.1.1.tar.gz](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1.tar.gz) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1.tar.gz.sha256) |

## Checking the install

Every section below ends by running `blockwright-cli --version`. Its first line names the version and the commit it was built from:

```text
blockwright-cli 0.1.1 (bd67fae)
```

The logo and the notices for the bundled fonts follow it.

## Linux: AppImage

One file that runs on any x86-64 Linux with glibc 2.36 or newer: Debian 12, Ubuntu 24.04 and later releases. It carries its own Qt, so it also runs where the distribution's Qt is too old for the packages below.

It needs a `fusermount3` or `fusermount` command on the `PATH`, from fuse3 or the older FUSE 2 package. Without either, set `APPIMAGE_EXTRACT_AND_RUN=1`, and the AppImage runs without FUSE.

Make it executable and run it:

```sh
chmod +x blockwright-0.1.1-x86_64.AppImage
./blockwright-0.1.1-x86_64.AppImage
```

Without FUSE:

```sh
APPIMAGE_EXTRACT_AND_RUN=1 ./blockwright-0.1.1-x86_64.AppImage
```

The same file is `blockwright-cli` when `--cli` comes first, or when it runs through a symlink named `blockwright-cli`:

```sh
./blockwright-0.1.1-x86_64.AppImage --cli --version
ln -s "$PWD/blockwright-0.1.1-x86_64.AppImage" ~/.local/bin/blockwright-cli
blockwright-cli --version
```

The symlink works from any folder on the `PATH`; `~/.local/bin` is one many distributions put there.

## Debian and Ubuntu

There is a `.deb` for each of these releases, and each one is for the release named in it only:

| Release | File |
|---|---|
| Debian 13 (trixie) | `blockwright_0.1.1-1_debian13_amd64.deb` |
| Debian testing (forky) | `blockwright_0.1.1-1_debian-testing_amd64.deb` |
| Ubuntu 26.04 | `blockwright_0.1.1-1_ubuntu26.04_amd64.deb` |
| Ubuntu 26.10 | `blockwright_0.1.1-1_ubuntu26.10_amd64.deb` |

Install the file for your release with apt, which fetches the libraries it depends on:

```sh
sudo apt install ./blockwright_0.1.1-1_debian13_amd64.deb
blockwright-cli --version
```

The `./` matters: without it apt looks for a package of that name in its archives. Debian 12 and Ubuntu 24.04 have a Qt older than 6.7, which Blockwright needs; use the AppImage there.

## Fedora

The `.rpm` is for Fedora 45:

```sh
sudo dnf install ./blockwright-0.1.1-1.fc45.x86_64.rpm
blockwright-cli --version
```

## Arch Linux

An AUR package is coming, but it isn't up yet. Until it is, build the package from the `PKGBUILD` attached to the release. Run makepkg as a user who isn't root; it needs the `base-devel` group installed, and asks for your password through sudo when it installs.

```sh
mkdir blockwright && cd blockwright
curl -LO https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/PKGBUILD
makepkg -si
blockwright-cli --version
```

makepkg downloads the source tarball from the release, checks it against the checksum in the `PKGBUILD`, builds it and runs the tests. `-s` installs the dependencies from the Arch repositories first, and `-i` installs the package. The `PKGBUILD` has no `.sha256` of its own; it carries the tarball's.

## FreeBSD

The port tarball holds a port for FreeBSD 14. It builds against the packaged Qt 6 and needs the ports framework in `/usr/ports`. If you don't have a ports tree, one way to get it is with git (`pkg install git`):

```sh
git clone --depth 1 https://git.FreeBSD.org/ports.git /usr/ports
```

Then, as root, install the build dependencies from packages, fetch the port, unpack it and build it:

```sh
pkg install cmake ninja qt6-base qt6-svg libzip zstd
fetch https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/blockwright-0.1.1-freebsd-port.tar.gz
tar xzf blockwright-0.1.1-freebsd-port.tar.gz
cd blockwright
make install clean
blockwright-cli --version
```

`make install` downloads the source tarball from the release and checks it against the port's `distinfo`. The programs go in `/usr/local/bin`.

## macOS

`Blockwright-0.1.1.dmg` holds one app that runs natively on Apple Silicon and Intel Macs, on macOS 12 (Monterey) or later. Open the dmg and drag Blockwright to Applications.

### Homebrew

Or install it from the Homebrew tap. Use the cask's full name, `funkpower/tap/blockwright`: Homebrew 7 refuses the short name for a cask from a tap it doesn't trust.

```sh
brew tap funkpower/tap https://git.pumpin.online/funkpower/homebrew-tap.git
brew install --cask funkpower/tap/blockwright
```

The cask installs the app in Applications and puts `blockwright-cli` on the `PATH`.

### Quarantine

The app is signed ad hoc, not with an Apple Developer ID, and it isn't notarized, so macOS blocks it the first time you open it. That holds for the dmg and for Homebrew alike. Before you open it, run this in Terminal:

```sh
xattr -dr com.apple.quarantine /Applications/Blockwright.app
```

That lets both the app and `blockwright-cli` run. If you only need the app, you can instead try to open it once, then go to **System Settings > Privacy & Security** and click **Open Anyway**; that leaves `blockwright-cli` blocked.

The command-line tool is inside the app, at `/Applications/Blockwright.app/Contents/MacOS/blockwright-cli`. From the dmg:

```sh
/Applications/Blockwright.app/Contents/MacOS/blockwright-cli --version
```

From Homebrew, `blockwright-cli --version`.

## Windows

`blockwright-0.1.1-x86_64.msi` is for 64-bit Windows 10 or later. The installer isn't signed, so Windows warns before it runs it:

1. The browser may warn that the file isn't commonly downloaded. Choose to keep it.
2. Open the MSI. Microsoft Defender SmartScreen shows a blue window, **Windows protected your PC**, saying it prevented an unrecognised app from starting. Click **More info**: the window names the file and **Unknown publisher**, and shows a **Run anyway** button. Click it.
3. User Account Control asks whether to let an app from an unknown publisher make changes to your device. Click **Yes**. The installer installs for every user on the PC, so it needs an administrator's approval.

The installer has no choices to make. It installs Blockwright into `C:\Program Files\Blockwright` and puts **Blockwright** in the Start menu. Installing a later MSI replaces the earlier version; an older MSI over a newer install is refused with "A newer version of Blockwright is already installed."

The programs are in `C:\Program Files\Blockwright\bin`. The installer doesn't put that folder on the `PATH`, so give the full path, in PowerShell:

```powershell
& "C:\Program Files\Blockwright\bin\blockwright-cli.exe" --version
```

## Building from source

Building needs a C++20 compiler, CMake 3.24 or later, Ninja, Qt 6.7 or later (Core, Gui, Widgets, Concurrent and Svg), libzip and zstd. Python 3 is optional at run time, for generator layers and scene scripts.

```sh
sha256sum -c blockwright-0.1.1.tar.gz.sha256
tar xzf blockwright-0.1.1.tar.gz
cd blockwright-0.1.1
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
cmake --build build
QT_QPA_PLATFORM=offscreen ctest --test-dir build
sudo cmake --install build
blockwright-cli --version
```

The tests need no display. They use an installed Catch2 3, and download one when there is none; `-DBUILD_TESTING=OFF` builds without them. `cmake --install` puts the programs in `/usr/local/bin` unless `-DCMAKE_INSTALL_PREFIX` names another prefix.

The package names of the dependencies differ from system to system. The [README](https://git.pumpin.online/funkpower/blockwright/src/tag/v0.1.1/README.md) lists what the build needs, and [packaging/README.md](https://git.pumpin.online/funkpower/blockwright/src/tag/v0.1.1/packaging/README.md), also in the source tarball, has the steps for each system's package. The Windows MSI is cross-built on Linux, as [packaging/windows/README.md](https://git.pumpin.online/funkpower/blockwright/src/tag/v0.1.1/packaging/windows/README.md) describes.

## Checksums

Each file but the `PKGBUILD` has a `.sha256` file beside it on the release page, holding its SHA-256 checksum and its name. Download both into one folder and check the file against it. On Linux and FreeBSD:

```sh
sha256sum -c blockwright-0.1.1-x86_64.AppImage.sha256
```

It prints the file's name and `OK`, or `FAILED` when the file doesn't match. On macOS:

```sh
shasum -a 256 -c Blockwright-0.1.1.dmg.sha256
```

On Windows, in PowerShell, `Get-FileHash` prints the checksum in capitals; compare it with the one in the `.sha256` file:

```powershell
Get-FileHash .\blockwright-0.1.1-x86_64.msi
Get-Content .\blockwright-0.1.1-x86_64.msi.sha256
```

## Uninstalling

| Installed with | To remove it |
|---|---|
| AppImage | Delete the AppImage, and the `blockwright-cli` symlink if you made one |
| Debian or Ubuntu `.deb` | `sudo apt remove blockwright` |
| Fedora `.rpm` | `sudo dnf remove blockwright` |
| Arch `PKGBUILD` | `sudo pacman -R blockwright` |
| FreeBSD port | `pkg delete blockwright`, as root |
| macOS dmg | Drag Blockwright from Applications to the Bin |
| Homebrew | `brew uninstall --cask funkpower/tap/blockwright`, then `brew untap funkpower/tap` if nothing else comes from the tap |
| Windows MSI | **Settings > Apps** (**Installed apps** on Windows 11, **Apps & features** on Windows 10), then **Blockwright** and **Uninstall** |
| From source | Remove the files `cmake --install` listed in `build/install_manifest.txt`: `xargs sudo rm -f < build/install_manifest.txt` |

Uninstalling leaves your pieces, projects, settings and library where they are.
