import SwiftUI

@available(iOS 17.0, *)
struct AdaptiveLayoutExample: View {
    var body: some View {
        NavigationSplitView {
            List { Text("Primary") }.navigationTitle("Items")
        } detail: {
            ContentUnavailableView("Select an item", systemImage: "rectangle.split.2x1")
        }
        .navigationSplitViewStyle(.balanced)
    }
}
