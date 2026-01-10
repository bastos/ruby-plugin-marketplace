# Claude Instructions

This repository is a Claude Code plugin marketplace. Follow the project
documentation in `README.md` and keep changes consistent with the marketplace
structure.

## Repo layout

- `.claude-plugin/marketplace.json`: marketplace manifest
- `plugins/`: contains individual plugins
  - `ruby-on-rails/`: Ruby on Rails development toolkit
  - `rspec/`: RSpec testing toolkit

## Adding plugins

Each plugin lives in `plugins/<plugin-name>/` with its own `.claude-plugin/plugin.json`.

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
- `feat(ruby-on-rails): add new skill for Solid Queue`
- `fix(marketplace): correct plugin path`
- `docs: update installation instructions`
- `feat: add new plugin`

## References

- https://www.conventionalcommits.org/en/v1.0.0/
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/plugin-marketplaces
