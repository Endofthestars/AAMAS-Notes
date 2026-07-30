from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SYNC_SCRIPT = ROOT / "scripts" / "sync_paper_notes_docs.sh"


class PaperNotesDocsSyncTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = Path(tempfile.mkdtemp(prefix="aamas-paper-notes-sync-"))
        self.upstream = self.temp_dir / "upstream"
        self.workspace = self.temp_dir / "workspace"
        self.cache = self.temp_dir / "cache"
        self.upstream.mkdir()
        self.workspace.mkdir()
        self.git("init", "--initial-branch=main")
        self.git("config", "user.name", "Test User")
        self.git("config", "user.email", "test@example.com")
        self.write_upstream(
            {
                "AAAI2026/vision/paper.md": "first",
                "ACL2025/nlp/paper.md": "acl",
                "index.md": "upstream index",
                "notes/local.md": "must not copy",
                "assets/favicon.svg": "upstream favicon",
            }
        )
        self.commit("initial")
        (self.workspace / "docs" / "notes").mkdir(parents=True)
        (self.workspace / "docs" / "notes" / "aamas.md").write_text(
            "local AAMAS note", encoding="utf-8"
        )
        (self.workspace / "docs" / "index.md").write_text(
            "local index", encoding="utf-8"
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def git(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=self.upstream,
            check=True,
            capture_output=True,
            text=True,
        )

    def write_upstream(self, files: dict[str, str]) -> None:
        docs = self.upstream / "docs"
        if docs.exists():
            shutil.rmtree(docs)
        for relative, content in files.items():
            path = docs / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        (self.upstream / "LICENSE").write_text(
            "CC BY-NC-SA 4.0\n", encoding="utf-8"
        )

    def commit(self, message: str) -> None:
        self.git("add", "-A")
        self.git("commit", "-m", message)

    def sync(
        self,
        *,
        force: bool = False,
        max_file_bytes: int | None = None,
    ) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env.update(
            {
                "PAPER_NOTES_UPSTREAM_URL": str(self.upstream),
                "PAPER_NOTES_CACHE_DIR": str(self.cache),
                "PAPER_NOTES_FORCE_SYNC": "1" if force else "0",
            }
        )
        if max_file_bytes is not None:
            env["PAPER_NOTES_MAX_FILE_BYTES"] = str(max_file_bytes)
        return subprocess.run(
            ["bash", str(SYNC_SCRIPT)],
            cwd=self.workspace,
            env=env,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_merges_conference_dirs_and_protects_local_docs(self) -> None:
        result = self.sync()
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(
            "first",
            (self.workspace / "docs/AAAI2026/vision/paper.md").read_text(),
        )
        self.assertEqual("local index", (self.workspace / "docs/index.md").read_text())
        self.assertEqual(
            "local AAMAS note",
            (self.workspace / "docs/notes/aamas.md").read_text(),
        )
        self.assertFalse((self.workspace / "docs/assets/favicon.svg").exists())
        self.assertIn(
            "upstream_commit:",
            (
                self.workspace / "data/provenance/PAPER_NOTES_UPSTREAM.md"
            ).read_text(),
        )
        self.assertEqual(
            ["AAAI2026", "ACL2025"],
            (
                self.workspace
                / "data/provenance/PAPER_NOTES_UPSTREAM_DIRS.txt"
            ).read_text().splitlines(),
        )

    def test_updates_and_deletes_only_managed_conference_dirs(self) -> None:
        self.assertEqual(0, self.sync().returncode)
        self.write_upstream(
            {
                "AAAI2026/vision/new.md": "updated",
                "ICML2026/ml/paper.md": "new conference",
            }
        )
        self.commit("replace docs")
        result = self.sync()
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertFalse((self.workspace / "docs/ACL2025").exists())
        self.assertFalse(
            (self.workspace / "docs/AAAI2026/vision/paper.md").exists()
        )
        self.assertEqual(
            "updated",
            (self.workspace / "docs/AAAI2026/vision/new.md").read_text(),
        )
        self.assertEqual(
            "new conference",
            (self.workspace / "docs/ICML2026/ml/paper.md").read_text(),
        )

    def test_unchanged_revision_is_noop(self) -> None:
        self.assertEqual(0, self.sync().returncode)
        state = self.workspace / "data/provenance/PAPER_NOTES_UPSTREAM.md"
        before = state.read_bytes()
        result = self.sync()
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("already current", result.stdout)
        self.assertEqual(before, state.read_bytes())

    def test_refuses_unmanaged_directory_collision(self) -> None:
        (self.workspace / "docs/AAAI2026").mkdir()
        marker = self.workspace / "docs/AAAI2026/local.md"
        marker.write_text("local", encoding="utf-8")
        result = self.sync()
        self.assertNotEqual(0, result.returncode)
        self.assertIn("unmanaged local directory", result.stderr)
        self.assertEqual("local", marker.read_text())

    def test_oversized_file_fails_before_modifying_docs(self) -> None:
        marker = self.workspace / "docs/index.md"
        result = self.sync(max_file_bytes=2)
        self.assertNotEqual(0, result.returncode)
        self.assertIn("oversized file", result.stderr)
        self.assertEqual("local index", marker.read_text())
        self.assertFalse((self.workspace / "docs/AAAI2026").exists())


if __name__ == "__main__":
    unittest.main()
