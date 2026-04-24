# Rails Guides: Request and Response

Use this when the diff touches routes, controllers, params, sessions, cookies,
redirects, rendering, or request flow.

Sources:
- Action Controller Overview: https://guides.rubyonrails.org/action_controller_overview.html
- Action Controller Advanced Topics: https://guides.rubyonrails.org/action_controller_advanced_topics.html
- Routing from the Outside In: https://guides.rubyonrails.org/routing.html

Rails mismatch cues:
- Use resourceful routing and conventional actions when they fit the domain.
- Keep controllers focused on request orchestration: load state, authorize,
  invoke domain behavior, and choose the response.
- Strong parameters should make accepted input explicit and match the model or
  form object being updated.
- Permit only attributes the caller should change; avoid `permit!` unless the
  surrounding code proves the input is trusted and intentionally unrestricted.
- Redirects should be intentional and safe; avoid user-controlled destinations
  unless the framework's safe redirect behavior is used correctly.
- Session and cookie changes should account for tampering, persistence, expiry,
  and sensitive data exposure.
- Response status codes should match the outcome, especially for validation
  errors, authorization failures, missing records, and non-HTML responses.
