---
description: Database migration management - create, run, rollback, status
argument-hint: [action] [options...]
allowed-tools: Read, Bash(rails:*, bundle:*), Glob, Grep
---

Migration action requested: $ARGUMENTS

**Available actions:**

| Action | Description | Example |
|--------|-------------|---------|
| `create` | Create a new migration | `create AddStatusToArticles status:string` |
| `run` | Run pending migrations | `run` |
| `rollback` | Rollback last migration | `rollback` or `rollback STEP=3` |
| `status` | Show migration status | `status` |
| `redo` | Rollback and re-run last | `redo` |
| `version` | Show current version | `version` |

**For the requested action:**

1. **Determine the action type** from arguments
2. **For `create`:**
   - Generate migration with `rails generate migration`
   - Suggest appropriate migration name (Add/Remove/Create prefix)
   - Include proper column types and indexes
   - Show migration file for review before running

3. **For `run`:**
   - Check for pending migrations first
   - Run `rails db:migrate`
   - Show what tables/columns were modified

4. **For `rollback`:**
   - Show which migration will be rolled back
   - Confirm before proceeding if destructive
   - Execute `rails db:rollback`

5. **For `status`:**
   - Run `rails db:migrate:status`
   - Highlight any down migrations

**Migration best practices:**
- Always add indexes on foreign keys
- Use `null: false` for required columns
- Add `default` values where appropriate
- For large tables, consider `disable_ddl_transaction!` and `algorithm: :concurrently`
- Never modify a migration that has been deployed

**Safe migration patterns:**
```ruby
# Add column with default (safe in Rails 5+)
add_column :users, :status, :string, default: "active", null: false

# Add index concurrently (PostgreSQL)
disable_ddl_transaction!
add_index :users, :email, algorithm: :concurrently

# Remove column in phases
# 1. Stop using column in code
# 2. Deploy code
# 3. Remove column with ignore
```

If no arguments provided, show migration status and ask what action to take.
