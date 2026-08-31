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
    def test_obsidian_views_use_frontmatter_status_and_base_board_kanban(self) -> None:
        intake = (PROJECT_ROOT / "research-queue" / "Research Queue Intake.base").read_text(encoding="utf-8")
        monitor = (PROJECT_ROOT / "research-queue" / "Research Queue Monitor.base").read_text(encoding="utf-8")
        self.assertIn("type: kanban", intake)
        self.assertIn("property: note.status", intake)
        self.assertNotIn("type: cards", intake)
        self.assertIn("type: table", monitor)
        self.assertIn("status", monitor)

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

            blank_type = tmp_path / "blank-type.md"
            blank_type.write_text(
                "| Ticker | Type |\n| --- | --- |\n| VIG |  |\n",
                encoding="utf-8",
            )
            code, error = run_queue_error(
                tmp_path,
                "intake",
                "--input-file",
                "blank-type.md",
                "--type",
                "ETF",
            )
            self.assertNotEqual(code, 0)
            self.assertEqual(error["error"]["code"], "invalid-instrument-type")

    def test_claim_renew_strict_success_and_item_block_routing(self) -> None:
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
                "--output",
                "wiki/result.md",
                "--now",
                "2026-08-31T01:00:00Z",
            )
            self.assertEqual(renewed["execution_phase"], "pre-write")

            (tmp_path / "wiki").mkdir()
            output = tmp_path / "wiki" / "result.md"
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
                "wiki/result.md",
                "--now",
                "2026-08-31T01:00:01Z",
                "--commit",
            )
            self.assertEqual(routed["status"], "Done")
            card = read_frontmatter(tmp_path / "research-queue" / "cards" / f"{card_id}.md")
            self.assertEqual(card["status"], "Done")
            self.assertIn("wiki/result.md", card["output_paths"])

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

            missing_output = run_queue(tmp_path, "intake", "--tickers", "IXUS", "--type", "ETF")
            missing_id = missing_output["created"][0]["card_id"]
            missing_claim = run_queue(tmp_path, "claim", "--card-id", missing_id, "--owner", "worker-a")
            strict_without_output = run_queue(
                tmp_path,
                "route",
                "--card-id",
                missing_id,
                "--owner",
                "worker-a",
                "--fencing-token",
                missing_claim["fencing_token"],
                "--handoff-json",
                handoff,
            )
            self.assertEqual(strict_without_output["status"], "Blocked")
            self.assertEqual(strict_without_output["result_code"], "durable-output-required")

    def test_expired_claim_recovery_and_stale_fencing(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            created = run_queue(
                tmp_path,
                "intake",
                "--tickers",
                "VIG,DGRO,IXUS",
                "--type",
                "ETF",
                "--now",
                "2026-08-31T00:00:00Z",
            )
            safe_id = created["created"][0]["card_id"]
            partial_id = created["created"][1]["card_id"]
            unknown_id = created["created"][2]["card_id"]
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
            unknown = run_queue(
                tmp_path,
                "claim",
                "--card-id",
                unknown_id,
                "--owner",
                "worker-a",
                "--phase",
                "mystery-phase",
                "--now",
                "2026-08-31T00:00:01Z",
            )
            recovery = run_queue(tmp_path, "recover", "--now", "2026-08-31T02:00:02Z")
            self.assertEqual(recovery["recovered_ready"][0]["card_id"], safe_id)
            self.assertEqual(
                {item["card_id"] for item in recovery["blocked_partial"]},
                {partial_id, unknown_id},
            )

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
            unknown_card = read_frontmatter(tmp_path / "research-queue" / "cards" / f"{unknown_id}.md")
            self.assertEqual(unknown_card["result_code"], "partial-write-recovery")

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
            staged = tmp_path / "staged.md"
            staged.write_text("staged human edit\n", encoding="utf-8")
            subprocess.run(["git", "add", "staged.md"], cwd=tmp_path, check=True)
            adapter = tmp_path / "adapter.py"
            adapter.write_text(
                "import json\n"
                "from pathlib import Path\n"
                "Path('wiki').mkdir(exist_ok=True)\n"
                "Path('wiki/result.md').write_text('# result\\n')\n"
                "print(json.dumps({'status':'PASS','scope':'item','durable_write':'completed','exhausted':False,'confirmation':'none','code':'durable-write-complete','reason':'Output was written.'}))\n",
                encoding="utf-8",
            )
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
                "--handoff-command",
                f"{sys.executable} adapter.py",
                "--output",
                "wiki/result.md",
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
            self.assertIn("A  staged.md", status)
            self.assertNotIn("wiki/result.md", status)
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
                json.dumps(
                    {
                        "status": [],
                        "scope": "item",
                        "durable_write": "completed",
                        "exhausted": False,
                        "confirmation": "none",
                        "code": "success",
                        "reason": "Malformed status should be rejected safely.",
                    }
                ),
            )
            self.assertEqual(result["status"], "Blocked")
            self.assertTrue(result["global_blocked"])
            card = read_frontmatter(tmp_path / "research-queue" / "cards" / f"{card_id}.md")
            self.assertEqual(card["result_code"], "unknown-result")

    def test_process_accepts_sequential_executable_handoff_adapter(self) -> None:
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
            created = run_queue(tmp_path, "intake", "--tickers", "VIG", "--type", "ETF")
            adapter = tmp_path / "adapter.py"
            adapter.write_text(
                "import json, os\n"
                "from pathlib import Path\n"
                "assert os.environ['RESEARCH_PROJECT_LEASE_TOKEN']\n"
                "assert os.environ['RESEARCH_CARD_FENCING_TOKEN']\n"
                "assert os.environ['RESEARCH_EXECUTION_PROFILE'] == 'scheduled-inline'\n"
                "assert json.loads(os.environ['RESEARCH_OUTPUT_PATHS']) == ['wiki/adapter-output.md']\n"
                "Path('wiki').mkdir(exist_ok=True)\n"
                "Path('wiki/adapter-output.md').write_text('# ' + os.environ['RESEARCH_TICKER'] + '\\n')\n"
                "print(json.dumps({'status':'PASS','scope':'item','durable_write':'completed','exhausted':False,'confirmation':'none','code':'success','reason':'adapter completed'}))\n",
                encoding="utf-8",
            )
            processed = run_queue(
                tmp_path,
                "process",
                "--count",
                "1",
                "--handoff-command",
                f"{sys.executable} adapter.py",
                "--output",
                "wiki/adapter-output.md",
                "--commit",
            )
            self.assertEqual(processed["completed"], [created["created"][0]["card_id"]])
            self.assertEqual(processed["skipped"], [])

    def test_unsupported_ready_cards_are_reported_without_claiming(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            created = run_queue(tmp_path, "intake", "--tickers", "VIG", "--type", "ETF")
            card_path = tmp_path / "research-queue" / "cards" / f"{created['created'][0]['card_id']}.md"
            card_path.write_text(
                card_path.read_text(encoding="utf-8").replace(
                    'workflow: "check-etf-performance"', 'workflow: "official-source-stock-research"'
                ),
                encoding="utf-8",
            )
            handoff = json.dumps(
                {
                    "status": "PASS",
                    "scope": "item",
                    "durable_write": "completed",
                    "exhausted": False,
                    "confirmation": "none",
                    "code": "success",
                    "reason": "not used",
                }
            )
            processed = run_queue(
                tmp_path,
                "process",
                "--count",
                "1",
                "--handoff-json",
                handoff,
            )
            self.assertEqual(processed["attempted"], [])
            self.assertEqual(processed["skipped"][0]["code"], "unsupported-workflow")

    def test_malformed_card_is_not_silently_ignored(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            cards_dir = tmp_path / "research-queue" / "cards"
            cards_dir.mkdir(parents=True)
            malformed = cards_dir / "rc-20260831T000000Z-deadbeef.md"
            malformed.write_text("not frontmatter\n", encoding="utf-8")
            code, error = run_queue_error(tmp_path, "list")
            self.assertNotEqual(code, 0)
            self.assertEqual(error["error"]["code"], "invalid-card")
            self.assertIn(malformed.name, error["error"]["reason"])

    def test_process_requires_and_honors_per_card_output_map_for_batches(self) -> None:
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
            created = run_queue(tmp_path, "intake", "--tickers", "VIG,DGRO", "--type", "ETF")
            output_map = tmp_path / "outputs.json"
            output_map.write_text(json.dumps({"VIG": ["wiki/vig.md"], "DGRO": ["wiki/dgro.md"]}), encoding="utf-8")
            adapter = tmp_path / "adapter.py"
            adapter.write_text(
                "import json, os\n"
                "from pathlib import Path\n"
                "name = 'wiki/' + os.environ['RESEARCH_TICKER'].lower() + '.md'\n"
                "Path('wiki').mkdir(exist_ok=True)\n"
                "Path(name).write_text(name + '\\n')\n"
                "print(json.dumps({'status':'PASS','scope':'item','durable_write':'completed','exhausted':False,'confirmation':'none','code':'success','reason':'Output was written.'}))\n",
                encoding="utf-8",
            )
            processed = run_queue(
                tmp_path,
                "process",
                "--count",
                "2",
                "--handoff-command",
                f"{sys.executable} adapter.py",
                "--output-map",
                "outputs.json",
                "--commit",
            )
            self.assertEqual(processed["completed"], [item["card_id"] for item in created["created"]])
            self.assertEqual(len(processed["completed"]), 2)

    def test_claim_next_can_retain_project_lease_across_commands(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            created = run_queue(tmp_path, "intake", "--tickers", "VIG", "--type", "ETF")
            claimed = run_queue(
                tmp_path,
                "claim-next",
                "--count",
                "1",
                "--owner",
                "manager-a",
                "--keep-lease",
            )
            self.assertEqual(claimed["claimed"][0]["card_id"], created["created"][0]["card_id"])
            self.assertTrue((tmp_path / "research-queue" / ".runtime" / "queue-lease.json").exists())
            renewed = run_queue(
                tmp_path,
                "renew",
                "--card-id",
                created["created"][0]["card_id"],
                "--owner",
                "manager-a",
                "--lease-token",
                claimed["lease_token"],
                "--fencing-token",
                claimed["claimed"][0]["fencing_token"],
                "--phase",
                "pre-write",
                "--now",
                "2026-08-31T01:00:00Z",
            )
            self.assertEqual(renewed["lease_expires_at"], "2026-08-31T03:00:00Z")
            lease_payload = json.loads((tmp_path / "research-queue" / ".runtime" / "queue-lease.json").read_text())
            self.assertEqual(lease_payload["lease_expires_at"], "2026-08-31T03:00:00Z")
            code, error = run_queue_error(tmp_path, "claim-next", "--count", "1", "--owner", "manager-b", "--now", "2026-08-31T01:00:01Z")
            self.assertNotEqual(code, 0)
            self.assertEqual(error["error"]["code"], "manager-overlap")
            released = run_queue(
                tmp_path,
                "lease-release",
                "--owner",
                "manager-a",
                "--lease-token",
                claimed["lease_token"],
                "--now",
                "2026-08-31T01:00:02Z",
            )
            self.assertTrue(released["released"])
            self.assertFalse((tmp_path / "research-queue" / ".runtime" / "queue-lease.json").exists())

    def test_recovery_ignores_preclaim_durable_edits_but_blocks_new_ones(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
            subprocess.run(["git", "config", "user.email", "queue@example.test"], cwd=tmp_path, check=True)
            subprocess.run(["git", "config", "user.name", "Queue Test"], cwd=tmp_path, check=True)
            wiki = tmp_path / "wiki"
            wiki.mkdir()
            keep = wiki / "keep.md"
            keep.write_text("pre-existing\n", encoding="utf-8")
            subprocess.run(["git", "add", "wiki/keep.md"], cwd=tmp_path, check=True)
            subprocess.run(["git", "commit", "-qm", "baseline"], cwd=tmp_path, check=True)
            created = run_queue(tmp_path, "intake", "--tickers", "VIG,DGRO", "--type", "ETF")
            run_queue(tmp_path, "claim", "--card-id", created["created"][0]["card_id"], "--owner", "worker-a", "--now", "2026-08-31T00:00:00Z")
            safe_recovery = run_queue(tmp_path, "recover", "--now", "2026-08-31T02:00:01Z")
            self.assertIn(created["created"][0]["card_id"], {item["card_id"] for item in safe_recovery["recovered_ready"]})
            run_queue(tmp_path, "claim", "--card-id", created["created"][1]["card_id"], "--owner", "worker-a", "--now", "2026-08-31T02:00:02Z")
            new_output = wiki / "new.md"
            new_output.write_text("partial\n", encoding="utf-8")
            recovery = run_queue(tmp_path, "recover", "--now", "2026-08-31T04:00:03Z")
            self.assertIn(created["created"][1]["card_id"], {item["card_id"] for item in recovery["blocked_partial"]})

    def test_recovery_blocks_when_git_evidence_is_unavailable(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
            subprocess.run(["git", "config", "user.email", "queue@example.test"], cwd=tmp_path, check=True)
            subprocess.run(["git", "config", "user.name", "Queue Test"], cwd=tmp_path, check=True)
            (tmp_path / "baseline.md").write_text("baseline\n", encoding="utf-8")
            subprocess.run(["git", "add", "baseline.md"], cwd=tmp_path, check=True)
            subprocess.run(["git", "commit", "-qm", "baseline"], cwd=tmp_path, check=True)
            created = run_queue(tmp_path, "intake", "--tickers", "VIG", "--type", "ETF", "--now", "2026-08-31T00:00:00Z")
            card_id = created["created"][0]["card_id"]
            claim = run_queue(tmp_path, "claim", "--card-id", card_id, "--owner", "worker-a", "--now", "2026-08-31T00:00:01Z")
            card_path = tmp_path / "research-queue" / "cards" / f"{card_id}.md"
            card_path.write_text(card_path.read_text(encoding="utf-8").replace("claim_baseline_paths: []", 'claim_baseline_paths: ["<git-status-unavailable>"]'), encoding="utf-8")
            recovered = run_queue(tmp_path, "recover", "--now", "2026-08-31T02:00:02Z")
            self.assertEqual(recovered["recovered_ready"], [])
            self.assertEqual(recovered["blocked_partial"][0]["result_code"], "partial-write-recovery")

    def test_recovery_materializes_terminal_card_after_commit_before_sync_crash(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as directory:
            tmp_path = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
            subprocess.run(["git", "config", "user.email", "queue@example.test"], cwd=tmp_path, check=True)
            subprocess.run(["git", "config", "user.name", "Queue Test"], cwd=tmp_path, check=True)
            (tmp_path / "baseline.md").write_text("baseline\n", encoding="utf-8")
            subprocess.run(["git", "add", "baseline.md"], cwd=tmp_path, check=True)
            subprocess.run(["git", "commit", "-qm", "baseline"], cwd=tmp_path, check=True)
            created = run_queue(tmp_path, "intake", "--tickers", "VIG", "--type", "ETF")
            card_id = created["created"][0]["card_id"]
            claim = run_queue(tmp_path, "claim", "--card-id", card_id, "--owner", "worker-a")
            run_queue(tmp_path, "renew", "--card-id", card_id, "--owner", "worker-a", "--fencing-token", claim["fencing_token"], "--phase", "pre-write", "--output", "wiki/crash.md")
            (tmp_path / "wiki").mkdir()
            (tmp_path / "wiki/crash.md").write_text("crash output\n", encoding="utf-8")
            card_path = tmp_path / "research-queue" / "cards" / f"{card_id}.md"
            before_route = card_path.read_text(encoding="utf-8")
            handoff = json.dumps({"status": "PASS", "scope": "item", "durable_write": "completed", "exhausted": False, "confirmation": "none", "code": "success", "reason": "output"})
            routed = run_queue(tmp_path, "route", "--card-id", card_id, "--owner", "worker-a", "--fencing-token", claim["fencing_token"], "--handoff-json", handoff, "--output", "wiki/crash.md", "--commit")
            self.assertEqual(routed["status"], "Done")
            card_path.write_text(before_route, encoding="utf-8")
            recovered = run_queue(tmp_path, "recover", "--now", "2026-08-31T23:00:00Z")
            self.assertEqual(recovered["recovered_done"][0]["card_id"], card_id)
            self.assertEqual(read_frontmatter(card_path)["status"], "Done")

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
                with self.assertRaises(QueueError) as expired:
                    first.renew(parse_time("2026-08-31T02:00:00Z"))
                self.assertEqual(expired.exception.code, "manager-overlap")
            finally:
                first.release()

    def test_bullets_seed_and_terminal_cards_allow_refresh(self) -> None:
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
            run_queue(
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
                "--output",
                "wiki/terminal.md",
            )
            (tmp_path / "wiki").mkdir()
            output = tmp_path / "wiki" / "terminal.md"
            output.write_text("# terminal\n", encoding="utf-8")
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
                "--output",
                "wiki/terminal.md",
                "--commit",
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
