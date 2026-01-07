import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

import 'flet_blurhash.dart';

class Extension extends FletExtension {
  @override
  Widget? createWidget(Key? key, Control control) {
    switch (control.type) {
      case "FletBlurHash":
        return FletBlurhashControl(control: control);
      default:
        return null;
    }
  }
}
