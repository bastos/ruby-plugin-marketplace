# Rails Guides: Async, Files, and Realtime

Use this when the diff touches background jobs, email, uploads, rich text, or
realtime features.

Sources:
- Active Job Basics: https://guides.rubyonrails.org/active_job_basics.html
- Action Mailer Basics: https://guides.rubyonrails.org/action_mailer_basics.html
- Active Storage Overview: https://guides.rubyonrails.org/active_storage_overview.html
- Action Text Overview: https://guides.rubyonrails.org/action_text_overview.html
- Action Cable Overview: https://guides.rubyonrails.org/action_cable_overview.html

Rails mismatch cues:
- Jobs should be idempotent, retry-aware, and explicit about queue, priority,
  arguments, exception handling, and transactional boundaries.
- Mailers should keep delivery asynchronous where appropriate and should be easy
  to preview or test using the app's existing test patterns.
- Upload handling should check authorization, content type, size, variants,
  lifecycle cleanup, and direct-upload trust boundaries.
- Rich text changes should account for sanitization, attachment permissions, and
  where rendered content is reused.
- Realtime code should scope streams and broadcasts to the right users or
  records and avoid leaking data across sessions.
