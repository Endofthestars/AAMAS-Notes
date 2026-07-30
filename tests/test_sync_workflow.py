from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/sync-paper-notes-docs.yml"


class PaperNotesSyncWorkflowTests(unittest.TestCase):
    def test_scheduled_workflow_uses_safe_merge_and_deploy_flow(self) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn('cron: "41 6 * * *"', workflow)
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("PAPER_NOTES_CACHE_DIR: ${{ runner.temp }}/paper-notes-upstream", workflow)
        self.assertIn("bash scripts/sync_paper_notes_docs.sh", workflow)
        self.assertIn("python3 scripts/validate_repository.py", workflow)
        self.assertIn("mkdocs build --strict", workflow)
        self.assertIn("automation/paper-notes-docs-sync", workflow)
        self.assertIn("git push --force-with-lease", workflow)
        self.assertIn("gh pr create", workflow)
        self.assertIn('gh pr merge "$PR_URL"', workflow)
        self.assertIn("--squash --delete-branch", workflow)
        self.assertIn("gh workflow run validate.yml", workflow)
        self.assertIn("gh workflow run deploy-pages.yml", workflow)
        self.assertNotIn("git push origin HEAD:main", workflow)


if __name__ == "__main__":
    unittest.main()
