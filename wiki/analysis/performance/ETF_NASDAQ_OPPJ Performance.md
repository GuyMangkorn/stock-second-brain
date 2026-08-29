---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:OPPJ
ticker: OPPJ
exchange: Nasdaq
fund: WisdomTree Japan Opportunities Fund
tracked_index: WisdomTree Japan Opportunities Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-29
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return; income reinvested; net of expenses where source-defined; secondary 2025 annual row marked *
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/OPPJ
  - geography/Japan
---

# OPPJ ETF Performance

> [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

OPPJ เป็น passive/index-tracking Japan equity ETF ของ WisdomTree ที่จดทะเบียน
บน Nasdaq และติดตาม WisdomTree Japan Opportunities Index. กองมีการเปลี่ยน
objective/index จาก DXJS / Japan Hedged SmallCap เป็น OPPJ / Japan Opportunities
มีผล 1 ก.ค. 2025 ดังนั้นประวัติระยะยาวเป็น spliced strategy record ไม่ใช่
track record ของกลยุทธ์ปัจจุบันล้วน ๆ.

Official WisdomTree month-end data ณ 31 ก.ค. 2026 ให้ NAV Total Return YTD
`24.40%`, rolling 10-year average annual return `17.00%`, 1-year `56.11%`,
3-year `31.08%` และ 5-year `24.91%`. Current NAV อยู่ที่ `US$57.915` ณ
28 ส.ค. 2026 และ closing market price `US$57.750` ณ 27 ส.ค. 2026. กองมี
expense ratio `0.58%`, total assets `US$283.78M` และ aggregate hedge ratio
`97.24%` ณ 28 ส.ค. 2026.

## Performance check

- `entity_key: NASDAQ:OPPJ`; Nasdaq listing; inception `2013-06-28`; CUSIP `97717W521`.
- Metric: `NAV Total Return` รวมเงินปันผล/การกระจายที่ reinvested และหัก fund expenses ตามนิยามของ issuer; market-price return แยกต่างหาก.
- Classification: `passive-index-tracking`; prospectus ระบุ representative sampling และลงทุนอย่างน้อย 80% ใน index constituents หรือสิ่งที่มีลักษณะทางเศรษฐกิจใกล้เคียงกัน; fund เป็น non-diversified.
- Issuer benchmark: `WisdomTree Japan Opportunities Index` (product/factsheet related symbol `WTJOPN`; index page symbol `WTJOP`); common reference คือ `S&P 500 Total Return` USD, dividends reinvested, ไม่ใช่ tracked index ของ OPPJ.
- Current strategy: index ใช้ 4 buckets ได้แก่ Berkshire Hathaway strategic holdings, total shareholder yield, corporate-governance improvers และ thematic opportunities; dynamic JPY/USD hedge อยู่ในช่วง 0-100%.
- Official rolling 10-year window: `2016-07-31` ถึง `2026-07-31`; issuer รายงาน average annual NAV TR `17.00%`. Raw endpoint ไม่ได้เปิดเผยใน reviewed capture; shown calculation จาก CAGR คือ normalized `100.00 → 480.68` หรือ implied cumulative `380.68%`, ไม่ใช่ sourced NAV/TR index level.

Annual rows ปี 2016-2024 มาจาก [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011309/oppj73125497k.htm); ปี 2025 เป็น secondary standardized NAV total return จาก [Schwab OPPJ report](https://www.schwab.wallst.com/schwab/Prospect/research/etfs/reports/reportRetrieve.asp?reportType=etfrc&symbol=OPPJ) และติด `*`:

| Year | OPPJ NAV TR | S&P 500 TR (USD; common ref.) |
|---|---:|---:|
| 2016 | 6.88% | 11.96% |
| 2017 | 29.46% | 21.83% |
| 2018 | -17.82% | -4.38% |
| 2019 | 18.33% | 31.49% |
| 2020 | -4.64% | 18.40% |
| 2021 | 11.98% | 28.71% |
| 2022 | 6.84% | -18.11% |
| 2023 | 36.69% | 26.29% |
| 2024 | 20.68% | 25.02% |
| 2025* | 36.20% | 17.88% |

### Calculations and current standardized return

- 2016-2025 annual rows: cumulative `244.89%`, rounded-input CAGR `13.18%`, population standard deviation `16.66%`, positive/negative years `8 / 2`.
- 2021-2025 annual rows: cumulative `68.80%`, rounded-input CAGR `21.87%`, population standard deviation `12.23%`, positive/negative years `5 / 0`.
- Cached S&P 500 TR common reference: 2016-2025 cumulative `298.33%` / CAGR `14.82%`; 2021-2025 cumulative `96.17%` / CAGR `14.43%`. This is a USD reference only and is not manager-skill or alpha evidence.
- Latest official July 2026 standardized NAV TR: YTD `24.40%`, 1-year `56.11%`, 3-year annualised `31.08%`, 5-year annualised `24.91%`, 10-year annualised `17.00%`, since inception annualised `15.24%`.
- July 2026 underlying-index versus NAV observations were `24.86%` vs `24.40%` YTD, `57.24%` vs `56.11%` 1-year, `31.76%` vs `31.08%` 3-year, `25.54%` vs `24.91%` 5-year and `17.66%` vs `17.00%` 10-year; the gaps are passive tracking/fee observations, not alpha.

**Up years / Down years**

- Best: 2023, **+36.69%**; worst: 2018, **-17.82%**.
- 2026 YTD: **+24.40% NAV TR**, as of 31 ก.ค. 2026.
- The annual 2025 row is secondary and the 2021-2025 window crosses the June/July 2025 objective and index change; do not read it as a continuous five-year record of the current strategy.

## Current fund snapshot

| Field | Value | As of |
|---|---:|---|
| NAV | US$57.915 | 2026-08-28 |
| Closing market price | US$57.750 | 2026-08-27 |
| Premium/discount to NAV | -0.09% | 2026-08-28 |
| Total assets | US$283.783M | 2026-08-28 |
| Shares outstanding | 4.90M | 2026-08-28 |
| 30-day average volume | 37,662 shares | 2026-08-27 |
| Median bid/ask spread | 0.49% | 2026-08-27 |
| Net expense ratio | 0.58% | 2026-08-28 |
| Distribution yield | 2.35% | 2026-08-27 |
| SEC 30-day yield | 1.77% | 2026-08-27 |
| Aggregate hedge ratio | 97.24% | 2026-08-28 |

Portfolio characteristics of the underlying holdings as of 27 ส.ค. 2026 were
P/E `14.17x`, estimated P/E `13.03x`, P/B `1.63x`, dividend yield `2.17%`, gross
buyback yield `1.75%` and net buyback yield `1.63%`. These are holdings metrics,
not valuation multiples of the fund's NAV.

Country exposure is Japan `100.00%`. Current top holdings include Sumitomo
`8.32%`, Mitsubishi `7.47%`, Marubeni `7.19%`, Mitsui `6.83%`, Itochu `5.90%`,
Kioxia `4.12%`, Tokio Marine `3.92%`, Panasonic `2.52%`, Tokyo Electron `2.32%`
and Hanwa `2.09%`; the top ten sum to approximately `50.68%` from the issuer's
rounded weights. Sector exposure is Industrials `48.27%`, Information Technology
`13.99%`, Materials `11.31%`, Financials `11.12%`, Consumer Discretionary `7.55%`,
Health Care `3.12%`, Consumer Staples `2.28%`, Communication Services `1.58%`
and Real Estate `0.78%`.

## Risk read-through

OPPJ ให้ Japan concentration และ sector concentration สูง โดย Industrials คิดเป็น
เกือบครึ่งของพอร์ตและกองเป็น non-diversified. Dynamic hedge ratio ช่วยลดผลของ
JPY/USD แต่ hedge ใช้ currency forwards/futures และไม่จำเป็นต้อง offset ค่าเงินได้
สมบูรณ์; hedge ratio ล่าสุด `97.24%` จึงเป็น snapshot ไม่ใช่ policy คงที่. ความเสี่ยง
หลักยังรวมถึง Japan macro/policy, trade/export cycle, geopolitical events,
derivatives/counterparty, market-price/NAV discount และ liquidity.

Secondary adjusted-market-price series จาก [PortfoliosLab OPPJ](https://portfolioslab.com/symbol/OPPJ) ระบุ maximum drawdown `-39.30%` จาก 9 ม.ค. 2018 ถึง 16 มี.ค. 2020 และ recovery 15 มี.ค. 2021; นี่เป็น proxy ไม่ใช่ official NAV drawdown. Official daily NAV series ที่เพียงพอสำหรับการ reproduce drawdown/recovery ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Source reconciliation and follow-up

The prior June 2026 official quarter-end capture reported NAV TR YTD `24.67%`
and rolling 10-year `17.89%`; the later WisdomTree July month-end capture reports
`24.40%` and `17.00%`. These are separate standardized as-of windows and are not
arithmetically mixed with the current August quote/hedge snapshot. The current
product page also retains legacy symbols `DXJS.NV` / `DXJS.SO`; they are issuer
data identifiers and do not change the canonical `NASDAQ:OPPJ` identity.

Follow-up:

- Replace the secondary 2025 calendar row when an official calendar-year NAV row is exposed.
- Track the post-2025 OPPJ strategy separately once it has a complete multi-year record.
- Locate an official daily NAV/TR history to replace the adjusted-price drawdown proxy.

## Sources

- [WisdomTree OPPJ product page](https://www.wisdomtree.com/us/products/equity/oppj) — official identity, strategy, current NAV/price, July standardized returns, holdings, sectors, portfolio characteristics, hedge ratio and distributions.
- [WisdomTree OPPJ factsheet](https://www.wisdomtree.com/us/media/wisdomtree-factsheet-oppj) — official June 2026 performance cross-check, NASDAQ listing, fee, fund size and strategy-change disclosure.
- [SEC OPPJ summary prospectus](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011309/oppj73125497k.htm) — passive management, 80% policy, index methodology, dynamic hedge and principal risks; official annual rows through 2024.
- [WisdomTree Japan Opportunities Index](https://www.wisdomtree.com/us/indexes/WTJOP) — current index design, components, industry/country profile and definitions.
- [Schwab OPPJ report](https://www.schwab.wallst.com/Prospect/research/etfs/reports/reportRetrieve.asp?reportType=etfrc&symbol=OPPJ) — secondary 2025 annual row and current July standardized cross-check.
- [PortfoliosLab OPPJ](https://portfolioslab.com/symbol/OPPJ) — secondary adjusted-price drawdown/recovery proxy.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
