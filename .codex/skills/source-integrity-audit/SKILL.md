---
name: source-integrity-audit
description: Use when the user asks to lint, audit, verify, clean, or inspect the stock-second-brain vault for unsupported numbers, stale data, conflicts, mismatched charts, missing links, or unresolved source gaps.
---

# Source Integrity Audit

## Modes

- `chat`: default for a scoped read-only check; at most 400 words, no memo.
- `lean`: save when the user asks for a durable audit or fixes are applied.
- `full`: explicit vault-wide audit with a durable memo.

## Checks

- unsupported numbers, stale current claims, and weak provenance
- conflicts and calculations without formulas or denominators
- chart/table/JSON mismatches
- missing source/entity/analysis backlinks and log entries
- orphan or duplicate notes
- unresolved gaps and stale follow-up
- plugin-specific blocks that undermine Markdown portability
- ETF identity collisions and ticker-only links that lose the exchange
- ETF holdings-weight, holdings-as-of, methodology, expense-ratio, AUM,
  price/NAV, premium/discount, distribution, and tracking freshness mismatches

## Workflow

1. Read `index.md` and `log.md`; inventory relevant entities, sources,
   fundamentals, and memos.
2. Inspect the requested scope and compare every selected chart with its owning
   table or JSON.
   For ETFs, compare entity and analysis claims with `raw/funds/`, verify that
   weight calculations use one holdings snapshot, and keep price/NAV dates
   separate from holdings and methodology dates.
3. Search risky numeric/current terms and trace claims to sources.
4. Rank findings `High`, `Medium`, or `Low` and report evidence with paths.
5. If fixes were requested, preserve facts by sourcing, relabeling, or moving
   them to the owning gap section; do not silently delete.
6. For durable output, save
   `wiki/analysis/audits/Source Integrity Audit YYYY-MM-DD.md` and append one
   workflow bullet to `log.md`.

## Severity

| Severity | Meaning |
|---|---|
| High | Unsupported or conflicting number, wrong chart, stale current value, or thesis-changing issue. |
| Medium | Missing link, weak provenance, unclear calculation, or ownership mismatch. |
| Low | Formatting drift, stale follow-up, or minor naming/dashboard issue. |

## Durable Memo

Use scope, findings by severity, chart/table checks, source-gap summary, fixes,
and follow-up. Omit empty severity sections. Keep the final chat handoff under
200 words.

Ask for a narrower scope only when a full pass cannot be completed honestly.
