---
description: Performance analysis - N+1 queries, slow queries, memory issues
argument-hint: [file-or-scope]
allowed-tools: Read, Grep, Glob
---

Performance analysis request: $ARGUMENTS

**Scope:** $ARGUMENTS (or entire application if empty)

**Perform comprehensive performance audit checking for:**

## 1. N+1 Query Detection

**Patterns that indicate N+1:**

```ruby
# N+1 in controller
def index
  @articles = Article.all  # Missing includes
end

# N+1 in view
<% @articles.each do |article| %>
  <%= article.author.name %>      # Query per article!
  <%= article.comments.count %>   # Another query per article!
<% end %>
```

**Fix patterns:**
```ruby
# Eager loading
Article.includes(:author, :comments)

# With nested associations
Article.includes(comments: :user)

# For counts, use counter_cache
belongs_to :article, counter_cache: true
```

## 2. Missing Indexes

**Check for:**
- Foreign keys without indexes
- Columns used in `where` clauses
- Columns used in `order`
- Columns with unique validations

**In migrations, look for:**
```ruby
# Missing index on foreign key
t.references :user  # Should have index: true (default in Rails 5+)

# Missing index on queried column
# If you see: User.where(email: ...) but no index on email
```

**Check schema.rb for:**
```ruby
# Good
add_index :articles, :user_id
add_index :users, :email, unique: true

# Missing compound index for common query
# User.where(status: "active").order(:last_login_at)
add_index :users, [:status, :last_login_at]
```

## 3. Expensive Queries

**Patterns to identify:**

```ruby
# Loading all records into memory
User.all.each { |u| ... }  # Use find_each instead

# Selecting all columns when only need few
User.all.map(&:email)  # Use pluck(:email) instead

# COUNT with conditions vs counter_cache
@article.comments.count  # Query each time

# Inefficient exists check
User.where(email: email).first.present?  # Use exists? instead
```

**Better alternatives:**
```ruby
# Batch processing
User.find_each(batch_size: 1000) { |u| ... }

# Pluck for single columns
User.pluck(:email)

# Exists for presence check
User.exists?(email: email)

# Select only needed columns
User.select(:id, :email, :name)
```

## 4. Memory Issues

**Patterns causing memory bloat:**

```ruby
# Loading large result sets
users = User.all.to_a  # Loads everything into memory

# Building large arrays
User.all.map { |u| transform(u) }

# String concatenation in loops
result = ""
items.each { |i| result += i.to_s }  # Use join or StringIO
```

**Solutions:**
```ruby
# Stream large datasets
User.find_each { |u| process(u) }

# Use lazy enumerators
User.find_each.lazy.map { |u| transform(u) }.first(100)

# Batch updates
User.in_batches(of: 1000).update_all(processed: true)
```

## 5. View Performance

**Check for:**

```erb
<!-- Querying in partials -->
<%= render partial: "comment", collection: @article.comments %>
<!-- If comments not eager loaded = N+1 -->

<!-- Complex helper methods -->
<%= expensive_calculation(@user) %>  <!-- Cache this -->

<!-- Missing fragment caching -->
<% @articles.each do |article| %>
  <!-- Should be cached -->
  <%= render article %>
<% end %>
```

**Solutions:**
```erb
<!-- Fragment caching -->
<% cache article do %>
  <%= render article %>
<% end %>

<!-- Collection caching -->
<%= render partial: "article", collection: @articles, cached: true %>
```

## 6. Background Job Opportunities

**Operations that should be async:**
- Sending emails
- External API calls
- Image processing
- Report generation
- Bulk updates

```ruby
# Instead of
UserMailer.welcome(user).deliver_now

# Use
UserMailer.welcome(user).deliver_later
```

## Output Format

For each issue found:

1. **Issue Type:** N+1 / Missing Index / Memory / etc.
2. **Severity:** Critical / High / Medium / Low
3. **Location:** File:line
4. **Code:** The problematic code
5. **Impact:** Performance cost
6. **Fix:** Specific solution with code

**Summary:**
- Total issues by category
- Estimated query reduction
- Top 5 priority fixes
- Recommended gems: bullet, rack-mini-profiler, memory_profiler

Search the specified scope and report all performance issues with actionable fixes.
