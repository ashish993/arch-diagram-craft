# Evidence note — checkout current state

## Scope and method

The diagram describes the supplied `submit_checkout` function and the three supplied behavioral tests. It is a current-state component and interaction view, not a proposed redesign. Solid arrows show the function's ordered calls and results; dashed lines explain ordering and compensation.

## Evidence map

| Diagram element / flow | Claim shown | Evidence and classification |
|---|---|---|
| Request inputs → `submit_checkout` | Inputs include cart, customer ID, payment token, inventory, payments, orders, events | `work/arch-diagram-craft/evals/fixtures/checkout-service/checkout.py:4` — direct fact |
| 1. reserve | Calls `inventory.reserve(cart.items)` before payment | `checkout.py:5`; `test_checkout.py:5-7` — direct fact; test confirms no payment call on inventory rejection |
| Inventory rejection | Returns rejected with `inventory_unavailable`; payment is not called | `checkout.py:5-6`; `test_checkout.py:5-7` — direct fact |
| 2. authorize | On successful reservation, calls `payments.authorize(payment_token, cart.total)` | `checkout.py:8` — direct fact |
| Payment decline compensation | Calls `inventory.release(cart.items)` and returns rejected with `payment_declined` | `checkout.py:9-11`; `test_checkout.py:10-12` — direct fact; test confirms one release |
| 3. save | On approved payment, saves customer ID, cart items, total, and authorization ID | `checkout.py:13` — direct fact |
| 4. publish | Publishes `OrderPlaced` with only `order_id` set to `order.id` | `checkout.py:14`; `test_checkout.py:15-17` — direct fact; test verifies the event payload contains only the order identifier |
| Accepted result | Returns accepted with `order_id` | `checkout.py:15` — direct fact |

## Limits

The source does not specify implementation details, network protocols, persistence technology, retries, concurrency behavior, or deployment topology. The diagram does not assert any of these. The dashed explanatory connectors are visual annotations of call order and the release action; they are not additional runtime calls.
