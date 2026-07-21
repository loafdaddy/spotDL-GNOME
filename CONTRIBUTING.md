# Contributing to spotDL GNOME

Thanks for considering a contribution. This is a Linux/Flatpak fork of [spotDL](https://github.com/spotDL/spotify-downloader) with a native GTK GUI — focused changes help a lot.

**Operators run the app with Flatpak** ([SETUP.md](SETUP.md)). A Python venv on the host is for contributors, not the supported end-user path.

## Quick start (contributors)

```bash
git clone https://github.com/loafdaddy/spotDL-GNOME.git
cd spotDL-GNOME

# Fedora: GTK 4 + libadwaita + PyGObject
sudo dnf install python3-gobject gtk4 libadwaita

python -m venv --system-site-packages .venv && source .venv/bin/activate
pip install -e ".[gui]"
python -m spotdl.gui
```

Smoke-test the real product path:

```bash
sudo dnf install flatpak flatpak-builder
./packaging/flatpak/build.sh
flatpak run io.github.loafdaddy.SpotdlGnome
```

Docs:

- [README.md](README.md) — short product overview
- [SETUP.md](SETUP.md) — ordered Flatpak install
- [docs/README.md](docs/README.md) — docs index
- [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) — local GUI / Flatpak notes
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — modules and runtime flow
- [docs/RELEASES.md](docs/RELEASES.md) — version history and how to cut a release
- [docs/TODO.md](docs/TODO.md) / [docs/ROADMAP.md](docs/ROADMAP.md) — status and direction
- [data/brand/README.md](data/brand/README.md) — brand assets

## Development loop

```bash
python -m spotdl.gui

black spotdl && isort spotdl
mypy --ignore-missing-imports --follow-imports silent spotdl
pylint --fail-under 10 spotdl
pytest -vvv tests
```

Typical change flow:

1. Branch from `main` (`git checkout -b improve/short-name`)
2. Make a focused change
3. Run format/lint/tests where relevant
4. Rebuild the Flatpak if you need a packaging check
5. Open a pull request against `main` with a short “why” in the description

## Project map

| Path | What it is |
|------|------------|
| `spotdl/` | Core download engine (mostly upstream) |
| `spotdl/gui/` | GTK 4 / libadwaita UI |
| `spotdl/gui/assets/` | Bundled brand mark for in-app chrome |
| `packaging/flatpak/` | Manifest, desktop entry, icons, build script |
| `data/brand/` | Lockup, mark, social banner |
| `docs/` | Product docs + MkDocs site |
| `docs/assets/` | README screenshots |

## Releases

When shipping a version, follow [docs/RELEASES.md](docs/RELEASES.md): bump `APP_VERSION` in `spotdl/gui/identity.py`, update AppStream metainfo, add a release section, tag `vX.Y.Z`, and publish a GitHub release. Keep [docs/TODO.md](docs/TODO.md) honest.

## Conventions

- Prefer small, focused PRs
- Match existing naming and module layout
- Avoid drive-by refactors unrelated to the change
- No emoji in **UI strings**; README marketing may use light emoji like sibling projects
- Do not document `pip install` as the operator path — Flatpak is the product runtime
- Keep brand accent green (`#22D662`); do not recolor toward Discoverr teal
- MIT license for contributions (same as the project)

## What helps most

- Bug reports with steps to reproduce (Fedora / Flatpak / from-source)
- Flatpak install testing via `./packaging/flatpak/build.sh` or the release bundle
- UI polish that fits Adwaita
- Finishing free-text Spotify search
- Docs clarity for first-time Flatpak users

## AI-assisted contributions

**AI tools are welcome.** You can use Cursor, Copilot, ChatGPT, Claude, or similar to help write code, docs, tests, or Flatpak packaging.

Expectations:

- You understand and stand behind the change
- You have built and/or run the relevant bits (or say clearly what you could not verify)
- Keep pull requests focused — avoid unrelated rewrites
- Call out in the description if AI helped in a substantial way (optional but appreciated)

Parts of this fork itself may have been written or edited with AI assistance. That is intentional for an early project moving quickly. Human review still applies to every merge.

## Brand

App icon and wordmark live under `data/brand/` and `packaging/flatpak/icons/`. Visual direction is dark + green accent with the wordmark **spotDL.** — see [data/brand/README.md](data/brand/README.md).

## Communication

- Issues and PRs: https://github.com/loafdaddy/spotDL-GNOME
- Be respectful; this is an early fork and maintainers may move slowly
