import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_blurhash/flutter_blurhash.dart';

class FletBlurhashControl extends StatelessWidget {
  final Control control;

  const FletBlurhashControl({
    super.key,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    control.notifyParent = true;

    final backend = FletBackend.of(context);

    Widget child;
    try {
      child = BlurHash(
        hash: control.getString("hash")!,
        color: control.getColor("color", context, Colors.grey)!,
        imageFit: control.getBoxFit("image_fit", BoxFit.fill)!,
        image: control.getString("image"),
        duration: control.getDuration(
          "duration",
          const Duration(milliseconds: 1000),
        )!,
        curve: control.getCurve("curve", Curves.easeOut)!,
        optimizationMode: _optimizationMode(
          control.getString("optimization_mode"),
        ),
        onDecoded: () =>
            backend.triggerControlEvent(control, "decode", "decode running!"),
        onDisplayed: () => backend.triggerControlEvent(
          control,
          "display",
          "display running!",
        ),
        onReady: () =>
            backend.triggerControlEvent(control, "ready", "ready running!"),
        onStarted: () =>
            backend.triggerControlEvent(control, "start", "start running!"),
      );
    } catch (e) {
      child = control.buildWidget("error_content") ??
          ErrorControl("something is wrong: $e");
    }

    return LayoutControl(control: control, child: child);
  }
}

BlurHashOptimizationMode _optimizationMode(String? type) {
  switch (type) {
    case "none":
      return BlurHashOptimizationMode.none;
    case "standard":
      return BlurHashOptimizationMode.standard;
    case "approximation":
      return BlurHashOptimizationMode.approximation;
    default:
      return BlurHashOptimizationMode.none;
  }
}
