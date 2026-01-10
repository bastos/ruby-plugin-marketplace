---
description: Run RuboCop linter with smart defaults and auto-correction options
argument-hint: "[file or directory] [--fix]"
allowed-tools: ["Bash", "Read", "Glob"]
---

# Run RuboCop Linter

Execute RuboCop static analysis with intelligent defaults.

## Arguments

The user may provide:
- **No argument**: Lint changed files or entire project
- **File/directory path**: Lint specific files
- **--fix**: Auto-correct safe violations
- **--fix-all**: Auto-correct all violations (including unsafe)

## Execution Strategy

### Check for RuboCop

```bash
# Verify RuboCop is available
bundle info rubocop 2>/dev/null || gem list rubocop
```

### Lint Specific Files

```bash
bundle exec rubocop path/to/file.rb
bundle exec rubocop app/models/
```

### Lint Changed Files Only

```bash
# Git diff files
bundle exec rubocop $(git diff --name-only --diff-filter=d HEAD | grep '\.rb$')

# Or staged files
bundle exec rubocop $(git diff --cached --name-only --diff-filter=d | grep '\.rb$')
```

### Auto-correct

```bash
# Safe auto-correct
bundle exec rubocop -a path/to/file.rb

# Unsafe auto-correct (may change behavior)
bundle exec rubocop -A path/to/file.rb

# Auto-correct with specific cops
bundle exec rubocop --only Style/StringLiterals -a
```

### Useful Options

```bash
# Show only offenses (no file names)
bundle exec rubocop --format simple

# Show offense counts by cop
bundle exec rubocop --format offenses

# Generate TODO file for gradual adoption
bundle exec rubocop --auto-gen-config

# Check specific cops
bundle exec rubocop --only Layout,Style/StringLiterals

# Exclude specific cops
bundle exec rubocop --except Metrics/MethodLength
```

## Output Handling

- Use `--format progress` for quick overview
- Use `--format clang` for IDE-friendly output with context
- Show cop names with `-D` for easier lookup
- Use `--parallel` for faster execution on large codebases

## Common Configurations

### Rails Omakase (rails/rubocop-rails-omakase)

```bash
# If using Rails Omakase
bundle exec rubocop -c .rubocop.yml
```

### Standard Ruby

```bash
# If using standardrb
bundle exec standardrb
bundle exec standardrb --fix
```

## Error Categories

Explain violation categories when showing results:
- **Layout**: Formatting, indentation, whitespace
- **Lint**: Potential bugs, ambiguous code
- **Metrics**: Complexity, length limits
- **Naming**: Variable/method naming conventions
- **Style**: Idiomatic Ruby style preferences
- **Security**: Potential security issues

## Examples

```
/ruby:lint                          # Lint entire project
/ruby:lint app/models/user.rb       # Lint specific file
/ruby:lint lib/ --fix               # Auto-fix safe issues in lib/
/ruby:lint --fix-all                # Auto-fix all issues (careful!)
```
