# Diagram visual QA report

Date: 2026-10-16

Scope: repository example gallery and GitHub Pages landing page. Scenarios are fictional teaching examples.

## Iteration log

| Review | Finding | Change | Recheck |
| --- | --- | --- | --- |
| Pages assembly | The initial site copy nested the examples directory and broke expected example URLs. | Assemble `docs/` at the site root, then copy the contents of `examples/` into `/examples/`. | Check the assembled paths and HTTP responses before publishing. |
| Research page route | Static artifact deployment does not convert the Markdown research source into the `.html` URL linked from the landing page. | Add a standalone `docs/research-notes.html` page and require it in the package validator. | Request the route in the assembled site at all tested widths; confirm HTTP 200 and no page overflow. |
| Research page mobile table | The three-column selection table compressed its text at phone width. | Stack each row into a labeled card below 600 px while retaining table semantics. | Re-render at 320 and 390 px; confirm the page remains within the viewport and the source basis is readable. |
| Clinic context/container | A relationship label crowded adjacent elements; actor responses were not consistently explicit. | Reposition the label and draw clear bidirectional arrows for request/response exchanges. | Render at desktop and narrow widths; trace arrowheads and label clearances. |
| Booking sequence | The first persistence path ended at the schedule participant, and the timeout outcome was underspecified. | Add an appointment store, connect persistence to it, and show the timeout branch and response. | Re-render all participants and follow messages top to bottom. |
| Booking sequence final sweep | The alternative frame excluded the patient lifeline even though both success and failure responses target the patient. | Extend the fragment around all participants affected by the alternatives. | Re-render at desktop and narrow widths; verify the frame encloses the branch participants and responses. |
| Deployment | An asynchronous route visually crossed an unrelated node, making its endpoint unclear. | Route the worker path around the queue and label the illustrative boundary. | Re-render and inspect crossings, endpoints, and boundary clearance. |
| Reimbursement process | A policy threshold was described without support in the process drawing; a note crowded the canvas. | Remove the unsupported threshold and move explanation outside the drawing. | Re-render lanes and decision paths at desktop and narrow widths. |
| Reimbursement process final sweep | The approval branch and payment completion arrowheads converged at the same activity edge and looked bidirectional. | Route the approval branch into the top of the payment activity and keep the completion path on its right edge. | Re-render and trace both endpoints; each now has a single clear direction. |
| Landing page | The embedded process preview was cropped on narrow screens. | Hide the iframe at narrow widths and provide a direct link to the complete accessible diagram. | Review the page at 320, 390, 768, 1024, and 1440 CSS pixels. |
| Landing page final sweep | At 320–390 px, the install command's intrinsic width expanded the lower grid beyond the viewport. A stale local preview bundle initially hid the fix. | Constrain the narrow layout grid with `minmax(0, 1fr)` and assemble the preview into a fresh directory from current sources. | Rebuild the bundle; browser-measure page width and re-render at 320, 390, 768, 1024, and 1440 px. No page-level overflow remains. |
| Diagram keyboard navigation | Focusable scroll regions did not respond to arrow keys in the browser. | Add explicit left/right and Home/End keyboard scrolling, with visible instructions. | Focus each region and verify horizontal position changes with keyboard input. |
| Order processing | Labels and small diagram text became too small when the whole wide canvas was scaled to a phone. | Preserve the diagram's native SVG scale, provide horizontal scrolling, a visible instruction, and a keyboard-focusable named scroll region. | Render desktop and narrow viewports and inspect all numbered flow paths. |
| Order processing flow order | The HTTP response was numbered after the asynchronous email path even though the source does not establish their relative ordering. | Leave the response unnumbered and keep the sequence numbers on the ordered event/worker path. | Compare flow order with the fictional source brief and evidence map. |
| Component label spacing | In the first render, availability, save, and persistence labels crowded each other or touched node edges. | Move labels into open whitespace, shorten the slot-result label, and increase the repository-to-store gap. | Rerender at native size and inspect every label against nearby nodes and connector lines. |
| Cloud architecture | The new workload example could be mistaken for a provider-specific deployment or security reference. | Use generic cloud service labels, mark the boundary illustrative, and list unknown identity, region, resilience, and network details. | Trace synchronous ingress, metadata/object persistence, queue-worker path, output, and failure signal; verify every label against its evidence note. |
| Component diagram | Component responsibilities could be confused with independently deployed services. | Keep all components inside one API container and call out the assumed process boundary. | Check each dependency direction and confirm the store/queue are outside the application component boundary. |
| Trust-boundary flow | A boundary or scanner symbol might imply security controls that were not established. | Label the zones as assumptions and explicitly state that boundaries do not prove controls; show clean and rejected outcomes. | Trace the upload, quarantine, scanner request/verdict, promotion, and retention route; check crossings and endpoints. |
| User flowchart | A no-availability branch or canceled change could lose the existing appointment outcome. | Add a branch to retain the current appointment and a separate clinic-contact route. | Follow Yes and No paths and confirm each ends in a named outcome without an unexplained loop. |

## Acceptance review

- The landing page, research page, and nine example pages were rendered in a browser at 320, 390, 768, 1024, and 1440 CSS pixels (55 page/viewport combinations). Local links and diagram scripts loaded without HTTP errors or browser exceptions; no page-level horizontal overflow remained. A native-size collision check found no edge labels overlapping node rectangles, and the rendered labels were manually inspected for arrow/label and text/box clearance.
- Each of the nine diagrams was visually reviewed at desktop and narrow width. Text, arrows, and boxes were checked for visible separation; labels were repositioned where the first render showed crowding. SVG text boxes were measured against their viewBox; no labels extended outside the canvas. Flow endpoints, labels, boundaries, and spacing were inspected in the rendered output.
- Each numbered or labeled flow was checked from source to arrowhead and against the scenario notes. Bidirectional exchanges use opposing arrowheads; dashed lines denote asynchronous flows where applicable.
- Node text, flow labels, frame boundaries, legends, and captions were inspected for clipping, overlap, and unintended crossings. Wide diagrams remain scrollable on narrow screens instead of shrinking labels below their intended size.
- The narrow-screen scroll regions retain native diagram width, are named for assistive technology, and respond to left/right and Home/End keys. Narrow-screen pages display scrolling instructions.
- The landing page links to the complete diagram instead of displaying a cropped mobile iframe.
- Example-specific facts, assumptions, and limitations are documented in adjacent `*-evidence.md` files. Cloud placement is explicitly illustrative; examples do not assert production security, availability, compliance, or standards conformance.

## Limits

This is a visual and structural review of fictional examples, not validation of a production architecture or a substitute for domain-owner review. Horizontal scrolling is intentional for wide diagrams. The design examples are not a guarantee of conformance to C4, UML, or BPMN; the notation and semantics must be checked for the intended deliverable.
