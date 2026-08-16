---
type: etf-performance-ranking
updated: 2026-08-07
scope: current-performance-pages
window: 2016-2025
return_basis: NAV total return
eligible_pages: 61
---

# ETF Performance Ranking — 2016-2025

> Screen จาก performance owner pages ที่มี annual NAV Total Return ครบ 2016-2025; ไม่ใช่คำแนะนำหรือ portfolio-fit claim.

## Bottom line

USA Top 10 นำโดย `DJD`, `DLN`, `VIG`, `VYM` และ `PFM`: `DJD` ไม่ใช่กองที่มี annual TR สูงสุด แต่ได้คะแนนจาก positive-year profile, longest positive streak และ downside stability. `VOO` และ `TDIV` ได้ `Weighted TR Score` สูง แต่ downside component ต่ำกว่า จึงอยู่ลำดับ 8-9; `FVD` ปิด Top 10 ด้วย downside ที่ดีกว่า high-volatility candidates.

Non-U.S. Regional Top 5 คือ `EPI` (India), `DXJ` (Japan), `ASEA` (Southeast Asia), `DEM` (Emerging Markets) และ `DDWM` (International). ผลนี้เป็น performance screen ตามข้อมูล 2016-2025; ไม่ควรตีความเป็นคำแนะนำการลงทุน, current-YTD forecast หรือ personal portfolio fit.

## Methodology and eligibility

- Common complete-calendar window: `2016-2025`; metric: `NAV Total Return` รวม reinvested distributions และ fund expenses; ไม่ใช้ market-price return, price return, YTD, partial year หรือ benchmark rows ใน score.
- Universe: `145` current performance owner pages → `61` eligible pages (`18` USA, `43` non-U.S.). Percentile universe ใช้ eligible 61 pages ร่วมกันในแต่ละปี.
- Primary region อ่านจาก verified underlying exposure และ region breadcrumb/frontmatter; ไม่ใช่ exchange location. Conservative continuity rule: issuer-disclosed index/strategy change ที่อยู่ภายใน 2016-2025 ถูกตัดออกเมื่อทำให้ record ไม่ใช่ like-for-like; breaks ก่อน 2016 หรือหลัง 2025 ไม่ตัดช่วงนี้.
- Eligibility: passive/index-tracking equity ETF, canonical `entity_key`, ครบ 10 annual observations, NAV TR basis ที่ยืนยันได้, ≥8 official/official-derived rows, และไม่มี material strategy/index break.
- Confidence codes: `O = official (1.00)`, `OD = official-derived (0.80)`, `S = secondary (0.50)`, `AI = AI-derived (0.25)`. Selected/eligible rows ทั้งหมดเป็น `O10`; ไม่พบ AI-derived annual row.

### Score formulas

ใช้ mid-rank percentile 0–100 ใน eligible universe: `P(x) = 100 × (rank_mid − 1) / (N − 1)`, `rank_mid = 1 + count(values < x) + 0.5 × count(values = x)`, `N = 61`; higher return/worst-year is better, while volatility uses `P(−volatility)`.

```text
Weighted annual TR percentile = Σ(confidence_weight_y × annual_percentile_y) / Σ(confidence_weight_y)
Weighted TR Score = 60 × Weighted annual TR percentile / 100
Consistency = 15 × (positive_years / 10) + 10 × (longest_positive_streak / 10)
volatility = sqrt(Σ(annual_return_y − mean_return)^2 / 10)  # population standard deviation
Downside stability = 10 × P(worst_annual_TR) / 100 + 5 × P(−volatility) / 100
Total Score = Weighted TR Score + Consistency + Downside stability
```

Tie-breakers: higher official-data coverage, higher `Consistency`, higher `Downside stability`, then ticker alphabetically. Non-U.S. selection ranks one common pool, keeps the highest-scoring ETF in each distinct primary region, then takes the five highest regional winners.

## USA Top 10

| Rank | ETF | entity_key | Primary region | Weighted TR /60 | Consistency /25 | Downside /15 | Total Score | Confidence mix | Up years | Longest streak | Worst year | Annual volatility |
|---:|---|---|---|---:|---:|---:|---:|---|---:|---:|---|---:|
| 1 | [[ETF_AMEX_DJD Performance|DJD]] — Invesco Dow Jones Industrial Average Dividend ETF | `NYSE Arca:DJD` | USA | 36.40 | 19.50 | 15.13 | 71.03 | O10 / OD0 / S0 / AI0 | 9 | 6 | 2022: -0.61% |
| 2 | [[ETF_AMEX_DLN Performance|DLN]] — WisdomTree U.S. LargeCap Dividend Fund | `NYSE Arca:DLN` | USA | 38.20 | 15.00 | 13.96 | 67.16 | O10 / OD0 / S0 / AI0 | 8 | 3 | 2018: -5.77% |
| 3 | [[ETF_AMEX_VIG Performance|VIG]] — Vanguard Dividend Appreciation ETF | `NYSE Arca:VIG` | USA | 40.00 | 15.00 | 12.13 | 67.13 | O10 / OD0 / S0 / AI0 | 8 | 3 | 2022: -9.79% |
| 4 | [[ETF_AMEX_VYM Performance|VYM]] — Vanguard High Dividend Yield ETF | `NYSE Arca:VYM` | USA | 36.65 | 15.00 | 14.46 | 66.11 | O10 / OD0 / S0 / AI0 | 8 | 3 | 2018: -5.87% |
| 5 | [[ETF_NASDAQ_PFM Performance|PFM]] — Invesco Dividend Achievers ETF | `Nasdaq:PFM` | USA | 36.60 | 15.00 | 14.38 | 65.98 | O10 / OD0 / S0 / AI0 | 8 | 3 | 2022: -6.23% |
| 6 | [[ETF_AMEX_DTD Performance|DTD]] — WisdomTree U.S. Total Dividend Fund | `NYSE Arca:DTD` | USA | 37.10 | 15.00 | 13.21 | 65.31 | O10 / OD0 / S0 / AI0 | 8 | 3 | 2018: -6.35% |
| 7 | [[ETF_NASDAQ_DVY Performance|DVY]] — iShares Select Dividend ETF | `Nasdaq:DVY` | USA | 34.50 | 17.00 | 13.04 | 64.54 | O10 / OD0 / S0 / AI0 | 8 | 5 | 2018: -6.30% |
| 8 | [[ETF_NYSE_ARCA_VOO Performance|VOO]] — Vanguard S&P 500 ETF | `NYSE Arca:VOO` | USA | 43.30 | 15.00 | 5.54 | 63.84 | O10 / OD0 / S0 / AI0 | 8 | 3 | 2022: -18.15% |
| 9 | [[ETF_NASDAQ_TDIV Performance|TDIV]] — First Trust NASDAQ Technology Dividend Index Fund | `Nasdaq:TDIV` | USA | 45.50 | 15.00 | 2.96 | 63.46 | O10 / OD0 / S0 / AI0 | 8 | 3 | 2022: -22.14% |
| 10 | [[ETF_AMEX_FVD Performance|FVD]] — First Trust Value Line® Dividend Index Fund | `NYSE Arca:FVD` | USA | 33.10 | 13.50 | 14.29 | 60.89 | O10 / OD0 / S0 / AI0 | 7 | 3 | 2022: -5.24% |

