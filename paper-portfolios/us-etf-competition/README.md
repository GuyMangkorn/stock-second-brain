# US ETF Paper Portfolio Competition

ระบบจำลองพอร์ต ETF สหรัฐฯ แบบ forward-only ระหว่าง `2026-09-02` ถึง
`2026-12-31` ด้วยเงินตั้งต้น `$100,000` โดยใช้
[[ETF Performance Index]] และหน้าใน
`wiki/analysis/performance/` เป็น research context ไม่ใช่แหล่งราคาปัจจุบัน

## Open first

- [[dashboard]] — current derived portfolio state
- [PROMPT.md](PROMPT.md) — English instructions for each scheduled run
- [config.yaml](config.yaml) — competition policy and risk limits
- [ledger/events.jsonl](ledger/events.jsonl) — append-only system of record
- [state/portfolio.json](state/portfolio.json) — derived state; safe to rebuild

## Operating boundary

- `Proposal Phase` is mandatory for the first 10 US trading sessions.
- Alpaca is the planned `Execution Mirror`; the local Portfolio Ledger is
  canonical. The connected Alpaca app currently exposes market-data GET tools
  only in this workspace, so automatic order submission remains blocked until
  an order-capable paper connector is explicitly available and authorized.
- Scheduled runs never enable automatic execution. A separate explicit user
  authorization is required after reconciliation.
- No margin, short sales, options, leveraged/inverse ETFs, or live-money orders.
- Any missing, stale, conflicting, or unavailable mandatory input ends in
  `BLOCKED/NO TRADE` without look-ahead backfilling.

## Commands

Validate and rebuild the derived state and dashboard:

```bash
python3 paper-portfolios/us-etf-competition/scripts/rebuild_portfolio.py --check
python3 paper-portfolios/us-etf-competition/scripts/rebuild_portfolio.py
```

Fetch documented Alpaca evidence after providing paper/data credentials outside
the repository:

```bash
export APCA_API_KEY_ID='...'
export APCA_API_SECRET_KEY='...'
python3 paper-portfolios/us-etf-competition/scripts/fetch_alpaca_data.py clock
```

The fetcher refuses to overwrite evidence and stores request parameters,
timestamps, the response, and a SHA-256 content hash. Never commit credentials.

## Price and market-data sources

The connected Alpaca plugin and the local fetcher use documented `GET` routes;
there is no private-endpoint scraping:

- `GET https://paper-api.alpaca.markets/v2/clock` and `/v2/calendar` for market
  status and US trading sessions.
- `GET https://data.alpaca.markets/v2/stocks/snapshots` for current bid/ask,
  trade and daily-bar context.
- `GET https://data.alpaca.markets/v2/stocks/bars/latest` for the latest minute
  bar and `GET https://data.alpaca.markets/v2/stocks/bars` for historical bars.
  The competition records `adjustment=all`, `currency=USD`, the feed, and the
  exact cutoff; use `sip` when entitled and do not silently mix feeds.
- `GET https://data.alpaca.markets/v1/corporate-actions` for splits and
  distributions. The endpoint is evidence only; the local ledger remains the
  accounting authority because Alpaca paper trading does not simulate every
  corporate action.

For fund facts, holdings, methodology and NAV performance, prefer the ETF issuer
product page/factsheet and SEC filings. Financial Datasets
([prices](https://docs.financialdatasets.ai/api-reference/prices)) and Twelve
Data ([time series](https://twelvedata.com/docs#time-series)) are documented
research-only alternatives; they are not wired into execution or allowed to
replace an unavailable mandatory Alpaca quote without a logged source decision.
Alpha Vantage's [daily endpoint](https://www.alphavantage.co/documentation/)
is another research-only alternative. Current price, NAV, holdings and
performance dates must remain separate in the evidence record.

Official Alpaca references: [historical stock bars](https://docs.alpaca.markets/us/reference/stockbars),
[paper trading](https://docs.alpaca.markets/us/docs/paper-trading),
[market calendar](https://docs.alpaca.markets/us/reference/getcalendar-1), and
[corporate actions](https://docs.alpaca.markets/us/reference/corporateactions-1).

## Disclaimer

This is an educational paper-trading simulation, not personalized investment
advice. It does not guarantee returns and must not invent unavailable evidence.
