# 🖼️ FLET BLUR HASH

![PyPI - Downloads](https://img.shields.io/pypi/dw/flet-blurhash)
![PyPI - Version](https://img.shields.io/pypi/v/flet-blurhash)

**flet-blurhash** is a **BlurHash implementation for Flet**, inspired by **BlurHash in Flutter**.
It shows a **blurred placeholder** while the real image loads, then fades smoothly into the image.

## ✨ Features

- 🚀 Fast BlurHash rendering
- 🖼️ Blurred placeholder while the image is loading
- ⏳ Smooth transition animation to the real image
- 🔌 Works as a native **Flet custom control**
- 💙 Simple API with Flutter-like concepts
- 🖥️ Multi-platform support:
  - Android 🟢
  - Linux 🟢
  - Web 🟢
  - Windows (untested)
  - macOS (untested)

## 📦 Installation

```bash
uv add flet-blurhash
```

Or with pip:

```bash
pip install flet-blurhash
```

## 🤖 Requirements

- **Python** `3.10+`
- **Flet** `1.1.2+`

> [!WARNING]
> This library requires Python `3.10` or newer and Flet `1.1.2` or newer.

## 🚀 Quick Start

> [!NOTE]
> Generate a hash from [blurha.sh](https://blurha.sh/).

```python
import flet as ft
from flet_blurhash import BlurHashOptimizationMode, FletBlurHash


def main(page: ft.Page):
    def on_display(e):
        print("display:", e.data)

    page.add(
        ft.Container(
            height=400,
            width=400,
            content=FletBlurHash(
                hash="LKO2:N%2Tw=w]~RBVZRi};RPxuwH",
                image="https://fastly.picsum.photos/id/21/3008/2008.jpg?hmac=T8DSVNvP-QldCew7WD4jj_S3mWwxZPqdF0CNPksSko4",
                duration=ft.Duration(seconds=3),
                curve=ft.AnimationCurve.BOUNCE_IN,
                optimization_mode=BlurHashOptimizationMode.APPROXIMATION,
                on_display=on_display,
            ),
        )
    )


ft.run(main)
```

## 🧠 Getting a BlurHash

A BlurHash is a short string that encodes a blurred version of an image. Use
[blurha.sh](https://blurha.sh/) to generate one from your image, then pass it to the
`hash` argument.

The `image` argument is optional. Without it, only the blurred placeholder is shown.

## 🎛️ API Reference

### `FletBlurHash`

| Property | Type | Default | Description |
| --- | --- | --- | --- |
| `hash` | `str` | required | BlurHash string from [blurha.sh](https://blurha.sh/). |
| `image` | `str \| None` | `None` | Image URL to load after the placeholder. |
| `color` | `ft.ColorValue` | `ft.Colors.GREY` | Background color shown before the hash is decoded. |
| `image_fit` | `ft.BoxFit` | `ft.BoxFit.FILL` | How the image fits inside the control. |
| `duration` | `ft.DurationValue` | `1000 ms` | Fade duration from placeholder to image. |
| `curve` | `ft.AnimationCurve` | `ft.AnimationCurve.EASE_OUT` | Animation curve for the fade. |
| `optimization_mode` | `BlurHashOptimizationMode` | `NONE` | Decoding performance mode. |
| `error_content` | `ft.Control \| None` | `None` | Custom widget shown if the widget fails to build. |

### Events

| Event | Fires when |
| --- | --- |
| `on_start` | Image download starts. |
| `on_decode` | The BlurHash has been decoded. |
| `on_ready` | The image has finished downloading. |
| `on_display` | The fade animation to the image has completed. |

All handlers receive a Flet event object. The event payload is available as `e.data`.

### Optimization modes

```python
from flet_blurhash import BlurHashOptimizationMode
```

| Mode | Description |
| --- | --- |
| `NONE` | Original algorithm. Kept for backward compatibility. |
| `STANDARD` | Optimized decoding with better cache locality and performance. |
| `APPROXIMATION` | Fastest mode. Uses an approximated sRGB conversion; slightly darker but significantly faster. |

## 🎬 Demo

<video src="assets/screen.mp4" width="600" controls autoplay loop muted>
  Your browser does not support the video tag.
</video>

[Open the demo video](assets/screen.mp4)

## 🛠️ Development

```bash
# Run the example app
just run

# Build the example app
just build linux
just build web
just build apk

# Run Python tests
uv run --group test pytest -q

# Check the Flutter extension
cd src/flutter/flet_blurhash
flutter pub get
dart analyze
```

The example app lives in `examples/flet_blurhash_example/` and uses this library
through an editable path dependency.

## 📄 License

MIT. See [LICENSE](LICENSE).
