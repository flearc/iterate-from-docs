# Reusable iteration templates

Read only the template needed for the current task. Keep working briefs outside the repository unless the project explicitly stores plans. Delete temporary artifacts when the iteration closes.

## Contents

- [Authority map](#authority-map)
- [Instruction scope map](#instruction-scope-map)
- [Brownfield baseline](#brownfield-baseline)
- [Iteration brief](#iteration-brief)
- [Parallel work map](#parallel-work-map)
- [Decision record](#decision-record)
- [Removal ledger](#removal-ledger)
- [Validation matrix](#validation-matrix)
- [Final handoff](#final-handoff)

## Authority map

```markdown
# Authority map: <change>

- Outcome: <observable result>
- User value: <why this result matters>
- Required behavior versus suggested mechanism: <separate them>
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

## Instruction scope map

Create one row per distinct instruction chain. Group paths only when every instruction owner is identical. Add separate source and destination rows for moves.

```markdown
| Target paths | Instruction chain, root to leaf | Most-specific constraints | Classification |
|---|---|---|---|
| <paths sharing one chain> | <root instructions> → <subtree instructions> | <local additions or narrowing> | authoritative |
| <fixture or generated path> | <governing outer chain> | <rules for editing the artifact> | fixture data / generated / authoritative |
```

Record unresolved contradictions below the table instead of silently choosing one rule. Omit this artifact for a small change whose targets all share one obvious chain.

## Brownfield baseline

Use this only for the affected scope of a long-lived project. Do not turn it into a repository-wide inventory.

```markdown
| Claim or behavior | Evidence | Authority class | Consumer/obligation | Action |
|---|---|---|---|---|
| <public promise or format> | <source/link/reproduction> | obligation | <named consumer/policy> | preserve/migrate/change explicitly |
| <maintained intended behavior> | <architecture/contract/decision> | current intent | <owner> | align implementation and docs |
| <reproducible behavior> | <real entry observation> | observed behavior | <consumer or none> | preserve/fix/remove after judgment |
| <old test/comment/commit> | <path/commit> | historical clue | <none/current relevance> | use as rationale, not authority |
| <conflicting claims> | <both owners> | unresolved conflict | <affected outcome> | resolve or request direction |
```

Record the compatibility policy, release status, and real consumers for the slice below the table. End adoption when the current change has trustworthy owners and evidence; leave unrelated debt alone.

## Iteration brief

```markdown
# Iteration: <one coherent slice>

## Outcome

<One externally observable outcome.>

## User value and mechanism

- Value: <why the outcome matters>
- Required behavior: <must hold>
- Suggested mechanism: <binding constraint, preferred approach, or replaceable idea>

## Constraints

- <Invariant or compatibility promise>
- <Documented architecture rule>
- <Security, durability, lifecycle, or platform constraint>
- <Compatibility or migration obligation>

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
- Proof strength: <regression that makes each selected check fail>
- Static/documentation: <relevant checks>

## Done

<Behavior works through the real entry, stale references are absent, and selected checks pass.>
```

## Parallel work map

Use this only when multiple agents have non-obvious dependencies, write ownership, or integration order.

```markdown
# Parallel work: <change>

- Base commit: <full revision>
- Branch and worktree state: <current branch, worktrees, staged/unstaged/untracked paths>
- User-owned baseline: <dirty paths plus relevant original hunks or content hashes>
- Integration owner: <parent agent>
- Write topology: <shared checkout with disjoint paths / isolated worktrees>

| Task | Depends on | Owner | Read scope | Exclusive write scope | Validation | Delivery |
|---|---|---|---|---|---|---|
| <bounded outcome> | <task or none> | <agent> | <paths/docs> | <paths or read-only> | `<command>` | <diff/commit/receipt> |

## Worker brief: <task>

- Goal: <observable result>
- Base: <revision and prerequisite results>
- Applicable instructions: <root-to-leaf chain>
- Read scope: <paths and sources>
- Exclusive write scope: <paths or read-only>
- Do not modify: <shared contracts, user changes, other owners>
- Git boundary: <prohibited operations or authorized branch/worktree actions>
- Validation: <focused commands and expected evidence>
- Stop and report when: <contract conflict, overlap, missing authority, or blocker>
- Return: <changed files, result, checks, assumptions, risks, and unresolved items>
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
