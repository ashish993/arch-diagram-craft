# Evaluation: current `arch-diagram-craft` skill

Scenario: `vague-target-architecture` (evals.json case 1)
Prompt: “Create an AWS architecture for my online store.”

## First-response score

- **Material questions: 3/3.** Questions resolve current vs. proposed state and source evidence; audience and level of detail; and requirements/fixed AWS choices that materially affect the architecture.
- **Wait vs. assumptions: Pass.** Explicitly waits before drawing and explains the unresolved choices affect scope, view, and evidence status. It permits optional design choices to be assumed only if the user has no fixed choices.
- **Plan elements: Not yet applicable / Pass for this turn.** Skill requires the concise plan once enough information is available, after clarification. The response correctly does not prematurely state a plan or create a diagram.
- **Implementation status: Pass.** No diagram or implementation was started before resolving material ambiguity; status is clearly stated as waiting for answers.

## Overall

Pass. The response follows the skill’s review → clarify → plan → implement sequence, stays within the three-question limit, focuses on material decisions, and does not treat unspecified AWS services as evidence.
