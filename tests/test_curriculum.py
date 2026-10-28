"""Protect cross-chat course continuity without implying student mastery."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATE = ROOT / "learning" / "state.json"
STATUSES = {"not_started", "in_progress", "needs_revision", "blocked", "passed"}
PROJECTS = [
    "P01-digital-logic",
    "P02-mcu-pcb",
    "P03-rtl-datapath",
    "P04-int8-mac",
    "P05-systolic-array",
    "P06-fpga-deployment",
    "P07-tiny-mlp",
    "P08-asic-flow",
]
REQUIRED = [
    "README.md", "AGENTS.md", "docs/CURRICULUM.md",
    "docs/TEACHING_PROTOCOL.md", "docs/CROSS_CHAT.md",
    "docs/HANDOFF.md", "docs/ASSESSMENT.md",
    "docs/STATE_MODEL.md", "docs/ENVIRONMENT.md",
    "docs/RESOURCES.md", "docs/EQUIPMENT.md",
    "learning/knowledge.md", "learning/decisions.md",
    "templates/STEP_RECORD.md", "templates/LAB_REPORT.md",
    ".github/workflows/ci.yml",
]


class CurriculumIntegrityTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = json.loads(STATE.read_text(encoding="utf-8"))

    def test_required_files_exist(self):
        for path in REQUIRED:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file(), path)

    def test_projects_have_complete_curricula(self):
        for index, slug in enumerate(PROJECTS, 1):
            path = ROOT / "projects" / slug / "README.md"
            self.assertTrue(path.is_file(), str(path))
            text = path.read_text(encoding="utf-8")
            for step in range(1, 7):
                self.assertIn(f"P{index:02d}-S{step:02d}", text, str(path))

    def test_state_schema_and_pointers(self):
        state = self.state
        self.assertEqual(2, state["schema_version"])
        self.assertEqual(14, state["cadence_days"])
        projects = state["projects"]
        steps = state["steps"]
        self.assertEqual(8, len(projects))
        self.assertEqual(48, len(steps))
        self.assertEqual(PROJECTS, [p["slug"] for p in projects])
        self.assertEqual([f"P{i:02d}" for i in range(1, 9)],
                         [p["id"] for p in projects])
        expected = [f"P{i:02d}-S{j:02d}"
                    for i in range(1, 9) for j in range(1, 7)]
        self.assertEqual(expected, [step["id"] for step in steps])
        self.assertIn(state["current_project"], [p["id"] for p in projects])
        current = next(s for s in steps if s["id"] == state["current_step"])
        self.assertEqual(state["current_project"], current["project"])
        self.assertEqual(state["current_step_status"], current["status"])

    def test_status_and_pass_evidence_integrity(self):
        def check_evidence(records):
            self.assertIsInstance(records, list)
            for rel in records:
                self.assertIsInstance(rel, str)
                path = pathlib.PurePosixPath(rel)
                self.assertFalse(path.is_absolute(), rel)
                self.assertNotIn("..", path.parts, rel)
                self.assertTrue((ROOT / path).is_file(), rel)

        for step in self.state["steps"]:
            with self.subTest(step=step["id"]):
                self.assertIn(step["status"], STATUSES)
                check_evidence(step["evidence"])
                if step["status"] == "passed":
                    self.assertTrue(step["evidence"], step["id"])
                    self.assertTrue(step["passed_at"], step["id"])
                    self.assertTrue(step["review_note"], step["id"])
                elif step["status"] == "not_started":
                    self.assertFalse(step["evidence"], step["id"])
        for project in self.state["projects"]:
            with self.subTest(project=project["id"]):
                self.assertIn(project["status"], STATUSES)
                check_evidence(project["evidence"])
                related = [s for s in self.state["steps"]
                           if s["project"] == project["id"]]
                if project["status"] == "passed":
                    self.assertTrue(all(s["status"] == "passed" for s in related))
                    self.assertTrue(project["passed_at"])
                    self.assertTrue(project["evidence"])

    def test_no_out_of_order_step_pass(self):
        passed = set()
        for step in self.state["steps"]:
            if step["status"] == "passed":
                index = int(step["id"][-2:])
                if index > 1:
                    prev = f"{step['project']}-S{index - 1:02d}"
                    self.assertIn(prev, passed,
                                  f"Cannot PASS {step['id']} before {prev}")
                passed.add(step["id"])


if __name__ == "__main__":
    unittest.main()
