# FAQ

## Product

**Does spotDL play music?**  
No. It downloads and tags files. Use [Cadence](https://github.com/loafdaddy/Cadence-Music) or another library player.

**Is this the upstream spotDL project?**  
This repository is a **Linux / GNOME Flatpak fork** with a native GTK UI. The download engine comes from [spotDL/spotify-downloader](https://github.com/spotDL/spotify-downloader).

**Why Flatpak instead of pip?**  
Flatpak bundles FFmpeg, Deno, and a consistent GNOME runtime so desktops “just work” without fighting system packages.

## Using the app

**What should I paste?**  
A Spotify track, album, or playlist URL. Free-text search by song name is experimental.

**Why does the first download take a while?**  
The engine starts matching and provider setup on first use. The loading screen is intentional so the UI never looks frozen.

**Where do files go?**  
Wherever you set in Preferences (output directory + folder template).

**Can I retry a failed song?**  
Yes — use the per-row **Retry** button after reading the error reason.

## Platform

**Windows / macOS?**  
Not in this fork. Upstream spotDL still covers other platforms via CLI / their releases.

**Does it need Docker?**  
No for the desktop app. Docker notes in [installation.md](installation.md) are for the upstream CLI workflow.

## Legal

**Is downloading allowed?**  
Users are responsible for their actions and any potential legal consequences. We do not support unauthorised downloading of copyrighted material.

## Contributing

**Are AI-assisted PRs welcome?**  
Yes — see [CONTRIBUTING.md](../CONTRIBUTING.md#ai-assisted-contributions).
