# Device and metrics

Do not publish exact device dimensions, hinge widths, safe-area values, or pose-specific measurements unless they were captured with a named Xcode/runtime/device configuration and a reproducible probe.

For a measurement report, record:

- Xcode and SDK versions;
- simulator runtime or hardware OS build;
- device pose and orientation;
- coordinate space and scale;
- window bounds, safe-area insets, and region frames;
- whether the value was observed once or reproduced.

Until those fields exist, describe geometry qualitatively and use container size, size classes, and system safe areas.
