---
description: Run Rake tasks with smart discovery and execution
argument-hint: "[task name or pattern]"
allowed-tools: ["Bash", "Read", "Glob"]
---

# Run Rake Tasks

Execute Rake tasks with intelligent discovery and contextual help.

## Arguments

The user may provide:
- **No argument**: List available tasks
- **Task name**: Run specific task (e.g., `db:migrate`)
- **Pattern**: Find matching tasks (e.g., `db:*`)
- **Task with args**: Run with arguments (e.g., `greet[Alice]`)

## Execution Strategy

### List Available Tasks

```bash
# All tasks with descriptions
bundle exec rake -T

# All tasks (including those without descriptions)
bundle exec rake -AT

# Filter by pattern
bundle exec rake -T db
bundle exec rake -T test
```

### Run a Task

```bash
bundle exec rake task_name

# With arguments
bundle exec rake "greet[Alice,Bob]"

# Multiple tasks
bundle exec rake db:migrate db:seed

# With environment
RAILS_ENV=production bundle exec rake db:migrate
```

### Trace Execution

```bash
# Show task dependencies and execution order
bundle exec rake task_name --trace

# Dry run (show what would be executed)
bundle exec rake task_name --dry-run
```

### Prerequisites

```bash
# Show task prerequisites
bundle exec rake -P task_name
```

## Common Tasks

### Database Tasks

```bash
# Generic database tasks (example structure)
bundle exec rake db:create
bundle exec rake db:migrate
bundle exec rake db:seed

# Note: These are examples. Actual task names depend on your Rakefile.
```

### Testing

```bash
bundle exec rake test
bundle exec rake test:models
bundle exec rake spec            # RSpec (if configured)
```

### Custom Tasks

Show how to find custom tasks in the project:

```bash
# List files defining tasks
ls lib/tasks/*.rake
```

## Output Handling

- Use `--trace` when debugging task failures
- Show task descriptions when listing
- Suggest related tasks when a task fails

## Examples

```
/ruby:rake                        # List all tasks
/ruby:rake -T db                  # List database tasks
/ruby:rake db:migrate             # Run migration
/ruby:rake "import[data.csv]"     # Run with argument
/ruby:rake --trace test           # Debug test task
```
