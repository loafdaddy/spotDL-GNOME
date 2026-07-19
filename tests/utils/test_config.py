import os
import platform
from pathlib import Path
from types import SimpleNamespace

import pytest

from spotdl.utils.config import *


@pytest.fixture()
def setup(tmp_path, monkeypatch):
    # get_spotdl_path() uses Path.home(), which calls os.path.expanduser("~").
    # Return a str so pathlib does not choke on a Path monkeypatch value.
    monkeypatch.setattr(Path, "home", classmethod(lambda cls: tmp_path))
    monkeypatch.setattr(os.path, "expanduser", lambda path: str(tmp_path))
    data = SimpleNamespace()
    data.directory = tmp_path
    yield data


def _expected_spotdl_path(home: Path) -> Path:
    """Match get_spotdl_path() layout for a brand-new home directory."""
    if platform.system() == "Linux":
        return home / ".config" / "spotdl"
    return home / ".spotdl"


def test_get_spotdl_path(setup):
    """
    Tests that the spotdl path is created if it does not exist.
    """

    expected = _expected_spotdl_path(setup.directory)
    assert get_spotdl_path() == expected
    assert expected.exists()


def test_get_config_path(setup):
    """
    Tests if the path to config file is correct.
    """

    assert get_config_file() == _expected_spotdl_path(setup.directory) / "config.json"


def test_get_cache_path(setup):
    """
    Tests if the path to the cache file is correct.
    """

    assert get_cache_path() == _expected_spotdl_path(setup.directory) / ".spotipy"


def test_get_temp_path(setup):
    """
    Tests if the path to the temp folder is correct.
    """

    assert get_temp_path() == _expected_spotdl_path(setup.directory) / "temp"


def test_get_config_not_created(setup):
    """
    Tests if exception is raised if config file does not exist.
    """

    with pytest.raises(ConfigError):
        get_config()


def test_use_official_api_default():
    """
    Tests that the official API client is opt-in.
    """

    settings = create_settings_type(SimpleNamespace(), {}, SPOTIFY_OPTIONS)

    assert settings["use_official_api"] is False


def test_use_official_api_from_config():
    """
    Tests that config can enable the official API client.
    """

    settings = create_settings_type(
        SimpleNamespace(),
        {"use_official_api": True},
        SPOTIFY_OPTIONS,
    )

    assert settings["use_official_api"] is True


def test_use_official_api_argument_overrides_config():
    """
    Tests that CLI arguments take priority over config values.
    """

    settings = create_settings_type(
        SimpleNamespace(use_official_api=True),
        {"use_official_api": False},
        SPOTIFY_OPTIONS,
    )

    assert settings["use_official_api"] is True
