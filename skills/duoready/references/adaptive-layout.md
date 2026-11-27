# Adaptive layout patterns

Use the available window and environment as inputs, not a device model name.

```swift
struct ContentView: View {
    @Environment(\.horizontalSizeClass) private var widthClass

    var body: some View {
        NavigationSplitView { Sidebar() } detail: { Detail() }
            .frame(maxWidth: 1200)
    }
}
```

This demonstrates stable system containers and a content cap; it is not evidence that any Duo-only API is available.
