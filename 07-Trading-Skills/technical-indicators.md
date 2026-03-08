---
name: technical-indicators
description: >
  Complete reference for all major technical indicators including trend, momentum, volume, and
  volatility indicators with exact formulas, settings, signals, and multi-timeframe analysis.
  Covers Elliott Wave theory, harmonic patterns, and Market Profile / Auction Market Theory.
  USE FOR: moving averages SMA EMA DEMA TEMA HMA, MACD signals, ADX trend strength, Parabolic SAR,
  Ichimoku cloud components signals, RSI divergence failure swings, Stochastic oscillator, CCI,
  Williams %R, ROC, OBV on balance volume, VWAP bands, accumulation distribution, MFI money flow,
  CMF Chaikin, Volume Profile POC VAH VAL, Bollinger Bands %B bandwidth squeeze, ATR multipliers,
  Keltner Channels, Donchian Channels, multi-timeframe analysis, Elliott Wave rules guidelines,
  Fibonacci wave relationships, harmonic patterns ABCD Gartley Butterfly Bat Crab Shark Cypher,
  Market Profile auction market theory TPO.
---

# Technical Indicators

## 1. Trend Indicators

### Simple Moving Average (SMA)
```
SMA(n) = (P₁ + P₂ + ... + Pₙ) ÷ n

Key Levels:
  20 SMA  → Short-term trend (day trading)
  50 SMA  → Medium-term trend (swing trading)
  100 SMA → Medium-long trend
  200 SMA → Long-term trend (bull/bear market line)

Signals:
  Price > 200 SMA → Bullish bias
  Price < 200 SMA → Bearish bias
  Golden Cross: 50 SMA crosses above 200 SMA → Bullish
  Death Cross: 50 SMA crosses below 200 SMA → Bearish
```

### Exponential Moving Average (EMA)
```
EMA = Price × k + EMA(prev) × (1 − k)
k = 2 ÷ (n + 1)

EMA responds faster to recent price changes than SMA
Key Levels: 9, 21, 50, 100, 200 EMA
```

### Double Exponential MA (DEMA)
```
DEMA = 2 × EMA(n) − EMA(EMA(n))
→ Reduces EMA lag; smoother than EMA
```

### Triple Exponential MA (TEMA)
```
EMA1 = EMA(n)
EMA2 = EMA(EMA1)
EMA3 = EMA(EMA2)
TEMA = 3 × EMA1 − 3 × EMA2 + EMA3
→ Minimal lag; good for trending markets
```

### Hull Moving Average (HMA)
```
WMA1 = WMA(n/2) × 2
WMA2 = WMA(n)
Raw HMA = WMA1 − WMA2
HMA = WMA(√n, Raw HMA)

→ Near-zero lag; very smooth; best for trend following
Crossover signals less whipsaw than EMA
```

### MA Signal System
| Condition | Signal |
|-----------|--------|
| Price > all MAs, MAs aligned up | Strong uptrend |
| Price < all MAs, MAs aligned down | Strong downtrend |
| Price crosses above 20 EMA | Short-term bullish |
| 9 EMA crosses above 21 EMA | Momentum shift bullish |
| 50 EMA crosses above 200 EMA (Golden Cross) | Long-term bullish |
| MAs converging / flat | Choppy, ranging market |

---

### MACD (Moving Average Convergence Divergence)
```
Standard Settings: 12, 26, 9

MACD Line = EMA(12) − EMA(26)
Signal Line = EMA(9) of MACD Line
Histogram = MACD Line − Signal Line

Signals:
1. Signal Line Crossover:
   MACD crosses above Signal → Bullish entry
   MACD crosses below Signal → Bearish entry

2. Zero Line Cross:
   MACD crosses above 0 → Bullish (trend confirmation)
   MACD crosses below 0 → Bearish

3. Histogram Divergence:
   Price makes new high, histogram lower → Bearish divergence
   Price makes new low, histogram higher → Bullish divergence

4. Centerline Strategies:
   Buy pullbacks to 0 line in uptrend
   Sell rallies to 0 line in downtrend

Best Timeframes: Daily for swing, 1h for day trading
Weakness: Lagging indicator; poor in ranging markets
```

---

