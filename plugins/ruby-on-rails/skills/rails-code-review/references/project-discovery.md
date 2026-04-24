# Project Discovery

Use this before applying Rails-mismatch checks in an unfamiliar Rails project.

Start with [rails-project-structure.md](rails-project-structure.md) when the
app is unfamiliar. Then read only what is needed for the changed files:

- Rails version and enabled frameworks: `Gemfile`, `Gemfile.lock`,
  `config/application.rb`, and framework-specific initializers.
- Database and migration constraints: `config/database.yml`, schema files,
  migration history near the changed migration, and adapter-specific notes.
- Test setup: `test/`, `spec/`, helper files, fixtures, factories, system test
  setup, and how the project names behavior tests.
- Request flow: routes, base controllers, authentication, authorization,
  current-user/current-account patterns, and error handling.
- Frontend setup: views, helpers, JavaScript entrypoints, Turbo/Stimulus usage,
  import maps, bundlers, or API-only configuration.
- Async and production setup: job backend, mailer delivery, storage service,
  cable configuration, caching, credentials, and deploy notes.
- Local instructions: repository instruction files, review rules, contribution
  docs, and comments near the changed code.

Do not assume a project uses a specific test framework, database, queue backend,
frontend stack, authentication library, or service-object pattern. Use the
project's actual choices, then flag only code that bypasses Rails guarantees,
contradicts local rules, or creates concrete operational cost.
