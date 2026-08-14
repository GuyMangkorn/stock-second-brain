#!/usr/bin/env bash
set -euo pipefail

skill_file="${1:-.codex/skills/trello-etf-processing/SKILL.md}"

assert_contains() {
  local needle="$1"
  rg -Fq "$needle" "$skill_file" || {
    echo "missing processing contract: $needle" >&2
    exit 1
  }
}

assert_not_contains() {
  local needle="$1"
  if rg -Fq "$needle" "$skill_file"; then
    echo "unexpected processing ownership: $needle" >&2
    exit 1
  fi
}

assert_contains 'one exact child card in Ready for AI'
assert_contains 'workflow: trello-etf-item'
assert_contains 'validate workflow trello-etf-item, parent_ari and ticker'
assert_contains 'match the child identity parent_ari + ticker'
assert_contains 'canonical uppercase ticker'
assert_contains 'title equal to ticker'
assert_contains 'move to In Progress'
assert_contains 'directly reread the same card'
assert_contains '$check-etf-performance <TICKER>'
assert_contains 'mode: lean'
assert_contains 'Forward it to trello-etf-result'
assert_contains 'If the lane does not confirm In Progress, return global claim-state-error and do not invoke downstream'
assert_contains 'never move the child to Done/Blocked directly'
