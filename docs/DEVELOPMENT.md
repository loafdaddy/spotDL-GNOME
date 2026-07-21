# Development

Contributor-oriented notes for the GNOME GUI and Flatpak. Product install for users: [SETUP.md](../SETUP.md). Conventions: [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## GUI from source

```bash
git clone https://github.com/loafdaddy/spotDL-GNOME.git
cd spotDL-GNOME

# Fedora example
sudo dnf install python3-gobject gtk4 libadwaita

python -m venv --system-site-packages .venv && source .venv/bin/activate
pip install -e ".[gui]"
python -m spotdl.gui
```

The bundled mark lives at `spotdl/gui/assets/spotdl-mark.svg` so the empty state still shows branding when the desktop icon theme is not installed.

---

## Flatpak build

```bash
sudo dnf install flatpak flatpak-builder
./packaging/flatpak/build.sh
flatpak run io.github.loafdaddy.SpotdlGnome
```

See [packaging/flatpak/README.md](../packaging/flatpak/README.md).

---

## Checks

```bash
black spotdl && isort spotdl
mypy --ignore-missing-imports --follow-imports silent spotdl
pylint --fail-under 10 spotdl
pytest -vvv tests
```

---

## Brand assets

Marketing SVGs: `data/brand/`.  
Desktop icon: `packaging/flatpak/icons/.../io.github.loafdaddy.SpotdlGnome.svg`.  
Keep the green palette and Cantarell Extra Bold lockup — see [data/brand/README.md](../data/brand/README.md).

---

## Docs site (optional)

```bash
mkdocs serve
```

Nav is defined in `mkdocs.yml`. GitHub-facing docs also live as plain Markdown (`SETUP.md`, `docs/*.md`) so they read well without MkDocs.
