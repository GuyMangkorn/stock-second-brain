#!/usr/bin/env python3
"""Validate and project the batch-first ETF market-data workflow.

The batch is the immutable source envelope for one Portfolio Run.  The price
log and screen cache are deliberately small Markdown projections so scheduled
runs do not need to open every historical evidence file.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import math
import os
import re
import tempfile
from collections.abc import Mapping
from pathlib import Path
from statistics import median
from typing import Any


MARKET_DATA_RELATIVE = Path("evidence") / "market-data"
BATCHES_RELATIVE = MARKET_DATA_RELATIVE / "batches"
LOG_HEADER = (
    "| Observation ID | Run ID | Ticker | Exchange-qualified identity | Price | Currency | "
    "Price basis | Source as-of | Retrieved at | Source | Direct URL | Evidence | Status |"
)
LOG_SEPARATOR = "|---|---|---|---|---:|---|---|---|---|---|---|---|---|"
CACHE_HEADER = (
    "| Ticker | Exchange-qualified identity | Latest Price | Currency | Price Basis | "
    "Source As-of | Retrieved At | Recent Completed Closes | 1-Session Return | "
    "5-Session Return | 20-Session Return | Recent Drawdown | "
    "Five-Session Median Dollar Volume | Evidence Batch | Evidence ID | Status |"
)
CACHE_SEPARATOR = "|---|---|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|"
CACHE_KIND = "etf-price-screen-cache"
MAX_CLOSES = 21  # latest close plus the prior 20 sessions for a true 20-session return
KNOWN_FLAGS = ("LIQUIDITY_FAIL", "STALE", "PRELIMINARY", "REFRESH_REQUIRED")


class MarketDataError(ValueError):
    """A deterministic, user-facing market-data validation or projection error."""


def _fail(evidence_id: str, field: str, message: str) -> None:
    raise MarketDataError(f"{evidence_id}.{field}: {message}")


def _required_text(value: Any, evidence_id: str, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        _fail(evidence_id, field, "must be a non-empty string")
    text = value.strip()
    if text in {"...", "sha256:..."}:
        _fail(evidence_id, field, "placeholder text is not valid evidence")
    return text


def _parse_time(value: Any, evidence_id: str, field: str) -> dt.datetime:
    text = _required_text(value, evidence_id, field)
    normalized = text[:-1] + "+00:00" if text.endswith("Z") else text
    try:
        parsed = dt.datetime.fromisoformat(normalized)
    except ValueError as exc:
        _fail(evidence_id, field, f"invalid ISO-8601 timestamp: {text!r}")
        raise AssertionError("unreachable") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        _fail(evidence_id, field, "timestamp must include a timezone")
    return parsed.astimezone(dt.timezone.utc)


def _parse_date(value: Any, evidence_id: str, field: str) -> dt.date:
    text = _required_text(value, evidence_id, field)
    try:
        return dt.date.fromisoformat(text)
    except ValueError as exc:
        _fail(evidence_id, field, f"invalid session date: {text!r}")
        raise AssertionError("unreachable") from exc


def _finite_number(value: Any, evidence_id: str, field: str, *, positive: bool = False) -> float:
    if isinstance(value, bool):
        _fail(evidence_id, field, "must be numeric")
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        _fail(evidence_id, field, "must be numeric")
        raise AssertionError("unreachable") from exc
    if not math.isfinite(number):
        _fail(evidence_id, field, "must be finite")
    if positive and number <= 0:
        _fail(evidence_id, field, "must be greater than zero")
    return number


def _normalized_hash(value: Any, evidence_id: str, field: str) -> str:
    text = _required_text(value, evidence_id, field).lower()
    digest = text[7:] if text.startswith("sha256:") else text
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        _fail(evidence_id, field, "must be a SHA-256 digest")
    return f"sha256:{digest}"


def _validate_hash(envelope: Mapping[str, Any], evidence_id: str) -> None:
    visible = _required_text(envelope.get("visible_response_text"), evidence_id, "visible_response_text")
    expected = "sha256:" + hashlib.sha256(visible.encode("utf-8")).hexdigest()
    actual = _normalized_hash(envelope.get("content_hash"), evidence_id, "content_hash")
    if actual != expected:
        _fail(evidence_id, "content_hash", f"does not match visible_response_text; expected {expected}")
    if envelope.get("response_sha256") is not None:
        response_hash = _normalized_hash(envelope.get("response_sha256"), evidence_id, "response_sha256")
        if response_hash != expected:
            _fail(evidence_id, "response_sha256", f"does not match visible_response_text; expected {expected}")


def _as_mapping(value: Any, evidence_id: str, field: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        _fail(evidence_id, field, "must be an object")
    return value


def _validate_envelope(
    envelope: Mapping[str, Any],
    batch_cutoff: dt.datetime,
    evidence_ids: set[str],
    *,
    envelope_name: str,
    require_calendar_fields: bool = False,
) -> None:
    evidence_id = _required_text(envelope.get("evidence_id"), envelope_name, "evidence_id")
    if evidence_id in evidence_ids:
        _fail(evidence_id, "evidence_id", "must be unique within the batch")
    evidence_ids.add(evidence_id)
    _required_text(envelope.get("kind"), evidence_id, "kind")
    retrieved_at = _parse_time(envelope.get("retrieved_at"), evidence_id, "retrieved_at")
    if retrieved_at < dt.datetime.min.replace(tzinfo=dt.timezone.utc):
        _fail(evidence_id, "retrieved_at", "is outside the supported timestamp range")
    envelope_cutoff = _parse_time(envelope.get("information_cutoff_at"), evidence_id, "information_cutoff_at")
    if envelope_cutoff > batch_cutoff:
        _fail(evidence_id, "information_cutoff_at", "cannot be after the batch information cutoff")
    if envelope.get("post_period_data_used") is not False:
        _fail(evidence_id, "post_period_data_used", "must be false")
    _validate_hash(envelope, evidence_id)
    if require_calendar_fields:
        for field in ("provider", "discovery_method", "discovery_query", "direct_url", "page_title"):
            _required_text(envelope.get(field), evidence_id, field)
        if not str(envelope["direct_url"]).startswith(("http://", "https://")):
            _fail(evidence_id, "direct_url", "must be an HTTP(S) URL")
    else:
        for field in ("provider", "method"):
            _required_text(envelope.get(field), evidence_id, field)


def _validate_session_observations(observation: Mapping[str, Any], evidence_id: str) -> None:
    history = observation.get("five_session_observations")
    if history is None:
        return
    if not isinstance(history, list):
        _fail(evidence_id, "five_session_observations", "must be a list")
    seen_dates: set[str] = set()
    for index, item in enumerate(history):
        item_id = f"{evidence_id}.five_session_observations[{index}]"
        item_map = _as_mapping(item, evidence_id, f"five_session_observations[{index}]")
        session_date = _required_text(item_map.get("session_date"), item_id, "session_date")
        _parse_date(session_date, item_id, "session_date")
        if session_date in seen_dates:
            _fail(item_id, "session_date", "must be unique within an observation")
        seen_dates.add(session_date)
        _finite_number(item_map.get("close"), item_id, "close", positive=True)
        if item_map.get("volume_shares") is not None:
            _finite_number(item_map.get("volume_shares"), item_id, "volume_shares")
        if item_map.get("dollar_volume_usd") is not None:
            _finite_number(item_map.get("dollar_volume_usd"), item_id, "dollar_volume_usd")


def validate_batch(batch: Mapping[str, Any]) -> None:
    """Validate a schema-v2 market-data batch before any projection write."""

    if not isinstance(batch, Mapping):
        raise MarketDataError("batch: must be an object")
    run_id = str(batch.get("run_id") or "batch")
    if batch.get("schema_version") != 2:
        _fail(run_id, "schema_version", "must equal 2")
    if batch.get("kind") != "market-data-batch":
        _fail(run_id, "kind", "must equal market-data-batch")
    _required_text(batch.get("competition_id"), run_id, "competition_id")
    _required_text(batch.get("run_id"), run_id, "run_id")
    analysis_at = _parse_time(batch.get("analysis_at"), run_id, "analysis_at")
    information_cutoff = _parse_time(batch.get("information_cutoff_at"), run_id, "information_cutoff_at")
    _parse_time(batch.get("created_at"), run_id, "created_at")
    if information_cutoff > analysis_at:
        _fail(run_id, "information_cutoff_at", "cannot be after analysis_at")
    _required_text(batch.get("evidence_status"), run_id, "evidence_status")
    if batch.get("post_period_data_used") is not False:
        _fail(run_id, "post_period_data_used", "must be false")

    evidence_ids: set[str] = set()
    clock = _as_mapping(batch.get("clock"), run_id, "clock")
    _validate_envelope(clock, information_cutoff, evidence_ids, envelope_name=run_id, require_calendar_fields=False)
    calendar = _as_mapping(batch.get("calendar"), run_id, "calendar")
    _validate_envelope(calendar, information_cutoff, evidence_ids, envelope_name=run_id, require_calendar_fields=True)

    observations = batch.get("observations")
    if not isinstance(observations, list):
        _fail(run_id, "observations", "must be a list")
    for index, raw_observation in enumerate(observations):
        observation = _as_mapping(raw_observation, run_id, f"observations[{index}]")
        fallback_id = f"{run_id}:observation:{index}"
        evidence_id = _required_text(observation.get("evidence_id"), fallback_id, "evidence_id")
        if evidence_id in evidence_ids:
            _fail(evidence_id, "evidence_id", "must be unique within the batch")
        evidence_ids.add(evidence_id)
        for field in (
            "observation_kind",
            "ticker",
            "exchange_qualified_identity",
            "discovery_query",
            "direct_url",
            "page_title",
            "currency",
            "price_basis",
        ):
            _required_text(observation.get(field), evidence_id, field)
        for field in ("visible_response_text", "content_hash", "retrieved_at", "source_as_of"):
            if field == "content_hash":
                _normalized_hash(observation.get(field), evidence_id, field)
            elif field in {"retrieved_at", "source_as_of"}:
                _parse_time(observation.get(field), evidence_id, field)
            else:
                _required_text(observation.get(field), evidence_id, field)
        if not str(observation["direct_url"]).startswith(("http://", "https://")):
            _fail(evidence_id, "direct_url", "must be an HTTP(S) URL")
        _validate_hash(observation, evidence_id)
        source_as_of = _parse_time(observation.get("source_as_of"), evidence_id, "source_as_of")
        if source_as_of > information_cutoff:
            _fail(evidence_id, "source_as_of", "cannot be after information_cutoff_at")
        _parse_time(observation.get("retrieved_at"), evidence_id, "retrieved_at")
        _finite_number(observation.get("price"), evidence_id, "price", positive=True)
        if observation.get("post_period_data_used") is not False:
            _fail(evidence_id, "post_period_data_used", "must be false")
        price_basis = str(observation["price_basis"]).lower()
        if "completed-session" in price_basis:
            if not observation.get("latest_completed_session"):
                _fail(evidence_id, "latest_completed_session", "is required for completed-session prices")
            _parse_date(observation.get("latest_completed_session"), evidence_id, "latest_completed_session")
        if observation.get("median_daily_dollar_volume_usd") is not None:
            _finite_number(
                observation.get("median_daily_dollar_volume_usd"),
                evidence_id,
                "median_daily_dollar_volume_usd",
            )
        _validate_session_observations(observation, evidence_id)


def load_batch(path: Path) -> dict[str, Any]:
    """Load and validate a JSON batch from a staging path."""

    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise MarketDataError(f"batch file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise MarketDataError(f"invalid batch JSON at {path}: {exc.msg}") from exc
    if not isinstance(value, dict):
        raise MarketDataError(f"batch file at {path} must contain a JSON object")
    validate_batch(value)
    return value


def _canonical_bytes(batch: Mapping[str, Any]) -> bytes:
    return json.dumps(batch, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _safe_cell(value: Any) -> str:
    return str(value).replace("|", r"\|").replace("\n", " ").strip()


def _unescape_cell(value: str) -> str:
    return value.replace(r"\|", "|").strip()


def _split_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return []
    parts = re.split(r"(?<!\\)\|", stripped)
    if parts and parts[0] == "":
        parts = parts[1:]
    if parts and parts[-1] == "":
        parts = parts[:-1]
    return [_unescape_cell(part) for part in parts]


def _table(text: str, header_marker: str) -> tuple[list[str], list[list[str]], int] | None:
    lines = text.splitlines(keepends=True)
    for index, line in enumerate(lines):
        cells = _split_row(line)
        if not cells or header_marker not in cells:
            continue
        if index + 1 >= len(lines) or not _split_row(lines[index + 1]):
            continue
        rows: list[list[str]] = []
        cursor = index + 2
        while cursor < len(lines):
            row = _split_row(lines[cursor])
            if not row or len(row) != len(cells):
                break
            if all(set(cell.replace("-", "").replace(":", "")) <= {"", ":"} for cell in row):
                cursor += 1
                continue
            rows.append(row)
            cursor += 1
        return cells, rows, cursor
    return None


def _field(row: Mapping[str, str], *names: str, default: str = "not disclosed") -> str:
    for name in names:
        value = row.get(name.lower())
        if value is not None and value != "":
            return value
    return default


def _map_row(header: list[str], cells: list[str]) -> dict[str, str]:
    return {key.strip().lower(): value for key, value in zip(header, cells)}


def _number_or_none(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    if not text or text.lower() in {"not disclosed", "n/a", "na", "-"}:
        return None
    text = text.removesuffix("%").strip()
    try:
        result = float(text)
    except ValueError:
        return None
    return result if math.isfinite(result) else None


def _parse_series(value: str) -> list[tuple[dt.date, float]]:
    if not value or value.lower() == "not disclosed":
        return []
    result: dict[dt.date, float] = {}
    for part in value.split(";"):
        if ":" not in part:
            continue
        date_text, price_text = part.strip().split(":", 1)
        try:
            session_date = dt.date.fromisoformat(date_text.strip())
            price = float(price_text.strip())
        except (ValueError, TypeError):
            continue
        if math.isfinite(price) and price > 0:
            result[session_date] = price
    return sorted(result.items(), key=lambda item: item[0], reverse=True)


def _format_series(series: list[tuple[dt.date, float]]) -> str:
    if not series:
        return "not disclosed"
    return ";".join(f"{session_date.isoformat()}:{price:.2f}" for session_date, price in series[:MAX_CLOSES])


def _format_percent(value: float | None) -> str:
    return "not disclosed" if value is None else f"{value:.2f}%"


def _return_at(series: list[tuple[dt.date, float]], sessions_back: int) -> float | None:
    if len(series) <= sessions_back:
        return None
    latest = series[0][1]
    prior = series[sessions_back][1]
    if prior == 0:
        return None
    return (latest / prior - 1) * 100


def _cache_row_from_legacy(row: Mapping[str, str]) -> dict[str, Any]:
    evidence = _field(row, "evidence")
    run_id = _field(row, "run id", default="not disclosed")
    return {
        "ticker": _field(row, "ticker"),
        "identity": _field(row, "exchange-qualified identity"),
        "latest_price": _number_or_none(_field(row, "latest price", "price")),
        "currency": _field(row, "currency"),
        "price_basis": _field(row, "price basis"),
        "source_as_of": _field(row, "source as-of"),
        "retrieved_at": _field(row, "retrieved at"),
        "recent_closes": _parse_series(_field(row, "recent completed closes")),
        "one_return": _field(row, "1-session return"),
        "five_return": _field(row, "5-session return"),
        "twenty_return": _field(row, "20-session return"),
        "drawdown": _field(row, "recent drawdown"),
        "median_dollar_volume": _field(row, "five-session median dollar volume"),
        "evidence_batch": _field(row, "evidence batch", "evidence", default="not disclosed"),
        "evidence_id": _field(row, "evidence id", "run id", default=run_id),
        "status": _field(row, "status"),
        "legacy_evidence": evidence,
    }


def _parse_cache(text: str) -> dict[str, dict[str, Any]]:
    parsed = _table(text, "Ticker")
    if parsed is None:
        return {}
    header, rows, _ = parsed
    result: dict[str, dict[str, Any]] = {}
    for cells in rows:
        mapped = _map_row(header, cells)
        ticker = _field(mapped, "ticker", default="").upper()
        if not ticker:
            continue
        result[ticker] = _cache_row_from_legacy(mapped)
    return result


def _status_for_observation(observation: Mapping[str, Any], batch: Mapping[str, Any]) -> str:
    status = observation.get("status") or observation.get("evidence_status") or batch.get("evidence_status")
    if status:
        return str(status)
    liquidity = observation.get("admission_liquidity_gate")
    if liquidity and str(liquidity).upper() != "PASS":
        return f"LIQUIDITY_FAIL_{liquidity}"
    return "PRELIMINARY"


def _merge_status(previous: str, incoming: str) -> str:
    if not previous:
        return incoming
    if "LIQUIDITY_FAIL" in previous and "LIQUIDITY_FAIL" not in incoming:
        return f"{incoming}_LIQUIDITY_FAIL"
    return incoming


def _observation_is_completed(observation: Mapping[str, Any]) -> bool:
    basis = str(observation.get("price_basis", "")).lower()
    return "completed-session" in basis and "intraday" not in basis


def _observation_sort_key(observation: Mapping[str, Any]) -> tuple[int, dt.datetime, int, str]:
    evidence_id = str(observation.get("evidence_id", ""))
    try:
        source_as_of = _parse_time(observation.get("source_as_of"), evidence_id or "observation", "source_as_of")
    except MarketDataError:
        source_as_of = dt.datetime.min.replace(tzinfo=dt.timezone.utc)
    return (
        1 if _observation_is_completed(observation) else 0,
        source_as_of,
        1 if observation.get("decision_reference") is True else 0,
        evidence_id,
    )


def _history_from_observation(observation: Mapping[str, Any]) -> list[tuple[dt.date, float]]:
    history: dict[dt.date, float] = {}
    raw_history = observation.get("five_session_observations") or []
    if isinstance(raw_history, list):
        for item in raw_history:
            if not isinstance(item, Mapping):
                continue
            try:
                session_date = dt.date.fromisoformat(str(item.get("session_date")))
                close = float(item.get("close"))
            except (TypeError, ValueError):
                continue
            if math.isfinite(close) and close > 0:
                history[session_date] = close
    if _observation_is_completed(observation) and observation.get("latest_completed_session"):
        try:
            session_date = dt.date.fromisoformat(str(observation["latest_completed_session"]))
            close = float(observation["price"])
        except (TypeError, ValueError):
            pass
        else:
            if math.isfinite(close) and close > 0:
                history[session_date] = close
    return sorted(history.items(), key=lambda item: item[0], reverse=True)


def _dollar_volume_median(observation: Mapping[str, Any]) -> float | None:
    raw_history = observation.get("five_session_observations") or []
    values: list[float] = []
    if isinstance(raw_history, list):
        for item in raw_history[:5]:
            if not isinstance(item, Mapping):
                continue
            explicit = _number_or_none(item.get("dollar_volume_usd"))
            close = _number_or_none(item.get("close"))
            volume = _number_or_none(item.get("volume_shares"))
            value = explicit if explicit is not None else (close * volume if close is not None and volume is not None else None)
            if value is not None and math.isfinite(value):
                values.append(value)
    if values:
        return float(median(values))
    return _number_or_none(observation.get("median_daily_dollar_volume_usd"))


def _choose_observations(observations: list[Mapping[str, Any]]) -> dict[str, Mapping[str, Any]]:
    grouped: dict[str, list[Mapping[str, Any]]] = {}
    for observation in observations:
        ticker = str(observation.get("ticker", "")).upper()
        if ticker:
            grouped.setdefault(ticker, []).append(observation)
    return {ticker: max(items, key=_observation_sort_key) for ticker, items in grouped.items()}


def _render_cache(rows: Mapping[str, Mapping[str, Any]], competition_id: str, updated_at: str) -> str:
    lines = [
        "---",
        f"kind: {CACHE_KIND}",
        f"competition_id: {competition_id}",
        "source_policy: browser-direct-web",
        "cache_role: preliminary-screen-only",
        f"updated_at: \"{updated_at}\"",
        "---",
        "",
        "# ETF Price Screen Cache",
        "",
        "ใช้สำหรับ preliminary screening เท่านั้น; ก่อน BUY ต้อง refresh direct quote และผ่าน admission gates.",
        "",
        CACHE_HEADER,
        CACHE_SEPARATOR,
    ]
    for ticker in sorted(rows):
        row = rows[ticker]
        series = list(row.get("recent_closes") or [])
        one_return = _return_at(series, 1)
        five_return = _return_at(series, 5)
        twenty_return = _return_at(series, 20)
        rolling_high = max((price for _, price in series), default=None)
        latest_price = _number_or_none(row.get("latest_price"))
        drawdown = None if latest_price is None or rolling_high in {None, 0} else (latest_price / rolling_high - 1) * 100
        median_volume = _number_or_none(row.get("median_dollar_volume"))
        evidence_batch = str(row.get("evidence_batch") or "not disclosed")
        lines.append(
            "| "
            + " | ".join(
                _safe_cell(value)
                for value in (
                    ticker,
                    row.get("identity", "not disclosed"),
                    "not disclosed" if latest_price is None else f"{latest_price:.2f}",
                    row.get("currency", "not disclosed"),
                    row.get("price_basis", "not disclosed"),
                    row.get("source_as_of", "not disclosed"),
                    row.get("retrieved_at", "not disclosed"),
                    _format_series(series),
                    _format_percent(one_return),
                    _format_percent(five_return),
                    _format_percent(twenty_return),
                    _format_percent(drawdown),
                    "not disclosed" if median_volume is None else f"{median_volume:.2f}",
                    evidence_batch,
                    row.get("evidence_id", "not disclosed"),
                    row.get("status", "PRELIMINARY"),
                )
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def merge_screen_cache(cache_text: str, batch: Mapping[str, Any]) -> str:
    """Merge validated quote observations into one bounded row per ticker."""

    validate_batch(batch)
    rows = _parse_cache(cache_text)
    chosen = _choose_observations([observation for observation in batch["observations"] if isinstance(observation, Mapping)])
    for ticker, observation in chosen.items():
        previous = rows.get(ticker, {})
        history: dict[dt.date, float] = {date: price for date, price in previous.get("recent_closes", [])}
        for date, price in _history_from_observation(observation):
            history[date] = price
        series = sorted(history.items(), key=lambda item: item[0], reverse=True)[:MAX_CLOSES]
        incoming_status = _status_for_observation(observation, batch)
        status = _merge_status(str(previous.get("status", "")), incoming_status)
        median_volume = _dollar_volume_median(observation)
        if median_volume is None:
            median_volume = previous.get("median_dollar_volume", "not disclosed")
        rows[ticker] = {
            "ticker": ticker,
            "identity": observation.get("exchange_qualified_identity", previous.get("identity", "not disclosed")),
            "latest_price": observation.get("price"),
            "currency": observation.get("currency", previous.get("currency", "not disclosed")),
            "price_basis": observation.get("price_basis", previous.get("price_basis", "not disclosed")),
            "source_as_of": observation.get("source_as_of", previous.get("source_as_of", "not disclosed")),
            "retrieved_at": observation.get("retrieved_at", previous.get("retrieved_at", "not disclosed")),
            "recent_closes": series,
            "median_dollar_volume": median_volume,
            "evidence_batch": f"[batch quote](batches/{batch['run_id']}.json)",
            "evidence_id": observation.get("evidence_id", "not disclosed"),
            "status": status,
        }
    updated_at = str(batch.get("created_at") or batch.get("analysis_at"))
    return _render_cache(rows, str(batch.get("competition_id", "not disclosed")), updated_at)


def _price_log_rows(text: str) -> tuple[list[str], list[dict[str, str]], int]:
    parsed = _table(text, "Observation ID")
    if parsed is None:
        return [], [], 0
    header, cells_rows, insert_at = parsed
    rows = [_map_row(header, cells) for cells in cells_rows]
    return header, rows, insert_at


def _row_sort_key(row: Mapping[str, str]) -> tuple[str, str, str]:
    return (
        _field(row, "source as-of", default=""),
        _field(row, "retrieved at", default=""),
        _field(row, "observation id", default=""),
    )


def _cache_row_from_log_rows(ticker: str, log_rows: list[dict[str, str]]) -> dict[str, Any]:
    ordered = sorted(log_rows, key=_row_sort_key, reverse=True)
    completed = [
        row
        for row in ordered
        if "completed-session" in _field(row, "price basis", default="").lower()
        and "intraday" not in _field(row, "price basis", default="").lower()
    ]
    basis = _field(completed[0], "price basis") if completed else _field(ordered[0], "price basis")
    history_map: dict[dt.date, float] = {}
    for row in completed:
        if _field(row, "price basis") != basis:
            continue
        try:
            source_as_of = _field(row, "source as-of")
            session_date = dt.date.fromisoformat(source_as_of[:10])
            price = float(_field(row, "price"))
        except (TypeError, ValueError):
            continue
        if math.isfinite(price) and price > 0:
            history_map.setdefault(session_date, price)
    series = sorted(history_map.items(), key=lambda item: item[0], reverse=True)[:MAX_CLOSES]
    latest = ordered[0]
    evidence_refs: list[str] = []
    for row in ordered:
        evidence = _field(row, "evidence", default="not disclosed")
        if evidence not in evidence_refs:
            evidence_refs.append(evidence)
    return {
        "ticker": ticker,
        "identity": _field(latest, "exchange-qualified identity"),
        "latest_price": _number_or_none(_field(latest, "price")),
        "currency": _field(latest, "currency"),
        "price_basis": _field(latest, "price basis"),
        "source_as_of": _field(latest, "source as-of"),
        "retrieved_at": _field(latest, "retrieved at"),
        "recent_closes": series,
        "median_dollar_volume": "not disclosed",
        "evidence_batch": "; ".join(evidence_refs) if evidence_refs else "not disclosed",
        "evidence_id": _field(latest, "observation id"),
        "status": _field(latest, "status"),
    }


def bootstrap_screen_cache(log_text: str) -> str:
    """Build the screen cache once from the complete append-only price log."""

    _, log_rows, _ = _price_log_rows(log_text)
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in log_rows:
        ticker = _field(row, "ticker", default="").upper()
        if ticker:
            grouped.setdefault(ticker, []).append(row)
    rows = {ticker: _cache_row_from_log_rows(ticker, values) for ticker, values in grouped.items() if values}
    retrieved_values = [_field(row, "retrieved at", default="") for row in log_rows]
    updated_at = max(retrieved_values, default="not disclosed")
    competition_id = "not disclosed"
    if log_text:
        match = re.search(r"^competition_id:\s*(.+?)\s*$", log_text, flags=re.MULTILINE)
        if match:
            competition_id = match.group(1).strip().strip('"')
    return _render_cache(rows, competition_id, updated_at)


def render_price_log_rows(batch: Mapping[str, Any]) -> list[str]:
    """Render one compact Markdown row per observation in a validated batch."""

    validate_batch(batch)
    rows: list[str] = []
    for observation in batch["observations"]:
        evidence_id = str(observation["evidence_id"])
        observation_id = f"obs-{batch['run_id']}-{evidence_id.rsplit(':', 1)[-1]}"
        evidence_path = f"batches/{batch['run_id']}.json"
        status = _status_for_observation(observation, batch)
        values = (
            observation_id,
            batch["run_id"],
            observation["ticker"],
            observation["exchange_qualified_identity"],
            f"{float(observation['price']):.2f}",
            observation["currency"],
            observation["price_basis"],
            observation["source_as_of"],
            observation["retrieved_at"],
            observation.get("provider", "not disclosed"),
            observation["direct_url"],
            f"[batch quote]({evidence_path}) ({evidence_id})",
            status,
        )
        rows.append("| " + " | ".join(_safe_cell(value) for value in values) + " |")
    return rows


def _ensure_log_text(text: str, competition_id: str) -> str:
    if _table(text, "Observation ID") is not None:
        return text
    return (
        "---\n"
        "kind: etf-price-log\n"
        f"competition_id: {competition_id}\n"
        "append_only: true\n"
        "canonical_history: true\n"
        "source_policy: browser-direct-web\n"
        "---\n\n"
        "# ETF Price Log\n\n"
        "" + LOG_HEADER + "\n" + LOG_SEPARATOR + "\n" + text
    )


def _append_rows_to_log(text: str, rows: list[str], competition_id: str) -> tuple[str, int]:
    text = _ensure_log_text(text, competition_id)
    lines = text.splitlines(keepends=True)
    table_info = _table(text, "Observation ID")
    if table_info is None:
        raise MarketDataError("price-log.table: unable to locate the canonical table")
    log_header, existing_rows_cells, insert_at = table_info
    existing_rows = [_map_row(log_header, cells) for cells in existing_rows_cells]
    existing_text = "\n".join(
        f"{row.get('evidence', '')} {row.get('observation id', '')}" for row in existing_rows
    )
    new_rows: list[str] = []
    duplicate_count = 0
    for row in rows:
        evidence_match = re.search(r"\(([^()]+:quote:[^)]+)\)", row)
        evidence_id = evidence_match.group(1) if evidence_match else row
        if evidence_id in existing_text or evidence_id in text:
            duplicate_count += 1
            continue
        new_rows.append(row)
    if not new_rows:
        return text, duplicate_count
    insertion = "".join(row + "\n" for row in new_rows)
    prefix = "".join(lines[:insert_at])
    suffix = "".join(lines[insert_at:])
    if prefix and not prefix.endswith("\n"):
        prefix += "\n"
    return prefix + insertion + suffix, duplicate_count


def _atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
    except Exception:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def _existing_canonical(path: Path) -> bytes | None:
    if not path.exists():
        return None
    try:
        existing = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise MarketDataError(f"immutable batch at {path} is not valid JSON") from exc
    if not isinstance(existing, dict):
        raise MarketDataError(f"immutable batch at {path} must contain a JSON object")
    return _canonical_bytes(existing)


def _summary(batch: Mapping[str, Any], *, duplicate: bool, created: int = 0, duplicate_observations: int = 0) -> dict[str, Any]:
    return {
        "status": "PASS",
        "run_id": batch["run_id"],
        "observations": len(batch["observations"]),
        "batch_files_created": created,
        "duplicate_batch": duplicate,
        "duplicate_observations": duplicate_observations,
    }


def record_batch(root: Path, batch_path: Path, *, check_only: bool = False) -> dict[str, Any]:
    """Record one immutable batch and update the two compact projections."""

    batch = load_batch(batch_path)
    destination = root / BATCHES_RELATIVE / f"{batch['run_id']}.json"
    canonical = _canonical_bytes(batch)
    existing = _existing_canonical(destination)
    if existing is not None:
        if existing != canonical:
            raise MarketDataError(f"immutable batch conflict at {destination}; refusing to overwrite")
        return _summary(batch, duplicate=True)
    if check_only:
        return _summary(batch, duplicate=False)

    market_data = root / MARKET_DATA_RELATIVE
    log_path = market_data / "price-log.md"
    cache_path = market_data / "latest-prices.md"
    current_log = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    current_cache = cache_path.read_text(encoding="utf-8") if cache_path.exists() else ""
    log_rows = render_price_log_rows(batch)
    updated_log, duplicate_observations = _append_rows_to_log(current_log, log_rows, str(batch["competition_id"]))
    updated_cache = merge_screen_cache(current_cache, batch)

    _atomic_write(destination, canonical)
    _atomic_write(log_path, updated_log.encode("utf-8"))
    _atomic_write(cache_path, updated_cache.encode("utf-8"))
    return _summary(batch, duplicate=False, created=1, duplicate_observations=duplicate_observations)


def bootstrap_cache(root: Path, *, check_only: bool = False) -> dict[str, Any]:
    """Rebuild the derived cache from the complete log in recovery mode."""

    log_path = root / MARKET_DATA_RELATIVE / "price-log.md"
    if not log_path.exists():
        raise MarketDataError(f"price log not found: {log_path}")
    log_text = log_path.read_text(encoding="utf-8")
    _, log_rows, _ = _price_log_rows(log_text)
    rendered = bootstrap_screen_cache(log_text)
    tickers = {row.get("ticker", "").upper() for row in log_rows if row.get("ticker")}
    if not check_only:
        _atomic_write(root / MARKET_DATA_RELATIVE / "latest-prices.md", rendered.encode("utf-8"))
    return {
        "status": "PASS",
        "mode": "bootstrap-cache",
        "input_price_rows": len(log_rows),
        "projected_ticker_rows": len(tickers),
        "check_only": check_only,
    }
