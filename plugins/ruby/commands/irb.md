---
description: Start an interactive Ruby session (IRB) with project context loaded
argument-hint: "[file or expression]"
allowed-tools: ["Bash", "Read", "Glob"]
---

# Start IRB Session

Launch an interactive Ruby session with the project context loaded.

## Arguments

The user may provide:
- **No argument**: Start IRB with project files loaded
- **File path**: Load a specific file before starting
- **Expression**: Evaluate an expression and show the result

## Execution Strategy

### Basic IRB Session

```bash
# With bundler context
bundle exec irb

# With project files
bundle exec irb -r ./lib/project_name
```

### Load Specific File

```bash
bundle exec irb -r ./path/to/file.rb
```

### Evaluate Expression

```bash
ruby -e "puts [1,2,3].map { |n| n * 2 }.inspect"
```

### With Pry (if available)

Check if Pry is installed and prefer it for better debugging:

```bash
# Check for Pry
bundle info pry 2>/dev/null && bundle exec pry || bundle exec irb
```

## Context Loading

Before starting the session:

1. Check for common entry points:
   - `lib/<project_name>.rb`
   - `config/environment.rb` (Rails-like)
   - `Gemfile` (ensure bundler context)

2. Suggest useful requires based on project:
   ```ruby
   require 'bundler/setup'
   require 'your_gem'
   ```

## Helpful Tips

Suggest these IRB features when relevant:

```ruby
# Show methods on an object
obj.methods.grep(/pattern/)

# Show source location
method(:method_name).source_location

# Pretty print
require 'pp'
pp complex_object

# Reload a file
load './lib/file.rb'
```

## Examples

```
/ruby:irb                           # Start basic session
/ruby:irb lib/my_gem.rb             # Load specific file
/ruby:irb "[1,2,3].sum"             # Evaluate expression
```