### ADX (Average Directional Index)
```
ADX measures TREND STRENGTH (not direction)
Range: 0–100

Calculation:
  +DM = Current High − Previous High (if positive)
  −DM = Previous Low − Current Low (if positive)
  TR = max(High−Low, |High−PrevClose|, |Low−PrevClose|)
  +DI = 100 × EMA(+DM) ÷ EMA(TR)
  −DI = 100 × EMA(−DM) ÷ EMA(TR)
  DX = 100 × |+DI − −DI| ÷ (+DI + −DI)
  ADX = EMA(DX, 14)

ADX Interpretation:
  < 20  → Weak/absent trend (ranging market)
  20–25 → Trend beginning to form
  25–40 → Moderate trend (use trend-following strategies)
  40–60 → Strong trend
  60+   → Very strong trend (potential exhaustion watch)

Direction via DI Lines:
  +DI > −DI → Uptrend
  −DI > +DI → Downtrend
  +DI crosses above −DI → Bullish signal
  −DI crosses above +DI → Bearish signal

Best Use: Filter for trend-following strategies
Only use breakout/trend strategies when ADX > 25
```

---

### Parabolic SAR
```
Settings: Step = 0.02, Max = 0.20

Interpretation:
  Dots below price → Uptrend; use as trailing stop
  Dots above price → Downtrend; use as trailing stop
  Price crosses dots → Trend reversal signal

Formula:
  Rising SAR(t) = SAR(t-1) + AF × (EP − SAR(t-1))
  AF starts at 0.02, increases by 0.02 each new high, max 0.20
  EP = Extreme point (highest high in uptrend)

Use:
  ✓ Excellent trailing stop in strong trends
  ✓ Clear visual signals
  ✗ Poor in sideways/choppy markets (whipsaws)
  
Best combined with: ADX > 25 to confirm trending condition
```

---

### Ichimoku Cloud (Ichimoku Kinko Hyo)

#### Five Components
```
1. Tenkan-sen (Conversion Line) = (9H + 9L) ÷ 2
   → 9-period midpoint; short-term trend

2. Kijun-sen (Base Line) = (26H + 26L) ÷ 2
   → 26-period midpoint; medium-term trend/support

3. Senkou Span A (Leading A) = (Tenkan + Kijun) ÷ 2, plotted 26 periods AHEAD
   → Forms top or bottom of Cloud (Kumo)

4. Senkou Span B (Leading B) = (52H + 52L) ÷ 2, plotted 26 periods AHEAD
   → Forms other edge of Cloud

5. Chikou Span (Lagging Span) = Current Close, plotted 26 periods BEHIND
   → Confirms trend; most important confirmation tool
```

#### Cloud (Kumo) Interpretation
```
Price ABOVE Cloud → Bullish (trend bias = long)
Price BELOW Cloud → Bearish (trend bias = short)
Price INSIDE Cloud → Neutral / Consolidation

Green Cloud (Span A > Span B) → Bullish sentiment
Red Cloud (Span B > Span A) → Bearish sentiment

Thick Cloud → Strong support/resistance
Thin Cloud → Weak support/resistance (easier to break through)
```

#### Ichimoku Signals
| Signal | Condition | Strength |
|--------|-----------|----------|
| **TK Cross Bullish** | Tenkan crosses above Kijun | Moderate |
| **TK Cross Bearish** | Tenkan crosses below Kijun | Moderate |
| **Strong Bullish** | TK cross above Cloud + Chikou above price | Strong |
| **Strong Bearish** | TK cross below Cloud + Chikou below price | Strong |
| **Cloud Support** | Price pullback to top of Cloud holds | Bullish |
| **Cloud Resistance** | Price rally to bottom of Cloud fails | Bearish |
| **Kumo Twist** | Cloud changes from red to green ahead | Bullish shift |
| **Chikou Confirm** | Chikou in open space (no obstruction) | Confirmation |

#### Perfect Ichimoku Buy Setup
```
All 5 criteria must be met:
  ✓ Price above Cloud
  ✓ Cloud is green (Span A > Span B)
  ✓ Tenkan above Kijun
  ✓ Chikou above price from 26 periods ago
  ✓ Price pulling back to Tenkan/Kijun for entry
```

---

## 2. Momentum Indicators

### RSI (Relative Strength Index)
```
Settings: 14 periods (default)

RSI = 100 − (100 ÷ (1 + RS))
RS = Average Gain ÷ Average Loss (over 14 periods)

Levels:
  RSI > 70 → Overbought (potential reversal short)
  RSI < 30 → Oversold (potential reversal long)
  RSI = 50 → Midpoint (trend confirmation)
  
Trend Trading:
  RSI 40–90 range in uptrends (buy dips to 40–50)
  RSI 10–60 range in downtrends (sell rallies to 50–60)
```

