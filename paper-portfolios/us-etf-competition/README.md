# US ETF Paper Portfolio Competition

ระบบจำลองพอร์ต ETF สหรัฐฯ แบบ forward-only ระหว่าง `2026-09-02` ถึง
`2026-12-31` ด้วยเงินตั้งต้น `$100,000` โดยใช้
[[ETF Performance Index]] และหน้าใน
`wiki/analysis/performance/` เป็น research context ไม่ใช่แหล่งราคาปัจจุบัน

## Open first

- [[dashboard]] — current derived portfolio state
- [PROMPT.md](PROMPT.md) — English instructions for each portfolio run
- [config.yaml](config.yaml) — competition policy and risk limits
- [ledger/events.jsonl](ledger/events.jsonl) — append-only system of record
- [state/portfolio.json](state/portfolio.json) — derived state; safe to rebuild

## Operating boundary

- `Proposal Phase` is mandatory for the first 10 US trading sessions.
- Browser/direct-web pages are read-only market evidence; the local Portfolio
  Ledger is canonical. Browser search is used for discovery, while quotes,
  calendars, NAVs, filings, and fund facts must be read from the opened direct
  page with explicit as-of/retrieval timestamps.
- Scheduled runs never enable automatic execution. A separate explicit user
  authorization is required after reconciliation.
- Manual runs are evaluated at the time they are invoked, regardless of the
  default 15:00 ET automation time. The run may record `BUY`, `REDUCE`, `SELL`,
  or `HOLD`; it should make no change when the existing portfolio is still the
  best supported decision.
- Every run records an `IN`/`OUT`/`HOLD` change log in the run note and ledger.
- No margin, short sales, options, leveraged/inverse ETFs, or live-money orders.
- Any missing, stale, conflicting, or unavailable mandatory input ends in
  `BLOCKED/NO TRADE` without look-ahead backfilling.

## Commands

Validate and rebuild the derived state and dashboard:

```bash
python3 paper-portfolios/us-etf-competition/scripts/rebuild_portfolio.py --check
python3 paper-portfolios/us-etf-competition/scripts/rebuild_portfolio.py
```

For a review, use the browser to search for the relevant official or reputable
source, open the direct result, and save an immutable evidence envelope under
`evidence/market-data/YYYY-MM-DD/`. Record the query, direct URL, page title,
visible values/text, source as-of time, retrieval time, and SHA-256 content hash.
Search snippets alone are never sufficient. Do not enter credentials or upload
portfolio files into a website.

Before searching, read [`latest-prices.md`](evidence/market-data/latest-prices.md)
and the tail of [`price-log.md`](evidence/market-data/price-log.md). Use those
observations for initial screening, then refresh only holdings, SPY, and
decision-relevant candidates. Every verified refresh gets one append-only log
row and one updated latest-cache row; stale cache values are not final quotes.

## Price and market-data sources

Use these browser sources in priority order:

- Official NYSE/Nasdaq or regulator pages for US trading dates, holidays, and
  early closes.
- ETF issuer product pages, fact sheets, holdings, NAV/performance pages, and
  SEC filings for fund identity, methodology, holdings, costs, and distributions.
- Direct reputable market-data pages for current quotes, bid/ask, volume, and
  historical prices when the page shows a timestamp or session date.

Keep current price, NAV, holdings, methodology, fund facts, and performance
dates separate in each evidence record. If a direct page cannot be verified or
the sources conflict, log `BLOCKED/NO TRADE` rather than backfilling with an
unrelated data feed.

## Disclaimer

This is an educational paper-trading simulation, not personalized investment
advice. It does not guarantee returns and must not invent unavailable evidence.
