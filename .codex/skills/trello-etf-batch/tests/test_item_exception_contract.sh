#!/usr/bin/env bash
set -euo pipefail

skill_file="${1:-.codex/skills/trello-etf-batch/SKILL.md}"

assert_contains() {
  local needle="$1"
  rg -Fq "$needle" "$skill_file" || {
    echo "missing contract: $needle" >&2
    exit 1
  }
}

assert_not_contains() {
  local needle="$1"
  if rg -Fq "$needle" "$skill_file"; then
    echo "unexpected contract: $needle" >&2
    exit 1
  fi
}

assert_contains 'A checked item means the ticker has been handled'
assert_contains 'matching `ETF queue` checklist item checked'
assert_contains 'Move the exception card to the configured `Blocked` list'
assert_contains 'continue to the next unattempted eligible ticker'
assert_contains 'checked item with an open matching exception'
assert_contains 'all items checked and no open exception'
assert_contains 'unfinished normal work remains'
assert_contains 'eligible retryable exception remains'
assert_contains 'only terminal or unconfirmed confirmation exceptions remain'
assert_contains 'leaves the affected checklist item unchanged'
assert_contains 'scheduler continues to inspect only `Ready for AI`'

assert_not_contains 'A checked item means the downstream performance workflow explicitly returned success for that ticker.'
assert_not_contains 'On an explicit downstream item-level failure, leave the item unchecked'
