Title: Installing Blockwright
Checked: Blockwright 0.1.2 (fb62a10)

# Installing Blockwright

Blockwright 0.1.2 was released on 19 November 2026. Its files and release notes are on the [release page](https://git.pumpin.online/funkpower/blockwright/releases/tag/v0.1.2). Every package installs two programs: `blockwright`, the editor, and `blockwright-cli`, which renders, converts and checks pieces without a display.

## Downloads

| System | File | Checksum |
|---|---|---|
| Linux, x86-64, any distribution with glibc 2.36 or newer | [blockwright-0.1.2-x86_64.AppImage](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-x86_64.AppImage) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-x86_64.AppImage.sha256) |
| Linux, x86-64, Flatpak | [blockwright-0.1.2-x86_64.flatpak](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-x86_64.flatpak) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-x86_64.flatpak.sha256) |
| Debian 13 | [blockwright_0.1.2-1_debian13_amd64.deb](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright_0.1.2-1_debian13_amd64.deb) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright_0.1.2-1_debian13_amd64.deb.sha256) |
| Ubuntu 26.04 | [blockwright_0.1.2-1_ubuntu26.04_amd64.deb](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright_0.1.2-1_ubuntu26.04_amd64.deb) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright_0.1.2-1_ubuntu26.04_amd64.deb.sha256) |
| Fedora 44 | [blockwright-0.1.2-1.fc44.x86_64.rpm](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-1.fc44.x86_64.rpm) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-1.fc44.x86_64.rpm.sha256) |
| Fedora 45 | [blockwright-0.1.2-1.fc45.x86_64.rpm](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-1.fc45.x86_64.rpm) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-1.fc45.x86_64.rpm.sha256) |
| Arch Linux | [PKGBUILD](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/PKGBUILD) | none; makepkg checks the source |
| FreeBSD 14 | [blockwright-0.1.2-freebsd-port.tar.gz](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-freebsd-port.tar.gz) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-freebsd-port.tar.gz.sha256) |
| macOS 12 (Monterey) or later, Apple Silicon and Intel | [Blockwright-0.1.1.dmg](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/Blockwright-0.1.1.dmg) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.1/Blockwright-0.1.1.dmg.sha256) |
| Windows 10 or later, x86-64 | [blockwright-0.1.2-x86_64.msi](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-x86_64.msi) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-x86_64.msi.sha256) |
| Source | [blockwright-0.1.2.tar.gz](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2.tar.gz) | [.sha256](https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2.tar.gz.sha256) |

## Checking the install

`blockwright-cli --version` ends each section. Its first line names the version and commit:

```text
blockwright-cli 0.1.2 (fb62a10)
```

The `.deb` and `.rpm` packages, the Arch package, the FreeBSD port, a source install and the Homebrew cask put `blockwright-cli` on the `PATH`. The others don't:

- The Flatpak runs it as `flatpak run --command=blockwright-cli online.pumpin.funkpower.blockwright`.
- The AppImage runs as `blockwright-cli` with `--cli` first, or through a symlink named `blockwright-cli` (a short script where AppImageLauncher is installed).
- The dmg keeps it inside the app bundle, and the Windows installer leaves its folder off the `PATH`. Their sections give the full path.

## Linux: AppImage

One file for any x86-64 Linux with glibc 2.36 or newer: Debian 12, Ubuntu 24.04 and later. It carries its own Qt.

It needs `fusermount3` or `fusermount` on the `PATH`, from fuse3 or FUSE 2. Without either, set `APPIMAGE_EXTRACT_AND_RUN=1`.

Run it:

```sh
chmod +x blockwright-0.1.2-x86_64.AppImage
./blockwright-0.1.2-x86_64.AppImage
```

Without FUSE:

```sh
APPIMAGE_EXTRACT_AND_RUN=1 ./blockwright-0.1.2-x86_64.AppImage
```

For `blockwright-cli`, put `--cli` first or use a symlink:

```sh
./blockwright-0.1.2-x86_64.AppImage --cli --version
mkdir -p ~/.local/bin
ln -s "$PWD/blockwright-0.1.2-x86_64.AppImage" ~/.local/bin/blockwright-cli
blockwright-cli --version
```

Any folder on the `PATH` works. A new `~/.local/bin` may join the `PATH` only at the next login.

Under AppImageLauncher (an `appimage-type2` entry in `/proc/sys/fs/binfmt_misc/`) the symlink starts the editor. Remove it (`rm ~/.local/bin/blockwright-cli`), or the script below is written over the AppImage. Then make `~/.local/bin/blockwright-cli` a script that puts `--cli` first, with the AppImage's full path for `/path/to`.

```sh
#!/bin/sh
exec /path/to/blockwright-0.1.2-x86_64.AppImage --cli "$@"
```

Then:

```sh
chmod +x ~/.local/bin/blockwright-cli
blockwright-cli --version
```

The first line is now `blockwright-cli 0.1.2 (fb62a10)`.

## Linux: Flatpak

One bundle for x86-64 Linux with Flatpak installed. Install it for your user; Flatpak fetches the KDE runtime it needs from Flathub:

```sh
sha256sum -c blockwright-0.1.2-x86_64.flatpak.sha256
flatpak install --user blockwright-0.1.2-x86_64.flatpak
flatpak run online.pumpin.funkpower.blockwright
flatpak run --command=blockwright-cli online.pumpin.funkpower.blockwright --version
```

The second `flatpak run` is `blockwright-cli`; it isn't put on the `PATH`.

The sandbox can read and write your home directory. For files elsewhere (another disk under `/mnt`, say), grant the path:

```sh
flatpak override --user --filesystem=/path/to/folder online.pumpin.funkpower.blockwright
```

The Library and the settings are in `~/.var/app/online.pumpin.funkpower.blockwright/`, apart from a native install's. Generators and scene scripts run with the runtime's Python 3, so Python modules installed for the system's Python aren't there unless they are in your home directory and on `PYTHONPATH`:

```sh
flatpak override --user --env=PYTHONPATH=/path/to/modules online.pumpin.funkpower.blockwright
```

## Debian and Ubuntu

On Ubuntu 26.04, install from the PPA. It covers Ubuntu 26.04, and updates come with the system's updates:

```sh
sudo add-apt-repository ppa:funkpower/blockwright
sudo apt update
sudo apt install blockwright
blockwright-cli --version
```

Otherwise, or on Debian, use a `.deb`. Each `.deb` is for one release. Version 0.1.2 has no `.deb` for Debian testing or Ubuntu 26.10:

| Release | File |
|---|---|
| Debian 13 (trixie) | `blockwright_0.1.2-1_debian13_amd64.deb` |
| Ubuntu 26.04 | `blockwright_0.1.2-1_ubuntu26.04_amd64.deb` |

Install yours with apt, which fetches its libraries:

```sh
sudo apt install ./blockwright_0.1.2-1_debian13_amd64.deb
blockwright-cli --version
```

Keep the `./`, or apt looks in its archives. Debian 12 and Ubuntu 24.04 have a Qt older than the 6.7 Blockwright needs; use the AppImage there.

## Fedora

An `.rpm` is built for Fedora 44 and for Fedora 45, each for its release only (`fc44` or `fc45` in the file name):

```sh
sudo dnf install ./blockwright-0.1.2-1.fc45.x86_64.rpm
blockwright-cli --version
```

## Arch Linux

There is no AUR package yet. Build from the release's `PKGBUILD`, as a user who isn't root, with `base-devel` installed. makepkg asks for your sudo password to install.

```sh
mkdir blockwright && cd blockwright
curl -LO https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/PKGBUILD
makepkg -si
blockwright-cli --version
```

makepkg downloads the source, checks its checksum, builds and runs the tests. `-s` installs the dependencies; `-i` installs the package.

## FreeBSD

The port is for FreeBSD 14 and needs the ports framework in `/usr/ports`. Without one, get it with git (`pkg install git`):

```sh
git clone --depth 1 https://git.FreeBSD.org/ports.git /usr/ports
```

Then, as root, install the build dependencies, fetch the port, unpack it and build it:

```sh
pkg install cmake ninja qt6-base qt6-svg libzip zstd
fetch https://git.pumpin.online/funkpower/blockwright/releases/download/v0.1.2/blockwright-0.1.2-freebsd-port.tar.gz
tar xzf blockwright-0.1.2-freebsd-port.tar.gz
cd blockwright
make install clean
blockwright-cli --version
```

`make install` downloads and checks the source. The programs go in `/usr/local/bin`.

## macOS

