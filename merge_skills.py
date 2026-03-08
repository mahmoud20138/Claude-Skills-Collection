"""Merge 153 individual skill files into ~23 categorized files."""
import os, re

SKILLS_DIR = r"C:\Users\Mamoud\.claude\skills"

MERGES = {
    # === AZURE (5 groups) ===
    "azure-infrastructure": [
        "azure-compute", "azure-storage", "azure-messaging", "azure-postgres",
        "azure-deploy", "azure-prepare", "azure-validate", "azure-cloud-migrate",
        "azure-resource-lookup", "azure-resource-visualizer"
    ],
    "azure-security-identity": [
        "azure-rbac", "azure-compliance", "entra-app-registration"
    ],
    "azure-ai-copilot": [
        "azure-ai", "azure-aigateway", "azure-hosted-copilot-sdk", "microsoft-foundry"
    ],
    "azure-devops-observability": [
        "azure-observability", "azure-diagnostics", "appinsights-instrumentation", "azure-kusto"
    ],
    "azure-cost-data": [
        "azure-cost-optimization"
    ],

    # === TRADING - TECHNICAL ANALYSIS (2 groups) ===
    "trading-technical-analysis": [
        "technical-analysis", "technical-analysis-complete", "technical-indicators",
        "market-structure-bos-choch", "mtf-confluence-scorer",
        "chart-pattern-scanner", "chart-pattern-recognition-vision",
        "candlestick-pattern-vision", "trendline-sr-vision",
        "chart-annotation-overlay", "chart-image-preprocessor", "chart-vision-renderer"
    ],
    "trading-indicators-signals": [
        "elliott-wave-engine", "fibonacci-strategy-engine", "harmonic-pattern-engine",
        "pivot-point-strategies", "volume-profile-strategy", "order-flow-delta-strategy",
        "liquidity-order-flow-mapper", "divergence-strategy-engine",
        "wyckoff-method-engine", "heikin-ashi-renko-strategies"
    ],

    # === TRADING - STRATEGIES (4 groups) ===
    "trading-strategies-core": [
        "trading-strategies-complete", "trading-strategies-playbook",
        "ict-trading-strategy", "ict-trading-tool",
        "supply-demand-zone-strategy", "price-action-pure-engine",
        "breakout-strategy-engine", "session-breakout-strategies",
        "mean-reversion-engine", "trend-following-systems"
    ],
    "trading-strategies-advanced": [
        "scalping-framework", "swing-trading-framework", "end-of-day-strategy",
        "gap-trading-strategy", "momentum-roc-strategy", "grid-trading-engine",
        "asian-session-scalper", "news-straddle-strategy",
        "carry-trade-calculator", "cot-positioning-strategy",
        "sentiment-extreme-contrarian", "options-trading"
    ],
    "trading-multi-asset-quant": [
        "quantitative-strategies", "quantitative-trading",
        "pair-correlation-engine", "correlation-regime-switcher",
        "cross-asset-arbitrage-engine", "intermarket-divergence-trader",
        "multi-pair-basket-trader", "synthetic-pair-constructor",
        "risk-premia-harvester", "multi-strategy-allocator"
    ],
    "trading-fundamentals-macro": [
        "fundamental-analysis", "fundamental-analysis-complete",
        "trading-fundamentals", "macro-economic-dashboard",
        "market-news-impact", "social-sentiment-scraper",
        "ai-signal-aggregator", "alternative-data-integrator",
        "seasonality-analyzer", "institutional-behavior-monitor",
        "event-timeline-linker"
    ],

    # === TRADING - RISK & EXECUTION ===
    "trading-risk-management": [
        "risk-manager-position-sizer", "trading-risk-psychology",
        "drawdown-recovery-protocol", "tail-risk-hedging",
        "risk-calendar-trade-filter", "monte-carlo-stress-tester",
        "spread-slippage-cost-analyzer", "market-impact-model",
        "multi-account-manager"
    ],
    "trading-execution-monitoring": [
        "execution-optimizer", "realtime-alert-pipeline",
        "trade-copier-signal-broadcaster", "market-microstructure-analyzer",
        "session-profiler", "market-regime-classifier",
        "volatility-surface-analyzer"
    ],

    # === TRADING - BACKTESTING & DATA ===
    "trading-backtesting-optimization": [
        "backtest-report-generator", "walk-forward-optimizer",
        "strategy-genetic-optimizer", "strategy-ab-tester",
        "strategy-decay-monitor", "parameter-sensitivity-analyzer",
        "rl-trade-agent"
    ],
    "trading-data-visualization": [
        "trading-data-science", "trade-journal-performance",
        "trading-plan-builder",
        "portfolio-optimizer", "programmatic-drawing"
    ],

    # === TRADING - MT5 & ICT SYSTEM ===
    "mt5-trading-system": [
        "mt5-master-orchestrator", "mt5-trade-executor-monitor",
        "mt5-ea-code-generator", "mt5-chart-browser",
        "ict-market-scanner-agent", "full-market-scanner",
        "trading-dashboard-bridge", "trading-brain-orchestrator"
    ],

    # === CLAUDE DEVELOPMENT (2 groups) ===
    "claude-plugin-development": [
        "plugin-structure", "plugin-settings", "hook-development",
        "command-development", "skill-development", "skill-creator",
        "mcp-integration", "settings-precedence"
    ],
    "claude-workflow-tools": [
        "claude-automation-recommender", "claude-md-improver",
        "few-shot-quality-prompting", "writing-rules",
        "playground", "example-skill"
    ],

    # === DEVELOPMENT & ARCHITECTURE ===
    "development-architecture": [
        "pro-code-architecture", "frontend-design", "elite-ui-design",
        "agent-development", "ai-agent-builder",
        "cross-platform-paths", "python-manager-discovery"
    ],

    # === DEVOPS & TESTING ===
    "devops-testing": [
        "run-e2e-tests", "run-integration-tests", "run-smoke-tests",
        "run-pre-commit-checks", "debug-failing-test",
        "generate-snapshot", "git-phase-restore"
    ],

    # === MISC TOOLS ===
    "misc-tools": [
        "aitk-stock-price-tool", "aitk-travel-planner"
    ],
}

