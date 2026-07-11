# Source Hierarchy

Use this hierarchy when choosing between sources or deciding what to trust.

## Preferred Order

1. SEC filings and official company filings:
   - 10-K, 10-Q, 8-K, 20-F, 6-K
   - annual report
   - quarterly report
   - proxy statement
   - official IR-hosted filing PDFs or HTML pages
2. Earnings transcripts and call materials:
   - official webcast transcript
   - earnings call transcript traceable to the company event
   - prepared remarks
   - Q&A transcript
   - shareholder letter
3. Financial statements and metrics:
   - official financial tables
   - investor presentation tables
   - company data books
   - structured statement data from reliable providers
   - market ratios when source/date are clear
4. News and web research:
   - reputable financial news
   - exchange pages
   - analyst summaries
   - current event context

## ETF Preferred Order

For passive, index-tracking equity ETFs use:

1. Official issuer prospectus, product page, factsheet, and shareholder report
2. Official issuer holdings file and official NAV data
3. Official index-provider methodology, constituent, and rebalance documents
4. Regulator and listing-exchange filings or product pages
5. Reputable market data for dated price, volume, spread, and peer context

Resolve `EXCHANGE:TICKER` before collecting facts. Record separate as-of dates
for holdings, NAV/price, AUM, distributions, performance, and methodology; page
access date does not replace the source's data date.

## Rules

- If primary and secondary sources conflict, prefer the higher-priority source.
- If two primary sources conflict, record the conflict with dates and do not
  silently average.
- If the source gives amounts but not percentages, calculations are allowed only
  when the denominator is shown.
- If a source is only a summary and cannot be traced to an original filing,
  transcript, release, or company page, treat it as context, not a durable fact.
- Every durable number should point back to a source path, URL, or explicit
  calculation.
- For ETF holdings, calculate concentration or overlap only from compatible
  snapshots and preserve disclosed cash or derivative positions.

## When To Stop

Stop and report `ไม่พบข้อมูลที่ยืนยันได้` when:

- no official source can be found
- ticker identity is ambiguous
- period labels, currency, or units are unclear
- source data conflicts and cannot be resolved
- ratio inputs are incomplete
- a segment taxonomy changes enough to make period comparison unsafe
- ETF benchmark, passive equity status, official methodology, or holdings
  cannot be verified
- the ETF is outside the supported passive equity scope
