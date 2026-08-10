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

assert_contains 'batch_size: <positive integer>'
assert_contains 'If it is absent, default to `1`'
assert_contains 'The card value is authoritative'
assert_contains 'up to `batch_size` items'
assert_contains 'sequentially'
assert_contains 'while batch capacity remains'
assert_contains 'increment `processed_count` once for the successful item'
assert_contains 'respect the parent card’s `batch_size`'