DESCRIPTIONS = {
    "azure-infrastructure": "Azure infrastructure skills: compute, storage, messaging, postgres, deployment, migration, resource management, and validation.",
    "azure-security-identity": "Azure security and identity: RBAC, compliance, Entra ID app registration.",
    "azure-ai-copilot": "Azure AI services: AI gateway, hosted copilot SDK, Microsoft Foundry integration.",
    "azure-devops-observability": "Azure observability and diagnostics: Application Insights, Kusto queries, monitoring.",
    "azure-cost-data": "Azure cost optimization and resource cost management.",
    "trading-technical-analysis": "Technical analysis: indicators, market structure (BOS/CHoCH), multi-timeframe confluence, chart patterns, candlestick vision, trendlines, S/R, chart overlays.",
    "trading-indicators-signals": "Advanced indicator engines: Elliott Wave, Fibonacci, harmonics, pivots, volume profile, order flow delta, liquidity mapping, divergence, Wyckoff, Heikin-Ashi/Renko.",
    "trading-strategies-core": "Core trading strategies: ICT, supply/demand zones, price action, breakout, session breakout, mean reversion, trend following.",
    "trading-strategies-advanced": "Advanced strategies: scalping, swing trading, end-of-day, gap trading, momentum, grid, Asian session, news straddle, carry trade, COT positioning, sentiment contrarian, options.",
    "trading-multi-asset-quant": "Quantitative and multi-asset: pair correlation, cross-asset arbitrage, intermarket divergence, basket trading, synthetic pairs, risk premia, multi-strategy allocation.",
    "trading-fundamentals-macro": "Fundamentals and macro: fundamental analysis, macro dashboard, news impact, social sentiment, AI signal aggregation, alternative data, seasonality, institutional monitoring.",
    "trading-risk-management": "Risk management: position sizing, psychology, drawdown recovery, tail hedging, risk calendar, Monte Carlo stress testing, cost analysis, market impact, multi-account.",
    "trading-execution-monitoring": "Execution and monitoring: order execution optimization, real-time alerts, trade copying, microstructure analysis, session profiling, regime classification, volatility surface.",
    "trading-backtesting-optimization": "Backtesting and optimization: report generation, walk-forward, genetic optimization, A/B testing, strategy decay, parameter sensitivity, reinforcement learning.",
    "trading-data-visualization": "Trading data and visualization: data science, trade journaling, plan builder, chart rendering, portfolio optimization, programmatic drawing.",
    "mt5-trading-system": "MT5 trading system: master orchestrator, trade executor/monitor, EA code generator, chart browser, ICT scanner, full market scanner, dashboard bridge, brain orchestrator.",
    "claude-plugin-development": "Claude plugin development: plugin structure, settings, hooks, commands, skills, MCP integration, settings precedence.",
    "claude-workflow-tools": "Claude workflow tools: automation recommender, CLAUDE.md improver, prompting techniques, writing rules, playground, examples.",
    "development-architecture": "Development and architecture: code architecture, frontend/UI design, agent development, cross-platform paths, Python manager discovery.",
    "devops-testing": "DevOps and testing: E2E tests, integration tests, smoke tests, pre-commit checks, debug failing tests, snapshots, git phase restore.",
    "misc-tools": "Miscellaneous tools: stock price lookup, travel planner.",
}

