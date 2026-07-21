# spotDL GNOME releases

Track every published version here. Update this file when cutting a release, then tag and publish on GitHub.

Current fork version in tree: **0.2.2** (`spotdl/gui/identity.py` `APP_VERSION` + AppStream metainfo).  
Upstream engine version: **4.5.0** (`pyproject.toml` / `spotdl/_version.py`).

## Versioning

This fork uses [Semantic Versioning](https://semver.org/) for the **GNOME / Flatpak app**:

| Part | Meaning |
|------|---------|
| **MAJOR** | Breaking GUI or Flatpak behaviour users must migrate for |
| **MINOR** | New features or UI surfaces |
| **PATCH** | Fixes and small polish |

The spotDL **engine** version stays aligned with upstream when vendored/synced; it is shown in About as `(engine x.y.z)`.

## How to cut a release

1. Bump `APP_VERSION` in `spotdl/gui/identity.py`
2. Add a matching `<release>` entry in `packaging/flatpak/io.github.loafdaddy.SpotdlGnome.metainfo.xml`
3. Add a section below in this file; update README version links if needed
4. Commit on `main`
5. Tag: `git tag -a v0.2.2 -m "spotDL GNOME 0.2.2"`
6. Push: `git push origin main --tags`
7. Create / update the GitHub release (notes can mirror the section below)
8. The `flatpak-release` workflow builds `io.github.loafdaddy.SpotdlGnome.flatpak` and attaches it to the tag release

## Releases

### 0.2.2 — 2026-07-21

**Status:** early build · not on Flathub yet

**Highlights**
- Brand kit elevated to Discoverr studio language (Cantarell Extra Bold lockup, gradients, social banner)
- In-app branding uses the bundled mark (`spotdl/gui/assets/`) so from-source runs still show the icon
- Docs reorganised: `SETUP.md`, `docs/README.md`, FAQ / Configuration / Architecture / Roadmap / TODO
- Removed Cadence references; playback is via any external music library

**Install**
- Flatpak bundle from the [GitHub release](https://github.com/loafdaddy/spotDL-GNOME/releases/tag/v0.2.2)
- Or build: `./packaging/flatpak/build.sh` then `flatpak run io.github.loafdaddy.SpotdlGnome`

### 0.2.1 — 2026-07-19

**Status:** early build · not on Flathub yet

**Highlights**
- Flatpak runtime bumped from EOL GNOME 48 to GNOME 50 (`org.gnome.Platform` / `Sdk` + CI image)

**Install**
- Flatpak bundle from the [GitHub release](https://github.com/loafdaddy/spotDL-GNOME/releases/tag/v0.2.1)
- Or build: `./packaging/flatpak/build.sh` then `flatpak run io.github.loafdaddy.SpotdlGnome`

### 0.2.0 — 2026-07-19

**Status:** early build · not on Flathub yet

**Highlights**
- spotDL. brand lockup and refreshed app icon (dark + green)
- In-app branding: home status page, welcome dialog, About (links to spotDL-GNOME)
- README / docs / CONTRIBUTING polish; AI-assisted contributions welcome
- Clarify that playback is via an external music library
- Default branch `main`; Linux-only CI and docs build (no Pages deploy)

**Install**
- Flatpak bundle from the [GitHub release](https://github.com/loafdaddy/spotDL-GNOME/releases/tag/v0.2.0)
- Or build: `./packaging/flatpak/build.sh` then `flatpak run io.github.loafdaddy.SpotdlGnome`

**AI note:** Substantial parts of this release were developed with AI assistance. AI-assisted contributions remain welcome — see [CONTRIBUTING.md](../CONTRIBUTING.md#ai-assisted-contributions).

### 0.1.0 — 2026-07-18 (first Flatpak GUI)

**Status:** initial fork release

**Highlights**
- Native GTK4 / libadwaita GUI on the spotDL engine
- Flatpak with bundled FFmpeg and Deno
- Progress UI, backup sources, history sidebar, preferences

**Install**
- GitHub: https://github.com/loafdaddy/spotDL-GNOME/releases/tag/v0.1.0
