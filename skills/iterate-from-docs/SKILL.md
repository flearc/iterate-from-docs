---
name: iterate-from-docs
description: Keep an existing codebase aligned during fast iteration by deriving changes from current documentation and Git evidence, assigning each fact one owner, updating code, tests, decisions, and docs together, deleting superseded surfaces, and selecting focused validation. Use when planning, implementing, reviewing, or cleaning up non-trivial features, fixes, refactors, removals, architecture changes, or documentation-heavy work where drift, speculative abstractions, stale docs, duplicate paths, dead compatibility code, or test and documentation bloat are risks.
---

# Iterate from Docs

Use documentation as a compact constraint system, not an implementation diary. Treat current code and tests as evidence of behavior, current docs as the intended system and public obligations, and Git history as evidence for why those choices exist. Reconcile conflicts explicitly; never let one source silently override the others.

Keep this workflow proportional to the change. It is guidance, not a demand to create every document type or run every check. Reuse the repository's existing structure and tools before adding process.

## Follow the narrow reading path

Read only the chain that can constrain the requested change:

1. Read repository and subtree instructions.
2. Read the architecture map or equivalent system overview.
3. Read the owning component reference, README, public API docs, and tests.
4. Read directly related decision records, known limitations, and operational rules.
5. Inspect Git history for the relevant paths, symbols, and rejected alternatives.

Do not read the full documentation corpus by default. Search by component name, API, configuration key, event, error text, and distinctive phrases. Exclude vendored and generated trees unless the task changes their owners.

Use Git to answer questions that current prose cannot:

- `git log --follow -- <path>` for the evolution of an owner;
- `git log -S'<symbol-or-text>' --all -- <scope>` for introductions and removals;
- `git blame -L <start>,<end> <path>` to locate the responsible change;
- `git show <commit> -- <scope>` to recover rationale and the complete affected surface;
- `git diff --name-status <merge-base>...HEAD` plus status output to include committed, staged, unstaged, and untracked work.

Treat commit messages as leads, then verify the diff and current owner. Do not preserve behavior only because old code once implemented it.

## Build an authority map

Before editing, identify:

- the observable outcome and explicit non-goals;
- the component that owns the behavior;
- the documented extension point or reason the owner itself must change;
- the public, model-visible, durable, wire, configuration, or security effects;
- the real entry path that proves the assembled behavior;
- the current document that owns each affected fact;
- the decision record that owns the rationale, if one exists;
- the code, tests, fixtures, docs, and compatibility paths that become obsolete.

If docs and code disagree, reproduce or inspect the behavior, locate the owning decision, and state the mismatch. Update the correct owner in the same change. Stop for user direction only when resolving the mismatch would materially change the requested outcome.

Read [references/templates.md](references/templates.md) when a written authority map, iteration brief, decision record, removal ledger, or validation matrix would help. Keep these artifacts temporary unless the repository has an explicit home for them.

## Classify the change

Classify the smallest coherent change as one of:

- **Feature:** add an observable capability.
- **Fix:** restore an existing obligation.
- **Simplification:** remove or unify behavior, code, or supported surface.
- **Architecture:** change how shipped components relate or who owns a concept.
- **Process:** change tooling or contributor workflow.
- **Testing:** change the evidence strategy or test infrastructure.
- **Mechanical:** rename, format, regenerate, or relocate without changing behavior, ownership, or rationale.

Use the classification to choose documentation and evidence, not to rename an ordinary refactor. A non-trivial change should update the existing decision owner or add one concise decision record when future maintainers could reasonably revisit the choice. A mechanical change should not create a ceremonial decision record.

## Lock the iteration contract

Define the slice before editing:

1. State one observable outcome.
2. State what remains unchanged.
3. Name the authoritative code and docs.
4. Name the extension point or ownership change.
5. List the old surface to remove or the reason none exists.
6. Select evidence for the changed behavior.
7. Set a stop condition: the outcome works through the real entry path, stale references are absent, and focused checks pass.

Prefer a complete vertical slice over several speculative layers. Do not add a generic interface, adapter, package, option, or extension hook without a present consumer or a documented independent-evolution need.

## Keep architecture explicit

- Extend through a documented extension point. Avoid product-specific branches in a central loop or shared core.
- Change the core only when the requested behavior changes its responsibility; update the architecture owner in the same change.
- Keep one owner for default resolution, validation, persistence, lifecycle, and presentation decisions. Make cross-component behavior explicit at the owning edge.
- Validate parsed, queued, file, durable, process, network, model, and tool inputs at their untyped edges. Trust typed same-process values after validation.
- Put deployment-varying choices in validated configuration. Do not hide tunables in constants or test hooks.
- Make user-visible or model-visible inputs reconstructable from the system's durable authority when replay, recovery, or audit is a product obligation.
- Prefer a maintained dependency when it deletes real owned implementation, dedicated tests, and documentation while matching the required semantics. Count wrappers and residual glue against that claim.

Require a new abstraction to make ownership clearer or remove repeated policy. Mere line reuse is insufficient.

## Give every fact one home

Adapt the repository's existing hierarchy; do not create a parallel documentation system.

| Information | Preferred owner |
|---|---|
| Standing rule needed in every task | Root or subtree agent/contributor instructions, kept brief |
| System composition and extension points | Architecture map |
| Component semantics, types, limits, and configuration | Component reference or package README |
| Caller-visible behavior and failures | Public API docs or JSDoc |
| Why a non-trivial choice won and what it gave up | Active decision record |
| Ordered procedure with an observable result | Cookbook or tutorial |
| Incident sequence and causal evidence | Postmortem |
| Exhaustive inventory derivable from source | Generated reference |
| Closed decision with historical but little forward value | Frozen archive, if the repository supports one |

