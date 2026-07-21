# spotDL brand

Visual direction: dark, calm, green accent — download signal with an original clock-arrow mark. Sibling feel to Discoverr and Cadence (dark + accent period), distinct palette.

| File | Use |
|------|-----|
| `spotdl-mark.svg` | Icon / avatar / favicon-style mark |
| `spotdl-lockup.svg` | README and marketing (“spotDL.”) |
| `spotdl-social-banner.svg` | GitHub / social Open Graph style banner |
| `../../packaging/flatpak/icons/hicolor/scalable/apps/io.github.loafdaddy.SpotdlGnome.svg` | Desktop / Flatpak app icon |
| `../../spotdl/gui/assets/spotdl-mark.svg` | In-app mark (bundled with the GUI) |

## Palette

| Token | Hex | Role |
|-------|-----|------|
| Accent | `#22D662` | Period, ring, highlights |
| Accent soft | `#7AEEA0` | Lighter ring / hand highlight |
| Accent deep | `#149A45` | Ring shadow stop |
| Deep | `#0F241C` | Mark background mid-stop |
| Deep top | `#163528` | Mark background highlight |
| Deep bottom | `#0A1612` | Mark background shadow |
| Soft text | `#F4FFF8` | Wordmark |
| Muted text | `#A8D4B8` | Banner subtitle |

Wordmark ends with a green period at normal font spacing.

## Typography

Lockup wordmark is **Cantarell Extra Bold** (GNOME’s classic UI face), outlined as SVG paths so GitHub and other hosts render the same weight without needing the font installed.

The green period uses the font’s normal advance after `spotDL` (as in typed `spotDL.`).

Fallback stack if you re-edit as live text: `Cantarell Extra Bold, Cantarell, Adwaita Sans, Inter, Segoe UI, Ubuntu, system-ui, sans-serif` at weight **800**.

## Usage notes

- Prefer the **lockup** in README heroes and marketing.
- Prefer the **mark** alone for app icons, About dialogs, small UI chrome, and square crops.
- Prefer the **social banner** for repository social preview / OG images.
- Do not recolor the accent to teal (Discoverr) or purple (Cadence) — those are sibling brands.
- Export PNG from the SVG if a host does not accept SVG uploads.

The scalable Flatpak/desktop icon matches `spotdl-mark.svg`.
