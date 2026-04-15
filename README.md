# Skills Collection

> **161 curated AI skills** across **6 domains** and **33 categories** — self-contained knowledge bases with code for trading, development, and automation.

[![Skills](https://img.shields.io/badge/skills-161-blue?style=for-the-badge)](.)
[![Domains](https://img.shields.io/badge/domains-6-green?style=for-the-badge)](.)
[![Categories](https://img.shields.io/badge/categories-33-orange?style=for-the-badge)](.)
[![Version](https://img.shields.io/badge/version-3.0-brightgreen?style=for-the-badge)](.)
[![License](https://img.shields.io/badge/license-MIT-informational?style=for-the-badge)](LICENSE)

---

## Table of Contents

- [What Are Skills?](#what-are-skills)
- [How Skills Work](#how-skills-work)
- [Skill Anatomy](#skill-anatomy)
- [Skill Types](#skill-types)
- [Architecture Overview](#architecture-overview)
- [Domain Breakdown](#domain-breakdown)
  - [Trading (106 Skills)](#01--trading--106-skills)
  - [AI Development (9 Skills)](#02--ai-development--9-skills)
  - [Software Engineering (22 Skills)](#03--software-engineering--22-skills)
  - [Claude Code Platform (18 Skills)](#04--claude-code-platform--18-skills)
  - [Data Acquisition (4 Skills)](#05--data-acquisition--4-skills)
  - [Domain Specific (2 Skills)](#06--domain-specific--2-skills)
- [Trading Lifecycle Map](#trading-lifecycle-map)
- [Skill Graph](#skill-graph)
- [How to Use](#how-to-use)
- [Index Files](#index-files)
- [Contributing](#contributing)
- [License](#license)

---

## What Are Skills?

**Skills** are self-contained Markdown files that serve as structured knowledge bases for AI coding assistants. Each skill contains:

- **Domain expertise** — curated knowledge on a specific topic (e.g., ICT Smart Money Concepts, MCP integration, backtesting systems)
- **Executable code** — Python, TypeScript, MQL5, SQL, and other languages embedded as runnable code blocks
- **Trigger keywords** — keywords in the YAML frontmatter that help AI assistants auto-select the right skill
- **Cross-references** — links to related skills, creating a navigable knowledge graph

Think of each skill as a **senior expert's brain dump** on one focused topic — distilled into a format that AI assistants can read, understand, and act on immediately.

### Why Skills?

| Problem | Solution |
|---------|----------|
| AI assistants lack domain-specific trading knowledge | Skills inject expert-level knowledge on demand |
| Context windows are limited | Skills are focused — only load what you need |
| Repetitive prompts for complex workflows | Skills encode complete multi-step processes |
| No consistency across sessions | Skills persist knowledge between conversations |
| Hard to discover related capabilities | `skills_index.json` provides a searchable graph |

---

## How Skills Work

```
┌──────────────────────────────────────────────────────────────────┐
│                        YOUR AI ASSISTANT                         │
│                   (Claude Code / Cursor / Copilot)               │
└──────────────┬─────────────────────────────────────┬────────────┘
               │                                     │
               │  "Analyze EURUSD with ICT concepts"  │
               ▼                                     │
┌──────────────────────────┐                          │
│   skills_index.json      │ ◄── Skill discovery      │
│   ─ 161 entries           │     via keyword match    │
│   ─ tags & categories     │     or manual reference  │
└──────────┬───────────────┘                          │
           │ matches: ict-smart-money                  │
           ▼                                          │
┌──────────────────────────────────────────┐          │
│  classified/01-trading/03-strategies/     │          │
│  01-ict-smart-money/                      │          │
│  ict-smart-money.md  (2,658 lines)        │          │
│                                           │          │
│  ┌─────────────────────────────────┐     │          │
│  │  YAML Frontmatter               │     │          │
│  │  name: ict-smart-money          │     │          │
│  │  tags: [ict, smc, liquidity]    │     │          │
│  │  related: [session-scalping...] │     │          │
│  └─────────────────────────────────┘     │          │
│  ┌─────────────────────────────────┐     │          │
│  │  Knowledge Sections              │     │          │
│  │  Market Structure (BOS/CHoCH)   │     │          │
│  │  Order Blocks                    │     │          │
│  │  Fair Value Gaps                 │     │          │
│  │  Killzones & Sessions            │     │          │
│  │  Liquidity Sweeps                │     │          │
│  └─────────────────────────────────┘     │          │
│  ┌─────────────────────────────────┐     │          │
│  │  Executable Code                 │     │          │
│  │  Python detection engines        │     │          │
│  │  MQL5 indicator code             │     │          │
│  │  Confluence scoring system       │     │          │
│  └─────────────────────────────────┘     │          │
└──────────────────────────────────────────┘          │
           │                                          │
           │  AI generates expert-level analysis       │
           ▼                                          │
┌──────────────────────────┐                          │
│  Output:                  │                          │
│  • Market structure map   │                          │
│  • Order block zones      │                          │
│  • FVG detection results  │                          │
│  • Confluence score       │                          │
│  • Trade plan             │                          │
└──────────────────────────┘                          │
```

---

## Skill Anatomy

Every skill follows the same structure. Here's the anatomy of a typical skill file:

```
ict-smart-money.md
│
├── YAML Frontmatter (metadata)
│   ├── name .................. Unique identifier
│   ├── description ........... What the skill does + trigger keywords
│   ├── kind .................. Type (reference, engine, tool, workflow...)
│   ├── category .............. Domain path (trading/strategies)
│   ├── status ................ active | deprecated | experimental
│   ├── tags .................. Searchable keywords
│   ├── related_skills ........ Linked skills (knowledge graph edges)
│   ├── skill_level ........... beginner | intermediate | advanced
│   └── aliases ............... Alternative names for discovery
│
├── Header Block
│   └── Skill card with domain, category, level, tags
│
├── Knowledge Sections (the core content)
│   ├── Section 1: Concept explanation
│   ├── Section 2: Detailed methodology
│   ├── Section 3: Implementation details
│   └── ...
│
├── Code Blocks (executable implementations)
│   ├── Python detection/analysis engines
│   ├── MQL5 indicator code
│   ├── Configuration examples
│   └── Usage demonstrations
│
└── Cross-references
    └── Links to related_skills for deeper exploration
```

### Example: YAML Frontmatter

```yaml
---
name: ict-smart-money
description: >
  ICT Smart Money Concepts — full methodology reference.
  Covers BOS/CHoCH, order blocks, FVG, killzones, liquidity...
  USE FOR: ICT, smart money, SMC, order block, BOS, CHoCH...
kind: reference
category: trading/strategies
status: active
tags: [trading, strategy, ict, smc, liquidity, orderflow, fvg, orderblock]
related_skills: [session-scalping, technical-analysis, liquidity-analysis]
skill_level: advanced
aliases: [ict-smc]
---
```

---

## Skill Types

Each skill has a `kind` field that describes its purpose:

| Kind | Count | Description | Example |
|------|-------|-------------|---------|
| `reference` | 68 | Knowledge bases with theory + code | `ict-smart-money`, `technical-analysis` |
| `engine` | 15 | Computational engines with algorithms | `breakout-strategy-engine`, `harmonic-pattern-engine` |
| `workflow` | 14 | Multi-step processes and sequences | `master-trading-workflow`, `trading-autopilot` |
| `tool` | 16 | Utility tools and integrations | `mt5-chart-browser`, `programmatic-drawing` |
| `meta` | 20 | Skills about skills / system-level | `skill-development`, `command-development` |
| `analyzer` | 10 | Data analysis and scoring systems | `market-regime-classifier`, `volume-analysis` |
| `agent` | 12 | Autonomous AI agent frameworks | `ai-trading-crew`, `freqtrade-bot` |
| `strategy` | 12 | Trading strategy implementations | `poc-bounce-strategy`, `dan-zanger-breakout` |
| `integration` | 4 | External service connections | `mcp-integration`, `discord-webhook` |
| `generator` | 2 | Content/code generation | `backtest-report-generator`, `skill-docs-generator` |
| `orchestrator` | 4 | High-level coordination | `trading-brain`, `strategy-selection` |

```
Skill Type Distribution
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
reference   ████████████████████████████████████████░  68  (42%)
meta        ████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░  20  (12%)
tool        █████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  16  (10%)
engine      █████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  15  (9%)
workflow    ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  14  (9%)
analyzer    ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  10  (6%)
agent       ███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  12  (7%)
strategy    ███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  12  (7%)
integration ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   4  (2%)
orchestrator████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   4  (2%)
generator   ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   2  (1%)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Architecture Overview

```
skills-export/
│
├── classified/                         ← 161 skills in 6 domains
│   │
│   ├── 01-trading/                     ← 106 skills (66%)
│   │   ├── 01-core-knowledge/          (7)   Forex, equities, futures, options, crypto, DeFi
│   │   ├── 02-analysis/                (9)   Price action, technical, fundamental, chart vision
│   │   ├── 03-strategies/              (22)  ICT/SMC, breakout, mean-reversion, sessions
│   │   ├── 04-market-context/          (14)  Regime, macro, correlation, breadth, volatility
│   │   ├── 05-risk-management/         (6)   Position sizing, drawdown, portfolio, monitoring
│   │   ├── 06-execution/               (6)   Algo, HFT, market-making, prop trading
│   │   ├── 07-data-signals/            (7)   Ingestion, sentiment, news, signals
│   │   ├── 08-mt5-platform/            (3)   Integration, charts, expert advisors
│   │   ├── 09-quant-ml/                (9)   Backtesting, ML, RL, genetic optimization
│   │   ├── 10-ai-trading-agents/       (7)   Multi-agent, autonomous, prediction markets
│   │   ├── 11-psychology-ops/          (3)   Psychology coaching, journalling, planning
│   │   ├── 12-infrastructure/          (5)   Alerts, Telegram, Discord, Notion, copier
│   │   └── 13-orchestration/           (8)   Master workflow, brain, autopilot, strategy selection
│   │
│   ├── 02-ai-development/              ← 9 skills (6%)
│   │   ├── 01-agent-building/          Agent frameworks, architecture, MCP integration
│   │   ├── 02-prompt-engineering/      Few-shot quality prompting
│   │   ├── 03-ml-tools/                Transformers.js
│   │   └── 04-spec-driven/             OpenSpec, Spec-Kit
│   │
│   ├── 03-software-engineering/        ← 22 skills (14%)
│   │   ├── 01-architecture/            System design, codebase intelligence, clean code
│   │   ├── 02-code-review-quality/     Code review, health snapshots
│   │   ├── 03-testing/                 E2E, integration, smoke, pre-commit, debug
│   │   ├── 04-ui-design/               Frontend, visualization, playground
│   │   ├── 05-dev-tools/               Git, GitHub Actions, HTTPie, sandboxes
│   │   └── 06-learning/                Interactive coding challenges
│   │
│   ├── 04-platform-claude-code/        ← 18 skills (11%)
│   │   ├── 01-plugin-development/      Commands, hooks, skills, plugins, settings
│   │   ├── 02-skill-management/        Analytics, docs, doctor, manager, test suite
│   │   ├── 03-automation-governance/   Recommender, governor, writing rules
│   │   └── 04-workflow-routing/        Memory, pipeline, router, builder
│   │
│   ├── 05-data-acquisition/            ← 4 skills (2%)
│   │   ├── 01-web-scraping/            Firecrawl CLI
│   │   ├── 02-video-knowledge/         YouTube extraction, video knowledge
│   │   └── 03-media-generation/        Video generation
│   │
│   └── 06-domain-specific/             ← 2 skills (1%)
│       ├── 01-scientific-computing/    FEATool multiphysics
│       └── 02-payments-saas/           Stripe best practices
│
├── .specify/                           ← System configuration
│   ├── memory/                         Constitution & persistent context
│   ├── scripts/                        Utility scripts
│   └── specs/                          Specs, data models, plans, tasks
│
├── .vscode/                            Editor settings
├── SKILLS_CATALOG.md                   Human-readable categorized catalog
├── skills_index.json                   Machine-readable index with metadata
├── README.md                           This file
├── LICENSE                             MIT License
└── CONTRIBUTING.md                     Contribution guidelines
```

### Domain Distribution

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│   01 Trading ████████████████████████████████████████████░░░  106 (66%)│
│   03 SoftEng ████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   22 (14%)│
│   04 Claude  █████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   18 (11%)│
│   02 AI Dev  ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    9  (6%)│
│   05 Data    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    4  (2%)│
│   06 Domain  █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    2  (1%)│
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Domain Breakdown

### 01 — Trading (106 Skills)

The trading domain is the largest section, covering the complete lifecycle from data ingestion to automated execution. Skills are organized into 13 subcategories that mirror a professional trading operation.

#### Subcategories

| # | Subcategory | Skills | Description | Key Skills |
|---|-------------|--------|-------------|------------|
| 1 | Core Knowledge | 7 | Fundamentals, asset class primers | `trading-fundamentals` (641L), `crypto-defi-trading` (1,436L) |
| 2 | Analysis | 9 | Technical, fundamental, chart vision AI | `technical-analysis` (2,609L), `price-action` (1,188L) |
| 3 | Strategies | 22 | ICT/SMC, breakout, mean-reversion, sessions | `ict-smart-money` (2,658L), `session-scalping` (1,261L) |
| 4 | Market Context | 14 | Regime, macro, correlation, volatility | `cross-asset-relationships` (763L), `correlation-crisis` |
| 5 | Risk Management | 6 | Position sizing, drawdown, portfolio | `risk-and-portfolio` (2,020L), `real-time-risk-monitor` |
| 6 | Execution | 6 | Algo trading, HFT, prop trading | `market-making-hft` (1,335L), `execution-algo-trading` |
| 7 | Data & Signals | 7 | Ingestion, sentiment, news intelligence | `market-intelligence` (1,291L), `news-intelligence` |
| 8 | MT5 Platform | 3 | Integration, charts, expert advisors | `mt5-integration` (1,501L), `mt5-chart-browser` (602L) |
| 9 | Quant & ML | 9 | Backtesting, ML models, RL, statistics | `backtesting-sim` (1,156L), `ml-trading` (550L) |
| 10 | AI Trading Agents | 7 | Multi-agent, autonomous, prediction | `ai-trading-crew`, `freqtrade-bot` (550L) |
| 11 | Psychology & Ops | 3 | Trading psychology, journaling, plans | `trade-journal-analytics` (462L) |
| 12 | Infrastructure | 5 | Alerts, Telegram, Discord, Notion | `realtime-alert-pipeline`, `telegram-bot` |
| 13 | Orchestration | 8 | Master workflow, brain, autopilot | `brain-ecosystem-mcp` (4,437L), `trading-brain` (1,256L) |

#### Top 15 Skills by Size

| Skill | Lines | Subcategory | Has Code |
|-------|-------|-------------|----------|
| `brain-ecosystem-mcp` | 4,437 | Orchestration | Yes |
| `ict-smart-money` | 2,658 | Strategies | Yes |
| `technical-analysis` | 2,609 | Analysis | Yes |
| `risk-and-portfolio` | 2,020 | Risk Management | Yes |
| `crypto-defi-trading` | 1,436 | Core Knowledge | Yes |
| `market-intelligence` | 1,291 | Data & Signals | Yes |
| `trading-brain` | 1,256 | Orchestration | Yes |
| `session-scalping` | 1,261 | Strategies | Yes |
| `mt5-integration` | 1,501 | MT5 Platform | Yes |
| `market-making-hft` | 1,335 | Execution | Yes |
| `price-action` | 1,188 | Analysis | Yes |
| `backtesting-sim` | 1,156 | Quant & ML | Yes |
| `cross-asset-relationships` | 763 | Market Context | Yes |
| `liquidity-analysis` | 529 | Strategies | Yes |
| `freqtrade-bot` | 550 | AI Agents | Yes |

---

### 02 — AI Development (9 Skills)

Skills for building AI agents, integrating ML models, and engineering prompts.

| Skill | Kind | Lines | Description |
|-------|------|-------|-------------|
| `agent-development` | meta | 476 | Agent creation patterns, frontmatter, tools |
| `ai-agent-builder` | reference | 530 | Professional AI agent building guide |
| `deepagents-langchain` | agent | 167 | LangGraph production framework by LangChain |
| `agentic-storage` | reference | 297 | Persistent storage patterns for AI agents |
| `mcp-integration` | integration | 558 | Model Context Protocol for Claude Code plugins |
| `few-shot-quality-prompting` | reference | 463 | Prompt engineering for consistent high-quality output |
| `transformers-js` | tool | 641 | Run ML models in JavaScript/TypeScript |
| `openspec` | tool | 86 | Spec-driven AI coding methodology |
| `spec-kit` | orchestrator | 238 | Spec-driven project scaffolding |

```
AI Development Skill Map
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                      ┌──────────────┐
                      │  Agent Dev   │ (476L)
                      │  meta        │
                      └──────┬───────┘
                             │
                 ┌───────────┼───────────┐
                 ▼           ▼           ▼
          ┌────────────┐ ┌──────────┐ ┌──────────────┐
          │ AI Agent   │ │ DeepAgent│ │ Agentic      │
          │ Builder    │ │ LangChain│ │ Storage      │
          │ (530L)     │ │ (167L)   │ │ (297L)       │
          └────────────┘ └──────────┘ └──────────────┘
                                          │
                                    ┌─────┴──────┐
                                    │ MCP Integ. │ (558L)
                                    └────────────┘

          ┌──────────────┐    ┌───────────────────┐
          │ Few-Shot     │    │ Transformers.js   │ (641L)
          │ Prompting    │    │ ML in JS/TS       │
          │ (463L)       │    └───────────────────┘
          └──────────────┘

          ┌──────────────┐    ┌───────────────────┐
          │ OpenSpec     │───▶│ Spec-Kit          │ (238L)
          │ (86L)        │    │ Orchestrator      │
          └──────────────┘    └───────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### 03 — Software Engineering (22 Skills)

Full-stack development skills covering architecture, quality, testing, UI, and tools.

| Subcategory | Skills | Highlights |
|-------------|--------|------------|
| **Architecture** | 5 | `gitnexus-codebase-intelligence` (1,034L), `pro-code-architecture`, `build-your-own-x`, `system-design-academy` |
| **Code Review** | 2 | `code-review`, `generate-snapshot` |
| **Testing** | 5 | `run-e2e-tests`, `run-integration-tests`, `run-smoke-tests`, `run-pre-commit-checks`, `debug-failing-test` |
| **UI Design** | 4 | `elite-ui-design`, `frontend-design`, `programmatic-drawing` (498L), `playground` (432L) |
| **Dev Tools** | 6 | `git-phase-restore` (367L), `httpie-cli` (285L), `github-actions-trigger`, `e2b-sandboxes` |
| **Learning** | 1 | `interactive-coding-challenges` |

#### Testing Workflow

```
┌─────────────────────────────────────────────────────┐
│                 Testing Skill Pipeline               │
│                                                      │
│  ┌──────────────┐   ┌──────────────┐                │
│  │ Pre-Commit   │──▶│ Unit Tests   │                │
│  │ Checks (137L)│   │ (via hooks)  │                │
│  └──────────────┘   └──────┬───────┘                │
│                             │                        │
│                     ┌───────▼───────┐                │
│                     │ Smoke Tests   │                │
│                     │ (131L)        │                │
│                     └───────┬───────┘                │
│                             │                        │
│              ┌──────────────┼──────────────┐         │
│              ▼                             ▼         │
│  ┌──────────────────┐         ┌──────────────────┐  │
│  │ Integration Tests│         │ Debug Failing    │  │
│  │ (117L)           │         │ Test (94L)       │  │
│  └────────┬─────────┘         └──────────────────┘  │
│           │                                          │
│           ▼                                          │
│  ┌──────────────────┐                               │
│  │ E2E Tests (130L) │                               │
│  └──────────────────┘                               │
└─────────────────────────────────────────────────────┘
```

---

### 04 — Claude Code Platform (18 Skills)

Skills for extending and managing the Claude Code ecosystem — plugins, hooks, commands, skill management, workflow routing, and governance.

| Subcategory | Skills | Purpose |
|-------------|--------|---------|
| **Plugin Development** | 5 | `command-development` (839L), `hook-development` (717L), `skill-development` (642L), `plugin-settings` (549L), `plugin-structure` (481L) |
| **Skill Management** | 5 | `skill-analytics`, `skill-docs-generator`, `skill-doctor`, `skill-manager`, `skill-test-suite` |
| **Automation Governance** | 4 | `claude-automation-recommender` (308L), `claude-md-improver`, `skill-execution-governor`, `writing-hookify-rules` |
| **Workflow Routing** | 4 | `context-memory`, `skill-pipeline`, `smart-skill-router`, `workflow-builder` |

#### Plugin Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    Claude Code Plugin                         │
│                                                               │
│  plugin.json ─────────┬──────────────────────────────────    │
│                       │                                       │
│  ┌─────────────┐     │     ┌──────────────────┐              │
│  │ Commands    │─────┤     │ Skills (.md)     │              │
│  │ /my-command │     │     │ ── knowledge      │              │
│  └─────────────┘     │     │ ── triggers       │              │
│                       │     │ ── code blocks    │              │
│  ┌─────────────┐     │     └──────────────────┘              │
│  │ Hooks       │─────┤                                       │
│  │ PreToolUse  │     │     ┌──────────────────┐              │
│  │ PostToolUse │     ├────▶│ Settings (.md)   │              │
│  │ Stop        │     │     │ ── YAML config    │              │
│  └─────────────┘     │     └──────────────────┘              │
│                       │                                       │
│  ┌─────────────┐     │     ┌──────────────────┐              │
│  │ MCP Servers │─────┘     │ .mcp.json        │              │
│  │ (external)  │           │ ── tool registry  │              │
│  └─────────────┘           └──────────────────┘              │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

### 05 — Data Acquisition (4 Skills)

| Skill | Lines | Description |
|-------|-------|-------------|
| `firecrawl-cli` | 540 | Web scraping with Firecrawl — crawl, scrape, map URLs |
| `video-knowledge-extractor` | 67 | Extract knowledge from video content |
| `youtube-video-to-knowledge` | 296 | Convert YouTube videos into structured knowledge |
| `video-gen` | 174 | AI-powered video generation |

### 06 — Domain Specific (2 Skills)

| Skill | Lines | Description |
|-------|-------|-------------|
| `featool-multiphysics` | 223 | FEATool multiphysics simulation (FEM/CFD) |
| `stripe-best-practices` | 34 | Stripe payment integration best practices |

---

## Trading Lifecycle Map

This diagram shows how the 106 trading skills connect across the complete trading lifecycle — from data infrastructure to automated execution:

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                        TRADING LIFECYCLE — 18 PHASES                        ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  PHASE 1 — INFRASTRUCTURE                                                   ║
║  ┌─────────────────┐ ┌──────────────┐ ┌─────────────┐ ┌──────────────────┐  ║
║  │ market-data-    │ │ tick-data-   │ │ mt5-        │ │ mt5-chart-      │  ║
║  │ ingestion       │ │ storage      │ │ integration │ │ browser         │  ║
║  └────────┬────────┘ └──────┬───────┘ └──────┬──────┘ └───────┬─────────┘  ║
║           │                 │                │                │              ║
║  ┌────────┴────────┐ ┌──────┴───────┐ ┌──────┴──────┐                       ║
║  │ realtime-alert- │ │ telegram-bot │ │ discord-    │ │ notion-sync       │  ║
║  │ pipeline        │ │              │ │ webhook     │ │                    │  ║
║  └─────────────────┘ └──────────────┘ └─────────────┘ └────────────────────┘  ║
║                                                                              ║
║  PHASE 2 — MACRO CONTEXT          PHASE 3 — REGIME                         ║
║  ┌───────────────────┐            ┌──────────────────┐                       ║
║  │ news-intelligence │────────────│ market-regime-   │                       ║
║  │ economic-calendar │            │ classifier       │                       ║
║  │ macro-dashboard   │            └────────┬─────────┘                       ║
║  │ cross-asset-rel.  │                     │                                  ║
║  │ institutional-tl  │                     ▼                                  ║
║  │ market-intel.     │            ┌──────────────────┐                       ║
║  └───────────────────┘            │ correlation-     │                       ║
║                                   │ regime-switcher  │                       ║
║                                   └──────────────────┘                       ║
║                                                                              ║
║  PHASE 4 — ANALYSIS               PHASE 5 — STRATEGY                       ║
║  ┌───────────────────┐            ┌──────────────────┐                       ║
║  │ price-action      │────────────│ ict-smart-money  │                       ║
║  │ technical-analysis│            │ breakout-engine  │                       ║
║  │ volume-analysis   │            │ mean-reversion   │                       ║
║  │ fibonacci-harmonic│            │ session-scalping │                       ║
║  │ elliott-wave      │            │ grid-trading     │                       ║
║  │ chart-vision (AI) │            │ strategy-select  │                       ║
║  └───────────────────┘            └──────────────────┘                       ║
║                                                                              ║
║  PHASE 6 — RISK                   PHASE 7 — EXECUTION                      ║
║  ┌───────────────────┐            ┌──────────────────┐                       ║
║  │ risk-of-ruin      │────────────│ execution-algo   │                       ║
║  │ drawdown-playbook │            │ market-making-hft│                       ║
║  │ portfolio-optim.  │            │ spread-slippage  │                       ║
║  │ real-time-risk    │            │ hedgequantx-prop │                       ║
║  └───────────────────┘            └──────────────────┘                       ║
║                                                                              ║
║  PHASE 8 — REVIEW & OPTIMIZE                                                ║
║  ┌───────────────┐ ┌───────────────┐ ┌──────────────┐ ┌─────────────────┐   ║
║  │ backtesting-  │ │ ml-trading    │ │ strategy-    │ │ trade-journal-  │   ║
║  │ sim           │ │ tensortrade   │ │ validation   │ │ analytics       │   ║
║  └───────────────┘ └───────────────┘ └──────────────┘ └─────────────────┘   ║
║                                                                              ║
║  ORCHESTRATION LAYER (runs everything)                                       ║
║  ┌──────────────────────────────────────────────────────────────────────┐    ║
║  │ trading-brain (1,256L) → brain-ecosystem-mcp (4,437L)              │    ║
║  │ master-trading-workflow (474L) → trading-autopilot → analyze       │    ║
║  └──────────────────────────────────────────────────────────────────────┘    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## Skill Graph

Skills reference each other through the `related_skills` field, creating a navigable knowledge graph. Here's a simplified view of key connections:

```
                              ┌─────────────────┐
                              │  trading-brain   │ ◄── Master Orchestrator
                              │  (1,256L)        │
                              └──┬──┬──┬──┬──┬──┘
                                 │  │  │  │  │
                    ┌────────────┘  │  │  │  └──────────────┐
                    ▼               │  │  │                  ▼
           ┌───────────────┐       │  │  │        ┌──────────────────┐
           │ risk-and-     │       │  │  │        │ multi-strategy   │
           │ portfolio     │       │  │  │        │ orchestration    │
           │ (2,020L)      │       │  │  │        └──────────────────┘
           └───────┬───────┘       │  │  │
                   │               │  │  │
        ┌──────────┼──────┐       │  │  │
        ▼          ▼      ▼       │  │  │
  ┌──────────┐ ┌───────┐ ┌─────┐ │  │  │
  │ risk-of- │ │drawdown│ │port-│ │  │  │
  │ ruin     │ │playbook│ │optim│ │  │  │
  └──────────┘ └───────┘ └─────┘ │  │  │
                                   │  │  │
     ┌─────────────────────────────┘  │  └─────────────────────┐
     ▼                                ▼                         ▼
  ┌──────────────┐         ┌──────────────────┐      ┌──────────────┐
  │ mt5-         │         │ market-intel     │      │ execution-   │
  │ integration  │         │ (1,291L)         │      │ algo-trading │
  │ (1,501L)     │         └──────┬───────────┘      └──────────────┘
  └──────┬───────┘                │
         │              ┌─────────┼─────────┐
         ▼              ▼         ▼         ▼
  ┌──────────────┐ ┌────────┐ ┌───────┐ ┌──────────┐
  │ mt5-chart-   │ │ news-  │ │social │ │ economic │
  │ browser      │ │ intel  │ │senti. │ │ calendar │
  └──────────────┘ └────────┘ └───────┘ └──────────┘
```

---

## How to Use

### With AI Coding Assistants

```
1. Point your AI assistant to the classified/ directory
2. The assistant reads skills_index.json to discover relevant skills
3. Skills are loaded on-demand based on your request keywords
4. Code blocks in skills are executed or adapted by the AI
```

**Example prompts:**
```
"Analyze EURUSD using ICT concepts"     → loads ict-smart-money
"Build a backtesting system"             → loads backtesting-sim
"Set up MCP for my plugin"              → loads mcp-integration
"Create a visual diagram"               → loads programmatic-drawing
"Review my trading risk"                → loads risk-and-portfolio
```

### As a Reference Library

```bash
# Browse the full catalog
cat SKILLS_CATALOG.md

# Search for a skill by keyword
grep -r "order block" classified/

# Query the JSON index
python -c "
import json
idx = json.load(open('skills_index.json'))
# Find all skills tagged 'ict'
for s in idx['skills']:
    if 'ict' in s['tags']:
        print(f\"{s['name']:30s} {s['path']}\")
"

# List all skills with code
python -c "
import json
idx = json.load(open('skills_index.json'))
code_skills = [s for s in idx['skills'] if s['has_code']]
print(f'{len(code_skills)} of {len(idx[\"skills\"])} skills contain executable code')
"
```

### With VS Code / Cursor

The included `.vscode/settings.json` enables Copilot agent mode. Reference skills via `@file` in your AI chat:

```
@file classified/01-trading/03-strategies/01-ict-smart-money/ict-smart-money.md
```

---

## Index Files

| File | Format | Description |
|------|--------|-------------|
| [`SKILLS_CATALOG.md`](SKILLS_CATALOG.md) | Markdown | Human-readable catalog — grouped by 33 categories with line counts |
| [`skills_index.json`](skills_index.json) | JSON | Machine-readable — 161 entries with name, path, kind, category, tags, related skills, line count |
| [`.specify/specs/`](.specify/specs/) | Mixed | System specs, data models, API contracts, plans, and task breakdowns |
| [`.specify/memory/`](.specify/memory/) | Markdown | Constitution and persistent context for AI sessions |

### JSON Index Schema

```json
{
  "version": "3.0",
  "generated": "2026-03-19",
  "total_skills": 161,
  "skills": [
    {
      "name": "skill-name",
      "description": "What the skill does + trigger keywords",
      "path": "01-trading/03-strategies/.../skill-name.md",
      "kind": "reference | engine | tool | workflow | ...",
      "category": "trading/strategies",
      "status": "active",
      "tags": ["trading", "strategy", "ict"],
      "related_skills": ["other-skill-1", "other-skill-2"],
      "lines": 2658,
      "has_code": true
    }
  ]
}
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

**Quick start:**
1. Place your `.md` skill in the right `classified/` subdirectory
2. Add an entry to `skills_index.json` with full metadata
3. Add an entry to `SKILLS_CATALOG.md` in the right category
4. Open a PR

## License

[MIT](LICENSE) — use freely in personal and commercial projects.
