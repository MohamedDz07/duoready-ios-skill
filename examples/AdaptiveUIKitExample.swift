import UIKit

@available(iOS 14.0, *)
final class AdaptiveSplitViewController: UISplitViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        setViewController(UINavigationController(rootViewController: UIViewController()), for: .primary)
        setViewController(UINavigationController(rootViewController: UIViewController()), for: .secondary)
        preferredSplitBehavior = .tile
    }
}
