# Evidence and assumptions — conceptual AWS online store

**Status:** Conceptual proposed view; draft, not reviewed or approved.
**Audience/use:** Solution discussion; show a single high-level request/response path.
**Reviewed:** 2026-10-16.
**Owner:** Not specified.
**Source:** User prompt for this scenario only; no implementation, deployment, or customer requirements supplied.

## Evidence map

| ID | Element / flow | Evidence and classification |
|---|---|---|
| E1 | Online store, customers, public entry, web/application/database tiers | Explicit prompt requirements. No actual deployed system is evidenced. |
| F1 | Customer hostname resolution → public entry | Conceptual flow inferred to make the requested public entry usable. DNS resolution represented using Route 53 as an assumption. |
| F2 | Customer HTTPS request/response | Prompt explicitly asks labeled request/response flows; HTTPS is a chosen illustrative client-edge protocol assumption. |
| F3 | Public entry → web tier | Logical request forwarding inferred from tier order; CloudFront and ALB are assumed service choices. Exact origin behavior/caching is unspecified. |
| F4 | Web tier ↔ application tier | Logical page/API request and response inferred from required tier relationship. ECS on Fargate for both tiers is assumed. |
| F5 | Application tier ↔ database tier | Query/update and result are conceptual labels inferred from the required database tier. Amazon RDS is assumed; engine and data model are unspecified. |
| A1 | AWS services: Route 53, CloudFront, ALB, ECS/Fargate, RDS | Illustrative service selections, not source-backed deployment facts. |
| A2 | Placement | Tier columns and directional path are conceptual organization only. Region, account, VPC, subnet, availability zones, and public/private placement are unknown; no placement/security claim is intended. |
| A3 | Tier responsibilities | Frontend, store API, relational persistence, and synchronous logical calls are conventional conceptual roles chosen to give the requested tiers meaning; not verified requirements. |

## Explicit gaps

No evidence was supplied for regions, account boundaries, network topology, service configuration, RDS engine, data classification, authentication/authorization, encryption, secrets, logging, backups, scaling, availability, disaster recovery, monitoring, operations, protocol behavior between tiers, or owners. None should be inferred from the diagram. Validate service choices, placement, data and security requirements, and operational needs with accountable architecture, application, security/privacy, data, and operations reviewers before implementation decisions.

## Visual QA record

The diagram is authored as editable HTML with inline SVG, semantic named groups/elements, title/description, and a keyboard-focusable scroll region at narrow widths. Flow IDs 1–12 are numbered in path order (DNS lookup/answer, HTTPS request and origin path, then return path); solid blue arrows indicate requests, dashed amber arrows indicate responses. Source and destination endpoints are geometrically explicit. Visual QA was attempted by opening the saved HTML in Chrome, but browser policy rejected the `file:` URL (only `http:` and `https:` are allowed) and explicitly prohibited workarounds or alternate browser surfaces. Therefore no rendered desktop or narrow-viewport inspection was performed, and visual QA is **not verified**. Source-level structure only was reviewed; this is not a substitute for visual inspection.