#### RSI Divergence
```
Regular Bullish Divergence:
  Price: Lower Low → Lower Low
  RSI:   Lower Low → HIGHER Low
  Signal: Bullish reversal

Regular Bearish Divergence:
  Price: Higher High → Higher High
  RSI:   Higher High → LOWER High
  Signal: Bearish reversal

Hidden Bullish Divergence (Continuation):
  Price: Higher Low
  RSI:   Lower Low
  Signal: Uptrend continuation (buy the dip)

Hidden Bearish Divergence (Continuation):
  Price: Lower High
  RSI:   Higher High
  Signal: Downtrend continuation (sell the rally)
```

#### RSI Failure Swings
```
Bullish Failure Swing (Strong Signal):
  1. RSI falls below 30 (oversold)
  2. RSI bounces above 30
  3. RSI pulls back but STAYS ABOVE 30 (failure)
  4. RSI breaks above recent peak → BUY SIGNAL

Bearish Failure Swing:
  1. RSI rises above 70 (overbought)
  2. RSI dips below 70
  3. RSI bounces but STAYS BELOW 70 (failure)
  4. RSI breaks below recent trough → SELL SIGNAL
```

---

### Stochastic Oscillator
```
Settings: %K=14, %D=3, Smooth=3

Fast Stochastic:
  %K = (Current Close − Lowest Low) ÷ (Highest High − Lowest Low) × 100
  %D = 3-period SMA of %K

Slow Stochastic (recommended):
  Slow %K = Fast %D
  Slow %D = 3-period SMA of Slow %K

Levels:
  Above 80 → Overbought
  Below 20 → Oversold

Signals:
  %K crosses above %D in oversold territory → Buy
  %K crosses below %D in overbought territory → Sell
  Divergence with price → Reversal warning
  
Stochastic RSI: Applies RSI formula to Stochastic → more sensitive
```

---

### CCI (Commodity Channel Index)
```
Settings: 14 or 20 periods

CCI = (Typical Price − SMA) ÷ (0.015 × Mean Deviation)
Typical Price = (High + Low + Close) ÷ 3

Levels:
  > +100 → Overbought / Strong trend (buy in strong uptrend)
  < −100 → Oversold / Strong downtrend (sell in downtrend)
  0 line → Neutral

Signals:
  Crosses above +100 → Bullish breakout
  Crosses below −100 → Bearish breakout
  Returns to 0 from extreme → Possible reversal
  Divergence → Leading reversal signal

Use: Good for cyclical markets; works well on commodities
```

---

### Williams %R
```
Settings: 14 periods

%R = (Highest High − Close) ÷ (Highest High − Lowest Low) × (−100)

Range: 0 to −100 (note: inverted scale)
  0 to −20   → Overbought
  −80 to −100 → Oversold

Signals (similar to Stochastic):
  Exit from overbought (below −20) → Sell
  Exit from oversold (above −80) → Buy
  Divergence → Reversal signal
  
Note: Very similar to Stochastic; choose one, not both
```

---

### Rate of Change (ROC)
```
Settings: 12 periods (daily), 9 (weekly)

ROC = ((Close − Close[n]) ÷ Close[n]) × 100

Signals:
  ROC > 0 → Upward momentum
  ROC < 0 → Downward momentum
  Zero line cross → Momentum shift
  Divergence → Reversal warning
  
Use: Relative Strength comparison across assets; momentum ranking
```

---

## 3. Volume Indicators

### OBV (On-Balance Volume)
```
If Close > Previous Close: OBV = OBV(prev) + Volume
If Close < Previous Close: OBV = OBV(prev) − Volume
If Close = Previous Close: OBV = OBV(prev)

Interpretation:
  OBV rising + Price rising → Confirmed uptrend
  OBV falling + Price falling → Confirmed downtrend
  OBV rising + Price flat → Accumulation (bullish)
  OBV falling + Price flat → Distribution (bearish)
  OBV diverges from price → Reversal warning

Key Insight: OBV should CONFIRM price action; divergence = warning
```

---

