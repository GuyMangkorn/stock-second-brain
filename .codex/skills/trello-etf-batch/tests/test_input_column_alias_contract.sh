#!/usr/bin/env bash
set -euo pipefail

skill_file="${1:-.codex/skills/trello-etf-batch/SKILL.md}"
prompt_file="${2:-.codex/skills/trello-etf-batch/automation-prompt.md}"

assert_contains() {
  local file="$1"
  local needle="$2"
  rg -Fq "$needle" "$file" || {
    echo "missing input-column contract in $file: $needle" >&2
    exit 1
  }
}

assert_not_contains() {
  local file="$1"
  local needle="$2"
  if rg -Fq "$needle" "$file"; then
    echo "stale input-column contract in $file: $needle" >&2
    exit 1
  fi
}

for contract_file in "$skill_file" "$prompt_file"; do
  assert_contains "$contract_file" 'resolve exactly one'
  assert_contains "$contract_file" '`Symbol`'
  assert_contains "$contract_file" '`Ticker`'
  assert_contains "$contract_file" 'case-insensitively'
  assert_contains "$contract_file" 'Both'
  assert_contains "$contract_file" 'aliases are ambiguous'
  assert_contains "$contract_file" 'neither alias'
  assert_contains "$contract_file" 'input-malformed'
  assert_contains "$contract_file" 'before any claim, checklist, or Trello mutation'
  assert_contains "$contract_file" 'trim whitespace and backticks'
  assert_contains "$contract_file" 'normalize each symbol to uppercase'
  assert_contains "$contract_file" 'preserve source order'
  assert_contains "$contract_file" 'deduplicate repeated symbols by keeping'
  assert_not_contains "$contract_file" 'has no `Symbol` column'
  assert_not_contains "$contract_file" 'a `Symbol` column'
done
assert_not_contains "$prompt_file" 'must contain a Markdown table with a `Symbol` column'
