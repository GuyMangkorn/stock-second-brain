#!/usr/bin/env bash
set -euo pipefail

skill_file="${1:-.codex/skills/trello-etf-backlog/SKILL.md}"

assert_contains() {
  local needle="$1"
  rg -Fq "$needle" "$skill_file" || {
    echo "missing backlog contract: $needle" >&2
    exit 1
  }
}

assert_not_contains() {
  local needle="$1"
  if rg -Fq "$needle" "$skill_file"; then
    echo "unexpected backlog ownership: $needle" >&2
    exit 1
  fi
}

assert_contains 'workflow: trello-etf-backlog'
assert_contains 'Accept legacy workflow: trello-etf-batch only when the card is in Backlog and has input'
assert_contains 'resolve exactly one Markdown table column named Symbol or Ticker'
assert_contains 'normalize each nonempty value to uppercase after trimming whitespace/backticks'
assert_contains 'preserve source order'
assert_contains 'deduplicate by first occurrence'
assert_contains 'parent_ari: <resolved master card ARI>'
assert_contains 'ticker: <CANONICAL_UPPERCASE_TICKER>'
assert_contains 'creation in Ready for AI'
assert_contains 'continuation through remaining missing tickers after an item-specific create error'
assert_contains 'Keep the master in Backlog if any identity is missing'
assert_contains 'When every identity exists, move master to Done and complete it'
assert_contains 'A child in Blocked or Done counts as created'

assert_not_contains 'ETF queue'
assert_not_contains 'exception card'
