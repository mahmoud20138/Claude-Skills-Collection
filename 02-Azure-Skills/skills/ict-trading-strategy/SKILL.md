# ICT Trading Strategy Skills

> Use this skill when working on ICT (Inner Circle Trader) Smart Money Concepts, MQL5 indicators, trading strategy code, or anything related to Mahmoud's trading framework.

---

## Core Methodology

ICT Smart Money Concepts by Michael J. Huddleston. Markets are driven by institutional order flow through three phases: **Accumulation, Manipulation, Distribution (AMD / Power of 3)**.

### The Five Pillars

1. **Market Structure** -- Where is the trend? (HH/HL = bullish, LH/LL = bearish)
2. **Liquidity** -- Where are the stops? (BSL above, SSL below)
3. **PD Arrays** -- Where do institutions enter? (FVG, OB, Breaker)
4. **Time** -- When does it happen? (Killzones only)
5. **Confluence** -- How many factors align? (Score >= 5 to trade)

### Price Delivery Algorithm

```
ERL (sweep liquidity) --> IRL (retrace to FVG/OB) --> ERL (target opposite liquidity)
```

---

## Market Structure

- **BOS (Break of Structure)**: Trend continuation -- price breaks prior swing in trend direction
- **CHoCH (Change of Character)**: Trend reversal warning -- breaks opposing swing
- **MSS (Market Structure Shift)**: CHoCH + displacement = confirmed reversal
- **MSS Validation**: Swing violation + displacement candle (large body, small wicks) + FVG created + occurs after liquidity sweep
- **Rule**: Never trade against TWO timeframes above your entry TF

### Multi-TF Hierarchy

```
Weekly --> Daily --> 4H --> 1H --> 15M/5M --> 1M
(bias)   (swing)  (intermediate) (entry) (execution) (precision)
```

---

## Liquidity

- **BSL (Buy-Side)**: Above swing highs, EQH, PDH, PWH, session highs
- **SSL (Sell-Side)**: Below swing lows, EQL, PDL, PWL, session lows
- **Sweep != Breakout**: Wick through + body closes back = sweep (high-prob reversal)
- **Equal highs/lows** are the strongest engineered liquidity pools

---

## PD Arrays (Entry Zones)

### Fair Value Gaps (FVG)
- 3-candle formation where C1 and C3 wicks don't overlap
- Best entry: upper 25% (bullish) or lower 25% (bearish) of the gap
- First touch (untouched) FVGs are strongest
- 50%+ filled = mitigated

### Order Blocks (OB)
- Last opposing candle before displacement
- **3-Part Validation**: Displacement + FVG creation + BOS/MSS (ALL required)
- Best entry: 50% of OB body (mean threshold)
- Price closing through entire OB body = invalidated

### OB Variants
- **Breaker Block**: Failed OB, now acts as S/R in opposite direction
- **Mitigation Block**: Partially filled OB, trade on second test
- **Reclaimed OB**: Swept but held -- strongest type

### Premium / Discount & OTE
```
100% -- Swing High ---- PREMIUM (sell entries)
 79% -- OTE Top
70.5% - OTE Sweet Spot (primary entry)
 62% -- OTE Bottom
 50% -- EQUILIBRIUM (skip -- no edge)
  0% -- Swing Low ----- DISCOUNT (buy entries)
```

### Fibonacci Levels (ICT Custom)
- Entry: 0.62, 0.705, 0.79 (OTE zone)
- Targets: -0.27, -0.62, -1.0, -1.5, -2.0, -2.5

---

## Time Theory -- Sessions & Killzones (EST)

| Session | Time (EST) | Action |
|---------|-----------|--------|
| Asian | 7 PM - 12 AM | Mark range (AH/AL) -- NO trading |
| **London KZ** | **2-5 AM** | **PRIMARY EXECUTION** |
| **NY Open KZ** | **8:30-11 AM** | **PRIMARY EXECUTION** |
| NY Lunch | 11 AM - 1 PM | **NO TRADING** |
| NY Afternoon | 1-3 PM | Secondary setups only |

### Silver Bullet Windows
- SB1: 2:00-3:00 AM (London Open)
- SB2: 3:00-4:00 AM (London Continuation)
- **SB3: 9:30-10:30 AM (NY Open -- PRIMARY)**

### News Rule
- No entries within 30 min before/after red-folder news
- FOMC/NFP/CPI days: consider sitting out or post-event only

---

## Trading Strategies

### Strategy A: MSS + FVG (Primary)
1. Establish HTF bias (Daily)
2. Mark key levels (PDH/PDL, AH/AL, EQH/EQL)
3. Wait for liquidity sweep (1H/15M)
4. Confirm MSS with displacement (15M/5M)
5. Enter at FVG in correct premium/discount zone
6. SL: beyond sweep point + 5-10 pip buffer
7. TP: nearest opposing liquidity | Min RR: 1:2

### Strategy B: Silver Bullet (Time-Based)
1. Pre-determine daily bias before window
2. Observe first 15 min of window (no entry)
3. Wait for displacement + FVG within the window
4. Entry before window closes | Min RR: 1:3

