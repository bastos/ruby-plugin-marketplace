# Bastos' Ruby Plugin Marketplace

A curated collection of Ruby plugins and skills for Codex, Claude Code, and Pi.

## Available Plugins

| Plugin | Description |
|--------|-------------|
| [ruby](plugins/ruby/) | Ruby development toolkit with 8 skills, 5 commands, and 1 agent |
| [ruby-on-rails](plugins/ruby-on-rails/) | Comprehensive Rails development toolkit with 16 skills, 8 commands, and 3 agents |
| [rspec](plugins/rspec/) | Comprehensive RSpec testing toolkit with 7 skills, 3 commands, and 2 agents |

## Installation

### Add the marketplace in Codex

```bash
/plugin marketplace add bastos/ruby-plugin-marketplace
```

Or with a local path:

```bash
/plugin marketplace add ./path/to/ruby-plugin-marketplace
```

### Add the marketplace in Claude Code

```bash
/plugin marketplace add bastos/ruby-plugin-marketplace
```

Or with a local path:

```bash
/plugin marketplace add ./path/to/ruby-plugin-marketplace
```

### Install a plugin

Use the marketplace name shown by your client.

Codex currently registers this GitHub marketplace as
`bastos-ruby-plugin-marketplace`:

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

Claude Code uses the marketplace manifest name `ruby-plugin-marketplace`:

```bash
/plugin install ruby@ruby-plugin-marketplace
/plugin install ruby-on-rails@ruby-plugin-marketplace
/plugin install rspec@ruby-plugin-marketplace
```

### Install in Pi

```bash
pi install git:github.com/bastos/ruby-plugin-marketplace
```

For a project-local install:

```bash
pi install -l git:github.com/bastos/ruby-plugin-marketplace
```

Pi loads the packaged skill directories declared in `package.json`. Claude Code
commands and agents remain available through the Claude Code plugin manifests.

## Structure

```
.
├── .codex-plugin/
│   └── marketplace.json     # Codex marketplace manifest
├── .claude-plugin/
│   └── marketplace.json     # Claude Code marketplace manifest
├── package.json             # Pi package manifest
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

## Validation

Before publishing root marketplace changes, check that every manifest is valid
JSON and that marketplace entries point at existing plugin directories.

## License

MIT
