#!/usr/bin/env python3
"""Validate the append-only ledger and rebuild portfolio state/dashboard.

The ledger is intentionally small and event based.  This module uses Decimal
for accounting, rejects ambiguous state transitions, and treats derived JSON
and Markdown as disposable projections.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import tempfile
from collections import OrderedDict
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any, Iterable


MONEY_QUANT = Decimal("0.0001")
QTY_QUANT = Decimal("0.000001")
PCT_QUANT = Decimal("0.01")
SUPPORTED_EVENT_TYPES = {
    "COMPETITION_CONFIGURED",
    "PHASE_CHANGED",
    "DECISION",
    "ORDER_SUBMITTED",
    "FILL",
    "MIRROR_SYNC",
    "DIVIDEND",
    "FEE",
    "SPLIT",
    "MARK",
    "RUN_BLOCKED",
    "FINAL_RECONCILIATION",
    "CORRECTION",
}
PASSIVE_EVENT_TYPES = {
    "DECISION",
    "ORDER_SUBMITTED",
    "MIRROR_SYNC",
    "RUN_BLOCKED",
    "FINAL_RECONCILIATION",
}


class LedgerError(Exception):
    """A deterministic, user-facing ledger failure."""


def now_utc() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def iso_time(value: dt.datetime) -> str:
    return value.astimezone(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def parse_time(value: Any, field: str) -> dt.datetime:
    if not isinstance(value, str) or not value.strip():
        raise LedgerError(f"{field} must be an ISO-8601 timestamp")
    text = value.strip().replace("Z", "+00:00")
    try:
        result = dt.datetime.fromisoformat(text)
    except ValueError as exc:
        raise LedgerError(f"{field} is not a valid ISO-8601 timestamp: {value!r}") from exc
    if result.tzinfo is None:
        raise LedgerError(f"{field} must include a timezone: {value!r}")
    return result.astimezone(dt.timezone.utc)


def decimal(value: Any, field: str) -> Decimal:
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise LedgerError(f"{field} must be numeric: {value!r}") from exc
    if not result.is_finite():
        raise LedgerError(f"{field} must be finite: {value!r}")
    return result


def rounded(value: Decimal, quant: Decimal = MONEY_QUANT) -> Decimal:
    return value.quantize(quant, rounding=ROUND_HALF_UP)


def json_number(value: Decimal | None, quant: Decimal = MONEY_QUANT) -> float | None:
    if value is None:
        return None
    return float(rounded(value, quant))


def event_type(event: dict[str, Any]) -> str:
    value = event.get("event_type")
    if not isinstance(value, str) or value not in SUPPORTED_EVENT_TYPES:
        raise LedgerError(f"unsupported event_type: {value!r}")
    return value


def load_events(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise LedgerError(f"ledger not found: {path}")
    events: list[dict[str, Any]] = []
    event_ids: set[str] = set()
    with path.open(encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, 1):
            line = raw_line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                raise LedgerError(f"invalid JSON at {path}:{line_number}: {exc.msg}") from exc
            if not isinstance(event, dict):
                raise LedgerError(f"ledger event at line {line_number} must be an object")
            event_id = event.get("event_id")
            if not isinstance(event_id, str) or not event_id.strip():
                raise LedgerError(f"ledger event at line {line_number} has no event_id")
            if event_id in event_ids:
                raise LedgerError(f"duplicate event_id: {event_id}")
            event_ids.add(event_id)
            event_type(event)
            parse_time(event.get("recorded_at"), f"{event_id}.recorded_at")
            parse_time(event.get("effective_at"), f"{event_id}.effective_at")
            events.append(event)
    if not events:
        raise LedgerError("ledger is empty; add COMPETITION_CONFIGURED first")
    return events


def corrected_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Apply explicit later corrections while retaining the original audit rows."""
    positions = {event["event_id"]: index for index, event in enumerate(events)}
    replacements: dict[str, dict[str, Any]] = {}
    for index, event in enumerate(events):
        if event["event_type"] != "CORRECTION":
            continue
        target = event.get("corrects_event_id")
        replacement = event.get("replacement")
        if not isinstance(target, str) or target not in positions:
            raise LedgerError(f"CORRECTION {event['event_id']} targets an unknown event")
        if positions[target] >= index:
            raise LedgerError(f"CORRECTION {event['event_id']} must target an earlier event")
        if not isinstance(replacement, dict):
            raise LedgerError(f"CORRECTION {event['event_id']} needs a replacement object")
        merged = dict(events[positions[target]])
        merged.update(replacement)
        merged["event_id"] = target
        if merged.get("event_type") == "CORRECTION":
            raise LedgerError(f"CORRECTION {event['event_id']} cannot replace with CORRECTION")
        event_type(merged)
        parse_time(merged.get("recorded_at"), f"{target}.recorded_at")
        parse_time(merged.get("effective_at"), f"{target}.effective_at")
        replacements[target] = merged
    return [
        replacements.get(event["event_id"], event)
        for event in events
        if event["event_type"] != "CORRECTION"
    ]


