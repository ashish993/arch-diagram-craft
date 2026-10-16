# Synthetic payment data-flow source brief

This fictional source brief is designed for evaluating diagram traceability and data-minimizing handoff. It contains no real customer, account, or payment data.

## Stated flow

1. A customer submits a cart and a payment token to the Store API over HTTPS.
2. The Store API calls an external Payment Provider over HTTPS with the payment token and amount.
3. The provider returns an authorization result and provider reference to the Store API.
4. The Store API stores the order ID, customer ID, amount, authorization result, and provider reference in the Order Database.
5. The Store API publishes an `OrderPlaced` event containing only the order ID to the internal Order Events topic.
6. The Operations Console reads order status and provider reference from the Store API. The brief does not specify operator roles, authentication, or audit controls.

## Boundaries and controls stated

- The customer, the store application account, and the external payment provider are separate trust zones.
- The Store API and Order Database are within the store application account.
- HTTPS is stated for customer-to-API and API-to-provider connections. Other encryption, identity, authorization, network placement, and secret-handling controls are unspecified.
- The brief gives no region, retention period, backup policy, availability target, RTO/RPO, alerting design, or support ownership.

## Data classes

- Customer ID: personal identifier; no actual ID or person is included here.
- Payment token and amount: payment-related data; tokenization scope and provider handling are not further described.
- Provider reference and authorization result: payment transaction metadata.
- Order ID: business identifier.

Do not add real-looking personal values to a diagram. Use these data-class labels only.
