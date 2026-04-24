# Component Checklist

Use this when the diff touches Rails app code.

## Diff Shape

- Is the diff small enough to understand?
- Does each changed file have a clear reason to change?
- Are unrelated refactors mixed into behavior changes?
- Are generated files, schema files, and lock files intentionally updated?
- Is the migration or data change compatible with deploy order and rollback?

## Models

- Does business logic live near the data and domain language it operates on?
- Are associations, validations, scopes, enums, callbacks, and concerns idiomatic for this app?
- Are callbacks cohesive, observable, and safe under retries, bulk updates, and tests?
- Would `delegated_type`, polymorphic associations, `has_many :through`, or a join model better represent the domain?
- Are custom service/query/form objects replacing simpler Active Record or Active Model behavior without enough benefit?
- Are transactions used where multi-record writes must succeed or fail together?

## Controllers and Routes

- Are controller actions thin and RESTful?
- Are custom actions better expressed as nested resources or separate CRUD controllers?
- Are strong parameters, authorization, response status, redirects, and error paths correct?
- Does the controller leak domain logic that belongs in a model, job, mailer, or a named object?
- Are redirects safe from open redirect behavior?

## Views and Interactive UI

- Are templates readable, with heavy branching moved to helpers, partials, local patterns, or model query methods?
- Do partial names, locals, form builders, and DOM ids preserve Rails rendering and form behavior?
- Are dynamic updates scoped to stable ids?
- Is custom JavaScript necessary, or can server-rendered Rails own the interaction?
- Is user-supplied HTML sanitized and escaped correctly?

## Jobs, Mailers, Cable, Storage, and Text

- Are jobs idempotent and safe to retry?
- Are job arguments serializable and stable?
- Are mailers previewable and tested where the project already tests mailers?
- Are uploads validated for content type, size, authorization, and lifecycle cleanup?
- Does rich text content respect sanitization and attachment permissions?
- Are real-time broadcasts authorized and scoped to the right stream?