### VWAP (Volume-Weighted Average Price)
```
VWAP = Σ(Typical Price × Volume) ÷ Σ Volume
Resets each trading session

VWAP Bands (Standard Deviation bands):
  VWAP ± 1 SD → Contains ~68% of price action
  VWAP ± 2 SD → Contains ~95% of price action
  VWAP ± 3 SD → Extreme deviation (mean reversion opportunity)

Trading Strategies:
  Above VWAP → Bullish; buy pullbacks to VWAP
  Below VWAP → Bearish; sell rallies to VWAP
  
  Institutional benchmark: Many algos and funds use VWAP
  Price above VWAP = Buyers in control
  Price below VWAP = Sellers in control

Day Trading Use:
  Open above VWAP → Long bias
  VWAP as support → Buy at VWAP, stop below
  VWAP as resistance → Sell at VWAP, stop above

Mean Reversion:
  Price at ±2 SD → Fade toward VWAP
  Price at ±3 SD → Strong mean reversion signal
```

---

### Accumulation/Distribution Line (A/D)
```
Money Flow Multiplier = ((Close − Low) − (High − Close)) ÷ (High − Low)
Money Flow Volume = MFM × Volume
A/D = Previous A/D + Current Money Flow Volume

Interpretation:
  A/D rising → Accumulation (buying pressure)
  A/D falling → Distribution (selling pressure)
  Divergence from price → Strong reversal signal

Key: Accounts for WHERE close is within bar's range
```

---

### MFI (Money Flow Index)
```
Settings: 14 periods

Typical Price = (H + L + C) ÷ 3
Money Flow = Typical Price × Volume
Positive MF: TP > Previous TP
Negative MF: TP < Previous TP

MFI = 100 − (100 ÷ (1 + (14-day Positive MF ÷ 14-day Negative MF)))

Levels:
  > 80 → Overbought
  < 20 → Oversold

Think of MFI as "Volume-Weighted RSI"
Divergence more significant due to volume confirmation
```

---

### CMF (Chaikin Money Flow)
```
Settings: 20 periods

CMF = 20-period Sum of (Money Flow Volume) ÷ 20-period Sum of Volume
Money Flow Volume = ((Close−Low) − (High−Close)) ÷ (High−Low) × Volume

Range: −1 to +1
  > 0 → Buying pressure; bullish
  < 0 → Selling pressure; bearish
  > +0.25 → Strong buying
  < −0.25 → Strong selling

Use: Confirm breakouts and trend direction
```

---

### Volume Profile
```
Key Levels:
  POC (Point of Control) → Price level with MOST volume traded
  VAH (Value Area High) → Upper boundary of Value Area
  VAL (Value Area Low) → Lower boundary of Value Area
  Value Area → Contains 68–70% of total session volume

Types:
  Session VP → Volume profile for single session
  Fixed Range VP → User-defined time range
  Visible Range VP → Current chart view
  Composite VP → Multiple sessions combined

Trading Applications:
  POC as Magnet: Price tends to return to POC
  VAH Resistance: Price often rejects at VAH
  VAL Support: Price often holds at VAL
  High Volume Node (HVN) → Strong S/R; price may consolidate
  Low Volume Node (LVN) → Price moves through quickly (gap fill areas)

Strategy Examples:
  Long: Price enters Value Area from below → Target POC, then VAH
  Short: Price enters Value Area from above → Target POC, then VAL
  Breakout: Price breaks above VAH with volume → Target measured move
```

---

## 4. Volatility Indicators

### Bollinger Bands
```
Settings: 20 SMA, ±2 Standard Deviations

Upper Band = 20 SMA + (2 × SD)
Middle Band = 20 SMA
Lower Band = 20 SMA − (2 × SD)

Key Metrics:
  %B = (Price − Lower Band) ÷ (Upper Band − Lower Band)
    %B > 1 → Price above upper band
    %B = 0.5 → Price at middle band
    %B < 0 → Price below lower band

  Bandwidth = (Upper − Lower) ÷ Middle × 100
    Expanding → Increasing volatility
    Contracting → Decreasing volatility (squeeze = explosive move incoming)

BB Squeeze:
  Bandwidth at 6-month low → Imminent breakout
  Direction of breakout confirmed by volume and price action

Strategies:
  Mean Reversion: Buy lower band, sell upper band (ranging markets only)
  Trend Following: Price rides upper band = uptrend; sell first close inside band
  Squeeze: Enter breakout direction with momentum confirmation
  W-Bottom: Two touches of lower band; second higher → bullish reversal
  M-Top: Two touches of upper band; second lower → bearish reversal
```

---

