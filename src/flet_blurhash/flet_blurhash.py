from dataclasses import field
from enum import Enum
from typing import Optional

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
    curve: ft.AnimationCurve = field(default_factory=lambda: ft.AnimationCurve.EASE_OUT)
    optimization_mode: BlurHashOptimizationMode = BlurHashOptimizationMode.NONE
    image: Optional[str] = None
    """
    enter the link of the image you want to display
    """

    on_decode: Optional[ft.ControlEventHandler["FletBlurHash"]] = None
    on_display: Optional[ft.ControlEventHandler["FletBlurHash"]] = None
    on_ready: Optional[ft.ControlEventHandler["FletBlurHash"]] = None
    on_start: Optional[ft.ControlEventHandler["FletBlurHash"]] = None
    # error
    error_content: Optional[ft.Control] = None
