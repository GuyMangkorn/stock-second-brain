---
type: etf-performance
instrument_type: ETF
entity_key: LSE:XMED
input_ticker: DXMEF
ticker: XMED
exchange: London Stock Exchange
fund: Xtrackers MSCI Europe UCITS ETF 1C
tracked_index: MSCI Total Return Net Europe Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-29
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-08-26
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-26
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return; income reinvested; net of expenses where source-defined; secondary annual/current proxy marked *
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/XMED
  - ticker/DXMEF
  - geography/Europe
---

# DXMEF / XMED ETF Performance

> [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

DXMEF เป็น OTC alias ของ Xtrackers MSCI Europe UCITS ETF 1C, ISIN
LU0274209237. DWS ยืนยัน official USD line คือ `LSE:XMED` และ share-class/fund
currency เป็น USD; กองทุนเป็น passive physical replication, accumulating,
all-in fee 0.12% และติดตาม MSCI Total Return Net Europe Index.

Official DWS factsheet ณ 2026-07-31 ให้ NAV USD 140.30, total fund assets
USD 9.93B และ 397 index constituents แต่ส่งต่อ annual performance ไปที่
online page โดยไม่แสดงตัวเลขใน factsheet ที่ตรวจ. จึงใช้ secondary Morningstar
USD total-return proxy แบบติด `*` สำหรับปี 2021-2025: cumulative 65.25%,
rounded-input CAGR 10.57%, annual-return standard deviation 17.17% และ up/down
years 4/1. Latest Morningstar USD snapshot ณ 2026-08-26 ให้ NAV/closing price
`US$141.55`, rolling 10-year `9.94%*` และ YTD `12.58%*`; ทั้งหมดไม่ถูกยกระดับ
เป็น official issuer performance fields.

## Performance check

- `entity_key: LSE:XMED`; input ticker `DXMEF`; canonical exchange London Stock Exchange, USD line; ISIN `LU0274209237`; share-class/fund launch 2007-01-10; domicile Luxembourg.
- Metric: secondary USD total-return proxy with income reinvested where the provider's growth series applies; official DWS factsheet's annual NAV rows were not exposed in the reviewed capture. Market-price return is not mixed into the table.
- Classification: `passive-index-tracking`; direct physical replication; accumulating share class; DWS all-in fee `0.12% p.a.`.
- Issuer benchmark: `MSCI Total Return Net Europe Index`, MSCI, USD base currency, 397 constituents, large-/mid-cap developed Europe and approximately 85% free-float coverage. Common reference is `S&P 500 Total Return` in USD, not the issuer benchmark.
- Official DWS NAV is `US$140.30` as of 2026-07-31; Morningstar's separate USD NAV/closing-price snapshot is `US$141.55` as of 2026-08-26. The dates and source roles differ and the values are not merged.

| Year | XMED total-return proxy* (USD; not issuer annual NAV table) | MSCI Total Return Net Europe | S&P 500 TR (USD; common ref.) |
|---|---:|---:|---:|
| 2021 | 16.58%* | not disclosed | 28.71% |
| 2022 | -14.85%* | not disclosed | -18.11% |
| 2023 | 20.18%* | not disclosed | 26.29% |
| 2024 | 2.02%* | not disclosed | 25.02% |
| 2025 | 35.77%* | not disclosed | 17.88% |

Secondary XMED rows compound to `65.25%*` / rounded-input CAGR `10.57%*` for
2021-2025. The cached S&P 500 TR compounds to `96.17%` / `14.43%` over the
same years. This is a USD common reference only; no manager-skill or alpha
claim is made.

**Up years / Down years**

- Up years / Down years: `4 / 1` in the secondary 2021-2025 rows.
- Best: 2025, `+35.77%*`; worst: 2022, `-14.85%*`.
- Least positive year: 2024, `+2.02%*`; population standard deviation: `17.17%*`.
- Morningstar rolling 10-year return: `9.94%*` as of 2026-08-26; DWS official rolling field was not disclosed in the reviewed factsheet.
- Morningstar current YTD: `+12.58%*` as of 2026-08-26; DWS official July factsheet did not expose a separate YTD figure.
- Morningstar trailing USD fields as of 2026-08-26: 1-year `21.70%*`, 3-year annualised `19.36%*`, and 5-year annualised `10.05%*`; these remain secondary observations.

## Source reconciliation and risk read-through

The DWS factsheet is the source of truth for identity, official listing, USD
currency, benchmark, fee, NAV, fund assets, replication, accumulation and
index/risk description. Morningstar's USD series is retained only to fill the
issuer annual/current performance gap. ETFdoc/Quantalys rows are labeled
Euro-performance and Stuttgarter's annual rows conflict with the Morningstar
USD series; neither is used in the calculation because the canonical share
class and XMED listing are USD.

Main risks are European country/sector and equity-market exposure, political
and economic events, currency movements, market-price/NAV timing and the
single-region concentration. Official DWS holdings and index data show a broad
large-/mid-cap Europe portfolio. As a supplemental secondary profile, Morningstar
reported Eurozone `51.06%`, Europe ex Euro `24.36%`, United Kingdom `21.63%`,
Financial Services `25.37%`, Industrials `19.52%`, and Healthcare `13.12%` as of
2026-07-31. Daily NAV maximum drawdown and recovery date were not disclosed in
the reviewed official sources.

## Sources

- [DWS Xtrackers MSCI Europe UCITS ETF 1C factsheet](https://etf.dws.com/download/asset/9851b59e-0dd9-4624-9a83-9f580e0a60a3) — official July 2026 identity, USD share class, LSE XMED mapping, fee, NAV, assets, replication, benchmark, constituents and risk disclosures.
- [DTCC OTC notice](https://www.dtcc.com/-/media/Files/pdf/2016/5/16/OTC-094.pdf) — DXMEF OTC symbol/name cross-check.
- [Morningstar XMED performance report](https://lt.morningstar.com/1c6qh1t6k9/etfreport/default.aspx?1=1&ClientFund=0&CurrencyId=USD&Id=0P0000M2W8&SecurityToken=0P0000M2W8%5D22%5D0%5DETEXG%24XLON&tab=1) — secondary USD annual growth rows as of 2026-07-31 and trailing fields as of 2026-08-26.
- [Morningstar XMED overview](https://lt.morningstar.com/1c6qh1t6k9/etfreport/default.aspx?1=1&ClientFund=0&CurrencyId=USD&Id=0P0000M2W8&SecurityToken=0P0000M2W8%5D22%5D0%5DETEXG%24XLON&tab=0) — secondary USD NAV/closing-price snapshot and portfolio profile.
- [ETFdoc Xtrackers MSCI Europe analysis](https://www.etfdoc.it/en/d/Ana/DBX1ME/LU0274209237_xtrackers-msci-europe-ucits-etf-1c) — secondary Euro-labelled annual/current rows retained for conflict review only.
- [Stuttgarter Xtrackers fund page](https://fonds.stuttgarter.de/product/LU0274209237/) — secondary conflicting annual/current and risk cross-check; not used in the USD calculation.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — common USD Total Return rows, dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]

## Follow-up

- Locate the issuer's online historical-performance endpoint or a dated DWS NAV series to replace the secondary annual/current proxy.
- Keep XMED's USD fund/share-class return separate from Euro-labelled secondary observations and from the LSE market-price series.
- Verify official daily NAV drawdown/recovery when a dated series is available.
