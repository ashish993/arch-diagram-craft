# Evidence and handoff

## Scope and status

Draft conceptual data-flow diagram for the fictional payment service, based only on `work/arch-diagram-craft/evals/fixtures/payment-flow/source-brief.md`. Synthetic data only. Customer-facing review draft; technical semantics need confirmation before publication. No production or compliance validation is implied.

## Evidence map

| ID | Diagram statement | Source | Classification |
|---|---|---|---|
| Z1 | Customer is separate trust zone | Boundaries and controls stated, bullet 1 | Fact |
| Z2 | Store API and Order Database are within store application account | Boundaries and controls stated, bullet 2 | Fact |
| Z3 | Payment Provider is separate trust zone | Boundaries and controls stated, bullet 1 | Fact |
| F1 | Customer sends cart and payment token to Store API over HTTPS | Stated flow 1 | Fact |
| F2 | Store API sends token and amount to Provider over HTTPS | Stated flow 2 | Fact |
| F3 | Provider returns authorization result and provider reference | Stated flow 3 | Fact |
| F4 | API stores order ID, customer ID, amount, authorization result, provider reference | Stated flow 4 | Fact |
| F5 | API publishes OrderPlaced containing only order ID | Stated flow 5 | Fact |
| F6 | Operations Console reads status and provider reference from API | Stated flow 6 | Fact |
| G1 | Identity/access, other encryption, network placement, secret handling unspecified | Boundaries and controls stated, bullet 3 | Open gap |
| G2 | Console roles, authentication and audit controls unspecified | Stated flow 6 | Open gap |
| G3 | Region, retention, backup, availability, RTO/RPO, alerts, support ownership unspecified | Boundaries and controls stated, bullet 4 | Open gap |

## Handoff notes

- Labels use only data classes and fields from the source; no realistic personal or payment values are shown.
- HTTPS appears only on the two stated connections. The trust-zone boundary does not imply additional controls.
- Review with Store API/data-owner and security stakeholders to confirm flow semantics and control gaps. Operations/platform owner should resolve retention, backup, availability, alerting and support questions. Confirm whether Operations Console access is role-restricted and audited.
- No compliance framework or certification claim is made.
- Render/visual inspection was not performed in this evaluation environment; inspect full-size and narrow-screen rendering before external use.

## Evaluation score (0–2 each)

| Criterion | Score | Rationale |
|---|---:|---|
| Data-minimizing labels | 2 | Uses field names and classes only; no realistic identifiers. |
| Evidence traceability | 2 | Stable IDs link diagram facts/gaps to numbered source statements. |
| Stated-only controls | 2 | Only HTTPS is asserted, exactly where stated; other controls are gaps. |
| Relevant review gaps/roles | 2 | Flags console access, operational controls and relevant review owners. |
| Status/assumptions | 2 | Clearly identifies fictional, draft, conceptual scope and validation limits. |
| Unsupported compliance claims | 2 | Explicitly makes none. |
| **Total** | **12/12** | Subject to visual QA and technical reviewer confirmation. |
