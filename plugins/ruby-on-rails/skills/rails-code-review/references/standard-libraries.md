# Standard Libraries

Use this when the diff adds custom helpers, dependencies, data parsing,
configuration code, file handling, networking, crypto, or framework plumbing.

Check whether Rails or language standard libraries would remove custom code or
a dependency.

## Rails Libraries

- Active Support: time zones, durations, notifications, cache helpers, concern support, inflections, `CurrentAttributes`, and core extensions already used by the app.
- Active Record and Active Model: associations, validations, callbacks, attributes, dirty tracking, encryption, transactions, query APIs, `delegated_type`, and non-persistent form-like models.
- Action Pack and Action View: routing, controller callbacks, strong parameters, cookies/sessions, redirects, rendering, helpers, form builders, partials, variants, and sanitization.
- Action Mailer, Action Mailbox, Active Job, Active Storage, Action Text, and Action Cable when the change touches email, async work, uploads, rich text, or real-time UI.
- Railties, engines, generators, Rake tasks, credentials, initializers, autoloading, and configuration when the change touches boot, packaging, or app structure.

## Language Standard Library

- Data formats: `JSON`, `CSV`, and safe YAML loading.
- URLs and HTTP: URI parsing, standard HTTP clients, TLS configuration, redirects, and timeouts.
- Security and identity: random IDs, digests, HMACs, and constant-time comparison helpers where available.
- Time, files, and IO: date/time APIs, path helpers, temp files, in-memory IO, and file utilities.
- Exceptions: rescue the narrowest meaningful exception; avoid `Exception`
  unless the code truly must catch process-level failures.
- Collections and logging: sets, structured logs, option parsing, and common enumerable behavior.
