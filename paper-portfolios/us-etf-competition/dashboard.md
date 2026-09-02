---
kind: paper-portfolio-dashboard
competition_id: us-etf-competition-2026
phase: proposal
as_of: 2026-09-02T15:33:36Z
portfolio_value: 100000.00
cash: 100000.00
cumulative_return_pct: 0.00
maximum_drawdown_pct: 0.00
---

# US ETF Paper Portfolio Dashboard

> [!info] Proposal Phase
> The local Portfolio Ledger is canonical; browser pages provide read-only market evidence.
> This dashboard is derived by `rebuild_portfolio.py`.

## Snapshot

| Metric | Value |
|---|---:|
| Portfolio value | $100,000.00 |
| Cash | $100,000.00 |
| Cash weight | 100.00% |
| Cumulative return | 0.00% |
| SPY operational benchmark | not started |
| Current drawdown | 0.00% |
| Maximum drawdown | 0.00% |
| Normal turnover | 0.00% |

## Positions

| Ticker | Quantity | Last Price | Market Value | Weight | Realized P&L |
|---|---:|---:|---:|---:|---:|
| — | — | — | — | — | — |

## Daily Equity Curve

No daily-close mark has been recorded yet.

## Latest Runs

```dataview
TABLE analysis_at AS "Analysis at", run_status AS "Status", action_count AS "Actions", portfolio_value AS "Portfolio value"
FROM "paper-portfolios/us-etf-competition/runs"
SORT analysis_at DESC
LIMIT 10
```

## Navigation

- [Mandate and workflow](PROMPT.md)
- [Configuration](config.yaml)
- [Canonical ledger](ledger/events.jsonl)
- [Derived state](state/portfolio.json)
- [Latest verified prices](evidence/market-data/latest-prices.md)
- [Price log](evidence/market-data/price-log.md)
- [[ETF Performance Index]]

This is an educational simulation, not personalized investment advice.
