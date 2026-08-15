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
assert_contains 'caller: trello-etf-processing'
assert_contains 'handoff: trello_handoff'
assert_contains 'return exactly one structured `trello_handoff` block'
assert_contains 'never infer success or failure from prose, links,'
assert_contains 'file existence'
assert_contains 'Forward it to trello-etf-result exactly once'
assert_contains 'invalid-envelope global-stop'
assert_contains 'sentinel'
assert_contains 'durable_write: unknown'
assert_contains 'exhausted: false'
assert_contains 'confirmation: none'
assert_contains 'code: unknown-result'
assert_contains 'Forward it to trello-etf-result'
assert_contains 'If the lane does not confirm In Progress, return global claim-state-error and do not invoke downstream'
assert_contains 'never'
assert_contains 'move the child to Done/Blocked directly'
