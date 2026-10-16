# Clinic appointments: example evidence

**Status:** fictional teaching scenario. No real clinic, product, or integration is represented. This is not an external reference architecture.

## Scenario statements used in the diagrams

| ID | Scenario statement | Used in |
| --- | --- | --- |
| C1 | Patients can search for and book clinic appointments. | Context; portal relationship |
| C2 | Clinic coordinators manage appointment schedules. | Context; coordinator console |
| C3 | An appointment service exchanges availability with a clinic scheduling system. | Context; container view |
| C4 | The service sends reminders through an external messaging provider. | Context; container view |
| C5 | The logical service has a patient portal, staff console, API, appointment store, queue, and reminder worker. | Container view |

## Assumptions and open questions

- “HTTPS” on the portal-to-API edge is a diagram assumption, not a fact from a specification.
- API, store, queue, and worker are logical container names. No runtime, vendor, protocol, deployment placement, authentication scheme, or data model is established.
- The clinic schedule integration contract and direction of synchronization require clarification; the view uses “read availability” as a simplifying assumption.
- Reminder timing, retries, delivery status, consent, and failure handling are outside this scenario.

## Traceability

The IDs above are invented source statements supplied for this example. When reusing the layout, replace them with exact source files/sections or workshop decisions. Do not cite this example as evidence about another system.