## Non-U.S. Regional Top 5

| Rank | ETF | entity_key | Primary region | Weighted TR /60 | Consistency /25 | Downside /15 | Total Score | Confidence mix | Up years | Longest streak | Worst year | Annual volatility |
|---:|---|---|---|---:|---:|---:|---:|---|---:|---:|---|---:|
| 1 | [[ETF_NYSE_ARCA_EPI Performance|EPI]] — WisdomTree India Earnings Fund | `NYSE Arca:EPI` | India | 35.60 | 15.00 | 9.79 | 60.39 | O10 / OD0 / S0 / AI0 | 8 | 3 | 2018: -10.44% |
| 2 | [[ETF_LSE_DXJ Performance|DXJ]] — WisdomTree Japan Equity UCITS ETF - USD Hedged | `LSE:DXJ` | Japan | 34.50 | 20.50 | 4.13 | 59.13 | O10 / OD0 / S0 / AI0 | 9 | 7 | 2018: -18.71% |
| 3 | [[ETF_NYSE_ARCA_ASEA Performance|ASEA]] — Global X FTSE Southeast Asia ETF | `NYSE Arca:ASEA` | Southeast Asia | 28.55 | 17.00 | 12.88 | 58.42 | O10 / OD0 / S0 / AI0 | 8 | 5 | 2020: -8.05% |
| 4 | [[ETF_AMEX_DEM Performance|DEM]] — WisdomTree Emerging Markets High Dividend Fund | `NYSE Arca:DEM` | Emerging Markets | 33.40 | 13.50 | 11.38 | 58.27 | O10 / OD0 / S0 / AI0 | 7 | 3 | 2022: -10.32% |
| 5 | [[ETF_CBOE_DDWM Performance|DDWM]] — WisdomTree Dynamic International Equity Fund | `Cboe BZX:DDWM` | International | 33.70 | 13.50 | 10.96 | 58.16 | O10 / OD0 / S0 / AI0 | 7 | 3 | 2018: -11.05% |

## Regional winner gate

ตารางนี้แสดง winner ของทุก non-U.S. primary region ก่อนตัดเหลือ Top 5; จึงตรวจได้ว่า selection ไม่ใช้ exchange location และไม่เลือกซ้ำ region.

| Regional rank | Primary region | Eligible ETFs | Regional winner | Total Score | Selected |
|---:|---|---:|---|---:|:---:|
| 1 | India | 2 | [[ETF_NYSE_ARCA_EPI Performance|EPI]] | 60.3917 | yes |
| 2 | Japan | 8 | [[ETF_LSE_DXJ Performance|DXJ]] | 59.1250 | yes |
| 3 | Southeast Asia | 1 | [[ETF_NYSE_ARCA_ASEA Performance|ASEA]] | 58.4250 | yes |
| 4 | Emerging Markets | 3 | [[ETF_AMEX_DEM Performance|DEM]] | 58.2750 | yes |
| 5 | International | 10 | [[ETF_CBOE_DDWM Performance|DDWM]] | 58.1583 | yes |
| 6 | Canada | 1 | [[ETF_NYSE_ARCA_EWC Performance|EWC]] | 56.8750 | no |
| 7 | Asia-Pacific | 5 | [[ETF_LSE_CPXJ Performance|CPXJ]] | 54.9917 | no |
| 8 | Australia | 2 | [[ETF_LSE_SAUS Performance|SAUS]] | 54.6583 | no |
| 9 | North America | 2 | [[ETF_AMEX_ENFR Performance|ENFR]] | 50.2083 | no |
| 10 | Germany | 1 | [[ETF_NYSE_ARCA_EWG Performance|EWG]] | 47.2583 | no |
| 11 | Europe | 1 | [[ETF_AMEX_FDD Performance|FDD]] | 46.2250 | no |
| 12 | Hong Kong | 1 | [[ETF_NYSE_ARCA_EWH Performance|EWH]] | 42.2750 | no |
| 13 | China | 4 | [[ETF_NASDAQ_FCA Performance|FCA]] | 39.0083 | no |
| 14 | Vietnam | 1 | [[ETF_CBOE_BZX_VNM Performance|VNM]] | 38.4750 | no |
| 15 | South Korea | 1 | [[ETF_NYSE_ARCA_EWY Performance|EWY]] | 38.3750 | no |

## Excluded candidates

มี `84` exclusions จาก current owner pages. Raw one-row-per-candidate ledger อยู่ที่ [[ETF_performance_ranking_sources_2026-08-07]]. เหตุผลด้านล่างคง wording เดียวกับ audit ledger.

