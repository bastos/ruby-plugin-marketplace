# Tests and Review Comments

Use this when assessing test coverage or writing review output.

## Tests

- Tests cover the changed behavior at the lowest useful Rails layer.
- Fixtures or factories match the project's established test patterns.
- Tests are deterministic: no wall-clock surprises, shared mutable state, random ordering dependencies, or network calls.
- Tests assert behavior, side effects, responses, persisted changes, or
  user-visible outcomes instead of framework internals or accessor existence.
- System tests assert user-visible behavior instead of implementation details.
- Regression tests exist for confirmed bugs and security fixes.

## Comment Calibration

Use strong comments for concrete failures:

```markdown
`OrdersController#create` writes the payment and shipment outside a transaction, so a shipment failure can leave a paid order without fulfillment. Wrap the write sequence in a transaction or move the operation behind a model method that owns the invariant.
Confidence: high.
```

Use softer comments for framework-fit concerns:

```markdown
This service object mostly delegates to `Project` and introduces a second place to look for the project lifecycle. Consider moving the transition methods onto `Project` unless another caller needs this orchestration boundary.
Confidence: medium.
```

Avoid comments that only say "not Rails-ish". Name the concrete cost: harder
navigation, duplicated invariants, missing framework behavior, unsafe
deployment, or unclear ownership.
