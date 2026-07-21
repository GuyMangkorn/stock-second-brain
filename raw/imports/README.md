# Raw Imports

Store source-backed inputs here before normalization.

Examples:

- `MSFT_latest_results_source.md`
- `AAPL_sec_filing_source_2026-05-17.md`
- `NVDA_earnings_transcript_digest_2026-05-17.md`
- `ASML_investor_presentation_source_2026-05-17.md`
- `ETF_AMEX_VIG_fund_source_2026-07-11.md`

Every source note should include ticker, company, source kind, URLs or local
paths, publication date, reporting scope, currency, units, extracted facts, and
missing/unverified fields.

For ETFs include `entity_key: EXCHANGE:TICKER`, fund/sponsor, benchmark,
passive-status evidence, separate data as-of dates, official methodology and
holdings sources. Performance refreshes may use one compact batch note,
`ETF_performance_sources_YYYY-MM-DD.md`, linked from the per-ETF performance
page.
