---
name: arch-diagram-craft
description: Use when a user asks to create, reverse-engineer, update, or review a system, cloud, component, data-flow, sequence, deployment, process, or security-boundary diagram from requirements or code, especially when evidence traceability, clarification, readable labels, correct arrows, or rendered visual QA matter.
---

# Architecture Diagram Craft

Create diagrams that communicate a system accurately and can be inspected and edited. Use HTML with native inline SVG by default. Choose another format when the user or delivery context requires it. Pick the view to answer a specific audience question; do not combine views just to make a diagram look comprehensive.

## Workflow

1. **Review the request for gaps.** Before drawing, check whether the user has specified enough to choose the diagram's purpose, view, scope, audience, and important elements/relationships. Read supplied notes, requirements, code, and prior conversation first; don't ask for details already present. Distinguish critical ambiguities that could change the diagram's meaning from optional implementation details that can be shown as assumptions.
2. **Ask focused questions when needed.** If a critical ambiguity remains, pause diagram implementation and ask up to three concise, relevant questions in one turn. Prefer questions that resolve scope, current-state versus target-state, audience/detail level, important actors or systems, or a consequential flow/boundary. Offer reasonable choices when they make answering easier. Don't ask a long generic questionnaire or block on optional details; record those as assumptions or open questions. When the request is sufficiently clear, say what you understood and proceed without asking for confirmation.
3. **Prepare a short plan.** Once enough information is available, summarize the agreed purpose and audience, selected view(s), evidence to use, important scope boundaries, deliverable format/location, and any remaining assumptions. Keep this proportional to the task (a few bullets for a simple diagram). If the user asks only for a plan or review, stop at that requested stage. Otherwise, the request to create the diagram authorizes implementation; don't add an approval gate after presenting the plan.
4. **Establish the evidence.** Read the supplied architecture, requirements, and relevant source files. Separate explicit facts from inferences and unknowns. Do not add plausible-sounding components, vendors, protocols, regions, or security controls without evidence. For a review, record each requested correction before editing.
5. **Choose the view.** First identify the audience and the question they need answered. Use the smallest view that answers it. Common choices include:

   | Audience question | Useful view | Show |
   | --- | --- | --- |
   | What is in scope, who uses it, and what does it depend on? | System context (C4) | System boundary, people, neighboring systems, named relationships |
   | What are the major runtime building blocks and how do they connect? | Container / high-level architecture (C4) | Applications, services, data stores, queues, external systems, protocols when known |
   | How is one service internally divided, and what depends on what? | Component diagram (C4 or UML) | A single container, its cohesive components, responsibilities, interfaces, and supported dependencies; omit source-code class detail |
   | What happens during one interaction? | Sequence / dynamic diagram (UML or equivalent) | Participants, time direction, ordered calls/events, responses and relevant branches |
   | Where does software run and what network/runtime boundaries apply? | Deployment view (C4/UML or cloud-specific) | Environments, zones, nodes/runtime, placement and network relationships supported by evidence |
   | Who performs a business process, and where are its decisions or handoffs? | BPMN process diagram or a simpler swimlane flow | Roles/participants, activities, decisions, start/end states, handoffs, exceptions in scope |
   | What steps does a person take, and which decisions change their route? | User flow / flowchart | One actor's steps, decision branches, recovery loops, and outcomes; do not mix technical message timing into a user flow |
   | Which records move, transform, or persist? | Data-flow diagram | Data stores, processes, external entities, labeled flows, trust crossings |
   | Which data crosses ownership or trust zones, and what protects each crossing? | Security / trust-boundary data-flow diagram | Explicit trust zones, external entities, processing, stores, directional flows, and only evidenced protocol/authentication/encryption controls; a boundary line does not itself prove a control |
   | How is the workload hosted in a cloud environment? | Cloud architecture / deployment diagram | Workload components, cloud/provider and account/project scope, network zones, managed services, entry/egress paths, and resilience/security controls only when sourced; label illustrative choices as assumptions |

   These are recurring, established view types, not a frequency ranking. C4 recommends selecting only the levels that add value; its context and container views are sufficient for many teams. BPMN is designed to communicate business-process semantics across business and technical stakeholders. Keep BPMN semantics distinct from informal flowcharts, and do not claim BPMN conformance unless the notation rules have been checked. Use separate diagrams when one view would obscure relationships. Ask for a missing critical scope decision; otherwise state a small, reversible assumption.
