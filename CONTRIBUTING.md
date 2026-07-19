# Contributing to spotDL GNOME

Thanks for considering a contribution. This is a Linux/Flatpak fork of [spotDL](https://github.com/spotDL/spotify-downloader) with a native GTK GUI — we need help on UI, packaging, docs, and the download experience.

## Quick start (GUI from source)

```bash
git clone https://github.com/loafdaddy/spotDL-GNOME.git
cd spotDL-GNOME

# Fedora: GTK 4 + libadwaita + PyGObject
sudo dnf install python3-gobject gtk4 libadwaita

python -m venv --system-site-packages .venv && source .venv/bin/activate
pip install -e ".[gui]"
python -m spotdl.gui
```

Flatpak build (closer to what users run):

```bash
sudo dnf install flatpak flatpak-builder
./packaging/flatpak/build.sh
flatpak run io.github.loafdaddy.SpotdlGnome
```

See [packaging/flatpak/README.md](packaging/flatpak/README.md) for details.

## Development loop

```bash
# Run the GUI
python -m spotdl.gui

# Format + lint (keep these green before a PR)
black spotdl && isort spotdl
mypy --ignore-missing-imports --follow-imports silent spotdl
pylint --fail-under 10 spotdl

# Tests
pytest -vvv tests
```

Typical change flow:

1. Create a branch from `main` (`git checkout -b feature/short-name`)
2. Make a focused change
3. Run format/lint/tests where relevant
4. Open a pull request against `main` with a short “why” in the description

## Project map

| Path | What it is |
|------|------------|
| `spotdl/` | Core download engine (mostly upstream) |
| `spotdl/gui/` | GTK 4 / libadwaita UI |
| `packaging/flatpak/` | Manifest, desktop entry, icons, build script |
| `data/brand/` | Lockup and mark for README / marketing |
| `docs/` | MkDocs site (installation, usage, contributing) |
| `screenshots/` | README screenshots |

Play downloaded music with **[Cadence](https://github.com/loafdaddy/Cadence-Music)** — a sibling native Linux player.

## What we need most right now

- Bug reports with steps to reproduce (Fedora / Flatpak / from-source)
- Flatpak install testing via `./packaging/flatpak/build.sh` or the release bundle
- UI polish that fits Adwaita
- Finishing free-text Spotify search
- Docs clarity for first-time Flatpak users

## AI-assisted contributions

**AI tools are welcome.** You can use Cursor, Copilot, ChatGPT, Claude, or similar to help write code, docs, tests, or Flatpak packaging.

A few expectations so reviews stay useful:

- You understand and stand behind the change — if asked, you can explain what it does and why
- You have built and/or run the relevant bits (or say clearly what you could not verify)
- Do not paste large generated dumps that rewrite unrelated files
- Prefer small PRs; call out in the description if AI helped in a substantial way (optional but appreciated)

Parts of this fork itself may have been written or edited with AI assistance. That is intentional for an early project moving quickly. Human review still applies to every merge.

## Code style

- Prefer small, focused PRs
- Match existing naming and module layout
- Avoid drive-by refactors unrelated to the change
- No emoji in docs or UI strings
- MIT license for contributions (same as the project)

## Brand

App icon and wordmark live under `data/brand/` and `packaging/flatpak/icons/`. Visual direction is dark + green accent with the wordmark **spotDL.** — see [data/brand/README.md](data/brand/README.md).

## Communication

- Issues and PRs: https://github.com/loafdaddy/spotDL-GNOME
- Be respectful; this is an early fork and maintainers may move slowly
