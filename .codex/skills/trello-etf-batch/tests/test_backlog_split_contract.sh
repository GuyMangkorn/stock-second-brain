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
assert_contains 'header named Symbol or Ticker matched case-insensitively'
assert_contains 'Both aliases or neither alias are `input-malformed`'
assert_contains 'normalize each nonempty value to uppercase after trimming whitespace/backticks'
assert_contains 'preserve source order'
assert_contains 'deduplicate by first occurrence'
assert_contains 'parent_ari + ticker is the idempotency key'
assert_contains 'title equal to ticker'
assert_contains 'parent_ari: <resolved master card ARI>'
assert_contains 'ticker: <CANONICAL_UPPERCASE_TICKER>'
assert_contains 'unarchived matching child in any lane counts as already created'
assert_contains 'creation in Ready for AI'
assert_contains 'continuation through remaining missing tickers after an item-specific create error'
assert_contains 'Keep the master in Backlog if any identity is missing'
assert_contains 'When every identity exists, move master to Done and complete it'
assert_contains 'A child in Blocked or Done counts as created'
assert_contains 'global failure'
assert_contains 'Stop without continuing mutations'
assert_contains 'leave every not-yet-confirmed ticker unclaimed'
assert_contains 'report only confirmed master and child state'
assert_contains 'Do not claim that a failed master move or completion succeeded'

assert_not_contains 'ETF queue'
assert_not_contains 'exception card'
