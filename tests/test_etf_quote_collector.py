import importlib.util
import json
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("collector", Path(__file__).resolve().parents[1] / "paper-portfolios/us-etf-competition/scripts/fetch_etf_quotes.py")
collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collector)


class QuoteTests(unittest.TestCase):
    def raw(self, **changes):
        q = dict(Outcome="Success", Identifier="TEST", Currency="USD", TradingHalted=False,
                 Last=100, Date="9/4/2026", Time="4:00:00 PM", UTCOffset=-4,
                 Security={"Symbol": "TEST", "Market": "NYSEARCA"})
        q.update(changes)
        return json.dumps([q])

    def test_timestamp_and_unverified_basis(self):
        result = collector.normalize(self.raw(), "TEST", "2026-09-05T00:00:00+00:00")
        self.assertEqual(result["source_as_of"], "2026-09-04T16:00:00-04:00")
        self.assertEqual(result["status"], "REQUIRES_REVIEW")
        self.assertNotIn("latest_completed_session", result)

    def test_reject_identity_future_and_invalid_prices(self):
        for changes in ({"Identifier": "OTHER"}, {"Last": True}, {"Last": -1},
                        {"Last": float("nan")}, {"Date": "9/6/2026"}, {"TradingHalted": True}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                collector.normalize(self.raw(**changes), "TEST", "2026-09-05T00:00:00+00:00")

    def test_retry_after(self):
        self.assertEqual(collector.cooldown("Retry-After: 3600", 0), 3600)
        self.assertEqual(collector.cooldown("Retry-After: invalid", 0), 900)
        self.assertEqual(collector.cooldown("Retry-After: Thu, 01 Jan 1970 02:00:00 GMT", 0), 7200)
