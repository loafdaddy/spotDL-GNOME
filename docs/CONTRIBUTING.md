# Contributing to spotDL GNOME

Thanks for considering a contribution. This is a Linux/Flatpak fork of [spotDL](https://github.com/spotDL/spotify-downloader) with a native GTK GUI.

The full guide lives in the repository root: **[CONTRIBUTING.md](https://github.com/loafdaddy/spotDL-GNOME/blob/main/CONTRIBUTING.md)**.

## Quick start (GUI from source)

```bash
git clone https://github.com/loafdaddy/spotDL-GNOME.git
cd spotDL-GNOME

sudo dnf install python3-gobject gtk4 libadwaita

python -m venv --system-site-packages .venv && source .venv/bin/activate
pip install -e ".[gui]"
python -m spotdl.gui
```

## Checks before a PR

```bash
black spotdl && isort spotdl
mypy --ignore-missing-imports --follow-imports silent spotdl
pylint --fail-under 10 spotdl
pytest -vvv tests
```

Branch from `main`, keep PRs focused, and open against `main`.

## AI-assisted contributions

**AI tools are welcome.** You remain responsible for what you submit: understand the change, keep pull requests focused, and verify what you can.

Full expectations: [AI-assisted contributions](https://github.com/loafdaddy/spotDL-GNOME/blob/main/CONTRIBUTING.md#ai-assisted-contributions).

## Play downloads in Cadence

After downloading, use **[Cadence](https://github.com/loafdaddy/Cadence-Music)** to play your library on Linux.

## Communication

- Issues and PRs: https://github.com/loafdaddy/spotDL-GNOME
