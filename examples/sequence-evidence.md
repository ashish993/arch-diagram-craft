# Booking confirmation: example evidence

**Status:** fictional interaction scenario for a developer-facing sequence diagram.

## Scenario statements used

| ID | Scenario statement | Diagram representation |
| --- | --- | --- |
| S1 | The patient portal submits appointment details to an appointment API. | Message 1 |
| S2 | The API asks the clinic schedule to reserve a selected slot. | Message 2 |
| S3 | If reservation succeeds, the API stores the appointment and returns a confirmation reference. | Success branch and response |
| S4 | A worker later delivers the scheduled reminder through a messaging provider. | Asynchronous event |
| S5 | If reservation times out or the slot is unavailable, the API returns an unavailable response and does not confirm the appointment. | Alternative failure branch |

## Explicit assumptions / questions

- Reservation happens before persistence. The actual system may use a different transaction or compensation strategy.
- The “timeout / slot unavailable” cases share one visual branch for readability, but may require different handling.
- Idempotency keys, retries, duplicate requests, cancellation, queue delivery guarantees, and notification consent are not specified.
- Numbering follows the depicted event order; message 7 is asynchronous and occurs after the confirmation response.

These scenario statements are invented for the sample. Replace them with API contracts, event schemas, and implementation evidence before using this view to guide code.
