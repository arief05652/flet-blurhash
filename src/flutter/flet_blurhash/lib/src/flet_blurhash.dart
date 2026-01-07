import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import "package:flutter_blurhash/flutter_blurhash.dart";

class FletBlurhashControl extends StatelessWidget {
  final Control control;

  const FletBlurhashControl({
    super.key,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    control.notifyParent = true;

    // attr
    var hash = control.getString("hash")!;
    var color = control.getColor("color", context, Colors.grey)!;
    var imageFit = control.getBoxFit("image_fit", BoxFit.fill)!;
    var image = control.getString("image");
    var duration =
        control.getDuration("duration", Duration(milliseconds: 1000))!;
    var curve = control.getCurve("curve", Curves.easeOut)!;
    var optimizationMode = control.getString("optimization_mode");
    var errorContent = control.buildWidget("error_content");

    var backend = FletBackend.of(context);

    Widget _blurHash() {
      try {
        return BlurHash(
          hash: hash,
          color: color,
          imageFit: imageFit,
          image: image,
          duration: duration,
          curve: curve,
          optimizationMode: _optimizationMode(optimizationMode),
          onDecoded: () =>
              backend.triggerControlEvent(control, "decode", "decode running!"),
          onDisplayed: () => backend.triggerControlEvent(
              control, "display", "display running!"),
          onReady: () =>
              backend.triggerControlEvent(control, "ready", "ready running!"),
          onStarted: () =>
              backend.triggerControlEvent(control, "start", "start running!"),
        );
      } catch (e) {
        return errorContent ?? ErrorControl("something is wrong: $e");
      }
    }

    return LayoutControl(
      control: control,
      child: _blurHash(),
    );
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
