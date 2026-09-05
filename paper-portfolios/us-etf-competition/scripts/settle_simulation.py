#!/usr/bin/env python3
"""Settle pending local decisions from a recorded, validated opening-price batch.

Default is a dry run. --write appends validated events under an exclusive ledger
lock and rebuilds projections. No network or broker calls are made.
"""
from __future__ import annotations

import argparse
import fcntl
import json
from pathlib import Path

import rebuild_portfolio as ledger
from market_data_pipeline import load_batch, MarketDataError


def settlement_events(events, batch, batch_path, recorded_at):
    if batch.get("competition_id") != ledger.apply_events(ledger.corrected_events(events))["competition_id"]:
        raise ledger.LedgerError("batch belongs to another competition")
    effective = ledger.corrected_events(events)
    state = ledger.apply_events(effective)
    if state["phase"] != "simulation":
        raise ledger.LedgerError("local simulation phase is not active")
    generated = []
    skipped = []
    pending = sorted(state["pending_decisions"], key=lambda d: (d["side"] == "BUY", d["event_id"]))
    for decision in pending:
        candidates = [o for o in batch["observations"]
                      if o["ticker"] == decision["ticker"]
                      and o["price_basis"] == "unadjusted-session-open"
                      and ledger.parse_time(o["source_as_of"], "source_as_of")
                      == ledger.parse_time(decision["execution_at"], "execution_at")]
        if not candidates:
            skipped.append({"decision": decision["event_id"], "reason": "awaiting predetermined session open evidence"})
            continue
        if len({str(o["price"]) for o in candidates}) != 1:
            skipped.append({"decision": decision["event_id"], "reason": "conflicting opening prices"})
            continue
        observation = candidates[0]
        if observation["currency"] != "USD" or observation["exchange_qualified_identity"] != decision["exchange_qualified_identity"]:
            raise ledger.LedgerError("opening quote identity/currency mismatch")
        if ledger.parse_time(observation["retrieved_at"], "retrieved_at") > ledger.parse_time(recorded_at, "recorded_at"):
            raise ledger.LedgerError("evidence retrieval cannot follow fill recording")
        opening = ledger.decimal(observation["price"], "opening")
        multiplier = ledger.Decimal("1.0005") if decision["side"] == "BUY" else ledger.Decimal("0.9995")
        fill = {
            "event_id": "simulated-fill-" + decision["event_id"],
            "event_type": "SIMULATED_FILL", "decision_event_id": decision["event_id"],
            "competition_id": state["competition_id"], "run_id": batch["run_id"],
            "recorded_at": recorded_at, "effective_at": decision["execution_at"],
            "ticker": decision["ticker"], "side": decision["side"],
            "quantity": decision["quantity"], "fill_price": str(ledger.rounded(opening * multiplier)),
            "execution_reference_price": str(opening), "execution_price_as_of": observation["source_as_of"],
            "price_basis": observation["price_basis"], "fee": "0",
            "risk_override": decision.get("risk_override", False),
            "source_evidence": [{"batch": batch_path, "evidence_id": observation["evidence_id"]}],
            "execution_status": "SIMULATED", "post_period_data_used": False,
        }
        try:
            ledger.apply_events(ledger.corrected_events(events + generated + [fill]))
        except ledger.LedgerError as exc:
            # Preserve unrelated executable candidates. An unfillable fixed order
            # expires instead of being silently resized using the future price.
            cancelled = {
                "event_id": "cancelled-" + decision["event_id"], "event_type": "DECISION_CANCELLED",
                "decision_event_id": decision["event_id"], "recorded_at": recorded_at,
                "effective_at": recorded_at, "reason": str(exc),
            }
            generated.append(cancelled)
            skipped.append({"decision": decision["event_id"], "reason": str(exc)})
        else:
            generated.append(fill)
    ledger.apply_events(ledger.corrected_events(events + generated))
    return generated, skipped


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--batch", type=Path, required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        path = args.batch.resolve()
        relative = path.relative_to(root / "evidence/market-data/batches")
        batch = load_batch(path)
        with (root / "ledger/events.jsonl").open("r+", encoding="utf-8") as handle:
            fcntl.flock(handle, fcntl.LOCK_EX)
            events = ledger.load_events(root / "ledger/events.jsonl")
            generated, skipped = settlement_events(events, batch, "evidence/market-data/batches/" + str(relative), ledger.iso_time(ledger.now_utc()))
            if args.write and generated:
                handle.seek(0, 2)
                handle.write("".join(json.dumps(e, sort_keys=True) + "\n" for e in generated))
                handle.flush()
            if args.write:
                state = ledger.apply_events(ledger.corrected_events(events + generated))
                ledger.atomic_write(root / "state/portfolio.json", json.dumps(state, indent=2, sort_keys=True) + "\n")
                ledger.atomic_write(root / "dashboard.md", ledger.render_dashboard(state))
        print(json.dumps({"status": "PASS", "written": args.write, "events": generated, "skipped": skipped}))
        return 0
    except (ledger.LedgerError, MarketDataError, ValueError, OSError, KeyError) as exc:
        print(json.dumps({"status": "BLOCKED", "reason": str(exc)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
