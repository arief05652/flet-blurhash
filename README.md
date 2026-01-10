# 🖼️ FLET BLUR HASH

![PyPI - Downloads](https://img.shields.io/pypi/dw/flet-blurhash)
![PyPI - Version](https://img.shields.io/pypi/v/flet-blurhash)


#### [en_translate](README_en.md)

**flet-blurhash** adalah implementasi **BlurHash untuk Flet**, terinspirasi dari **BlurHash di Flutter**.
Library ini memungkinkan kamu menampilkan **placeholder blur** sebelum gambar asli selesai dimuat, sehingga UI terasa lebih halus dan profesional.


## ✨ Fitur Utama

* 🚀 **BlurHash rendering cepat**
* 🖼️ Menampilkan placeholder sebelum image selesai load
* ⏳ Animasi transisi ke gambar asli
* 🔌 Terintegrasi langsung dengan **Flet custom control**
* 💙 API simpel & mirip konsep Flutter
* 🖥️ Support multi-platform:
    * Android 🟢
    * Linux 🟢
    * Windows (untested)
    * macOS (untested)
    * Web 🟢

## 📦 Instalasi

```bash
uv add flet-blurhash
```

## 🤖 Requirements

* **Python** `3.12`
* **Flet** `0.80.0`

> [!WARNING]
> ⚠️ Library ini tidak kompatibel dengan Python versi di bawah `3.12` atau Flet versi selain `0.80.0`.


## 🚀 Contoh Penggunaan

> [!NOTE]
> Kamu bisa mendapatkan hash dari web ini [blura.sh](https://blurha.sh/)

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


<p align="center">Semoga project ini bermanfaat 🥰</p>
