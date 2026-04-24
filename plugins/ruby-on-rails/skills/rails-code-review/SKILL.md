---
name: rails-code-review
description: "Portable staff-level Rails code review workflow for any Rails project: local changes, branch diffs, pull requests, Rails architecture, Rails conventions, and maintainability reviews. Use this whenever the user asks to review Rails code or Rails application changes. If the review target is not explicit, ask whether to review local changes, this branch against main, or a pull request before proceeding."
version: 1.0.0
---

# Rails Code Review

Review Rails changes with concrete repository evidence. `SKILL.md` defines the workflow; [references/review-rubric.md](references/review-rubric.md) provides context, examples, review lenses, and detailed Rails component checks.

Read the reference after you know the target and changed files. Use it to identify code that fights Rails behavior or bypasses Rails primitives, not to impose generic style.

This skill must work in any Rails project. Discover the app's Rails version,
testing setup, database, frontend choices, background job backend,
authentication and authorization patterns, and local instructions before
applying the rubric.

## Intake

First identify the review target. If the user did not say which one, ask one concise question:

```text
Which review target should I use: local staged/uncommitted changes, this branch against main, or a pull request?
```

Use the explicit target when provided:

- Local staged or uncommitted code: review `git diff --staged` and `git diff`; include committed-but-unpushed changes only if the user asks for all local changes.
- Branch against main: compare the current branch with the repository's main branch using the merge base, for example `git diff "$(git merge-base HEAD origin/main)"..HEAD` after confirming the base branch.
- Pull request review: use the repository's pull request tooling when available. Read existing inline comments if the user wants feedback posted or asks you to avoid duplicates.

Do not post PR comments, resolve threads, stage, commit, or run destructive commands unless the user explicitly asks.

## Review Workflow

1. Collect the diff for the chosen target.
2. Read repository instructions and project docs that apply to changed files.
3. Read [references/project-discovery.md](references/project-discovery.md) to adapt the review to this app.
4. Read the reference rubric for source context and detailed review criteria.
5. Inspect surrounding code only to answer concrete questions raised by the diff.
6. Compare the change against existing local patterns.
7. Report only evidence-backed findings.

Ignore generated and lock files unless the issue is specifically about dependency or generated-artifact drift.

Leave whitespace, house style, and simple linting to the project. Human review should focus on behavior, design, risk, and changeability.

## Finding Rules

Only report findings that are backed by repository evidence.

- Include file and line whenever possible.
- Explain the runtime or maintenance consequence, not just the preference.
- Separate correctness, security, performance, framework alignment, and maintainability findings.
- Avoid speculative rewrites. If a concern is only project preference, omit it.
- Use the reference rubric as calibration, then judge the local code.

Severity guide:

- `P0`: breaks production, leaks data, corrupts data, or creates an urgent security issue.
- `P1`: likely bug, security issue, migration hazard, or severe performance problem.
- `P2`: maintainability, Rails alignment, or reliability issue that will likely cost the team soon.
- `P3`: small cleanup, naming, or consistency issue worth considering but not blocking.

## Output

Lead with findings. Keep the review brief and actionable.

If issues were found:

```markdown
N issues found.

[1-3 sentence summary of overall risk and the main themes.]

1. `path/to/file.rb:42` - [P1] [category] Short title
   The issue and why it matters.
   Suggested fix: concrete fix when straightforward.
   Confidence: high|medium|low.
```

If no issues were found:

```markdown
No issues found.

[1-3 sentences explaining the target reviewed, the main Rails areas checked, and any residual test or runtime risk.]
```

For PR posting, only when asked, convert each finding into a concise inline comment and post a single review body summarizing the count. Do not duplicate already-addressed inline comments.
