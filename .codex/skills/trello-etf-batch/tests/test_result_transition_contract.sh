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
assert_contains 'move to Done, complete it'
assert_contains 'For every non-success or invalid envelope'
assert_contains 'append/update result_status, result_scope, result_code, result_reason, durable_write and confirmation'
assert_contains 'move to Blocked'
assert_contains 'Do not complete it'
assert_contains 'preserve workflow/parent_ari/ticker'
assert_contains 'Trello mutation/auth failure is global'

assert_not_contains 'create an exception card'
assert_not_contains 'create or reuse exactly one exception card'
