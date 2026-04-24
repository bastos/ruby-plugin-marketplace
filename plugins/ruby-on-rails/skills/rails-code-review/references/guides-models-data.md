# Rails Guides: Models and Data

Use this when the diff touches models, persistence, associations, validations,
callbacks, migrations, or queries.

Sources:
- Active Record Basics: https://guides.rubyonrails.org/active_record_basics.html
- Active Record Associations: https://guides.rubyonrails.org/association_basics.html
- Active Record Validations: https://guides.rubyonrails.org/active_record_validations.html
- Active Record Callbacks: https://guides.rubyonrails.org/active_record_callbacks.html
- Active Record Migrations: https://guides.rubyonrails.org/active_record_migrations.html
- Active Record Query Interface: https://guides.rubyonrails.org/active_record_querying.html

Rails mismatch cues:
- Models represent persisted data and domain behavior; avoid moving model-owned
  behavior into orchestration code without a clear reason.
- Follow naming and schema conventions before adding explicit configuration.
- Keep model validations and database constraints aligned; validations alone do
  not protect all write paths.
- Use association declarations instead of manual foreign-key plumbing when they
  represent the domain, and check
  that database columns and foreign keys match the association.
- Use callbacks only when the behavior belongs to the record lifecycle and is
  safe under retries, tests, bulk updates, and background execution.
- Check whether a migration is reversible, deployable with existing data, and
  compatible with the database adapter in use.
- Use query APIs that express intent and avoid raw SQL unless the query truly
  needs it.