### ATR (Average True Range)
```
Settings: 14 periods (standard)

True Range = max(High−Low, |High−PrevClose|, |Low−PrevClose|)
ATR = EMA(True Range, 14)

ATR Multipliers for Stop Loss:
  Conservative: 2.0× ATR
  Standard: 2.5× ATR
  Aggressive: 1.5× ATR
  Volatile markets: 3.0× ATR

ATR Position Sizing:
  Dollar Risk ÷ (ATR × Multiplier) = Number of Shares/Contracts

ATR-Based Targets:
  Target 1: 1.5× ATR from entry
  Target 2: 3.0× ATR from entry
  Target 3: 5.0× ATR from entry

ATR Channel:
  Upper = Price + (1.5 × ATR)
  Lower = Price − (1.5 × ATR)
  Price outside channel = volatility expansion
```

---

### Keltner Channels
```
Settings: EMA=20, ATR=10, Multiplier=2

Middle Line = 20 EMA
Upper Channel = 20 EMA + (2 × ATR)
Lower Channel = 20 EMA − (2 × ATR)

Signals:
  Price above upper channel → Strong uptrend / overbought
  Price below lower channel → Strong downtrend / oversold
  Price re-enters from upper → Potential reversal
  
Combined with Bollinger Bands:
  BB inside Keltner Channels → SQUEEZE (low volatility)
  BB outside Keltner Channels → Expansion phase
  Squeeze + Momentum direction → Best breakout setups
```

---

### Donchian Channels
```
Settings: 20 periods (day), 55 periods (Turtle Trading)

Upper = Highest High of n periods
Lower = Lowest Low of n periods
Middle = (Upper + Lower) ÷ 2

Turtle Trading System:
  Entry: Price breaks 55-period Donchian high/low
  Exit: Price breaks 20-period Donchian in opposite direction
  Stop: 2× ATR from entry
  
Breakout Signals:
  New 20-day high → Short-term bullish
  New 55-day high → Longer-term bullish breakout
  New 52-week high → Major bullish breakout signal
```

---

## 5. Multi-Timeframe Analysis Framework

### The 3-Timeframe System
```
For Each Trading Style:

Day Trading:
  Higher TF: Daily (trend bias)
  Middle TF: 1-hour (setup confirmation)
  Lower TF: 15-minute (entry timing)

Swing Trading:
  Higher TF: Weekly (trend bias)
  Middle TF: Daily (setup confirmation)
  Lower TF: 4-hour (entry timing)

Scalping:
  Higher TF: 15-minute (trend bias)
  Middle TF: 5-minute (setup)
  Lower TF: 1-minute (entry timing)
```

### MTF Analysis Process
```
Step 1: Higher TF → Determine primary trend direction
  Is price above/below key MAs?
  What phase is the market in?
  Are we at key HTF support/resistance?

Step 2: Middle TF → Find setup
  Is there a pullback in direction of HTF trend?
  Is a pattern forming at key level?
  Are momentum indicators aligned?

Step 3: Lower TF → Time entry
  Look for trigger candle at LTF level
  Entry after confirmation of reversal
  Set stop just beyond LTF structure
```

---

## 6. Elliott Wave Theory

### Elliott Wave Rules (MUST be satisfied)
```
5-wave Impulse:
  Rule 1: Wave 2 NEVER retraces more than 100% of Wave 1
  Rule 2: Wave 3 is NEVER the shortest impulse wave
  Rule 3: Wave 4 NEVER overlaps into Wave 1 price territory
           (Exception: Diagonal triangles in Wave 1 or 5)
```

### Elliott Wave Guidelines
```
Wave 1: Often muted; not widely recognized
Wave 2: Typically 50–61.8% retracement of Wave 1
Wave 3: Longest and strongest; 161.8% of Wave 1 common
Wave 4: Typically 38.2% retracement of Wave 3
Wave 5: Often equals Wave 1 in length; or 61.8% of W1+W3

Corrective Waves (A-B-C):
  Zigzag: Sharp correction (5-3-5)
  Flat: Sideways correction (3-3-5)
  Triangle: Converging correction (3-3-3-3-3)
  Complex: Combination of above (X waves connecting)
```

### Fibonacci Relationships in Elliott
| Wave | Typical Fibonacci Relationship |
|------|-------------------------------|
| Wave 2 | 50%, 61.8% retrace of Wave 1 |
| Wave 3 | 161.8%, 261.8% of Wave 1 |
| Wave 4 | 38.2% retrace of Wave 3 |
| Wave 5 | 61.8% or 100% of Wave 1 |
| Wave A | 100% of Wave 5 often |
| Wave B | 50–78.6% retrace of Wave A |
| Wave C | 100%, 161.8% of Wave A |

---

## 7. Harmonic Patterns

