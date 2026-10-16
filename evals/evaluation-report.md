# Scenario evaluation: `arch-diagram-craft`

Date: 2026-10-16  
Method: fresh-context agent runs using the previous skill snapshot and the current skill, followed by a qualitative artifact review.

## Method and limits

- The prior version is the skill file at commit `d92109f`; current is the version updated at `a72ddb1`.
- Four scenarios were run against both versions: vague target architecture, scoped conceptual architecture, code-grounded current state, and customer-facing sensitive-data handoff. Each run used a separate agent context. The vague-request case also continued through a simulated clarification response under both versions.
- Agents were asked to use only the assigned skill version and scenario inputs. Results are qualitative, small-sample comparisons; they are not a statistically reliable benchmark and model/tool variance remains possible.
- Visual inspection was blocked in several fresh contexts by browser visibility or local-file/browser policy. Static parsing or source inspection does not count as visual QA. Those outputs remain visually unverified.
- The diagrams are synthetic evaluation artifacts, not production architecture recommendations.

## Comparative results

| Scenario | Previous skill | Current skill | Assessment |
|---|---|---|---|
| Vague AWS request | Asked three relevant questions, waited, and volunteered a concise plan despite no explicit plan requirement. | Asked three relevant questions and waited. In the multi-turn run it stated purpose, audience, view, evidence, scope, assumptions, and deliverables before drawing. | Both versions performed well. The updated instructions make the plan a required, repeatable step; this small sample cannot establish a reliable behavior improvement. |
| Scoped three-tier request | Proceeded without questions, marked service and placement assumptions, and produced an evidence note. | Also proceeded without questions; separated prompt facts, logical-flow assumptions, and service/placement assumptions, with open requirements listed. | No clear quality delta observed. Rendered desktop/mobile QA was not verified for either artifact due browser restrictions. |
| Code-grounded current state | Diagrammed reservation, authorization, order persistence, event publication, and evidenced rejection/compensation; cited code/test evidence and avoided deployment claims. Desktop and narrow visual QA was completed; an initial connector-label collision was corrected and rerendered. | Covered the same source-supported behavior, cited source/test lines, and marked runtime, protocol, and deployment unknowns. Browser visibility was unavailable, so visual QA was not verified. | Source grounding passed in both. The difference in visual QA reflects tool access in the run context, not evidence that the current skill regressed or improved visually. |
| Sensitive-data customer handoff | Evaluator scored 12/12 for data minimization, traceability, stated-only controls, review gaps/roles, status, and avoiding compliance claims. | Passed data minimization, evidence, stated-only controls, scoped security/privacy/operations roles, and compliance restraint. Explicitly recorded the missing service owner and approval status. Visual QA was blocked. | Both outputs were strong. Current handoff makes ownership and pending reviewer responsibilities more explicit; this comparison is qualitative and not enough to claim a measured reliability gain. |

## Conclusions

1. The previous skill already led agents to ask questions on a vague architecture request, state assumptions, and preserve evidence. The updated workflow formalizes plan-before-implementation behavior rather than introducing it from nothing.
2. The scoped handoff checklist improved the explicitness of the customer-facing review record in the observed current-skill artifact, especially ownership/status and named reviewer responsibilities. Further runs are needed to determine consistency.
3. Evidence-grounded diagram content passed the sampled scenarios under both versions.
4. Visual QA is not established suite-wide: three current-skill diagram runs could not be inspected in a browser, and one of the two vague-request continuations also lacks rendered review. Treat those artifacts as drafts until rendered inspection is performed.

## Artifact index

The generated artifacts below are retained for review. `old/` means the prior skill snapshot; `current/` means the updated skill. All diagrams are synthetic.

- **Vague request:** [old first response](results/old/vague-target-architecture/first-response.md), [old follow-up plan](results/old/vague-target-architecture/continued/plan.md), [old diagram](results/old/vague-target-architecture/continued/architecture.html), [current first response](results/current/vague-target-architecture/first-response.md), [current follow-up plan](results/current/vague-target-architecture/continued/plan.md), [current diagram](results/current/vague-target-architecture/continued/online-store-aws.html).
- **Scoped AWS:** [old diagram](results/old/scoped-conceptual-three-tier/three-tier.html), [current diagram](results/current/scoped-conceptual-three-tier/architecture.html), with an evidence note beside each.
- **Checkout code:** [old diagram](results/old/code-grounded-current-state/checkout-current-state.html), [current diagram](results/current/code-grounded-current-state/checkout-current-state.html), with code/test evidence beside each.
- **Payment data flow:** [old diagram](results/old/customer-facing-sensitive-data-handoff/payment-flow.html), [current diagram](results/current/customer-facing-sensitive-data-handoff/payment-flow.html), with handoff evidence beside each.

## Next evaluation gate

Repeat these scenarios with more than one model or agent runtime, especially the vague-request and high-stakes handoff cases. For every diagram-producing run, use a renderer accessible to that agent, inspect native-size and narrow layouts, and record defect/fix/rerender evidence. Do not claim enterprise readiness until technical owners have reviewed the relevant semantics and the intended-use checks are complete.
