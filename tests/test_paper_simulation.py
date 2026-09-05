import copy
import hashlib
import json
import subprocess
import tempfile
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "paper-portfolios/us-etf-competition/scripts"
sys.path.insert(0, str(SCRIPTS))
import rebuild_portfolio as ledger
import settle_simulation as settlement
from test_market_data_pipeline import valid_batch


def event(key, kind, at, **fields):
    return dict(event_id=key, event_type=kind, effective_at=at, recorded_at=at, **fields)


def history():
    return [event("config", "COMPETITION_CONFIGURED", "2026-09-01T14:00:00Z",
                  competition_id="test", starting_cash="100000", phase="proposal"),
            event("activate", "PHASE_CHANGED", "2026-09-01T15:00:00Z",
                  phase="simulation", user_authorized=True)]


def decision(key="buy", ticker="VOO", side="BUY", quantity="100", cap="12000"):
    return event(key, "DECISION", "2026-09-02T19:00:00Z", run_id="review-1",
                 status="PENDING", execution_model="next-session-open", ticker=ticker,
                 exchange_qualified_identity="NYSEARCA:" + ticker,
                 side=side, quantity=quantity, maximum_notional_usd=cap,
                 decision_reference_price="100", execution_at="2026-09-03T13:30:00Z",
                 source_evidence=["test-decision-evidence"], calendar_evidence="test-calendar")


def batch(ticker="VOO", price=100):
    return {"competition_id": "test", "run_id": "settlement-1", "observations": [{
        "ticker": ticker, "exchange_qualified_identity": "NYSEARCA:" + ticker,
        "currency": "USD", "price": price, "price_basis": "unadjusted-session-open",
        "source_as_of": "2026-09-03T13:30:00Z", "retrieved_at": "2026-09-03T14:00:00Z",
        "evidence_id": "open:" + ticker}]}


def settle(events, evidence=None):
    return settlement.settlement_events(events, evidence or batch(), "test-batch.json", "2026-09-03T15:00:00Z")


