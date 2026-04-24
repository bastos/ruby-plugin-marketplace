# Rails Mismatch Red Flags

Use this when deciding whether a concern is a Rails mismatch with concrete cost.

Report a finding only when one of these creates a concrete local cost:

- Manual SQL, table plumbing, or foreign-key handling duplicates Active Record
  associations, validations, transactions, migrations, or query APIs.
- Controller code owns domain decisions, multi-record invariants, or data repair
  that belongs closer to the model or a named domain object.
- Custom routes or action names obscure a CRUD-shaped resource that would make
  authorization, redirects, tests, and links easier to follow.
- Manual parameter parsing, form naming, or nested attribute handling bypasses
  strong parameters or Rails form conventions.
- String-built HTML, URLs, tags, JSON, CSV, or redirects bypasses escaping,
  route helpers, serializers/templates, or safe redirect behavior.
- A custom abstraction hides framework lifecycle boundaries such as validation,
  callbacks, transactions, after-commit behavior, job retries, or rendering.
- New code ignores local Rails patterns already used for the same problem.
- A dependency or helper replaces a Rails primitive without reducing complexity
  or closing a concrete behavior gap.

Do not flag a service object, concern, callback, decorator, presenter, or form
object just because it exists. Flag it only when it duplicates framework
behavior, splits an invariant so it is easy to miss, or conflicts with the
project's established Rails patterns.