def position_template() -> dict[str, Decimal]:
    return {"quantity": Decimal("0"), "total_cost": Decimal("0"), "realized_pnl": Decimal("0")}


def apply_events(events: Iterable[dict[str, Any]]) -> dict[str, Any]:
    ordered = sorted(
        enumerate(events),
        key=lambda pair: (parse_time(pair[1]["effective_at"], "effective_at"), parse_time(pair[1]["recorded_at"], "recorded_at"), pair[0]),
    )
    configured = False
    competition_id = ""
    starting_cash = Decimal("0")
    cash = Decimal("0")
    phase = "proposal"
    benchmark_symbol = "SPY"
    positions: OrderedDict[str, dict[str, Decimal]] = OrderedDict()
    last_prices: dict[str, Decimal] = {}
    daily_curve: list[dict[str, Any]] = []
    seen_daily_dates: set[str] = set()
    benchmark_start: Decimal | None = None
    latest_benchmark: Decimal | None = None
    high_water_mark: Decimal | None = None
    latest_mark: dict[str, Any] | None = None
    total_turnover = Decimal("0")
    normal_turnover = Decimal("0")
    applied_event_ids: list[str] = []

    def require_configured(event_id: str) -> None:
        if not configured:
            raise LedgerError(f"{event_id} appears before COMPETITION_CONFIGURED")

    def calculate_equity() -> Decimal:
        for ticker, position in positions.items():
            if position["quantity"] > 0 and ticker not in last_prices:
                raise LedgerError(f"no mark price for open position {ticker}")
        return cash + sum((position["quantity"] * last_prices[ticker] for ticker, position in positions.items()), Decimal("0"))

    for _, event in ordered:
        kind = event["event_type"]
        event_id = event["event_id"]
        applied_event_ids.append(event_id)
        if kind == "COMPETITION_CONFIGURED":
            if configured:
                raise LedgerError("only one COMPETITION_CONFIGURED event is allowed")
            configured = True
            competition_id = str(event.get("competition_id", ""))
            if not competition_id:
                raise LedgerError("COMPETITION_CONFIGURED needs competition_id")
            starting_cash = decimal(event.get("starting_cash"), f"{event_id}.starting_cash")
            if starting_cash <= 0:
                raise LedgerError("starting_cash must be positive")
            cash = starting_cash
            benchmark_symbol = str(event.get("benchmark_symbol", "SPY")).upper()
            phase = str(event.get("phase", "proposal"))
            if phase not in {"proposal", "automatic"}:
                raise LedgerError(f"invalid initial phase: {phase}")
            continue

        require_configured(event_id)
        if kind == "PHASE_CHANGED":
            new_phase = str(event.get("phase", ""))
            if new_phase not in {"proposal", "automatic"}:
                raise LedgerError(f"invalid phase in {event_id}: {new_phase!r}")
            if new_phase == "automatic" and event.get("user_authorized") is not True:
                raise LedgerError(f"automatic phase requires explicit user_authorized=true in {event_id}")
            phase = new_phase
        elif kind in PASSIVE_EVENT_TYPES:
            continue
        elif kind == "FILL":
            ticker = str(event.get("ticker", "")).upper()
            side = str(event.get("side", "")).upper()
            quantity = decimal(event.get("quantity"), f"{event_id}.quantity")
            price = decimal(event.get("fill_price", event.get("price")), f"{event_id}.fill_price")
            fee = decimal(event.get("fee", "0"), f"{event_id}.fee")
            if not ticker or side not in {"BUY", "SELL"} or quantity <= 0 or price <= 0 or fee < 0:
                raise LedgerError(f"invalid FILL fields in {event_id}")
            notional = quantity * price
            total_turnover += notional
            if not event.get("risk_override", False):
                normal_turnover += notional
            position = positions.setdefault(ticker, position_template())
            if side == "BUY":
                cost = notional + fee
                if cash < cost:
                    raise LedgerError(f"insufficient cash for BUY {event_id}: need {cost}, have {cash}")
                cash -= cost
                position["quantity"] += quantity
                position["total_cost"] += cost
                last_prices[ticker] = price
            else:
                if quantity > position["quantity"]:
                    raise LedgerError(f"SELL exceeds position for {ticker} in {event_id}")
                average_cost = position["total_cost"] / position["quantity"] if position["quantity"] else Decimal("0")
                proceeds = notional - fee
                cash += proceeds
                position["quantity"] -= quantity
                position["total_cost"] -= average_cost * quantity
                position["realized_pnl"] += proceeds - average_cost * quantity
                last_prices[ticker] = price
                if position["quantity"] == 0:
                    position["total_cost"] = Decimal("0")
        elif kind == "DIVIDEND":
            amount = event.get("amount")
            if amount is None:
                quantity = decimal(event.get("quantity"), f"{event_id}.quantity")
                per_share = decimal(event.get("per_share"), f"{event_id}.per_share")
                amount = quantity * per_share
            amount_decimal = decimal(amount, f"{event_id}.amount")
            if amount_decimal < 0:
                raise LedgerError(f"DIVIDEND amount cannot be negative in {event_id}")
            cash += amount_decimal
        elif kind == "FEE":
            amount = decimal(event.get("amount"), f"{event_id}.amount")
            if amount < 0 or cash < amount:
                raise LedgerError(f"invalid FEE amount in {event_id}")
            cash -= amount
        elif kind == "SPLIT":
            ticker = str(event.get("ticker", "")).upper()
            ratio = decimal(event.get("ratio"), f"{event_id}.ratio")
            if ticker not in positions or ratio <= 0:
                raise LedgerError(f"invalid SPLIT in {event_id}")
            positions[ticker]["quantity"] *= ratio
            if ticker in last_prices:
                last_prices[ticker] /= ratio
        elif kind == "MARK":
            prices = event.get("prices")
            if not isinstance(prices, dict):
                raise LedgerError(f"MARK {event_id} needs a prices object")
            for ticker, value in prices.items():
                last_prices[str(ticker).upper()] = decimal(value, f"{event_id}.prices.{ticker}")
            benchmark_value = event.get("benchmark_price")
            if benchmark_value is not None:
                latest_benchmark = decimal(benchmark_value, f"{event_id}.benchmark_price")
            equity = calculate_equity()
            scope = str(event.get("scope", "intraday"))
            mark_time = parse_time(event["effective_at"], f"{event_id}.effective_at")
            latest_mark = {
                "event_id": event_id,
                "effective_at": iso_time(mark_time),
                "session_date": str(event.get("session_date", mark_time.date().isoformat())),
                "scope": scope,
                "equity": json_number(equity),
                "cash": json_number(cash),
                "benchmark_price": json_number(latest_benchmark),
            }
            if scope == "daily-close":
                session_date = latest_mark["session_date"]
                if session_date in seen_daily_dates:
                    raise LedgerError(f"duplicate daily-close MARK for {session_date}; use CORRECTION")
                seen_daily_dates.add(session_date)
                if latest_benchmark is not None and benchmark_start is None:
                    benchmark_start = latest_benchmark
                if high_water_mark is None or equity > high_water_mark:
                    high_water_mark = equity
                drawdown = (equity / high_water_mark - 1) if high_water_mark else Decimal("0")
                daily_curve.append(
                    {
                        "event_id": event_id,
                        "session_date": session_date,
                        "equity": json_number(equity),
                        "benchmark_price": json_number(latest_benchmark),
                        "drawdown_pct": json_number(drawdown * 100, PCT_QUANT),
                    }
                )
        elif kind == "CORRECTION":
            raise LedgerError("internal error: corrections must be applied before processing")
        else:
            raise LedgerError(f"unhandled event type: {kind}")

    if not configured:
        raise LedgerError("ledger has no COMPETITION_CONFIGURED event")
    equity = calculate_equity()
    latest_daily = daily_curve[-1] if daily_curve else None
    max_drawdown = min((Decimal(str(row["drawdown_pct"])) for row in daily_curve), default=Decimal("0"))
    current_drawdown = Decimal(str(latest_daily["drawdown_pct"])) if latest_daily else Decimal("0")
    benchmark_return = None
    if benchmark_start is not None and latest_daily and latest_daily.get("benchmark_price") is not None:
        benchmark_return = (Decimal(str(latest_daily["benchmark_price"])) / benchmark_start - 1) * 100
    state_positions: dict[str, Any] = {}
    for ticker, position in positions.items():
        if position["quantity"] <= 0:
            continue
        avg_cost = position["total_cost"] / position["quantity"]
        market_value = position["quantity"] * last_prices[ticker]
        state_positions[ticker] = {
            "quantity": json_number(position["quantity"], QTY_QUANT),
            "average_cost": json_number(avg_cost),
            "last_price": json_number(last_prices[ticker]),
            "market_value": json_number(market_value),
            "weight_pct": json_number(market_value / equity * 100, PCT_QUANT) if equity else 0.0,
            "realized_pnl": json_number(position["realized_pnl"]),
        }
    state = {
        "schema_version": 1,
        "competition_id": competition_id,
        "starting_cash": json_number(starting_cash),
        "phase": phase,
        "cash": json_number(cash),
        "portfolio_value": json_number(equity),
        "cash_weight_pct": json_number(cash / equity * 100, PCT_QUANT) if equity else 0.0,
        "cumulative_return_pct": json_number((equity / starting_cash - 1) * 100, PCT_QUANT),
        "current_drawdown_pct": json_number(current_drawdown, PCT_QUANT),
        "maximum_drawdown_pct": json_number(max_drawdown, PCT_QUANT),
        "benchmark": {
            "symbol": benchmark_symbol,
            "start_price": json_number(benchmark_start),
            "return_pct": json_number(benchmark_return, PCT_QUANT),
        },
        "last_mark": latest_mark,
        "daily_equity_curve": daily_curve,
        "normal_turnover_usd": json_number(normal_turnover),
        "normal_turnover_pct": json_number(normal_turnover / starting_cash * 100, PCT_QUANT) if starting_cash else 0.0,
        "total_turnover_usd": json_number(total_turnover),
        "events_processed": len(applied_event_ids),
        "positions": state_positions,
        "generated_at": iso_time(now_utc()),
    }
    return state


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False, prefix=f".{path.name}.") as handle:
        handle.write(text)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def fmt(value: Any, suffix: str = "") -> str:
    if value is None:
        return "not started"
    if isinstance(value, float):
        return f"{value:,.2f}{suffix}"
    return f"{value}{suffix}"


