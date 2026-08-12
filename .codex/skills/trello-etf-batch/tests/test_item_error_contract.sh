#!/usr/bin/env bash
set -euo pipefail

skill_file="${1:-.codex/skills/trello-etf-batch/SKILL.md}"
prompt_file="${2:-.codex/skills/trello-etf-batch/automation-prompt.md}"

assert_contains() {
  local file="$1"
  local needle="$2"
  rg -Fq "$needle" "$file" || {
    echo "missing contract in $file: $needle" >&2
    exit 1
  }
}

assert_not_contains() {
  local file="$1"
  local needle="$2"
  if rg -Fq "$needle" "$file"; then
    echo "unexpected contract in $file: $needle" >&2
    exit 1
  fi
}

for contract_file in "$skill_file" "$prompt_file"; do
  assert_contains "$contract_file" 'item-level error is `status: ERROR` with `scope: item`'
  assert_contains "$contract_file" 'known ticker-scoped downstream `ERROR`'
  assert_contains "$contract_file" 'reported `scope: global`'
  assert_contains "$contract_file" 'scope: item` or `scope: global`'
  assert_contains "$contract_file" '`research-sub-agent-unavailable` may be item-level'
  assert_contains "$contract_file" 'item-level error'
  assert_contains "$contract_file" 'create or reuse exactly one exception card'
  assert_contains "$contract_file" 'check only the matching `ETF queue` item'
  assert_contains "$contract_file" 'continue to the next eligible ticker'
  assert_contains "$contract_file" 'Trello/tool/auth failures remain global'
  assert_not_contains "$contract_file" 'any `status: ERROR` is always global'
done

assert_contains "$prompt_file" 'Configuration, input, target, board, list, and checklist failures before moving the parent to In Progress return without any Trello mutation'
assert_contains "$prompt_file" 'If the move succeeds but the direct reread does not confirm In Progress, stop without any further Trello mutation or downstream call'
assert_contains "$prompt_file" 'Only a global failure after this invocation moved the parent to `In Progress` and the direct re-read confirmed that lane may move the parent to `Blocked`'
assert_contains "$prompt_file" 'status: PASS|WARNING|CHANGES_REQUIRED|BLOCKED|ERROR'
assert_contains "$prompt_file" 'scope: item|global|unknown'
assert_contains "$prompt_file" 'durable_write: completed|not_completed|unknown'
assert_contains "$prompt_file" 'exhausted: true|false'
assert_contains "$prompt_file" 'confirmation: none|required|confirmed'
assert_contains "$prompt_file" 'code: <stable code>'
assert_contains "$prompt_file" 'reason: <concise reason>'
assert_contains "$prompt_file" 'All fields are required. Missing, unknown, or contradictory fields are global'
assert_contains "$prompt_file" 'An accepted `WARNING` requires `status: WARNING`, `scope: item`, `durable_write: not_completed`, `exhausted: false`, `confirmation: required`, `code: review-warning|confirmation-required`, and `reason: <concise reason>`'
assert_contains "$prompt_file" 'An accepted `CHANGES_REQUIRED` or `BLOCKED` requires `status: CHANGES_REQUIRED|BLOCKED`, `scope: item`, `durable_write: not_completed`, `exhausted: true`, `confirmation: none`, `code: unsupported-etf-type|item-pre-save-non-pass|item-hard-data-gap|research-sub-agent-unavailable|item-downstream-error`, and `reason: <concise reason>`'
assert_contains "$prompt_file" 'An accepted item-level `ERROR` requires `status: ERROR`'
assert_contains "$prompt_file" '`code: research-sub-agent-unavailable|item-downstream-error`'
assert_contains "$prompt_file" '`reason: <concise reason>`'
assert_contains "$prompt_file" 'Before its downstream call, move each selected retry exception card to the configured active list; if that move or update fails, treat it as a global failure and stop the run'
assert_contains "$prompt_file" 'not an exactly-once distributed lock'
