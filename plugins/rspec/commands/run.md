---
description: Run RSpec tests with smart filtering by file, line, tag, or pattern
argument-hint: "[file:line | tag | pattern]"
allowed-tools: ["Bash", "Read", "Glob"]
---

# Run RSpec Tests

Execute RSpec tests with intelligent filtering and output formatting.

## Arguments

The user may provide:
- **File path**: `spec/models/user_spec.rb`
- **File with line**: `spec/models/user_spec.rb:42`
- **Tag**: `:focus`, `:slow`, `type:model`
- **Pattern**: `user`, `authentication`
- **No argument**: Run all specs or contextual specs

## Execution Strategy

### With File Path
Run the specific file or file:line:
```bash
bundle exec rspec spec/models/user_spec.rb
bundle exec rspec spec/models/user_spec.rb:42
```

### With Tag
Run specs matching the tag:
```bash
bundle exec rspec --tag focus
bundle exec rspec --tag type:model
bundle exec rspec --tag ~slow  # exclude slow
```

### With Pattern
Find and run matching spec files:
```bash
bundle exec rspec --pattern "**/user*_spec.rb"
```

### No Arguments
If in a spec file context, run that file. Otherwise, run the full suite or ask user preference.

## Output Handling

- Use `--format documentation` for readable output
- Use `--format progress` for large suites
- Show `--profile 5` for slow tests when suite > 20 specs
- On failure, show failing examples with `--only-failures` hint

## Common Flags

Suggest these when relevant:
- `--fail-fast` - Stop on first failure
- `--seed 12345` - Reproduce random order
- `--bisect` - Find minimal failing set
- `--next-failure` - Run next pending failure

## Examples

```
/rspec:run                           # Run all or contextual
/rspec:run spec/models/              # Run all model specs
/rspec:run user_spec.rb:25           # Run specific line
/rspec:run :focus                    # Run focused tests
/rspec:run --tag slow                # Run slow tagged tests
```
