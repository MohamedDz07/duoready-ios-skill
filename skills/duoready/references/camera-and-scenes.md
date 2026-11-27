# Camera and scenes

Camera and multi-scene code has two independent sources of change: the active window and the capture hardware. Discover available capture devices and capabilities rather than assuming one camera, one display, or one orientation.

Keep capture-session reconfiguration separate from scene phase changes. A fold or window transition may require layout and capture updates while the scene remains active. Preserve scene identity and state when multiple instances of the app are possible.

Any camera-direction or rotation API specific to iPhone Duo must be both Apple-documented and found in the installed SDK before use. Otherwise label it unverified and provide a supported fallback.
