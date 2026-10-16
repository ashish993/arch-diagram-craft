# Baseline score — old arch-diagram-craft

Scenario: “Create an AWS architecture for my online store.”

- **Asks material questions before diagram:** Yes. The prompt does not establish whether this is a real existing system or a proposed design, what audience/purpose the diagram serves, or key workload and operational constraints. Those affect the view and content.
- **Maximum / quality of questions:** Three grouped questions, a reasonable maximum. They target current-state evidence, audience/view, and constraints. The third offers useful examples without prescribing a specific AWS stack.
- **Concise plan:** Yes. It says it will select the smallest useful AWS view, distinguish confirmed information from assumptions, and deliver editable HTML/SVG plus a companion note.
- **Stops pending answer:** Yes. It explicitly leaves the architecture open pending scope clarification; no diagram or vendor components are invented.
- **Assumptions:** No architecture assumptions are made. Output format is stated as the planned default from the skill. The open-scope questions are material rather than reversible presentation assumptions.

Overall: Strong baseline behavior for this vague request. It honors the skill’s instruction to ask on missing critical scope and avoids treating plausible AWS patterns as evidence.
