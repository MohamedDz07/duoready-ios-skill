# Split views and navigation

Use `NavigationSplitView` or `UISplitViewController` when selection or navigation drives a primary and secondary column. Let the system collapse or expand the hierarchy as the window changes.

Do not swap navigation containers solely because the device changed pose. Preserve selection and navigation state, and test deep links, sheets, back navigation, state restoration, and an empty detail state.

An arrangement can sit inside a navigated detail view when the detail itself has two related panes, but navigation remains outside the arrangement.