| Exclusion reason | Candidates |
|---|---|
| incomplete 2016-2025 annual NAV TR coverage | [[ETF_AMEX_DIVI Performance|DIVI (NYSE Arca:DIVI)]], [[ETF_CBOE_BBJP Performance|BBJP (Cboe BZX:BBJP)]], [[ETF_CBOE_BZX_BBAX Performance|BBAX (Cboe BZX:BBAX)]], [[ETF_CBOE_BZX_CNYA Performance|CNYA (Cboe BZX:CNYA)]], [[ETF_CBOE_BZX_INDA Performance|INDA (Cboe BZX:INDA)]], [[ETF_CBOE_BZX_SMIN Performance|SMIN (Cboe BZX:SMIN)]], [[ETF_CBOE_DDLS Performance|DDLS (Cboe BZX:DDLS)]], [[ETF_EURONEXT_AMSTERDAM_ICHN Performance|ICHN (Euronext Amsterdam:ICHN)]], [[ETF_LSE_DXJA Performance|DXJA (LSE:DXJA)]], [[ETF_LSE_FLXI Performance|FLXI (LSE:FLXI)]], [[ETF_LSE_KWEB Performance|KWEB (LSE:KWEB)]], [[ETF_LSE_SJPA Performance|SJPA (LSE:SJPA)]], [[ETF_LSE_VAPU Performance|VAPU (LSE:VAPU)]], [[ETF_LSE_VDJP Performance|VDJP (LSE:VDJP)]], [[ETF_LSE_VJPU Performance|VJPU (LSE:VJPU)]], [[ETF_NASDAQ_AAXJ Performance|AAXJ (NASDAQ:AAXJ)]], [[ETF_NASDAQ_AIA Performance|AIA (NASDAQ:AIA)]], [[ETF_NASDAQ_CNQQ Performance|CNQQ (NASDAQ:CNQQ)]], [[ETF_NASDAQ_ENZL Performance|ENZL (NASDAQ:ENZL)]], [[ETF_NASDAQ_EWJV Performance|EWJV (NASDAQ:EWJV)]], [[ETF_NASDAQ_IND Performance|IND (Nasdaq:IND)]], [[ETF_NASDAQ_INDH Performance|INDH (Nasdaq:INDH)]], [[ETF_NASDAQ_INDQ Performance|INDQ (Nasdaq:INDQ)]], [[ETF_NASDAQ_INDY Performance|INDY (NASDAQ:INDY)]], [[ETF_NASDAQ_MCHI Performance|MCHI (NASDAQ:MCHI)]], [[ETF_NASDAQ_SMHC Performance|SMHC (Nasdaq:SMHC)]], [[ETF_NASDAQ_TCHI Performance|TCHI (NASDAQ:TCHI)]], [[ETF_NASDAQ_WDAF Performance|WDAF (Nasdaq:WDAF)]], [[ETF_NYSE_ARCA_ASHR Performance|ASHR (NYSE Arca:ASHR)]], [[ETF_NYSE_ARCA_ASHS Performance|ASHS (NYSE Arca:ASHS)]], [[ETF_NYSE_ARCA_CNXT Performance|CNXT (NYSE Arca:CNXT)]], [[ETF_NYSE_ARCA_DBJP Performance|DBJP (NYSE Arca:DBJP)]], [[ETF_NYSE_ARCA_DGIN Performance|DGIN (NYSE Arca:DGIN)]], [[ETF_NYSE_ARCA_DVYA Performance|DVYA (NYSE Arca:DVYA)]], [[ETF_NYSE_ARCA_ECNS Performance|ECNS (NYSE Arca:ECNS)]], [[ETF_NYSE_ARCA_EPHE Performance|EPHE (NYSE Arca:EPHE)]], [[ETF_NYSE_ARCA_EWM Performance|EWM (NYSE Arca:EWM)]], [[ETF_NYSE_ARCA_EWS Performance|EWS (NYSE Arca:EWS)]], [[ETF_NYSE_ARCA_EWT Performance|EWT (NYSE Arca:EWT)]], [[ETF_NYSE_ARCA_FLAU Performance|FLAU (NYSE Arca:FLAU)]], [[ETF_NYSE_ARCA_FLAX Performance|FLAX (NYSE Arca:FLAX)]], [[ETF_NYSE_ARCA_FLCA Performance|FLCA (NYSE Arca:FLCA)]], [[ETF_NYSE_ARCA_FLCH Performance|FLCH (NYSE Arca:FLCH)]], [[ETF_NYSE_ARCA_FLIN Performance|FLIN (NYSE Arca:FLIN)]], [[ETF_NYSE_ARCA_FLJH Performance|FLJH (NYSE Arca:FLJH)]], [[ETF_NYSE_ARCA_FLJP Performance|FLJP (NYSE Arca:FLJP)]], [[ETF_NYSE_ARCA_FLKR Performance|FLKR (NYSE Arca:FLKR)]], [[ETF_NYSE_ARCA_FLTW Performance|FLTW (NYSE Arca:FLTW)]], [[ETF_NYSE_ARCA_FXI Performance|FXI (NYSE Arca:FXI)]], [[ETF_NYSE_ARCA_GMF Performance|GMF (NYSE Arca:GMF)]], [[ETF_NYSE_ARCA_GSJY Performance|GSJY (NYSE Arca:GSJY)]], [[ETF_NYSE_ARCA_GXC Performance|GXC (NYSE Arca:GXC)]], [[ETF_NYSE_ARCA_HEWJ Performance|HEWJ (NYSE Arca:HEWJ)]], [[ETF_NYSE_ARCA_INCO Performance|INCO (NYSE Arca:INCO)]], [[ETF_NYSE_ARCA_INQQ Performance|INQQ (NYSE Arca:INQQ)]], [[ETF_NYSE_ARCA_IPAC Performance|IPAC (NYSE Arca:IPAC)]], [[ETF_NYSE_ARCA_JPXN Performance|JPXN (NYSE Arca:JPXN)]], [[ETF_NYSE_ARCA_KBA Performance|KBA (NYSE Arca:KBA)]], [[ETF_NYSE_ARCA_KCAI Performance|KCAI (NYSE Arca:KCAI)]], [[ETF_NYSE_ARCA_KDEF Performance|KDEF (NYSE Arca:KDEF)]], [[ETF_NYSE_ARCA_KGRN Performance|KGRN (NYSE Arca:KGRN)]], [[ETF_NYSE_ARCA_KMCA Performance|KMCA (NYSE Arca:KMCA)]], [[ETF_NYSE_ARCA_KSTR Performance|KSTR (NYSE Arca:KSTR)]], [[ETF_NYSE_ARCA_KTEC Performance|KTEC (NYSE Arca:KTEC)]], [[ETF_NYSE_ARCA_KURE Performance|KURE (NYSE Arca:KURE)]], [[ETF_NYSE_ARCA_THD Performance|THD (NYSE Arca:THD)]], [[ETF_NYSE_ARCA_VNAM Performance|VNAM (NYSE Arca:VNAM)]], [[ETF_NYSE_KPHO Performance|KPHO (NYSE:KPHO)]], [[ETF_XETRA_VJPA Performance|VJPA (XETRA:VJPA)]] |
| incomplete 2016-2025 annual NAV TR coverage | [[ETF_CBOE_BZX_CALF Performance|CALF (Cboe BZX:CALF)]] — only 2018-2024 are complete calendar rows; 2025 is an issuer 1 Year/YTD field |
| 2016 row is an official inception-year partial, not a complete calendar year | [[ETF_NASDAQ_VIGI Performance|VIGI (NASDAQ:VIGI)]], [[ETF_NASDAQ_VYMI Performance|VYMI (Nasdaq:VYMI)]] |
| 2025 is secondary and the 2025 history crosses the 2025-07-01 strategy/index break; not continuous like-for-like record | [[ETF_NASDAQ_OPPJ Performance|OPPJ (NASDAQ:OPPJ)]] |
| all ten rows are a secondary dividend-reinvested market-price proxy; unresolved NAV TR basis | [[ETF_NYSE_ARCA_KWEB Performance|KWEB (NYSE Arca:KWEB)]] |
| all ten rows are a secondary total-return proxy; no official NAV TR record | [[ETF_NYSE_ARCA_IDX Performance|IDX (NYSE Arca:IDX)]] |
| fund objective/strategy and underlying index changed in 2018-12-06; 2016-2025 is not continuous current-strategy history | [[ETF_NYSE_ARCA_CHIQ Performance|CHIQ (NYSE Arca:CHIQ)]] |
| issuer discloses a benchmark change before 2020-06-22 inside the ranking window; not continuous like-for-like benchmark history | [[ETF_LSE_IAPD Performance|IAPD (LSE:IAPD)]] |
| only five official annual rows; 2016-2020 are secondary proxy rows, so official/official-derived coverage is 5/10 (<8) | [[ETF_AMEX_DGRO Performance|DGRO (AMEX:DGRO)]] |
| successor fund/reorganization and current FTSE index methodology changes fall inside 2016-2025; not continuous like-for-like record | [[ETF_NYSE_ARCA_CQQQ Performance|CQQQ (NYSE Arca:CQQQ)]] |
| underlying benchmark changed on 2020-02-11; 2016-2025 mixes pre- and post-change indices | [[ETF_LSE_CSKR Performance|CSKR (LSE:CSKR)]] |
| underlying index changed on 2018-04-17 from Taiwan to India; not continuous like-for-like record | [[ETF_NASDAQ_NFTY Performance|NFTY (NASDAQ:NFTY)]] |
| underlying index changed on 2018-06-01; 2016-2025 mixes pre- and post-change indices | [[ETF_NASDAQ_EEMA Performance|EEMA (NASDAQ:EEMA)]] |
| underlying index changed on 2019-05-29; 2016-2025 mixes pre- and post-change indices | [[ETF_NYSE_ARCA_EIDO Performance|EIDO (NYSE Arca:EIDO)]] |
| underlying index changed on 2020-04-30; 2016-2025 mixes prior MVIS and current MarketGrader history | [[ETF_NYSE_ARCA_GLIN Performance|GLIN (NYSE Arca:GLIN)]] |

