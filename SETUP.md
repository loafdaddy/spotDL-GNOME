# spotDL setup

<p align="center">
  <img src="data/brand/spotdl-mark.svg" alt="spotDL mark" width="72"/>
</p>

Dummy-proof install. Do the steps **in order**.

**Runtime is Flatpak.** You do not need a Python venv to use the app. Contributors: [CONTRIBUTING.md](CONTRIBUTING.md).

Overview: [README.md](README.md) · Configuration: [docs/CONFIGURATION.md](docs/CONFIGURATION.md) · Releases: [docs/RELEASES.md](docs/RELEASES.md).

---

## Checklist

| # | Step | You will have |
|---|------|----------------|
| 0 | Prerequisites | Flatpak + Flathub |
| 1 | Install | App on your system |
| 2 | First run | Welcome dialog + Preferences |
| 3 | Download | A tagged file in your music folder |
| 4 | Play | Files open in your music library (optional) |

---

## 0. Prerequisites

- [ ] Linux desktop (Wayland or X11)
- [ ] Flatpak installed
- [ ] Network access to pull the GNOME runtime from Flathub (first install only)

```bash
# Fedora
sudo dnf install -y flatpak

# Debian / Ubuntu
sudo apt install -y flatpak

flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

---

## 1. Install

### Option A — prebuilt bundle (recommended)

1. Download `io.github.loafdaddy.SpotdlGnome.flatpak` from the
   [latest release](https://github.com/loafdaddy/spotDL-GNOME/releases/latest).
2. Install and run:

```bash
flatpak install --user ./io.github.loafdaddy.SpotdlGnome.flatpak
flatpak run io.github.loafdaddy.SpotdlGnome
```

This only pulls the shared GNOME **runtime** — no SDK and no local compile.

### Option B — build the Flatpak from source

```bash
sudo dnf install -y flatpak flatpak-builder   # or apt equivalent
git clone https://github.com/loafdaddy/spotDL-GNOME.git
cd spotDL-GNOME
./packaging/flatpak/build.sh
flatpak run io.github.loafdaddy.SpotdlGnome
```

Details: [packaging/flatpak/README.md](packaging/flatpak/README.md).

### Option C — GUI from a Python venv (developers)

```bash
git clone https://github.com/loafdaddy/spotDL-GNOME.git
cd spotDL-GNOME
sudo dnf install python3-gobject gtk4 libadwaita   # Fedora example
python -m venv --system-site-packages .venv && source .venv/bin/activate
pip install -e ".[gui]"
python -m spotdl.gui
```

---

## 2. First run

On first launch you should see:

1. The **spotDL.** home status page (green download-clock mark)
2. A **Welcome** dialog asking you to open Preferences

Set at least:

| Preference | Suggestion |
|------------|------------|
| Output directory | Your Music folder (or a dedicated Downloads/Music path) |
| Format | `mp3` for compatibility, `flac` / `opus` for quality |
| Folder template | Keep the default album-artist layout unless you know you want another |

Full reference: [docs/CONFIGURATION.md](docs/CONFIGURATION.md).

---

## 3. Smoke test

1. Copy a Spotify **track** URL from the Spotify app or website.
2. Paste it into the search field.
3. Press **Download**.
4. Wait for the loading phase, then the progress row.
5. When done, use the toast action or History sidebar to open the file location.

If a song fails, read the inline reason and use **Retry**. Backup audio sources are tried automatically.

---

## 4. Play your downloads

spotDL does not include a player. Point your music library or player at the same folder you chose in Preferences.

---

## Updating

**Bundle install**

1. Download the newer `.flatpak` from Releases.
2. `flatpak install --user ./io.github.loafdaddy.SpotdlGnome.flatpak`

**Source Flatpak**

```bash
git pull
./packaging/flatpak/build.sh
```

---

## Troubleshooting

| Symptom | What to try |
|---------|-------------|
| Flatpak cannot find runtime | Ensure Flathub remote is added (step 0) |
| First download feels stuck | Wait — the loading screen covers engine startup |
| Song fails repeatedly | Check the error line; try another track; confirm network |
| Icon missing in from-source runs | Expected if the desktop icon is not installed; Flatpak shows the brand mark |
| Permission / folder errors | Pick a writable output directory in Preferences |

More CLI-oriented notes: [docs/troubleshooting.md](docs/troubleshooting.md) · [docs/FAQ.md](docs/FAQ.md).

---

## Next

- Configuration details → [docs/CONFIGURATION.md](docs/CONFIGURATION.md)
- Architecture → [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- Contribute → [CONTRIBUTING.md](CONTRIBUTING.md)
