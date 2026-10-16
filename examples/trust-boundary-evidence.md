# Document upload trust boundaries: example evidence

**Status:** fictional security-review teaching example. Boundary and control annotations are deliberately conservative.

## Scenario statements used

| ID | Scenario statement | Diagram representation |
| --- | --- | --- |
| T1 | A user uploads a document and metadata to an application endpoint. | User zone → application ingress |
| T2 | The application creates an upload record and stores the original object in a quarantine area. | Ingress → metadata store and quarantine store |
| T3 | A scanning service reads the quarantined object and returns a verdict. | Quarantine → external scanner → application verdict handler |
| T4 | A clean verdict moves the object to an available area; a rejected verdict remains quarantined for review. | Explicit decision paths |
| T5 | Each box is assigned to a distinct trust/ownership zone for threat-model discussion. | Dashed trust boundaries |

## Assumptions / open questions

- The external scanner, quarantine design, promotion mechanism, access checks, encryption, transport security, retention, and audit controls are illustrative and unverified.
- The diagram shows trust crossings, not proof that the crossing is authenticated, encrypted, authorized, or safe.
- Confirm data classification, user identity, file validation, scanner threat model, failure/retry behavior, and reviewer responsibilities with system owners.
