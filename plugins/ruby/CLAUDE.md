# Claude Instructions

This is the Ruby plugin for Claude Code. Follow the project documentation in
`README.md` and keep changes consistent with the existing plugin structure.

## Repo layout

- `agents/`: subagent definitions
- `commands/`: CLI command docs
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

- `feat(agents): add skills bindings for ruby-developer`
- `fix(commands): correct irb session handling`
- `refactor(skills)!: rename skill directory`
- `feat: support new metaprogramming patterns`
- `docs: update skill documentation`

## References

- https://www.conventionalcommits.org/en/v1.0.0/
- https://code.claude.com/docs/en/plugins
- https://github.com/rails/rubocop-rails-omakase

## Ruby style

Follow Ruby community style conventions:

- Use 2-space indentation
- Prefer `snake_case` for methods and variables
- Use `CamelCase` for classes and modules
- Freeze string literals in Ruby 3.x
- Keep methods under 10 lines when practical
- Prefer guard clauses over nested conditionals

## Skill structure

Each skill follows this structure:

```
skills/skill-name/
├── SKILL.md           # Main skill content with YAML frontmatter
└── references/        # Optional detailed reference files
    └── topic.md
```

Skill frontmatter requires:

- `name`: Skill identifier
- `description`: When to activate this skill (include trigger phrases)
- `version`: Semantic version

## Testing

Run Ruby code examples in skills through IRB or create test files to verify
correctness before committing changes.
