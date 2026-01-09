---
description: Analyze and search Rails routes
argument-hint: [search-term-or-action]
allowed-tools: Read, Bash(rails:*, bundle:*, grep:*), Grep
---

Routes request: $ARGUMENTS

**Available actions:**

| Action | Description |
|--------|-------------|
| (empty) | Show all routes |
| `[search]` | Search routes by path, controller, or helper |
| `controller:[name]` | Show routes for specific controller |
| `unused` | Find controllers/actions without routes |

**Execute based on request:**

1. **Show all routes:**
   ```bash
   rails routes
   ```

2. **Search routes:**
   ```bash
   rails routes -g [search-term]
   ```

3. **Controller-specific:**
   ```bash
   rails routes -c [controller-name]
   ```

**Output format:**
```
Prefix       Verb   URI Pattern                  Controller#Action
articles     GET    /articles(.:format)          articles#index
article      GET    /articles/:id(.:format)      articles#show
             POST   /articles(.:format)          articles#create
```

**Analyze the routes and provide:**

1. **Route summary:**
   - Total number of routes
   - Grouped by controller
   - HTTP verbs distribution

2. **For search results:**
   - Matching routes with full details
   - Related routes (same controller)
   - URL helpers to use in code

3. **Route helpers for views/controllers:**
   ```ruby
   articles_path        # GET /articles
   article_path(@article)  # GET /articles/:id
   new_article_path     # GET /articles/new
   edit_article_path(@article)  # GET /articles/:id/edit
   ```

4. **Identify potential issues:**
   - Missing RESTful actions
   - Non-standard route patterns
   - Conflicting routes

**Common route patterns:**

```ruby
# RESTful resources
resources :articles

# Nested resources
resources :articles do
  resources :comments, only: [:create, :destroy]
end

# Member and collection routes
resources :articles do
  member do
    post :publish
  end
  collection do
    get :drafts
  end
end

# Namespace
namespace :admin do
  resources :users
end
```

If showing all routes results in too many, group them by controller and summarize.
