# spotDL.

**A native GNOME desktop app for downloading music from Spotify**  
GTK4 · libadwaita · Flatpak · Linux

[v0.2.2](https://github.com/loafdaddy/spotDL-GNOME/releases/tag/v0.2.2)
·
[Setup](../SETUP.md)
·
[Releases](RELEASES.md)
·
[Contributing](../CONTRIBUTING.md)
·
[Docs index](README.md)

spotDL finds songs from your Spotify tracks, albums, and playlists on YouTube and downloads them — complete with album art, lyrics, and metadata. This Linux fork wraps the [spotDL](https://github.com/spotDL/spotify-downloader) engine in a native **GTK 4 / libadwaita** interface, packaged as a self-contained **Flatpak**.

Built to feel like it ships with Fedora Workstation: Wayland-first, Flatpak-friendly, no Electron.

> Paste a Spotify link → download organised files → play them in your music library.

## Try it

Full Flatpak walkthrough: **[SETUP.md](../SETUP.md)**.

```bash
flatpak install --user ./io.github.loafdaddy.SpotdlGnome.flatpak
flatpak run io.github.loafdaddy.SpotdlGnome
```

## Docs map

| Doc | What it covers |
|-----|----------------|
| [SETUP.md](../SETUP.md) | Flatpak install and first-run smoke test |
| [CONFIGURATION.md](CONFIGURATION.md) | Preferences and templates |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Engine / GUI / Flatpak |
| [FAQ.md](FAQ.md) | Common questions |
| [RELEASES.md](RELEASES.md) | SemVer history |
| [ROADMAP.md](ROADMAP.md) / [TODO.md](TODO.md) | Direction and status |
| [DEVELOPMENT.md](DEVELOPMENT.md) | Contributor notes |

## Music sourcing & legal

spotDL uses YouTube (and backup sources) for downloads. The highest available bitrate is used (128 kbps for regular YouTube, up to 256 kbps for YouTube Music premium accounts).

**Software vs usage.** spotDL is open-source software with legitimate non-infringing uses (for example, downloading royalty-free or public-domain music you have permission to obtain). Open source does not mean unrestricted downloading of copyrighted material. Using this tool to download copyrighted tracks without permission from the rights holders is copyright infringement in most jurisdictions.

**Platform terms of service.** Using spotDL may also violate the terms of the services involved:
- **Spotify** prohibits automated access, scraping, and tools that copy, record, or extract content from their service.
- **YouTube** prohibits downloading or ripping audio/video streams unless YouTube or the content creator provides a download link or explicit permission.

Metadata from Spotify (track titles, artists, album art, and similar) is obtained via Spotify’s public API where configured. Audio itself is not downloaded from Spotify; it is matched and fetched from YouTube and other backup sources. Using public or authorized APIs for metadata is not the same as extracting or ripping stream content in ways those platforms forbid.

> **Note**
> Users are responsible for their actions and any potential legal consequences. We do not support unauthorised downloading of copyrighted material and take no responsibility for user actions. Only download content you have the right to obtain.

## Credits

Built on [spotDL](https://github.com/spotDL/spotify-downloader).

## License

[MIT](https://github.com/loafdaddy/spotDL-GNOME/blob/main/LICENSE)
