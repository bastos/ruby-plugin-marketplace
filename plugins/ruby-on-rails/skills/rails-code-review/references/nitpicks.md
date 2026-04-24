# Nitpicks

Use this only when the user explicitly asks for nitpicks, polish, cleanup, or a
minor-comment pass. Do not mix these into a normal blocking review.

Sources for the general feel:
- Ruby Style Guide: https://rubystyle.guide/
- Rails Style Guide: https://rails.rubystyle.guide/
- RuboCop Rails cops: https://docs.rubocop.org/rubocop-rails/latest/cops_rails.html
- Rails Guides: https://guides.rubyonrails.org/
- Rails PR review patterns: https://levelup.gitconnected.com/i-reviewed-50-junior-rails-prs-d8fee70ebf21

Rules for using nitpicks:
- Project style, `.rubocop.yml`, formatter config, and surrounding code win.
- If a linter or formatter will catch it, prefer saying that rather than adding
  a human review comment.
- Keep comments optional: "Consider..." or "Minor: ...".
- Skip any nitpick that would make the code less clear locally.

Do not downgrade these to nitpicks:
- N+1 queries, missing eager loading, or database calls hidden inside loops.
- Missing database indexes, uniqueness constraints, foreign keys, or null
  constraints when the change relies on them.
- Overly broad strong parameters such as `permit!`.
- `rescue Exception` or swallowed failures that hide process shutdown,
  signals, or real operational errors.
- Tests that do not assert behavior, side effects, or user-visible outcomes.

Common Ruby nitpicks:
- Remove needless `return`, `self`, `begin`, interpolation, or temporary
  variables when the result stays obvious.
- Use predicate names ending in `?` for boolean methods where the project does.
- Use guard clauses only when they reduce nesting without hiding the main path.
- Keep block variable names descriptive once the block has real logic.
- Avoid broad `rescue`, modifier `rescue`, and exceptions for normal flow.
- Use `fetch`, `key?`, `values_at`, or keyword arguments when they make nil or
  missing-key behavior more explicit.

Common Rails nitpicks:
- Use route helpers, form helpers, tag helpers, and DOM id helpers instead of
  hand-built strings when the helper makes intent clearer.
- Use symbolic HTTP statuses when the project already does.
- Prefer explicit partial locals over hidden instance-variable dependencies.
- Use `find_by`, `exists?`, `pick`, `ids`, or `pluck` when they express the
  query more directly and do not change loading behavior.
- Use Rails time and formatting helpers when time zone or locale matters.
- Keep small controller/view conditionals readable; move them only when reuse or
  branching complexity justifies it.

Common test nitpicks:
- Name tests by behavior, not implementation.
- Prefer focused assertions over broad "truthy" checks.
- Avoid setup that hides the one value relevant to the example.
- Keep factories or fixtures consistent with the project instead of mixing both
  in the same area without a reason.
