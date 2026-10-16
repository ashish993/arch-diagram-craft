# Expense reimbursement: example evidence

**Status:** fictional, simplified business-process scenario. The notation is BPMN-inspired, not asserted to conform to BPMN 2.0.

## Scenario statements used

| ID | Scenario statement | Diagram representation |
| --- | --- | --- |
| B1 | An employee submits an expense claim with a receipt and purpose. | Start and submission task |
| B2 | Finance checks whether the submission is complete. | Finance-lane task and gateway |
| B3 | An incomplete claim returns to the employee for correction and resubmission. | Correction loop |
| B4 | A manager approves or rejects a complete claim. | Manager task and gateway |
| B5 | Approved claims go to accounts payable for payment scheduling. | Cross-lane handoff |
| B6 | Rejected claims close without payment; scheduled claims end as paid/closed. | Two distinct end states |

## Assumptions / open questions

- No policy threshold is encoded in the diagram; approval criteria and delegations are unspecified.
- The example omits receipt validation, duplicate claims, currency handling, tax, audit history, SLA/timer events, and exceptions.
- The role lanes, completeness gate, and outcomes are invented for instruction. Confirm the real policy owner and process before operational use.

The [OMG overview of BPMN](https://www.omg.org/bpmn/) describes BPMN as a bridge between business users and technical implementers. This simplified sample borrows familiar process concepts but is not a conformance claim.