6. **Plan the visual hierarchy.** Group by meaningful system or trust boundary. Keep labels concise, reserve color for a small number of focal items, and use a legend only when a visual encoding needs explanation. Prefer readable text and whitespace over fitting everything into one canvas. Split an overloaded view.
7. **Draw with explicit relationships.** Give each important connector a source, destination, direction, and concise label. Route it so its start and arrowhead visibly meet the intended elements. Number flows when sequence matters, and include a matching flow key if numbers alone are ambiguous. Do not imply direction through proximity or line crossings.
8. **Keep a shared model for multiple views.** When one system needs context, container, dynamic, and deployment views, maintain one named element and relationship inventory, then select the relevant subset for each view. Keep element names, boundaries, and relationship meanings consistent across views. If a text DSL or diagram editor is a better fit, use it; do not redraw the same architecture independently in ways that let views drift.
9. **Preserve traceability.** Keep an evidence map alongside the diagram or in an accompanying note: stable element/flow identifier, source statement or file and location, and whether it is a fact, inference, assumption, or open question. For important relationships, record source, destination, direction, data/action, and any supported protocol or trust-boundary crossing. Do not put internal review clutter on a presentation diagram unless requested.
10. **Render, inspect, revise, and repeat.** Render the actual deliverable in its target renderer at the intended delivery size and at a narrow viewport. Inspect the rendered page, not just the source or an SVG export. For each edit to diagram geometry, labels, styling, connectors, boundaries, or legend, render again and inspect again before making the next edit. Record specific defects and fixes as feedback; continue until the acceptance checks below pass. Do not treat a successful parse, generated image, automatic layout, or single final screenshot as visual QA. If a defect cannot be resolved, disclose it and do not describe the diagram as ready.
11. **Deliver clearly.** Provide editable source and requested exports together. Summarize key assumptions, unresolved evidence gaps, the notation/renderer used, and what was checked. Do not claim verification you did not perform.

## Clarification and planning behavior

Use a review → clarify → plan → implement sequence for ambiguous requests:

- **Review:** Parse the requested outcome, diagram audience and purpose, current or proposed state, available source evidence, named elements/flows, and requested deliverables. Inspect relevant project files before asking.
- **Clarify:** Ask only about missing decisions that materially affect scope or semantics. Ask no more than three questions at once. If the request already gives enough to draw a useful view, do not delay for completeness; proceed and label noncritical unknowns.
- **Plan:** Briefly state what view you will create, what sources you will trust, what is in/out of scope, where outputs will go, and which details remain assumptions. Do not expose hidden reasoning; provide useful decisions and rationale only.
- **Implement:** When the user requested a diagram, proceed after presenting the plan; the plan is not a request for another approval. If the user requested review or planning only, stop there. If a materially different interpretation remains unresolved, wait for the user's answer before drawing.

For example, “Create an AWS architecture for my online store” leaves open whether the user wants a current-state or proposed design, which requirements and AWS services are known, and what level of detail is needed. Ask a compact set of questions about those points before drawing. If the user says “make a conceptual draft and choose sensible options,” proceed with clearly marked assumptions instead of interrogating them.

## Choose a representation that fits the work

- Hand-positioned HTML/SVG is useful when the deliverable needs a branded, self-contained, interactive web page with precise geometry. It makes connector routing and exact spacing the author's responsibility.
- A diagram-as-code tool can make changes reviewable and repeatable. Mermaid and PlantUML provide textual definitions with generated layouts; Structurizr DSL keeps a C4 model and multiple views together. A visual editor such as diagrams.net can be a better fit when stakeholders need direct editing or a broad shape library.
- Treat automatic layout as a first draft. It cannot establish that the source evidence, abstraction level, endpoint, branch semantics, trust boundary, or label placement is correct. Inspect the exact exported format in the renderer your audience will receive.
- For text-based sources, keep the source file with the diagram output and pin or record the renderer/version when reproducible geometry matters. Check tool-specific layout/accessibility limitations before promising them.
- When exporting from a visual editor, retain its native editable file alongside SVG/PNG/PDF exports. Reopen or reimport the editable source to check that the handoff still supports later changes; a picture-like export alone may lose the model.

