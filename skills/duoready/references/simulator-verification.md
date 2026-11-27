# Simulator verification

Use a named Xcode and runtime. Test the outer display, inner display, flat and partially folded states, and split-view multitasking when the environment supports them. Do not claim a pose was tested from a screenshot alone.

For every observation, record the pose, orientation, window bounds, safe-area insets, active reserved regions, and whether the result was reproduced. If Device Hub or a hardware feature is unavailable, say so and keep the result as unverified.

The repository does not include commands that create or delete simulators. Keep simulator lifecycle under the developer's control.
