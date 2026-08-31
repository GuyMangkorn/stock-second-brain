#!/usr/bin/env python3
"""Deterministic Markdown Research Queue command surface.

The queue deliberately has one public boundary: the commands in this module.
Project-scoped skills orchestrate these commands, while this module owns card
schema, intake normalization, state transitions, leases, recovery, and result
routing.  It uses only the Python standard library so it can run from a saved
Obsidian checkout without a virtualenv.
"""

from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import hashlib
import json
import os
import re
import secrets
import shlex
import subprocess
import sys
import tempfile
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping, Sequence


STATUS_READY = "Ready"
STATUS_IN_PROGRESS = "In Progress"
STATUS_BLOCKED = "Blocked"
STATUS_DONE = "Done"
STATUS_CANCELLED = "Cancelled"
CARD_STATUSES = {
    STATUS_READY,
    STATUS_IN_PROGRESS,
    STATUS_BLOCKED,
    STATUS_DONE,
    STATUS_CANCELLED,
}
ACTIVE_STATUSES = {STATUS_READY, STATUS_IN_PROGRESS, STATUS_BLOCKED}
TERMINAL_STATUSES = {STATUS_DONE, STATUS_CANCELLED}
SUPPORTED_EXECUTION_PROFILES = {"interactive-delegated", "scheduled-inline"}
SUPPORTED_ETF_WORKFLOW = "check-etf-performance"
FUTURE_STOCK_WORKFLOW = "official-source-stock-research"
HANDOFF_FIELDS = {
    "status",
    "scope",
    "durable_write",
    "exhausted",
    "confirmation",
    "code",
    "reason",
}
HANDOFF_STATUSES = {"PASS", "WARNING", "CHANGES_REQUIRED", "BLOCKED", "ERROR"}
HANDOFF_SCOPES = {"item", "global", "unknown"}
HANDOFF_WRITES = {"completed", "not_completed", "unknown"}
HANDOFF_CONFIRMATIONS = {"none", "required", "confirmed"}
SUCCESS_CODES = {"success", "durable-write-complete"}
SAFE_RECOVERY_PHASES = {"claimed", "pre-write", "research", "preflight"}
DURABLE_OUTPUT_PREFIXES = ("raw/", "wiki/", "index.md", "log.md")
GIT_STATUS_UNAVAILABLE = "<git-status-unavailable>"
DEFAULT_HANDOFF_TIMEOUT_SECONDS = 6600.0
ITEM_BLOCK_CODES = {
    "review-warning",
    "confirmation-required",
    "unsupported-etf-type",
    "item-pre-save-non-pass",
    "item-hard-data-gap",
    "item-downstream-error",
    "research-sub-agent-unavailable",
}
CARD_ID_RE = re.compile(r"^rc-[0-9]{8}T[0-9]{6,}Z-[a-f0-9]{8}$")
BATCH_ID_RE = re.compile(r"^rb-[0-9]{8}T[0-9]{6,}Z-[a-f0-9]{8}$")
TICKER_RE = re.compile(r"^[A-Z0-9][A-Z0-9._:-]*$")
TYPE_ALIASES = {"ETF": "ETF", "ETFS": "ETF", "STOCK": "Stock", "STOCKS": "Stock"}

CARD_FIELD_ORDER = [
    "kind",
    "card_id",
    "title",
    "status",
    "workflow",
    "instrument_type",
    "input_ticker",
    "created_at",
    "updated_at",
    "batch_id",
    "entity_key",
    "exchange",
    "claim_owner",
    "claimed_at",
    "lease_expires_at",
    "fencing_token",
    "claim_baseline_paths",
    "execution_phase",
    "result_status",
    "result_scope",
    "result_code",
    "result_reason",
    "durable_write",
    "confirmation",
    "output_paths",
    "planned_output_paths",
    "planned_output_baselines",
    "output_links",
    "completed_at",
    "commit_id",
]
BATCH_FIELD_ORDER = [
    "kind",
    "batch_id",
    "status",
    "created_at",
    "updated_at",
    "source",
    "authorized",
    "input_type",
    "requested_count",
    "created_card_ids",
    "reused_card_ids",
    "rejected_items",
]
REQUIRED_CARD_FIELDS = {
    "kind",
    "card_id",
    "title",
    "status",
    "workflow",
    "instrument_type",
    "input_ticker",
    "created_at",
    "updated_at",
}


class QueueError(Exception):
    """A user-visible deterministic queue error."""

    def __init__(self, code: str, message: str, *, global_failure: bool = True):
        super().__init__(message)
        self.code = code
        self.message = message
        self.global_failure = global_failure


def parse_time(value: str | None) -> dt.datetime:
    if value is None or value == "":
        return dt.datetime.now(dt.timezone.utc)
    if not isinstance(value, str):
        raise QueueError("workflow-config-mismatch", f"invalid timestamp: {value!r}")
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = dt.datetime.fromisoformat(text)
    except ValueError as exc:
        raise QueueError("workflow-config-mismatch", f"invalid timestamp: {value}") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def iso_time(value: dt.datetime) -> str:
    value = value.astimezone(dt.timezone.utc)
    timespec = "microseconds" if value.microsecond else "seconds"
    return value.isoformat(timespec=timespec).replace("+00:00", "Z")


def normalize_code(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return re.sub(r"[-_\s]+", "-", value.strip().lower())


def normalize_type(value: str | None) -> str | None:
    if value is None:
        return None
    return TYPE_ALIASES.get(value.strip().upper())


def normalize_workflow(value: str | None, instrument_type: str) -> str:
    if value is None or not value.strip():
        return SUPPORTED_ETF_WORKFLOW if instrument_type == "ETF" else FUTURE_STOCK_WORKFLOW
    workflow = value.strip().lower().replace("$", "")
    aliases = {
        "etf-performance": SUPPORTED_ETF_WORKFLOW,
        "check_etf_performance": SUPPORTED_ETF_WORKFLOW,
        "check-etf-performance": SUPPORTED_ETF_WORKFLOW,
        "official-source-stock-research": FUTURE_STOCK_WORKFLOW,
        "stock-research": FUTURE_STOCK_WORKFLOW,
    }
    return aliases.get(workflow, workflow)


def normalize_ticker(value: str) -> str:
    ticker = value.strip().strip("`").strip().lstrip("$").upper()
    ticker = re.sub(r"\s+", "", ticker)
    if not ticker or not TICKER_RE.fullmatch(ticker):
        raise QueueError("invalid-ticker", f"invalid ticker: {value!r}")
    return ticker


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value in {"null", "~"}:
        return None
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.startswith("[") and value.endswith("]"):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return [part.strip().strip("\"'") for part in value[1:-1].split(",") if part.strip()]
    if value.startswith("{") and value.endswith("}"):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"\"", "'"}:
        if value[0] == '"':
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                pass
        return value[1:-1]
    if re.fullmatch(r"-?[0-9]+", value):
        return int(value)
    return value


def parse_markdown(text: str) -> tuple[dict[str, Any], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise QueueError("invalid-card", "Markdown file has no frontmatter")
    try:
        end = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration as exc:
        raise QueueError("invalid-card", "frontmatter is not closed") from exc
    props: dict[str, Any] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise QueueError("invalid-card", f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        props[key.strip()] = parse_scalar(value)
    body = "\n".join(lines[end + 1 :]).lstrip("\n")
    return props, body


def yaml_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (list, tuple, dict)):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def dump_markdown(props: Mapping[str, Any], body: str) -> str:
    ordered = list(dict.fromkeys(CARD_FIELD_ORDER + BATCH_FIELD_ORDER + list(props)))
    lines = ["---"]
    for key in ordered:
        if key not in props:
            continue
        lines.append(f"{key}: {yaml_scalar(props[key])}")
    lines.append("---")
    if body:
        lines.append("")
        lines.append(body.rstrip())
    return "\n".join(lines) + "\n"


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())
        temporary = Path(handle.name)
    os.replace(temporary, path)
    # Best-effort directory sync makes the replacement survive a sudden
    # process/machine stop on filesystems that support directory fsync. The
    # rename itself remains the atomicity boundary when directory fsync is not
    # available (for example, on some macOS volume configurations).
    try:
        descriptor = os.open(path.parent, os.O_RDONLY)
    except OSError:
        return
    try:
        os.fsync(descriptor)
    except OSError:
        pass
    finally:
        os.close(descriptor)


def validate_card_props(props: Mapping[str, Any], expected_card_id: str | None = None) -> None:
    """Validate the immutable and lifecycle-independent card schema."""
    missing = sorted(field for field in REQUIRED_CARD_FIELDS if field not in props)
    if missing:
        raise QueueError("invalid-card", f"missing required card fields: {', '.join(missing)}")
    if props.get("kind") != "research-card":
        raise QueueError("invalid-card", "missing research-card identity")
    card_id = props.get("card_id")
    if not isinstance(card_id, str) or not CARD_ID_RE.fullmatch(card_id):
        raise QueueError("invalid-card", "card_id is malformed")
    if expected_card_id is not None and card_id != expected_card_id:
        raise QueueError("invalid-card", f"card identity mismatch: {expected_card_id}")
    status = props.get("status")
    if not isinstance(status, str) or status not in CARD_STATUSES:
        raise QueueError("invalid-card", f"unsupported card status: {status!r}")
    for field in ("title", "workflow", "instrument_type", "input_ticker"):
        value = props.get(field)
        if not isinstance(value, str) or not value.strip():
            raise QueueError("invalid-card", f"{field} is missing or malformed")
    if props.get("instrument_type") not in {"ETF", "Stock"}:
        raise QueueError("invalid-card", f"unsupported instrument_type: {props.get('instrument_type')!r}")
    for field in ("created_at", "updated_at"):
        value = props.get(field)
        if not isinstance(value, str) or not value.strip():
            raise QueueError("invalid-card", f"{field} is missing or malformed")
        parse_time(value)
    for field in ("claimed_at", "lease_expires_at", "completed_at"):
        if field in props and props[field] is not None:
            if not isinstance(props[field], str) or not props[field].strip():
                raise QueueError("invalid-card", f"{field} is malformed")
            parse_time(props[field])
    for field in ("claim_baseline_paths", "output_paths", "planned_output_paths", "output_links"):
        if field in props and props[field] is not None:
            value = props[field]
            if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
                raise QueueError("invalid-card", f"{field} must be a string list")
    if "planned_output_baselines" in props and props["planned_output_baselines"] is not None:
        baselines = props["planned_output_baselines"]
        if not isinstance(baselines, Mapping) or not all(
            isinstance(key, str) and (value is None or isinstance(value, str))
            for key, value in baselines.items()
        ):
            raise QueueError("invalid-card", "planned_output_baselines must be an object of fingerprints")


