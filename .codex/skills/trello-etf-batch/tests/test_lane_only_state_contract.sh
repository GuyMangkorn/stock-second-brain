#!/usr/bin/env bash
set -euo pipefail

skill_file="${1:-.codex/skills/trello-etf-batch/SKILL.md}"
prompt_file="${2:-.codex/skills/trello-etf-batch/automation-prompt.md}"

assert_contains() {
  local file="$1"
  local needle="$2"
  rg -Fq "$needle" "$file" || {
    echo "missing lane-only contract in $file: $needle" >&2
    exit 1
  }
}

assert_not_contains() {
  local file="$1"
  local needle="$2"
  if rg -Fq "$needle" "$file"; then
    echo "unexpected parent-status contract in $file: $needle" >&2
    exit 1
  fi
}

for contract_file in "$skill_file" "$prompt_file"; do
  assert_contains "$contract_file" '`Ready for AI` is the only eligible parent lane'
  assert_contains "$contract_file" '`In Progress` means a worker may be active'
  assert_contains "$contract_file" 'Do not read, validate, write, or delete legacy `trello-etf-batch-status` blocks'
  assert_contains "$contract_file" 'move it to `In Progress`'
  assert_contains "$contract_file" 'read the exact parent directly again'
  assert_contains "$contract_file" 'normal items before eligible retries'
  assert_contains "$contract_file" 'move the parent to `Blocked`'
  assert_not_contains "$contract_file" 'claim_token'
  assert_not_contains "$contract_file" 'state: ready'
  assert_not_contains "$contract_file" 'state: running'
  assert_not_contains "$contract_file" 'list/status block'
  assert_not_contains "$contract_file" 'appropriate retry flag'
  assert_not_contains "$contract_file" 'Clear the claim'
  assert_not_contains "$contract_file" 'set the parent status'
done
