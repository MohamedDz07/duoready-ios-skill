import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]

class SkillFormatTests(unittest.TestCase):
    def test_skill_frontmatter(self):
        content = (ROOT / "skills/duoready/SKILL.md").read_text()
        self.assertRegex(content, r"\A---\nname: duoready\ndescription: .+\n---\n")

    def test_required_files(self):
        for relative in ["README.md", "LICENSE", "CONTRIBUTING.md", "skills/duoready/SKILL.md", "skills/duoready/scripts/audit_swiftui.py", "skills/duoready/scripts/audit.sh", "skills/duoready/scripts/check_sdk.sh", "skills/duoready/agents/openai.yaml", "skills/duoready/assets/DuoLayoutProbe.swift", "evals/evals.json", "evals/grade.py"]:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_skill_references_are_linked(self):
        skill = (ROOT / "skills/duoready/SKILL.md").read_text()
        for name in ["api-reference.md", "arrangement-views.md", "reserved-regions.md", "vertical-controls.md", "split-views.md", "camera-and-scenes.md", "device-and-metrics.md", "verification.md", "audit-checklist.md", "simulator-verification.md"]:
            self.assertIn(name, skill)

if __name__ == "__main__":
    unittest.main()
