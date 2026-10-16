# Scenario evaluation: `arch-diagram-craft`

Date: 2026-10-16  
Method: qualitative review of expected behavior against the previous and revised skill instructions.

## Scope and limits

The previous skill text was read from commit `d92109f` (before the clarification-first workflow). The revised skill was checked against four realistic prompts in `evals.json`.

This environment does not permit fresh-agent delegation, and no independent model runs were available. The baseline column therefore records what the old written guidance explicitly covered; the revised column records a reviewer trace of the new instructions against each expected behavior. This is a scenario-based documentation review, not empirical evidence that agents consistently follow the skill. Do not present these results as a benchmark or a production-readiness certification.

## Results

| Scenario | Previous skill text | Revised skill text | Finding |
|---|---|---|---|
| Vague target architecture | Partial: it said to ask for a missing critical scope decision, but did not define a short question protocol or a plan-before-build step. | Covered: request-gap review, up to three focused questions, a concise plan, then implementation when requested. | Clarification and planning gap addressed in the instructions. |
| Sufficiently scoped conceptual three-tier request | Covered: evidence and assumptions were required, but no explicit plan summary was required. | Covered: proceed without unnecessary questions, summarize the plan, mark optional unknowns, and run visual QA. | Avoids making clarification a mandatory delay. |
| Code-grounded current-state diagram | Covered: source inspection and separation of facts, assumptions, and unknowns were explicit. | Covered: same evidence rules remain, and the view/scope are confirmed in the plan. | Existing source-grounding behavior preserved. |
| Customer-facing sensitive-data handoff | Partial: evidence notes and knowledgeable reviewer were mentioned, but roles and security/privacy/operations handoff checks were not specified. | Covered as a scoped checklist: status/owner, evidence/decisions, applicable security/privacy, reliability/operations, interface/data, review roles, and sharing hygiene. | Enterprise handoff gaps addressed without making every checklist item universal. |

## Changes made from the review

- Rewrote the description to start with “Use when...” and name trigger situations instead of summarizing the workflow.
- Added an enterprise/customer-facing checklist with explicit scope qualifiers and a non-certification statement.
- Kept the clarification-first workflow and visual QA requirements intact.

## Remaining evaluation work

Run independent baseline and with-skill executions of these prompts in fresh contexts, using the same model and inputs, and score each expected behavior. Include rendered artifact inspection for diagram-producing cases. Repeat on failures and update the skill only when the failure mode is clear. Until then, claims about consistent agent behavior remain unverified.
