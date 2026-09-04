# US ETF Paper Portfolio Competition

ระบบจำลองพอร์ต ETF สหรัฐฯ แบบ forward-only และ open-ended ด้วยเงินตั้งต้น
`$100,000` เพื่อดูผลลัพธ์ระยะ 1 ปีหรือนานกว่านั้น โดยใช้
[[ETF Performance Index]] และหน้าใน
`wiki/analysis/performance/` เป็น research context ไม่ใช่แหล่งราคาปัจจุบัน

## Open first

- [[dashboard]] — current derived portfolio state
- [PROMPT.md](PROMPT.md) — English instructions for each portfolio run
- [config.yaml](config.yaml) — competition policy and risk limits
- [ledger/events.jsonl](ledger/events.jsonl) — append-only system of record
- [state/portfolio.json](state/portfolio.json) — derived state; safe to rebuild

## Operating boundary

- `Proposal Phase` is mandatory for the first 10 completed US trading sessions
  after the first valid daily mark is recorded.
- The portfolio has no competition end date. It continues until the user
  explicitly asks to stop or close it; no date-based liquidation is performed.
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
- The decision quote freshness gate is one US trading day, using
  `freshness_gate.decision_quote_trading_sessions: 1`; it is not a five-minute
  or rolling clock-hours gate. Same-day quotes remain preferable when available.
- Performance and fund-facts freshness is three calendar months, represented by
  the operational `freshness_gate.performance_fund_facts_days: 90` setting. The
  decision-price quote gate above remains unchanged.
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

Record one captured market-data batch and update both compact projections:

```bash
python3 paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py \
  --root paper-portfolios/us-etf-competition --batch /path/to/captured-batch.json
```

If the screen cache is missing or invalid, rebuild it once from the complete
price log in recovery mode:

```bash
python3 paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py \
  --root paper-portfolios/us-etf-competition --bootstrap-cache
```

For a review, use the browser to search for the relevant official or reputable
source, open the direct result, and capture the clock, calendar, and relevant
market-data pages in one immutable batch under `evidence/market-data/batches/`.
Record the query, direct URL, page title, visible values/text, source as-of time,
retrieval time, and SHA-256 content hash. Search snippets alone are never
sufficient. Do not enter credentials or upload portfolio files into a website.
The dated directories under `evidence/market-data/YYYY-MM-DD/` are legacy
evidence and remain read-only; do not create new per-ticker JSON files there.

Before searching, read the screen cache in
[`latest-prices.md`](evidence/market-data/latest-prices.md) and the tail of
[`price-log.md`](evidence/market-data/price-log.md). Use those observations for
initial screening, then refresh only holdings, SPY, and decision-relevant
candidates. The recorder writes one append-only log row per verified
observation and one updated cache row per ticker; stale cache values are not
final quotes.

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
