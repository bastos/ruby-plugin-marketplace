---
description: Analyze test coverage and identify untested code
argument-hint: "[file or directory]"
allowed-tools: ["Bash", "Read", "Glob", "Grep"]
---

# Analyze Test Coverage

Identify gaps in test coverage and suggest specs to write.

## Arguments

- **File path**: Analyze coverage for specific file
- **Directory**: Analyze coverage for directory
- **No argument**: Analyze overall project coverage

## Analysis Strategy

### 1. Check SimpleCov Setup
Look for SimpleCov in the project:
```ruby
# spec/spec_helper.rb or spec/rails_helper.rb
require 'simplecov'
SimpleCov.start 'rails'
```

If not present, suggest adding it.

### 2. Run Coverage Report
```bash
COVERAGE=true bundle exec rspec
open coverage/index.html
```

### 3. Analyze Results
Parse coverage output to identify:
- Files with < 80% coverage
- Uncovered methods
- Uncovered branches
- Files with no specs at all

## Coverage Analysis

### For Specific File
1. Find corresponding spec file
2. Compare public methods in source vs described in spec
3. Identify missing test cases

### For Directory
1. List all source files
2. Find missing spec files
3. Calculate coverage percentage

### Project-Wide
1. List files without specs
2. Identify low-coverage areas
3. Prioritize by importance (models > services > helpers)

## Output Format

Provide actionable report:
```
## Coverage Analysis

### Missing Specs (No spec file exists)
- app/services/notification_service.rb
- app/models/concerns/auditable.rb

### Low Coverage (< 80%)
- app/models/order.rb (65%)
  - Missing: #calculate_tax, #apply_discount
- app/services/payment_processor.rb (45%)
  - Missing: error handling paths

### Suggested Priority
1. OrderProcessor - critical business logic
2. PaymentProcessor - handles money
3. NotificationService - user-facing
```

## Recommendations

When reporting coverage gaps:
- Prioritize critical business logic
- Suggest specific test cases
- Consider edge cases and error paths
- Note integration test opportunities

## Examples

```
/rspec:coverage                      # Full project analysis
/rspec:coverage app/models/          # Models coverage
/rspec:coverage app/models/user.rb   # Single file coverage
```
