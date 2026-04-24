# Source Context

Use these sources to identify framework behavior the code may be bypassing.
Findings still need concrete local evidence.

## Primary Sources

- Rails Guides index: https://guides.rubyonrails.org/
- Rails Doctrine: https://rubyonrails.org/doctrine
- Rails API: https://api.rubyonrails.org/
- Rails source: https://github.com/rails/rails

Use the guide for the app's Rails version. The current Guides index exposes
versioned guides and, as of this reference pass, lists Rails Guides v8.1.3.

## How to Use Sources

- Use Guides pages to check whether framework features already cover the change.
- Use API docs for method-level behavior when a finding depends on exact options.
- Use source only when guides and API docs do not answer a local code question.
- Do not report a finding because a source organizes code differently. Report
  it only when the local code has a concrete correctness, security,
  performance, maintainability, or operability cost.
