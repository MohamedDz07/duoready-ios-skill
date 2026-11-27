# Audit checklist

Use this reading order for an existing app:

1. Confirm deployment targets, supported orientations, scene configuration, and navigation containers.
2. Search for screen bounds, device-model checks, fixed frames, manual offsets, and hard-coded safe-area values.
3. Inspect centered content, full-width controls, grids, and hero heights at compact and wide-short sizes.
4. Check whether toolbars, tab bars, sheets, and custom button stacks remain reachable when space becomes asymmetric.
5. Separate navigation problems from two-pane layout problems before choosing a container.
6. Check media and camera assumptions for multiple windows and display changes.
7. Record evidence and label each conclusion as source, compile, or behavior evidence.

The checklist identifies risk; it does not establish that a layout is broken.
