# Plan

- **Purpose and audience:** Proposed conceptual AWS design for solution architects; explain customer browsing and checkout with an external payment provider.
- **View:** One high-level cloud architecture view, emphasizing the storefront request path and checkout/payment interaction. No account/VPC topology or operational deployment claims.
- **Evidence:** The user's follow-up is the sole requirements source. AWS service selections below are illustrative design assumptions, not requirements or validated recommendations.
- **Scope:** Customer browser, CloudFront, S3-hosted storefront, API Gateway, Lambda, DynamoDB, and external payment provider. Show payment redirection/authorization as a conceptual exchange; webhook contract and exact sequence remain unspecified.
- **Assumptions / confirmation:** Assume a serverless starting point and a hosted storefront. Confirm AWS region, expected scale/traffic, security/privacy/data requirements, catalog/inventory/order ownership, payment API and webhook behavior, identity/session model, and availability/recovery targets before implementation.
- **Deliverables:** Editable self-contained HTML with inline SVG and companion evidence/QA note in this directory.
