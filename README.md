> [!Note]
> Documentation is currently being prepared. Please wait.


### How to use
```python
import flet as ft

from flet_blurhash import BlurHashOptimizationMode, FletBlurHash


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.always_on_top = True

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