class SimulationTests(unittest.TestCase):
    def test_pending_then_buy_and_idempotent_retry(self):
        events = history() + [decision()]
        before = ledger.apply_events(events)
        self.assertEqual(before["cash"], 100000)
        self.assertEqual(len(before["pending_decisions"]), 1)
        fills, gaps = settle(events)
        self.assertEqual(gaps, [])
        state = ledger.apply_events(events + fills)
        self.assertEqual(state["cash"], 89995)
        self.assertEqual(state["portfolio_value"], 99995)
        self.assertEqual(state["positions"]["VOO"]["average_cost"], 100.05)
        self.assertEqual(state["pending_decisions"], [])
        self.assertEqual(settle(events + fills)[0], [])

    def test_sell_updates_cash_and_pnl(self):
        events = history() + [decision()]
        events += settle(events)[0]
        sell = decision("sell", side="SELL", quantity="50", cap="7000")
        sell.update(recorded_at="2026-09-03T19:00:00Z", effective_at="2026-09-03T19:00:00Z",
                    execution_at="2026-09-04T13:30:00Z")
        evidence = batch(price=110)
        evidence["observations"][0].update(source_as_of="2026-09-04T13:30:00Z", retrieved_at="2026-09-04T14:00:00Z")
        fills, _ = settlement.settlement_events(events + [sell], evidence, "test", "2026-09-04T15:00:00Z")
        state = ledger.apply_events(events + [sell] + fills)
        self.assertEqual(state["cash"], 95492.25)
        self.assertEqual(state["positions"]["VOO"]["quantity"], 50)
        self.assertEqual(state["positions"]["VOO"]["realized_pnl"], 494.75)

    def test_same_day_or_unapproved_phase_rejected(self):
        for changed in ("phase", "date"):
            events = history() + [decision()]
            if changed == "phase":
                events[1]["user_authorized"] = False
            else:
                events[2]["execution_at"] = "2026-09-02T13:30:00Z"
            with self.assertRaises(ledger.LedgerError):
                ledger.apply_events(events)

    def test_missing_or_wrong_open_stays_pending(self):
        for field, value in (("price_basis", "adjusted close"), ("source_as_of", "2026-09-04T13:30:00Z")):
            evidence = batch()
            evidence["observations"][0][field] = value
            fills, gaps = settle(history() + [decision()], evidence)
            self.assertEqual(fills, [])
            self.assertEqual(len(gaps), 1)

    def test_gap_cancels_one_candidate_and_settles_other(self):
        events = history() + [decision(cap="9999"), decision("second", ticker="VEA")]
        evidence = batch()
        evidence["observations"] += batch(ticker="VEA")["observations"]
        fills, gaps = settle(events, evidence)
        self.assertEqual(len(gaps), 1)
        state = ledger.apply_events(events + fills)
        self.assertNotIn("VOO", state["positions"])
        self.assertIn("VEA", state["positions"])
        self.assertEqual(state["pending_decisions"], [])

    def test_identity_conflict_rejected(self):
        evidence = batch()
        evidence["observations"][0]["currency"] = "EUR"
        with self.assertRaises(ledger.LedgerError):
            settle(history() + [decision()], evidence)

    def test_duplicate_and_tampered_fill_rejected(self):
        events = history() + [decision()]
        fills, _ = settle(events)
        for field, value in (("quantity", "101"), ("fill_price", "100"),
                             ("execution_price_as_of", "2026-09-02T13:30:00Z")):
            bad = copy.deepcopy(fills)
            bad[0][field] = value
            with self.assertRaises(ledger.LedgerError):
                ledger.apply_events(events + bad)
        with self.assertRaises(ledger.LedgerError):
            ledger.apply_events(events + fills + fills)

    def test_cash_and_position_guard(self):
        fills, gaps = settle(history() + [decision(quantity="1000", cap="200000")])
        self.assertEqual(fills[0]["event_type"], "DECISION_CANCELLED")
        self.assertTrue(gaps)
        self.assertEqual(ledger.apply_events(history() + [decision(quantity="1000", cap="200000")] + fills)["cash"], 100000)

    def test_cli_validated_batch_write_retry_and_corrupt_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "ledger").mkdir()
            batches = root / "evidence/market-data/batches"
            batches.mkdir(parents=True)
            path = batches / "test.json"
            evidence = valid_batch()
            evidence["competition_id"] = "test"
            observation = evidence["observations"][1]
            observation.update(price=100, price_basis="unadjusted-session-open",
                               source_as_of="2026-09-03T13:30:00Z",
                               visible_response_text="TEST FIXTURE: VOO unadjusted session Open 100")
            digest = "sha256:" + hashlib.sha256(observation["visible_response_text"].encode()).hexdigest()
            observation.update(content_hash=digest, response_sha256=digest)
            evidence["observations"] = [observation]
            path.write_text(json.dumps(evidence))
            ledger_path = root / "ledger/events.jsonl"
            original = "".join(json.dumps(e) + "\n" for e in history() + [decision()])
            ledger_path.write_text(original)
            command = [sys.executable, str(SCRIPTS / "settle_simulation.py"), "--root", str(root), "--batch", str(path)]
            dry = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(dry.returncode, 0, dry.stdout)
            self.assertEqual(ledger_path.read_text(), original)
            written = subprocess.run(command + ["--write"], capture_output=True, text=True)
            self.assertEqual(written.returncode, 0, written.stdout)
            after = ledger_path.read_text()
            retry = subprocess.run(command + ["--write"], capture_output=True, text=True)
            self.assertEqual(retry.returncode, 0, retry.stdout)
            self.assertEqual(ledger_path.read_text(), after)
            self.assertEqual(json.loads((root / "state/portfolio.json").read_text())["cash"], 89995)
            observation["visible_response_text"] = "tampered"
            path.write_text(json.dumps(evidence))
            bad = subprocess.run(command + ["--write"], capture_output=True, text=True)
            self.assertEqual(bad.returncode, 2)
            self.assertEqual(ledger_path.read_text(), after)


if __name__ == "__main__":
    unittest.main()
