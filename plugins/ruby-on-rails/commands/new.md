---
description: Create a new Rails application with smart defaults
argument-hint: app_name [options...]
allowed-tools: Bash(rails:*), Read, Write
---

Create new Rails app: $ARGUMENTS

## Rails New Command

Generate a new Rails application with customized options based on the request.

### Basic Usage

```bash
rails new app_name [options]
```

### Common Options

| Option | Description |
|--------|-------------|
| `--database=DATABASE` | Preconfigure database (postgresql, mysql, sqlite3) |
| `--api` | API-only application (no views/assets) |
| `--minimal` | Minimal Rails app (fewer defaults) |
| `--skip-test` | Skip test files |
| `--skip-system-test` | Skip system test files |
| `--skip-action-mailer` | Skip Action Mailer |
| `--skip-action-mailbox` | Skip Action Mailbox |
| `--skip-action-text` | Skip Action Text |
| `--skip-active-storage` | Skip Active Storage |
| `--skip-action-cable` | Skip Action Cable |
| `--skip-hotwire` | Skip Hotwire (Turbo + Stimulus) |
| `--skip-jbuilder` | Skip Jbuilder |
| `--skip-bundle` | Don't run bundle install |
| `--css=FRAMEWORK` | CSS framework (tailwind, bootstrap, bulma, postcss, sass) |
| `--javascript=BUNDLER` | JS approach (importmap, esbuild, rollup, webpack) |
| `--skip-javascript` | Skip JavaScript |

### Database Options

```bash
# PostgreSQL (recommended for production)
rails new myapp --database=postgresql

# MySQL
rails new myapp --database=mysql

# SQLite (default)
rails new myapp
```

### Common Configurations

**Full-stack app with PostgreSQL and Tailwind:**
```bash
rails new myapp --database=postgresql --css=tailwind
```

**API-only app:**
```bash
rails new myapp --api --database=postgresql
```

**Minimal app:**
```bash
rails new myapp --minimal --database=postgresql
```

**Skip testing:**
```bash
rails new myapp --database=postgresql --skip-test
```

**Modern full-stack with esbuild:**
```bash
rails new myapp --database=postgresql --javascript=esbuild --css=tailwind
```

### Interpretation Guide

Based on user request, determine:

1. **App name**: Extract from arguments or ask
2. **Database**: Default to PostgreSQL for most apps, SQLite for tutorials/simple apps
3. **CSS framework**: If user mentions Tailwind, Bootstrap, etc.
4. **API mode**: If user mentions "API", "backend only", "no frontend"
5. **Skip options**: Based on what features they don't need

### After Creation

After running `rails new`, suggest:
1. `cd app_name`
2. `rails db:create`
3. For PostgreSQL: Ensure PostgreSQL is running
4. Consider adding gems based on requirements

Generate the appropriate `rails new` command based on the user's request.
