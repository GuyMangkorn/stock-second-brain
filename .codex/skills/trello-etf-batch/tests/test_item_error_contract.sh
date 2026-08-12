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
  assert_contains "$contract_file" 'ERROR + `scope: item`'
  assert_contains "$contract_file" '`research-sub-agent-unavailable` may be item-level'
  assert_contains "$contract_file" 'item-level error'
  assert_contains "$contract_file" 'create or reuse exactly one exception card'
  assert_contains "$contract_file" 'check only the matching `ETF queue` item'
  assert_contains "$contract_file" 'continue to the next eligible ticker'
  assert_contains "$contract_file" 'Trello/tool/auth failures remain global'
  assert_not_contains "$contract_file" 'any `status: ERROR` is always global'
done
