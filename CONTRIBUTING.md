# Contributing to Claude Skills Collection

Thank you for considering contributing!

## How to Contribute

### Add a New Skill

1. Fork the repository
2. Choose the correct category folder (01-07)
3. Create a new skill file or folder following the existing structure
4. Add your skill to `SKILL-INDEX.md`
5. Update the skills count in `README.md`
6. Submit a Pull Request

### Skill File Format

Each skill should include:
- **Name** - Clear, descriptive name
- **Description** - What the skill does
- **Trigger keywords** - Words that activate the skill
- **Instructions** - Step-by-step workflow
- **References** (optional) - Links to docs, SDKs, examples

### Categories

| Folder | Category | Topics |
|--------|----------|--------|
| `01-Custom-Claude-Skills/` | General | AI agents, UI, architecture, prompts |
| `02-Azure-Skills/` | Azure Cloud | Deploy, compute, storage, compliance |
| `03-Claude-Plugin-Skills/` | Plugins | Agents, commands, hooks, MCP |
| `04-AITK-Prompts/` | Prompts | Browser, fixes, PRs, tools |
| `05-VSCode-Extension-Skills/` | VSCode | Testing, debugging, environments |
| `06-OpenCode-Skills/` | OpenCode | SDK, plugins, extensions |
| `07-Trading-Skills/` | Trading | MQL5, ICT, risk, backtesting |

### Reporting Issues

- Use [GitHub Issues](https://github.com/mahmoud20138/Claude-Skills-Collection/issues)
- Include the skill name and category
- Describe the expected vs actual behavior

## Guidelines

- Keep skill descriptions concise
- Include trigger keywords for auto-loading
- Follow the existing folder structure
- Test skills with Claude Code before submitting
- No external dependencies unless absolutely necessary
