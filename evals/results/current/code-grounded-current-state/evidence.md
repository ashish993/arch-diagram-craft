# Checkout current-state diagram — evidence note

**Scope:** Synthetic `submit_checkout` function and behavioral examples only. View covers logical collaborators and one synchronous interaction. This is a current-state description, not a proposal.

## Supported facts

| ID | Diagram claim | Evidence | Type |
|---|---|---|---|
| C1 | `submit_checkout` receives cart, customer ID, payment token, and inventory/payments/orders/events collaborators | `evals/fixtures/checkout-service/checkout.py:4` | Fact |
| F1 | Inventory reservation is the first collaborator call; failure returns `inventory_unavailable` | `checkout.py:5–6`; test confirms payment call count is zero at `test_checkout.py:4–7` | Fact |
| F2 | Payment authorization follows successful reservation; decline releases the cart items and returns `payment_declined` | `checkout.py:8–11`; test confirms one release at `test_checkout.py:10–14` | Fact |
| F3 | Approved authorization is followed by order save with customer ID, items, total, and authorization ID | `checkout.py:13` | Fact |
| F4 | Then `OrderPlaced` is published with `order_id`, followed by accepted response with order ID | `checkout.py:14–15`; test checks event name/payload at `test_checkout.py:16–18` | Fact |
| F5 | Test evidence asserts the event payload contains only the order identifier | `test_checkout.py:16–18` | Fact |

## Unknowns and limits

- Collaborator implementations, protocols, call timing, persistence technology, event transport/durability, and runtime/deployment are not specified in these two files.
- Error/exception behavior for collaborator failures, especially after order save or event publication, is unspecified.
- Test fixture implementation is not supplied; test assertions are treated as behavioral evidence, not as evidence of a particular mock or runtime design.
- “Compensation” shown is narrowly the explicit `inventory.release(cart.items)` call after declined payment. There is no evidenced payment void or order rollback.
