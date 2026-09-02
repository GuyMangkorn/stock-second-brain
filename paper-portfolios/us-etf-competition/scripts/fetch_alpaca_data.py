#!/usr/bin/env python3
"""Fetch immutable Alpaca market evidence through documented GET endpoints.

The script deliberately does not place orders. It writes one new JSON envelope
per successful fetch and refuses to overwrite existing evidence.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


DATA_BASE_URL = "https://data.alpaca.markets"
PAPER_BASE_URL = "https://paper-api.alpaca.markets"
SYMBOL_RE = re.compile(r"^[A-Z][A-Z0-9.-]*$")


class EvidenceError(Exception):
    """Structured user-facing fetch failure."""


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def iso_time(value: dt.datetime) -> str:
    return value.astimezone(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def normalize_symbols(raw: str | None) -> list[str]:
    if not raw:
        return []
    symbols: list[str] = []
    for value in raw.split(","):
        symbol = value.strip().upper()
        if not symbol or not SYMBOL_RE.fullmatch(symbol):
            raise EvidenceError(f"invalid symbol: {value!r}")
        if symbol not in symbols:
            symbols.append(symbol)
    return symbols


def compact_params(values: dict[str, Any]) -> dict[str, str]:
    return {
        key: str(value)
        for key, value in values.items()
        if value is not None and value != ""
    }


def build_request(args: argparse.Namespace) -> tuple[str, str, dict[str, str]]:
    """Return base URL, endpoint path, and non-secret query parameters."""
    kind = args.kind
    if kind == "clock":
        return PAPER_BASE_URL, "/v2/clock", {}
    if kind == "calendar":
        params = compact_params({"start": args.start, "end": args.end, "date_type": "TRADING"})
        return PAPER_BASE_URL, "/v2/calendar", params
    if kind == "bars":
        symbols = normalize_symbols(args.symbols)
        if not symbols:
            raise EvidenceError("bars requires at least one symbol")
        params = compact_params(
            {
                "symbols": ",".join(symbols),
                "timeframe": args.timeframe,
                "start": args.start,
                "end": args.end,
                "asof": args.asof,
                "adjustment": args.adjustment,
                "feed": args.feed,
                "currency": "USD",
                "limit": args.limit,
                "sort": "asc",
            }
        )
        return DATA_BASE_URL, "/v2/stocks/bars", params
    if kind == "snapshots":
        symbols = normalize_symbols(args.symbols)
        if not symbols:
            raise EvidenceError("snapshots requires at least one symbol")
        params = compact_params({"symbols": ",".join(symbols), "feed": args.feed})
        return DATA_BASE_URL, "/v2/stocks/snapshots", params
    if kind == "corporate-actions":
        symbols = normalize_symbols(args.symbols)
        params = compact_params(
            {
                "symbols": ",".join(symbols) if symbols else None,
                "start": args.start,
                "end": args.end,
                "region": "us",
            }
        )
        return DATA_BASE_URL, "/v1/corporate-actions", params
    raise EvidenceError(f"unsupported evidence kind: {kind}")


def credentials() -> tuple[str, str]:
    key_id = os.environ.get("APCA_API_KEY_ID", "").strip()
    secret = os.environ.get("APCA_API_SECRET_KEY", "").strip()
    if not key_id or not secret:
        raise EvidenceError(
            "missing APCA_API_KEY_ID or APCA_API_SECRET_KEY; keep credentials outside the repository"
        )
    return key_id, secret


def fetch_json(url: str, key_id: str, secret: str, timeout: float) -> Any:
    request = urllib.request.Request(
        url,
        method="GET",
        headers={
            "Accept": "application/json",
            "APCA-API-KEY-ID": key_id,
            "APCA-API-SECRET-KEY": secret,
            "User-Agent": "stock-second-brain-etf-paper-portfolio/1",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise EvidenceError(f"Alpaca HTTP {exc.code}: {detail[:500]}") from exc
    except urllib.error.URLError as exc:
        raise EvidenceError(f"Alpaca request failed: {exc.reason}") from exc
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise EvidenceError("Alpaca response was not valid JSON") from exc


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def safe_write_json(path: Path, value: Any) -> None:
    if path.exists():
        raise EvidenceError(f"refusing to overwrite evidence: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False, prefix=f".{path.name}."
    ) as handle:
        json.dump(value, handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def default_root() -> Path:
    return Path(__file__).resolve().parents[1]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=default_root())
    parser.add_argument("--output", type=Path)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--dry-run", action="store_true", help="print the documented request without fetching")
    subparsers = parser.add_subparsers(dest="kind", required=True)

    subparsers.add_parser("clock")

    calendar = subparsers.add_parser("calendar")
    calendar.add_argument("--start", required=True)
    calendar.add_argument("--end", required=True)

    bars = subparsers.add_parser("bars")
    bars.add_argument("--symbols", required=True)
    bars.add_argument("--timeframe", default="1Day")
    bars.add_argument("--start", required=True)
    bars.add_argument("--end", required=True)
    bars.add_argument("--asof", help="optional data availability cutoff, YYYY-MM-DD")
    bars.add_argument("--adjustment", choices=["raw", "split", "dividend", "spin-off", "all"], default="all")
    bars.add_argument("--feed", choices=["iex", "sip"], default="sip")
    bars.add_argument("--limit", type=int, default=10000)

    snapshots = subparsers.add_parser("snapshots")
    snapshots.add_argument("--symbols", required=True)
    snapshots.add_argument("--feed", choices=["iex", "sip"], default="iex")

    actions = subparsers.add_parser("corporate-actions")
    actions.add_argument("--symbols")
    actions.add_argument("--start", required=True)
    actions.add_argument("--end", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        base_url, endpoint, params = build_request(args)
        query = urllib.parse.urlencode(params)
        url = f"{base_url}{endpoint}" + (f"?{query}" if query else "")
        if args.dry_run:
            print(json.dumps({"method": "GET", "endpoint": endpoint, "params": params, "url": url}, indent=2))
            return 0

        requested_at = utc_now()
        key_id, secret = credentials()
        payload = fetch_json(url, key_id, secret, args.timeout)
        received_at = utc_now()
        payload_hash = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        envelope = {
            "schema_version": 1,
            "provider": "Alpaca",
            "method": "GET",
            "kind": args.kind,
            "endpoint": endpoint,
            "params": params,
            "requested_at": iso_time(requested_at),
            "received_at": iso_time(received_at),
            "response_sha256": payload_hash,
            "response": payload,
        }
        if args.output:
            output = args.output if args.output.is_absolute() else args.root / args.output
        else:
            day = received_at.strftime("%Y-%m-%d")
            stamp = received_at.strftime("%Y%m%dT%H%M%SZ")
            output = args.root / "evidence" / "market-data" / day / f"{args.kind}_{stamp}_{payload_hash[:12]}.json"
        safe_write_json(output, envelope)
        print(json.dumps({"status": "PASS", "path": str(output), "response_sha256": payload_hash}))
        return 0
    except EvidenceError as exc:
        print(json.dumps({"status": "BLOCKED", "action": "NO_TRADE", "error": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
