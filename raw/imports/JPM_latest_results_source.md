---
type: source-note
ticker: JPM
company: JPMorgan Chase & Co.
source_kind: latest-results
search_date: 2026-07-11
reporting_scope: 1Q26 reported results, FY2025 annual context, and current market check
currency: USD
normalized_output: raw/financials/JPM_fundamentals.md
entity: "[[JPM]]"
tags: [source/latest-results, ticker/JPM]
---

# JPM - Latest Results Source

## Source Map

- [JPMorganChase Quarterly Earnings](https://www.jpmorganchase.com/ir/quarterly-earnings) — official IR index; latest reported period is 1Q26.
- [1Q26 Earnings Press Release](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2026/1st-quarter/a5fd2d13-877b-43b2-8b58-81bad4399c87.pdf) — official release, published 2026-04-14.
- [1Q26 Earnings Supplement](https://www.sec.gov/Archives/edgar/data/19617/000162828026024990/a1q26erfex992supplement.htm) — SEC Form 8-K Exhibit 99.2; quarterly income, balance sheet, segment, capital, and EPS tables.
- [1Q26 10-Q](https://www.sec.gov/Archives/edgar/data/19617/000162828026029344/jpm-20260331.htm) — SEC filing for the period ended 2026-03-31, filed 2026-05-01.
- [1Q26 Earnings Presentation](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2026/1st-quarter/ba305358-f754-4f76-a59d-5278b3bcf99a.pdf) — official outlook and business drivers.
- [1Q26 Earnings Transcript](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2026/1st-quarter/1q26-earnings-transcript.pdf) — official call transcript, 2026-04-14.
- [2025 Annual Report](https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/annualreport-2025.pdf) — official FY2025 annual report, released April 2026.
- [JPMorgan Plans Dividend Increase and New Repurchase Program](https://www.jpmorganchase.com/ir/news/2026/jpmc-dividend-increase-common-share-repurchase) — official capital-return update, 2026-06-24.
- [JPMorgan to Host 2Q26 Earnings Call](https://www.jpmorganchase.com/ir/news/2026/jpmc-to-host-second-quarter-2026-earnings-call) — official schedule; 2Q26 results due 2026-07-14.
- [JPM Historical Price](https://stockanalysis.com/stocks/jpm/history/) — market-data check; $336.47 close on 2026-07-10, checked 2026-07-11.

## Reporting Scope

บริษัทคือ JPMorgan Chase & Co. (NYSE: JPM), รายงานเป็น USD และ fiscal year สิ้นสุดวันที่ 31 ธันวาคม. ผลประกอบการล่าสุดที่ยืนยันได้คือ 1Q26 งวดสิ้นสุด 31 มีนาคม 2026 และประกาศวันที่ 14 เมษายน 2026. 2Q26 ยังไม่รายงาน ณ วันค้นข้อมูล และมีกำหนดประกาศวันที่ 14 กรกฎาคม 2026.

## Currency / Units

ตัวเลข financial statement และ supplemental tables ใช้ USD millions เว้นแต่ระบุเป็น per-share, ratio, percentage, หรือ billions. หุ้นใช้ millions of common shares.

## Extracted Facts

### 1Q26 Firmwide

- Reported total net revenue: $49,836 million; managed revenue: $50,536 million.
- Net interest income: $25,366 million; noninterest revenue: $24,470 million.
- Noninterest expense: $26,850 million; provision for credit losses: $2,507 million.
- Net income: $16,494 million; diluted EPS: $5.94; ROE: 19%; ROTCE: 23%.
- Standardized CET1 ratio: 14.3%; Advanced CET1 ratio: 14.1%; standardized CET1 capital: $291,090 million; total loss-absorbing capacity: $572,078 million.
- Period-end total assets: $4,900,475 million; total loans: $1,503,520 million; total deposits: $2,675,520 million; long-term debt: $448,764 million.
- Common stockholders' equity: $343,993 million; total stockholders' equity: $364,038 million; book value per share: $128.38; tangible book value per share: $108.87; period-end common shares: 2,679.5 million.
- Segment net income: CCB $4,976 million, CIB $9,044 million, AWM $1,775 million, Corporate $699 million.

### Outlook / Capital Allocation

- Management's FY2026 outlook: total NII approximately $103 billion, NII excluding Markets approximately $95 billion, adjusted expense approximately $105 billion, and Card Services net charge-off rate approximately 3.4%; the NII and expense outlooks are market dependent.
- On 2026-06-24, the Board announced an intended quarterly common dividend of $1.65 for 3Q26, subject to customary approval, up from $1.50, and authorized a new $50 billion common share repurchase program effective 2026-07-01.
- Management described lower rates as a drag on Markets NII and said the outlook assumes that pressure is primarily offset in noninterest revenue. Management also highlighted credit-cycle, leveraged lending, geopolitical, and regulatory-capital risks.

### FY2025 Annual Context

- FY2025 total net revenue: $182,447 million; noninterest expense: $95,640 million; pre-provision profit: $86,807 million; provision for credit losses: $14,212 million; net income: $57,048 million.
- FY2025 diluted EPS: $20.02; book value per share: $126.99; tangible book value per share: $107.56; ROE: 17%; ROTCE: 20%.
- FY2025 period-end loans: $1,493,429 million; total assets: $4,424,900 million; deposits: $2,559,320 million; common stockholders' equity: $342,393 million; common shares: 2,696.2 million.

## Missing / Unverified Data

- 2Q26 results, updated guidance, and post-2026-03-31 balance-sheet data are not yet available because the scheduled release is 2026-07-14.
- Current market-data source verifies the 2026-07-10 close at $336.47; intraday or live price is not used.
- A bank-specific valuation is required; a simple corporate FCF DCF is not an appropriate primary model for JPM.

## Handoff For Ingest

Normalize FY2023-FY2025 annual context and 1Q25/2Q25/3Q25/4Q25/1Q26 quarterly trends where periods are compatible. Keep market price outside normalized company facts. Prioritize net income, EPS, book value/TBVPS, ROE/ROTCE, revenue, expenses, credit costs, loans, deposits, capital ratios, segment net income, and FY2026 management outlook. For P6, use the transcript and annual report to assess CCB, CIB, AWM, capital allocation, credit-cycle risk, and regulatory-capital sensitivity. For P11, use a bank-specific P/BV/TBV or excess-return scenario with current price $336.47 as the market check; do not force a FCF DCF.
