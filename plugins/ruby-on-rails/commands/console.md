---
description: Rails console helper - query builder, model inspection, debugging
argument-hint: [query-or-action]
allowed-tools: Read, Bash(rails:*, bundle:*, ruby:*), Grep, Glob
---

Console request: $ARGUMENTS

**Purpose:** Help construct and explain Rails console commands without needing to open an interactive console.

**Available helpers:**

| Action | Description |
|--------|-------------|
| `query [description]` | Build ActiveRecord query from description |
| `inspect [model]` | Show model attributes, associations, validations |
| `count [model]` | Quick count with optional conditions |
| `find [description]` | Build finder for specific records |
| `update [description]` | Build safe update command |
| `explain [query]` | Explain what a query does |

**For the request:**

1. **Parse the intent** - Understand what data operation is needed

2. **Build the command:**
   - Use proper ActiveRecord syntax
   - Include eager loading if needed
   - Add safety checks for destructive operations

3. **Explain the command:**
   - What it does step by step
   - Expected return value
   - Potential N+1 or performance issues

4. **Provide the executable command:**
   ```ruby
   # Ready to paste into rails console
   User.where(status: "active").includes(:profile).order(created_at: :desc).limit(10)
   ```

**Common console patterns:**

```ruby
# Find records
User.find(1)
User.find_by(email: "test@example.com")
User.where(role: "admin")

# Counting
User.count
User.where(active: true).count
Article.group(:status).count

# Recent records
User.order(created_at: :desc).limit(5)

# With associations
User.includes(:articles).where(articles: { status: "published" })

# Aggregations
Order.sum(:total)
Order.average(:total)
Order.maximum(:total)

# Updates (be careful!)
User.find(1).update(name: "New Name")
User.where(role: nil).update_all(role: "user")

# Debugging
User.last.attributes
User.reflect_on_all_associations
User.validators_on(:email)
```

**Safety warnings:**
- Always show command before suggesting execution
- Warn about destructive operations (update_all, delete_all, destroy_all)
- Suggest `dry_run` or count first for bulk operations
- Recommend transactions for multi-step operations

If the request is ambiguous, ask clarifying questions about the data operation needed.