Write the complete fact in its owner and link to it elsewhere. Keep essential local obligations at the point of use, but do not repeat architecture, rationale, catalogs, or history.

Write durable docs in current-state language. Keep plans in proposed decisions; rewrite them as present-tense decisions after shipping. Keep commit and migration stories in Git, decision records, or postmortems. Avoid status annotations such as “implemented,” “temporary,” or “future” in standing docs.

Generate tables, graphs, API inventories, and catalogs from source when completeness matters. Add a freshness check so generated docs cannot drift. Do not hand-maintain a second index when tree navigation or search already provides discovery.

Use document budgets only for standing, accretion-prone docs. When a budget fails, relocate first, condense second, and raise the limit only when the owner genuinely needs more space. Do not impose blanket limits on exhaustive references.

## Implement one coherent change

Update the owning behavior and its evidence together:

1. Change the source owner or extension plugin.
2. Update focused unit tests for local semantics and edge cases.
3. Update assembled acceptance for user-visible, model-visible, protocol, lifecycle, or persistence behavior.
4. Update the owning README, reference, public docs, or JSDoc.
5. Update or add the decision record when the rationale is non-trivial.
6. Regenerate derivative docs and snapshots from their sources.
7. Remove superseded code, exports, configuration, schemas, fixtures, tests, docs, and records.
8. Search the whole eligible repository for stale names, paths, options, and claims.

Do not defer obvious cleanup created by the current change. Do not broaden into unrelated cleanup whose correctness needs a separate decision or validation story.

## Delete complete surfaces

Treat deletion as a first-class implementation tool. Investigate removal when finding:

- two paths that install, configure, or execute the same capability;
- a package, adapter, or helper with no assembled consumer;
- a product control or option with no backing behavior;
- an extension point created only for hypothetical use;
- compatibility parsing without an external compatibility obligation;
- a test-only implementation presented as product surface;
- source branches made impossible by the type or configuration model;
- uncovered code that has no required behavior;
- docs that restate generated inventories, history, or another owner;
- tests and snapshots that only prove behavior being removed.

For complete removal, inspect and resolve every row below:

- production source and exports;
- package manifests, dependency graphs, loaders, and build entries;
- configuration, schema, persisted data, wire formats, and migrations;
- public APIs, generated catalogs, examples, and user docs;
- tests, fixtures, snapshots, mocks, and CI lanes;
- decision records, inbound links, and reintroduction conditions;
- caches or user data, deciding explicitly whether to migrate, ignore, or delete them.

Do not keep aliases, parsers, no-op flags, migration shims, or compatibility packages “just in case.” Preserve them only for a named consumer or compatibility promise. A pre-release or internal project may prefer a clean break; a released project must evaluate its stated compatibility policy.

Consolidate a fully superseded decision into the current owner only after preserving unique rationale, rejected alternatives, consequences, verification obligations, and reintroduction conditions. Keep partially superseded decisions cross-linked. Archive closed history only when it still has evidence value; otherwise delete obsolete proposals and redundant records according to repository policy.

## Match evidence to the changed surface

Select the smallest evidence set that can fail for the intended regression:

| Changed surface | Evidence |
|---|---|
| Pure local logic | Focused unit tests and type/lint checks |
| Lifecycle, registry, concurrency, or teardown | Integration tests exercising real ownership and disposal |
| Composition or plugin wiring | Load the real configuration or application entry path |
| Human/model-visible output | Keyless snapshot or golden output through the assembled product |
| Durable or wire behavior | Replay/round-trip tests and format/version checks |
| Published package, binary, worker, or generated artifact | Built-artifact smoke under the shipping runtime |
| External provider behavior | Real-API smoke that self-skips without credentials, when feasible |
| Documentation | Link, anchor, code-fence, generated-freshness, ownership, and scoped budget checks |
| Removal | Static reference search plus surviving real-entry acceptance |

Verify the world, not a component's self-report: re-read the file, query the state, inspect emitted bytes, or run the published entry. Mock only expensive or nondeterministic edges; keep downstream behavior real.

Run focused checks once after the change stabilizes. Let CI own exhaustive matrices unless the change is irreducibly repository-wide, the user requests a full rehearsal, or CI diagnosis requires it. Add a new permanent check only for a deterministic invariant worth enforcing; do not turn every review preference into CI.

## Review for drift and bloat

Review the diff against the verified base and include every dirty worktree layer. Ask:

- Does the observable outcome match the iteration contract?
- Does each changed fact have one current owner?
- Is a special case entering a central component instead of an extension point?
- Does any new abstraction, option, package, or document lack a current consumer?
- Did the change leave two ways to perform the same task?
- Did removal cover configuration, docs, tests, generated artifacts, and decisions?
- Do tests reach the real entry path and observe external state?
- Are docs describing current behavior rather than the change story?
- Can a generated artifact or machine check replace a hand-maintained inventory?
- Is new code or prose paying permanent maintenance cost for a temporary need?

Use additions and deletions as signals, not goals. A feature may grow the repository; a simplification should demonstrate reduced owned behavior or maintenance burden, not merely move code behind another wrapper.

## Finish without residue

- Remove temporary plans, scratch files, debug hooks, obsolete TODOs, and unused fixtures.
- Move a proposed decision to its shipped lifecycle and rewrite future-tense plans as current facts.
- Repair links and regenerate derived artifacts from owners.
- Confirm repository searches find no stale names or contradictory claims.
- Report the outcome, owning docs and decisions updated, meaningful deletions, checks actually run, and genuine deferred risks.
- Do not add a summary document that repeats the diff or decision record.

End when the requested behavior works, its rationale and contract have current owners, obsolete surfaces are gone, and the narrow evidence passes.
