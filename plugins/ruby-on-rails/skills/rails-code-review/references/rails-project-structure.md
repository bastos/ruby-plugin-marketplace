# Rails Project Structure

Use this for a first pass through an unfamiliar Rails app. Not every project has
every directory, and engines or API-only apps may move or omit pieces.

Look here first:

- `config/routes.rb`: URL shape, resource names, nesting, constraints, and mounted engines.
- `app/controllers/`: request orchestration, authentication hooks, authorization, params, redirects, and response formats.
- `app/models/`: persisted domain objects, associations, validations, callbacks, scopes, and model concerns.
- `app/views/` and `app/helpers/`: rendered templates, partials, forms, helper logic, and escaping boundaries.
- `app/jobs/`: async work, queue choice, retries, idempotency, and side effects outside requests.
- `app/mailers/`: email entry points, delivery assumptions, previews, and tests.
- `app/channels/`, `app/javascript/`, and related frontend directories: realtime behavior and browser-side code when present.
- `db/migrate/`, `db/schema.rb`, or `db/structure.sql`: data shape, constraints, indexes, and migration history.
- `config/application.rb`, `config/environments/`, and `config/initializers/`: enabled frameworks, autoloading, security defaults, cache, queue, storage, and environment behavior.
- `test/` or `spec/`: project test framework, fixtures/factories, helper APIs, system tests, and naming patterns.
- `lib/`: tasks, framework extensions, import/export code, or non-request support code.

Rails mismatch clues:

- Code for a changed behavior is split across surprising directories without a clear lifecycle boundary.
- A controller, job, view, or helper owns data invariants that are already represented in models or database constraints.
- A custom directory replaces a Rails layer without making ownership, testing, or failure behavior clearer.
