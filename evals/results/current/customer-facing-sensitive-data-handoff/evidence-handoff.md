# Evidence and review handoff

**Artifact:** `payment-flow.html` (self-contained HTML with editable inline SVG)
**Status:** Draft, not approved; current logical flow as described in the fictional source brief
**Audience/use:** Customer-facing discussion of data movement and open review items
**Review date:** 2026-10-16
**System owner:** Not named in source; assign Store service owner before external approval
**Source:** `work/arch-diagram-craft/evals/fixtures/payment-flow/source-brief.md` (sections “Stated flow”, “Boundaries and controls stated”, and “Data classes”). The brief has no line numbers; flow numbers below follow its numbered statements.

## Evidence map

| ID | Element / flow | Evidence | Classification |
|---|---|---|---|
| F1 | Customer → Store API: cart and payment token over HTTPS | Source brief, Stated flow 1; HTTPS also in Boundaries and controls stated | Stated fact |
| F2 | Store API → Payment Provider: payment token and amount over HTTPS | Stated flow 2; HTTPS also in Boundaries and controls stated | Stated fact |
| F3 | Payment Provider → Store API: authorization result and provider reference | Stated flow 3 | Stated fact |
| F4 | Store API → Order Database: order ID, customer ID, amount, authorization result, provider reference | Stated flow 4 | Stated fact |
| F5 | Store API → Order Events topic: `OrderPlaced`, containing only order ID | Stated flow 5 | Stated fact |
| F6 | Operations Console reads order status and provider reference from Store API | Stated flow 6 | Stated fact; operator roles/authentication/audit unspecified |
| Z1 | Customer, store application account, and external provider are separate trust zones; Store API and Order Database are in store application account | Boundaries and controls stated | Stated fact; logical zones only |
| D1 | Customer ID is personal data; payment token and amount are payment-related data; provider reference and authorization result are payment transaction metadata; order ID is business identifier | Data classes | Stated fact |

No other protocol or control is drawn as present. The trust boundary lines express zone separation stated by the brief; they do not assert network isolation or protection.

## Open review gaps and handoff

| Review role | Status | Questions / evidence needed |
|---|---|---|
| Store service owner / architecture | Pending | Confirm diagram semantics, API/database/event ownership, event path, and whether this logical current-state view is accurate. |
| Security | Pending | Confirm API and console identity/authentication, authorization, network controls, encryption beyond the two HTTPS links, secret handling, and logging/audit controls. No such controls are established by this brief. |
| Privacy | Pending | Confirm customer-ID handling, purpose/access, retention/deletion, and whether provider data handling requires additional review. No privacy assessment or compliance conclusion is made. |
| Payment/data owner | Pending | Confirm tokenization scope, provider handling, amount/reference/result classification and access. No values or token examples are included. |
| Reliability / operations | Pending | Confirm region, availability target, backup/restore, retention, RTO/RPO, monitoring/alerting, support ownership, and runbook/escalation path. The source supplies none. |
| Customer-facing approver | Pending | Confirm intended audience, sharing permissions for the source reference, and approval to circulate after technical/security/privacy reviews. |

## Data minimization and claims

The diagram contains data-class labels only and no real-looking customer, account, token, amount, or provider-reference values. It shows only the two HTTPS connections explicitly stated. The response arrow from provider and the internal API-to-database/topic/console paths are labeled with the stated data and are not assigned unstated protocols or protections. The brief does not establish compliance, security posture, control effectiveness, production validation, or approval; none is claimed here.

## QA record

- HTML/SVG source is self-contained, has a document title, accessible SVG title/description, named trust zones, and keyboard-focusable horizontal scroll region.
- Flow directions and labels were checked against the six numbered source statements; only customer-to-API and API-to-provider carry HTTPS labels.
- Control and operations unknowns are called out in the diagram and expanded above.
- A local browser render was attempted, but the available browser blocked the localhost page (`ERR_BLOCKED_BY_CLIENT`); visual QA and narrow-viewport inspection are therefore **not verified**. Static geometry review found and corrected the API-to-provider route so it avoids the Operations Console box. The browser restriction prevented confirming the correction in a rendered viewport. This draft requires rendered review before it is described as ready for external circulation.
