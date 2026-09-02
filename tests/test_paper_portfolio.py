import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO_ROOT = PROJECT_ROOT / "paper-portfolios" / "us-etf-competition"
REBUILD = PORTFOLIO_ROOT / "scripts" / "rebuild_portfolio.py"
FETCH = PORTFOLIO_ROOT / "scripts" / "fetch_alpaca_data.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


REBUILD_MODULE = load_module(REBUILD, "paper_rebuild")
FETCH_MODULE = load_module(FETCH, "paper_fetch")


def configured(event_id="config"):
    return {
        "event_id": event_id,
        "event_type": "COMPETITION_CONFIGURED",
        "recorded_at": "2026-09-01T16:00:00Z",
        "effective_at": "2026-09-01T16:00:00Z",
        "competition_id": "test",
        "starting_cash": "100000",
        "phase": "proposal",
        "benchmark_symbol": "SPY",
    }


def event(event_id, event_type, effective_at, **fields):
    value = {
        "event_id": event_id,
        "event_type": event_type,
        "recorded_at": effective_at,
        "effective_at": effective_at,
    }
    value.update(fields)
    return value


def state_for(events):
    return REBUILD_MODULE.apply_events(REBUILD_MODULE.corrected_events(events))


class PaperPortfolioLedgerTests(unittest.TestCase):
    def test_buy_mark_dividend_sell_and_benchmark(self):
        events = [
            configured(),
            event("buy", "FILL", "2026-09-02T19:00:00Z", ticker="QQQ", side="BUY", quantity="100", fill_price="100"),
            event("mark-1", "MARK", "2026-09-02T20:00:00Z", session_date="2026-09-02", scope="daily-close", prices={"QQQ": 110}, benchmark_price=500),
            event("div", "DIVIDEND", "2026-09-03T14:00:00Z", ticker="QQQ", amount="100"),
            event("sell", "FILL", "2026-09-04T19:00:00Z", ticker="QQQ", side="SELL", quantity="50", fill_price="120"),
            event("mark-2", "MARK", "2026-09-04T20:00:00Z", session_date="2026-09-04", scope="daily-close", prices={"QQQ": 120}, benchmark_price=510),
        ]
        state = state_for(events)
        self.assertEqual(state["cash"], 96100.0)
        self.assertEqual(state["positions"]["QQQ"]["quantity"], 50.0)
        self.assertEqual(state["portfolio_value"], 102100.0)
        self.assertEqual(state["benchmark"]["return_pct"], 2.0)
        self.assertEqual(state["maximum_drawdown_pct"], 0.0)

    def test_daily_maximum_drawdown_uses_high_water_mark(self):
        events = [
            configured(),
            event("buy", "FILL", "2026-09-02T19:00:00Z", ticker="VIG", side="BUY", quantity="1000", fill_price="100"),
            event("mark-1", "MARK", "2026-09-02T20:00:00Z", session_date="2026-09-02", scope="daily-close", prices={"VIG": 100}, benchmark_price=500),
            event("mark-2", "MARK", "2026-09-03T20:00:00Z", session_date="2026-09-03", scope="daily-close", prices={"VIG": 80}, benchmark_price=490),
            event("mark-3", "MARK", "2026-09-04T20:00:00Z", session_date="2026-09-04", scope="daily-close", prices={"VIG": 90}, benchmark_price=505),
        ]
        state = state_for(events)
        self.assertEqual(state["maximum_drawdown_pct"], -20.0)
        self.assertEqual(state["current_drawdown_pct"], -10.0)

    def test_mirror_sync_does_not_change_ledger(self):
        events = [
            configured(),
            event("sync", "MIRROR_SYNC", "2026-09-02T18:00:00Z", ticker="VIG", side="BUY", quantity="100", fill_price="100"),
        ]
        state = state_for(events)
        self.assertEqual(state["cash"], 100000.0)
        self.assertEqual(state["positions"], {})

    def test_correction_replaces_original_event_without_rewriting_history(self):
        events = [
            configured(),
            event("buy", "FILL", "2026-09-02T19:00:00Z", ticker="VIG", side="BUY", quantity="10", fill_price="100"),
            event("correction", "CORRECTION", "2026-09-03T19:00:00Z", corrects_event_id="buy", replacement={"fill_price": "90"}),
        ]
        corrected = REBUILD_MODULE.corrected_events(events)
        self.assertEqual(len(corrected), 2)
        self.assertEqual(corrected[1]["event_id"], "buy")
        self.assertEqual(corrected[1]["fill_price"], "90")
        state = REBUILD_MODULE.apply_events(corrected)
        self.assertEqual(state["cash"], 99100.0)
        self.assertEqual(state["positions"]["VIG"]["average_cost"], 90.0)

    def test_split_preserves_cost_and_adjusts_quantity(self):
        events = [
            configured(),
            event("buy", "FILL", "2026-09-02T19:00:00Z", ticker="VIG", side="BUY", quantity="10", fill_price="100"),
            event("split", "SPLIT", "2026-09-03T19:00:00Z", ticker="VIG", ratio="2"),
            event("mark", "MARK", "2026-09-03T20:00:00Z", session_date="2026-09-03", scope="daily-close", prices={"VIG": 55}, benchmark_price=500),
        ]
        state = state_for(events)
        self.assertEqual(state["positions"]["VIG"]["quantity"], 20.0)
        self.assertEqual(state["positions"]["VIG"]["average_cost"], 50.0)
        self.assertEqual(state["portfolio_value"], 100100.0)

    def test_oversell_is_blocked(self):
        events = [
            configured(),
            event("buy", "FILL", "2026-09-02T19:00:00Z", ticker="VIG", side="BUY", quantity="10", fill_price="100"),
            event("sell", "FILL", "2026-09-03T19:00:00Z", ticker="VIG", side="SELL", quantity="11", fill_price="100"),
        ]
        with self.assertRaises(REBUILD_MODULE.LedgerError):
            state_for(events)

    def test_cli_rebuild_check_passes_and_fetch_dry_run_is_documented(self):
        result = subprocess.run([sys.executable, str(REBUILD), "--check"], capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('"status": "PASS"', result.stdout)
        dry_run = subprocess.run([sys.executable, str(FETCH), "--dry-run", "bars", "--symbols", "SPY, VIG", "--start", "2026-09-01", "--end", "2026-09-01", "--asof", "2026-09-01"], capture_output=True, text=True, check=False)
        self.assertEqual(dry_run.returncode, 0, dry_run.stderr)
        request = json.loads(dry_run.stdout)
        self.assertEqual(request["method"], "GET")
        self.assertEqual(request["endpoint"], "/v2/stocks/bars")
        self.assertEqual(request["params"]["adjustment"], "all")
        self.assertEqual(request["params"]["symbols"], "SPY,VIG")
        self.assertEqual(request["params"]["asof"], "2026-09-01")
        corporate_actions = subprocess.run(
            [sys.executable, str(FETCH), "--dry-run", "corporate-actions", "--symbols", "VIG", "--start", "2026-09-01", "--end", "2026-09-02"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(corporate_actions.returncode, 0, corporate_actions.stderr)
        corporate_request = json.loads(corporate_actions.stdout)
        self.assertEqual(corporate_request["endpoint"], "/v1/corporate-actions")
        self.assertEqual(corporate_request["params"]["region"], "us")


if __name__ == "__main__":
    unittest.main()
