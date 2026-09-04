import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO_ROOT = PROJECT_ROOT / "paper-portfolios" / "us-etf-competition"
PIPELINE = PORTFOLIO_ROOT / "scripts" / "market_data_pipeline.py"
RECORDER = PORTFOLIO_ROOT / "scripts" / "record_market_data_batch.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PIPELINE_MODULE = load_module(PIPELINE, "market_data_pipeline")


def sha256_text(value: str) -> str:
    return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def _clock():
    visible = "Invocation clock: 2026-09-04 04:02:54 EDT (America/New_York)"
    return {
        "evidence_id": "run-2026-09-04-040254-et:clock",
        "provider": "system clock",
        "method": "local-time-command",
        "kind": "invocation-clock",
        "retrieved_at": "2026-09-04T08:42:28Z",
        "visible_response_text": visible,
        "content_hash": sha256_text(visible),
        "information_cutoff_at": "2026-09-04T08:02:54Z",
        "post_period_data_used": False,
    }


def _calendar():
    visible = "NYSE calendar confirms September 4, 2026 is a normal trading day"
    return {
        "evidence_id": "run-2026-09-04-040254-et:calendar",
        "provider": "NYSE",
        "method": "browser-direct-web",
        "kind": "calendar",
        "discovery_method": "browser_search",
        "discovery_query": "site:nyse.com September 4 2026 trading calendar",
        "direct_url": "https://www.nyse.com/trade/hours-calendars",
        "page_title": "Holidays & Trading Hours",
        "retrieved_at": "2026-09-04T08:42:28Z",
        "visible_response_text": visible,
        "content_hash": sha256_text(visible),
        "information_cutoff_at": "2026-09-04T08:02:54Z",
        "post_period_data_used": False,
    }


def _observation(ticker: str, identity: str, price: float, closes: list[tuple[str, float, int]], *, status="VERIFIED_COMPLETED_SESSION_CLOSE"):
    visible = f"{ticker} | {identity} | completed-session close {price:.2f}"
    return {
        "evidence_id": f"run-2026-09-04-040254-et:quote:{ticker}",
        "observation_kind": "quote-history",
        "ticker": ticker,
        "exchange_qualified_identity": identity,
        "provider": "StockAnalysis.com",
        "underlying_data_source": "Tiingo",
        "method": "browser-direct-web",
        "discovery_method": "browser_search",
        "discovery_query": f"site:stockanalysis.com/etf/{ticker.lower()}/history {ticker} ETF historical price",
        "direct_url": f"https://stockanalysis.com/etf/{ticker.lower()}/history/",
        "page_title": f"{ticker} Historical Stock Price Data",
        "visible_response_text": visible,
        "content_hash": sha256_text(visible),
        "response_sha256": sha256_text(visible),
        "retrieved_at": "2026-09-04T08:42:28Z",
        "source_as_of": "2026-09-03T16:00:00-04:00",
        "price": price,
        "currency": "USD",
        "price_basis": "completed-session close",
        "latest_completed_session": closes[0][0],
        "five_session_observations": [
            {"session_date": date, "close": close, "volume_shares": volume}
            for date, close, volume in closes
        ],
        "median_daily_dollar_volume_usd": 50000000.0,
        "status": status,
        "decision_reference": ticker == "VOO",
        "post_period_data_used": False,
    }


def valid_batch() -> dict[str, object]:
    return {
        "schema_version": 2,
        "kind": "market-data-batch",
        "competition_id": "us-etf-competition-2026",
        "run_id": "run-2026-09-04-040254-et",
        "analysis_at": "2026-09-04T08:02:54Z",
        "information_cutoff_at": "2026-09-04T08:02:54Z",
        "created_at": "2026-09-04T08:42:28Z",
        "evidence_status": "verified",
        "post_period_data_used": False,
        "clock": _clock(),
        "calendar": _calendar(),
        "observations": [
            _observation(
                "SPY",
                "NYSEARCA:SPY",
                773.17,
                [
                    ("2026-09-03", 773.17, 9000000),
                    ("2026-09-02", 765.16, 8000000),
                ],
            ),
            _observation(
                "VOO",
                "NYSEARCA:VOO",
                710.72,
                [
                    ("2026-09-03", 710.72, 8536838),
                    ("2026-09-02", 703.41, 7702258),
                    ("2026-09-01", 700.28, 6447027),
                    ("2026-08-31", 704.89, 5719456),
                    ("2026-08-28", 707.24, 8054710),
                    ("2026-08-27", 692.00, 6728083),
                ],
            ),
        ],
    }


