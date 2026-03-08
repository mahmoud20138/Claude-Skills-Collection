# Claude Skills Collection

**Created:** March 5, 2026
**Last Updated:** March 5, 2026
**Location:** C:/Users/Mamoud/Desktop/Claude-Skills-Collection/
**Total Skills:** 69 across 7 categories

## Overview

This folder contains a comprehensive collection of all Claude-related skills, prompts, and automation tools gathered from various locations on your system.

> **See also:** [SKILL-INDEX.md](SKILL-INDEX.md) for the complete master index with trigger keywords for every skill.

## Directory Structure

```
Claude-Skills-Collection/
├── README.md (this file)
├── SKILL-INDEX.md (master index with all skills)
├── EXPORT-SUMMARY.md (export/backup log)
│
├── 01-Custom-Claude-Skills/          (6 skills)
│   ├── ai-agent-builder.md
│   ├── elite-ui-design.md
│   ├── few-shot-quality-prompting.md
│   ├── ict-trading-strategy.md
│   ├── pro-code-architecture.md
│   └── programmatic-drawing.md
│
├── 02-Azure-Skills/                  (24 skills)
│   ├── azure-ai/
│   ├── azure-aigateway/
│   ├── azure-cloud-migrate/
│   ├── azure-compliance/
│   ├── azure-compute/
│   ├── azure-cost-optimization/
│   ├── azure-deploy/
│   ├── azure-diagnostics/
│   ├── azure-hosted-copilot-sdk/
│   ├── azure-kusto/
│   ├── azure-messaging/
│   ├── azure-observability/
│   ├── azure-postgres/
│   ├── azure-prepare/
│   ├── azure-rbac/
│   ├── azure-resource-lookup/
│   ├── azure-resource-visualizer/
│   ├── azure-storage/
│   ├── azure-validate/
│   ├── entra-app-registration/
│   ├── microsoft-foundry/
│   ├── appinsights-instrumentation/
│   ├── git-phase-restore/
│   └── skill-creator/
│
├── 03-Claude-Plugin-Skills/          (10 skills)
│   ├── claude-automation-recommender/
│   ├── claude-md-improver/
│   ├── frontend-design/
│   ├── example-skill/
│   ├── writing-rules/
│   ├── agent-development/
│   ├── command-development/
│   ├── hook-development/
│   ├── mcp-integration/
│   └── skill-development/
│
├── 04-AITK-Prompts/                  (7 prompts)
│   ├── browser-use/
│   ├── claude-opus-4-5-migration/
│   ├── context7-docs-lookup/
│   ├── create-pr/
│   ├── electron-chromium-upgrade/
│   ├── fix/
│   └── tools/
│
├── 05-VSCode-Extension-Skills/       (9 skills)
│   ├── cross-platform-paths/
│   ├── debug-failing-test/
│   ├── generate-snapshot/
│   ├── python-manager-discovery/
│   ├── run-e2e-tests/
│   ├── run-integration-tests/
│   ├── run-pre-commit-checks/
│   ├── run-smoke-tests/
│   └── settings-precedence/
│
├── 06-OpenCode-Skills/               (5 packages)
│   ├── @opencode-ai/sdk (v1.2.15 & v1.2.16)
│   ├── @opencode-ai/plugin (v1.2.15 & v1.2.16)
│   ├── anthropic.claude-code-2.1.63-win32-x64/
│   └── README.md
│
└── 07-Trading-Skills/                (8 skills) ← NEW
    ├── mql5-indicator-development/
    ├── mql5-ea-development/
    ├── ict-market-structure/
    ├── ict-order-blocks/
    ├── ict-liquidity-concepts/
    ├── multi-timeframe-analysis/
    ├── risk-management-engine/
    └── backtesting-optimization/
```

## Skills Inventory

### 1. Custom Claude Skills (6 Skills)
Located in: `01-Custom-Claude-Skills/`
Source: `C:/Users/Mamoud/.claude/skills/`

1. **ai-agent-builder.md**
   - **Purpose:** Build AI-powered coding agents with tool use and multi-step orchestration
   - **Triggers:** "agent", "agentic", "tool use", "function calling"
   - **Key Features:** Agent architecture, tool design, skill loading, context management

2. **elite-ui-design.md**
   - **Purpose:** Generate production-grade, visually stunning UI code
   - **Triggers:** "beautiful UI", "polished", "pro-level design", "dashboard"
   - **Key Features:** Design systems, typography, animations, accessibility

3. **few-shot-quality-prompting.md**
   - **Purpose:** Master prompt engineering for professional AI output
   - **Triggers:** "prompt engineering", "better results", "improve output"
   - **Key Features:** 7-layer prompts, few-shot patterns, evaluation frameworks

