# AGENTS.md

Flet custom-control extension: a Python API (`src/flet_blurhash/`) backed by a Flutter widget (`src/flutter/flet_blurhash/`). Both sides are coupled by string identifiers and must be changed together.

## Commands

- Run the example: `just run` (from repo root).
- Build the example: `just build linux`, `just build web`, or `just build apk`.
- Serve built web output: `just serve` (only after `just build web`).
- `just run web` is broken: it passes `web` as the script path. For web, use `cd examples/flet_blurhash_example && uv run flet run -w -d -r`.
- The Justfile commands `cd examples/flet_blurhash_example` themselves; do not run `flet run` from the repo root. The example resolves the extension via `tool.uv.sources` and `tool.flet.dev_packages` (`path = "../../"`, editable).
- Run tests: `uv run --group test pytest -q`. Tested locally on Python 3.10-3.14; no CI workflow is configured.
- Verify Dart: `cd src/flutter/flet_blurhash && flutter pub get && dart analyze`.
- For packaging changes, run `uv build` and confirm the wheel contains top-level `flutter/flet_blurhash/`.

## Cross-language contract

- Python `@ft.control("FletBlurHash")` must match `case "FletBlurHash"` in `src/flutter/flet_blurhash/lib/src/extension.dart`.
- Dart reads attributes by Python field name: `hash`, `color`, `image_fit`, `duration`, `curve`, `optimization_mode`, `image`, `error_content`. Renaming a Python field requires updating `flet_blurhash.dart`.
- `BlurHashOptimizationMode` values (`none`, `standard`, `approximation`) are parsed in `_optimizationMode()` in the Dart widget. Adding a mode requires both sides.
- Dart emits `decode`/`display`/`ready`/`start`, which map to Python `on_decode`/`on_display`/`on_ready`/`on_start`.

## Layout / packaging

- `src/flutter/` is not Python code. Setuptools ships it as `site-packages/flutter/`, and `flet build`/`flet debug` auto-register every `flutter/*/pubspec.yaml`. Do not move it under `src/flet_blurhash/`.
- The Flutter package depends on `flet: ^1.1.2` (Flutter `>=3.47.0`) and `flutter_blurhash: ^0.9.1`.
- Requires Python `>=3.10` and targets Flet `1.1.x`. `@ft.control` and `FletExtension` APIs are version-sensitive; avoid broad Flet upgrades.

## Repo conventions

- `README.md` is the single English README. Keep its usage and API reference current.
- The demo video is `assets/screen.mp4` and is embedded in `README.md`.
- Root `uv.lock` and the example's `uv.lock` are committed.
