# Reusable iteration templates

Read only the template needed for the current task. Keep working briefs outside the repository unless the project explicitly stores plans. Delete temporary artifacts when the iteration closes.

## Contents

- [Authority map](#authority-map)
- [Iteration brief](#iteration-brief)
- [Decision record](#decision-record)
- [Removal ledger](#removal-ledger)
- [Validation matrix](#validation-matrix)
- [Final handoff](#final-handoff)

## Authority map

```markdown
# Authority map: <change>

- Outcome: <observable result>
- Non-goals: <behavior intentionally unchanged>
- Source owner: <component/path>
- Extension point or ownership change: <mechanism>
- Public or durable effects: <API/UI/model/log/config/wire effects>
- Real entry path: <command/application/configuration>
- Contract owner: <README/reference/JSDoc>
- Rationale owner: <existing decision record or none>
- Git evidence: <commits/paths explaining the current choice>
- Superseded surface: <code/tests/docs/config to remove>
- Stop condition: <observable acceptance and focused checks>
```

## Iteration brief

```markdown
# Iteration: <one coherent slice>

## Outcome

<One externally observable outcome.>

## Constraints

- <Invariant or compatibility promise>
- <Documented architecture rule>
- <Security, durability, lifecycle, or platform constraint>

## Non-goals

- <Tempting adjacent work excluded from this slice>

## Change

- Owner: <path/component>
- Mechanism: <extension point or ownership update>
- Deletion: <old path removed, or evidence that none exists>
- Docs: <owners updated; derivative artifacts regenerated>

## Evidence

- Local semantics: <focused test>
- Assembled behavior: <real-entry test or snapshot>
- Static/documentation: <relevant checks>

## Done

<Behavior works through the real entry, stale references are absent, and selected checks pass.>
```

## Decision record

Create this only for a non-trivial choice that maintainers may revisit. Update an existing owner instead of creating a duplicate.

### Proposed

```markdown
# Decision: <title>

Status: proposed

## Problem

<Problem stated without assuming the solution.>

## Proposal

<Intended ownership and behavior.>

## Alternatives considered

**<Alternative>.** <Why it loses.>

## Acceptance criteria

- <Observable completion state>

## Risks

- <Failure risk or capability knowingly given up>
```

### Implemented

```markdown
# Decision: <title>

Status: implemented

## Problem

<Problem that remains understandable after shipping.>

## Decision

<Present-tense shipped behavior and ownership.>

## Alternatives considered

**<Alternative>.** <Why it lost.>

## Consequences

- <What the decision buys>
- <What it costs or removes>
- <Verification that pins the decision>
- <Condition for reintroduction, if relevant>
```

## Removal ledger

```markdown
# Removal ledger: <surface>

| Area | Current evidence | Action | Verification |
|---|---|---|---|
| Consumers | <assembled consumers or none> | <retain/remove> | <real-entry check> |
| Source/exports | <paths> | <delete/update> | <search/build> |
| Manifests/dependencies | <paths> | <delete/update> | <install/hygiene> |
| Config/schema/data/wire | <keys/formats> | <remove/migrate/ignore> | <round trip/search> |
| Docs/examples/catalogs | <owners> | <remove/update/regenerate> | <doc checks> |
| Tests/fixtures/snapshots | <paths> | <remove/update> | <surviving acceptance> |
| Decisions/links | <records> | <update/consolidate/archive/delete> | <link/search checks> |
| User caches/data | <locations> | <migrate/leave/delete> | <explicit policy> |
```

## Validation matrix

```markdown
| Obligation | Failure introduced by this change | Evidence that turns red | Command |
|---|---|---|---|
| <local contract> | <regression> | <focused unit/integration test> | `<command>` |
| <assembled behavior> | <wiring/lifecycle failure> | <real-entry acceptance> | `<command>` |
| <published behavior> | <artifact/runtime failure> | <built smoke/snapshot> | `<command>` |
| <docs invariant> | <stale owner/link/catalog> | <documentation check> | `<command>` |
| <complete removal> | <stale reference/surface> | <search/static check> | `<command>` |
```

Omit rows that do not apply. Add a row only when it can fail for a concrete regression.

## Final handoff

```markdown
Outcome: <what now works or no longer exists>

Updated owners:
- <code owner>
- <contract/rationale owner>

Removed:
- <obsolete code, tests, docs, configuration, or compatibility surface>

Checks run:
- `<command>` — <result>

Deferred:
- <genuine risk or separately scoped work; omit when none>
```
