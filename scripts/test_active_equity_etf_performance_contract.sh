#!/usr/bin/env bash
set -euo pipefail

project_root="/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain"
skill_root="/Users/mangkornkatawong/.codex/skills/check-etf-performance"
skill_file="$skill_root/SKILL.md"
workflow_file="$skill_root/workflow.md"
rules_file="$project_root/AGENTS.md"

assert_contains() {
  local file_path="$1"
  local expected="$2"
  if ! grep -Fq -- "$expected" "$file_path"; then
    echo "missing contract text in $file_path: $expected" >&2
    exit 1
  fi
}

assert_contains "$skill_file" 'active-equity-long-only'
assert_contains "$skill_file" 'passive-index'
assert_contains "$skill_file" 'systematic-active'
assert_contains "$skill_file" 'management_benchmark'
assert_contains "$skill_file" 'Excess CAGR'
assert_contains "$skill_file" 'positive return-only'
assert_contains "$skill_file" 'negative return-only'
assert_contains "$skill_file" 'risk-adjusted evidence not verified'
assert_contains "$skill_file" 'covered-call'
assert_contains "$skill_file" 'reviewer_dispatch: not-attempted-by-design'

assert_contains "$workflow_file" 'Management mode'
assert_contains "$workflow_file" 'Active process subtype'
assert_contains "$workflow_file" 'Management benchmark selection reason'
assert_contains "$workflow_file" 'Risk-adjusted evidence'
assert_contains "$workflow_file" 'scheduled-local'

assert_contains "$rules_file" 'active long-only equity ETFs'
assert_contains "$rules_file" 'official-source-etf-research'

echo 'active equity ETF performance contract: PASS'
