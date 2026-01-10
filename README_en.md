# 🖼️ FLET BLUR HASH

![PyPI - Downloads](https://img.shields.io/pypi/dw/flet-blurhash)
![PyPI - Version](https://img.shields.io/pypi/v/flet-blurhash)

#### [id_translate](README.md)


**flet-blurhash** is a **BlurHash implementation for Flet**, inspired by **BlurHash in Flutter**.
This library allows you to display **blurred placeholders** before the actual image finishes loading, making your UI feel smoother and more professional.

## ✨ Key Features

* 🚀 **Fast BlurHash rendering**
* 🖼️ Displays placeholders while images are loading
* ⏳ Smooth transition animations to the original image
* 🔌 Seamlessly integrated as a **Flet custom control**
* 💙 Simple API, following Flutter-like concepts
* 🖥️ Support multi-platform:
    * Android 🟢
    * Linux 🟢
    * Windows (untested)
    * macOS (untested)
    * Web 🟢


## 📦 Installation

```bash
uv add flet-blurhash
```

## 🤖 Requirements

* **Python** `3.12`
* **Flet** `0.80.0`

> [!WARNING]
> ⚠️ This library is not compatible with Python versions below `3.12` or Flet versions other than `0.80.0`.

## 🚀 Usage Example

> [!NOTE]
> You can generate hashes from [blurha.sh](https://blurha.sh/)

```python
import flet as ft
from flet_blurhash import BlurHashOptimizationMode, FletBlurHash

def main(page: ft.Page):
    def display(e):
        print("display: ", e.data)

    page.add(
        ft.Container(
            height=400,
            width=400,
            content=FletBlurHash(
                hash="LKO2:N%2Tw=w]~RBVZRi};RPxuwH",
                image="https://fastly.picsum.photos/id/21/3008/2008.jpg?hmac=T8DSVNvP-QldCew7WD4jj_S3mWwxZPqdF0CNPksSko4",
                duration=ft.Duration(seconds=3),
                on_display=display,
                curve=ft.AnimationCurve.BOUNCE_IN,
                optimization_mode=BlurHashOptimizationMode.APPROXIMATION,
            ),
        )
    )

ft.run(main)
```

## 📺️ What you get

<video src="assets/sreen.mp4" width="400" height=200 autoplay loop muted controls>
  video
</video>


<p align="center">Hope this project is useful for you! 🥰</p>