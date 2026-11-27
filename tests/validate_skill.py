import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).parents[1]

class SkillFormatTests(unittest.TestCase):
    def test_skill_frontmatter(self):
        content = (ROOT / "skills/duoready/SKILL.md").read_text()
        self.assertRegex(content, r"\A---\nname: duoready\ndescription: .+\n---\n")

    def test_required_files(self):
        for relative in ["README.md", "LICENSE", "skills/duoready/SKILL.md", "skills/duoready/scripts/audit_swiftui.py", "skills/duoready/scripts/check_sdk.sh"]:
            self.assertTrue((ROOT / relative).is_file(), relative)

if __name__ == "__main__":
    unittest.main()
