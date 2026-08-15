---
name: trello-etf-result
description: "Use when a Trello ETF child card needs to be moved to Done or Blocked from a validated processing result."
---

# Trello ETF Result Router

Route one already-selected Trello ETF child card from the complete result
envelope returned by Skill 3. This skill owns only the selected child result
transition. It does not select cards, create cards, invoke ETF research, write
vault files, or manage the parent workflow.

## Required target and inputs

Require one exact child-card target by Trello card URL or ARI. Do not search by
title, ticker, or workflow key. Resolve exactly one card directly; zero or
multiple resolutions are global failures.

The resolved child must contain and preserve these identity lines:

```text
workflow: trello-etf-item
parent_ari: <resolved parent card ARI>
ticker: <canonical uppercase TICKER>
```

Consume the complete Skill 3 result envelope. Require all seven fields,
including their allowed values and normalized stable-code form:

```text
status: PASS|WARNING|CHANGES_REQUIRED|BLOCKED|ERROR
scope: item|global|unknown
durable_write: completed|not_completed|unknown
exhausted: true|false
confirmation: none|required|confirmed
code: <normalized-stable-code>
reason: <concise-one-sentence-reason>
```

Normalize `code` by trimming, lowercasing, and replacing spaces and underscores
with hyphens. A missing, malformed, unknown, or contradictory field makes the
envelope invalid. The invalid-envelope routing rule below applies only after
the exact child target and child identity have already been resolved.

Before any description update or lane mutation, directly reread the resolved
child and require its current lane to be `In Progress`. If the reread does not
confirm `In Progress`, return global `claim-state-error`/state error with no
card mutation. Never reprocess a child in `Ready for AI`, `Blocked`, or `Done`.

## Strict success contract

Only this combination is success: PASS + scope item + durable_write completed + exhausted false + confirmation none + success or durable-write-complete

For a successful result, require status PASS, scope item, durable_write completed, exhausted false, confirmation none, and normalized `code` equal to
`success` or `durable-write-complete`. Then:

1. Preserve every existing child description line and metadata. Do not replace
   `workflow`, `parent_ari`, or `ticker`.
2. Move the selected child to `Done`.
3. Complete the selected child.
4. Return the confirmed child card identity and any output links supplied by
   the result envelope.

For strict success, move to Done, complete it, preserve metadata, and return
card/output links.

Do not call a result successful merely because its status is PASS. All seven
fields and the exact combination above are required.

Non-success results are WARNING, CHANGES_REQUIRED, BLOCKED, or ERROR.

## Closed result decision matrix

After recognizing the invalid-envelope sentinel below, accept only these
item-scoped combinations as ordinary results:

- `PASS` + `scope: item` + `durable_write: completed` + `exhausted: false` +
  `confirmation: none` + `code: success|durable-write-complete` is strict
  success.
- `WARNING` + `scope: item` + `durable_write: not_completed` +
  `exhausted: false` + `confirmation: required` +
  `code: review-warning|confirmation-required` is an accepted item block.
- `CHANGES_REQUIRED` or `BLOCKED` + `scope: item` +
  `durable_write: not_completed` + `exhausted: true` + `confirmation: none` +
  `code: unsupported-etf-type|item-pre-save-non-pass|item-hard-data-gap|item-downstream-error`
  is an accepted item block.
- `ERROR` + `scope: item` + `durable_write: not_completed` +
  `exhausted: false` + `confirmation: none` +
  `code: research-sub-agent-unavailable|item-downstream-error` is an accepted
  item block.

Do not accept `scope: global` or `scope: unknown` as an ordinary item result.
Any other status, field combination, or stable code is contradictory/invalid
and follows the known-child global-stop rule below.

## Blocked routing contract

For every non-success or invalid envelope, append/update result_status, result_scope, result_code, result_reason, durable_write and confirmation in the child description. For every non-success or invalid envelope, append or update these result
metadata lines in the child description:

```text
result_status: <status>
result_scope: <scope>
result_code: <normalized-stable-code>
result_reason: <reason>
durable_write: <completed|not_completed|unknown>
confirmation: <none|required|confirmed>
```

## Invalid-envelope global stop

Before applying the ordinary matrix, recognize this exact complete envelope as
the normalized invalid-envelope global-stop sentinel:

```text
status: ERROR
scope: global
durable_write: unknown
exhausted: false
confirmation: none
code: unknown-result
reason: <missing, malformed, or contradictory downstream result>
```

When the exact child target and child identity are already resolved, an invalid or contradictory envelope is a known-child failure. Persist this exact safe
failure metadata on that selected child:

```text
result_status: BLOCKED
result_scope: global
result_code: unknown-result
result_reason: <concise validation-failure reason>
durable_write: unknown
confirmation: none
```

Then move that child to `Blocked`. Return `global_blocked` to the manager only
after the description update and lane move are each confirmed. The manager
must stop and not continue to other cards after `global_blocked`. Do not claim
any unconfirmed mutation. If the exact child target or child identity was not
resolved, stop as a global pre-mutation failure without changing a card.

An invalid or contradictory envelope is therefore global_blocked for the
manager but still uses the selected child as the safe persistence owner.

Keep the existing child metadata intact, especially `workflow`, `parent_ari`,
and `ticker`. For a valid non-success envelope, persist its normalized result
fields and concise reason, then move the child to `Blocked`. For an invalid or
contradictory envelope, use the exact `unknown-result` metadata and
`global_blocked` stop above. For every non-success or invalid envelope, move to Blocked.
preserve workflow/parent_ari/ticker. Do not complete it. Exception-card
creation is prohibited: the selected child owns its own failure state.

Return the confirmed child card identity, final lane, persisted result
metadata, and the result/output links when available. A non-success result is
not a global failure merely because it is non-success; it is routed to the
selected child. Trello mutation, card lookup, authentication, board, or tool
failure is global: report the confirmed state, do not claim an unconfirmed
move or completion, and do not create any exception card. Trello mutation/auth failure is global.
