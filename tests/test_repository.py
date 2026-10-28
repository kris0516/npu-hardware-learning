import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class RepositoryStructureTest(unittest.TestCase):
    def test_learning_structure_exists(self):
        for path in ("README.md", "LICENSE", ".gitignore", "projects", "notebooks", "docs", "rtl", "tests"):
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).exists())