@dataclass(frozen=True)
class InputItem:
    ticker: str
    instrument_type: str
    workflow: str | None = None


@dataclass
class Card:
    props: dict[str, Any]
    body: str
    path: Path


class ProjectLease:
    """A best-effort atomic project lease with a two-hour renewable TTL."""

    def __init__(self, store: "QueueStore", owner: str, now: dt.datetime, ttl: dt.timedelta):
        self.store = store
        self.owner = owner
        self.now = now
        self.ttl = ttl
        self.token = secrets.token_hex(16)
        self.path = store.runtime_dir / "queue-lease.json"
        self.lock_path = store.runtime_dir / "queue-lease.lock"
        self.acquired = False

    def _payload(self, now: dt.datetime) -> dict[str, Any]:
        return {
            "owner": self.owner,
            "fencing_token": self.token,
            "acquired_at": iso_time(now),
            "lease_expires_at": iso_time(now + self.ttl),
        }

    def _lock(self) -> int:
        self.store.runtime_dir.mkdir(parents=True, exist_ok=True)
        descriptor: int | None = None
        try:
            descriptor = os.open(self.lock_path, os.O_RDWR | os.O_CREAT, 0o600)
            fcntl.flock(descriptor, fcntl.LOCK_EX)
            return descriptor
        except OSError as exc:
            if descriptor is not None:
                os.close(descriptor)
            raise QueueError("manager-overlap", "queue lease lock could not be acquired") from exc

    @staticmethod
    def _unlock(descriptor: int) -> None:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
        finally:
            os.close(descriptor)

    def _current_locked(self, now: dt.datetime) -> dict[str, Any]:
        try:
            current = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise QueueError("manager-overlap", "queue lease disappeared or is malformed") from exc
        if not isinstance(current, Mapping):
            raise QueueError("manager-overlap", "queue lease is malformed")
        if current.get("fencing_token") != self.token or current.get("owner") != self.owner:
            raise QueueError("manager-overlap", "queue lease fencing token changed")
        try:
            expiry_text = current.get("lease_expires_at")
            if not isinstance(expiry_text, str) or not expiry_text.strip():
                raise QueueError("manager-overlap", "queue lease has an invalid expiry")
            expires = parse_time(expiry_text)
        except QueueError as exc:
            raise QueueError("manager-overlap", "queue lease has an invalid expiry") from exc
        if expires <= now:
            raise QueueError("manager-overlap", "queue lease expired")
        return current

    def acquire(self) -> "ProjectLease":
        payload = self._payload(self.now)
        descriptor = self._lock()
        try:
            try:
                existing = json.loads(self.path.read_text(encoding="utf-8"))
                if not isinstance(existing, Mapping):
                    raise QueueError("manager-overlap", "queue lease exists and is malformed")
                expiry_text = existing.get("lease_expires_at")
                if not isinstance(expiry_text, str) or not expiry_text.strip():
                    raise QueueError("manager-overlap", "queue lease has an invalid expiry")
                expires = parse_time(expiry_text)
            except FileNotFoundError:
                # The lease disappeared between the existence check and read;
                # the lock prevents another cooperating manager from doing so.
                existing = None
                expires = self.now - dt.timedelta(seconds=1)
            except (OSError, json.JSONDecodeError, QueueError) as exc:
                raise QueueError("manager-overlap", "queue lease exists and cannot be inspected") from exc
            if existing is not None and expires > self.now:
                raise QueueError("manager-overlap", f"queue lease held by {existing.get('owner', 'unknown')}")
            try:
                self.path.unlink()
            except FileNotFoundError:
                pass
            try:
                # Write a complete payload to a temporary file, then atomically
                # replace the lease path. A crash can leave only an ignored
                # temporary artifact, never a half-written JSON lease.
                atomic_write(self.path, json.dumps(payload, ensure_ascii=False))
            except OSError as exc:
                raise QueueError("manager-overlap", "queue lease could not be written") from exc
            self.acquired = True
            return self
        finally:
            self._unlock(descriptor)

    def renew(self, now: dt.datetime) -> None:
        if not self.acquired:
            raise QueueError("manager-overlap", "queue lease is not held")
        descriptor = self._lock()
        try:
            self._current_locked(now)
            atomic_write(self.path, json.dumps(self._payload(now), ensure_ascii=False))
        finally:
            self._unlock(descriptor)

    def assert_current(self, now: dt.datetime) -> dict[str, Any]:
        if not self.acquired:
            raise QueueError("manager-overlap", "queue lease is not held")
        descriptor = self._lock()
        try:
            return self._current_locked(now)
        finally:
            self._unlock(descriptor)

    def release(self) -> None:
        if not self.acquired:
            return
        descriptor = self._lock()
        try:
            try:
                current = json.loads(self.path.read_text(encoding="utf-8"))
                if isinstance(current, Mapping) and current.get("fencing_token") == self.token and current.get("owner") == self.owner:
                    self.path.unlink(missing_ok=True)
            except (OSError, json.JSONDecodeError):
                pass
        finally:
            self.acquired = False
            self._unlock(descriptor)

    def __enter__(self) -> "ProjectLease":
        return self.acquire()

    def __exit__(self, *_: Any) -> None:
        self.release()


