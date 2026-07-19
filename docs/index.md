# spotDL.

**A native GNOME desktop app for downloading music from Spotify**  
GTK4 · libadwaita · Flatpak · Linux

[v0.2.0](https://github.com/loafdaddy/spotDL-GNOME/releases/tag/v0.2.0)
·
[Release history](RELEASES.md)
·
[Contributing](CONTRIBUTING.md)
·
[Play with Cadence](https://github.com/loafdaddy/Cadence-Music)

spotDL finds songs from your Spotify tracks, albums, and playlists on YouTube and downloads them — complete with album art, lyrics, and metadata. This is a Linux fork that wraps the [spotDL](https://github.com/spotDL/spotify-downloader) engine in a native **GTK 4 / libadwaita** interface, packaged as a self-contained **Flatpak**.

This aims to feel like it ships with Fedora Workstation: Wayland-first, Flatpak-friendly, no Electron.

> Paste a Spotify link → download organised files → play them in [Cadence](https://github.com/loafdaddy/Cadence-Music).

## AI disclaimer

Parts of this fork — including the GTK GUI, Flatpak packaging, docs, and branding — have been written or edited with **AI assistance** (for example Cursor and similar tools). That is intentional for an early project moving quickly. The upstream spotDL engine remains the work of the [spotDL project](https://github.com/spotDL/spotify-downloader) and its contributors.

**AI-assisted contributions are welcome.** Use Cursor, Copilot, ChatGPT, Claude, or any other assistant if it helps you. You remain responsible for what you submit: understand the change, keep pull requests focused, and verify what you can.

Full expectations: [Contributing — AI-assisted contributions](CONTRIBUTING.md#ai-assisted-contributions).

## Try it

### Flatpak (recommended)

Grab the prebuilt bundle from the
[latest release](https://github.com/loafdaddy/spotDL-GNOME/releases/latest):

```bash
sudo dnf install -y flatpak
flatpak remote-add --if-not-exists --user flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install --user ./io.github.loafdaddy.SpotdlGnome.flatpak
flatpak run io.github.loafdaddy.SpotdlGnome
```

### Build from source

```bash
sudo dnf install -y flatpak flatpak-builder
git clone https://github.com/loafdaddy/spotDL-GNOME.git
cd spotDL-GNOME
./packaging/flatpak/build.sh
```

See also [Installation](installation.md) for CLI-oriented notes inherited from upstream.

## Play your downloads

spotDL does not play music. Use **[Cadence](https://github.com/loafdaddy/Cadence-Music)** — a modern native Linux music library — pointed at your download folder.

## What works today

- Paste a Spotify track, album, or playlist URL and download
- Live progress and helpful errors with per-track retry
- Automatic backup audio sources
- Organised folders and download history
- Format / bitrate / lyrics preferences
- FFmpeg and Deno bundled in the Flatpak

## Known limitations

- Free-text name search is experimental; paste a Spotify link for reliable results
- This fork targets Linux / Flatpak only

## Contributing

1. Read [Contributing](CONTRIBUTING.md)
2. Open an issue for bugs or ideas
3. Fork, branch from `main`, open a PR

AI-assisted PRs are welcome under the expectations in Contributing.

## Music sourcing & legal

spotDL uses YouTube (and backup sources) for downloads.

> **Note**
> Users are responsible for their actions and any potential legal consequences. We do not support unauthorised downloading of copyrighted material and take no responsibility for user actions.

## Credits

Built on [spotDL](https://github.com/spotDL/spotify-downloader). Sibling player: [Cadence](https://github.com/loafdaddy/Cadence-Music).

## License

[MIT](https://github.com/loafdaddy/spotDL-GNOME/blob/main/LICENSE)
