from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_repository",
    ROOT / "scripts" / "validate_repository.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

SYNC_SPEC = importlib.util.spec_from_file_location(
    "sync_dblp",
    ROOT / "scripts" / "sync_dblp.py",
)
assert SYNC_SPEC and SYNC_SPEC.loader
SYNC_MODULE = importlib.util.module_from_spec(SYNC_SPEC)
SYNC_SPEC.loader.exec_module(SYNC_MODULE)


class RepositoryTest(unittest.TestCase):
    def test_repository_invariants(self) -> None:
        self.assertEqual(MODULE.validate(), [])

    def test_sources_cover_initial_window(self) -> None:
        sources = MODULE.load_json(ROOT / "data" / "sources.json")["sources"]
        self.assertEqual({source["year"] for source in sources}, {2022, 2023, 2024, 2025, 2026})

    def test_dblp_page_url_overrides_paging_fields(self) -> None:
        url = SYNC_MODULE.page_url(
            "https://dblp.org/search/publ/api?q=example&h=1000&format=json",
            200,
        )
        self.assertIn("h=100", url)
        self.assertIn("f=200", url)
        self.assertIn("format=json", url)

    def test_dblp_hit_normalization_starts_unreviewed(self) -> None:
        record = SYNC_MODULE.normalize_hit(
            {
                "info": {
                    "authors": {"author": [{"text": "Ada Agent"}, {"text": "Max Planner"}]},
                    "title": "A Reliable Multi-Agent Planner.",
                    "year": "2025",
                    "pages": "10-19",
                    "key": "conf/ifaamas/AgentPlanner25",
                    "doi": "10.0000/example",
                    "ee": "https://doi.org/10.0000/example",
                    "url": "db/conf/ifaamas/AgentPlanner25",
                }
            },
            2025,
        )
        assert record is not None
        self.assertEqual(record["authors"], ["Ada Agent", "Max Planner"])
        self.assertEqual(record["note_status"], "metadata_only")
        self.assertEqual(record["topics"], ["unclassified"])
        self.assertEqual(record["doi"], "10.0000/example")


if __name__ == "__main__":
    unittest.main()
