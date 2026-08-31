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
import hashlib
import json
import os
import re
import secrets
import subprocess
import sys
import tempfile
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Iterator, Mapping, Sequence


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
    "execution_phase",
    "result_status",
    "result_scope",
    "result_code",
    "result_reason",
    "durable_write",
    "confirmation",
    "output_paths",
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


class QueueError(Exception):
    """A user-visible deterministic queue error."""

    def __init__(self, code: str, message: str, *, global_failure: bool = True):
        super().__init__(message)
        self.code = code
        self.message = message
        self.global_failure = global_failure


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def parse_time(value: str | None) -> dt.datetime:
    if not value:
        return dt.datetime.now(dt.timezone.utc)
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
        temporary = Path(handle.name)
    os.replace(temporary, path)


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
        self.acquired = False

    def _payload(self, now: dt.datetime) -> dict[str, Any]:
        return {
            "owner": self.owner,
            "fencing_token": self.token,
            "acquired_at": iso_time(now),
            "lease_expires_at": iso_time(now + self.ttl),
        }

    def acquire(self) -> "ProjectLease":
        self.store.runtime_dir.mkdir(parents=True, exist_ok=True)
        payload = self._payload(self.now)
        for _ in range(2):
            try:
                descriptor = os.open(self.path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            except FileExistsError:
                try:
                    existing = json.loads(self.path.read_text(encoding="utf-8"))
                    expires = parse_time(existing.get("lease_expires_at"))
                except (OSError, json.JSONDecodeError, QueueError):
                    raise QueueError("manager-overlap", "queue lease exists and cannot be inspected")
                if expires > self.now:
                    raise QueueError("manager-overlap", f"queue lease held by {existing.get('owner', 'unknown')}")
                try:
                    self.path.unlink()
                except FileNotFoundError:
                    continue
                continue
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                json.dump(payload, handle, ensure_ascii=False)
            self.acquired = True
            return self
        raise QueueError("manager-overlap", "queue lease could not be acquired")

    def renew(self, now: dt.datetime) -> None:
        if not self.acquired:
            raise QueueError("manager-overlap", "queue lease is not held")
        try:
            current = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise QueueError("manager-overlap", "queue lease disappeared") from exc
        if current.get("fencing_token") != self.token or current.get("owner") != self.owner:
            raise QueueError("manager-overlap", "queue lease fencing token changed")
        atomic_write(self.path, json.dumps(self._payload(now), ensure_ascii=False))

    def release(self) -> None:
        if not self.acquired:
            return
        try:
            current = json.loads(self.path.read_text(encoding="utf-8"))
            if current.get("fencing_token") == self.token:
                self.path.unlink(missing_ok=True)
        except (OSError, json.JSONDecodeError):
            pass
        self.acquired = False
        try:
            self.path.parent.rmdir()
            self.store.queue_dir.rmdir()
        except OSError:
            pass

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
        if props.get("kind") != "research-card" or props.get("card_id") != card_id:
            raise QueueError("invalid-card", f"card identity mismatch: {card_id}")
        if props.get("status") not in CARD_STATUSES:
            raise QueueError("invalid-card", f"unsupported card status: {props.get('status')}")
        return Card(props, body, path)

    def write_card(self, card: Card) -> None:
        atomic_write(card.path, dump_markdown(card.props, card.body))

    def iter_cards(self) -> Iterator[Card]:
        if not self.cards_dir.exists():
            return
        for path in sorted(self.cards_dir.glob("rc-*.md")):
            try:
                props, body = parse_markdown(path.read_text(encoding="utf-8"))
                if props.get("kind") == "research-card" and props.get("card_id"):
                    yield Card(props, body, path)
            except QueueError:
                continue

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
            card = Card(props, "This Research Card tracks one instrument and one explicit Research Workflow.\n", self.card_path(card_id))
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
        atomic_write(self.batch_path(batch_id), dump_markdown(batch_props, "This Research Batch records card materialization, not downstream research completion.\n"))
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
        card = self.load_card(card_id)
        if card.props.get("status") != STATUS_READY:
            raise QueueError("claim-state-error", f"card is not Ready: {card_id}")
        if card.props.get("workflow") != SUPPORTED_ETF_WORKFLOW:
            raise QueueError("unsupported-workflow", f"card workflow is not supported in V1: {card.props.get('workflow')}")
        token = uuid.uuid4().hex
        card.props.update({
            "status": STATUS_IN_PROGRESS,
            "updated_at": iso_time(now),
            "claim_owner": owner,
            "claimed_at": iso_time(now),
            "lease_expires_at": iso_time(now + dt.timedelta(hours=2)),
            "fencing_token": token,
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

    def renew(self, card_id: str, *, owner: str, fencing_token: str, now: dt.datetime | None = None, phase: str | None = None) -> dict[str, Any]:
        now = now or dt.datetime.now(dt.timezone.utc)
        card = self.load_card(card_id)
        assert_claim(card, owner, fencing_token, now)
        card.props["lease_expires_at"] = iso_time(now + dt.timedelta(hours=2))
        if phase:
            card.props["execution_phase"] = phase
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
    ) -> dict[str, Any]:
        now = now or dt.datetime.now(dt.timezone.utc)
        card = self.load_card(card_id)
        assert_claim(card, owner, fencing_token, now)
        normalized, validation_error = validate_handoff(handoff)
        if validation_error:
            return self._route_blocked(
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

        output_paths = normalize_output_paths(self.root, outputs)
        if normalized["status"] == "PASS" and normalized["scope"] == "item" and normalized["durable_write"] == "completed" and normalized["exhausted"] is False and normalized["confirmation"] == "none" and normalized["code"] in SUCCESS_CODES:
            missing = [path for path in output_paths if not (self.root / path).exists()]
            if missing:
                return self._route_blocked(
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
                "output_links": [f"[[{path[:-3] if path.endswith('.md') else path}]]" for path in output_paths],
                "commit_id": f"queue/{card_id}",
            })
            clear_claim(card.props)
            if entity_key:
                card.props["entity_key"] = entity_key
            self.write_card(card)
            commit_result = self._commit_terminal(card, output_paths, now) if commit else {"committed": False}
            if commit and not commit_result.get("committed") and commit_result.get("error"):
                failed = self.load_card(card_id)
                return self._route_blocked(
                    failed,
                    now,
                    status="ERROR",
                    scope="global",
                    code="git-commit-failed",
                    reason=commit_result["error"],
                    durable_write="completed",
                    confirmation="none",
                    global_blocked=True,
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
            return self._route_blocked(
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
        return self._route_blocked(
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
    ) -> dict[str, Any]:
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
        clear_claim(card.props)
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
            return {"committed": False, "reason": "not-a-git-checkout"}
        message = f"research: complete {card.props['input_ticker']} ({card.props['card_id']})"
        add_result = subprocess.run(["git", "-C", str(self.root), "add", "--", *paths], check=False, capture_output=True, text=True)
        if add_result.returncode != 0:
            return {"committed": False, "error": (add_result.stderr or add_result.stdout).strip() or "git add failed"}
        command = ["git", "-C", str(self.root), "commit", "--only", "-m", message, "--", *paths]
        try:
            completed = subprocess.run(command, check=False, capture_output=True, text=True)
        except OSError as exc:
            return {"committed": False, "error": str(exc)}
        if completed.returncode != 0:
            subprocess.run(["git", "-C", str(self.root), "reset", "-q", "--", *paths], check=False, capture_output=True, text=True)
            return {"committed": False, "error": (completed.stderr or completed.stdout).strip() or "git commit failed"}
        sha = subprocess.run(["git", "-C", str(self.root), "rev-parse", "HEAD"], check=False, capture_output=True, text=True).stdout.strip()
        return {"committed": True, "commit_sha": sha}

    def recover(self, *, now: dt.datetime | None = None) -> dict[str, Any]:
        now = now or dt.datetime.now(dt.timezone.utc)
        ready: list[dict[str, Any]] = []
        blocked: list[dict[str, Any]] = []
        for card in list(self.iter_cards()):
            if card.props.get("status") != STATUS_IN_PROGRESS:
                continue
            expiry_text = card.props.get("lease_expires_at")
            if not expiry_text or parse_time(str(expiry_text)) > now:
                continue
            phase = str(card.props.get("execution_phase") or "").lower()
            output_paths = card.props.get("output_paths") or []
            partial = phase in {"writing", "finalizing"} or bool(output_paths)
            if partial:
                item = self._route_recovery(card, now, ready_state=False)
                blocked.append(item)
            else:
                item = self._route_recovery(card, now, ready_state=True)
                ready.append(item)
        return {"command": "recover", "recovered_ready": ready, "blocked_partial": blocked}

    def _route_recovery(self, card: Card, now: dt.datetime, *, ready_state: bool) -> dict[str, Any]:
        if ready_state:
            card.props.update({
                "status": STATUS_READY,
                "updated_at": iso_time(now),
                "execution_phase": "recovered-ready",
                "result_code": "lease-expired",
                "result_reason": "Expired claim had no durable output write.",
            })
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
    for key in ("claim_owner", "claimed_at", "lease_expires_at", "fencing_token"):
        props.pop(key, None)


def assert_claim(card: Card, owner: str, token: str, now: dt.datetime) -> None:
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
    fields = ("card_id", "title", "status", "workflow", "instrument_type", "input_ticker", "created_at", "updated_at", "lease_expires_at", "fencing_token", "execution_phase", "result_code", "output_paths")
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
    if status not in HANDOFF_STATUSES or scope not in HANDOFF_SCOPES or durable_write not in HANDOFF_WRITES or confirmation not in HANDOFF_CONFIRMATIONS or not isinstance(exhausted, bool) or not code or not isinstance(reason, str) or not reason.strip():
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


def normalize_output_paths(root: Path, outputs: Sequence[str]) -> list[str]:
    result: list[str] = []
    for raw in outputs:
        candidate = Path(raw)
        if candidate.is_absolute():
            raise QueueError("workflow-config-mismatch", f"output must be project-relative: {raw}")
        resolved = (root / candidate).resolve()
        try:
            relative = resolved.relative_to(root)
        except ValueError as exc:
            raise QueueError("workflow-config-mismatch", f"output escapes project root: {raw}") from exc
        text = str(relative)
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
        row_type = normalize_type(row[type_index]) if type_index is not None and len(row) > type_index and row[type_index] else default_type
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
    claim_next.add_argument("--now")

    renew = subparsers.add_parser("renew", help="renew one card lease")
    renew.add_argument("--card-id", required=True)
    renew.add_argument("--owner", required=True)
    renew.add_argument("--fencing-token", required=True)
    renew.add_argument("--phase")
    renew.add_argument("--now")

    route = subparsers.add_parser("route", help="route one structured research_handoff")
    route.add_argument("--card-id", required=True)
    route.add_argument("--owner", required=True)
    route.add_argument("--fencing-token", required=True)
    route.add_argument("--handoff-json", required=True)
    route.add_argument("--output", action="append", default=[])
    route.add_argument("--entity-key")
    route.add_argument("--commit", action="store_true")
    route.add_argument("--now")

    process = subparsers.add_parser("process", help="process Ready cards with a supplied handoff fixture")
    process.add_argument("--count", required=True)
    process.add_argument("--owner", default="research-queue-manager")
    process.add_argument("--execution-profile", default="scheduled-inline")
    process.add_argument("--handoff-json")
    process.add_argument("--handoff-file")
    process.add_argument("--output", action="append", default=[])
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


def process_cards(store: QueueStore, *, count: int, owner: str, execution_profile: str, handoff_provider: Callable[[Card], Mapping[str, Any]], outputs: Sequence[str] = (), now: dt.datetime | None = None, commit: bool = False) -> dict[str, Any]:
    count = positive_count(str(count))
    if execution_profile not in SUPPORTED_EXECUTION_PROFILES:
        raise QueueError("workflow-config-mismatch", f"unsupported execution profile: {execution_profile}")
    now = now or dt.datetime.now(dt.timezone.utc)
    attempted: list[str] = []
    completed: list[str] = []
    blocked: list[str] = []
    global_failure: dict[str, str] | None = None
    with store.project_lease(owner, now) as lease:
        for summary in store.list_cards(STATUS_READY):
            if len(attempted) >= count:
                break
            if summary.get("workflow") != SUPPORTED_ETF_WORKFLOW:
                continue
            card_id = summary["card_id"]
            attempted.append(card_id)
            claim = store.claim(card_id, owner=owner, now=now)
            card = store.load_card(card_id)
            try:
                handoff = handoff_provider(card)
                routed = store.route(card_id, handoff, owner=owner, fencing_token=claim["fencing_token"], outputs=outputs, now=now, commit=commit)
            except QueueError as exc:
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
            lease.renew(now)
    return {
        "command": "process",
        "execution_profile": execution_profile,
        "requested_count": count,
        "attempted": attempted,
        "completed": completed,
        "blocked": blocked,
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


def dispatch(args: argparse.Namespace) -> dict[str, Any]:
    root = Path(args.root).expanduser().resolve()
    store = QueueStore(root)
    if args.command in {"intake", "seed"}:
        source_text, source_name = read_input(args, root)
        source = "one-time-seed" if args.command == "seed" else args.source
        with store.project_lease(args.owner, parse_time(args.now)):
            return store.intake(source_text, default_type=args.default_type, workflow=getattr(args, "workflow", None), dry_run=getattr(args, "dry_run", False), source=source, now=parse_time(args.now))
    if args.command == "list":
        return {"command": "list", "cards": store.list_cards(args.status)}
    if args.command == "claim":
        with store.project_lease(args.owner, parse_time(args.now)):
            return store.claim(args.card_id, owner=args.owner, phase=args.phase, now=parse_time(args.now))
    if args.command == "claim-next":
        count = positive_count(args.count)
        claimed: list[dict[str, Any]] = []
        with store.project_lease(args.owner, parse_time(args.now)):
            for summary in store.list_cards(STATUS_READY):
                if len(claimed) >= count:
                    break
                if summary.get("workflow") != SUPPORTED_ETF_WORKFLOW:
                    continue
                claimed.append(store.claim(summary["card_id"], owner=args.owner, now=parse_time(args.now)))
        return {"command": "claim-next", "requested_count": count, "claimed": claimed}
    if args.command == "renew":
        with store.project_lease(args.owner, parse_time(args.now)):
            return store.renew(args.card_id, owner=args.owner, fencing_token=args.fencing_token, phase=args.phase, now=parse_time(args.now))
    if args.command == "route":
        handoff = load_handoff(args.handoff_json)
        with store.project_lease(args.owner, parse_time(args.now)):
            return store.route(args.card_id, handoff, owner=args.owner, fencing_token=args.fencing_token, outputs=args.output, entity_key=args.entity_key, now=parse_time(args.now), commit=args.commit)
    if args.command == "process":
        if not args.handoff_json and not args.handoff_file:
            raise QueueError("workflow-config-mismatch", "process requires a structured handoff fixture or a project-relative handoff file")
        if args.handoff_json and args.handoff_file:
            raise QueueError("workflow-config-mismatch", "provide only one handoff fixture")
        if args.handoff_file:
            path = (root / args.handoff_file).resolve()
            try:
                path.relative_to(root)
            except ValueError as exc:
                raise QueueError("workflow-config-mismatch", "handoff file escapes project root") from exc
            raw_handoff = path.read_text(encoding="utf-8")
        else:
            raw_handoff = args.handoff_json
        handoff = load_handoff(raw_handoff)
        return process_cards(store, count=positive_count(args.count), owner=args.owner, execution_profile=args.execution_profile, handoff_provider=lambda _card: handoff, outputs=args.output, now=parse_time(args.now), commit=args.commit)
    if args.command == "recover":
        with store.project_lease("research-queue-recovery", parse_time(args.now)):
            return store.recover(now=parse_time(args.now))
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