4. **ict-trading-strategy.md**
   - **Purpose:** ICT Smart Money Concepts and MQL5 trading
   - **Triggers:** "ICT", "Smart Money", "trading strategy", "order blocks"
   - **Key Features:** Market structure, liquidity, PD arrays, risk management

5. **pro-code-architecture.md**
   - **Purpose:** Senior-engineer-level code architecture
   - **Triggers:** "clean code", "production-grade", "refactor", "best practices"
   - **Key Features:** SOLID principles, design patterns, error handling, testing

6. **programmatic-drawing.md**
   - **Purpose:** Generate visual art and diagrams through code
   - **Triggers:** "draw", "illustrate", "visualize", "diagram"
   - **Key Features:** SVG, Canvas, p5.js, Three.js, D3.js

---

### 2. Azure Skills (24 Skills)
Located in: `02-Azure-Skills/`
Source: `C:/Users/Mamoud/.agents/skills/`

1. **azure-ai** - Azure AI Search, Speech, OpenAI, Document Intelligence
2. **azure-aigateway** - API Management as AI Gateway
3. **azure-cloud-migrate** - Migrate AWS/GCP to Azure
4. **azure-compliance** - Security audits, compliance, Key Vault monitoring
5. **azure-compute** - VM recommendations, VMSS
6. **azure-cost-optimization** - Cost analysis and optimization
7. **azure-deploy** - Deploy to Azure (azd up, Bicep, Terraform)
8. **azure-diagnostics** - Debug production issues (Container/Function Apps)
9. **azure-hosted-copilot-sdk** - GitHub Copilot SDK apps
10. **azure-kusto** - Azure Data Explorer, KQL queries
11. **azure-messaging** - Event Hubs, Service Bus troubleshooting
12. **azure-observability** - Monitor, App Insights, Log Analytics
13. **azure-postgres** - PostgreSQL with Entra ID passwordless auth
14. **azure-prepare** - Prepare apps for Azure deployment
15. **azure-rbac** - Role assignments, least-privilege access
16. **azure-resource-lookup** - List/find Azure resources
17. **azure-resource-visualizer** - Architecture diagrams (Mermaid)
18. **azure-storage** - Blob, File, Queue, Table storage
19. **azure-validate** - Pre-deployment validation
20. **entra-app-registration** - Azure AD app registration, OAuth 2.0, MSAL
21. **microsoft-foundry** - AI Foundry, models, agents, RBAC
22. **appinsights-instrumentation** - App Insights SDK instrumentation
23. **git-phase-restore** - Restore to previous project phases via Git
24. **skill-creator** - Create new skills

---

### 3. Claude Plugin Skills (10 Skills)
Located in: `03-Claude-Plugin-Skills/`
Source: `C:/Users/Mamoud/.claude/plugins/marketplaces/claude-plugins-official/plugins/`

1. **claude-automation-recommender** - Codebase automation analysis
2. **claude-md-improver** - CLAUDE.md file auditing
3. **frontend-design** - Distinct frontend design
4. **example-skill** - Skill template example
5. **writing-rules** - Automation rules
6. **agent-development** - Agent creation patterns
7. **command-development** - Command creation
8. **hook-development** - Hook creation patterns
9. **mcp-integration** - MCP server setup
10. **skill-development** - Skill development workflow

---

### 4. AITK Prompts (7 Prompts)
Located in: `04-AITK-Prompts/`
Source: `C:/Users/Mamoud/.aitk/prompts/`

1. **browser-use** - Browser automation
2. **claude-opus-4-5-migration** - Claude migration guide
3. **context7-docs-lookup** - Documentation lookup
4. **create-pr** - Pull request creation
5. **electron-chromium-upgrade** - Electron upgrades
6. **fix** - Intelligent bug fixing
7. **tools** - General-purpose tooling

---

### 5. VSCode Extension Skills (9 Skills)
Located in: `05-VSCode-Extension-Skills/`
Source: `C:/Users/Mamoud/.antigravity/extensions/ms-python.vscode-python-envs-*/`

1. **cross-platform-paths** - Cross-platform path handling
2. **debug-failing-test** - Test debugging
3. **generate-snapshot** - Snapshot generation
4. **python-manager-discovery** - Python environment discovery
5. **run-e2e-tests** - End-to-end testing
6. **run-integration-tests** - Integration testing
7. **run-pre-commit-checks** - Pre-commit validation
8. **run-smoke-tests** - Smoke testing
9. **settings-precedence** - Settings management

---

### 6. OpenCode Skills (5 Packages)
Located in: `06-OpenCode-Skills/`