## Required quality checks

- Components and relationships match the available evidence; distinguish facts from inferred placement or flow.
- Every arrowhead visibly points to and touches the intended destination; its tail visibly starts at the intended source. Check direction against the evidence rather than inferring it from label placement or visual proximity. Show bidirectional flows with two clear opposing arrowheads or two separately labeled connectors.
- No text is hidden, clipped, cut off, or outside its intended box or diagram frame. All labels stay within the canvas, node, boundary, or callout assigned to them.
- No unintended overlap between text, nodes, boundaries, legends, arrows, and connectors; the only expected contact is a connector meeting its intended source or destination. Labels must not sit on box borders or arrow lines; arrowheads and paths must not run through labels or unrelated boxes. If the layout cannot provide clear separation, reroute, increase spacing, shorten wording without losing meaning, or split the diagram.
- Spacing is deliberate: text is inset from box edges, connector labels have clear space on every side, nodes do not crowd boundaries, and adjacent elements remain distinct at native size. Never solve crowding by shrinking text until it is hard to read.
- Labels remain readable at the intended native size and on narrow screens. If a wide diagram needs horizontal scrolling on mobile, make the scroll region keyboard-accessible and identify it for assistive technology.
- Trust boundaries are named and connector crossings are explicit.
- Numbered flows follow the stated process order and have no unexplained gaps or duplicates.
- The diagram has a clear title, scope, and legend when symbols or colors need one.
- HTML/SVG output is inspectable, self-contained where practical, and accessible: meaningful document title, SVG `role="img"`, and an accessible name/description.
- Diagram type and detail match the audience and purpose; avoid adding implementation detail to a business process view or deployment claims to a logical architecture view.
- Assumptions, unknowns, and evidence references are visible in companion notes. Do not imply production validation, security posture, availability, compliance, or standards conformance without evidence.

## Visual QA feedback loop

Treat visual QA as an iterative acceptance gate, not a closing polish pass:

1. Render the current HTML in a real browser after creating the first draft.
2. Inspect each diagram's full rendered extent at desktop/native size and a narrow viewport. Read every label at its intended size; follow every connector from source to arrowhead; verify that no text, arrow, or box touches or overlaps another; inspect clear space around labels, nodes, and boundaries.
3. Write down each concrete defect with its location and a specific correction. Do not make a batch of geometry edits from memory without re-rendering.
4. Apply a focused correction, render again immediately, and check that the original defect is gone and no new overlap or wrong endpoint was introduced.
5. Repeat steps 2–4 after every diagram change until all applicable checks pass. Then do one final review of every diagram and the containing page at desktop and mobile widths.
6. Report the checks performed, material iterations/fixes, remaining limitations, and whether the acceptance checks passed. If browser rendering or visual inspection was unavailable, say so plainly and do not claim enterprise readiness.

“Enterprise-ready” describes completion of this evidence, semantics, visual, accessibility, and audience-fit review for the agreed scope; it is not a blanket guarantee of correctness, compliance, security, or production suitability.

## Output format

For HTML/SVG, place the diagram in one saved `.html` file with inline `<svg>`, a `viewBox`, and minimal embedded CSS. Use semantic groups and stable IDs where that helps later edits. Keep presentation notes outside the SVG drawing area. Do not use raster screenshots as the only source when editable vector output is feasible.

For high-stakes or customer-facing architecture, include a separate evidence map and have a knowledgeable reviewer confirm technical semantics before publication.

## Enterprise and customer-facing handoff

Apply only the checks relevant to the diagram's purpose. Record out-of-scope items as such rather than implying they were assessed. Keep the diagram concise; place detail in the evidence/handoff note.

