#!/usr/bin/env python3
"""CLI for recording one immutable market-data batch and its projections."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from market_data_pipeline import MarketDataError, bootstrap_cache, record_batch


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="portfolio project root")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--batch", type=Path, help="captured batch JSON staging path")
    mode.add_argument("--bootstrap-cache", action="store_true", help="rebuild latest-prices.md from price-log.md")
    parser.add_argument("--check", action="store_true", help="validate and report without changing project files")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.bootstrap_cache:
            summary = bootstrap_cache(args.root, check_only=args.check)
        else:
            summary = record_batch(args.root, args.batch, check_only=args.check)
    except MarketDataError as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
