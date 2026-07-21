# Architecture

High-level layout for the GNOME fork. Day-to-day status: [TODO.md](TODO.md) · releases: [RELEASES.md](RELEASES.md).

## Modules

| Path | Role |
|------|------|
| `spotdl/` | Upstream download engine (matching, tagging, lyrics, providers) |
| `spotdl/gui/` | GTK 4 / libadwaita desktop UI |
| `spotdl/gui/assets/` | Bundled brand mark for in-app chrome |
| `packaging/flatpak/` | Manifest, desktop entry, icons, build script |
| `data/brand/` | Marketing lockup, mark, social banner |
| `docs/` | Product docs + MkDocs site |
| `tests/` | Engine and utility tests |

## Runtime flow

```text
User pastes Spotify URL
        │
        ▼
  spotdl/gui/window.py   ← Adwaita UI, progress rows, history
        │
        ▼
  spotdl/gui/backend.py  ← background thread + event queue
        │
        ▼
  spotdl engine          ← search / match / download / tag
        │
        ▼
  Files on disk (+ optional .lrc)
```

## Flatpak

- App ID: `io.github.loafdaddy.SpotdlGnome`
- Command: `spotdl-gui`
- Runtime: GNOME Platform (see manifest)
- Bundles FFmpeg and Deno so YouTube extraction works offline from the host package set

## Branding

Studio family with Discoverr (teal): dark base, accent period wordmark, Cantarell Extra Bold lockup. spotDL’s accent is green (`#22D662`). Details: [data/brand/README.md](../data/brand/README.md).