- **Status and ownership:** Identify current state, proposed state, or conceptual view; intended audience and use; system/service owner; version or review date; and whether the diagram is draft, reviewed, or approved. Never imply approval from visual polish.
- **Evidence and decisions:** Cite source documents, repositories, or decisions with versions/locations where practical. Separate confirmed facts, proposed choices, assumptions, and unresolved questions. Track decisions that materially affect the design.
- **Security and privacy (when relevant):** Identify data classes and trust boundaries; show identity, authorization, encryption, secrets, logging, residency, and control ownership only when sourced. Record threat-model or privacy-review status and gaps. Do not infer compliance from a control icon or boundary.
- **Reliability and operations (when relevant):** Include only supported availability/failure domains, recovery objectives, backup/restore, scaling/capacity, monitoring, alerting, operational ownership, and runbook/support paths. Mark targets and mechanisms that still need confirmation.
- **Interfaces and data (when relevant):** Make flow direction and purpose explicit; include supported protocols, data contracts, error/retry behavior, and ownership. Mark unknown semantics rather than fabricating them.
- **Review handoff:** Name the required reviewers by role (for example, architecture, service, security, privacy, data, and operations owners) according to scope. Record review status, date, and unresolved findings. A diagram is not ready for implementation approval until the accountable owner has reviewed its technical semantics.
- **Sharing hygiene:** Do not copy credentials, tokens, secrets, or unnecessary personal/customer data into diagrams, evidence notes, screenshots, or public repositories. Prefer data-class or role labels. Follow the source material's classification and access rules, and confirm that shared references are accessible to their intended recipients.

Report status narrowly, for example: “visual QA passed; evidence mapped; security and operations review pending.” This checklist supports a controlled handoff; it does not itself establish enterprise readiness, compliance, security, or production suitability.

## Example gallery

Use the repository's examples to calibrate audience, scope, evidence notes, and diagram type. They are fictional teaching scenarios, not reference architectures or claims about a real deployment. Each example has a source brief and evidence map. Preserve that distinction when adapting them; replace every fictional fact with supplied evidence.

- `examples/context-container.html` — solution architect: a clinic appointment service, its users and neighboring systems, followed by an application-level container view.
- `examples/cloud-architecture.html` — cloud architect: an illustrative event-driven media-processing workload with public ingress, private processing, object storage, queue, and managed services; all provider choices are assumptions.
- `examples/component.html` — developer: a single appointment API container decomposed into request, availability, booking, persistence, and reminder components.
- `examples/trust-boundary.html` — security reviewer: a fictional document-upload flow crossing user, application, and external scanning trust zones, with trust decisions and unspecified controls visible.
- `examples/flowchart.html` — product/business analyst: a user flow for rescheduling an appointment, including a decision, recovery route, and terminal outcomes.
- `examples/sequence.html` — developer: a booking confirmation interaction, with a timeout branch and asynchronous notification.
- `examples/deployment.html` — platform/solution architect: an environment placement view across a public edge, private application zone, and managed data services. Placement is illustrative and must not be treated as a security recommendation.
- `examples/business-process.html` — business and delivery teams: an expense reimbursement process with role lanes, policy decision, rejection path, and completion states.

The examples deliberately use different fictional domains from the original order-processing sample. Read each adjacent `*-evidence.md` before treating its diagram as an input or template.

## References for selecting views

- [C4 model diagram types](https://c4model.com/diagrams) describes context, container, component, code, and supporting dynamic/deployment views, and advises using only levels that add value.
- [OMG BPMN overview](https://www.omg.org/bpmn/) describes BPMN as a notation intended to be understandable to business users while representing process semantics for technical users.
- [OMG UML overview](https://www.omg.org/UML/what-is-uml.htm) groups UML structural, behavioral, and interaction diagrams, including deployment, activity, state-machine, and sequence diagrams.
- [AWS reference architecture diagrams](https://docs.aws.amazon.com/reference-architecture-diagrams/) provides recurring cloud architecture examples such as application, data, migration, and DevOps architectures. Vendor examples are pattern references, not evidence for a user's actual system.
- [Mermaid architecture diagrams](https://mermaid.js.org/syntax/architecture) and [Mermaid layout options](https://mermaid.js.org/config/layouts) show architecture-as-text and generated layout approaches.
- [PlantUML sequence diagrams](https://plantuml.com/en/sequence-diagram) show text-defined participants and messages with generated placement.
- [Structurizr DSL](https://docs.structurizr.com/dsl) keeps an architecture model and multiple views together; its [dynamic-view cookbook](https://docs.structurizr.com/dsl/cookbook/dynamic-view/) demonstrates ordered interactions.
- [diagrams.net](https://www.diagrams.net/) is a visual editing option for flowcharts, UML, database models, BPMN, and architecture views.
