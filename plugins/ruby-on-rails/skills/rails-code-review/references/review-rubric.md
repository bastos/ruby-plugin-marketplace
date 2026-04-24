# Rails Code Review References

This directory holds focused context files for `rails-code-review`.

Read this index after collecting the review target and changed files. Then load
only the reference files that match the diff or the question you need to answer.
These references are for Rails-mismatch detection, not formatting or local
project rules.

## Reference Map

- [project-discovery.md](project-discovery.md): how to adapt the review to any Rails project before applying the rubric.
- [rails-project-structure.md](rails-project-structure.md): basic Rails app structure and first places to inspect.
- [source-context.md](source-context.md): Rails source map and how to use it without imposing unrelated rules.
- [nitpicks.md](nitpicks.md): optional minor Ruby/Rails polish comments; load only when the user asks for nitpicks.
- [rails-mismatch-red-flags.md](rails-mismatch-red-flags.md): common signs that code is bypassing or fighting Rails.
- [guides-models-data.md](guides-models-data.md): Rails Guides context for models, associations, validations, callbacks, migrations, and querying.
- [guides-request-response.md](guides-request-response.md): Rails Guides context for routing, controllers, params, sessions, cookies, and redirects.
- [guides-views-ui.md](guides-views-ui.md): Rails Guides context for templates, partials, layouts, forms, helpers, and JavaScript integration.
- [guides-async-files-realtime.md](guides-async-files-realtime.md): Rails Guides context for jobs, mailers, storage, rich text, and real-time features.
- [guides-security-production.md](guides-security-production.md): Rails Guides context for security, caching, performance, configuration, and production readiness.
- [guides-testing.md](guides-testing.md): Rails Guides context for model, controller, integration, system, mailer, job, route, view, and parallel tests.
- [review-lenses.md](review-lenses.md): high-level lenses for framework fit, correctness, and system impact.
- [component-checklist.md](component-checklist.md): Rails component checklist for models, controllers, routes, views, jobs, mailers, storage, text, and cable.
- [data-security-performance.md](data-security-performance.md): database, migration, security, performance, and operability checks.
- [tests-and-comments.md](tests-and-comments.md): test review guidance and comment calibration.
- [standard-libraries.md](standard-libraries.md): Rails and language standard library checks.

## Loading Rule

Load the smallest relevant file. For example, when reviewing a migration, load
`guides-models-data.md` and `data-security-performance.md`; when reviewing a
controller-only diff, load `guides-request-response.md` and
`component-checklist.md`.

Do not flag formatting, file ordering, or local architecture choices unless
they hide behavior, bypass Rails guarantees, or conflict with a project rule you
actually read.

Load `nitpicks.md` only for an explicit nitpick, polish, or cleanup pass.
