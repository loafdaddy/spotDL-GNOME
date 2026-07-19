# spotDL.

<p align="center">
  <img src="data/brand/spotdl-lockup.svg" alt="spotDL." width="420"/>
</p>

<p align="center">
  <strong>A native GNOME desktop app for downloading music from Spotify</strong><br/>
  GTK4 · libadwaita · Flatpak · Linux
</p>

<p align="center">
  <a href="https://github.com/loafdaddy/spotDL-GNOME/releases/tag/v0.2.1">v0.2.1</a>
  ·
  <a href="docs/RELEASES.md">Release history</a>
  ·
  <a href="CONTRIBUTING.md">Contributing</a>
  ·
  <a href="https://github.com/loafdaddy/Cadence-Music">Play with Cadence</a>
</p>

spotDL finds songs from your Spotify tracks, albums, and playlists on YouTube and downloads them — complete with album art, lyrics, and metadata. This is a Linux fork that wraps the [spotDL](https://github.com/spotDL/spotify-downloader) engine in a native **GTK 4 / libadwaita** interface, packaged as a self-contained **Flatpak**.

This aims to feel like it ships with Fedora Workstation: Wayland-first, Flatpak-friendly, no Electron.

> Paste a Spotify link → download organised files → play them in [Cadence](https://github.com/loafdaddy/Cadence-Music).

<p align="center">
  <img src="screenshots/spotdl-home.png" alt="spotDL desktop app" width="720">
</p>

## AI disclaimer

Parts of this fork — including the GTK GUI, Flatpak packaging, docs, and branding — have been written or edited with **AI assistance** (for example Cursor and similar tools). That is intentional for an early project moving quickly. The upstream spotDL engine remains the work of the [spotDL project](https://github.com/spotDL/spotify-downloader) and its contributors.

**AI-assisted contributions are welcome.** Use Cursor, Copilot, ChatGPT, Claude, or any other assistant if it helps you. You remain responsible for what you submit: understand the change, keep pull requests focused, and verify what you can.

Full expectations: [CONTRIBUTING.md — AI-assisted contributions](CONTRIBUTING.md#ai-assisted-contributions).

## Try it

### Flatpak (recommended)

Grab the prebuilt `io.github.loafdaddy.SpotdlGnome.flatpak` from the
[latest release](https://github.com/loafdaddy/spotDL-GNOME/releases/latest) and install it.
This only pulls the GNOME **runtime** (shared with other Flatpak apps) — no SDK and no building.

```bash
# One-time: Flatpak + Flathub
sudo dnf install -y flatpak          # Debian/Ubuntu: sudo apt install -y flatpak
flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# Install the downloaded bundle
flatpak install --user ./io.github.loafdaddy.SpotdlGnome.flatpak
flatpak run io.github.loafdaddy.SpotdlGnome
```

### Build from source

```bash
sudo dnf install -y flatpak flatpak-builder
git clone https://github.com/loafdaddy/spotDL-GNOME.git
cd spotDL-GNOME
./packaging/flatpak/build.sh
flatpak run io.github.loafdaddy.SpotdlGnome
```

Details: [packaging/flatpak/README.md](packaging/flatpak/README.md).

### From source (GUI development)

```bash
git clone https://github.com/loafdaddy/spotDL-GNOME.git
cd spotDL-GNOME

# Requires system GTK 4 + libadwaita + PyGObject
python -m venv --system-site-packages .venv && source .venv/bin/activate
pip install -e ".[gui]"
python -m spotdl.gui
```

Full contributor workflow: [CONTRIBUTING.md](CONTRIBUTING.md).

## Play your downloads

spotDL downloads and tags files; it does not play them. For a native Linux music library that fits the same GNOME / Flatpak world, use **[Cadence](https://github.com/loafdaddy/Cadence-Music)** — point it at your Music folder (or wherever you save downloads) and play offline.

## What works today

- Paste a Spotify track, album, or playlist URL and download
- Live progress with a loading phase so the first download never feels frozen
- Automatic backup sources (YouTube Music → YouTube → SoundCloud → Bandcamp)
- Inline error reasons and per-track **Retry**
- Organised folders (default `Album artist / Album /`), configurable in Preferences
- Download history sidebar
- Format & quality settings (mp3, flac, opus, m4a, ogg, wav), bitrate, threads, synced lyrics
- FFmpeg and Deno bundled in the Flatpak

## Known limitations

- Free-text search by song name is experimental; **pasting a Spotify link** is the supported flow
- Linux / Flatpak only in this fork (Windows/macOS packaging from upstream was removed)

Planned next steps: first-class Spotify search, optional drag-and-drop of links, Flathub distribution.

## Contributing

We want help. Good first steps:

1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Open an issue for bugs or ideas
3. Fork, branch from `main`, open a PR

No contribution is too small — docs and Flatpak testing count. AI-assisted PRs are fine; see the [AI disclaimer](#ai-disclaimer) above.

## Architecture

| Path | Role |
|------|------|
| `spotdl/` | Upstream download engine (matching, tagging, lyrics) |
| `spotdl/gui/` | GTK 4 / libadwaita desktop UI |
| `packaging/flatpak/` | Flatpak manifest, icons, build script |
| `data/brand/` | README lockup and mark |

## Music sourcing & legal

spotDL uses YouTube (and the backup sources above) for downloads. The highest available bitrate is used (128 kbps for regular YouTube, up to 256 kbps for YouTube Music premium accounts).

> **Note**
> Users are responsible for their actions and any potential legal consequences. We do not support unauthorised downloading of copyrighted material and take no responsibility for user actions.

## Credits

This project builds on the excellent [spotDL](https://github.com/spotDL/spotify-downloader) engine. Matching Spotify metadata to audio, tagging, and lyrics come from spotDL and its contributors.

## License

MIT. See [LICENSE](LICENSE).
