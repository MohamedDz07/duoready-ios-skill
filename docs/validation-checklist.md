# Validation checklist

Use this checklist before describing an adaptation as verified.

- Record Xcode version, iOS SDK, deployment target, runtime, device or simulator, and orientation.
- Run the repository tests and the source audit.
- Test compact, regular, wide, and short-height windows where the target supports them.
- Test Dynamic Type, VoiceOver focus order, keyboard presentation, RTL, and reduced motion.
- Test scene reconnect, background/foreground, state restoration, and multiple scene instances where applicable.
- Test split view and any reserved-region or arrangement behavior only when the installed SDK exposes the APIs.
- For hardware claims, record hardware model, OS build, pose, and whether the result differs from the simulator.

Passing this checklist does not prove every layout is correct; it records the scope of validation.