The newest macOS build is [0.1.1](https://git.pumpin.online/funkpower/blockwright/releases/tag/v0.1.1); 0.1.2 has no dmg, and the Homebrew cask installs 0.1.1 too. `Blockwright-0.1.1.dmg` holds one app for Apple Silicon and Intel Macs, on macOS 12 (Monterey) or later. Open the dmg and drag Blockwright to Applications.

### Homebrew

Or install the cask by its full name, `funkpower/tap/blockwright`; Homebrew 7 refuses the short name from an untrusted tap.

```sh
brew tap funkpower/tap https://git.pumpin.online/funkpower/homebrew-tap.git
brew install --cask funkpower/tap/blockwright
```

The cask also links `blockwright-cli` onto the `PATH`.

### Quarantine

The app isn't notarized, so macOS blocks it the first time you open it, from the dmg or from Homebrew. Before you open it, run this in Terminal:

```sh
xattr -dr com.apple.quarantine /Applications/Blockwright.app
```

That lets the app and `blockwright-cli` run. For the app alone, try to open it once, then click **Open Anyway** in **System Settings > Privacy & Security**; `blockwright-cli` stays blocked.

From the dmg, `blockwright-cli` is inside the app:

```sh
/Applications/Blockwright.app/Contents/MacOS/blockwright-cli --version
```

From Homebrew, `blockwright-cli --version`.

## Windows

`blockwright-0.1.2-x86_64.msi` is for 64-bit Windows 10 or later. The installer isn't signed, so Windows warns before running it:

1. If the browser warns that the file isn't commonly downloaded, keep it.
2. Open the MSI. SmartScreen shows **Windows protected your PC**. Click **More info**, then **Run anyway**.
3. User Account Control asks to let an app from an unknown publisher make changes. Click **Yes**; the install is for every user.

The installer asks nothing. It installs into `C:\Program Files\Blockwright` and puts **Blockwright** in the Start menu.

A later MSI replaces the earlier version. An older MSI over a newer install is refused with "A newer version of Blockwright is already installed."

The programs are in `C:\Program Files\Blockwright\bin`, off the `PATH`. In PowerShell:

```powershell
& "C:\Program Files\Blockwright\bin\blockwright-cli.exe" --version
```

## Building from source

Building needs:

- a C++20 compiler, CMake 3.24 or later and Ninja;
- Qt 6.7 or later (Core, Gui, Widgets, Concurrent and Svg);
- libzip 1.7 or later and zstd.

Python 3 is optional at run time, for generator layers and scene scripts.

```sh
sha256sum -c blockwright-0.1.2.tar.gz.sha256
tar xzf blockwright-0.1.2.tar.gz
cd blockwright-0.1.2
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
cmake --build build
QT_QPA_PLATFORM=offscreen ctest --test-dir build
sudo cmake --install build
blockwright-cli --version
```

The tests use an installed Catch2 3 or download one; `-DBUILD_TESTING=OFF` skips them. `cmake --install` puts the programs in `/usr/local/bin` unless `-DCMAKE_INSTALL_PREFIX` names another prefix.

The [README](https://git.pumpin.online/funkpower/blockwright/src/tag/v0.1.2/README.md) lists what the build needs, and [packaging/README.md](https://git.pumpin.online/funkpower/blockwright/src/tag/v0.1.2/packaging/README.md), also in the tarball, has each system's package steps. The Windows MSI is cross-built on Linux, as [packaging/windows/README.md](https://git.pumpin.online/funkpower/blockwright/src/tag/v0.1.2/packaging/windows/README.md) describes.

## Checksums

Each file but the `PKGBUILD` has a `.sha256` beside it. Download both into one folder and check. On Linux and FreeBSD:

```sh
sha256sum -c blockwright-0.1.2-x86_64.AppImage.sha256
```

It prints the file's name and `OK`, or `FAILED`. On macOS:

```sh
shasum -a 256 -c Blockwright-0.1.1.dmg.sha256
```

On Windows, in PowerShell, compare `Get-FileHash`'s checksum (in capitals) with the `.sha256` file's:

```powershell
Get-FileHash .\blockwright-0.1.2-x86_64.msi
Get-Content .\blockwright-0.1.2-x86_64.msi.sha256
```

## Uninstalling

| Installed with | To remove it |
|---|---|
| AppImage | Delete the AppImage, and the `blockwright-cli` symlink or script if you made one |
| Flatpak | `flatpak uninstall online.pumpin.funkpower.blockwright`, then `flatpak uninstall --unused` for the runtime |
| Debian or Ubuntu `.deb` | `sudo apt remove blockwright` |
| Ubuntu PPA | `sudo apt remove blockwright`, then `sudo add-apt-repository --remove ppa:funkpower/blockwright` |
| Fedora `.rpm` | `sudo dnf remove blockwright` |
| Arch `PKGBUILD` | `sudo pacman -R blockwright` |
| FreeBSD port | `pkg delete blockwright`, as root |
| macOS dmg | Drag Blockwright from Applications to the Bin |
| Homebrew | `brew uninstall --cask funkpower/tap/blockwright`, then `brew untap funkpower/tap` if nothing else comes from the tap |
| Windows MSI | **Settings > Apps** (**Installed apps** on Windows 11, **Apps & features** on Windows 10), then **Blockwright** and **Uninstall** |
| From source | Remove the files `cmake --install` listed in `build/install_manifest.txt`: `xargs sudo rm -f < build/install_manifest.txt` |

Uninstalling leaves your pieces, projects, settings and library where they are. For the Flatpak, `flatpak uninstall --delete-data online.pumpin.funkpower.blockwright` also removes its settings and library in `~/.var/app/online.pumpin.funkpower.blockwright/`.