### Strategy C: Judas Swing (Reversal)
- False move at session open against daily bias
- Sweeps known liquidity, then reverses with displacement
- London: sweeps Asian range | NY: sweeps London extreme
- Enter from FVG after MSS confirmation | Min RR: 1:2

### Strategy D: Market Maker Models
- **MMBM (Buy)**: Consolidation > engineering SSL > reversal at HTF PD Array > targets BSL
- **MMSM (Sell)**: Consolidation > sweep BSL > displacement down > targets SSL
- Enter FVG/OB after MSS + SMT divergence | Min RR: 1:3

### Strategy E: Unicorn Model
- Breaker Block + FVG overlap = high-conviction entry zone
- OB fails > becomes Breaker > displacement creates FVG > overlap is the entry
- Min RR: 1:3

### Strategy F: ICT 2022 Entry Model
1. Daily bias + key levels + NY midnight range marked
2. Wait for liquidity sweep of midnight/Asian range
3. Confirm MSS on LTF (5M/3M/1M)
4. Enter at PD Array in correct zone | Min RR: 1:3

---

## Risk Management (Non-Negotiable Rules)

| Rule | Value |
|------|-------|
| Max risk per trade | 1% (0.5% first month live) |
| Max concurrent trades | 2 (same direction only) |
| Max daily loss | 3% (then STOP) |
| Max weekly loss | 5% (then STOP) |
| Consecutive losses | 2 = stop that session |
| Correlated pairs | Count as 1 trade at 1% combined |
| Max trades per day | 3 |

### Position Sizing
```
Position Size = (Account Balance x Risk%) / (SL Pips x Pip Value)
```

### Drawdown Protocol
- 3% daily: stop for day
- 5% weekly: stop for week + review journal
- 10% monthly: reduce to 0.5%, 1 week demo
- 15% from peak: stop live, backtest 50 more trades
- 20% from peak: full review, 1 month demo

---

## Trade Management

1. **Entry to TP1**: No SL movement, no adding to position
2. **At TP1**: Close 50-75%, move SL to breakeven
3. **After TP1**: Trail SL using LTF swing points
4. **Close triggers**: TP2 hit, opposing MSS on 15M, red-folder news, 3 PM EST (day trades), Friday 2 PM EST

---

## Confluence Scoring (Score Before Every Entry)

| Factor | Points |
|--------|--------|
| HTF Bias alignment | +2 |
| Killzone timing | +2 |
| Liquidity sweep confirmed | +2 |
| MSS/CHoCH confirmed | +2 |
| FVG entry | +1 |
| Order Block entry | +1 |
| OTE zone (62-79%) | +1 |
| Premium/Discount correct | +1 |
| SMT Divergence | +1 |
| NWOG alignment | +1 |

- **8-12**: Full risk (1%) | **5-7**: Half risk (0.5%) | **< 5**: NO TRADE
- **Hard requirements** (must have all 4): HTF bias + Killzone + Sweep + MSS = base 8

---

## IPDA & Weekly Profiles

### IPDA Look-Back Windows
- 20-day: short-term targets | 40-day: medium-term | 60-day: long-term

### NWOG (New Week Opening Gap)
- Friday close to Sunday open gap -- strong weekly magnet
- Track last 4 NWOGs + current

### Weekly Day Tendencies
- **Monday**: Range establishment, one weekly extreme often forms
- **Tuesday**: Most common for weekly low (bullish) or high (bearish)
- **Wednesday**: Pivot/reversal point
- **Thursday**: Expansion day -- strong conviction moves
- **Friday**: Profit-taking, close before weekend

---

## MQL5 Indicator Arsenal (Key Indicators)

### Market Structure & SMC
- `AdvanceSMC.mq5` -- Advanced SMC structure detection
- `Smart_Money_Algo_Pro_E5.mq5` -- CHOCH, OB, demand/supply
- `ICT_OB_BB_Detector_v3.mq5` -- Order Blocks & Breaker Blocks
- `SwingHL_Pro_v8_5.mq5` -- Professional swing high/low detection

### FVG Detection
- `SMC_FVG_Validator_v24b.mq5` -- FVG validation & filtering
- `SMC_FVG_ML_Optimized_v22.mq5` -- ML-optimized FVG detection
- `FVG_Trade_Analyzer_V3.mq5` -- FVG trade simulation with SL/TP

### Session & Killzone
- `ICT_SilverBullet_PRO.mq5` -- Silver Bullet pattern detection
- `London_Hunter_v21.20.mq5` -- London session breakout analysis
- `ICT_Unicorn_Model.mq5` -- Unicorn pattern identification

### Order Flow & Volume
- `MM_Ultimate_Pro_Analyzer.mq5` -- Volume delta, CVD, BOS/CHoCH, FVG, OB
- `OrderFlowAnalysis.mq5` -- Order flow analysis

### Multi-Symbol Scanning
- `MS_Breakout_Monitor_v94.mq5` -- 32+ symbol breakout monitoring
- `MS_London_Hunter_v21b.mq5` -- Multi-symbol London session scan
- `MS_NY_Breakout_Monitor_v1a.mq5` -- Multi-symbol NY breakout scan

