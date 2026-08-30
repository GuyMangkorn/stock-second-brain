---
type: etf-performance
instrument_type: ETF
entity_key: LSE:TDIV
ticker: TDIV
input_ticker: TKCPF
exchange: London Stock Exchange
fund: VanEck Morningstar Developed Markets Dividend Leaders UCITS ETF
tracked_index: Morningstar Developed Markets Large Cap Dividend Leaders Screened Select Index (Gross Total Return)
benchmark: S&P 500 Total Return
management_mode: passive-index
implementation: physical-full-replication
track_record: established
risk_evidence: not-verified
updated: 2026-08-30
performance_as_of: 2025-12-31 (calendar) / 2026-07-31 (standardized) / 2026-08-28 (current)
calendar_years_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-08-28
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28 / 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: EUR NAV Total Return; distributions reinvested under issuer gross-reinvestment convention; net of fees
return_currency: EUR
tags:
  - analysis/etf-performance
  - ticker/TKCPF
  - ticker/TDIV
  - geography/International
---

# TKCPF / TDIV ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

`TKCPF` เป็น OTC input alias ของกองทุน VanEck Morningstar Developed Markets
Dividend Leaders UCITS ETF และถูก resolve เป็น official USD listing `LSE:TDIV`,
ISIN `NL0011683594`; ไม่ใช่ `Nasdaq:TDIV` ซึ่งเป็น First Trust คนละกองทุน.
Issuer performance เป็น EUR NAV Total Return ของ share class/กองทุนเดียวกัน
โดยไม่อนุมาน FX conversion ไปยัง USD listing. Official current page รายงาน
NAV TR YTD `+18.12%` ณ 2026-08-28 และ factsheet ณ 2026-07-31 รายงาน rolling
10-year average annual NAV TR `+12.38%` เทียบ index `+13.04%`. Complete
calendar rows ที่ยืนยันได้คือ 2017-2025: fund cumulative `+147.44%` และ
rounded-input CAGR `+10.59%` เทียบ tracked index `+159.85%` / `+11.19%`.

## Fund and measurement

- `entity_key: LSE:TDIV`; official USD line on London Stock Exchange; fund inception `2016-05-23`; domicile Netherlands; base/return currency EUR.
- กองทุนเป็น passive, physical full replication, UCITS และใช้ `Morningstar Developed Markets Large Cap Dividend Leaders Screened Select Index (Gross Total Return)` เป็น tracked index. Index มีหุ้น 100 ตัวและใช้ total dividend weighting; fund distributes income quarterly.
- TER `0.38%`; official product page reports net assets approximately `€9.5B` and NAV `€55.42` ณ 2026-08-28. July factsheet reports net assets `€8,981.6M`, shares `163.3M`, holdings `100`, P/E `13.85`, P/B `1.79`, and 12-month yield `3.00%` ณ 2026-07-31.
- Standardized factsheet ณ 2026-07-31: fund/index NAV TR คือ 1M `6.10%`/`6.21%`, 3M `5.97%`/`6.11%`, YTD `17.22%`/`17.83%`, 1Y `32.19%`/`33.22%`, 3Y `20.95%`/`21.78%`, 5Y `18.93%`/`19.69%`, 10Y `12.38%`/`13.04%`, และตั้งแต่ inception `12.74%`/`13.42%`.
- Return series ใช้ issuer Dutch gross-reinvestment convention; นักลงทุนจริงอาจได้ผลต่างจากภาษี, trading costs, FX และ listing currency. Current YTD จาก product page กับ standardized July YTD เป็นคนละ as-of window และไม่ถูก merge.

## Annual performance

Issuer factsheet เว้นแถว 2016 ไว้เพราะกองทุนเริ่มในเดือนพฤษภาคม; จึงไม่เติมค่า
หรือ annualize ปี partial และใช้เฉพาะ complete calendar years 2017-2025.

