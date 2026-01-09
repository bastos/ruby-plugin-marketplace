# Ruby on Rails Plugin for Claude Code

A comprehensive Rails development toolkit with 15 skills covering all major Rails components, helping you build Rails 7+ applications with Hotwire following best practices for security and performance.

## Features

### Skills (Auto-activate)

**Core Framework:**
- **Rails Conventions** — MVC patterns, naming conventions, Rails Way philosophy
- **Action Controller** — Controllers, params, filters, render, redirect, sessions
- **Action View** — ERB templates, partials, layouts, form helpers, view helpers
- **Rails Migrations** — Database schema, column types, indexes, foreign keys

**Data & Storage:**
- **ActiveRecord** — Associations, validations, queries, scopes
- **Active Storage** — File uploads, attachments, variants, cloud services
- **Action Text** — Rich text editing with Trix, attachments

**Background & Communication:**
- **Active Job** — Background jobs, queues, retries
- **Action Mailer** — Email sending, templates, delivery, previews
- **Action Cable** — WebSockets, channels, broadcasting, real-time features

**Frontend:**
- **Hotwire** — Turbo Frames, Turbo Streams (9 actions), Stimulus controllers
- **JavaScript in Rails** — Import maps, jsbundling-rails, Turbo helpers, request.js

**Performance & Deployment:**
- **Rails Caching** — Fragment caching, Rails.cache, cache keys, conditional GET
- **Kamal** — Configure and deploy Rails apps with Kamal

**Testing:**
- **Minitest** — Minitest patterns, fixtures, integration tests

### Commands

| Command | Description |
|---------|-------------|
| `/new` | Create a new Rails application with smart defaults |
| `/rails:generate` | Smart Rails generator with suggestions |
| `/rails:migrate` | Migration management (create, run, rollback) |
| `/rails:test` | Run tests with smart filtering |
| `/rails:routes` | Analyze and search routes |
| `/rails:console` | Rails console helper |
| `/rails:security` | Security audit for vulnerabilities |
| `/rails:performance` | N+1 and query performance analysis |

### Agents

| Agent | Description |
|-------|-------------|
| **Rails Reviewer** | Proactively reviews Rails code for best practices |
| **Minitest Tester** | Writes Minitest tests following Rails testing guides |
| **Rails Developer** | Builds and refactors Rails features with staff-level practices |

### Hooks

- Pre-commit validation for pending migrations and missing indexes

## Installation

### Via Marketplace (Recommended)

```
# Add the marketplace
/plugin marketplace add bastos/ruby-on-rails

# Install the plugin
/plugin install ruby-on-rails@bastos-plugins
```

### Via Claude Code CLI

```bash
claude --plugin-dir /path/to/plugins/ruby-on-rails
```

## Configuration

Create `.claude/rails.local.md` in your project for custom settings:

```yaml
---
test_framework: minitest
ignored_checks:
  - pending_migrations
custom_generators:
  - my_generator
---

# Project-specific Rails notes

- Using PostgreSQL
- Custom authentication
```

## Requirements

- Ruby 3.0+
- Rails 7.0+
- Claude Code

## Usage Examples

### Generate a new resource

```
/rails:generate
> Generate a User model with email and name
```

### Run security audit

```
/rails:security
> Check this controller for security issues
```

### Analyze performance

```
/rails:performance
> Find N+1 queries in this code
```

## Development

### Skill Validation

After editing skills, run the validator:

```bash
python scripts/validate_skills.py
```

This checks:
- Frontmatter has required fields (`name`, `description`, `version`)
- Skill names match folder names
- Relative links point to existing files

## License

MIT
