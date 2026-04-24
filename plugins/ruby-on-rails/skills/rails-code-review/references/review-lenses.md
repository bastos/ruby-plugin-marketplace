# Review Lenses

Use these lenses to decide whether a finding is worth reporting.

## Framework Fit

- Check whether a Rails primitive already provides the behavior.
- Keep controllers thin: load records, authorize, call the domain operation, choose response.
- Keep domain behavior close to models when it naturally belongs to persisted concepts.
- Check whether a RESTful, CRUD-shaped resource would make the behavior clearer than a custom command controller.
- Use Rails security defaults where they apply.

## Rails Mismatch

- Challenge custom layers only when they obscure a Rails lifecycle, duplicate framework behavior, or split an invariant across too many files.
- Treat concerns and callbacks as valid Rails tools when they are cohesive and make behavior easier to find.
- Check whether server-rendered flows can own the interaction cleanly before adding custom JavaScript.
- Look for places where CRUD-shaped resources, named models, partials, or model methods would remove accidental orchestration.

## Code Structure Cost

- Names should make the Rails object and domain role obvious.
- Avoid splitting cohesive Rails behavior so much that callbacks, validations, transactions, or authorization become hard to locate.
- Tests should describe behavior and be deterministic.
- Flag complexity only when it makes behavior hard to verify or changes risky.

## System Impact

- Reliability: transactions, retries, idempotency, background job failure modes, concurrency, and data integrity.
- Performance: N+1 queries, unbounded loads, missing indexes, expensive callbacks, cache invalidation, unnecessary serialization, and slow tests.
- Security: authorization gaps, mass assignment, unsafe SQL, XSS, open redirects, secrets, file upload risk, SSRF, and unsafe deserialization.
- Operability: logging, instrumentation, error reporting, migrations, data backfills, feature flags, and rollback path.
- Ownership: whether future maintainers can locate the behavior and modify it in six months.
