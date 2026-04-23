# Tradecraft — Commands Reference

Every skill in Tradecraft is invoked as `/tradecraft:<skill-name>`. Total: **165** skills across **6** domains (plus 12 currently uncategorized).

To install, see [INSTALL.md](INSTALL.md). To browse by domain, jump to:

- [Trading](#trading) (101)
- [AI Development](#ai-development) (7)
- [Software Engineering](#software-engineering) (20)
- [Claude Code Platform](#claude-code-platform) (19)
- [Data Acquisition](#data-acquisition) (4)
- [Domain Specific](#domain-specific) (2)
- [Uncategorized](#uncategorized) (12)

---

## Trading

| Command | Description |
|---|---|
| `/tradecraft:ai-signal-aggregator` | ML-powered signal aggregation across ALL strategy skills — combines signals from every strategy using weighted voting, random forest meta-learner, and confidence calibration. THE MASTER SIGNAL COMBINER. Use for "combi... |
| `/tradecraft:ai-trading-crew` | AI Trading Crew — 50-agent AutoGen system for US stock analysis. 8 specialized teams (Technical, Fundamental, Macro, Sentiment, Quant, Risk, Execution, Strategy) reporting to a Head Coach supervisor. Risk team has vet... |
| `/tradecraft:alternative-data-integrator` | Alternative data sources for trading signals — Google Trends, web traffic, search volume, shipping/supply chain data, satellite imagery proxies, and economic nowcasting. Use this skill whenever the user asks about "al... |
| `/tradecraft:analyze` | Instant full trading analysis — just type a symbol. Auto-detects asset class, timeframe, and runs the complete 18-phase master workflow. Use for ANY ticker/symbol like "EURUSD", "AAPL", "BTCUSD", "XAUUSD", "SPY", "NQ"... |
| `/tradecraft:analyze-gold` | Pre-configured combination command for gold (XAUUSD) analysis. Runs the full pair-analyze pipeline tuned for gold's volatility profile, session behavior, and dollar sensitivity. USE FOR - analyze gold, analyze XAUUSD,... |
| `/tradecraft:analyze-us30` | Pre-configured combination command for US30 (Dow Jones Industrial Average CFD) analysis. Runs the full pair-analyze pipeline tuned for US30's session-driven flow, earnings sensitivity, and Fed-rate reactivity. USE FOR... |
| `/tradecraft:asian-session-scalper` | Tokyo session low-volatility scalping setups — range-bound strategies for the quietest session. Use for "Asian scalp", "Tokyo session trade", "Asian range", "night scalping", "low vol scalp", "Asian session strategy",... |
| `/tradecraft:backtest-report-generator` | Generates publication-quality backtest reports with equity curves, Monte Carlo simulations, tearsheets, and comprehensive risk analysis. Use this skill whenever the user asks to "generate a backtest report", "create t... |
| `/tradecraft:backtesting-sim` | Backtesting and simulation: vectorized backtesting, paper trading simulation, strategy A/B testing, automated strategy building, natural language to strategy, and trading plan generation. USE FOR: backtest, backtestin... |
| `/tradecraft:borsellino-10-commandments` | Lewis Borsellino's 10 Commandments of Trading — the discipline framework from the largest S&P pit trader in Chicago history ($4.7M in one day, 10% of S&P volume, 20 years without a losing year). Covers trading for suc... |
| `/tradecraft:breakout-strategy-engine` | Pre-built breakout strategy templates — volatility squeeze detection, range breakout, momentum breakout with confirmation filters. Use this skill whenever the user asks about "breakout strategy", "Bollinger squeeze", ... |
| `/tradecraft:capitulation-mean-reversion` | Lance Breitstein's $100M+ capitulation mean reversion framework — 7-variable checklist, slope analysis for waterfalls, "Right Side of the V" entry method, multi-variable mental rubric scoring, and prior-bar-highs/lows... |
| `/tradecraft:chart-vision` | Complete chart vision pipeline — render charts, preprocess images, detect candlestick patterns, detect classical chart patterns, detect trendlines and S/R levels, and annotate results back onto charts. Use this skill ... |
| `/tradecraft:correlation-crisis` | Correlation breakdown during crises, tail risk measurement (VaR, CVaR, fat tails), regime-dependent correlation matrices, hedging strategies by volatility regime, and stress testing protocols. Use for correlation cris... |
| `/tradecraft:correlation-regime-switcher` | Automatically switches strategy sets when correlation regimes change. Use this skill whenever the user asks about "correlation regime change", "adaptive strategy switching", "when correlations break", "regime-based st... |
| `/tradecraft:cross-asset-arbitrage-engine` | Statistical arbitrage, triangular arbitrage, basis trades, and convergence detection across instruments. Use this skill whenever the user asks about "arbitrage", "stat arb", "pairs trading", "triangular arbitrage", "c... |
| `/tradecraft:cross-asset-relationships` | Cross-asset and quantitative analysis: pair correlations, correlation heatmaps, currency strength, cross-timeframe divergence, intermarket analysis, market breadth, carry trades, swap rates, risk premia, and multi-pai... |
| `/tradecraft:crypto-defi-trading` | Crypto and DeFi trading: DEX analysis (Uniswap, SushiSwap, Curve), on-chain analytics, MEV detection, impermanent loss, yield farming metrics, DeFi risk analysis, token metrics, liquidity pool analysis, whale tracking... |
| `/tradecraft:dan-zanger-breakout-strategy` | Dan Zanger's complete breakout trading strategy - the system that turned $10,775 into $42 million in 23 months. Chart pattern breakouts with volume confirmation and strict risk management. |
| `/tradecraft:discord-webhook` | Send trading alerts, signals, and analysis summaries to Discord via webhook. Integrates with realtime-alert-pipeline, trading-brain, and trade-journal-analytics. |
| `/tradecraft:drawdown-playbook` | Drawdown taxonomy, tiered response protocols (caution to emergency), equity curve health analysis, recovery mathematics, and pre-drawdown preparation. Use for drawdown, equity curve, max drawdown, recovery protocol, d... |
| `/tradecraft:economic-calendar` | Economic calendar data: high-impact event detection, news avoidance windows, pre-event volatility expansion, post-event fade, event-driven trade setup. USE FOR: economic calendar, economic events, news events, NFP, CP... |
| `/tradecraft:economic-indicator-tracker` | Track leading, lagging, and coincident economic indicators systematically. Use for "economic indicators", "leading indicator", "lagging indicator", "PMI tracker", "GDP tracker", "jobs data", "inflation tracker", "econ... |
| `/tradecraft:elliott-wave-engine` | Elliott Wave counting and forecasting — impulse waves, corrective patterns, wave degree. Use for "Elliott Wave", "wave count", "impulse wave", "corrective wave", "wave 3", "wave 5", "ABC correction", "wave analysis", ... |
| `/tradecraft:equities-trading` | Equities and stock CFD trading: NYSE/NASDAQ sessions, stock-specific mechanics, earnings impact, sector rotation, index correlation, gap trading, opening range. USE FOR: stocks, equities, stock CFD, NYSE, NASDAQ, earn... |
| `/tradecraft:execution-algo-trading` | Institutional execution algorithms: TWAP, VWAP, Implementation Shortfall, POV, Iceberg orders, slippage analysis, market impact, and TCA. USE FOR: execution, TWAP, VWAP, implementation shortfall, slippage, market impa... |
| `/tradecraft:fetch-quotes` | Cascading market-data fetcher. Prefers yfinance (free, no credentials) and falls back to a local MT5 terminal when available for broker-exact pricing. Returns OHLCV bars plus a latest quote as JSON, optionally with a ... |
| `/tradecraft:fibonacci-harmonic-wave` | Fibonacci retracement/extension levels, harmonic pattern detection (Gartley, Butterfly, Bat, Crab, Cypher, Shark), and Elliott Wave counting with Python engines. Use for Fibonacci levels, harmonic pattern, Elliott Wav... |
| `/tradecraft:forex-trading` | Forex market specifics: major/minor/exotic pairs, currency pair mechanics, pip values, lot sizes, swap/rollover, session overlaps, carry trades, central bank impact. USE FOR: forex pairs, currency pairs, pip value, lo... |
| `/tradecraft:freqtrade-bot` | Freqtrade — open-source Python crypto trading bot. Backtesting, hyperopt (ML parameter optimization), FreqAI (self-training adaptive strategies), Telegram + WebUI control. Supports Binance, Kraken, Bybit, OKX, Gate.io... |
| `/tradecraft:futures-trading` | Futures markets: contract specs, margin, rollover dates, commodity futures, index futures, interest rate futures, contango/backwardation, basis risk. USE FOR: futures contract, futures margin, rollover, expiry, contan... |
| `/tradecraft:gap-trading-strategy` | Gap trading — opening gaps, gap fill probability, gap-and-go, fade the gap. Use for "gap trading", "opening gap", "gap fill", "gap and go", "fade the gap", "Sunday gap", "weekend gap", "gap statistics", "gap probabili... |
| `/tradecraft:gold-orb-ea` | GOLD_ORB — MQL5 Expert Advisor for XAUUSD 1H Opening Range Breakout. Identifies opening range (first 1H candle after 1:02 AM server time), confirms consolidation (min 3 candles), then trades breakouts. Buy signal on r... |
| `/tradecraft:grid-trading-engine` | Systematic grid trading — place buy/sell orders at fixed intervals across a price range. Use for "grid trading", "grid bot", "grid strategy", "buy the dips grid", "DCA grid", "range grid", "grid order placement", or a... |
| `/tradecraft:harmonic-pattern-engine` | Harmonic pattern detection — Gartley, Butterfly, Bat, Crab, Cypher, Shark with Fibonacci ratio validation. Use for "harmonic pattern", "Gartley", "Butterfly pattern", "Bat pattern", "Crab pattern", "Cypher", "XABCD", ... |
| `/tradecraft:hurst-exponent-dynamics-crisis-prediction` | Mark Vogel's Oxford ISF Conference research on rolling-window Hurst exponent dynamics of wavelet-denoised S&P 500 returns (2000-2020). Covers the chaos analysis framework, cascadic wavelet denoising, recurrence quanti... |
| `/tradecraft:ict-smart-money` | ICT (Inner Circle Trader) Smart Money Concepts — full methodology reference by Michael J. Huddleston. Covers market structure (BOS/CHoCH/MSS), order blocks, smart money traps, supply/demand zones, Wyckoff method, inst... |
| `/tradecraft:ict-trading-tool` | Automated MT5 trading tool using ICT Smart Money Concepts. Scans 21 instruments, scores setups (0-12), generates charts, executes and monitors trades. Use for ICT scanner, MT5 automated trading, scan for ICT setups, o... |
| `/tradecraft:institutional-timeline` | Central bank policy tracking, COT positioning analysis, FX intervention detection, and event timeline linking with causal chain analysis. Use for central bank, COT report, institutional flow, FX intervention, policy d... |
| `/tradecraft:jdub-price-action-strategy` | Jdub Trades' 3-step price action framework: Direction, Location, Execution. Three-bar confirmation entry pattern (lead, reaction, confirmation candle). Key POIs: old highs/lows, PDH/PDL, opening print/previous day clo... |
| `/tradecraft:liquidity-analysis` | Advanced liquidity analysis: pool identification, institutional flow detection, DOM/orderbook reading, volume concentration mapping, dark pool activity, micro-structure signals, real-time liquidity monitoring, slippag... |
| `/tradecraft:macro-economic-dashboard` | Macro economic inter-market analysis dashboard — DXY, VIX, yield curves, bond spreads, commodity flows, and cross-asset correlations. Use this skill whenever the user asks about "DXY", "dollar index", "VIX", "volatili... |
| `/tradecraft:market-breadth-analyzer` | Market breadth — how many pairs trending vs ranging, overall market health, breadth divergence. Use for "market breadth, breadth scan, market health, how many trending, broad market, pairs trending", or any related qu... |
| `/tradecraft:market-data-ingestion` | Market data ingestion pipelines: OHLCV data fetching from MT5, yfinance, Alpha Vantage, data cleaning, normalization, missing bar handling, multi-symbol batch fetching. USE FOR: market data, OHLCV, fetch data, downloa... |
| `/tradecraft:market-impact-model` | Estimate your own orders' market impact and optimize execution for larger accounts. Use this skill whenever the user asks about "market impact", "slippage model", "order impact", "large order execution", "TWAP", "VWAP... |
| `/tradecraft:market-intelligence` | Complete market intelligence layer — macro analysis, regime classification, news impact, sentiment, institutional behavior, event timelines, pair correlations, and trading fundamentals. Includes NLP sentiment scoring,... |
| `/tradecraft:market-making-hft` | Market making and high-frequency trading: quote generation, inventory management, order book analysis, latency tracking, microstructure signals, spoofing detection, optimal execution (TWAP/VWAP), Avellaneda-Stoikov mo... |
| `/tradecraft:market-regime-classifier` | ML-powered market regime classification — trending, ranging, volatile, quiet. Automatically adapts strategy selection based on detected regime. Use this skill whenever the user asks "is the market trending", "what reg... |
| `/tradecraft:market-structure-bos-choch` | Market structure analysis — Break of Structure (BOS), Change of Character (CHoCH), premium/ discount, market structure shifts, and candle-close swing validation (Jonathan Jarvis method). Use for "BOS", "break of struc... |
| `/tradecraft:master-trading-workflow` | Master 18-phase trading workflow — the definitive skill sequence for any trade. Covers infrastructure through automation. Use for "trading workflow", "full process", "trade checklist", "how to trade", "complete tradin... |
| `/tradecraft:mean-reversion-engine` | Mean reversion strategy templates — Bollinger bounce, RSI extreme fade, Z-score reversion with regime guard. Use this skill for "mean reversion", "fade the move", "RSI overbought oversold", "Bollinger bounce", "revers... |
| `/tradecraft:ml-trading` | Machine learning for trading — supervised classification/regression (XGBoost, LSTM), feature engineering, unsupervised regime detection (K-Means, HMM), reinforcement learning (PPO), NLP sentiment, and time-series cros... |
| `/tradecraft:mt5-chart-browser` | MT5 chart browser, pair scanner, indicator engine, and GPU-accelerated chart image analysis. Use this skill whenever the user asks to open MT5, browse pairs, view charts, apply indicators, screenshot charts, analyze c... |
| `/tradecraft:mt5-integration` | MT5 integration: chart browser, EA code generation, GPU chart analysis, multi-account management, pair scanning, OHLCV data engine, indicator engine, and MQL5 development. USE FOR: mt5, metatrader, EA, expert advisor,... |
| `/tradecraft:mtf-confluence-scorer` | Scores multi-timeframe alignment and outputs confluence heat maps. Use this skill whenever the user asks about "multi-timeframe analysis", "MTF confluence", "timeframe alignment", "higher timeframe bias", "are timefra... |
| `/tradecraft:multi-pair-basket-trader` | Trade currency baskets instead of individual pairs — USD basket, EUR basket, risk-on basket. Use for "basket trade", "currency basket", "trade USD strength", "sell EUR basket", "multi pair trade", "basket execution", ... |
| `/tradecraft:multi-strategy-orchestration` | Pipeline for running multiple trading strategies simultaneously. Signal arbitration, conflict resolution, capital allocation per strategy, risk aggregation, and regime switchover logic. The brain that coordinates all ... |
| `/tradecraft:news-intelligence` | Multi-source news intelligence gathering, cross-domain analysis, and skill routing for comprehensive situational awareness. Use this skill whenever the user asks "what's happening", "news today", "catch me up", "morni... |
| `/tradecraft:news-straddle-strategy` | News trading strategies — pre-news straddle, spike fade, news momentum riding, and event volatility strategies. Use for "news trading", "straddle NFP", "trade the news", "news spike", "fade the spike", "news momentum"... |
| `/tradecraft:notion-sync` | Sync trade journal entries, analysis notes, and skill outputs to Notion. Bidirectional — read watchlists from Notion, write trade logs back. |
| `/tradecraft:openalice-trading-agent` | OpenAlice — experimental file-driven autonomous AI trading agent running locally. "Your research desk, quant team, trading floor, and risk manager on your laptop 24/7." Uses "Trading-as-Git" workflow (stage → commit →... |
| `/tradecraft:options-trading` | Full options trading: Black-Scholes pricing, Greeks, IV surface, multi-leg strategies, and option screening. USE FOR: options, black-scholes, greeks, delta, gamma, theta, vega, implied volatility, iron condor, straddl... |
| `/tradecraft:pair-analyze` | Parametric combination command that runs a full multi-skill trading analysis for any symbol. Composes regime classification, structure (ICT/SMC), liquidity, entry refinement, risk sizing, and an execution plan. USE FO... |
| `/tradecraft:pair-scanner-screener` | Scan all available pairs for specific technical conditions — overbought, oversold, breakout, squeeze, divergence, pattern match. Use for "scan all pairs", "screener", "find setups", "which pairs have RSI oversold", "s... |
| `/tradecraft:poc-bounce-strategy` | Complete Volume Profile POC (Point of Control) bounce trading strategy with level detection, confluence scoring, multi-timeframe analysis, and trade management. Use whenever the user asks about "POC bounce", "point of... |
| `/tradecraft:polymarket-prediction-agents` | AI agent framework for autonomous trading on Polymarket prediction markets. Connects LLMs to Polymarket's DEX via Gamma API, supports RAG with Chroma DB, integrates news/betting/web-search data sources. Uses py-clob-c... |
| `/tradecraft:portfolio-optimization` | Modern portfolio construction: Markowitz MVO, Risk Parity, Black-Litterman, Hierarchical Risk Parity (HRP), Kelly Criterion, VaR/CVaR tail risk, and portfolio analytics. USE FOR: portfolio optimization, Markowitz, eff... |
| `/tradecraft:price-action` | Pure price action analysis: candlestick patterns & statistics, chart pattern recognition, harmonic patterns, Elliott Wave theory, and trendline/S&R detection. USE FOR: price action trading, candlestick pattern identif... |
| `/tradecraft:quant-ml-trading` | Complete quantitative and ML-powered trading toolkit — strategy validation, genetic optimization, decay monitoring, reinforcement learning, signal aggregation, data science pipelines, and statistical/quant foundations... |
| `/tradecraft:real-time-risk-monitor` | Real-time portfolio risk monitoring with live metrics (drawdown, exposure, correlation, VaR), configurable alert thresholds, kill switches for emergency stops, and ASCII dashboard display. Use for risk monitor, live r... |
| `/tradecraft:realtime-alert-pipeline` | Condition monitoring, multi-trigger alerts, and notification pipeline for trading signals. Use this skill whenever the user asks about "set an alert", "price alert", "notify me when", "trigger alert", "condition monit... |
| `/tradecraft:risk-and-portfolio` | Complete trading risk management, portfolio construction, performance tracking, and quantitative stress testing — all in one skill. The safety layer for all trading decisions. RISK MANAGEMENT: "risk management", "posi... |
| `/tradecraft:risk-calendar-trade-filter` | Determines when NOT to trade by mapping event blackout zones, session quality windows, and risk filters. Use this skill whenever the user asks "should I trade today", "is it safe to trade", "any events to avoid", "bla... |
| `/tradecraft:risk-of-ruin` | Risk of Ruin formula, Kelly Criterion (full and fractional), Monte Carlo survival simulation, and position sizing models (fixed fractional, volatility-adjusted, fixed ratio). Use for risk of ruin, Kelly criterion, Mon... |
| `/tradecraft:session-profiler` | Statistical analysis of trading sessions — London, New York, Tokyo, and their overlaps. Use this skill whenever the user asks about "best time to trade", "session analysis", "London session", "New York session", "Toky... |
| `/tradecraft:session-scalping` | Session-based and short-term strategies: Asian session scalping, session breakouts, scalping frameworks, breakout strategies, gap trading, grid trading, end-of-day, and swing trading. Opening Range Break & Retest (ORB... |
| `/tradecraft:smart-money-trap-detector` | Detect fake breakouts, stop hunts, liquidity grabs, and institutional traps. Use for "fake breakout", "trap", "stop hunt", "liquidity grab", "bull trap", "bear trap", "false break", "smart money trap", "institutional ... |
| `/tradecraft:smc-beginner-pro-guide` | Smart Risk's SMC beginner-to-pro framework: 5 core concepts — market direction (mitigation-based control), liquidity (stop hunting + grab patterns), supply & demand zones (3-candle rule, 3 marking methods), order bloc... |
| `/tradecraft:social-sentiment-scraper` | Scrapes and analyzes social media sentiment from Twitter/X, Reddit, TradingView, and market sentiment indicators like Fear & Greed Index and retail positioning. Use this skill whenever the user asks about "market sent... |
| `/tradecraft:spread-slippage-cost-analyzer` | Measure real execution costs, compare brokers, detect hidden fees and spread widening. Use this skill for "spread analysis", "slippage", "execution cost", "broker comparison", "hidden fees", "spread widening", "cost o... |
| `/tradecraft:statistics-timeseries` | Statistical analysis and time series modeling for trading: regime detection, probability modeling, edge validation, correlation modeling, distribution analysis, hypothesis testing, ARIMA models, stationarity testing, ... |
| `/tradecraft:strategy-genetic-optimizer` | Evolutionary algorithm engine that breeds, mutates, and evolves trading strategies automatically. Use this skill whenever the user asks to "optimize strategy", "evolve parameters", "genetic algorithm", "breed strategi... |
| `/tradecraft:strategy-selection` | Meta-skill for selecting the optimal trading strategy based on current market conditions, session timing, volatility regime, and asset class. Routes to the correct strategy skill. USE FOR: which strategy to use, what ... |
| `/tradecraft:strategy-validation` | End-to-end strategy validation — backtest tearsheet (Sharpe, Sortino, Calmar, VaR), walk-forward optimization, Monte Carlo stress testing, parameter sensitivity heatmaps, and strategy A/B testing. Use for validate str... |
| `/tradecraft:synthetic-pair-constructor` | Build custom synthetic instruments from weighted pair combinations. Use this skill whenever the user asks about "synthetic pair", "basket construction", "custom index", "weighted basket", "create a currency basket", "... |
| `/tradecraft:technical-analysis` | Complete technical analysis knowledge base covering candlestick patterns, chart patterns, technical indicators, support/resistance, Fibonacci levels, pivot points, and supply/demand zones. Includes Python strategy eng... |
| `/tradecraft:telegram-bot` | Send trading alerts and psychology nudges to Telegram. Mobile notifications for trade setups, risk warnings, and trade-psychology-coach messages. |
| `/tradecraft:tensortrade-rl` | TensorTrade — composable RL framework for building and training reinforcement learning trading agents. Modular TradingEnv with Observer, ActionScheme, RewardScheme, Portfolio, Exchange components. Integrates Ray RLlib... |
| `/tradecraft:tick-data-storage` | Tick data collection and storage: real-time tick capture from MT5, efficient storage formats (Parquet, HDF5), tick aggregation to OHLCV, bid/ask spread tracking. USE FOR: tick data, real-time data, live data feed, dat... |
| `/tradecraft:trade-copier-signal-broadcaster` | Format and distribute trading signals to MT5 copiers, Telegram bots, Discord bots, and webhook endpoints. Use this skill whenever the user asks about "trade copier", "signal service", "broadcast signals", "Telegram tr... |
| `/tradecraft:trade-journal-analytics` | Complete trade journalling system: trade logging, performance analytics, streak analysis, drawdown tracking, tag drill-down, and report generation. USE FOR: trade journal, log trade, performance report, win rate, expe... |
| `/tradecraft:trade-psychology-coach` | Trading psychology monitoring — tilt detection, emotional state tracking, trade-psychology-coach bias alerts, discipline scoring, and behavioral pattern recognition. Use for "trading psychology", "am I tilted", "reven... |
| `/tradecraft:trading-agents-llm` | Multi-agent LLM trading framework that mirrors real-world trading firm dynamics. Specialized agents (Fundamentals, Sentiment, News, Technical analysts + Researcher debate + Trader + Risk Manager) collaborate to analyz... |
| `/tradecraft:trading-brain` | Master Trading Brain — the TOP-LEVEL orchestrator implementing the 7-layer autonomous trading architecture. This is the PRIMARY entry point for ALL trading tasks. USE THIS SKILL FIRST FOR: "analyze the market", "what ... |
| `/tradecraft:trading-fundamentals` | Core trading knowledge covering market structure, order types, asset classes, timeframes, risk management, position sizing, trading psychology, and journaling. USE FOR: explain market structure, what is a market order... |
| `/tradecraft:trading-gym-rl-env` | TradingGym — OpenAI Gym-style RL trading environment toolkit for tick and OHLC data. Supports training, backtesting, and (planned) live trading via IB API. 3-action discrete space (hold/buy/sell), configurable observa... |
| `/tradecraft:trading-plan-builder` | Structured pre-market routine, watchlist generation, daily preparation checklist, and trading plan templates. Use this skill for "trading plan", "pre-market routine", "daily prep", "watchlist", "what should I focus on... |
| `/tradecraft:volatility-surface-analyzer` | Implied volatility, vol smile, term structure, and vol arbitrage signal analysis. Use this skill whenever the user asks about "implied volatility", "vol smile", "volatility surface", "term structure", "vol skew", "IV ... |
| `/tradecraft:volume-analysis` | Volume Profile (POC, VAH, VAL, HVN, LVN), Order Flow & Delta analysis, and Wyckoff accumulation/distribution detection with Python engines. Use for volume profile, order flow, delta divergence, Wyckoff, POC level, or ... |
| `/tradecraft:xtrading-analyze` | Full multi-strategy market analysis using the 6-layer autonomous trading AI. Fetches live MT5 data, generates charts, then runs the complete analysis pipeline through multi-agent system, trade-psychology-coach layer, ... |
| `/tradecraft:zone-refinement-sniper-entry` | Supply & Demand zone refinement strategy for sniper entries — drop timeframes to find smaller zones inside larger zones, dramatically amplifying R:R (1.9R to 6.25R on same trade). Covers extreme zone selection, standa... |

## AI Development

| Command | Description |
|---|---|
| `/tradecraft:agent-development` | This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent... |
| `/tradecraft:ai-agent-builder` | Expert guide for building AI-powered coding agents that produce professional-quality output. Trigger whenever the user asks to build an AI agent, coding assistant, automation pipeline, tool-using LLM system, or says "... |
| `/tradecraft:few-shot-quality-prompting` | Master guide for crafting prompts that make AI models produce professional-quality code and UI consistently. Trigger whenever the user asks about prompt engineering, improving AI output quality, building system prompt... |
| `/tradecraft:mcp-integration` | This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROO... |
| `/tradecraft:openspec` | OpenSpec — lightweight fluid spec framework for AI-assisted development. USE FOR: "openspec", "opsx", "/opsx:propose", "propose feature", "spec before coding", "iterative spec", "brownfield spec", "AI spec framework",... |
| `/tradecraft:spec-kit` | GitHub Spec Kit — Spec-Driven Development with AI coding agents. Structures AI coding by creating living spec artifacts before implementation. USE FOR: "spec kit", "spec-driven", "specify init", "write a spec", "creat... |
| `/tradecraft:transformers-js` | Use Transformers.js to run state-of-the-art machine learning models directly in JavaScript/TypeScript. Supports NLP (text classification, translation, summarization), computer vision (image classification, object dete... |

## Software Engineering

| Command | Description |
|---|---|
| `/tradecraft:agentic-storage` | Agentic storage architecture — persistent memory for AI agents using MCP, immutable versioning, sandboxing, and intent validation. Covers the stateless problem in LLM agents, RAG limitations (read-only), MCP protocol ... |
| `/tradecraft:code-review` | Reviews code changes using CodeRabbit AI. Use when user asks for code review, PR feedback, code quality checks, security issues, or wants autonomous fix-review cycles. |
| `/tradecraft:debug-failing-test` | Debug a failing test using an iterative logging approach, then clean up and document the learning. |
| `/tradecraft:e2b-sandboxes` | E2B open-source cloud sandboxes for executing AI-generated code securely. USE FOR: run code in sandbox, e2b, code interpreter, execute AI code, secure code execution, isolated environment, AI coding agent execution, r... |
| `/tradecraft:elite-ui-design` | Generates production-grade, visually stunning UI code that rivals top design studios. Trigger whenever the user asks to build any interface — web apps, dashboards, landing pages, mobile screens, component libraries, o... |
| `/tradecraft:frontend-design` | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids gener... |
| `/tradecraft:git-phase-restore` | Autonomous Git-based project phase restoration. Uses Git history (commits, tags, branches, diffs, semantic messages) to identify and restore any development phase automatically. Trigger for: "restore to when X worked"... |
| `/tradecraft:github-actions-trigger` | Trigger GitHub Actions workflows from Claude Code. Auto-run tests, deploy, or validate when skills like run-pre-commit-checks complete. |
| `/tradecraft:httpie-cli` | HTTPie — human-friendly CLI HTTP client for APIs, debugging, testing and scripting. USE FOR: "httpie", "http cli", "api testing", "http request terminal", "curl alternative", "test API from command line", "send HTTP r... |
| `/tradecraft:interactive-coding-challenges` | 120+ interactive coding challenges in Jupyter Notebooks covering data structures, algorithms, system design and OOP for interview prep. USE FOR: coding challenges, algorithm practice, data structures interview, leetco... |
| `/tradecraft:ip-rotation` | Rotate IP addresses when sessions are rate-limited or blocked by YouTube or other services. USE FOR: ip rotation, rate limit, proxy, tor, blocked, 429 error, youtube block. |
| `/tradecraft:playground` | Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a pla... |
| `/tradecraft:pro-code-architecture` | Produces senior-engineer-level code architecture across any language or platform. Trigger whenever the user asks to build a feature, module, service, or full app — or says "clean code", "scalable", "production-grade",... |
| `/tradecraft:programmatic-drawing` | Expert skill for generating visual art, diagrams, illustrations, charts, and drawings programmatically using SVG, HTML Canvas, p5.js, Three.js, Mermaid, and D3. Trigger whenever the user asks to draw, illustrate, visu... |
| `/tradecraft:python-manager-discovery` | Environment manager-specific discovery patterns and known issues. Use when working on or reviewing environment discovery code for conda, poetry, pipenv, pyenv, or venv. |
| `/tradecraft:run-e2e-tests` | Run E2E tests to verify complete user workflows like environment discovery, creation, and selection. Use this before releases or after major changes. |
| `/tradecraft:run-integration-tests` | Run integration tests to verify that extension components work together correctly. Use this after modifying component interactions or event handling. |
| `/tradecraft:run-pre-commit-checks` | Run the mandatory pre-commit checks before committing code. Includes lint, type checking, and unit tests. MUST be run before every commit. |
| `/tradecraft:run-smoke-tests` | Run smoke tests to verify extension functionality in a real VS Code environment. Use this when checking if basic features work after changes. |
| `/tradecraft:system-design-academy` | Real-world system design case studies from 40+ major tech companies + 114 concepts. USE FOR: system design, design Twitter, design YouTube, design Uber, design Netflix, design WhatsApp, design Slack, design Instagram,... |

## Claude Code Platform

| Command | Description |
|---|---|
| `/tradecraft:claude-automation-recommender` | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improvi... |
| `/tradecraft:claude-md-improver` | Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality repor... |
| `/tradecraft:command-development` | This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with fil... |
| `/tradecraft:context-memory` | Persist and recall state between skill invocations. Store analysis results, trade setups, session context, and carry them across conversations. |
| `/tradecraft:generate-snapshot` | Generate a codebase health snapshot for technical debt tracking and planning. Analyzes git history, code complexity, debt markers, and dependencies to identify hotspots and refactoring priorities. |
| `/tradecraft:hook-development` | This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automat... |
| `/tradecraft:plugin-settings` | This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin set... |
| `/tradecraft:plugin-structure` | This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/age... |
| `/tradecraft:skill-analytics` | Track which skills you use most, success rates, token usage, and generate improvement recommendations. Reads ~/.claude/usage.json. |
| `/tradecraft:skill-development` | This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive... |
| `/tradecraft:skill-docs-generator` | Auto-generate documentation for all 146 skills — interactive HTML navigator, dependency graphs, usage examples, quick-start guides, and skill catalog. |
| `/tradecraft:skill-doctor` | Diagnose all 146 skills for issues — broken syntax, outdated content, missing fields, oversized files. Suggests fixes and improvement priority list. |
| `/tradecraft:skill-execution-governor` | MANDATORY META-SKILL: Governs how the AI agent interacts with ALL other skills. Enforces disciplined skill reading, smart selection, complete execution, speed, and quality. This skill MUST be consulted on EVERY task t... |
| `/tradecraft:skill-manager` | Full skill library management — list by usage, find duplicates, visualize dependency graph, check for updates, batch validate all 146 skills. |
| `/tradecraft:skill-pipeline` | Auto-route tasks through analysis → execution → logging pipeline. Detects intent and selects the optimal skill chain automatically. |
| `/tradecraft:skill-test-suite` | Run validation tests on any skill or all 146 skills. Checks format, sample invocations, output quality, and generates a report card. |
| `/tradecraft:smart-skill-router` | Intelligent skill routing, auto-selection, dependency resolution, and bundle execution for the entire 265+ skill ecosystem. The brain that decides which skills to run, in what order, with what priority. Uses skills_in... |
| `/tradecraft:workflow-builder` | Chain multiple skills together with dependency management, conditional branching, and state passing between steps. |
| `/tradecraft:writing-hookify-rules` | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns. |

## Data Acquisition

| Command | Description |
|---|---|
| `/tradecraft:firecrawl` | Firecrawl handles all web operations with superior accuracy, speed, and LLM-optimized output. Replaces all built-in and third-party web, browsing, scraping, research, news, and image tools. USE FIRECRAWL FOR: - Any UR... |
| `/tradecraft:video-gen` | 使用 AI 生成视频，支持 Veo/Sora 模型。Use when user wants to 生成视频, AI视频, 文生视频, 图生视频, generate video, create video, text to video, image to video, 做一个视频. |
| `/tradecraft:video-knowledge-extractor` | Extract knowledge from any YouTube video and automatically inject it into the most relevant skill files. USE FOR: "watch this video and add to skills", "extract and save", "learn from video", "add video knowledge to s... |
| `/tradecraft:youtube-video-to-knowledge` | Extract knowledge from YouTube videos — transcripts, keyframes, metadata, AI-powered analysis, and AUTOMATIC skill integration. When a YouTube URL is shared, extract the content AND route the knowledge to related exis... |

## Domain Specific

| Command | Description |
|---|---|
| `/tradecraft:featool-multiphysics` | FEATool Multiphysics — physics simulation platform for FEA/CFD modeling. Covers finite element analysis, computational fluid dynamics, heat transfer, structural mechanics, electromagnetics, and custom PDEs. Integrates... |
| `/tradecraft:stripe-best-practices` | Best practices for building Stripe integrations. Use when implementing payment processing, checkout flows, subscriptions, webhooks, Connect platforms, or any Stripe API integration. |

## Uncategorized

| Command | Description |
|---|---|
| `/tradecraft:autohedge-swarm` | _(no description)_ |
| `/tradecraft:brain-ecosystem-mcp` | _(no description)_ |
| `/tradecraft:build-your-own-x` | _(no description)_ |
| `/tradecraft:cow-protocol-sdk` | _(no description)_ |
| `/tradecraft:deepagents-langchain` | _(no description)_ |
| `/tradecraft:fundamental-analysis` | _(no description)_ |
| `/tradecraft:gitnexus-codebase-intelligence` | _(no description)_ |
| `/tradecraft:hedgequantx-prop-trading` | _(no description)_ |
| `/tradecraft:ritmex-crypto-agent` | _(no description)_ |
| `/tradecraft:smc-python-library` | _(no description)_ |
| `/tradecraft:stocksight-sentiment` | _(no description)_ |
| `/tradecraft:trading-autopilot` | _(no description)_ |

## Notes

12 skill file(s) have incomplete frontmatter and may show as uncategorized until the description is added:

- `/tradecraft:autohedge-swarm` - yaml: mapping values are not allowed here
  in "<unicode string>", line 2, column 116:
     ... rchitecture. Sequential pipeline: Director → Quant → Risk Manage ... 
                                         ^
- `/tradecraft:brain-ecosystem-mcp` - yaml: mapping values are not allowed here
  in "<unicode string>", line 2, column 118:
     ... r Claude Code. Brain (280 tools): error memory, code intelligenc ... 
                                         ^
- `/tradecraft:build-your-own-x` - yaml: mapping values are not allowed here
  in "<unicode string>", line 2, column 127:
     ... gies from scratch. 30 categories: databases, Docker, Git, OS, co ... 
                                         ^
- `/tradecraft:cow-protocol-sdk` - yaml: mapping values are not allowed here
  in "<unicode string>", line 2, column 129:
     ... tion. Coincidence of Wants (CoW): batch auction matching, solver ... 
                                         ^
- `/tradecraft:deepagents-langchain` - yaml: mapping values are not allowed here
  in "<unicode string>", line 2, column 102:
     ... by LangChain. Batteries-included: planning (write_todos), filesy ... 
                                         ^
- `/tradecraft:fundamental-analysis` - yaml: mapping values are not allowed here
  in "<unicode string>", line 2, column 603:
     ... rs, or business quality. USE FOR: P/E ratio, P/B ratio, EV/EBITD ... 
                                         ^
- `/tradecraft:gitnexus-codebase-intelligence` - yaml: mapping values are not allowed here
  in "<unicode string>", line 2, column 126:
     ... raphs for AI agents. 7 MCP tools: symbol discovery (BM25+semanti ... 
                                         ^
- `/tradecraft:hedgequantx-prop-trading` - yaml: mapping values are not allowed here
  in "<unicode string>", line 2, column 185:
     ... , Tradovate (3 firms). Two modes: proprietary HQX strategy or co ... 
                                         ^
- `/tradecraft:ritmex-crypto-agent` - yaml: mapping values are not allowed here
  in "<unicode string>", line 2, column 256:
     ... uilt on Bun (TypeScript). Agents: data p
                                         ^
- `/tradecraft:smc-python-library` - yaml: mapping values are not allowed here
  in "<unicode string>", line 2, column 114:
     ... on OHLC DataFrames. 8 indicators: FVG, Swing Highs/Lows, BOS/CHo ... 
                                         ^
- `/tradecraft:stocksight-sentiment` - yaml: mapping values are not allowed here
  in "<unicode string>", line 2, column 257:
     ... or local install. Asset-agnostic: works
                                         ^
- `/tradecraft:trading-autopilot` - yaml: mapping values are not allowed here
  in "<unicode string>", line 2, column 51:
     ... autonomous trading orchestration: regime detection → strategy se ... 
                                         ^
