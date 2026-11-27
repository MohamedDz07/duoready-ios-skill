# Reserved regions

Reserved regions describe space the app should avoid for system-owned or device-specific areas such as a fold or camera occlusion. Query them only for custom-positioned content; system containers already account for many system regions.

Treat region data as dynamic. A region may appear, disappear, or change frame while the scene remains active. Do not hard-code a hinge width, camera inset, or orientation-specific coordinate.

For custom content, keep controls and text out of active division or occlusion regions, while allowing scrollable content to pass through when that is intentional and readable. Verify the exact region kinds, options, coordinate space, and availability in the SDK before writing production code.
