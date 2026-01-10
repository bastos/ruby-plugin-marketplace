---
description: Manage Ruby dependencies with Bundler
argument-hint: "[command] [options]"
allowed-tools: ["Bash", "Read", "Glob"]
---

# Manage Dependencies with Bundler

Execute Bundler commands for dependency management.

## Arguments

The user may provide:
- **No argument**: Run `bundle install`
- **Command**: Specific bundler command (e.g., `update`, `add`, `info`)
- **Gem name**: For add/update/info commands

## Execution Strategy

### Install Dependencies

```bash
# Install all gems from Gemfile.lock
bundle install

# Install without development/test gems
bundle install --without development test

# Install to vendor directory
bundle install --path vendor/bundle

# Update Gemfile.lock to match Gemfile
bundle install --redownload
```

### Update Gems

```bash
# Update all gems
bundle update

# Update specific gem (and its dependencies)
bundle update rails

# Update gem conservatively (minimal changes)
bundle update --conservative rails

# Update only patch versions
bundle update --patch
```

### Add Gems

```bash
# Add gem to Gemfile and install
bundle add nokogiri

# Add with version constraint
bundle add rails --version "~> 7.0"

# Add to specific group
bundle add rspec --group test

# Add without installing
bundle add sidekiq --skip-install
```

### Remove Gems

```bash
# Remove from Gemfile
bundle remove nokogiri
```

### Gem Information

```bash
# Show installed version and source
bundle info rails

# Show where gem is installed
bundle info rails --path

# List all installed gems
bundle list

# Show outdated gems
bundle outdated

# Show outdated with newer versions
bundle outdated --strict
```

### Check Dependencies

```bash
# Verify Gemfile.lock is up to date
bundle check

# Show dependency tree
bundle viz  # requires graphviz

# Audit for security vulnerabilities
bundle audit
```

### Execute Commands

```bash
# Run command in bundle context
bundle exec rails server
bundle exec rspec
bundle exec rubocop

# Open gem in editor
bundle open rails
```

### Lock File Management

```bash
# Generate lock file without installing
bundle lock

# Update platforms in lock file
bundle lock --add-platform x86_64-linux

# Remove platform
bundle lock --remove-platform x86_64-linux
```

### Clean Up

```bash
# Remove unused gems
bundle clean

# Force removal (dangerous)
bundle clean --force
```

## Gemfile Tips

When editing Gemfile, suggest:

```ruby
# Version constraints
gem "rails", "~> 7.0"    # >= 7.0.0, < 8.0
gem "pg", ">= 1.0"       # Any version >= 1.0
gem "puma", "~> 5.0.0"   # >= 5.0.0, < 5.1.0

# Groups
group :development, :test do
  gem "rspec-rails"
end

# Platform-specific
gem "bcrypt", platforms: :ruby

# Git sources
gem "my_gem", git: "https://github.com/user/my_gem.git"
gem "my_gem", git: "...", branch: "main"

# Local path (development)
gem "my_gem", path: "../my_gem"
```

## Troubleshooting

```bash
# Clear cache and reinstall
rm -rf vendor/bundle .bundle
bundle install

# Reset to locked versions
bundle install --redownload

# Debug resolution issues
bundle install --verbose
```

## Examples

```
/ruby:bundle                      # Install dependencies
/ruby:bundle update rails         # Update Rails gem
/ruby:bundle add sidekiq          # Add Sidekiq gem
/ruby:bundle outdated             # Show outdated gems
/ruby:bundle info pg              # Show pg gem info
/ruby:bundle exec rspec           # Run RSpec
```
