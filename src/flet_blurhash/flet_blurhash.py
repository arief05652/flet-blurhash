from dataclasses import field
from enum import Enum

import flet as ft


class BlurHashOptimizationMode(Enum):
    NONE = "none"
    """
    The original algorithm, provided for backward compatibility.
    """

    STANDARD = "standard"
    """
    Optimized decoding with better cache locality and performance.
    """

    APPROXIMATION = "approximation"
    """
    Fastest mode with an approximated sRGB conversion that produces slightly
    darker results but significantly improves performance.
    """


@ft.control("FletBlurHash")
class FletBlurHash(ft.LayoutControl):
    """
    You can display images smoothly with this class.

    Example:
        ```python
        FletBlurHash(
            hash="LKO2:N%2Tw=w]~RBVZRi};RPxuwH",
            image="https://fastly.picsum.photos/id/21/3008/2008.jpg?hmac=T8DSVNvP-QldCew7WD4jj_S3mWwxZPqdF0CNPksSko4",
            duration=ft.Duration(seconds=3),
            on_display=display,
            curve=ft.AnimationCurve.BOUNCE_IN,
            optimization_mode=BlurHashOptimizationMode.APPROXIMATION,
        )
        ```
    """

    hash: str
    """
    Enter the hash result you got from this website `https://blurha.sh/`.
    """

    color: ft.ColorValue = ft.Colors.GREY
    image_fit: ft.BoxFit = ft.BoxFit.FILL
    duration: ft.DurationValue = field(
        default_factory=lambda: ft.Duration(milliseconds=1000)
    )
    curve: ft.AnimationCurve = ft.AnimationCurve.EASE_OUT
    optimization_mode: BlurHashOptimizationMode = BlurHashOptimizationMode.NONE
    image: str | None = None
    """
    Enter the link of the image you want to display.
    """

    on_decode: ft.ControlEventHandler["FletBlurHash"] | None = None
    on_display: ft.ControlEventHandler["FletBlurHash"] | None = None
    on_ready: ft.ControlEventHandler["FletBlurHash"] | None = None
    on_start: ft.ControlEventHandler["FletBlurHash"] | None = None
    # error
    error_content: ft.Control | None = None