class QueueStore:
    """Filesystem-backed queue store and state machine."""

    def __init__(self, root: Path | str):
        self.root = Path(root).expanduser().resolve()
        self.queue_dir = self.root / "research-queue"
        self.cards_dir = self.queue_dir / "cards"
        self.batches_dir = self.queue_dir / "batches"
        self.runtime_dir = self.queue_dir / ".runtime"

    def ensure(self) -> None:
        self.cards_dir.mkdir(parents=True, exist_ok=True)
        self.batches_dir.mkdir(parents=True, exist_ok=True)

    def project_lease(self, owner: str, now: dt.datetime | None = None) -> ProjectLease:
        if not owner.strip():
            raise QueueError("workflow-config-mismatch", "owner is required")
        return ProjectLease(self, owner.strip(), now or dt.datetime.now(dt.timezone.utc), dt.timedelta(hours=2))

    def existing_project_lease(self, owner: str, fencing_token: str, now: dt.datetime | None = None) -> ProjectLease:
        """Resume a lease intentionally kept by a previous queue command."""
        if not owner.strip() or not fencing_token.strip():
            raise QueueError("workflow-config-mismatch", "owner and lease token are required")
        lease = self.project_lease(owner, now)
        lease.token = fencing_token.strip()
        lease.acquired = True
        lease.assert_current(lease.now)
        return lease

    def card_path(self, card_id: str) -> Path:
        if not CARD_ID_RE.fullmatch(card_id):
            raise QueueError("invalid-card", f"invalid card id: {card_id}")
        return self.cards_dir / f"{card_id}.md"

    def batch_path(self, batch_id: str) -> Path:
        if not BATCH_ID_RE.fullmatch(batch_id):
            raise QueueError("invalid-batch", f"invalid batch id: {batch_id}")
        return self.batches_dir / f"{batch_id}.md"

    def load_card(self, card_id: str) -> Card:
        path = self.card_path(card_id)
        try:
            text = path.read_text(encoding="utf-8")
        except FileNotFoundError as exc:
            raise QueueError("card-not-found", f"card not found: {card_id}") from exc
        props, body = parse_markdown(text)
        validate_card_props(props, expected_card_id=card_id)
        return Card(props, body, path)

    def write_card(self, card: Card) -> None:
        atomic_write(card.path, dump_markdown(card.props, card.body))

    def iter_cards(self) -> Iterator[Card]:
        if not self.cards_dir.exists():
            return
        for path in sorted(self.cards_dir.glob("rc-*.md")):
            try:
                props, body = parse_markdown(path.read_text(encoding="utf-8"))
                validate_card_props(props, expected_card_id=path.stem)
                yield Card(props, body, path)
            except (OSError, QueueError) as exc:
                raise QueueError("invalid-card", f"cannot inspect card {path.name}: {exc}") from exc

    def _new_id(self, prefix: str, now: dt.datetime) -> str:
        return f"{prefix}-{now.strftime('%Y%m%dT%H%M%S%fZ')}-{secrets.token_hex(4)}"

    def _active_index(self) -> dict[tuple[str, str], Card]:
        result: dict[tuple[str, str], Card] = {}
        for card in self.iter_cards():
            if card.props.get("status") in ACTIVE_STATUSES:
                key = (str(card.props.get("input_ticker", "")).upper(), str(card.props.get("workflow", "")))
                if key not in result:
                    result[key] = card
        return result

    def intake(
        self,
        source_text: str,
        *,
        default_type: str | None = None,
        workflow: str | None = None,
        dry_run: bool = False,
        source: str = "intake",
        now: dt.datetime | None = None,
    ) -> dict[str, Any]:
        now = now or dt.datetime.now(dt.timezone.utc)
        items = parse_input(source_text, default_type=default_type, workflow=workflow)
        if not items:
            raise QueueError("invalid-input", "no ticker items found")
        normalized: list[InputItem] = []
        seen: set[tuple[str, str]] = set()
        for item in items:
            ticker = normalize_ticker(item.ticker)
            item_type = normalize_type(item.instrument_type)
            if item_type is None:
                raise QueueError("invalid-instrument-type", f"unsupported instrument type: {item.instrument_type}")
            item_workflow = normalize_workflow(item.workflow, item_type)
            if item_type == "ETF" and item_workflow != SUPPORTED_ETF_WORKFLOW:
                raise QueueError("unsupported-workflow", f"ETF workflow is not supported in V1: {item_workflow}")
            key = (ticker, item_workflow)
            if key in seen:
                continue
            seen.add(key)
            normalized.append(InputItem(ticker, item_type, item_workflow))

        batch_id = self._new_id("rb", now)
        active = self._active_index()
        plan: list[dict[str, Any]] = []
        for item_index, item in enumerate(normalized):
            key = (item.ticker, str(item.workflow))
            if key in active:
                existing = active[key]
                plan.append({
                    "action": "reused",
                    "card_id": existing.props["card_id"],
                    "ticker": item.ticker,
                    "instrument_type": item.instrument_type,
                    "workflow": item.workflow,
                    "status": existing.props["status"],
                    "path": str(existing.path.relative_to(self.root)),
                })
            elif item.instrument_type == "Stock":
                plan.append({
                    "action": "rejected",
                    "ticker": item.ticker,
                    "instrument_type": item.instrument_type,
                    "workflow": item.workflow,
                    "code": "unsupported-processor",
                    "reason": "Stock processing is reserved for a future V1 processor.",
                })
            else:
                card_now = now + dt.timedelta(microseconds=item_index)
                card_id = self._new_id("rc", card_now)
                plan.append({
                    "action": "created",
                    "card_id": card_id,
                    "ticker": item.ticker,
                    "instrument_type": item.instrument_type,
                    "workflow": item.workflow,
                    "status": STATUS_READY,
                    "created_at": iso_time(card_now),
                    "path": str((self.cards_dir / f"{card_id}.md").relative_to(self.root)),
                })

        created = [entry for entry in plan if entry["action"] == "created"]
        reused = [entry for entry in plan if entry["action"] == "reused"]
        rejected = [entry for entry in plan if entry["action"] == "rejected"]
        if dry_run:
            return {
                "command": "intake",
                "dry_run": True,
                "batch_id": batch_id,
                "status": "Proposed",
                "created": created,
                "reused": reused,
                "rejected": rejected,
            }

        self.ensure()
        created_ids: list[str] = []
        for entry in created:
            card_id = entry["card_id"]
            props: dict[str, Any] = {
                "kind": "research-card",
                "card_id": card_id,
                "title": f"{entry['instrument_type']} performance — {entry['ticker']}" if entry["instrument_type"] == "ETF" else f"{entry['instrument_type']} research — {entry['ticker']}",
                "status": STATUS_READY,
                "workflow": entry["workflow"],
                "instrument_type": entry["instrument_type"],
                "input_ticker": entry["ticker"],
                "created_at": entry.get("created_at", iso_time(now)),
                "updated_at": iso_time(now),
                "batch_id": batch_id,
            }
            card = Card(props, "การ์ดนี้ติดตามเครื่องมือหนึ่งรายการและ Research Workflow ที่ระบุไว้ชัดเจน\n", self.card_path(card_id))
            self.write_card(card)
            created_ids.append(card_id)

        rejected_items = [
            {"ticker": entry["ticker"], "instrument_type": entry["instrument_type"], "workflow": entry["workflow"], "code": entry["code"], "reason": entry["reason"]}
            for entry in rejected
        ]
        batch_props = {
            "kind": "research-batch",
            "batch_id": batch_id,
            "status": "Done",
            "created_at": iso_time(now),
            "updated_at": iso_time(now),
            "source": source,
            "authorized": True,
            "input_type": "markdown-or-inline",
            "requested_count": len(normalized),
            "created_card_ids": created_ids,
            "reused_card_ids": [entry["card_id"] for entry in reused],
            "rejected_items": rejected_items,
        }
        atomic_write(self.batch_path(batch_id), dump_markdown(batch_props, "Batch นี้บันทึกการสร้างการ์ดเท่านั้น ไม่ได้ยืนยันว่า downstream research เสร็จแล้ว\n"))
        return {
            "command": "intake",
            "dry_run": False,
            "batch_id": batch_id,
            "status": "Done",
            "created": created,
            "reused": reused,
            "rejected": rejected,
        }

    def list_cards(self, status: str | None = None) -> list[dict[str, Any]]:
        if status:
            status = canonical_status(status)
        cards = [card for card in self.iter_cards() if status is None or card.props.get("status") == status]
        cards.sort(key=lambda card: (parse_time(str(card.props.get("created_at", ""))), str(card.props.get("card_id", ""))))
        return [card_summary(card) for card in cards]

    def claim(self, card_id: str, *, owner: str, now: dt.datetime | None = None, phase: str = "claimed") -> dict[str, Any]:
        now = now or dt.datetime.now(dt.timezone.utc)
        if not owner.strip():
            raise QueueError("workflow-config-mismatch", "owner is required")
        card = self.load_card(card_id)
        if card.props.get("status") != STATUS_READY:
            raise QueueError("claim-state-error", f"card is not Ready: {card_id}")
        if card.props.get("workflow") != SUPPORTED_ETF_WORKFLOW:
            raise QueueError("unsupported-workflow", f"card workflow is not supported in V1: {card.props.get('workflow')}")
        token = uuid.uuid4().hex
        baseline_paths = self._durable_working_tree_paths(card)
        card.props.update({
            "status": STATUS_IN_PROGRESS,
            "updated_at": iso_time(now),
            "claim_owner": owner,
            "claimed_at": iso_time(now),
            "lease_expires_at": iso_time(now + dt.timedelta(hours=2)),
            "fencing_token": token,
            "claim_baseline_paths": baseline_paths,
            "execution_phase": phase,
        })
        self.write_card(card)
        reread = self.load_card(card_id)
        if reread.props.get("status") != STATUS_IN_PROGRESS or reread.props.get("fencing_token") != token:
            raise QueueError("claim-state-error", f"claim could not be confirmed: {card_id}")
        return {
            "card_id": card_id,
            "status": STATUS_IN_PROGRESS,
            "owner": owner,
            "fencing_token": token,
            "lease_expires_at": reread.props["lease_expires_at"],
            "execution_phase": phase,
            "path": str(reread.path.relative_to(self.root)),
        }

    def renew(self, card_id: str, *, owner: str, fencing_token: str, now: dt.datetime | None = None, phase: str | None = None, outputs: Sequence[str] = ()) -> dict[str, Any]:
        now = now or dt.datetime.now(dt.timezone.utc)
        card = self.load_card(card_id)
        assert_claim(card, owner, fencing_token, now)
        planned_outputs = normalize_output_paths(self.root, outputs)
        # Fingerprinting can be non-trivial for a large vault; re-read the
        # card after that work so the lease token is checked immediately before
        # the renewal mutation.
        card = self.load_card(card_id)
        assert_claim(card, owner, fencing_token, now)
        card.props["lease_expires_at"] = iso_time(now + dt.timedelta(hours=2))
        if phase:
            card.props["execution_phase"] = phase
        if planned_outputs:
            baselines = card.props.get("planned_output_baselines") or {}
            if not isinstance(baselines, Mapping):
                raise QueueError("invalid-card", "planned output baselines must be an object")
            baselines = dict(baselines)
            for path in planned_outputs:
                if path not in baselines:
                    baselines[path] = file_fingerprint(self.root / path)
            card.props["planned_output_paths"] = planned_outputs
            card.props["planned_output_baselines"] = baselines
        card.props["updated_at"] = iso_time(now)
        self.write_card(card)
        return {
            "card_id": card_id,
            "status": STATUS_IN_PROGRESS,
            "owner": owner,
            "fencing_token": fencing_token,
            "lease_expires_at": card.props["lease_expires_at"],
            "execution_phase": card.props.get("execution_phase"),
        }

    def route(
        self,
        card_id: str,
        handoff: Mapping[str, Any],
        *,
        owner: str,
        fencing_token: str,
        outputs: Sequence[str] = (),
        now: dt.datetime | None = None,
        commit: bool = False,
        entity_key: str | None = None,
        project_lease: ProjectLease | None = None,
    ) -> dict[str, Any]:
        now = now or dt.datetime.now(dt.timezone.utc)
        if project_lease is not None:
            project_lease.assert_current(now)
        card = self.load_card(card_id)
        assert_claim(card, owner, fencing_token, now)

        def block(card_for_route: Card, timestamp: dt.datetime, **kwargs: Any) -> dict[str, Any]:
            """Route a non-success while retaining the project lease fence."""
            return self._route_blocked(
                card_for_route,
                timestamp,
                project_lease=project_lease,
                **kwargs,
            )

        normalized, validation_error = validate_handoff(handoff)
        if validation_error:
            return block(
                card,
                now,
                status="BLOCKED",
                scope="global",
                code="unknown-result",
                reason=validation_error,
                durable_write="unknown",
                confirmation="none",
                global_blocked=True,
            )

        try:
            output_paths = normalize_output_paths(self.root, outputs)
        except QueueError as exc:
            return block(
                card,
                now,
                status="ERROR",
                scope="global",
                code=exc.code,
                reason=exc.message,
                durable_write="unknown",
                confirmation="none",
                global_blocked=True,
            )
        if normalized["status"] == "PASS" and normalized["scope"] == "item" and normalized["durable_write"] == "completed" and normalized["exhausted"] is False and normalized["confirmation"] == "none" and normalized["code"] in SUCCESS_CODES:
            if not output_paths:
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code="durable-output-required",
                    reason="A successful handoff must name at least one durable project-relative output.",
                    durable_write="unknown",
                    confirmation="none",
                    global_blocked=True,
                )
            if not commit:
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code="git-commit-required",
                    reason="A successful handoff must request the scoped terminal Git commit.",
                    durable_write="completed",
                    confirmation="none",
                    global_blocked=True,
                )
            try:
                planned_paths = normalize_output_paths(self.root, card.props.get("planned_output_paths") or [])
            except QueueError as exc:
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code=exc.code,
                    reason=exc.message,
                    durable_write="unknown",
                    confirmation="none",
                    global_blocked=True,
                )
            if not planned_paths:
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code="durable-output-scope-required",
                    reason="Successful routing requires output paths declared by renew before downstream writes.",
                    durable_write="unknown",
                    confirmation="none",
                    global_blocked=True,
                )
            if planned_paths != output_paths:
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code="durable-output-scope-mismatch",
                    reason="Route output paths must exactly match the pre-write output scope.",
                    durable_write="unknown",
                    confirmation="none",
                    global_blocked=True,
                )
            baseline_paths = {str(path) for path in (card.props.get("claim_baseline_paths") or [])}
            working_tree_paths = self._durable_working_tree_paths(card)
            if GIT_STATUS_UNAVAILABLE in baseline_paths or GIT_STATUS_UNAVAILABLE in working_tree_paths:
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code="durable-output-evidence-unavailable",
                    reason="Git status could not establish a safe durable output scope.",
                    durable_write="unknown",
                    confirmation="none",
                    global_blocked=True,
                )
            dirty_conflicts = [path for path in output_paths if path in baseline_paths]
            if dirty_conflicts:
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code="durable-output-conflict",
                    reason=f"Durable output was already dirty before claim: {dirty_conflicts[0]}",
                    durable_write="unknown",
                    confirmation="none",
                    global_blocked=True,
                )
            unexpected = [path for path in working_tree_paths if path not in baseline_paths and path not in output_paths]
            if unexpected:
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code="durable-output-scope-mismatch",
                    reason=f"Downstream changed an undeclared durable output: {unexpected[0]}",
                    durable_write="unknown",
                    confirmation="none",
                    global_blocked=True,
                )
            missing = [path for path in output_paths if not (self.root / path).exists()]
            directories = [path for path in output_paths if (self.root / path).is_dir()]
            if missing:
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code="durable-write-missing",
                    reason=f"durable output is missing: {missing[0]}",
                    durable_write="unknown",
                    confirmation="none",
                    global_blocked=True,
                )
            if directories:
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code="durable-output-invalid",
                    reason=f"durable output must be a file: {directories[0]}",
                    durable_write="unknown",
                    confirmation="none",
                    global_blocked=True,
                )
            baselines = card.props.get("planned_output_baselines") or {}
            if not isinstance(baselines, Mapping) or any(path not in baselines for path in output_paths):
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code="durable-output-baseline-required",
                    reason="Each durable output must have a pre-write baseline.",
                    durable_write="unknown",
                    confirmation="none",
                    global_blocked=True,
                )
            if any(baselines[path] is not None and not isinstance(baselines[path], str) for path in output_paths):
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code="durable-output-baseline-invalid",
                    reason="Durable output baselines are malformed.",
                    durable_write="unknown",
                    confirmation="none",
                    global_blocked=True,
                )
            unchanged = [
                path for path in output_paths
                if baselines[path] is not None and file_fingerprint(self.root / path) == baselines[path]
            ]
            if unchanged:
                return block(
                    card,
                    now,
                    status="ERROR",
                    scope="global",
                    code="durable-output-unchanged",
                    reason=f"Durable output was not changed after the pre-write boundary: {unchanged[0]}",
                    durable_write="unknown",
                    confirmation="none",
                    global_blocked=True,
                )
            # Re-read and fence immediately before the terminal card write;
            # validation above may have taken long enough for an expired claim
            # to be recovered and re-claimed by another worker.
            if project_lease is not None:
                project_lease.assert_current(now)
            card = self.load_card(card_id)
            assert_claim(card, owner, fencing_token, now)
            card.props.update({
                "status": STATUS_DONE,
                "updated_at": iso_time(now),
                "completed_at": iso_time(now),
                "execution_phase": "completed",
                "result_status": normalized["status"],
                "result_scope": normalized["scope"],
                "result_code": normalized["code"],
                "result_reason": normalized["reason"],
                "durable_write": normalized["durable_write"],
                "confirmation": normalized["confirmation"],
                "output_paths": output_paths,
                "planned_output_paths": output_paths,
                "output_links": [f"[[{path[:-3] if path.endswith('.md') else path}]]" for path in output_paths],
                "commit_id": f"queue/{card_id}",
            })
            clear_claim(card.props)
            if entity_key:
                card.props["entity_key"] = entity_key
            commit_result = self._commit_terminal(card, output_paths, now) if commit else {"committed": False}
            if commit and not commit_result.get("committed"):
                failed = self.load_card(card_id)
                return block(
                    failed,
                    now,
                    status="ERROR",
                    scope="global",
                    code="git-commit-failed",
                    reason=commit_result.get("error") or commit_result.get("reason") or "Git commit did not complete.",
                    durable_write="completed",
                    confirmation="none",
                    global_blocked=True,
                    fenced=False,
                )
            return {
                "card_id": card_id,
                "status": STATUS_DONE,
                "outcome": "done",
                "output_paths": output_paths,
                "commit": commit_result,
                "global_blocked": False,
            }

        if is_accepted_item_block(normalized):
            return block(
                card,
                now,
                status=normalized["status"],
                scope=normalized["scope"],
                code=normalized["code"],
                reason=normalized["reason"],
                durable_write=normalized["durable_write"],
                confirmation=normalized["confirmation"],
                global_blocked=False,
            )
        return block(
            card,
            now,
            status="BLOCKED",
            scope="global",
            code="unknown-result",
            reason="Downstream result was contradictory or outside the accepted matrix.",
            durable_write="unknown",
            confirmation="none",
            global_blocked=True,
        )

    def _route_blocked(
        self,
        card: Card,
        now: dt.datetime,
        *,
        status: str,
        scope: str,
        code: str,
        reason: str,
        durable_write: str,
        confirmation: str,
        global_blocked: bool,
        fenced: bool = True,
        project_lease: ProjectLease | None = None,
    ) -> dict[str, Any]:
        if project_lease is not None:
            project_lease.assert_current(now)
        if fenced:
            # All blocked transitions must use the same claim snapshot that
            # was validated by the caller. This closes the check-then-write
            # window across recovery/reclaim races.
            current = self.load_card(card.props["card_id"])
            assert_claim(
                current,
                str(card.props.get("claim_owner") or ""),
                str(card.props.get("fencing_token") or ""),
                now,
            )
            if current.props.get("fencing_token") != card.props.get("fencing_token"):
                raise QueueError("claim-state-error", "stale fencing token before blocked transition")
            card = current
        card.props.update({
            "status": STATUS_BLOCKED,
            "updated_at": iso_time(now),
            "execution_phase": "blocked",
            "result_status": status,
            "result_scope": scope,
            "result_code": normalize_code(code),
            "result_reason": reason.strip() or "No reason supplied.",
            "durable_write": durable_write,
            "confirmation": confirmation,
        })
        for key in ("completed_at", "commit_id"):
            card.props.pop(key, None)
        clear_claim(card.props)
        if project_lease is not None:
            project_lease.assert_current(now)
        self.write_card(card)
        reread = self.load_card(card.props["card_id"])
        if reread.props.get("status") != STATUS_BLOCKED or reread.props.get("result_code") != normalize_code(code):
            raise QueueError("claim-state-error", "blocked transition could not be confirmed")
        return {
            "card_id": card.props["card_id"],
            "status": STATUS_BLOCKED,
            "outcome": "global_blocked" if global_blocked else "blocked",
            "result_code": reread.props["result_code"],
            "result_reason": reread.props["result_reason"],
            "global_blocked": global_blocked,
        }

    def _commit_terminal(self, card: Card, output_paths: Sequence[str], now: dt.datetime) -> dict[str, Any]:
        paths = [str(card.path.relative_to(self.root)), *output_paths]
        if not (self.root / ".git").exists():
            return {"committed": False, "error": "not-a-git-checkout"}
        message = f"research: complete {card.props['input_ticker']} ({card.props['card_id']})"
        index_result = subprocess.run(["git", "-C", str(self.root), "rev-parse", "--git-path", "index"], check=False, capture_output=True, text=True)
        if index_result.returncode != 0 or not index_result.stdout.strip():
            return {"committed": False, "error": "git index could not be resolved"}
        index_path = Path(index_result.stdout.strip())
        if not index_path.is_absolute():
            index_path = self.root / index_path
        temporary_index = index_path.with_name(f"queue-index-{secrets.token_hex(8)}")
        temporary_card = self.runtime_dir / f"terminal-card-{secrets.token_hex(8)}.md"
        commit_succeeded = False
        materialization_error: str | None = None
        try:
            self.runtime_dir.mkdir(parents=True, exist_ok=True)
            temporary_card.write_text(dump_markdown(card.props, card.body), encoding="utf-8")
            env = os.environ.copy()
            env["GIT_INDEX_FILE"] = str(temporary_index)
            # Start from HEAD rather than copying the caller's index. This
            # keeps unrelated staged edits out of the queue commit and avoids
            # resetting those edits if the commit fails.
            read_tree = subprocess.run(["git", "-C", str(self.root), "read-tree", "HEAD"], env=env, check=False, capture_output=True, text=True)
            if read_tree.returncode != 0:
                return {"committed": False, "error": (read_tree.stderr or read_tree.stdout).strip() or "git index could not be initialized"}
            add_result = subprocess.run(["git", "-C", str(self.root), "add", "--", *output_paths], env=env, check=False, capture_output=True, text=True)
            if add_result.returncode != 0:
                return {"committed": False, "error": (add_result.stderr or add_result.stdout).strip() or "git add failed"}
            card_blob = subprocess.run(["git", "-C", str(self.root), "hash-object", "-w", "--", str(temporary_card)], check=False, capture_output=True, text=True)
            if card_blob.returncode != 0 or not card_blob.stdout.strip():
                return {"committed": False, "error": (card_blob.stderr or card_blob.stdout).strip() or "card blob could not be prepared"}
            card_rel = str(card.path.relative_to(self.root))
            update_index = subprocess.run(["git", "-C", str(self.root), "update-index", "--add", "--cacheinfo", f"100644,{card_blob.stdout.strip()},{card_rel}"], env=env, check=False, capture_output=True, text=True)
            if update_index.returncode != 0:
                return {"committed": False, "error": (update_index.stderr or update_index.stdout).strip() or "card could not be staged"}
            command = ["git", "-C", str(self.root), "commit", "-m", message]
            try:
                completed = subprocess.run(command, env=env, check=False, capture_output=True, text=True)
            except OSError as exc:
                return {"committed": False, "error": str(exc)}
            if completed.returncode != 0:
                return {"committed": False, "error": (completed.stderr or completed.stdout).strip() or "git commit failed"}
            commit_succeeded = True
            # Materialize exactly the committed card after the commit. A crash
            # before this point leaves the old In Progress file on disk, which
            # recovery can reconcile against the terminal card blob in HEAD.
            try:
                self.write_card(card)
            except (OSError, QueueError, ValueError) as exc:
                # The commit is already authoritative. Do not demote the card
                # to Blocked because a filesystem sync failed; recovery can
                # materialize the terminal card from HEAD on the next run.
                materialization_error = str(exc)
        finally:
            temporary_index.unlink(missing_ok=True)
            temporary_card.unlink(missing_ok=True)
        try:
            sync_result = subprocess.run(["git", "-C", str(self.root), "add", "--", *paths], check=False, capture_output=True, text=True)
        except OSError as exc:
            sync_result = None
            sync_error = str(exc)
        else:
            sync_error = (sync_result.stderr or sync_result.stdout).strip() or "git index sync failed" if sync_result.returncode != 0 else ""
        if sync_result is None or sync_result.returncode != 0:
            if commit_succeeded:
                try:
                    sha_result = subprocess.run(["git", "-C", str(self.root), "rev-parse", "HEAD"], check=False, capture_output=True, text=True)
                except OSError as exc:
                    sha = ""
                    sha_error = str(exc)
                else:
                    sha = sha_result.stdout.strip() if sha_result.returncode == 0 else ""
                    sha_error = sha_result.stderr.strip() if sha_result.returncode != 0 else ""
                return {
                    "committed": True,
                    "materialized": materialization_error is None,
                    "commit_sha": sha or None,
                    "commit_sha_verified": bool(sha),
                    "error": materialization_error or sync_error or sha_error or "Git commit SHA could not be verified.",
                }
            return {"committed": False, "error": sync_error}
        try:
            sha_result = subprocess.run(["git", "-C", str(self.root), "rev-parse", "HEAD"], check=False, capture_output=True, text=True)
        except OSError as exc:
            sha = ""
            sha_error = str(exc)
        else:
            sha = sha_result.stdout.strip() if sha_result.returncode == 0 else ""
            sha_error = sha_result.stderr.strip() if sha_result.returncode != 0 else ""
        result: dict[str, Any] = {
            "committed": commit_succeeded,
            "materialized": materialization_error is None,
            "commit_sha": sha or None,
            "commit_sha_verified": bool(sha),
        }
        if materialization_error:
            result["error"] = materialization_error
        if not sha:
            result["error"] = sha_error or "Git commit SHA could not be verified."
        return result

    def recover(self, *, now: dt.datetime | None = None, project_lease: ProjectLease | None = None) -> dict[str, Any]:
        now = now or dt.datetime.now(dt.timezone.utc)
        ready: list[dict[str, Any]] = []
        blocked: list[dict[str, Any]] = []
        recovered_done: list[dict[str, Any]] = []
        for card in list(self.iter_cards()):
            # The initial iterator is only a selection snapshot. Re-read each
            # candidate before changing it so a concurrent renewal/reclaim
            # cannot be overwritten by stale recovery state.
            card = self.load_card(card.props["card_id"])
            terminal = self._head_terminal_card(card)
            if terminal is not None and card.props.get("status") == STATUS_IN_PROGRESS:
                if project_lease is not None:
                    project_lease.assert_current(now)
                current = self.load_card(card.props["card_id"])
                if current.props.get("status") != STATUS_IN_PROGRESS or current.props.get("fencing_token") != card.props.get("fencing_token"):
                    raise QueueError("claim-state-error", "stale claim before terminal recovery")
                if project_lease is not None:
                    project_lease.assert_current(now)
                self.write_card(terminal)
                recovered_done.append({"card_id": card.props["card_id"], "status": STATUS_DONE, "result_code": terminal.props.get("result_code")})
                continue
            if card.props.get("status") != STATUS_IN_PROGRESS:
                continue
            expiry_text = card.props.get("lease_expires_at")
            if not expiry_text or parse_time(str(expiry_text)) > now:
                continue
            phase = str(card.props.get("execution_phase") or "").lower()
            output_paths = card.props.get("output_paths") or []
            planned_paths = card.props.get("planned_output_paths") or []
            if isinstance(planned_paths, str):
                planned_paths = [planned_paths]
            planned_existing = [path for path in planned_paths if (self.root / str(path)).exists()]
            baseline_paths = card.props.get("claim_baseline_paths") or []
            if isinstance(baseline_paths, str):
                baseline_paths = [baseline_paths]
            working_tree_paths = self._durable_working_tree_paths(card)
            baseline_set = set(str(item) for item in baseline_paths)
            git_status_unknown = GIT_STATUS_UNAVAILABLE in baseline_set or GIT_STATUS_UNAVAILABLE in working_tree_paths
            changed_outputs = [path for path in working_tree_paths if path not in baseline_set and path != GIT_STATUS_UNAVAILABLE]
            # Only an explicit, known pre-write phase with no output evidence is
            # safe to retry. Unknown phases and ambiguous working-tree changes
            # are conservatively blocked for human inspection.
            partial = (
                phase not in SAFE_RECOVERY_PHASES
                or bool(output_paths)
                or bool(planned_existing)
                or bool(changed_outputs)
                or git_status_unknown
            )
            if partial:
                item = self._route_recovery(card, now, ready_state=False, project_lease=project_lease)
                blocked.append(item)
            else:
                item = self._route_recovery(card, now, ready_state=True, project_lease=project_lease)
                ready.append(item)
        return {"command": "recover", "recovered_ready": ready, "blocked_partial": blocked, "recovered_done": recovered_done}

    def _head_terminal_card(self, card: Card) -> Card | None:
        """Read a committed terminal card for crash recovery after commit."""
        if not (self.root / ".git").exists():
            return None
        relative = str(card.path.relative_to(self.root))
        result = subprocess.run(["git", "-C", str(self.root), "show", f"HEAD:{relative}"], check=False, capture_output=True, text=True)
        if result.returncode != 0:
            return None
        try:
            props, body = parse_markdown(result.stdout)
        except QueueError:
            return None
        try:
            validate_card_props(props, expected_card_id=card.props.get("card_id"))
        except QueueError:
            return None
        if props.get("status") != STATUS_DONE:
            return None
        if props.get("commit_id") != f"queue/{card.props.get('card_id')}":
            return None
        return Card(props, body, card.path)

    def _durable_working_tree_paths(self, card: Card) -> list[str]:
        """Return changed durable paths unrelated to this queue card.

        This is intentionally conservative: if Git status cannot be read, the
        caller receives a sentinel and recovery blocks instead of retrying a
        potentially partial write. Queue/runtime files and the claimed card
        itself are excluded because they are expected state mutations.
        """
        if not (self.root / ".git").exists():
            return []
        result = subprocess.run(
            ["git", "-C", str(self.root), "status", "--porcelain", "--untracked-files=all"],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return [GIT_STATUS_UNAVAILABLE]
        card_rel = str(card.path.relative_to(self.root))
        changed: list[str] = []
        for line in result.stdout.splitlines():
            if len(line) < 4:
                continue
            path = line[3:].strip().strip('"')
            if " -> " in path:
                path = path.split(" -> ", 1)[1].strip().strip('"')
            if path == card_rel or path.startswith("research-queue/"):
                continue
            if path.startswith(DURABLE_OUTPUT_PREFIXES):
                changed.append(path)
        return changed

    def _route_recovery(self, card: Card, now: dt.datetime, *, ready_state: bool, project_lease: ProjectLease | None = None) -> dict[str, Any]:
        if project_lease is not None:
            project_lease.assert_current(now)
        current = self.load_card(card.props["card_id"])
        if current.props.get("status") != STATUS_IN_PROGRESS or current.props.get("fencing_token") != card.props.get("fencing_token"):
            raise QueueError("claim-state-error", "stale claim before recovery transition")
        card = current
        if ready_state:
            card.props.update({
                "status": STATUS_READY,
                "updated_at": iso_time(now),
                "execution_phase": "recovered-ready",
                "result_code": "lease-expired",
                "result_reason": "Expired claim had no durable output write.",
            })
            for key in ("planned_output_paths", "planned_output_baselines"):
                card.props.pop(key, None)
        else:
            card.props.update({
                "status": STATUS_BLOCKED,
                "updated_at": iso_time(now),
                "execution_phase": "blocked",
                "result_status": "BLOCKED",
                "result_scope": "item",
                "result_code": "partial-write-recovery",
                "result_reason": "Expired claim may have begun a durable write; inspect before retry.",
                "durable_write": "unknown",
                "confirmation": "none",
            })
        clear_claim(card.props)
        if project_lease is not None:
            project_lease.assert_current(now)
        self.write_card(card)
        return {"card_id": card.props["card_id"], "status": card.props["status"], "result_code": card.props.get("result_code")}

    def transition(self, card_id: str, target: str, *, now: dt.datetime | None = None, reason: str | None = None) -> dict[str, Any]:
        now = now or dt.datetime.now(dt.timezone.utc)
        target = canonical_status(target)
        card = self.load_card(card_id)
        current = card.props["status"]
        if current in TERMINAL_STATUSES:
            raise QueueError("invalid-transition", f"terminal card cannot change: {card_id}")
        allowed = {
            (STATUS_READY, STATUS_BLOCKED),
            (STATUS_BLOCKED, STATUS_READY),
            (STATUS_READY, STATUS_CANCELLED),
            (STATUS_BLOCKED, STATUS_CANCELLED),
            (STATUS_IN_PROGRESS, STATUS_CANCELLED),
        }
        if (current, target) not in allowed:
            raise QueueError("invalid-transition", f"unsupported transition: {current} -> {target}")
        card.props.update({"status": target, "updated_at": iso_time(now)})
        if target == STATUS_BLOCKED and reason:
            card.props["result_reason"] = reason.strip()
        if target == STATUS_CANCELLED:
            card.props["execution_phase"] = "cancelled"
            clear_claim(card.props)
        self.write_card(card)
        return card_summary(self.load_card(card_id))


def clear_claim(props: dict[str, Any]) -> None:
    for key in ("claim_owner", "claimed_at", "lease_expires_at", "fencing_token", "claim_baseline_paths"):
        props.pop(key, None)


def assert_claim(card: Card, owner: str, token: str, now: dt.datetime) -> None:
    if not owner.strip() or not token.strip():
        raise QueueError("workflow-config-mismatch", "owner and fencing token are required")
    if card.props.get("status") != STATUS_IN_PROGRESS:
        raise QueueError("claim-state-error", f"card is not In Progress: {card.props.get('card_id')}")
    if card.props.get("claim_owner") != owner or card.props.get("fencing_token") != token:
        raise QueueError("claim-state-error", "stale fencing token or owner")
    expiry = card.props.get("lease_expires_at")
    if not expiry or parse_time(str(expiry)) <= now:
        raise QueueError("claim-state-error", "card lease has expired")


def canonical_status(value: str) -> str:
    normalized = value.strip().lower().replace("_", " ").replace("-", " ")
    aliases = {
        "ready": STATUS_READY,
        "in progress": STATUS_IN_PROGRESS,
        "blocked": STATUS_BLOCKED,
        "done": STATUS_DONE,
        "cancelled": STATUS_CANCELLED,
        "canceled": STATUS_CANCELLED,
    }
    if normalized not in aliases:
        raise QueueError("invalid-status", f"unsupported status: {value}")
    return aliases[normalized]


def card_summary(card: Card) -> dict[str, Any]:
    fields = ("card_id", "title", "status", "workflow", "instrument_type", "input_ticker", "created_at", "updated_at", "lease_expires_at", "fencing_token", "execution_phase", "result_code", "planned_output_paths", "output_paths")
    result = {key: card.props[key] for key in fields if key in card.props}
    result["path"] = str(card.path)
    return result


def validate_handoff(handoff: Mapping[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    if not isinstance(handoff, Mapping):
        return None, "Downstream result was missing or not an object."
    if set(handoff) != HANDOFF_FIELDS:
        return None, "Downstream result was missing, malformed, or contradictory."
    status = handoff.get("status")
    scope = handoff.get("scope")
    durable_write = handoff.get("durable_write")
    exhausted = handoff.get("exhausted")
    confirmation = handoff.get("confirmation")
    code = normalize_code(handoff.get("code"))
    reason = handoff.get("reason")
    if (
        not isinstance(status, str)
        or status not in HANDOFF_STATUSES
        or not isinstance(scope, str)
        or scope not in HANDOFF_SCOPES
        or not isinstance(durable_write, str)
        or durable_write not in HANDOFF_WRITES
        or not isinstance(confirmation, str)
        or confirmation not in HANDOFF_CONFIRMATIONS
        or not isinstance(exhausted, bool)
        or not code
        or not isinstance(reason, str)
        or not reason.strip()
    ):
        return None, "Downstream result was missing, malformed, or contradictory."
    return {
        "status": status,
        "scope": scope,
        "durable_write": durable_write,
        "exhausted": exhausted,
        "confirmation": confirmation,
        "code": code,
        "reason": reason.strip(),
    }, None


def is_accepted_item_block(handoff: Mapping[str, Any]) -> bool:
    status = handoff["status"]
    if handoff["scope"] != "item":
        return False
    if handoff["durable_write"] != "not_completed" or handoff["confirmation"] not in {"none", "required"}:
        return False
    code = handoff["code"]
    if status == "WARNING":
        return handoff["exhausted"] is False and handoff["confirmation"] == "required" and code in {"review-warning", "confirmation-required"}
    if status in {"CHANGES_REQUIRED", "BLOCKED"}:
        return handoff["exhausted"] is True and handoff["confirmation"] == "none" and code in {"unsupported-etf-type", "item-pre-save-non-pass", "item-hard-data-gap", "item-downstream-error"}
    if status == "ERROR":
        return handoff["exhausted"] is False and handoff["confirmation"] == "none" and code in {"research-sub-agent-unavailable", "item-downstream-error"}
    return False


def file_fingerprint(path: Path) -> str | None:
    """Return a stable content digest for a pre-write output baseline."""
    if not path.exists():
        return None
    if path.is_dir():
        raise QueueError("workflow-config-mismatch", f"output must identify a file, not a directory: {path}")
    try:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()
    except OSError as exc:
        raise QueueError("workflow-config-mismatch", f"output could not be fingerprinted: {path}") from exc


def normalize_output_paths(root: Path, outputs: Sequence[str]) -> list[str]:
    result: list[str] = []
    for raw in outputs:
        if not isinstance(raw, str) or not raw.strip():
            raise QueueError("workflow-config-mismatch", f"output must be a non-empty project-relative file: {raw!r}")
        if raw.strip().endswith(("/", os.sep)):
            raise QueueError("workflow-config-mismatch", f"output must identify a file, not a directory: {raw}")
        candidate = Path(raw)
        if candidate.is_absolute():
            raise QueueError("workflow-config-mismatch", f"output must be project-relative: {raw}")
        resolved = (root / candidate).resolve()
        try:
            relative = resolved.relative_to(root)
        except ValueError as exc:
            raise QueueError("workflow-config-mismatch", f"output escapes project root: {raw}") from exc
        if resolved == root or candidate == Path(".") or ".git" in candidate.parts or ".obsidian" in candidate.parts:
            raise QueueError("workflow-config-mismatch", f"output must identify a scoped project file: {raw}")
        if resolved.exists() and resolved.is_dir():
            raise QueueError("workflow-config-mismatch", f"output must identify a file, not a directory: {raw}")
        text = str(relative)
        if not (text.startswith("raw/") or text.startswith("wiki/") or text in {"index.md", "log.md"}):
            raise QueueError("workflow-config-mismatch", f"output must be under raw/, wiki/, index.md, or log.md: {raw}")
        if text not in result:
            result.append(text)
    return result


def parse_input(text: str, *, default_type: str | None, workflow: str | None) -> list[InputItem]:
    default_type = normalize_type(default_type)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    if any("|" in line for line in lines) and len(lines) >= 2:
        table = parse_table(lines, default_type=default_type, workflow=workflow)
        if table:
            return table
    items: list[InputItem] = []
    for line in lines:
        if re.match(r"^[-*+]\s+", line):
            line = re.sub(r"^[-*+]\s+", "", line)
            match = re.match(r"(?P<ticker>[^\s,(]+)(?:\s*[\[(](?P<type>ETF|Stock|Stock[s]?|ETF[s]?)[\])])?(?:\s+.*)?$", line, re.I)
            if not match:
                raise QueueError("invalid-input", f"cannot parse list item: {line}")
            item_type = normalize_type(match.group("type")) or default_type
            if item_type is None:
                raise QueueError("invalid-instrument-type", f"type is required for {match.group('ticker')}")
            items.append(InputItem(match.group("ticker"), item_type, workflow))
            continue
        for token in line.split(","):
            token = token.strip()
            if not token:
                continue
            match = re.match(r"^(?P<ticker>[^\s(]+)(?:\s*[\[(](?P<type>ETF|Stock|Stock[s]?|ETF[s]?)[\])])?$", token, re.I)
            if not match:
                raise QueueError("invalid-input", f"cannot parse ticker item: {token}")
            item_type = normalize_type(match.group("type")) or default_type
            if item_type is None:
                raise QueueError("invalid-instrument-type", f"type is required for {match.group('ticker')}")
            items.append(InputItem(match.group("ticker"), item_type, workflow))
    return items


def parse_table(lines: Sequence[str], *, default_type: str | None, workflow: str | None) -> list[InputItem]:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines if "|" in line]
    if len(rows) < 2 or not re.fullmatch(r"[-: ]+", rows[1][0] if rows[1] else ""):
        return []
    header = [cell.lower().replace(" ", "_") for cell in rows[0]]
    ticker_index = next((i for i, value in enumerate(header) if value in {"ticker", "symbol", "input_ticker"}), None)
    type_index = next((i for i, value in enumerate(header) if value in {"type", "instrument_type", "instrument"}), None)
    workflow_index = next((i for i, value in enumerate(header) if value in {"workflow", "research_workflow"}), None)
    if ticker_index is None:
        raise QueueError("invalid-input", "Markdown table needs a Ticker column")
    items: list[InputItem] = []
    for row in rows[2:]:
        if len(row) <= ticker_index or not row[ticker_index].strip():
            continue
        if type_index is not None:
            # Once a Type column is present every non-empty row must declare a
            # type explicitly; a command-level default cannot silently classify
            # an ambiguous mixed table row.
            if len(row) <= type_index or not row[type_index].strip():
                raise QueueError("invalid-instrument-type", f"table row has no Type: {row[ticker_index]}")
            row_type = normalize_type(row[type_index])
        else:
            row_type = default_type
        if row_type is None:
            raise QueueError("invalid-instrument-type", f"table row has no Type: {row[ticker_index]}")
        row_workflow = row[workflow_index] if workflow_index is not None and len(row) > workflow_index and row[workflow_index] else workflow
        items.append(InputItem(row[ticker_index], row_type, row_workflow))
    return items


def read_input(args: argparse.Namespace, root: Path) -> tuple[str, str]:
    if bool(args.tickers) == bool(args.input_file):
        raise QueueError("workflow-config-mismatch", "provide exactly one of --tickers or --input-file")
    if args.input_file:
        candidate = Path(args.input_file)
        if candidate.is_absolute():
            raise QueueError("workflow-config-mismatch", "input file must be project-relative")
        path = (root / candidate).resolve()
        try:
            path.relative_to(root)
        except ValueError as exc:
            raise QueueError("workflow-config-mismatch", "input file escapes project root") from exc
        try:
            return path.read_text(encoding="utf-8"), str(path.relative_to(root))
        except FileNotFoundError as exc:
            raise QueueError("input-not-found", f"input file not found: {args.input_file}") from exc
    return args.tickers, "inline"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Deterministic Markdown Research Queue")
    parser.add_argument("--root", default=".", help="saved project checkout")
    subparsers = parser.add_subparsers(dest="command", required=True)

    intake = subparsers.add_parser("intake", help="create a Research Batch and Ready cards")
    intake.add_argument("--tickers")
    intake.add_argument("--input-file")
    intake.add_argument("--type", dest="default_type")
    intake.add_argument("--workflow")
    intake.add_argument("--dry-run", action="store_true")
    intake.add_argument("--now")
    intake.add_argument("--source", default="intake")
    intake.add_argument("--owner", default="research-card-intake")

    seed = subparsers.add_parser("seed", help="one-time seed using normal Intake")
    seed.add_argument("--tickers")
    seed.add_argument("--input-file")
    seed.add_argument("--type", dest="default_type", default="ETF")
    seed.add_argument("--now")
    seed.add_argument("--owner", default="research-card-intake")

    listing = subparsers.add_parser("list", help="list cards")
    listing.add_argument("--status")

    claim = subparsers.add_parser("claim", help="claim one Ready card")
    claim.add_argument("--card-id", required=True)
    claim.add_argument("--owner", required=True)
    claim.add_argument("--phase", default="claimed")
    claim.add_argument("--now")

    claim_next = subparsers.add_parser("claim-next", help="claim oldest supported Ready cards")
    claim_next.add_argument("--count", required=True)
    claim_next.add_argument("--owner", required=True)
    claim_next.add_argument("--keep-lease", action="store_true", help="keep the project lease for later renew/route commands")
    claim_next.add_argument("--now")

    renew = subparsers.add_parser("renew", help="renew one card lease")
    renew.add_argument("--card-id", required=True)
    renew.add_argument("--owner", required=True)
    renew.add_argument("--fencing-token", required=True)
    renew.add_argument("--phase")
    renew.add_argument("--output", action="append", default=[], help="planned durable output path; repeatable")
    renew.add_argument("--lease-token", help="project lease token returned by claim-next --keep-lease")
    renew.add_argument("--now")

    route = subparsers.add_parser("route", help="route one structured research_handoff")
    route.add_argument("--card-id", required=True)
    route.add_argument("--owner", required=True)
    route.add_argument("--fencing-token", required=True)
    route.add_argument("--handoff-json", required=True)
    route.add_argument("--output", action="append", default=[])
    route.add_argument("--entity-key")
    route.add_argument("--commit", action="store_true")
    route.add_argument("--lease-token", help="project lease token returned by claim-next --keep-lease")
    route.add_argument("--now")

    lease_release = subparsers.add_parser("lease-release", help="release a persistent project lease")
    lease_release.add_argument("--owner", required=True)
    lease_release.add_argument("--lease-token", required=True)
    lease_release.add_argument("--now")

    process = subparsers.add_parser("process", help="process Ready cards with a handoff fixture or executable adapter")
    process.add_argument("--count", required=True)
    process.add_argument("--owner", default="research-queue-manager")
    process.add_argument("--execution-profile", default="scheduled-inline")
    process.add_argument("--handoff-json")
    process.add_argument("--handoff-file")
    process.add_argument("--handoff-command", help="command whose stdout is one complete seven-field handoff JSON object")
    process.add_argument("--handoff-timeout-seconds", type=float, default=DEFAULT_HANDOFF_TIMEOUT_SECONDS, help="maximum adapter runtime; must stay below the two-hour lease")
    process.add_argument("--output", action="append", default=[])
    process.add_argument("--output-map", help="project-relative JSON object keyed by card_id or ticker to output path lists")
    process.add_argument("--commit", action="store_true")
    process.add_argument("--now")

    recover = subparsers.add_parser("recover", help="recover expired claims")
    recover.add_argument("--now")

    for name, target in (("hold", STATUS_BLOCKED), ("unblock", STATUS_READY), ("cancel", STATUS_CANCELLED)):
        transition = subparsers.add_parser(name, help=f"move a card to {target}")
        transition.add_argument("--card-id", required=True)
        transition.add_argument("--reason")
        transition.add_argument("--now")
    return parser


def positive_count(value: str) -> int:
    if not re.fullmatch(r"[1-9][0-9]*", value):
        raise QueueError("workflow-config-mismatch", "count must be a positive base-10 integer")
    return int(value)


def process_cards(store: QueueStore, *, count: int, owner: str, execution_profile: str, handoff_provider: Callable[[Card], Mapping[str, Any]], outputs: Sequence[str] = (), output_provider: Callable[[Card], Sequence[str]] | None = None, context_updater: Callable[[str, str, Sequence[str]], None] | None = None, now: dt.datetime | None = None, commit: bool = False) -> dict[str, Any]:
    count = positive_count(str(count))
    if execution_profile not in SUPPORTED_EXECUTION_PROFILES:
        raise QueueError("workflow-config-mismatch", f"unsupported execution profile: {execution_profile}")
    fixed_now = now
    start_now = fixed_now or dt.datetime.now(dt.timezone.utc)
    clock = (lambda: fixed_now) if fixed_now is not None else (lambda: dt.datetime.now(dt.timezone.utc))
    attempted: list[str] = []
    completed: list[str] = []
    blocked: list[str] = []
    skipped: list[dict[str, Any]] = []
    global_failure: dict[str, str] | None = None
    recovery: dict[str, Any] = {"recovered_ready": [], "blocked_partial": []}
    with store.project_lease(owner, start_now) as lease:
        recovery = store.recover(now=clock(), project_lease=lease)
        lease.renew(clock())
        for summary in store.list_cards(STATUS_READY):
            if len(attempted) >= count:
                break
            if summary.get("workflow") != SUPPORTED_ETF_WORKFLOW:
                skipped.append({
                    "card_id": summary.get("card_id"),
                    "ticker": summary.get("input_ticker"),
                    "workflow": summary.get("workflow"),
                    "code": "unsupported-workflow",
                    "reason": "Ready card is outside the V1 ETF processor boundary.",
                })
                continue
            card_id = summary["card_id"]
            attempted.append(card_id)
            card_now = clock()
            claim = store.claim(card_id, owner=owner, now=card_now)
            card = store.load_card(card_id)
            try:
                card_outputs = output_provider(card) if output_provider is not None else outputs
                # Revalidate the card fencing token immediately before the
                # downstream workflow may begin a durable write, and record
                # the planned scope for stale-claim recovery.
                lease.renew(clock())
                store.renew(
                    card_id,
                    owner=owner,
                    fencing_token=claim["fencing_token"],
                    phase="pre-write",
                    outputs=card_outputs,
                    now=clock(),
                )
                card = store.load_card(card_id)
                if context_updater is not None:
                    context_updater(lease.token, execution_profile, card_outputs)
                handoff = handoff_provider(card)
                # Renew again after the bounded adapter/workflow returns so the
                # terminal card/output commit still runs under a live project
                # lease even when the research call takes a substantial time.
                lease.renew(clock())
                routed = store.route(card_id, handoff, owner=owner, fencing_token=claim["fencing_token"], outputs=card_outputs, now=clock(), commit=commit, project_lease=lease)
            except QueueError as exc:
                # A malformed/configuration failure after claim must leave an
                # inspectable known-card global block rather than strand it in
                # In Progress. Fencing/lease failures remain untouched so
                # recovery can make the safe decision.
                if exc.global_failure and exc.code not in {"claim-state-error", "manager-overlap"}:
                    blocked_result = store._route_blocked(
                        card,
                        clock(),
                        status="ERROR",
                        scope="global",
                        code=exc.code,
                        reason=exc.message,
                        durable_write="unknown",
                        confirmation="none",
                        global_blocked=True,
                        project_lease=lease,
                    )
                    blocked.append(card_id)
                    global_failure = {"code": blocked_result["result_code"], "reason": blocked_result["result_reason"]}
                else:
                    global_failure = {"code": exc.code, "reason": exc.message}
                break
            if routed.get("global_blocked"):
                global_failure = {"code": routed.get("result_code", "unknown-result"), "reason": routed.get("result_reason", "global result failure")}
                blocked.append(card_id)
                break
            if routed.get("status") == STATUS_DONE:
                completed.append(card_id)
            else:
                blocked.append(card_id)
            lease.renew(clock())
    return {
        "command": "process",
        "execution_profile": execution_profile,
        "requested_count": count,
        "attempted": attempted,
        "completed": completed,
        "blocked": blocked,
        "skipped": skipped,
        "recovered_ready": recovery["recovered_ready"],
        "recovered_blocked": recovery["blocked_partial"],
        "recovered_done": recovery.get("recovered_done", []),
        "global_failure": global_failure,
    }


def load_handoff(raw: str) -> Mapping[str, Any]:
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise QueueError("workflow-config-mismatch", f"invalid handoff JSON: {exc.msg}") from exc
    if not isinstance(value, Mapping):
        raise QueueError("workflow-config-mismatch", "handoff JSON must be an object")
    return value


def load_output_map(raw: str, root: Path) -> dict[str, list[str]]:
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise QueueError("workflow-config-mismatch", f"invalid output map JSON: {exc.msg}") from exc
    if not isinstance(value, Mapping):
        raise QueueError("workflow-config-mismatch", "output map must be an object")
    result: dict[str, list[str]] = {}
    for key, outputs in value.items():
        if not isinstance(key, str) or not key.strip() or not isinstance(outputs, list) or not all(isinstance(path, str) for path in outputs):
            raise QueueError("workflow-config-mismatch", "output map values must be string path lists")
        result[key.strip()] = normalize_output_paths(root, outputs)
    return result


def dispatch(args: argparse.Namespace) -> dict[str, Any]:
    root = Path(args.root).expanduser().resolve()
    store = QueueStore(root)
    if args.command in {"intake", "seed"}:
        source_text, source_name = read_input(args, root)
        source = "one-time-seed" if args.command == "seed" else args.source
        if getattr(args, "dry_run", False):
            return store.intake(source_text, default_type=args.default_type, workflow=getattr(args, "workflow", None), dry_run=True, source=source, now=parse_time(args.now))
        with store.project_lease(args.owner, parse_time(args.now)):
            return store.intake(source_text, default_type=args.default_type, workflow=getattr(args, "workflow", None), source=source, now=parse_time(args.now))
    if args.command == "list":
        return {"command": "list", "cards": store.list_cards(args.status)}
    if args.command == "claim":
        with store.project_lease(args.owner, parse_time(args.now)):
            return store.claim(args.card_id, owner=args.owner, phase=args.phase, now=parse_time(args.now))
    if args.command == "claim-next":
        count = positive_count(args.count)
        claimed: list[dict[str, Any]] = []
        skipped: list[dict[str, Any]] = []
        lease_now = parse_time(args.now)

        def select_cards() -> None:
            for summary in store.list_cards(STATUS_READY):
                if len(claimed) >= count:
                    break
                if summary.get("workflow") != SUPPORTED_ETF_WORKFLOW:
                    skipped.append({
                        "card_id": summary.get("card_id"),
                        "ticker": summary.get("input_ticker"),
                        "workflow": summary.get("workflow"),
                        "code": "unsupported-workflow",
                        "reason": "Ready card is outside the V1 ETF processor boundary.",
                    })
                    continue
                claimed.append(store.claim(summary["card_id"], owner=args.owner, now=lease_now))

        persistent_lease: ProjectLease | None = None
        recovery: dict[str, Any]
        if args.keep_lease:
            persistent_lease = store.project_lease(args.owner, lease_now)
            persistent_lease.acquire()
            try:
                recovery = store.recover(now=lease_now, project_lease=persistent_lease)
                persistent_lease.renew(lease_now)
                select_cards()
            except Exception:
                persistent_lease.release()
                raise
            if not claimed:
                persistent_lease.release()
        else:
            with store.project_lease(args.owner, lease_now) as lease:
                recovery = store.recover(now=lease_now, project_lease=lease)
                select_cards()

        result = {"command": "claim-next", "requested_count": count, "claimed": claimed, "skipped": skipped, "recovered_ready": recovery["recovered_ready"], "recovered_blocked": recovery["blocked_partial"], "recovered_done": recovery.get("recovered_done", [])}
        if persistent_lease and claimed:
            result["lease_token"] = persistent_lease.token
        return result
    if args.command == "renew":
        command_now = parse_time(args.now) if args.now else None
        lease_now = command_now or dt.datetime.now(dt.timezone.utc)
        if args.lease_token:
            lease = store.existing_project_lease(args.owner, args.lease_token, lease_now)
            try:
                lease.renew(lease_now)
                return store.renew(args.card_id, owner=args.owner, fencing_token=args.fencing_token, phase=args.phase, outputs=args.output, now=command_now)
            except QueueError:
                lease.release()
                raise
            except Exception:
                lease.release()
                raise
        with store.project_lease(args.owner, lease_now):
            return store.renew(args.card_id, owner=args.owner, fencing_token=args.fencing_token, phase=args.phase, outputs=args.output, now=command_now)
    if args.command == "route":
        command_now = parse_time(args.now) if args.now else None
        lease_now = command_now or dt.datetime.now(dt.timezone.utc)
        if args.lease_token:
            lease = store.existing_project_lease(args.owner, args.lease_token, lease_now)
            try:
                lease.renew(lease_now)
                handoff = load_handoff(args.handoff_json)
                result = store.route(args.card_id, handoff, owner=args.owner, fencing_token=args.fencing_token, outputs=args.output, entity_key=args.entity_key, now=command_now, commit=args.commit, project_lease=lease)
            except QueueError:
                lease.release()
                raise
            except Exception:
                lease.release()
                raise
            if result.get("global_blocked"):
                lease.release()
            return result
        handoff = load_handoff(args.handoff_json)
        with store.project_lease(args.owner, lease_now) as lease:
            return store.route(args.card_id, handoff, owner=args.owner, fencing_token=args.fencing_token, outputs=args.output, entity_key=args.entity_key, now=command_now, commit=args.commit, project_lease=lease)
    if args.command == "lease-release":
        command_now = parse_time(args.now)
        lease = store.existing_project_lease(args.owner, args.lease_token, command_now)
        lease.release()
        return {"command": "lease-release", "owner": args.owner, "released": True}
    if args.command == "process":
        sources = sum(bool(value) for value in (args.handoff_json, args.handoff_file, args.handoff_command))
        if sources != 1:
            raise QueueError("workflow-config-mismatch", "process requires exactly one handoff JSON, project-relative handoff file, or executable adapter")
        requested_count = positive_count(args.count)
        if args.output and args.output_map:
            raise QueueError("workflow-config-mismatch", "provide either --output or --output-map, not both")
        if requested_count > 1 and args.output and not args.output_map:
            raise QueueError("workflow-config-mismatch", "batch processing requires per-card --output-map; one static output scope is unsafe")
        output_map: dict[str, list[str]] = {}
        if args.output_map:
            map_path = (root / args.output_map).resolve()
            try:
                map_path.relative_to(root)
            except ValueError as exc:
                raise QueueError("workflow-config-mismatch", "output map escapes project root") from exc
            output_map = load_output_map(map_path.read_text(encoding="utf-8"), root)
        adapter_context: dict[str, Any] = {}
        context_updater: Callable[[str, str, Sequence[str]], None] | None = None
        if args.handoff_json:
            handoff = load_handoff(args.handoff_json)
            handoff_provider: Callable[[Card], Mapping[str, Any]] = lambda _card: handoff
        elif args.handoff_file:
            path = (root / args.handoff_file).resolve()
            try:
                path.relative_to(root)
            except ValueError as exc:
                raise QueueError("workflow-config-mismatch", "handoff file escapes project root") from exc
            handoff = load_handoff(path.read_text(encoding="utf-8"))
            handoff_provider = lambda _card: handoff
        else:
            try:
                command = shlex.split(args.handoff_command)
            except ValueError as exc:
                raise QueueError("workflow-config-mismatch", f"invalid handoff command: {exc}") from exc
            if not command:
                raise QueueError("workflow-config-mismatch", "handoff command cannot be empty")
            if args.handoff_timeout_seconds <= 0 or args.handoff_timeout_seconds >= 2 * 60 * 60:
                raise QueueError("workflow-config-mismatch", "handoff timeout must be positive and less than the two-hour lease")

            def command_provider(card: Card) -> Mapping[str, Any]:
                env = os.environ.copy()
                env.update({
                    "RESEARCH_CARD_ID": str(card.props["card_id"]),
                    "RESEARCH_CARD_PATH": str(card.path.relative_to(root)),
                    "RESEARCH_TICKER": str(card.props["input_ticker"]),
                    "RESEARCH_WORKFLOW": str(card.props["workflow"]),
                    "RESEARCH_CARD_FENCING_TOKEN": str(card.props["fencing_token"]),
                    "RESEARCH_PROJECT_LEASE_TOKEN": str(adapter_context.get("project_lease_token") or ""),
                    "RESEARCH_EXECUTION_PROFILE": str(adapter_context.get("execution_profile") or args.execution_profile),
                    "RESEARCH_OUTPUT_PATHS": json.dumps(adapter_context.get("output_paths") or [], ensure_ascii=False),
                })
                try:
                    completed = subprocess.run(command, cwd=root, env=env, check=False, capture_output=True, text=True, timeout=args.handoff_timeout_seconds)
                except OSError as exc:
                    raise QueueError("workflow-config-mismatch", f"Handoff adapter could not start: {exc}") from exc
                except subprocess.TimeoutExpired as exc:
                    return {
                        "status": "BLOCKED",
                        "scope": "global",
                        "durable_write": "unknown",
                        "exhausted": True,
                        "confirmation": "none",
                        "code": "unknown-result",
                        "reason": f"Handoff adapter exceeded timeout ({args.handoff_timeout_seconds:g}s): {exc}",
                    }
                if completed.returncode != 0:
                    detail = (completed.stderr or completed.stdout).strip() or f"adapter exited with status {completed.returncode}"
                    return {
                        "status": "ERROR",
                        "scope": "global",
                        "durable_write": "unknown",
                        "exhausted": True,
                        "confirmation": "none",
                        "code": "unknown-result",
                        "reason": detail,
                    }
                try:
                    return load_handoff(completed.stdout)
                except QueueError as exc:
                    return {
                        "status": "BLOCKED",
                        "scope": "global",
                        "durable_write": "unknown",
                        "exhausted": True,
                        "confirmation": "none",
                        "code": "unknown-result",
                        "reason": exc.message,
                    }

            handoff_provider = command_provider
            def update_adapter_context(project_lease_token: str, execution_profile: str, card_outputs: Sequence[str]) -> None:
                adapter_context.update({
                    "project_lease_token": project_lease_token,
                    "execution_profile": execution_profile,
                    "output_paths": list(card_outputs),
                })
            context_updater = update_adapter_context
        process_now = parse_time(args.now) if args.now else None
        output_provider = None
        if output_map:
            def map_outputs(card: Card) -> Sequence[str]:
                return output_map.get(str(card.props["card_id"]), output_map.get(str(card.props["input_ticker"]), []))
            output_provider = map_outputs
        return process_cards(store, count=requested_count, owner=args.owner, execution_profile=args.execution_profile, handoff_provider=handoff_provider, outputs=args.output, output_provider=output_provider, context_updater=context_updater, now=process_now, commit=args.commit)
    if args.command == "recover":
        recovery_now = parse_time(args.now) if args.now else None
        lease_now = recovery_now or dt.datetime.now(dt.timezone.utc)
        with store.project_lease("research-queue-recovery", lease_now) as lease:
            return store.recover(now=recovery_now, project_lease=lease)
    if args.command in {"hold", "unblock", "cancel"}:
        target = {"hold": STATUS_BLOCKED, "unblock": STATUS_READY, "cancel": STATUS_CANCELLED}[args.command]
        with store.project_lease("research-queue-human", parse_time(args.now)):
            return store.transition(args.card_id, target, reason=args.reason, now=parse_time(args.now))
    raise QueueError("workflow-config-mismatch", f"unknown command: {args.command}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
        result = dispatch(args)
    except QueueError as exc:
        print(json.dumps({"error": {"code": exc.code, "reason": exc.message, "global": exc.global_failure}}, ensure_ascii=False))
        return 2
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": {"code": "queue-runtime-error", "reason": str(exc), "global": True}}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
