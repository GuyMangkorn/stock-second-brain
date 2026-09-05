#!/usr/bin/env python3
"""Capture ETF.com quotes for inclusion in a reviewed portfolio evidence batch.

Outputs a staging packet, not a complete market-data batch or settlement input.
Uses curl for the HTTP client tested with this endpoint; no third-party packages.
"""
import argparse
import datetime as dt
import email.utils
import fcntl
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import tempfile
import time

URL = "https://api-prod.etf.com//v2/quotes/delayedquotes?tickers="
INTERVAL = 10
TTL = 900


def normalize(raw, ticker, retrieved):
    rows = json.loads(raw)
    if not isinstance(rows, list) or len(rows) != 1:
        raise ValueError("expected one quote")
    quote = rows[0]
    if quote.get("Outcome") != "Success" or quote.get("Identifier") != ticker:
        raise ValueError("quote outcome/identity mismatch")
    if quote.get("Currency") != "USD" or quote.get("TradingHalted") is not False:
        raise ValueError("currency mismatch or halted/unknown trading status")
    price = quote.get("Last")
    if isinstance(price, bool) or not isinstance(price, (int, float)) or not math.isfinite(price) or price <= 0:
        raise ValueError("invalid last price")
    offset = quote["UTCOffset"]
    if isinstance(offset, bool) or not isinstance(offset, (int, float)):
        raise ValueError("invalid UTC offset")
    stamp = dt.datetime.strptime(quote["Date"] + " " + quote["Time"], "%m/%d/%Y %I:%M:%S %p")
    stamp = stamp.replace(tzinfo=dt.timezone(dt.timedelta(hours=offset)))
    if stamp > dt.datetime.fromisoformat(retrieved):
        raise ValueError("future quote timestamp")
    security = quote["Security"]
    if security.get("Symbol") != ticker or not security.get("Market"):
        raise ValueError("missing exchange-qualified identity")
    return {
        "observation_kind": "delayed-quote", "ticker": ticker,
        "exchange_qualified_identity": security["Market"] + ":" + ticker,
        "discovery_query": URL + ticker, "direct_url": URL + ticker,
        "page_title": "ETF.com delayed quote: " + ticker,
        "provider": "ETF.com", "retrieved_at": retrieved,
        "source_as_of": stamp.isoformat(), "currency": "USD", "price": price,
        "price_basis": "delayed last trade; adjustment basis unverified",
        "visible_response_text": raw,
        "content_hash": "sha256:" + hashlib.sha256(raw.encode()).hexdigest(),
        "post_period_data_used": False, "status": "REQUIRES_REVIEW",
        "source_message": quote.get("Message"),
    }


def cooldown(headers, now):
    for line in headers.splitlines():
        if line.lower().startswith("retry-after:"):
            value = line.split(":", 1)[1].strip()
            try:
                return now + max(TTL, int(value))
            except ValueError:
                try:
                    return max(now + TTL, email.utils.parsedate_to_datetime(value).timestamp())
                except (ValueError, TypeError, OverflowError):
                    pass
    return now + TTL


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--symbols", required=True, help="comma-separated US ETF tickers")
    parser.add_argument("--output", type=Path, required=True, help="new staging packet path")
    args = parser.parse_args()
    symbols = list(dict.fromkeys(s.strip().upper() for s in args.symbols.split(",")))
    if not symbols or any(not re.fullmatch(r"[A-Z][A-Z0-9.-]{0,14}", s) for s in symbols):
        parser.error("invalid ticker")
    if args.output.exists():
        parser.error("output exists; refusing to overwrite")
    runtime = Path(__file__).resolve().parents[1] / ".runtime" / "etf-quotes"
    runtime.mkdir(parents=True, exist_ok=True)
    packet = {"kind": "etf-quote-staging-packet", "observations": [], "gaps": []}
    with (runtime / "lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        state_path = runtime / "state.json"
        state = json.loads(state_path.read_text()) if state_path.exists() else {}
        for ticker in symbols:
            cache = runtime / (ticker + ".json")
            try:
                if cache.exists():
                    saved = json.loads(cache.read_text())
                    if 0 <= time.time() - saved["captured_epoch"] < TTL:
                        packet["observations"].append(dict(saved["observation"], cache_hit=True))
                        continue
                if time.time() < state.get("blocked_until", 0):
                    raise ValueError("API cooldown active; use ETF.com page then legacy sources")
                time.sleep(max(0, state.get("last_request", 0) + INTERVAL - time.time()))
                state["last_request"] = time.time()
                state_path.write_text(json.dumps(state))
                with tempfile.TemporaryDirectory() as tmp:
                    body, headers = Path(tmp) / "body", Path(tmp) / "headers"
                    result = subprocess.run([
                        "curl", "--http1.1", "--silent", "--show-error", "--max-time", "25",
                        "--user-agent", "PostmanRuntime/2.5.0", "--output", str(body),
                        "--dump-header", str(headers), "--write-out", "%{http_code}", URL + ticker,
                    ], capture_output=True, text=True, timeout=30)
                    code = result.stdout.strip()
                    if code in {"403", "429"}:
                        state["blocked_until"] = cooldown(headers.read_text(), time.time())
                        state_path.write_text(json.dumps(state))
                    if result.returncode or code != "200":
                        raise ValueError("HTTP " + code + "; " + result.stderr[:200])
                    raw = body.read_bytes().decode("utf-8")
                retrieved = dt.datetime.now(dt.timezone.utc).isoformat()
                observation = normalize(raw, ticker, retrieved)
                cache.write_text(json.dumps({"captured_epoch": time.time(), "observation": observation}))
                packet["observations"].append(dict(observation, cache_hit=False))
            except (ValueError, KeyError, TypeError, OSError, subprocess.TimeoutExpired) as exc:
                packet["gaps"].append({"ticker": ticker, "reason": str(exc),
                                       "fallback_url": "https://www.etf.com/" + ticker})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as handle:
        json.dump(packet, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(json.dumps({"output": str(args.output), "quotes": len(packet["observations"]),
                      "gaps": packet["gaps"]}))
    return 2 if packet["gaps"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
