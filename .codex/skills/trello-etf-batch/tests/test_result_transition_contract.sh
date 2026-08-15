#!/usr/bin/env bash
set -euo pipefail

skill_file="${1:-.codex/skills/trello-etf-result/SKILL.md}"

assert_contains() {
  local needle="$1"
  rg -Fq "$needle" "$skill_file" || {
    echo "missing result contract: $needle" >&2
    exit 1
  }
}

assert_not_contains() {
  local needle="$1"
  if rg -Fq "$needle" "$skill_file"; then
    echo "unexpected result ownership: $needle" >&2
    exit 1
  fi
}

assert_contains 'status: PASS|WARNING|CHANGES_REQUIRED|BLOCKED|ERROR'
assert_contains 'scope: item|global|unknown'
assert_contains 'durable_write: completed|not_completed|unknown'
assert_contains 'exhausted: true|false'
assert_contains 'confirmation: none|required|confirmed'
assert_contains 'code: <normalized-stable-code>'
assert_contains 'reason: <concise-one-sentence-reason>'
assert_contains 'Only this combination is success: PASS + scope item + durable_write completed + exhausted false + confirmation none + success or durable-write-complete'
assert_contains 'For a successful result, require status PASS, scope item, durable_write completed, exhausted false, confirmation none'
assert_contains 'When the exact child target and child identity are already resolved'
assert_contains 'invalid or contradictory envelope is a known-child failure'
assert_contains 'result_code: unknown-result'
assert_contains 'Return `global_blocked` to the manager only'
assert_contains 'The manager'
assert_contains 'must stop and not continue'
assert_contains 'other cards after `global_blocked`'
assert_contains 'Do not claim'
assert_contains 'any unconfirmed mutation'
assert_contains 'Non-success results are WARNING, CHANGES_REQUIRED, BLOCKED, or ERROR'
assert_contains 'Closed result decision matrix'
assert_contains 'WARNING` + `scope: item` + `durable_write: not_completed'
assert_contains 'CHANGES_REQUIRED` or `BLOCKED` + `scope: item`'
assert_contains 'ERROR` + `scope: item` + `durable_write: not_completed'
assert_contains 'Do not accept `scope: global` or `scope: unknown` as an ordinary item result'
assert_contains 'exact complete envelope as'
assert_contains 'normalized invalid-envelope global-stop sentinel'
assert_contains 'status: ERROR'
assert_contains 'scope: global'
assert_contains 'durable_write: unknown'
assert_contains 'exhausted: false'
assert_contains 'confirmation: none'
assert_contains 'code: unknown-result'
assert_contains 'require its current lane to be `In Progress`'
assert_contains 'return global `claim-state-error`/state error'
assert_contains 'with no'
assert_contains 'card mutation'
assert_contains 'move to Done, complete it'
assert_contains 'For every non-success or invalid envelope'
assert_contains 'append/update result_status, result_scope, result_code, result_reason, durable_write and confirmation'
assert_contains 'move to Blocked'
assert_contains 'Do not complete it'
assert_contains 'preserve workflow/parent_ari/ticker'
assert_contains 'Trello mutation/auth failure is global'

assert_not_contains 'create an exception card'
assert_not_contains 'create or reuse exactly one exception card'