def strip_frontmatter(content):
    """Remove YAML frontmatter from markdown content."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3:].strip()
    return content.strip()

def get_name_from_filename(filename):
    """Convert filename to display name."""
    return filename.replace(".md", "").replace("-", " ").title()

def main():
    # Verify all source files exist
    all_sources = []
    for group, files in MERGES.items():
        for f in files:
            all_sources.append(f)
            path = os.path.join(SKILLS_DIR, f + ".md")
            if not os.path.exists(path):
                print(f"WARNING: Missing source file: {path}")

    # Check for files not covered by any merge group
    existing = set(f.replace(".md", "") for f in os.listdir(SKILLS_DIR) if f.endswith(".md"))
    covered = set(all_sources)
    uncovered = existing - covered
    if uncovered:
        print(f"NOTE: {len(uncovered)} files not in any merge group (will be kept as-is):")
        for u in sorted(uncovered):
            print(f"  - {u}")

    # Check for duplicates across groups
    seen = {}
    for group, files in MERGES.items():
        for f in files:
            if f in seen:
                print(f"ERROR: Duplicate '{f}' in groups '{seen[f]}' and '{group}'")
                return
            seen[f] = group

    # Perform merges
    created = 0
    deleted = 0
    for group_name, source_files in MERGES.items():
        desc = DESCRIPTIONS.get(group_name, f"Merged skill group: {group_name}")

        # Build trigger list from all source descriptions
        triggers = set()
        triggers.add(group_name.replace("-", " "))
        for sf in source_files:
            triggers.add(sf.replace("-", " "))

        trigger_str = ", ".join(sorted(triggers))

        # Build merged content
        sections = []
        valid_sources = []
        for sf in source_files:
            path = os.path.join(SKILLS_DIR, sf + ".md")
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as fh:
                    content = fh.read()
                body = strip_frontmatter(content)
                if body:
                    display_name = get_name_from_filename(sf)
                    sections.append(f"## {display_name}\n\n{body}")
                    valid_sources.append(sf)

        if not sections:
            print(f"SKIP: No content for group '{group_name}'")
            continue

        # Build frontmatter
        frontmatter = f"""---
name: {group_name}
description: >
  {desc}
  Trigger for: {trigger_str}.
---"""

        merged_content = frontmatter + "\n\n# " + get_name_from_filename(group_name) + "\n\n" + "\n\n---\n\n".join(sections) + "\n"

        # Write merged file
        out_path = os.path.join(SKILLS_DIR, group_name + ".md")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(merged_content)
        created += 1
        print(f"CREATED: {group_name}.md ({len(valid_sources)} sources merged)")

        # Delete consumed source files (only if different from output name)
        for sf in valid_sources:
            if sf != group_name:
                src_path = os.path.join(SKILLS_DIR, sf + ".md")
                if os.path.exists(src_path):
                    os.remove(src_path)
                    deleted += 1

    remaining = len([f for f in os.listdir(SKILLS_DIR) if f.endswith(".md")])
    print(f"\nDONE: Created {created} merged files, deleted {deleted} source files.")
    print(f"Total skills now: {remaining}")

if __name__ == "__main__":
    main()
