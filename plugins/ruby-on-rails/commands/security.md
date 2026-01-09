---
description: Security audit for Rails application - OWASP checks, vulnerability detection
argument-hint: [file-or-scope]
allowed-tools: Read, Grep, Glob, Bash(bundle:*, brakeman:*)
---

Security audit request: $ARGUMENTS

**Scope:** $ARGUMENTS (or entire application if empty)

**Perform comprehensive security audit checking for:**

## 1. SQL Injection

**Check for:**
- Raw SQL with string interpolation
- Unsafe `where` clauses
- `find_by_sql` with user input
- `order` with user input

**Patterns to find:**
```ruby
# DANGEROUS
where("name = '#{params[:name]}'")
find_by_sql("SELECT * FROM users WHERE id = #{params[:id]}")
order(params[:sort])

# SAFE
where(name: params[:name])
where("name = ?", params[:name])
order(Arel.sql(sanitize_sql(sort_column)))
```

## 2. Cross-Site Scripting (XSS)

**Check for:**
- `html_safe` on user input
- `raw()` with untrusted content
- Missing `sanitize()` in views
- JavaScript with user data

**Patterns to find:**
```erb
<!-- DANGEROUS -->
<%= raw(user_content) %>
<%= params[:content].html_safe %>

<!-- SAFE -->
<%= sanitize(user_content) %>
<%= user_content %>  <!-- Auto-escaped -->
```

## 3. Mass Assignment

**Check for:**
- Missing `permit` in strong parameters
- Overly permissive `permit` (especially admin flags)
- `permit!` usage

**Patterns:**
```ruby
# DANGEROUS
params.permit!
params.require(:user).permit(:role, :admin)

# SAFE
params.require(:user).permit(:name, :email)
```

## 4. Authentication Issues

**Check for:**
- Hardcoded credentials
- Weak password requirements
- Missing authentication on sensitive actions
- Session fixation vulnerabilities

## 5. Authorization Flaws

**Check for:**
- Missing authorization checks
- Direct object references without ownership verification
- Admin actions without role checks

```ruby
# DANGEROUS
def show
  @article = Article.find(params[:id])
end

# SAFE
def show
  @article = current_user.articles.find(params[:id])
end
```

## 6. Insecure Direct Object References (IDOR)

**Check for:**
- Accessing resources by ID without ownership check
- Predictable resource identifiers
- Missing scope restrictions

## 7. Cross-Site Request Forgery (CSRF)

**Check for:**
- `skip_forgery_protection` usage
- Missing CSRF tokens in forms
- API endpoints without proper authentication

## 8. Sensitive Data Exposure

**Check for:**
- Secrets in code (API keys, passwords)
- Logging sensitive data
- Unencrypted sensitive columns
- Sensitive data in URLs

## 9. Security Headers

**Check for:**
- Content Security Policy
- X-Frame-Options
- X-Content-Type-Options
- Strict-Transport-Security

## 10. Dependency Vulnerabilities

**Run:**
```bash
bundle audit check --update
```

**Output format:**

For each finding:
1. **Severity:** Critical/High/Medium/Low
2. **Location:** File and line number
3. **Description:** What the vulnerability is
4. **Impact:** What could happen if exploited
5. **Fix:** How to remediate with code example

**Summary at end:**
- Total issues by severity
- Top priority fixes
- Recommended security gems (brakeman, bundler-audit, rack-attack)

Search the specified files (or all app/ and config/ files) and report all security issues found.
