# Data, Security, and Performance

Use this when the diff changes data flow, persistence, security boundaries,
background work, deployment behavior, or hot paths.

## Data and Performance

- Are queries bounded, indexed, and eager-loaded where needed?
- Do collection views, serializers, jobs, or loops access associations that
  should be preloaded before iteration?
- Do new foreign keys, lookup columns, and unique values have database-level
  indexes or constraints matching the query and integrity requirements?
- Are query APIs chosen to avoid unnecessary object allocation?
- Are migrations reversible, non-blocking for the target database, and safe for existing data?
- Are null constraints, foreign keys, unique indexes, and check constraints aligned with model validations?
- Are cache keys, invalidation paths, and fragment caches correct?
- Are callbacks, broadcasts, and jobs avoided in bulk paths unless they are intentional?

## Security

- Authorization is checked at every entry point, including jobs, channels, downloads, and nested resources.
- SQL uses parameter binding or query builder APIs instead of interpolation.
- HTML, rich text, Markdown, JSON, CSV, and file names are escaped or sanitized for their target context.
- Secrets stay in credentials, environment, or secret stores and never in logs.
- Deserialization uses safe APIs and verified inputs.
- External HTTP calls protect against SSRF, timeouts, redirects, and unbounded responses.

## Operability

- Failures are logged or reported at the layer that can act on them.
- Background jobs have retry, discard, and idempotency behavior that matches the side effect.
- Data backfills and migrations can be deployed safely with existing app versions.
- Rollback behavior is understood for schema changes, feature flags, and background jobs.
- Instrumentation exists for behavior that will be hard to debug from logs alone.
