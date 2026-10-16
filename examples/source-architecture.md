# Example system facts

This is a fictional fixture for evaluating the skill.

- A browser client calls the public API over HTTPS.
- The API validates a bearer token, then sends an order request to the Order Service over HTTPS.
- The Order Service reads and writes order records in PostgreSQL over TLS.
- The Order Service publishes an `OrderPlaced` event to a message queue.
- The Email Worker consumes that event and calls an external email provider over HTTPS.
- The browser receives an order ID and status after the database transaction commits. Email delivery is asynchronous.
- No cache, WAF, cloud vendor, region, network segmentation, or queue technology is specified.

## Expected review points

- Do not invent a cache, infrastructure vendor, or deployment region.
- Show asynchronous email delivery separately from the synchronous browser response.
- Preserve the bearer-token validation claim without inventing an identity provider.
- Distinguish the public API boundary from the external email provider boundary.
- Make the message queue producer/consumer directions explicit.

