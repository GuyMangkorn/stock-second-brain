#!/usr/bin/env bash
set -euo pipefail

skill_file="${1:-.codex/skills/trello-etf-batch/SKILL.md}"
prompt_file="${2:-.codex/skills/trello-etf-batch/automation-prompt.md}"

assert_contains() {
  local file="$1"
  local needle="$2"
  rg -Fq "$needle" "$file" || {
    echo "missing manager contract in $file: $needle" >&2
    exit 1
  }
}

for contract_file in "$skill_file" "$prompt_file"; do
  assert_contains "$contract_file" 'sequentially'
  assert_contains "$contract_file" 'attempted_this_run'
  assert_contains "$contract_file" 'Ready for AI'
  assert_contains "$contract_file" 'must not overlap manager workers'
done

assert_contains "$skill_file" 'task: backlog|etf-performance'
assert_contains "$skill_file" 'count: <positive base-10 integer>'
assert_contains "$skill_file" 'count must be a positive base-10 integer'
assert_contains "$skill_file" 'Reject missing, duplicate, zero, negative, fractional or nonnumeric values'
assert_contains "$skill_file" 'at most count'
assert_contains "$skill_file" 'For task backlog'
assert_contains "$skill_file" '$trello-etf-backlog'
assert_contains "$skill_file" 'exclusive board-scoped manager lock keyed by the resolved board ARI'
assert_contains "$skill_file" 'manager-overlap'
assert_contains "$skill_file" 'For task etf-performance'
assert_contains "$skill_file" 'trello-etf-processing(child card)'
assert_contains "$skill_file" '→ trello-etf-result(child card, processing result)'
assert_contains "$skill_file" 'Never touch other lanes'

assert_contains "$prompt_file" 'task: etf-performance'
assert_contains "$prompt_file" 'count: 1'
