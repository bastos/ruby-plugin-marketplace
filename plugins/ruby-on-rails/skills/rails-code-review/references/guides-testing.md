# Rails Guides: Testing

Use this when judging whether a change has the right kind of test coverage.

Source:
- Testing Rails Applications: https://guides.rubyonrails.org/testing.html

Rails mismatch cues:
- Match the test layer to the behavior: model tests for model invariants,
  controller or request tests for request behavior, integration tests for flows,
  and system tests for user-visible browser behavior.
- Check that fixtures, factories, helpers, and setup follow the local project's
  existing test patterns.
- Tests should run in the test environment, use the test database safely, and
  avoid depending on execution order.
- Use assertions that describe behavior instead of assertions that mirror the
  implementation.
- Job, mailer, cable, route, view, and helper changes should use the specialized
  test helpers available in Rails when the project already exercises those
  layers.
- Parallel test behavior matters when tests touch global state, time, files,
  queues, external services, or shared database records.
