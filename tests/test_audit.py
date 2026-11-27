import importlib.util
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).parents[1]
SPEC = importlib.util.spec_from_file_location("audit", ROOT / "skills/duoready/scripts/audit_swiftui.py")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)

class AuditTests(unittest.TestCase):
    def test_reports_fixed_frame(self):
        with tempfile.TemporaryDirectory() as folder:
            path = pathlib.Path(folder) / "View.swift"
            path.write_text('Text("x").frame(width: 390)\n')
            self.assertEqual([item["rule"] for item in AUDIT.scan(pathlib.Path(folder))], ["fixed-frame"])

    def test_ignores_non_swift_files(self):
        with tempfile.TemporaryDirectory() as folder:
            pathlib.Path(folder, "README.md").write_text("UIScreen.main.bounds")
            self.assertEqual(list(AUDIT.scan(pathlib.Path(folder))), [])

if __name__ == "__main__":
    unittest.main()
