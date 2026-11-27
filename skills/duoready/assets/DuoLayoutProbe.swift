import SwiftUI

/// Optional DEBUG-only probe. It reports ordinary geometry; Duo-specific region
/// queries must be added only after the installed SDK confirms their spelling.
@available(iOS 17.0, *)
struct DuoLayoutProbe<Content: View>: View {
    let label: String
    @ViewBuilder let content: () -> Content

    var body: some View {
        content()
            .background {
                GeometryReader { proxy in
                    Color.clear
                        .onAppear { log(proxy.size) }
                        .onChange(of: proxy.size) { _, size in log(size) }
                }
            }
    }

    private func log(_ size: CGSize) {
        #if DEBUG
        print("DuoLayoutProbe[\(label)] size=\(size.width)x\(size.height)")
        #endif
    }
}