### ABCD Pattern
```
AB = CD (time and price symmetry)
BC: 61.8% or 78.6% of AB
CD: 127.2% or 161.8% of BC

Bullish ABCD: Buy at D
Bearish ABCD: Sell at D
Stop: Beyond D by structure
Target: B level (38.2% and 61.8% of AD)
```

### Gartley Pattern
```
XA: Initial move
AB: 61.8% retrace of XA
BC: 38.2–88.6% retrace of AB
CD: 78.6% retrace of XA (PRZ = Potential Reversal Zone)
Note: BC can project 127.2–161.8% to locate D

Bullish Gartley: Buy at D (78.6% of XA)
Stop: Below X
Target 1: 61.8% of CD
Target 2: 127.2% of CD
Reliability: 65–70%
```

### Butterfly Pattern
```
XA: Initial move
AB: 78.6% retrace of XA
BC: 38.2–88.6% retrace of AB
CD: 127.2% OR 161.8% extension of XA (beyond X)
PRZ: 127.2–161.8% of XA

Reliability: 70–75%
Note: D extends BEYOND X (unlike Gartley)
```

### Bat Pattern
```
AB: 38.2–50% retrace of XA (key differentiator from Gartley)
BC: 38.2–88.6% retrace of AB
CD: 88.6% retrace of XA (PRZ)

Reliability: 72–78%
Tighter stops than Gartley; high accuracy
```

### Crab Pattern
```
AB: 38.2–61.8% retrace of XA
BC: 38.2–88.6% retrace of AB
CD: 161.8% extension of XA (deepest extension)
PRZ: 161.8% of XA

Reliability: 65–70%
Most extreme extension; use tight stops
```

### Shark Pattern
```
Initial 0X move
X to A: Any move
A to B: 113% extension of 0A
B to C: 88.6% retrace of 0B or 161.8% of AB
PRZ at C: 88.6% of 0X or 113% of XA
```

### Cypher Pattern
```
XA: Initial move
AB: 38.2–61.8% retrace of XA
BC: 127.2–141.4% extension of XA
CD: 78.6% retrace of XC (PRZ)

Reliability: 70–75%
```

### Harmonic Pattern Trading Rules
```
Entry: At PRZ (Potential Reversal Zone)
Confirmation: Wait for reversal candle at PRZ
Stop: Beyond the extreme of pattern (D or X depending on pattern)
Target 1: 38.2% retrace of CD
Target 2: 61.8% retrace of CD  
Target 3: Full retracement to AB or beyond

Risk Management: Risk 1–1.5% per harmonic trade
Timeframes: Best on 1h, 4h, Daily charts
```

---

## 8. Market Profile / Auction Market Theory

### Key Concepts
```
TPO (Time Price Opportunity): Letter assigned to each price traded in a given period
Initial Balance (IB): Price range of first 1 hour; sets the day's range expectation
Value Area: Price range containing 70% of volume/TPOs
POC: Most frequently traded price
```

### Market Profile Day Types
| Day Type | Characteristics | Trading Approach |
|----------|----------------|-----------------|
| **Normal** | Opens, finds value near open | Range trade IB extremes |
| **Normal Variation** | Breaks IB in one direction | Trade breakout direction |
| **Trend Day** | Strong directional move; range expands all day | Trend follow; don't fade |
| **Double Distribution** | Two distinct value areas | Trade between distributions |
| **Neutral** | Balanced; rotates but no breakout | Fade extremes |
| **Spike and Distribution** | Gap + auction finding value | Trade inside distribution |

### Auction Market Theory Principles
```
1. Markets are always in the process of facilitating trade
2. Price moves to FIND responsive buyers and sellers
3. Price moves AWAY from value to advertise opportunity
4. When price finds two-sided trade, it consolidates (value)
5. When price fails to find trade, it moves away (trend)

Auction Phases:
  Initiation → Price moves to discover new value
  Responsive → Participants respond at extremes (mean reversion)
  Facilitation → Price rotates within value area

Trading Signals:
  Price above prior day VAH → Bullish; long opportunities
  Price below prior day VAL → Bearish; short opportunities
  Price returns to prior POC → Magnet effect
  Price breaks out of prior day range + volume → Trending day
```

### Market Profile vs. Volume Profile
| Feature | Market Profile | Volume Profile |
|---------|---------------|---------------|
| Unit | TPO (time) | Volume |
| POC | Most TIME spent | Most VOLUME traded |
| Data need | TPO letters | Actual volume by price |
| Best use | Auction analysis | Liquidity analysis |
| Preference | Futures traders | Stock/equity traders |
