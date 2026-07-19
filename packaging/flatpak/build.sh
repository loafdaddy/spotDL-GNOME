#!/usr/bin/env bash
#
# Build the spotDL Flatpak locally.
#
# Usage:
#   ./packaging/flatpak/build.sh            # build + install (per-user)
#   ./packaging/flatpak/build.sh --run      # build + install + launch the app
#   ./packaging/flatpak/build.sh --bundle   # build + export a single-file
#                                           # .flatpak you can share/upload
#
set -euo pipefail

APP_ID="io.github.loafdaddy.SpotdlGnome"
RUNTIME_VERSION="50"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MANIFEST="${SCRIPT_DIR}/${APP_ID}.yml"
BUILD_DIR="${SCRIPT_DIR}/build-dir"
REPO_DIR="${SCRIPT_DIR}/build-repo"
BUNDLE_PATH="${SCRIPT_DIR}/${APP_ID}.flatpak"

mode="install"
run_after=0
for arg in "$@"; do
  case "$arg" in
    --run) run_after=1 ;;
    --bundle) mode="bundle" ;;
    *) echo "Unknown option: $arg" >&2; exit 2 ;;
  esac
done

if ! command -v flatpak-builder >/dev/null 2>&1; then
  echo "flatpak-builder is not installed."
  echo "On Fedora:        sudo dnf install flatpak-builder"
  echo "On Debian/Ubuntu: sudo apt install flatpak-builder"
  echo "On Arch:          sudo pacman -S flatpak-builder"
  exit 1
fi

# Ensure Flathub is configured for the current user.
flatpak --user remote-add --if-not-exists flathub \
  https://flathub.org/repo/flathub.flatpakrepo

# Install the GNOME runtime + SDK the manifest builds against.
flatpak --user install -y flathub \
  "org.gnome.Platform//${RUNTIME_VERSION}" \
  "org.gnome.Sdk//${RUNTIME_VERSION}"

if [[ "${mode}" == "bundle" ]]; then
  # Build, export into a local OSTree repo, then wrap that into a single
  # distributable .flatpak file (what gets attached to a GitHub release).
  flatpak-builder --user --force-clean --repo="${REPO_DIR}" \
    "${BUILD_DIR}" "${MANIFEST}"
  flatpak build-bundle "${REPO_DIR}" "${BUNDLE_PATH}" "${APP_ID}" \
    --runtime-repo=https://flathub.org/repo/flathub.flatpakrepo
  echo
  echo "Created ${BUNDLE_PATH}"
  echo "Install it with: flatpak install --user \"${BUNDLE_PATH}\""
  exit 0
fi

# Build and install into the user installation.
flatpak-builder --user --install --force-clean \
  "${BUILD_DIR}" "${MANIFEST}"

echo
echo "Installed ${APP_ID}."
echo "Launch it with: flatpak run ${APP_ID}"

if [[ "${run_after}" -eq 1 ]]; then
  exec flatpak run "${APP_ID}"
fi