1. **@opencode-ai/sdk (v1.2.15)** - AI SDK client/server library
2. **@opencode-ai/sdk (v1.2.16)** - Latest SDK with V2 API
3. **@opencode-ai/plugin (v1.2.15)** - Plugin development framework
4. **@opencode-ai/plugin (v1.2.16)** - Latest plugin with Zod validation
5. **Claude Code Extension (v2.1.63)** - VSCode integration walkthrough

---

### 7. Trading Skills (8 Skills) — NEW
Located in: `07-Trading-Skills/`

1. **mql5-indicator-development** - Build custom MT5 indicators with proper buffer management
2. **mql5-ea-development** - Create Expert Advisors with entry/exit logic and risk management
3. **ict-market-structure** - Identify market structure shifts (BOS, CHoCH) using ICT concepts
4. **ict-order-blocks** - Detect and trade order blocks, breaker blocks, mitigation blocks
5. **ict-liquidity-concepts** - Map liquidity pools, sweeps, and fair value gaps for entries
6. **multi-timeframe-analysis** - Implement top-down multi-timeframe analysis in MQL5
7. **risk-management-engine** - Position sizing, risk-per-trade, and drawdown control systems
8. **backtesting-optimization** - Strategy tester optimization, walk-forward analysis, validation

---

## How to Use These Skills

### Method 1: Direct File Access
Simply navigate to the skill folder and read the SKILL.md file to understand what the skill does and how to use it.

### Method 2: Claude Code Integration
Skills are automatically loaded by Claude Code based on triggers in the skill description.

### Method 3: Manual Loading
You can manually invoke skills using Claude Code commands or by referencing the skill in your prompts.

---

## Total Skills Count

| Category | Count |
|----------|-------|
| Custom Claude Skills | 6 |
| Azure Skills | 24 |
| Claude Plugin Skills | 10 |
| AITK Prompts | 7 |
| VSCode Extension Skills | 9 |
| OpenCode Skills | 5 |
| Trading Skills (NEW) | 8 |
| **TOTAL** | **69 professional skills** |

---

## Backup Information

**Created from:**
- `C:/Users/Mamoud/.claude/skills/`
- `C:/Users/Mamoud/.agents/skills/`
- `C:/Users/Mamoud/.claude/plugins/marketplaces/claude-plugins-official/plugins/`
- `C:/Users/Mamoud/.aitk/prompts/`
- `C:/Users/Mamoud/.antigravity/extensions/`
- `C:/Users/Mamoud/AppData/Roaming/MetaQuotes/Terminal/*/MQL5/` (Trading Skills)

**Backup Date:** March 5, 2026
**Total Size:** ~20-25 MB

---

## Quick Reference

### Most Commonly Used Skills:
1. **ai-agent-builder** - For building AI agents
2. **elite-ui-design** - For beautiful UI design
3. **pro-code-architecture** - For production code
4. **ict-trading-strategy** - For trading applications
5. **programmatic-drawing** - For visual generation
6. **azure-deploy** - For Azure deployments
7. **skill-creator** - For creating new skills
8. **mql5-ea-development** - For MQL5 Expert Advisors (NEW)
9. **risk-management-engine** - For trade risk management (NEW)

### Skill Triggering
Skills automatically trigger based on keywords in your prompts. Each skill has specific trigger phrases defined in its description. See [SKILL-INDEX.md](SKILL-INDEX.md) for the complete trigger keyword reference.

---

## Maintenance

To update this collection:
1. Re-run the collection script
2. Or manually copy new skills to the appropriate subfolder
3. Update this README with new additions
4. Update SKILL-INDEX.md with the new skill entries

---

## Changelog

### March 5, 2026 — v2.0 (Major Update)
- **Added** `07-Trading-Skills/` with 8 new MQL5/MT5 trading automation skills
- **Cleaned up** duplicate folders (removed empty `04-VSCode-Extension-Skills`, `05-AITK-Prompts`, `06-Project-Skills`)
- **Updated** VSCode Extension Skills count from 5 → 9 (discovered 4 additional skills)
- **Updated** total skills count from 52 → 69
- **Created** comprehensive `SKILL-INDEX.md` master index with trigger keywords

### March 5, 2026 — v1.0 (Initial)
- Initial collection of 52+ skills across 6 categories

---

## Notes

- All skills are in their original format (SKILL.md files with YAML frontmatter)
- Skills can be edited/customized as needed
- Some skills may have additional reference files in their directories
- The collection preserves the original directory structure where applicable
- Trading Skills are designed for MetaTrader 5 / MQL5 development

---

**Enjoy your comprehensive skills collection!** 🚀
