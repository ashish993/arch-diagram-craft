# Evidence map for the example

| Diagram ID | Element or flow | Source | Status |
|---|---|---|---|
| N1 | Browser client | `source-architecture.md`, first bullet | Fact |
| N2 | Public API | `source-architecture.md`, first and second bullets | Fact |
| N3 | Order Service | `source-architecture.md`, second and third bullets | Fact |
| N4 | PostgreSQL | `source-architecture.md`, third bullet | Fact |
| N5 | Message queue | `source-architecture.md`, fourth and seventh bullets | Fact; technology unspecified |
| N6 | Email Worker | `source-architecture.md`, fifth and seventh bullets | Fact |
| N7 | External email provider | `source-architecture.md`, fifth bullet | Fact; provider unspecified |
| F1 | Browser → API, HTTPS request | `source-architecture.md`, first bullet | Fact |
| F2 | API → Order Service, HTTPS order request | `source-architecture.md`, second bullet | Fact |
| F3 | Order Service ↔ PostgreSQL, TLS read/write | `source-architecture.md`, third bullet | Fact |
| F4 | Order Service → queue, `OrderPlaced` event | `source-architecture.md`, fourth bullet | Fact |
| F5 | Queue → Email Worker, consume event | `source-architecture.md`, fifth and seventh bullets | Fact |
| F6 | Email Worker → provider, HTTPS | `source-architecture.md`, fifth bullet | Fact |
| F7 | API → Browser, order ID/status after commit | `source-architecture.md`, sixth bullet | Fact; synchronous response ordering relative to event publication is unspecified |