### Recommended Setups per Strategy
- **A (MSS+FVG)**: AdvanceSMC + SMC_FVG_Validator_v24b + ICT_OB_BB_Detector_v3 + EnhancedRangeBox_Pro_v3
- **B (Silver Bullet)**: ICT_SilverBullet_PRO + SMC_FVG_Finder_v1a + London_Hunter_v21.20
- **C (Judas Swing)**: Smart_Money_Algo_Pro_E5 + SMC_FVG_Validator_v24b + EnhancedRangeBox_Pro_v3
- **D (Market Maker)**: MM_Ultimate_Pro_Analyzer + ICT_OB_BB_Detector_v3 + BreakerBlocks_v2
- **E (Unicorn)**: ICT_Unicorn_Model + BreakerBlocks_v2 + SMC_FVG_Validator_v24b

---

## Markets & Pairs

| Market | Instruments | Best Sessions |
|--------|------------|---------------|
| Forex | EUR/USD, GBP/USD, EUR/GBP, USD/CHF, USD/CAD | London, NY |
| Commodities | XAU/USD, XAG/USD | NY |
| Indices | NAS100, US30, SPX500 | NY |
| Crypto | BTC/USD, ETH/USD | All sessions |

### SMT Divergence Pairs
- EUR/USD <-> GBP/USD (positive) | ES/SPX <-> NAS100 (positive)
- XAU/USD <-> XAG/USD (positive) | DXY <-> EUR/USD (inverse)

---

## Key Abbreviations

| Abbr | Meaning |
|------|---------|
| PDH/PDL | Previous Day High/Low |
| PWH/PWL | Previous Week High/Low |
| AH/AL | Asian Range High/Low |
| EQH/EQL | Equal Highs/Lows |
| BSL/SSL | Buy-Side/Sell-Side Liquidity |
| FVG | Fair Value Gap |
| OB | Order Block |
| BB | Breaker Block |
| MSS | Market Structure Shift |
| BOS | Break of Structure |
| CHoCH | Change of Character |
| OTE | Optimal Trade Entry (62-79% Fib) |
| NWOG | New Week Opening Gap |
| AMD/PO3 | Accumulation-Manipulation-Distribution / Power of 3 |
| IPDA | Interbank Price Delivery Algorithm |
| IRL/ERL | Internal/External Range Liquidity |
| MMBM/MMSM | Market Maker Buy/Sell Model |
| SMT | Smart Money Technique (Divergence) |
| IFVG | Inverse Fair Value Gap |

---

## Pre-Trade Checklist (Every Trade)

```
[ ] 1. Daily bias: BULLISH / BEARISH (neutral = NO TRADE)
[ ] 2. Killzone active: London (2-5 AM) / NY (8:30-11 AM)
[ ] 3. No red-folder news within 30 min
[ ] 4. Liquidity sweep confirmed
[ ] 5. MSS confirmed (displacement + FVG)
[ ] 6. Entry at PD Array (FVG / OB / Breaker)
[ ] 7. Correct zone (discount for buys, premium for sells)
[ ] 8. RR >= minimum for strategy
[ ] 9. Risk <= 1% of account
[ ] 10. Confluence score >= 5
[ ] 11. Daily loss < 3%
[ ] 12. Consecutive losses < 2 this session

ALL CHECKED = EXECUTE | ANY FAIL = STAND ASIDE
```

---

## Daily Execution Routine

1. **Pre-Market (40 min before KZ)**: Check calendar, Weekly/Daily context, determine bias, mark levels (PDH/PDL/AH/AL/EQH/EQL), plan 3 scenarios (bullish/bearish/no-trade), set alerts
2. **During Killzone**: Alert triggers > 15M/5M charts > observe sweep > wait for MSS+FVG > check confluence > execute if score >= 5
3. **Post-Trade**: Journal every trade, review entry quality, update levels for tomorrow, close charts

---

## Backtesting & Progression

### Backtesting Targets (100 trades minimum per strategy)
- Win Rate > 45% | Avg RR > 1:2 | Expectancy > 0 | Profit Factor > 1.5 | Max DD < 15%

### Progression Path
1. **Weeks 1-2**: Education (study, identify concepts on charts, no trades)
2. **Weeks 3-6**: Backtest Strategy A on EUR/USD (100 trades)
3. **Weeks 7-10**: Demo trading (3 consecutive profitable weeks to proceed)
4. **Months 3-5**: Live at 0.5% risk (execution quality focus)
5. **Month 6+**: Scale to 1% after 3 profitable months
6. **Month 12+**: All 6 strategies, multi-symbol, 3-5% monthly target

---

## Source Files

| File | Description |
|------|-------------|
| `P1/ICT_MASTER_STRATEGY_PLAN.md` | Complete master reference |
| `P1/01_ict_core_concepts.md` | Core SMC concepts |
| `P1/02_ict_detailed_strategies.md` | Strategy summaries |
| `P1/03_ict_daily_routine.md` | Daily execution process |
| `P1/04_ict_risk_psychology.md` | Risk & psychology framework |
| `P1/subs/` | Deep-dive guides per topic |
