# RSpec Plugin for Claude Code

A comprehensive RSpec testing toolkit with 7 skills covering core RSpec, matchers, mocks, Rails integration, Factory Bot, test organization, and performance optimization.

## Features

### Skills (Auto-activate)

**Core RSpec:**
- **RSpec Core** — describe, it, context, let, before/after, subject, hooks
- **RSpec Matchers** — Built-in matchers, custom matchers, compound matchers
- **RSpec Mocks** — Doubles, stubs, spies, verifying doubles, partial doubles

**Rails Integration:**
- **RSpec Rails** — Request specs, system specs, model specs, mailer specs
- **Factory Bot** — Factories, traits, sequences, associations, build strategies

**Organization & Performance:**
- **Spec Organization** — File structure, shared examples, shared contexts, tagging
- **Spec Performance** — Profiling, parallel tests, let vs let!, optimization

### Commands

| Command | Description |
|---------|-------------|
| `/rspec:run` | Run specs with smart filtering (file, line, tag, pattern) |
| `/rspec:generate` | Generate spec file for a class or Rails component |
| `/rspec:coverage` | Analyze test coverage and identify gaps |

### Agents

| Agent | Description |
|-------|-------------|
| **RSpec Writer** | Proactively writes comprehensive specs following best practices |
| **Spec Reviewer** | Reviews specs for quality, performance, and coverage |

## Installation

### Via Marketplace

```
# Add the marketplace
/plugin marketplace add bastos/ruby-on-rails

# Install the plugin
/plugin install rspec@bastos-plugins
```

### Via Claude Code CLI

```bash
claude --plugin-dir /path/to/plugins/rspec
```

## Requirements

- Ruby 3.0+
- RSpec 3.x
- Claude Code

## Usage Examples

### Run Specific Specs

```
/rspec:run spec/models/user_spec.rb
/rspec:run spec/models/user_spec.rb:42
/rspec:run :focus
```

### Generate Specs

```
/rspec:generate User
/rspec:generate app/services/order_processor.rb
```

### Analyze Coverage

```
/rspec:coverage
/rspec:coverage app/models/
```

### Using Skills

The skills activate automatically when you ask relevant questions:

```
"How do I write a custom matcher?"
"What's the difference between let and let!?"
"How do I mock an external API?"
"How do I speed up my test suite?"
```

## Best Practices

This plugin follows and teaches:

- **Behavior-driven testing** — Test what code does, not how
- **Verifying doubles** — Catch interface changes early
- **Build over create** — Faster tests with less database
- **One expectation per example** — Clear, focused tests
- **Descriptive names** — Tests as documentation

## License

MIT
