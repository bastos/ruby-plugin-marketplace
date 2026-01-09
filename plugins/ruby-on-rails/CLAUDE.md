# Claude Instructions

This is the Ruby on Rails plugin for Claude Code. Follow the
project documentation in `README.md` and keep changes consistent with the
existing plugin structure.

## Repo layout
- `agents/`: subagent definitions
- `commands/`: CLI command docs
- `hooks/`: hook configuration
- `skills/`: skill definitions and references
- `.claude-plugin/plugin.json`: plugin metadata

## Commit messages (Conventional Commits)
Use Conventional Commits v1.0.0 for all commit messages.

Format:
`<type>[optional scope][!]: <description>`

Optional body and footers must be separated by a blank line:
```
<type>[optional scope][!]: <description>

[optional body]

[optional footer(s)]
```

Rules:
- `type` is required and is a short noun (e.g., `feat`, `fix`, `docs`).
- `scope` is optional and should be a short noun in parentheses.
- `description` is required and follows `: ` (colon + space).
- Breaking changes must use `!` after type/scope or a `BREAKING CHANGE:` footer.
- `BREAKING CHANGE` must be uppercase.
- Additional types are allowed (e.g., `build`, `chore`, `ci`, `docs`, `style`,
  `refactor`, `perf`, `test`).

Examples:
- `feat(agents): add skills bindings for rails-reviewer`
- `fix(commands): correct migrate help text`
- `refactor(skills)!: rename skill directory`
- `feat: support new hook configuration`
- `fix: handle missing skill references`
  `BREAKING CHANGE: skill lookup now requires explicit names`

## References
- https://www.conventionalcommits.org/en/v1.0.0/
- https://claude.md
- https://github.com/rails/rubocop-rails-omakase

## Ruby style
Follow the Rails Omakase RuboCop rules:
https://github.com/rails/rubocop-rails-omakase

## Skill validation
Run the skill validator after editing skills:
`python scripts/validate_skills.py`
