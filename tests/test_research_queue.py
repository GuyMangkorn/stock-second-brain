import json
import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
QUEUE_SCRIPT = PROJECT_ROOT / "scripts" / "research_queue.py"


def run_queue(tmp_path: Path, *args: str) -> dict:
    result = subprocess.run(
        [sys.executable, str(QUEUE_SCRIPT), "--root", str(tmp_path), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr or result.stdout
    return json.loads(result.stdout)


def run_queue_error(tmp_path: Path, *args: str) -> tuple[int, dict]:
    result = subprocess.run(
        [sys.executable, str(QUEUE_SCRIPT), "--root", str(tmp_path), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.returncode, json.loads(result.stdout)


def read_frontmatter(path: Path) -> dict:
    lines = path.read_text().splitlines()
    assert lines[0] == "---"
    end = lines.index("---", 1)
    values = {}
    for line in lines[1:end]:
        key, value = line.split(":", 1)
        values[key] = value.strip().strip('"')
    return values


class ResearchQueueCliTests(unittest.TestCase):
    def test_single_etf_intake_creates_batch_and_ready_card(self) -> None:
        with self.subTest("single ETF intake"):
            import tempfile

            with tempfile.TemporaryDirectory() as directory:
                tmp_path = Path(directory)
                result = run_queue(
                    tmp_path, "intake", "--tickers", "VIG", "--type", "ETF"
                )

                self.assertEqual(result["status"], "Done")
                self.assertEqual(len(result["created"]), 1)
                self.assertEqual(result["created"][0]["ticker"], "VIG")
                self.assertEqual(result["created"][0]["status"], "Ready")

                cards = list((tmp_path / "research-queue" / "cards").glob("*.md"))
                batches = list((tmp_path / "research-queue" / "batches").glob("*.md"))
                self.assertEqual(len(cards), 1)
                self.assertEqual(len(batches), 1)

                card = read_frontmatter(cards[0])
                self.assertEqual(card["kind"], "research-card")
                self.assertEqual(card["status"], "Ready")
                self.assertEqual(card["workflow"], "check-etf-performance")
                self.assertEqual(card["instrument_type"], "ETF")
                self.assertEqual(card["input_ticker"], "VIG")
                self.assertEqual(card["card_id"], result["created"][0]["card_id"])

    def test_intake_forms_dry_run_and_active_duplicate_policy(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            dry_run = run_queue(
                tmp_path,
                "intake",
                "--tickers",
                "vig, DGRO, VIG",
                "--type",
                "ETF",
                "--dry-run",
            )
            self.assertTrue(dry_run["dry_run"])
            self.assertEqual(len(dry_run["created"]), 2)
            self.assertFalse((tmp_path / "research-queue").exists())

            created = run_queue(
                tmp_path,
                "intake",
                "--tickers",
                "vig, DGRO",
                "--type",
                "ETF",
            )
            duplicate = run_queue(
                tmp_path,
                "intake",
                "--tickers",
                "VIG,DGRO",
                "--type",
                "ETF",
            )
            self.assertEqual(len(created["created"]), 2)
            self.assertEqual(len(duplicate["created"]), 0)
            self.assertEqual(len(duplicate["reused"]), 2)

            card_path = tmp_path / duplicate["reused"][0]["path"]
            props = read_frontmatter(card_path)
            self.assertEqual(props["status"], "Ready")

    def test_markdown_table_requires_explicit_type_for_mixed_items(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            source = tmp_path / "watchlist.md"
            source.write_text(
                "| Ticker | Type |\n| --- | --- |\n| VIG | ETF |\n| MSFT | Stock |\n",
                encoding="utf-8",
            )
            result = run_queue(
                tmp_path,
                "intake",
                "--input-file",
                "watchlist.md",
            )
            self.assertEqual(len(result["created"]), 1)
            self.assertEqual(result["created"][0]["ticker"], "VIG")
            self.assertEqual(len(result["rejected"]), 1)
            self.assertEqual(result["rejected"][0]["code"], "unsupported-processor")

            ambiguous = tmp_path / "ambiguous.md"
            ambiguous.write_text(
                "| Ticker |\n| --- |\n| VIG |\n| MSFT |\n", encoding="utf-8"
            )
            code, error = run_queue_error(
                tmp_path,
                "intake",
                "--input-file",
                "ambiguous.md",
            )
            self.assertNotEqual(code, 0)
            self.assertEqual(error["error"]["code"], "invalid-instrument-type")

    def test_claim_renew_strict_success_and_item_block_routing(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            created = run_queue(
                tmp_path,
                "intake",
                "--tickers",
                "VIG,DGRO",
                "--type",
                "ETF",
                "--now",
                "2026-08-31T00:00:00Z",
            )
            card_id = created["created"][0]["card_id"]
            claim = run_queue(
                tmp_path,
                "claim",
                "--card-id",
                card_id,
                "--owner",
                "worker-a",
                "--now",
                "2026-08-31T00:00:01Z",
            )
            renewed = run_queue(
                tmp_path,
                "renew",
                "--card-id",
                card_id,
                "--owner",
                "worker-a",
                "--fencing-token",
                claim["fencing_token"],
                "--phase",
                "pre-write",
                "--now",
                "2026-08-31T01:00:00Z",
            )
            self.assertEqual(renewed["execution_phase"], "pre-write")

            output = tmp_path / "result.md"
            output.write_text("# VIG result\n", encoding="utf-8")
            handoff = json.dumps(
                {
                    "status": "PASS",
                    "scope": "item",
                    "durable_write": "completed",
                    "exhausted": False,
                    "confirmation": "none",
                    "code": "success",
                    "reason": "Durable ETF performance outputs were written.",
                }
            )
            routed = run_queue(
                tmp_path,
                "route",
                "--card-id",
                card_id,
                "--owner",
                "worker-a",
                "--fencing-token",
                claim["fencing_token"],
                "--handoff-json",
                handoff,
                "--output",
                "result.md",
                "--now",
                "2026-08-31T01:00:01Z",
            )
            self.assertEqual(routed["status"], "Done")
            card = read_frontmatter(tmp_path / "research-queue" / "cards" / f"{card_id}.md")
            self.assertEqual(card["status"], "Done")
            self.assertIn("result.md", card["output_paths"])

            blocked_id = created["created"][1]["card_id"]
            blocked_claim = run_queue(
                tmp_path,
                "claim",
                "--card-id",
                blocked_id,
                "--owner",
                "worker-a",
                "--now",
                "2026-08-31T00:00:01Z",
            )
            item_block = run_queue(
                tmp_path,
                "route",
                "--card-id",
                blocked_id,
                "--owner",
                "worker-a",
                "--fencing-token",
                blocked_claim["fencing_token"],
                "--handoff-json",
                json.dumps(
                    {
                        "status": "BLOCKED",
                        "scope": "item",
                        "durable_write": "not_completed",
                        "exhausted": True,
                        "confirmation": "none",
                        "code": "item-hard-data-gap",
                        "reason": "Official source history is incomplete.",
                    }
                ),
                "--now",
                "2026-08-31T00:00:02Z",
            )
            self.assertEqual(item_block["status"], "Blocked")
            self.assertFalse(item_block["global_blocked"])

    def test_expired_claim_recovery_and_stale_fencing(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            created = run_queue(
                tmp_path,
                "intake",
                "--tickers",
                "VIG,DGRO",
                "--type",
                "ETF",
                "--now",
                "2026-08-31T00:00:00Z",
            )
            safe_id = created["created"][0]["card_id"]
            partial_id = created["created"][1]["card_id"]
            safe = run_queue(
                tmp_path,
                "claim",
                "--card-id",
                safe_id,
                "--owner",
                "worker-a",
                "--now",
                "2026-08-31T00:00:01Z",
            )
            partial = run_queue(
                tmp_path,
                "claim",
                "--card-id",
                partial_id,
                "--owner",
                "worker-a",
                "--phase",
                "writing",
                "--now",
                "2026-08-31T00:00:01Z",
            )
            recovery = run_queue(tmp_path, "recover", "--now", "2026-08-31T02:00:02Z")
            self.assertEqual(recovery["recovered_ready"][0]["card_id"], safe_id)
            self.assertEqual(recovery["blocked_partial"][0]["card_id"], partial_id)

            code, error = run_queue_error(
                tmp_path,
                "renew",
                "--card-id",
                safe_id,
                "--owner",
                "worker-a",
                "--fencing-token",
                safe["fencing_token"],
                "--now",
                "2026-08-31T02:00:03Z",
            )
            self.assertNotEqual(code, 0)
            self.assertEqual(error["error"]["code"], "claim-state-error")

            blocked = read_frontmatter(tmp_path / "research-queue" / "cards" / f"{partial_id}.md")
            self.assertEqual(blocked["result_code"], "partial-write-recovery")

    def test_manager_processes_sequentially_and_commits_only_card_scope(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
            subprocess.run(["git", "config", "user.email", "queue@example.test"], cwd=tmp_path, check=True)
            subprocess.run(["git", "config", "user.name", "Queue Test"], cwd=tmp_path, check=True)
            baseline = tmp_path / "baseline.md"
            baseline.write_text("baseline\n", encoding="utf-8")
            subprocess.run(["git", "add", "baseline.md"], cwd=tmp_path, check=True)
            subprocess.run(["git", "commit", "-qm", "baseline"], cwd=tmp_path, check=True)

            created = run_queue(
                tmp_path,
                "intake",
                "--tickers",
                "VIG,DGRO",
                "--type",
                "ETF",
                "--now",
                "2026-08-31T00:00:00Z",
            )
            unrelated = tmp_path / "unrelated.md"
            unrelated.write_text("human edit\n", encoding="utf-8")
            output = tmp_path / "result.md"
            output.write_text("# result\n", encoding="utf-8")
            handoff = json.dumps(
                {
                    "status": "PASS",
                    "scope": "item",
                    "durable_write": "completed",
                    "exhausted": False,
                    "confirmation": "none",
                    "code": "durable-write-complete",
                    "reason": "Output was written and verified.",
                }
            )
            processed = run_queue(
                tmp_path,
                "process",
                "--count",
                "1",
                "--owner",
                "manager-a",
                "--execution-profile",
                "scheduled-inline",
                "--handoff-json",
                handoff,
                "--output",
                "result.md",
                "--commit",
                "--now",
                "2026-08-31T00:00:01Z",
            )
            self.assertEqual(processed["attempted"], [created["created"][0]["card_id"]])
            self.assertEqual(processed["completed"], [created["created"][0]["card_id"]])
            self.assertEqual(processed["blocked"], [])
            self.assertIsNone(processed["global_failure"])

            status = subprocess.run(
                ["git", "status", "--short"],
                cwd=tmp_path,
                check=True,
                capture_output=True,
                text=True,
            ).stdout
            self.assertIn("?? unrelated.md", status)
            self.assertNotIn("result.md", status)
            first_card_path = f"research-queue/cards/{created['created'][0]['card_id']}.md"
            self.assertNotIn(first_card_path, status)
            log = subprocess.run(
                ["git", "log", "--oneline", "--format=%s", "-1"],
                cwd=tmp_path,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            self.assertIn("research: complete VIG", log)

    def test_invalid_handoff_is_known_card_global_stop(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            created = run_queue(tmp_path, "intake", "--tickers", "VIG", "--type", "ETF")
            card_id = created["created"][0]["card_id"]
            claim = run_queue(tmp_path, "claim", "--card-id", card_id, "--owner", "worker-a")
            result = run_queue(
                tmp_path,
                "route",
                "--card-id",
                card_id,
                "--owner",
                "worker-a",
                "--fencing-token",
                claim["fencing_token"],
                "--handoff-json",
                json.dumps({"status": "PASS"}),
            )
            self.assertEqual(result["status"], "Blocked")
            self.assertTrue(result["global_blocked"])
            card = read_frontmatter(tmp_path / "research-queue" / "cards" / f"{card_id}.md")
            self.assertEqual(card["result_code"], "unknown-result")

    def test_human_hold_unblock_cancel_and_project_lease_overlap(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            created = run_queue(tmp_path, "intake", "--tickers", "VIG", "--type", "ETF")
            card_id = created["created"][0]["card_id"]
            held = run_queue(tmp_path, "hold", "--card-id", card_id, "--reason", "Need source confirmation")
            self.assertEqual(held["status"], "Blocked")
            unblocked = run_queue(tmp_path, "unblock", "--card-id", card_id)
            self.assertEqual(unblocked["status"], "Ready")
            cancelled = run_queue(tmp_path, "cancel", "--card-id", card_id)
            self.assertEqual(cancelled["status"], "Cancelled")
            code, error = run_queue_error(tmp_path, "unblock", "--card-id", card_id)
            self.assertNotEqual(code, 0)
            self.assertEqual(error["error"]["code"], "invalid-transition")

            import sys
            sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
            from research_queue import QueueError, QueueStore, parse_time

            store = QueueStore(tmp_path)
            first = store.project_lease("first", parse_time("2026-08-31T00:00:00Z"))
            first.acquire()
            try:
                with self.assertRaises(QueueError) as raised:
                    store.project_lease("second", parse_time("2026-08-31T01:00:00Z")).acquire()
                self.assertEqual(raised.exception.code, "manager-overlap")
            finally:
                first.release()

    def test_bullets_seed_and_terminal_cards_allow_refresh(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            bullets = "- VIG\n- DGRO (ETF)\n"
            seeded = run_queue(
                tmp_path,
                "seed",
                "--tickers",
                "VIG,DGRO",
                "--type",
                "ETF",
            )
            self.assertEqual(seeded["status"], "Done")
            self.assertTrue(seeded["batch_id"].startswith("rb-"))
            card_id = seeded["created"][0]["card_id"]
            claim = run_queue(tmp_path, "claim", "--card-id", card_id, "--owner", "worker-a")
            done = run_queue(
                tmp_path,
                "route",
                "--card-id",
                card_id,
                "--owner",
                "worker-a",
                "--fencing-token",
                claim["fencing_token"],
                "--handoff-json",
                json.dumps(
                    {
                        "status": "PASS",
                        "scope": "item",
                        "durable_write": "completed",
                        "exhausted": False,
                        "confirmation": "none",
                        "code": "success",
                        "reason": "Durable output complete.",
                    }
                ),
            )
            self.assertEqual(done["status"], "Done")
            refreshed = run_queue(
                tmp_path,
                "intake",
                "--tickers",
                "VIG",
                "--type",
                "ETF",
            )
            self.assertEqual(len(refreshed["created"]), 1)
            self.assertNotEqual(refreshed["created"][0]["card_id"], card_id)

            parsed = run_queue(
                tmp_path,
                "intake",
                "--tickers",
                bullets,
                "--type",
                "ETF",
                "--dry-run",
            )
            self.assertEqual(
                [item["ticker"] for item in parsed["created"] + parsed["reused"]],
                ["VIG", "DGRO"],
            )
