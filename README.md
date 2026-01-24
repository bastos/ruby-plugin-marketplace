# Bastos' Ruby Plugin Marketplace

A curated collection of Ruby plugins for Claude Code.

## Available Plugins

| Plugin | Description |
|--------|-------------|
| [ruby](plugins/ruby/) | Ruby development toolkit with 8 skills, 5 commands, and 1 agent |
| [ruby-on-rails](plugins/ruby-on-rails/) | Comprehensive Rails development toolkit with 15 skills, 8 commands, and 3 agents |
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

Ruby (core):

```bash
/plugin install ruby@ruby-plugin-marketplace
```

Ruby on Rails:

```bash
/plugin install ruby-on-rails@ruby-plugin-marketplace
```

RSpec:

```bash
/plugin install rspec@ruby-plugin-marketplace
```

## Structure

```
.
├── .claude-plugin/
│   └── marketplace.json     # Marketplace manifest
└── plugins/
    ├── ruby/                # Ruby development toolkit
    │   ├── .claude-plugin/
    │   ├── agents/
    │   ├── commands/
    │   └── skills/
    ├── ruby-on-rails/       # Rails development toolkit
    │   ├── .claude-plugin/
    │   ├── agents/
    │   ├── commands/
    │   ├── skills/
    │   └── scripts/
    └── rspec/               # RSpec testing toolkit
        ├── .claude-plugin/
        ├── agents/
        ├── commands/
        └── skills/
```

## Contributing

1. Create a new plugin in `plugins/<plugin-name>/`
2. Add a `.claude-plugin/plugin.json` manifest
3. Add the plugin entry to `.claude-plugin/marketplace.json`
4. Submit a pull request

## License

MIT