| Calendar year | TDIV fund NAV TR | Morningstar index gross TR | S&P 500 Total Return |
|---|---:|---:|---:|
| 2017 | +3.30% | +3.80% | +21.83% |
| 2018 | -7.50% | -7.10% | -4.38% |
| 2019 | +22.50% | +23.20% | +31.49% |
| 2020 | -10.40% | -10.00% | +18.40% |
| 2021 | +26.90% | +27.20% | +28.71% |
| 2022 | +15.80% | +16.60% | -18.11% |
| 2023 | +11.80% | +12.60% | +26.29% |
| 2024 | +16.00% | +16.70% | +25.02% |
| 2025 | +23.80% | +24.70% | +17.88% |

## Up years / Down years

- 2017-2025: `7 / 2` up/down years; best year 2021 `+26.90%`; worst year 2020 `-10.40%`.
- Fund compound `1.033 × 0.925 × 1.225 × 0.896 × 1.269 × 1.158 × 1.118 × 1.160 × 1.238 = 2.474439`, or cumulative `+147.44%`; rounded-input CAGR is `+10.59%`.
- Tracked-index compound is `2.598529`, or cumulative `+159.85%`; rounded-input CAGR is `+11.19%`. Fund-minus-index CAGR is approximately `-0.60 pp`, with `0/9` years beating the tracked index. This is a tracking observation, not alpha.
- Common 2021-2025 window: fund cumulative `+135.93%` / rounded-input CAGR `+18.73%`; index cumulative `+143.03%` / CAGR `+19.44%`; cached S&P 500 TR cumulative `+96.17%` / CAGR `+14.43%`. S&P 500 is a common reference only and is not the strategy benchmark.
- Issuer's rolling 10-year annualized field `+12.38%` is kept separate from the 2017-2025 calendar calculation because it is a different rolling window and as-of date.

## Risk read-through

กองทุนมี developed-market country, FX, equity, dividend-factor, financials และ
valuation sensitivity; dividend selection และ quarterly rebalancing อาจทำให้
ผลตอบแทนต่างจาก broad-market developed-equity ETFs. Official risk evidence
สำหรับ daily NAV maximum drawdown, recovery date/duration และ risk-adjusted
persistence ยัง `ไม่พบข้อมูลที่ยืนยันได้`. จึงไม่ใช้ OTC price series หรือ USD
listing price แทน official EUR NAV TR และไม่สร้าง premium/discount claim.

## Source-quality notes

- Official VanEck factsheet and product page are canonical for identity,
  performance, current NAV/YTD, fund facts, and index definition. The 2016
  partial-year blank is preserved; no missing annual return is inferred.
- `TKCPF` is retained as the input ticker for Trello traceability, while
  `LSE:TDIV` is the canonical identity. The official fund performance is EUR
  based even though the selected London listing is USD; no FX conversion is
  calculated.
- No official daily NAV series sufficient for maximum drawdown or recovery was
  verified. S&P 500 TR rows are the cached common USD reference and are not
  evidence of management skill.

## Sources

- [VanEck UK product page](https://www.vaneck.com/uk/en/investments/dividend-etf/index) — current official NAV, YTD return, assets, TER, inception and passive/index-tracking classification through 2026-08-28.
- [VanEck Morningstar Developed Markets Dividend Leaders UCITS ETF factsheet](https://www.vaneck.com/uk/en/library/fact-sheets/tdiv-fact-sheet.pdf) — ISIN, listings, fund/index standardized returns, 2017-2025 annual rows, fund facts, distribution and risk disclosures.
- [VanEck KIID](https://www.vaneck.com/globalassets/home/ucits/documents/kids/KIID_VanEck-Morningstar-Developed-Markets-Dividend-Leaders-UCITS-ETF_en-UK.pdf) — passive objective, index construction, physical replication, distribution policy, TER and risk indicator.
- [OTC TKCPF identity cross-check](https://stockanalysis.com/quote/otc/TKCPF/) — secondary alias/name cross-check only; not used for NAV return calculations.
- S&P 500 Total Return 2017-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
