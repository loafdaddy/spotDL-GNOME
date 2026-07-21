"""
In-app brand helpers for the spotDL GNOME GUI.

Keeps the download-clock mark visible even when the desktop icon theme
does not include ``io.github.loafdaddy.SpotdlGnome`` (common for from-source runs).
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)

__all__ = ["ASSETS_DIR", "MARK_PATH", "load_mark_paintable"]

ASSETS_DIR = Path(__file__).resolve().parent / "assets"
MARK_PATH = ASSETS_DIR / "spotdl-mark.svg"


def load_mark_paintable(size: int = 128, scale: int = 1) -> Optional[Any]:
    """Return a paintable for the bundled mark, or ``None`` if unavailable."""

    if not MARK_PATH.is_file():
        return None

    try:
        # Lazy import: keep this module importable without system GTK bindings.
        import gi  # pylint: disable=import-outside-toplevel

        gi.require_version("Gtk", "4.0")
        from gi.repository import Gio, Gtk  # pylint: disable=import-outside-toplevel
    except (ImportError, ValueError):
        logger.debug("GTK unavailable; skipping brand mark paintable")
        return None

    try:
        return Gtk.IconPaintable.new_for_file(
            Gio.File.new_for_path(str(MARK_PATH)),
            size,
            scale,
        )
    except Exception:  # pylint: disable=broad-except
        logger.debug("Could not load brand mark from %s", MARK_PATH, exc_info=True)
        return None
