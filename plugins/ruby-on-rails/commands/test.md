---
description: Run tests with smart filtering - supports Minitest
argument-hint: [file-or-pattern] [options...]
allowed-tools: Read, Bash(bundle:*, rails:*, ruby:*), Glob, Grep
---

Test request: $ARGUMENTS

**First, detect the testing framework:**
- Check for `test/` directory and `test_helper.rb` → Minitest
- Check Gemfile for `minitest`

**Based on detected framework, run appropriate commands:**

## Minitest Commands

| Pattern | Command |
|---------|---------|
| All tests | `rails test` |
| Single file | `rails test test/models/user_test.rb` |
| Single test | `rails test test/models/user_test.rb:25` |
| System tests | `rails test:system` |
| Directory | `rails test test/models/` |

**For the requested test run:**

1. **Parse arguments** to determine:
   - Specific file(s) to test
   - Line number for single test
   - Directory or pattern
   - Special flags (--fail-fast, --seed, etc.)

2. **Run the tests** using appropriate command

3. **Analyze results:**
   - If all pass: Report success with timing
   - If failures: Show failing test details and suggest fixes
   - If errors: Identify root cause

4. **For failing tests, provide:**
   - The assertion that failed
   - Expected vs actual values
   - Relevant code context
   - Suggested fix

**Quick shortcuts:**
- Empty argument: Run all tests
- File path: Run that file
- Model/controller name: Find and run related tests
- `failed`: Re-run only failed tests (if the app tracks failures)

If tests are failing, analyze the output and provide actionable fixes.
