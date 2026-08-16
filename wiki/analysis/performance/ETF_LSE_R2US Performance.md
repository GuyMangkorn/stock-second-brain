---
type: etf-performance
instrument_type: ETF
entity_key: LSE:R2US
ticker: SSEUF
listing_ticker: R2US
exchange: LSE
fund: State Street SPDR Russell 2000 U.S. Small Cap UCITS ETF (Acc)
tracked_index: Russell 2000 Index (Net Total Return)
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/SSEUF
  - geography/United-States
---

# SSEUF / R2US Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

SSEUF เป็น OTC alias ของ USD listing `LSE:R2US` ใน State Street SPDR Russell
2000 U.S. Small Cap UCITS ETF (Acc). กองทุนเป็น passive/index-tracking,
accumulating U.S. small-cap equity ETF ที่ติดตาม Russell 2000 Index. Official
2016-2025 Fund Net/NAV return ให้ cumulative `140.61%` และ rounded-input CAGR
`9.18%`; ใน common 2021-2025 window ให้ CAGR `5.70%` ต่ำกว่า S&P 500 Total
Return `14.43%`. Official current NAV/Fund Net YTD คือ `18.69%` ณ 2026-07-31.

## Performance check

- Input ticker: `SSEUF` (OTC alias)
- Canonical entity key: `LSE:R2US` (official USD London Stock Exchange line; ISIN `IE00BJ38QD84`)
- Inception: 2014-06-30
- Asset class / structure: Equity; UCITS; accumulating; optimized replication
- TER: 0.30%
- Metric: issuer `Fund Net` performance, NAV-based and net of fund fees; accumulated income is retained in NAV; USD share class
- Tracked index (issuer benchmark): Russell 2000 Index, Net Total Return (`RU20N30U`)
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR: official cumulative `163.53%` / annualized `10.18%` as of 2026-07-31; raw rolling endpoints are not disclosed
- Since-inception NAV TR: official cumulative `177.36%` / annualized `8.81%` as of 2026-07-31
- Common calendar window: official complete 2016-2025; cumulative `140.61%` / rounded-input CAGR `9.18%`
- 2021-2025 cumulative `31.94%` / CAGR `5.70%`; S&P 500 cached 2021-2025 cumulative `96.17%` / CAGR `14.43%`
- Current official NAV/Fund Net YTD: `18.69%` as of 2026-07-31

| Year | ETF Fund Net / NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 20.97% | 11.96% |
| 2017 | 13.98% | 21.83% |
| 2018 | -11.34% | -4.38% |
| 2019 | 24.98% | 31.49% |
| 2020 | 19.36% | 18.40% |
| 2021 | 14.70% | 28.71% |
| 2022 | -20.78% | -18.11% |
| 2023 | 16.27% | 26.29% |
| 2024 | 11.19% | 25.02% |
| 2025 | 12.32% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ R2US;
annual rows ใช้ cached USD Total Return convention ณ 2025-12-31. ตัวเลข
cumulative/CAGR เป็น rounded-input calculations จาก official Fund Net rows.

## Up years / Down years

- Up years / Down years: 8 / 2 in the complete 2016-2025 window
- Best: 2019, +24.98%
- Least positive: 2024, +11.19%
- Worst: 2022, -20.78%
- Least bad down year: 2018, -11.34%
- Current official NAV/Fund Net YTD: +18.69% as of 2026-07-31

## Risk read-through

R2US มี small-cap, country, liquidity และ USD-share-class currency risk; กองทุน
ใช้ optimized sampling แทนการถือหลักทรัพย์ครบทุกตัว และ State Street รายงาน
standard deviation 3-year `19.67%` กับ tracking error `0.08%` ณ 2026-07-31.
KID ระบุว่ากองทุนเป็น index-tracking/passively managed และอาจใช้ derivatives
เพื่อ efficient portfolio management; ไม่ใช่ derivative-heavy ETF. Official
daily NAV history สำหรับคำนวณ max drawdown และ recovery ยังไม่พบข้อมูลที่ยืนยันได้.

## Sources

- [Official State Street R2US/ZPRR product page](https://www.ssga.com/uk/en_gb/institutional/etfs/state-street-spdr-russell-2000-us-small-cap-ucits-etf-acc-zprr-gy) — identity, listing map, benchmark, official performance, current NAV/YTD and risk metrics.
- [Official State Street July 2026 factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-zprr-gy.pdf) — ISIN, LSE USD ticker R2US, benchmark, TER, share-class structure and performance table.
- [Official State Street KID](https://www.ssga.com/library-content/kids?country=ie&documentType=kid&isin=IE00BJ38QD84&language=en_gb&ticker=zprr-gy) — index-tracking/passive objective, optimization policy and risk disclosures.
- [Google Finance SSEUF alias page](https://www.google.com/finance/beta/quote/SSEUF%3AOTCMKTS) (secondary OTC alias/currency cross-check)
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- [S&P 500 historical reference](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true)
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
