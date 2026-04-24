# Bastos' Ruby Plugin Marketplace

A curated collection of Ruby plugins for Codex and Claude Code.

## Available Plugins

| Plugin | Description |
|--------|-------------|
| [ruby](plugins/ruby/) | Ruby development toolkit with 8 skills, 5 commands, and 1 agent |
| [ruby-on-rails](plugins/ruby-on-rails/) | Comprehensive Rails development toolkit with 16 skills, 8 commands, and 3 agents |
| [rspec](plugins/rspec/) | Comprehensive RSpec testing toolkit with 7 skills, 3 commands, and 2 agents |

## Installation

### Add the marketplace

```bash
/plugin marketplace add bastos/ruby-plugin-marketplace
```

Or with a local path:

```bash
/plugin marketplace add ./path/to/ruby-plugin-marketplace
```

### Install a plugin

Use the marketplace name shown by your client. Codex currently registers this
GitHub marketplace as `bastos-ruby-plugin-marketplace`.

Ruby (core):

```bash
/plugin install ruby@bastos-ruby-plugin-marketplace
```

Ruby on Rails:

```bash
/plugin install ruby-on-rails@bastos-ruby-plugin-marketplace
```

RSpec:

```bash
/plugin install rspec@bastos-ruby-plugin-marketplace
```

## Structure

```
.
├── .codex-plugin/
│   └── marketplace.json     # Codex marketplace manifest
├── .claude-plugin/
│   └── marketplace.json     # Claude Code marketplace manifest
└── plugins/
    ├── ruby/                # Ruby development toolkit
    │   ├── .codex-plugin/
    │   ├── .claude-plugin/
    │   ├── agents/
    │   ├── commands/
    │   └── skills/
    ├── ruby-on-rails/       # Rails development toolkit
    │   ├── .codex-plugin/
    │   ├── .claude-plugin/
    │   ├── agents/
    │   ├── commands/
    │   ├── skills/
    │   └── scripts/
    └── rspec/               # RSpec testing toolkit
        ├── .codex-plugin/
        ├── .claude-plugin/
        ├── agents/
        ├── commands/
        └── skills/
```

## Contributing

1. Create a new plugin in `plugins/<plugin-name>/`
2. Add `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json` manifests
3. Add the plugin entry to `.codex-plugin/marketplace.json` and `.claude-plugin/marketplace.json`
4. Submit a pull request

## License

MIT
