import unittest

from main import clean_text, detect_skills


class TestTextCleaning(unittest.TestCase):
    def test_removes_blank_lines_and_extra_spaces(self):
        raw_text = "  Python   developer  \n\n  SQL   skills \n"
        self.assertEqual(clean_text(raw_text), "Python developer SQL skills")

    def test_empty_text_stays_empty(self):
        self.assertEqual(clean_text(" \n \n"), "")


class TestSkillDetection(unittest.TestCase):
    def test_detects_skills_without_case_sensitivity(self):
        text = "I have PYTHON experience and use sql."
        self.assertEqual(detect_skills(text, ["Python", "SQL"]), ["Python", "SQL"])

    def test_does_not_match_skill_inside_a_longer_word(self):
        text = "I enjoy pythonista communities."
        self.assertEqual(detect_skills(text, ["Python"]), [])


if __name__ == "__main__":
    unittest.main()