def render_dashboard(state: dict[str, Any]) -> str:
    rows = [
        ("Portfolio value", f"${state['portfolio_value']:,.2f}"),
        ("Cash", f"${state['cash']:,.2f}"),
        ("Cash weight", f"{state['cash_weight_pct']:.2f}%"),
        ("Cumulative return", f"{state['cumulative_return_pct']:.2f}%"),
        (f"{state['benchmark']['symbol']} operational benchmark", fmt(state["benchmark"]["return_pct"], "%")),
        ("Current drawdown", f"{state['current_drawdown_pct']:.2f}%"),
        ("Maximum drawdown", f"{state['maximum_drawdown_pct']:.2f}%"),
        ("Normal turnover", f"{state['normal_turnover_pct']:.2f}%"),
    ]
    lines = [
        "---",
        "kind: paper-portfolio-dashboard",
        f"competition_id: {state['competition_id']}",
        f"phase: {state['phase']}",
        f"as_of: {state['generated_at']}",
        f"portfolio_value: {state['portfolio_value']:.2f}",
        f"cash: {state['cash']:.2f}",
        f"cumulative_return_pct: {state['cumulative_return_pct']:.2f}",
        f"maximum_drawdown_pct: {state['maximum_drawdown_pct']:.2f}",
        "---",
        "",
        "# US ETF Paper Portfolio Dashboard",
        "",
        f"> [!info] {state['phase'].title()} Phase",
        "> The local Portfolio Ledger is canonical; browser pages provide read-only market evidence.",
        "> This dashboard is derived by `rebuild_portfolio.py`.",
        "",
        "## Snapshot",
        "",
        "| Metric | Value |",
        "|---|---:|",
    ]
    lines.extend(f"| {label} | {value} |" for label, value in rows)
    lines.extend(["", "## Positions", "", "| Ticker | Quantity | Last Price | Market Value | Weight | Realized P&L |", "|---|---:|---:|---:|---:|---:|"])
    if state["positions"]:
        for ticker, position in state["positions"].items():
            lines.append(
                f"| {ticker} | {position['quantity']:,.6f} | ${position['last_price']:,.2f} | ${position['market_value']:,.2f} | {position['weight_pct']:.2f}% | ${position['realized_pnl']:,.2f} |"
            )
    else:
        lines.append("| — | — | — | — | — | — |")
    lines.extend(["", "## Daily Equity Curve", ""])
    if state["daily_equity_curve"]:
        lines.extend(["| Session | Portfolio Equity | Benchmark Price | Drawdown |", "|---|---:|---:|---:|"])
        for row in state["daily_equity_curve"]:
            benchmark = "not marked" if row["benchmark_price"] is None else f"${row['benchmark_price']:,.2f}"
            lines.append(f"| {row['session_date']} | ${row['equity']:,.2f} | {benchmark} | {row['drawdown_pct']:.2f}% |")
    else:
        lines.append("No daily-close mark has been recorded yet.")
    lines.extend([
        "",
        "## Latest Runs",
        "",
        "```dataview",
        'TABLE analysis_at AS "Analysis at", run_status AS "Status", action_count AS "Actions", portfolio_value AS "Portfolio value"',
        'FROM "paper-portfolios/us-etf-competition/runs"',
        "SORT analysis_at DESC",
        "LIMIT 10",
        "```",
        "",
        "## Navigation",
        "",
        "- [Mandate and workflow](PROMPT.md)",
        "- [Configuration](config.yaml)",
        "- [Canonical ledger](ledger/events.jsonl)",
        "- [Derived state](state/portfolio.json)",
        "- [Latest verified prices](evidence/market-data/latest-prices.md)",
        "- [Price log](evidence/market-data/price-log.md)",
        "- [[ETF Performance Index]]",
        "",
        "This is an educational simulation, not personalized investment advice.",
        "",
    ])
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="validate/rebuild in memory without writing projections")
    parser.add_argument("--stdout", action="store_true", help="print the derived state JSON")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    try:
        source_events = load_events(root / "ledger" / "events.jsonl")
        state = apply_events(corrected_events(source_events))
        if not args.check:
            atomic_write(root / "state" / "portfolio.json", json.dumps(state, indent=2, sort_keys=True) + "\n")
            atomic_write(root / "dashboard.md", render_dashboard(state))
        if args.stdout:
            print(json.dumps(state, indent=2, sort_keys=True))
        else:
            print(json.dumps({"status": "PASS", "check_only": args.check, "events_processed": state["events_processed"], "portfolio_value": state["portfolio_value"]}))
        return 0
    except LedgerError as exc:
        print(json.dumps({"status": "BLOCKED", "action": "NO_TRADE", "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
