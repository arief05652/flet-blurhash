import dataclasses

import flet as ft
import pytest

from flet_blurhash import BlurHashOptimizationMode, FletBlurHash

HASH = "LKO2:N%2Tw=w]~RBVZRi};RPxuwH"


def test_control_type_name_matches_dart() -> None:
    assert FletBlurHash(hash=HASH)._c == "FletBlurHash"


def test_control_is_layout_control() -> None:
    assert isinstance(FletBlurHash(hash=HASH), ft.LayoutControl)


def test_hash_is_required() -> None:
    with pytest.raises(TypeError):
        FletBlurHash()  # type: ignore[call-arg]


def test_defaults() -> None:
    control = FletBlurHash(hash=HASH)

    assert control.color == ft.Colors.GREY
    assert control.image_fit == ft.BoxFit.FILL
    assert control.duration == ft.Duration(milliseconds=1000)
    assert control.curve == ft.AnimationCurve.EASE_OUT
    assert control.optimization_mode is BlurHashOptimizationMode.NONE
    assert control.image is None
    assert control.error_content is None
    assert control.on_decode is None
    assert control.on_display is None
    assert control.on_ready is None
    assert control.on_start is None


def test_duration_default_is_per_instance() -> None:
    first = FletBlurHash(hash=HASH)
    second = FletBlurHash(hash=HASH)

    assert first.duration is not second.duration

    first.duration.milliseconds = 1
    assert second.duration.milliseconds == 1000


def test_custom_values() -> None:
    def handler(event: ft.Event[FletBlurHash]) -> None:
        pass

    control = FletBlurHash(
        hash=HASH,
        color=ft.Colors.RED,
        image_fit=ft.BoxFit.CONTAIN,
        duration=ft.Duration(seconds=2),
        curve=ft.AnimationCurve.BOUNCE_IN,
        optimization_mode=BlurHashOptimizationMode.APPROXIMATION,
        image="https://example.com/image.jpg",
        on_decode=handler,
        on_display=handler,
        on_ready=handler,
        on_start=handler,
    )

    assert control.color == ft.Colors.RED
    assert control.image_fit == ft.BoxFit.CONTAIN
    assert control.duration == ft.Duration(seconds=2)
    assert control.curve == ft.AnimationCurve.BOUNCE_IN
    assert control.optimization_mode is BlurHashOptimizationMode.APPROXIMATION
    assert control.image == "https://example.com/image.jpg"
    assert control.on_decode is handler
    assert control.on_display is handler
    assert control.on_ready is handler
    assert control.on_start is handler


def test_error_content_accepts_control() -> None:
    error = ft.Text("error")

    assert FletBlurHash(hash=HASH, error_content=error).error_content is error


def test_optimization_mode_values_match_dart_contract() -> None:
    assert {mode.name: mode.value for mode in BlurHashOptimizationMode} == {
        "NONE": "none",
        "STANDARD": "standard",
        "APPROXIMATION": "approximation",
    }


def test_fields_read_by_dart_exist() -> None:
    names = {field.name for field in dataclasses.fields(FletBlurHash)}

    assert {
        "hash",
        "color",
        "image_fit",
        "duration",
        "curve",
        "optimization_mode",
        "image",
        "error_content",
        "on_decode",
        "on_display",
        "on_ready",
        "on_start",
    } <= names
