# Rails Guides: Security and Production

Use this when the diff changes authentication or authorization boundaries,
input/output handling, caching, deployment behavior, configuration, or
production diagnostics.

Sources:
- Securing Rails Applications: https://guides.rubyonrails.org/security.html
- Caching with Rails: https://guides.rubyonrails.org/caching_with_rails.html
- Tuning Performance for Deployment: https://guides.rubyonrails.org/tuning_performance_for_deployment.html
- Configuring Rails Applications: https://guides.rubyonrails.org/configuring.html
- Error Reporting in Rails Applications: https://guides.rubyonrails.org/error_reporting.html

Rails mismatch cues:
- Check every entry point for authorization, not only controller actions.
- Treat SQL, HTML, redirects, file names, deserialization, and external requests
  as separate security contexts with separate escaping or validation needs.
- Cache keys and invalidation paths should match the data being rendered.
- Production performance changes should account for concurrency, memory, eager
  loading, queue workers, and database pressure.
- Configuration changes should be environment-specific where needed and should
  not expose secrets through logs, source, or client-visible payloads.
- Error handling should preserve debugging signal without swallowing failures
  that callers or operators need to know about.
