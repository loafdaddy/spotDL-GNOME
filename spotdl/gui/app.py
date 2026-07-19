"""
The Adw.Application subclass that hosts the spotDL GUI.
"""

import logging
from typing import Any, Optional

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

# pylint: disable=wrong-import-position
from gi.repository import Adw, Gio, Gtk  # noqa: E402

from spotdl._version import __version__  # noqa: E402
from spotdl.gui.window import SpotdlWindow  # noqa: E402

logger = logging.getLogger(__name__)

__all__ = ["SpotdlApplication", "APP_ID", "APP_NAME", "APP_VERSION"]

APP_ID = "io.github.loafdaddy.SpotdlGnome"
APP_NAME = "spotDL"
# Fork / Flatpak release version (engine version remains spotdl.__version__).
APP_VERSION = "0.2.1"


class SpotdlApplication(Adw.Application):
    """Top-level libadwaita application for spotDL."""

    def __init__(self) -> None:
        super().__init__(
            application_id=APP_ID,
            # pylint: disable=no-member
            flags=Gio.ApplicationFlags.DEFAULT_FLAGS,
        )
        self.window: Optional[SpotdlWindow] = None

    def do_startup(self) -> None:  # noqa: D401  pylint: disable=arguments-differ
        """Set up application-wide actions and accelerators."""

        Adw.Application.do_startup(self)

        self._add_action("preferences", self._on_preferences, ["<primary>comma"])
        self._add_action("about", self._on_about)
        self._add_action("quit", lambda *_: self.quit(), ["<primary>q"])

    def do_activate(self) -> None:  # noqa: D401  pylint: disable=arguments-differ
        """Present the main window, creating it on first activation."""

        if self.window is None:
            self.window = SpotdlWindow(application=self)
        self.window.present()

    def _add_action(self, name: str, callback: Any, accels: Any = None) -> None:
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if accels:
            self.set_accels_for_action(f"app.{name}", accels)

    def _on_preferences(self, *_args: Any) -> None:
        # Imported lazily to keep startup snappy.
        # pylint: disable=import-outside-toplevel
        from spotdl.gui.preferences import SpotdlPreferences

        prefs = SpotdlPreferences(self.window)
        prefs.present(self.window)

    def _on_about(self, *_args: Any) -> None:
        about = Adw.AboutDialog(
            application_name=APP_NAME,
            application_icon=APP_ID,
            version=f"{APP_VERSION} (engine {__version__})",
            developer_name="loafdaddy",
            website="https://github.com/loafdaddy/spotDL-GNOME",
            issue_url="https://github.com/loafdaddy/spotDL-GNOME/issues",
            license_type=Gtk.License.MIT_X11,
            comments=(
                "A native GTK4 / libadwaita desktop app for Linux that downloads "
                "music from Spotify. Built on the spotDL engine. Play downloads "
                "with Cadence."
            ),
        )
        about.add_credit_section(
            "Based on", ["spotDL https://github.com/spotDL/spotify-downloader"]
        )
        about.add_credit_section(
            "Play with", ["Cadence https://github.com/loafdaddy/Cadence-Music"]
        )
        about.present(self.window)