## Source-confidence mix and data quality

| Population | Official | Official-derived | Secondary | AI-derived | Applied weights |
|---|---:|---:|---:|---:|---|
| Eligible annual cells (`61 × 10`) | 610 | 0 | 0 | 0 | `1.00` for every cell |
| Explicit proxy/derived annual cells in excluded candidates | 0 | 0 | 26 | 0 | not scored |

- `AI-derived` annual rows identified: `0`; therefore the reduced `0.25` weight was available in the rule but not applied. No AI-derived row is silently treated as official.
- The excluded secondary rows are: DGRO 2016-2020 (`5`), OPPJ 2025 (`1`), IDX 2016-2025 (`10`), and NYSE Arca:KWEB 2016-2025 (`10`). Official rows in mixed candidates remain excluded with the candidate; only explicitly labelled proxy rows are counted here.
- `FCA` has a documented official 2024/2025 source conflict; the owner page records the reconciliation and uses the audited/reporting values, so FCA remains eligible as official data.
- VIG's legacy owner metadata `AMEX:VIG` is reconciled to issuer-verified `NYSE Arca:VIG`; annual values are unchanged and the alias is preserved in the source note.

## Reproduction audit — all eligible pages

Annual returns are the values used in the percentile universe. `O10` means all ten annual observations are official; score fields are shown to four decimals, before display rounding in the Top 10 tables.

