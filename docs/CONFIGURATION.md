# Configuration

spotDL GNOME stores preferences in the shared spotDL config file (same keys the CLI understands). Change them from **Menu → Preferences**.

Setup walkthrough: [SETUP.md](../SETUP.md).

---

## Common settings

| Setting | What it does | Typical value |
|---------|--------------|---------------|
| Output directory | Where files are written | `~/Music` or `~/Downloads/Music` |
| Format | Container / codec | `mp3`, `flac`, `opus`, `m4a`, `ogg`, `wav` |
| Bitrate | Target quality (where applicable) | `128k` … `320k` or `disable` |
| Threads | Parallel downloads | `4` on a typical desktop |
| Lyrics | Embed / sync lyrics | Off, or synced `.lrc` when you want them |
| Folder template | Path pattern under the output directory | Album-artist layout (default) |

---

## Folder template examples

Templates use spotDL formatter tokens. Examples:

```text
{artists}/{album}/{title}.{output-ext}
{album-artist}/{album}/{track-number} - {title}.{output-ext}
{artists}/{title}.{output-ext}
```

Keep templates simple until you know your library player’s expectations. Artist/album folders work well with most library apps.

---

## Audio sources

When a match fails, the GUI tries backup providers automatically:

1. YouTube Music  
2. YouTube  
3. SoundCloud  
4. Bandcamp  

You do not need to configure API keys for the default desktop flow.

---

## Spotify credentials (advanced)

The engine can use bundled default Spotify credentials. Power users who hit rate limits can set their own client ID/secret via the underlying spotDL config — see upstream docs linked from [installation.md](installation.md).

---

## Config file location

On a normal Linux install the config lives under your user spotDL directory (typically `~/.config/spotdl/` or the Flatpak-equivalent sandbox path). Prefer the Preferences UI over hand-editing unless you know what you are changing.
