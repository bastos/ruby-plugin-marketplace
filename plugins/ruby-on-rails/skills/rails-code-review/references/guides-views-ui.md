# Rails Guides: Views and UI

Use this when the diff touches templates, partials, layouts, helpers, forms, or
JavaScript integration.

Sources:
- Action View Overview: https://guides.rubyonrails.org/action_view_overview.html
- Layouts and Rendering: https://guides.rubyonrails.org/layouts_and_rendering.html
- Action View Helpers: https://guides.rubyonrails.org/action_view_helpers.html
- Form Helpers: https://guides.rubyonrails.org/form_helpers.html
- Working with JavaScript in Rails: https://guides.rubyonrails.org/working_with_javascript_in_rails.html

Rails mismatch cues:
- Views should render state; avoid burying domain decisions in templates.
- Use partials to make repeated or dense templates readable, but keep locals
  explicit enough that the partial is understandable in isolation.
- Layout and rendering choices should follow the request format and avoid
  surprising implicit renders.
- Form helpers should line up with model names, parameter structure, validation
  errors, and the expected controller strong parameters.
- Use framework-provided helpers for escaping, tagging, formatting, forms,
  and DOM ids over custom string construction.
- Keep JavaScript integration narrow and progressive; use server-rendered
  flows when they cover the interaction cleanly.