| ETF | entity_key | Region | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Confidence | Wtd TR pct | TR score | Up | Streak | Consistency | Worst | Volatility | Worst pct | Worst score | Inv-vol pct | Vol score | Downside | Total |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|
| [[ETF_AMEX_DJD Performance|DJD]] | `NYSE Arca:DJD` | USA | +16.93% | +21.63% | +0.11% | +22.37% | +0.94% | +22.33% | -0.61% | +9.26% | +13.79% | +15.72% | O10 / OD0 / S0 / AI0 | 60.6667 | 36.4000 | 9 | 6 | 19.5000 | 2022 -0.61% | 8.8201 | 100.8333 | 10.0833 | 100.8333 | 5.0417 | 15.1250 | 71.0250 |
| [[ETF_AMEX_DLN Performance|DLN]] | `NYSE Arca:DLN` | USA | +15.37% | +18.21% | -5.77% | +29.03% | +4.55% | +25.60% | -3.79% | +9.93% | +19.55% | +15.59% | O10 / OD0 / S0 / AI0 | 63.6667 | 38.2000 | 8 | 3 | 15.0000 | 2018 -5.77% | 11.0129 | 97.5000 | 9.7500 | 84.1667 | 4.2083 | 13.9583 | 67.1583 |
| [[ETF_AMEX_VIG Performance|VIG]] | `NYSE Arca:VIG` | USA | +11.84% | +22.22% | -2.02% | +29.71% | +15.46% | +23.64% | -9.79% | +14.46% | +17.02% | +14.18% | O10 / OD0 / S0 / AI0 | 66.6667 | 40.0000 | 8 | 3 | 15.0000 | 2022 -9.79% | 11.1579 | 80.8333 | 8.0833 | 80.8333 | 4.0417 | 12.1250 | 67.1250 |
| [[ETF_AMEX_VYM Performance|VYM]] | `NYSE Arca:VYM` | USA | +16.87% | +16.42% | -5.87% | +24.20% | +1.14% | +26.14% | -0.42% | +6.53% | +17.60% | +15.43% | O10 / OD0 / S0 / AI0 | 61.0833 | 36.6500 | 8 | 3 | 15.0000 | 2018 -5.87% | 10.2773 | 95.8333 | 9.5833 | 97.5000 | 4.8750 | 14.4583 | 66.1083 |
| [[ETF_NASDAQ_PFM Performance|PFM]] | `Nasdaq:PFM` | USA | +14.64% | +17.35% | -4.40% | +26.79% | +9.54% | +23.19% | -6.23% | +11.31% | +16.98% | +13.88% | O10 / OD0 / S0 / AI0 | 61.0000 | 36.6000 | 8 | 3 | 15.0000 | 2022 -6.23% | 10.0736 | 94.1667 | 9.4167 | 99.1667 | 4.9583 | 14.3750 | 65.9750 |
| [[ETF_AMEX_DTD Performance|DTD]] | `NYSE Arca:DTD` | USA | +16.59% | +17.25% | -6.35% | +28.28% | +2.57% | +26.14% | -3.81% | +10.44% | +18.75% | +14.22% | O10 / OD0 / S0 / AI0 | 61.8333 | 37.1000 | 8 | 3 | 15.0000 | 2018 -6.35% | 11.1376 | 90.8333 | 9.0833 | 82.5000 | 4.1250 | 13.2083 | 65.3083 |
| [[ETF_NASDAQ_DVY Performance|DVY]] | `Nasdaq:DVY` | USA | +21.50% | +15.00% | -6.30% | +22.70% | -4.90% | +31.63% | +1.92% | +1.09% | +16.19% | +11.64% | O10 / OD0 / S0 / AI0 | 57.5000 | 34.5000 | 8 | 5 | 17.0000 | 2018 -6.30% | 12.0367 | 92.5000 | 9.2500 | 75.8333 | 3.7917 | 13.0417 | 64.5417 |
| [[ETF_NYSE_ARCA_VOO Performance|VOO]] | `NYSE Arca:VOO` | USA | +11.93% | +21.78% | -4.42% | +31.46% | +18.35% | +28.66% | -18.15% | +26.25% | +24.98% | +17.84% | O10 / OD0 / S0 / AI0 | 72.1667 | 43.3000 | 8 | 3 | 15.0000 | 2022 -18.15% | 14.9228 | 29.1667 | 2.9167 | 52.5000 | 2.6250 | 5.5417 | 63.8417 |
| [[ETF_NASDAQ_TDIV Performance|TDIV]] | `Nasdaq:TDIV` | USA | +19.63% | +21.90% | -3.01% | +33.31% | +17.27% | +29.56% | -22.14% | +36.78% | +24.51% | +25.19% | O10 / OD0 / S0 / AI0 | 75.8333 | 45.5000 | 8 | 3 | 15.0000 | 2022 -22.14% | 16.9851 | 15.8333 | 1.5833 | 27.5000 | 1.3750 | 2.9583 | 63.4583 |
| [[ETF_AMEX_FVD Performance|FVD]] | `NYSE Arca:FVD` | USA | +19.94% | +12.48% | -3.44% | +26.56% | -0.01% | +24.86% | -5.24% | +4.10% | +10.00% | +8.19% | O10 / OD0 / S0 / AI0 | 55.1667 | 33.1000 | 7 | 3 | 13.5000 | 2022 -5.24% | 10.7263 | 99.1667 | 9.9167 | 87.5000 | 4.3750 | 14.2917 | 60.8917 |
| [[ETF_NASDAQ_PEY Performance|PEY]] | `Nasdaq:PEY` | USA | +31.56% | +8.64% | -7.36% | +24.61% | -3.76% | +26.03% | +2.49% | +7.35% | +5.14% | +0.62% | O10 / OD0 / S0 / AI0 | 52.3333 | 31.4000 | 8 | 5 | 17.0000 | 2018 -7.36% | 12.6516 | 87.5000 | 8.7500 | 70.8333 | 3.5417 | 12.2917 | 60.6917 |
| [[ETF_NYSE_ARCA_EPI Performance|EPI]] | `NYSE Arca:EPI` | India | +2.24% | +39.03% | -10.44% | +1.70% | +18.07% | +28.02% | -5.72% | +26.31% | +11.11% | +1.83% | O10 / OD0 / S0 / AI0 | 59.3333 | 35.6000 | 8 | 3 | 15.0000 | 2018 -10.44% | 15.3161 | 75.8333 | 7.5833 | 44.1667 | 2.2083 | 9.7917 | 60.3917 |
| [[ETF_AMEX_DON Performance|DON]] | `NYSE Arca:DON` | USA | +20.30% | +14.86% | -8.27% | +23.42% | -5.40% | +30.19% | -4.76% | +13.98% | +14.12% | +3.91% | O10 / OD0 / S0 / AI0 | 56.0000 | 33.6000 | 7 | 3 | 13.5000 | 2018 -8.27% | 12.5523 | 84.1667 | 8.4167 | 72.5000 | 3.6250 | 12.0417 | 59.1417 |
| [[ETF_LSE_DXJ Performance|DXJ]] | `LSE:DXJ` | Japan | +0.73% | +22.17% | -18.71% | +18.53% | +2.82% | +18.07% | +6.48% | +40.46% | +30.55% | +31.19% | O10 / OD0 / S0 / AI0 | 57.5000 | 34.5000 | 9 | 7 | 20.5000 | 2018 -18.71% | 16.6908 | 25.8333 | 2.5833 | 30.8333 | 1.5417 | 4.1250 | 59.1250 |
| [[ETF_NYSE_ARCA_IMVP Performance|IMVP]] | `NYSE Arca:IMVP` | India | +0.11% | +37.12% | -8.10% | +4.83% | +18.96% | +23.94% | -9.54% | +22.61% | +9.52% | +1.72% | O10 / OD0 / S0 / AI0 | 54.3333 | 32.6000 | 8 | 3 | 15.0000 | 2022 -9.54% | 14.3935 | 82.5000 | 8.2500 | 59.1667 | 2.9583 | 11.2083 | 58.8083 |
| [[ETF_NYSE_ARCA_ASEA Performance|ASEA]] | `NYSE Arca:ASEA` | Southeast Asia | +8.39% | +31.89% | -6.35% | +7.78% | -8.05% | +5.26% | +5.16% | +4.43% | +11.42% | +18.46% | O10 / OD0 / S0 / AI0 | 47.5833 | 28.5500 | 8 | 5 | 17.0000 | 2020 -8.05% | 10.8795 | 85.8333 | 8.5833 | 85.8333 | 4.2917 | 12.8750 | 58.4250 |
| [[ETF_AMEX_DEM Performance|DEM]] | `NYSE Arca:DEM` | Emerging Markets | +22.54% | +24.87% | -7.31% | +19.37% | -5.64% | +11.69% | -10.32% | +20.93% | +5.22% | +20.54% | O10 / OD0 / S0 / AI0 | 55.6667 | 33.4000 | 7 | 3 | 13.5000 | 2022 -10.32% | 12.9585 | 79.1667 | 7.9167 | 69.1667 | 3.4583 | 11.3750 | 58.2750 |
| [[ETF_CBOE_DDWM Performance|DDWM]] | `Cboe BZX:DDWM` | International | +14.18% | +18.52% | -11.05% | +21.03% | -4.20% | +14.33% | -1.27% | +15.44% | +10.65% | +30.10% | O10 / OD0 / S0 / AI0 | 56.1667 | 33.7000 | 7 | 3 | 13.5000 | 2018 -11.05% | 11.9594 | 70.8333 | 7.0833 | 77.5000 | 3.8750 | 10.9583 | 58.1583 |
| [[ETF_AMEX_DHS Performance|DHS]] | `NYSE Arca:DHS` | USA | +17.85% | +11.68% | -7.25% | +22.58% | -5.68% | +23.11% | +7.88% | -0.19% | +17.98% | +12.92% | O10 / OD0 / S0 / AI0 | 52.8333 | 31.7000 | 7 | 2 | 12.5000 | 2018 -7.25% | 10.5757 | 89.1667 | 8.9167 | 92.5000 | 4.6250 | 13.5417 | 57.7417 |
| [[ETF_NYSE_ARCA_EWC Performance|EWC]] | `NYSE Arca:EWC` | Canada | +24.30% | +16.00% | -17.20% | +27.40% | +5.60% | +26.74% | -12.77% | +14.62% | +12.25% | +36.03% | O10 / OD0 / S0 / AI0 | 60.8333 | 36.5000 | 8 | 3 | 15.0000 | 2018 -17.20% | 16.4208 | 37.5000 | 3.7500 | 32.5000 | 1.6250 | 5.3750 | 56.8750 |
| [[ETF_AMEX_SDOG Performance|SDOG]] | `NYSE Arca:SDOG` | USA | +22.36% | +12.67% | -11.30% | +24.09% | -0.37% | +24.40% | -0.13% | +4.06% | +14.84% | +11.08% | O10 / OD0 / S0 / AI0 | 54.0000 | 32.4000 | 7 | 3 | 13.5000 | 2018 -11.30% | 11.3544 | 67.5000 | 6.7500 | 79.1667 | 3.9583 | 10.7083 | 56.6083 |
| [[ETF_LSE_IJPD Performance|IJPD]] | `LSE:IJPD` | Japan | -1.90% | +20.70% | -14.10% | +20.40% | +9.00% | +12.80% | -2.70% | +34.50% | +25.60% | +27.70% | O10 / OD0 / S0 / AI0 | 57.5000 | 34.5000 | 7 | 3 | 13.5000 | 2018 -14.10% | 14.7299 | 54.1667 | 5.4167 | 55.8333 | 2.7917 | 8.2083 | 56.2083 |
| [[ETF_LSE_CPXJ Performance|CPXJ]] | `LSE:CPXJ` | Asia-Pacific | +7.70% | +25.80% | -10.40% | +18.20% | +6.40% | +4.70% | -6.10% | +6.30% | +4.50% | +20.40% | O10 / OD0 / S0 / AI0 | 46.1667 | 27.7000 | 8 | 3 | 15.0000 | 2018 -10.40% | 10.6774 | 77.5000 | 7.7500 | 90.8333 | 4.5417 | 12.2917 | 54.9917 |
| [[ETF_LSE_SAUS Performance|SAUS]] | `LSE:SAUS` | Australia | +11.00% | +19.60% | -12.30% | +22.50% | +8.40% | +9.00% | -5.70% | +14.30% | +0.80% | +14.30% | O10 / OD0 / S0 / AI0 | 47.4167 | 28.4500 | 8 | 3 | 15.0000 | 2018 -12.30% | 10.4193 | 65.0000 | 6.5000 | 94.1667 | 4.7083 | 11.2083 | 54.6583 |
| [[ETF_NYSE_ARCA_EWA Performance|EWA]] | `NYSE Arca:EWA` | Australia | +11.10% | +19.60% | -12.30% | +22.40% | +8.30% | +9.09% | -5.74% | +13.98% | +0.82% | +14.12% | O10 / OD0 / S0 / AI0 | 46.5000 | 27.9000 | 8 | 3 | 15.0000 | 2018 -12.30% | 10.3840 | 65.0000 | 6.5000 | 95.8333 | 4.7917 | 11.2917 | 54.1917 |
| [[ETF_AMEX_IDOG Performance|IDOG]] | `NYSE Arca:IDOG` | International | +3.97% | +25.81% | -13.09% | +20.86% | -1.34% | +11.36% | -4.23% | +22.64% | +1.53% | +39.83% | O10 / OD0 / S0 / AI0 | 53.8333 | 32.3000 | 7 | 3 | 13.5000 | 2018 -13.09% | 15.4476 | 59.1667 | 5.9167 | 40.8333 | 2.0417 | 7.9583 | 53.7583 |
| [[ETF_NASDAQ_PID Performance|PID]] | `Nasdaq:PID` | International | +9.92% | +19.03% | -11.08% | +25.44% | -6.55% | +24.25% | -6.36% | +14.68% | +2.81% | +24.40% | O10 / OD0 / S0 / AI0 | 49.8333 | 29.9000 | 7 | 3 | 13.5000 | 2018 -11.08% | 13.3742 | 69.1667 | 6.9167 | 67.5000 | 3.3750 | 10.2917 | 53.6917 |
| [[ETF_NYSE_ARCA_EPP Performance|EPP]] | `NYSE Arca:EPP` | Asia-Pacific | +7.40% | +25.40% | -10.70% | +17.90% | +6.00% | +4.42% | -6.45% | +5.92% | +4.04% | +20.16% | O10 / OD0 / S0 / AI0 | 43.1667 | 25.9000 | 8 | 3 | 15.0000 | 2018 -10.70% | 10.6809 | 72.5000 | 7.2500 | 89.1667 | 4.4583 | 11.7083 | 52.6083 |
| [[ETF_NASDAQ_VXUS Performance|VXUS]] | `Nasdaq:VXUS` | International | +4.72% | +27.52% | -14.42% | +21.58% | +11.32% | +8.69% | -15.99% | +15.56% | +5.20% | +32.23% | O10 / OD0 / S0 / AI0 | 51.0000 | 30.6000 | 8 | 3 | 15.0000 | 2022 -15.99% | 15.1362 | 44.1667 | 4.4167 | 49.1667 | 2.4583 | 6.8750 | 52.4750 |
| [[ETF_CBOE_IDV Performance|IDV]] | `Cboe BZX:IDV` | International | +7.70% | +19.60% | -10.50% | +23.10% | -5.40% | +11.97% | -6.75% | +10.75% | +3.97% | +51.69% | O10 / OD0 / S0 / AI0 | 50.3333 | 30.2000 | 7 | 3 | 13.5000 | 2018 -10.50% | 17.2689 | 74.1667 | 7.4167 | 24.1667 | 1.2083 | 8.6250 | 52.3250 |
| [[ETF_NASDAQ_FYC Performance|FYC]] | `NASDAQ:FYC` | USA | +13.92% | +23.19% | -5.60% | +16.80% | +32.08% | +21.75% | -25.75% | +14.15% | +24.05% | +24.34% | O10 / OD0 / S0 / AI0 | 57.5000 | 34.5000 | 8 | 3 | 15.0000 | 2022 -25.75% | 16.2828 | 10.8333 | 1.0833 | 34.1667 | 1.7083 | 2.7917 | 52.2917 |
| [[ETF_NYSE_ARCA_DGS Performance|DGS]] | `NYSE Arca:DGS` | Emerging Markets | +14.91% | +35.48% | -15.39% | +17.28% | +4.14% | +15.60% | -12.15% | +18.92% | +2.13% | +20.40% | O10 / OD0 / S0 / AI0 | 49.0833 | 29.4500 | 8 | 3 | 15.0000 | 2018 -15.39% | 14.7540 | 47.5000 | 4.7500 | 54.1667 | 2.7083 | 7.4583 | 51.9083 |
| [[ETF_AMEX_DES Performance|DES]] | `NYSE Arca:DES` | USA | +31.06% | +8.66% | -12.74% | +20.30% | -4.41% | +26.71% | -10.94% | +16.40% | +9.79% | +0.26% | O10 / OD0 / S0 / AI0 | 47.8333 | 28.7000 | 7 | 3 | 13.5000 | 2018 -12.74% | 14.5173 | 60.8333 | 6.0833 | 57.5000 | 2.8750 | 8.9583 | 51.1583 |
| [[ETF_AMEX_DWM Performance|DWM]] | `NYSE Arca:DWM` | International | +2.88% | +23.46% | -13.54% | +19.07% | -1.94% | +10.44% | -9.11% | +16.56% | +4.56% | +34.40% | O10 / OD0 / S0 / AI0 | 47.5000 | 28.5000 | 7 | 3 | 13.5000 | 2018 -13.54% | 14.2363 | 57.5000 | 5.7500 | 62.5000 | 3.1250 | 8.8750 | 50.8750 |
| [[ETF_LSE_CJPU Performance|CJPU]] | `LSE:CJPU` | Japan | +1.90% | +23.40% | -13.30% | +19.10% | +14.00% | +1.20% | -17.00% | +19.80% | +8.20% | +24.50% | O10 / OD0 / S0 / AI0 | 46.8333 | 28.1000 | 8 | 3 | 15.0000 | 2022 -17.00% | 14.0347 | 40.8333 | 4.0833 | 65.8333 | 3.2917 | 7.3750 | 50.4750 |
| [[ETF_NYSE_ARCA_VPL Performance|VPL]] | `NYSE Arca:VPL` | Asia-Pacific | +5.31% | +28.60% | -13.85% | +17.61% | +16.58% | +1.51% | -15.21% | +15.58% | +1.27% | +33.16% | O10 / OD0 / S0 / AI0 | 47.1667 | 28.3000 | 8 | 3 | 15.0000 | 2022 -15.21% | 15.4287 | 49.1667 | 4.9167 | 42.5000 | 2.1250 | 7.0417 | 50.3417 |
| [[ETF_AMEX_ENFR Performance|ENFR]] | `NYSE Arca:ENFR` | North America | +41.95% | -0.09% | -18.29% | +21.20% | -24.31% | +39.60% | +18.33% | +15.05% | +42.06% | +5.93% | O10 / OD0 / S0 / AI0 | 55.0000 | 33.0000 | 7 | 5 | 15.5000 | 2020 -24.31% | 22.5153 | 12.5000 | 1.2500 | 9.1667 | 0.4583 | 1.7083 | 50.2083 |
| [[ETF_NYSE_ARCA_EWJ Performance|EWJ]] | `NYSE Arca:EWJ` | Japan | +1.96% | +23.56% | -13.17% | +19.19% | +14.03% | +1.56% | -17.36% | +19.78% | +6.80% | +25.92% | O10 / OD0 / S0 / AI0 | 47.5833 | 28.5500 | 8 | 3 | 15.0000 | 2022 -17.36% | 14.2610 | 35.8333 | 3.5833 | 60.8333 | 3.0417 | 6.6250 | 50.1750 |
| [[ETF_AMEX_DTH Performance|DTH]] | `NYSE Arca:DTH` | International | +5.10% | +20.33% | -12.57% | +17.74% | -7.05% | +8.62% | -2.12% | +15.19% | +2.03% | +42.41% | O10 / OD0 / S0 / AI0 | 44.8333 | 26.9000 | 7 | 3 | 13.5000 | 2018 -12.57% | 15.0657 | 62.5000 | 6.2500 | 50.8333 | 2.5417 | 8.7917 | 49.1917 |
| [[ETF_LSE_IJPU Performance|IJPU]] | `LSE:IJPU` | Japan | +1.80% | +23.30% | -13.40% | +19.00% | +13.80% | +1.10% | -17.10% | +19.70% | +8.20% | +24.50% | O10 / OD0 / S0 / AI0 | 44.8333 | 26.9000 | 8 | 3 | 15.0000 | 2022 -17.10% | 14.0423 | 39.1667 | 3.9167 | 64.1667 | 3.2083 | 7.1250 | 49.0250 |
| [[ETF_LSE_VDPX Performance|VDPX]] | `LSE:VDPX` | Asia-Pacific | +8.49% | +32.21% | -14.37% | +16.97% | +18.67% | +1.05% | -12.65% | +11.00% | -5.67% | +40.91% | O10 / OD0 / S0 / AI0 | 46.5000 | 27.9000 | 7 | 3 | 13.5000 | 2018 -14.37% | 17.3412 | 52.5000 | 5.2500 | 22.5000 | 1.1250 | 6.3750 | 47.7750 |
| [[ETF_AMEX_AMLP Performance|AMLP]] | `NYSE Arca:AMLP` | North America | +15.15% | -7.80% | -12.67% | +5.95% | -32.53% | +39.49% | +25.12% | +21.39% | +22.61% | +5.88% | O10 / OD0 / S0 / AI0 | 51.1667 | 30.7000 | 7 | 5 | 15.5000 | 2020 -32.53% | 20.1400 | 4.1667 | 0.4167 | 15.8333 | 0.7917 | 1.2083 | 47.4083 |
| [[ETF_NYSE_ARCA_EWG Performance|EWG]] | `NYSE Arca:EWG` | Germany | +2.60% | +27.40% | -22.30% | +20.60% | +11.30% | +4.85% | -22.17% | +22.90% | +10.32% | +35.15% | O10 / OD0 / S0 / AI0 | 49.6667 | 29.8000 | 8 | 3 | 15.0000 | 2018 -22.30% | 18.3483 | 14.1667 | 1.4167 | 20.8333 | 1.0417 | 2.4583 | 47.2583 |
| [[ETF_AMEX_DFJ Performance|DFJ]] | `NYSE Arca:DFJ` | Japan | +11.04% | +31.62% | -17.63% | +17.02% | -0.06% | +0.51% | -8.65% | +21.60% | +3.24% | +30.87% | O10 / OD0 / S0 / AI0 | 46.4167 | 27.8500 | 7 | 3 | 13.5000 | 2018 -17.63% | 15.5731 | 34.1667 | 3.4167 | 39.1667 | 1.9583 | 5.3750 | 46.7250 |
| [[ETF_CBOE_EFAV Performance|EFAV]] | `Cboe BZX:EFAV` | International | -1.86% | +21.57% | -5.80% | +16.78% | +0.19% | +7.02% | -14.76% | +11.98% | +5.28% | +26.16% | O10 / OD0 / S0 / AI0 | 40.1667 | 24.1000 | 7 | 3 | 13.5000 | 2022 -14.76% | 12.0989 | 50.8333 | 5.0833 | 74.1667 | 3.7083 | 8.7917 | 46.3917 |
| [[ETF_AMEX_FDD Performance|FDD]] | `NYSE Arca:FDD` | Europe | +2.58% | +19.04% | -8.83% | +23.09% | -2.64% | +15.07% | -15.67% | +13.42% | +0.60% | +61.85% | O10 / OD0 / S0 / AI0 | 46.0000 | 27.6000 | 7 | 3 | 13.5000 | 2022 -15.67% | 20.7083 | 45.8333 | 4.5833 | 10.8333 | 0.5417 | 5.1250 | 46.2250 |
| [[ETF_NYSE_ARCA_VSS Performance|VSS]] | `NYSE Arca:VSS` | International | +4.37% | +30.26% | -18.43% | +21.73% | +11.95% | +12.81% | -21.22% | +15.25% | +2.67% | +29.99% | O10 / OD0 / S0 / AI0 | 46.1667 | 27.7000 | 8 | 3 | 15.0000 | 2022 -21.22% | 16.8642 | 17.5000 | 1.7500 | 29.1667 | 1.4583 | 3.2083 | 45.9083 |
| [[ETF_NASDAQ_KBWD Performance|KBWD]] | `Nasdaq:KBWD` | USA | +20.62% | +11.93% | -8.78% | +20.56% | -15.21% | +31.85% | -18.99% | +19.98% | +4.43% | +5.51% | O10 / OD0 / S0 / AI0 | 46.5000 | 27.9000 | 7 | 3 | 13.5000 | 2022 -18.99% | 16.1429 | 24.1667 | 2.4167 | 37.5000 | 1.8750 | 4.2917 | 45.6917 |
| [[ETF_NYSE_ARCA_SCJ Performance|SCJ]] | `NYSE Arca:SCJ` | Japan | +7.60% | +30.90% | -16.40% | +19.00% | +6.30% | -2.40% | -12.70% | +12.95% | +3.26% | +29.66% | O10 / OD0 / S0 / AI0 | 42.2500 | 25.3500 | 7 | 3 | 13.5000 | 2018 -16.40% | 15.1534 | 42.5000 | 4.2500 | 47.5000 | 2.3750 | 6.6250 | 45.4750 |
| [[ETF_NASDAQ_FJP Performance|FJP]] | `NASDAQ:FJP` | Japan | +2.91% | +26.70% | -17.66% | +8.27% | +1.71% | -0.69% | -12.04% | +22.42% | +5.84% | +32.14% | O10 / OD0 / S0 / AI0 | 43.1667 | 25.9000 | 7 | 3 | 13.5000 | 2018 -17.66% | 15.2817 | 32.5000 | 3.2500 | 45.8333 | 2.2917 | 5.5417 | 44.9417 |
| [[ETF_LSE_CEMA Performance|CEMA]] | `LSE:CEMA` | Emerging Markets | +5.48% | +41.88% | -15.99% | +18.47% | +27.57% | -5.20% | -21.00% | +7.57% | +11.98% | +32.40% | O10 / OD0 / S0 / AI0 | 47.6667 | 28.6000 | 7 | 3 | 13.5000 | 2022 -21.00% | 19.4816 | 19.1667 | 1.9167 | 17.5000 | 0.8750 | 2.7917 | 44.8917 |
| [[ETF_NYSE_ARCA_DLS Performance|DLS]] | `NYSE Arca:DLS` | International | +7.00% | +30.95% | -18.69% | +22.11% | -1.23% | +11.66% | -17.36% | +15.40% | +3.24% | +33.49% | O10 / OD0 / S0 / AI0 | 45.5000 | 27.3000 | 7 | 3 | 13.5000 | 2018 -18.69% | 17.0403 | 27.5000 | 2.7500 | 25.8333 | 1.2917 | 4.0417 | 44.8417 |
| [[ETF_NASDAQ_FPA Performance|FPA]] | `NASDAQ:FPA` | Asia-Pacific | +0.29% | +35.93% | -20.71% | +7.35% | +14.89% | +2.75% | -15.62% | +10.67% | +3.84% | +42.31% | O10 / OD0 / S0 / AI0 | 40.5000 | 24.3000 | 8 | 3 | 15.0000 | 2018 -20.71% | 18.7042 | 20.8333 | 2.0833 | 19.1667 | 0.9583 | 3.0417 | 42.3417 |
| [[ETF_NYSE_ARCA_EWH Performance|EWH]] | `NYSE Arca:EWH` | Hong Kong | +1.80% | +35.60% | -8.30% | +9.70% | +4.60% | -3.43% | -6.72% | -14.04% | +0.10% | +34.89% | O10 / OD0 / S0 / AI0 | 39.8333 | 23.9000 | 6 | 2 | 11.0000 | 2023 -14.04% | 16.2245 | 55.8333 | 5.5833 | 35.8333 | 1.7917 | 7.3750 | 42.2750 |
| [[ETF_NASDAQ_FCA Performance|FCA]] | `Nasdaq:FCA` | China | -4.96% | +58.35% | -17.87% | +17.34% | +13.58% | -1.18% | -17.10% | -9.32% | +15.43% | +42.95% | O10 / OD0 / S0 / AI0 | 43.4167 | 26.0500 | 5 | 2 | 9.5000 | 2018 -17.87% | 23.9834 | 30.8333 | 3.0833 | 7.5000 | 0.3750 | 3.4583 | 39.0083 |
| [[ETF_LSE_FXC Performance|FXC]] | `LSE:FXC` | China | +1.80% | +34.51% | -12.39% | +13.76% | +10.06% | -20.70% | -20.01% | -13.57% | +31.03% | +28.16% | O10 / OD0 / S0 / AI0 | 41.8333 | 25.1000 | 6 | 2 | 11.0000 | 2021 -20.70% | 20.3222 | 22.5000 | 2.2500 | 12.5000 | 0.6250 | 2.8750 | 38.9750 |
| [[ETF_CBOE_BZX_VNM Performance|VNM]] | `Cboe BZX:VNM` | Vietnam | -9.78% | +35.76% | -14.14% | +8.86% | +9.72% | +22.52% | -44.47% | +15.95% | -10.19% | +62.42% | O10 / OD0 / S0 / AI0 | 43.5000 | 26.1000 | 6 | 3 | 12.0000 | 2022 -44.47% | 28.1052 | 0.8333 | 0.0833 | 5.8333 | 0.2917 | 0.3750 | 38.4750 |
| [[ETF_NYSE_ARCA_EWY Performance|EWY]] | `NYSE Arca:EWY` | South Korea | +7.10% | +44.40% | -20.30% | +8.30% | +39.70% | -7.56% | -26.70% | +19.05% | -20.79% | +97.57% | O10 / OD0 / S0 / AI0 | 44.1667 | 26.5000 | 6 | 2 | 11.0000 | 2022 -26.70% | 36.3074 | 7.5000 | 0.7500 | 2.5000 | 0.1250 | 0.8750 | 38.3750 |
| [[ETF_NASDAQ_CXSE Performance|CXSE]] | `NASDAQ:CXSE` | China | -1.20% | +78.04% | -27.95% | +36.44% | +60.58% | -23.77% | -28.89% | -18.67% | +9.59% | +36.39% | O10 / OD0 / S0 / AI0 | 46.1667 | 27.7000 | 5 | 2 | 9.5000 | 2022 -28.89% | 36.8533 | 5.8333 | 0.5833 | 0.8333 | 0.0417 | 0.6250 | 37.8250 |
| [[ETF_NASDAQ_PGJ Performance|PGJ]] | `NASDAQ:PGJ` | China | -11.36% | +59.97% | -29.16% | +31.91% | +53.58% | -42.76% | -24.36% | -2.45% | +5.88% | +13.73% | O10 / OD0 / S0 / AI0 | 38.3333 | 23.0000 | 5 | 2 | 9.5000 | 2021 -42.76% | 32.8838 | 2.5000 | 0.2500 | 4.1667 | 0.2083 | 0.4583 | 32.9583 |
| [[ETF_NASDAQ_KBWY Performance|KBWY]] | `Nasdaq:KBWY` | USA | +33.05% | +0.86% | -18.04% | +23.44% | -25.82% | +31.14% | -18.90% | +12.75% | -3.45% | -5.33% | O10 / OD0 / S0 / AI0 | 35.8333 | 21.5000 | 5 | 2 | 9.5000 | 2020 -25.82% | 20.1895 | 9.1667 | 0.9167 | 14.1667 | 0.7083 | 1.6250 | 32.6250 |
## Sources

- Numeric source of truth: each linked ETF performance owner page in the tables above; each owner page retains the issuer source URL(s), return basis, annual as-of/source batch, and any conflict or gap.
- Dated ranking source/reconciliation note: [[ETF_performance_ranking_sources_2026-08-07]].
- Canonical VIG exchange check: [Vanguard VIG product page](https://investor.vanguard.com/investment-products/etfs/profile/vig) — issuer page states the ETF is listed on NYSE Arca; the legacy `AMEX:VIG` alias is not used as the displayed key.
- Current YTD, rolling 10-year figures, market price, and S&P 500 comparison rows are context only and are not inputs to this ranking.