LEGACY_CACHE = """---
kind: etf-price-cache
competition_id: us-etf-competition-2026
source_policy: browser-direct-web
cache_role: preliminary-screen-only
updated_at: \"2026-09-03T08:15:41Z\"
---

# Latest Verified ETF Price Cache

| Ticker | Exchange-qualified identity | Price | Currency | Price basis | Source as-of | Retrieved at | Source | Direct URL | Evidence | Run ID | Status |
|---|---|---:|---|---|---|---|---|---|---|---|---|
| SPY | NYSEARCA:SPY | 765.16 | USD | completed-session adjusted close | 2026-09-02T16:00:00-04:00 | 2026-09-03T08:15:41Z | StockAnalysis.com | https://stockanalysis.com/etf/spy/history/ | [quote](2026-09-03/quote_SPY.json) | run-2026-09-03-040324-et | PRELIMINARY |
"""


LEGACY_PRICE_LOG = """---
kind: etf-price-log
competition_id: us-etf-competition-2026
append_only: true
canonical_history: true
source_policy: browser-direct-web
---

# ETF Price Log

| Observation ID | Run ID | Ticker | Exchange-qualified identity | Price | Currency | Price basis | Source as-of | Retrieved at | Source | Direct URL | Evidence | Status |
|---|---|---|---|---:|---|---|---|---|---|---|---|---|
| obs-spy-1 | run-old | SPY | NYSEARCA:SPY | 765.16 | USD | completed-session adjusted close | 2026-09-02T16:00:00-04:00 | 2026-09-03T08:15:41Z | StockAnalysis.com | https://stockanalysis.com/etf/spy/history/ | [quote](2026-09-03/quote_SPY.json) | PRELIMINARY |
| obs-voo-1 | run-old | VOO | NYSEARCA:VOO | 703.41 | USD | completed-session close | 2026-09-02T16:00:00-04:00 | 2026-09-03T08:15:41Z | StockAnalysis.com | https://stockanalysis.com/etf/voo/history/ | [quote](2026-09-03/quote_VOO.json) | PRELIMINARY |
| obs-voo-2 | run-old-2 | VOO | NYSEARCA:VOO | 700.28 | USD | completed-session close | 2026-09-01T16:00:00-04:00 | 2026-09-04T08:15:41Z | StockAnalysis.com | https://stockanalysis.com/etf/voo/history/ | [quote](2026-09-04/quote_VOO.json) | PRELIMINARY |

Historical prose after this table must not be parsed as another row.
"""


