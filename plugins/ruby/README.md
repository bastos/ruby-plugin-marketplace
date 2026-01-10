# Ruby Plugin for Claude Code

A comprehensive Ruby development toolkit with 8 skills covering Ruby features, metaprogramming, stdlib, design patterns, performance optimization, gem development, Rake, and Bundler.

## Features

### Skills (Auto-activate)

**Ruby:**
- **Ruby Core** — Blocks, procs, lambdas, pattern matching, enumerables, error handling, Ruby 3.x features
- **Metaprogramming** — DSLs, method_missing, define_method, hooks, class_eval, instance_eval
- **Ruby Stdlib** — FileUtils, JSON, CSV, YAML, Net::HTTP, Struct, Set, Date/Time, Logger

**Design & Performance:**
- **Design Patterns** — SOLID principles, creational, structural, and behavioral patterns in Ruby
- **Performance** — Profiling, benchmarking, memory optimization, GC tuning
- **Gem Development** — Creating, testing, documenting, and publishing gems

**Tooling:**
- **Rake** — Task automation, dependencies, file tasks, namespaces
- **Bundler** — Dependency management, Gemfile, version constraints, gem sources

### Commands

| Command | Description |
|---------|-------------|
| `/ruby:irb` | Start an interactive Ruby session with project context |
| `/ruby:lint` | Run RuboCop with smart defaults and auto-correction |
| `/ruby:benchmark` | Profile and compare Ruby code performance |
| `/ruby:rake` | Run Rake tasks with smart discovery |
| `/ruby:bundle` | Manage dependencies with Bundler |

### Agents

| Agent | Description |
|-------|-------------|
| **Ruby Developer** | Master Ruby 3.2+ with metaprogramming, performance optimization, and idiomatic patterns |

## Installation

### Via Marketplace

```
# Add the marketplace
/plugin marketplace add bastos/ruby-plugin-marketplace

# Install the plugin
/plugin install ruby@bastos-plugins
```

### Via Claude Code CLI

```bash
claude --plugin-dir /path/to/plugins/ruby
```

## Requirements

- Ruby 3.2+
- Claude Code

## Usage Examples

### Interactive Ruby Session

```
/ruby:irb                           # Start IRB session
/ruby:irb lib/my_gem.rb             # Load specific file
```

### Linting

```
/ruby:lint                          # Lint entire project
/ruby:lint app/models/user.rb       # Lint specific file
/ruby:lint lib/ --fix               # Auto-fix safe issues
```

### Benchmarking

```
/ruby:benchmark                     # Analyze for optimizations
/ruby:benchmark benchmarks/ops.rb   # Run benchmark file
```

### Using Skills

The skills activate automatically when you ask relevant questions:

```
"How do I create a DSL in Ruby?"
"What's the difference between a Proc and a Lambda?"
"How do I profile memory usage in Ruby?"
"Show me the Strategy pattern in Ruby"
"How do I publish a gem to RubyGems?"
"How do I create a Rake task with arguments?"
"How do version constraints work in Bundler?"
```

## Best Practices

This plugin follows and teaches:

- **Idiomatic Ruby** — Write code that feels natural to Ruby developers
- **Explicit Over Magic** — Use metaprogramming judiciously
- **Composition Over Inheritance** — Prefer modules and delegation
- **Profile Before Optimizing** — Measure, don't guess
- **Test Everything** — Write tests as part of every change

## Related Plugins

- **ruby-on-rails** — Ruby on Rails development toolkit
- **rspec** — RSpec testing toolkit

## License

MIT
