# Evidence note — conceptual AWS three-tier online store

## Scope and view

A single conceptual cloud architecture view for the requested online-store scenario. The diagram shows customers, public entry, web, application, and database tiers, with labeled request and response flows. There was no supplied architecture source or deployment brief, so this is a teaching concept rather than evidence of an existing system.

## Evidence and classification

| ID | Element / flow | Evidence or rationale | Classification |
|---|---|---|---|
| E1 | Customers | Explicitly requested in prompt | Fact about requested scope |
| E2 | Public entry, web, application, database tiers | Explicitly requested in prompt | Fact about requested scope |
| E3 | Route 53, CloudFront, ALB | Chosen as plausible AWS public-entry components for the concept | Assumption |
| E4 | EC2 web server | Chosen to represent the web tier | Assumption |
| E5 | EC2 store API / logic | Chosen to represent the application tier | Assumption |
| E6 | Amazon RDS | Chosen to represent a managed relational database | Assumption |
| F1 | Customer → public entry → web → application → database | High-level request progression needed to express the requested three-tier concept | Assumed logical flow; protocol/details unspecified |
| F2 | Database → application → web → public entry → customer | Reverse progression for a response | Assumed logical flow; response payload unspecified |

## Open questions / unspecified

- No AWS account, region, VPC, subnet, AZ, or public/private placement was specified; tier boxes are logical groupings, not deployment boundaries.
- Database engine, data model, persistence requirements, and transaction behavior are unspecified.
- Authentication, authorization, TLS termination, WAF, secrets, monitoring, backup, scaling, and availability requirements are unspecified and intentionally omitted.
- The exact application protocol and response semantics are unspecified. HTTPS at customer entry and HTTP to origin are illustrative labels, not prescribed configuration.

## Visual review

Editable source is a self-contained HTML page with inline SVG, accessible title/description, stable viewBox, and a keyboard-focusable horizontal scroll region. Request and response paths are explicitly labeled and arrows use distinct colors. I did not render the page in a browser or inspect desktop/narrow-viewport screenshots during this baseline run; visual acceptance therefore remains unverified.