class MarketDataPipelineTests(unittest.TestCase):
    def test_valid_batch_passes_validation(self):
        PIPELINE_MODULE.validate_batch(valid_batch())

    def test_validation_rejects_required_evidence_failures(self):
        cases = []

        missing_url = copy.deepcopy(valid_batch())
        del missing_url["observations"][0]["direct_url"]
        cases.append(("missing direct URL", missing_url))

        duplicate_id = copy.deepcopy(valid_batch())
        duplicate_id["observations"][0]["evidence_id"] = duplicate_id["clock"]["evidence_id"]
        cases.append(("duplicate evidence ID", duplicate_id))

        altered_text = copy.deepcopy(valid_batch())
        altered_text["observations"][0]["visible_response_text"] += " altered"
        cases.append(("altered visible text", altered_text))

        late_source = copy.deepcopy(valid_batch())
        late_source["observations"][0]["source_as_of"] = "2026-09-05T16:00:00-04:00"
        cases.append(("source after cutoff", late_source))

        post_period = copy.deepcopy(valid_batch())
        post_period["post_period_data_used"] = True
        cases.append(("post-period data", post_period))

        missing_basis = copy.deepcopy(valid_batch())
        del missing_basis["observations"][0]["price_basis"]
        cases.append(("missing price basis", missing_basis))

        for name, batch in cases:
            with self.subTest(name=name):
                with self.assertRaises(PIPELINE_MODULE.MarketDataError):
                    PIPELINE_MODULE.validate_batch(batch)

    def test_merge_screen_cache_keeps_one_row_and_calculates_returns(self):
        rendered = PIPELINE_MODULE.merge_screen_cache(LEGACY_CACHE, valid_batch())
        self.assertIn("etf-price-screen-cache", rendered)
        self.assertIn("VOO", rendered)
        self.assertEqual(rendered.count("| VOO |"), 1)
        self.assertIn("1.04%", rendered)
        self.assertIn("2.71%", rendered)
        self.assertIn("PRELIMINARY", rendered)

    def test_render_price_log_rows_projects_each_quote_without_visible_text(self):
        rows = PIPELINE_MODULE.render_price_log_rows(valid_batch())
        self.assertEqual(len(rows), 2)
        self.assertTrue(all("batches/run-2026-09-04-040254-et.json" in row for row in rows))
        self.assertTrue(all("completed-session close" not in row for row in rows))
        self.assertIn("run-2026-09-04-040254-et:quote:VOO", rows[1])

    def test_bootstrap_screen_cache_preserves_legacy_links_and_one_row_per_ticker(self):
        rendered = PIPELINE_MODULE.bootstrap_screen_cache(LEGACY_PRICE_LOG)
        self.assertIn("etf-price-screen-cache", rendered)
        self.assertEqual(rendered.count("| SPY |"), 1)
        self.assertEqual(rendered.count("| VOO |"), 1)
        self.assertIn("2026-09-03/quote_SPY.json", rendered)
        self.assertIn("2026-09-04/quote_VOO.json", rendered)

    def test_record_batch_creates_one_batch_and_no_ticker_json_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            market_data = root / "evidence" / "market-data"
            market_data.mkdir(parents=True)
            (market_data / "latest-prices.md").write_text(LEGACY_CACHE, encoding="utf-8")
            (market_data / "price-log.md").write_text(LEGACY_PRICE_LOG, encoding="utf-8")
            batch_path = root / "staging" / "run.json"
            batch_path.parent.mkdir()
            batch_path.write_text(json.dumps(valid_batch(), indent=2), encoding="utf-8")

            result = PIPELINE_MODULE.record_batch(root, batch_path)
            self.assertEqual(result["batch_files_created"], 1)
            canonical = market_data / "batches" / "run-2026-09-04-040254-et.json"
            self.assertEqual(list((market_data / "batches").glob("*.json")), [canonical])
            self.assertEqual(list((market_data / "batches").glob("quote_*.json")), [])
            self.assertEqual((market_data / "price-log.md").read_text(encoding="utf-8").count("run-2026-09-04-040254-et:quote:"), 2)
            self.assertEqual((market_data / "latest-prices.md").read_text(encoding="utf-8").count("| VOO |"), 1)

    def test_recording_same_batch_twice_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            market_data = root / "evidence" / "market-data"
            market_data.mkdir(parents=True)
            (market_data / "latest-prices.md").write_text(LEGACY_CACHE, encoding="utf-8")
            (market_data / "price-log.md").write_text(LEGACY_PRICE_LOG, encoding="utf-8")
            batch_path = root / "staging" / "run.json"
            batch_path.parent.mkdir()
            batch_path.write_text(json.dumps(valid_batch(), indent=2), encoding="utf-8")

            PIPELINE_MODULE.record_batch(root, batch_path)
            log_after_first = (market_data / "price-log.md").read_bytes()
            cache_after_first = (market_data / "latest-prices.md").read_bytes()
            second = PIPELINE_MODULE.record_batch(root, batch_path)
            self.assertEqual(second["duplicate_batch"], True)
            self.assertEqual((market_data / "price-log.md").read_bytes(), log_after_first)
            self.assertEqual((market_data / "latest-prices.md").read_bytes(), cache_after_first)

    def test_check_only_does_not_modify_project_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            market_data = root / "evidence" / "market-data"
            market_data.mkdir(parents=True)
            (market_data / "latest-prices.md").write_text(LEGACY_CACHE, encoding="utf-8")
            (market_data / "price-log.md").write_text(LEGACY_PRICE_LOG, encoding="utf-8")
            batch_path = root / "staging" / "run.json"
            batch_path.parent.mkdir()
            batch_path.write_text(json.dumps(valid_batch(), indent=2), encoding="utf-8")
            before = sorted(path.relative_to(root) for path in root.rglob("*"))

            result = PIPELINE_MODULE.record_batch(root, batch_path, check_only=True)
            after = sorted(path.relative_to(root) for path in root.rglob("*"))
            self.assertEqual(result["status"], "PASS")
            self.assertEqual(before, after)

    def test_recorder_cli_check_only_outputs_pass(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            market_data = root / "evidence" / "market-data"
            market_data.mkdir(parents=True)
            (market_data / "latest-prices.md").write_text(LEGACY_CACHE, encoding="utf-8")
            (market_data / "price-log.md").write_text(LEGACY_PRICE_LOG, encoding="utf-8")
            batch_path = root / "staging" / "run.json"
            batch_path.parent.mkdir()
            batch_path.write_text(json.dumps(valid_batch(), indent=2), encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(RECORDER), "--root", str(root), "--batch", str(batch_path), "--check"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
