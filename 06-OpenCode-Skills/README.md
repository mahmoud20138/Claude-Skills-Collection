# OpenCode AI Skills Collection

**Created:** March 5, 2026
**Location:** C:/Users/Mamoud/Desktop/Claude-Skills-Collection/06-OpenCode-skills/

## Overview

This folder contains OpenCode AI SDK and Plugin tools for building AI-powered coding assistants and tools.

---

## 📦 OpenCode AI SDK (@opencode-ai/sdk)

**Version:** 1.2.16
**License:** MIT

### Features

- **Client Library** - Build AI-powered clients
- **Server Framework** - Create AI tool servers
- **V2 API** - Latest generation API
- **TypeScript Support** - Full type definitions

### Exports

```javascript
// Main SDK
import { ... } from '@opencode-ai/sdk'

// Client only
import { ... } from '@opencode-ai/sdk/client'

// Server only
import { ... } from '@opencode-ai/sdk/server'

// V2 API
import { ... } from '@opencode-ai/sdk/v2'
import { ... } from '@opencode-ai/sdk/v2/client'
import { ... } from '@opencode-ai/sdk/v2/server'
```

---

## 🔌 OpenCode AI Plugin (@opencode-ai/plugin)

**Version:** 1.2.16
**License:** MIT

### Features

- **Plugin Development** - Build custom plugins
- **Tool Integration** - Create AI tools
- **Shell Commands** - Execute shell commands
- **Example Templates** - Ready-to-use examples

### Exports

```javascript
// Main Plugin API
import { ... } from '@opencode-ai/plugin'

// Tool utilities
import { ... } from '@opencode-ai/plugin/tool'

// Shell execution
import { ... } from '@opencode-ai/plugin/shell'
```

---

## 📁 File Structure

```
06-OpenCode-skills/
├── @opencode-ai/
│   ├── plugin@1.2.15@@@1/
│   │   ├── dist/
│   │   │   ├── index.js
│   │   │   ├── index.d.ts
│   │   │   ├── tool.js
│   │   │   ├── tool.d.ts
│   │   │   ├── shell.js
│   │   │   ├── shell.d.ts
│   │   │   ├── example.js
│   │   │   └── example.d.ts
│   │   └── package.json
│   │
│   ├── plugin@1.2.16@@@1/
│   │   └── [same structure as above]
│   │
│   ├── sdk@1.2.15@@@1/
│   │   ├── dist/
│   │   │   ├── index.js
│   │   │   ├── index.d.ts
│   │   │   ├── client.js
│   │   │   ├── client.d.ts
│   │   │   ├── server.js
│   │   │   ├── server.d.ts
│   │   │   └── v2/
│   │   └── package.json
│   │
│   └── sdk@1.2.16@@@1/
│       └── [same structure as above]
│
├── anthropic.claude-code-2.1.63-win32-x64/
│   ├── README.md
│   └── resources/
│       └── walkthrough/
│           ├── step1.md
│           ├── step2.md
│           ├── step3.md
│           └── step4.md
│
└── README.md (this file)
```

---

## 🚀 Quick Start

### Using the SDK

```javascript
import { Client } from '@opencode-ai/sdk/v2/client'

const client = new Client({
  apiKey: process.env.OPENCODE_API_KEY
})

// Use the client
const result = await client.generateCode({
  prompt: "Create a React component"
})
```

### Creating a Plugin

```javascript
import { Tool, Shell } from '@opencode-ai/plugin'

const myTool = new Tool({
  name: "my-custom-tool",
  description: "Does something useful",
  execute: async (input) => {
    // Your logic here
    return result
  }
})

export default myTool
```

---

## 📚 Documentation

### OpenCode AI SDK

- **Client API** - For consuming AI services
- **Server API** - For building AI tool servers
- **V2 API** - Latest features and improvements

### OpenCode AI Plugin

- **Tool API** - Create custom tools
- **Shell API** - Execute shell commands safely
- **Example Templates** - Get started quickly

---

## 🔧 Dependencies

### SDK Dependencies
- None (zero runtime dependencies)

### Plugin Dependencies
- `@opencode-ai/sdk` (peer dependency)
- `zod` (for schema validation)

---

## 💡 Use Cases

1. **Build AI Tools** - Create custom AI-powered tools
2. **Plugin Development** - Extend OpenCode AI capabilities
3. **Client Integration** - Integrate OpenCode AI into your apps
4. **Server Deployment** - Deploy AI tool servers
5. **Shell Automation** - Automate shell commands with AI

---

## 🎯 Key Features

### SDK Features
- ✅ Zero dependencies
- ✅ Full TypeScript support
- ✅ V2 API with improved ergonomics
- ✅ Client & Server libraries
- ✅ OpenAPI-generated types

### Plugin Features
- ✅ Tool creation framework
- ✅ Shell execution utilities
- ✅ Example templates
- ✅ Zod schema validation
- ✅ TypeScript support

---

## 📖 Resources

### Included Walkthrough
The `anthropic.claude-code-2.1.63-win32-x64/resources/walkthrough/` folder contains:
- **Step 1** - Getting started
- **Step 2** - Basic usage
- **Step 3** - Advanced features
- **Step 4** - Best practices

---

## 🔗 Related Links

- OpenCode AI Documentation: https://opencode.ai/docs
- Plugin Development Guide: https://opencode.ai/docs/plugins
- SDK Reference: https://opencode.ai/docs/sdk

---

**Total Packages:** 4 (2 SDK versions + 2 Plugin versions)
**Last Updated:** March 5, 2026
