---
name: arch-diagram-craft
description: Create and review source-grounded software architecture and data-flow diagrams as editable HTML with inline SVG. Use when a diagram must preserve documented components, trust boundaries, numbered flows, and readable, correctly directed connectors.
---

# Architecture Diagram Craft

Create diagrams that communicate a system accurately and can be inspected and edited. Use HTML with native inline SVG by default. Choose another format when the user or delivery context requires it.

## Workflow

1. **Establish the evidence.** Read the supplied architecture, requirements, and relevant source files. Separate explicit facts from inferences and unknowns. Do not add plausible-sounding components, vendors, protocols, regions, or security controls without evidence. For a review, record each requested correction before editing.
2. **Choose the view.** Use a component architecture for topology, a data-flow diagram for ordered exchanges, a deployment view for placement, or separate views when combining them would obscure relationships. Ask for a missing critical scope decision; otherwise state a small, reversible assumption.
3. **Plan the visual hierarchy.** Group by meaningful system or trust boundary. Keep labels concise, reserve color for a small number of focal items, and use a legend only when a visual encoding needs explanation. Prefer readable text and whitespace over fitting everything into one canvas. Split an overloaded view.
4. **Draw with explicit relationships.** Give each important connector a source, destination, direction, and concise label. Route it so its start and arrowhead visibly meet the intended elements. Number flows when sequence matters, and include a matching flow key if numbers alone are ambiguous. Do not imply direction through proximity or line crossings.
5. **Preserve traceability.** Keep a small evidence map alongside the diagram or in an accompanying note: diagram element/flow, source statement or file and location, and whether it is a fact, inference, or open question. Do not put internal review clutter on a presentation diagram unless requested.
6. **Render and inspect.** Open the actual output at its intended viewing size. Check every label for clipping and legibility; every box and connector for collision or overlap; every arrowhead for direction and endpoint; every boundary crossing for a clear ingress/egress; and every numbered flow against its evidence. Revise and inspect again after changes. A structural check or successful file generation does not replace visual inspection.
7. **Deliver clearly.** Provide the editable source and any requested export together. Summarize key assumptions and unresolved evidence gaps. Do not claim verification you did not perform.

## Required quality checks

- Components and relationships match the available evidence; distinguish facts from inferred placement or flow.
- No text, node, boundary, legend, or connector overlaps in a way that harms reading.
- Labels remain readable at the intended native size and are not clipped.
- Arrowheads point to the intended destination; bidirectional flows are shown deliberately.
- Trust boundaries are named and connector crossings are explicit.
- Numbered flows follow the stated process order and have no unexplained gaps or duplicates.
- The diagram has a clear title, scope, and legend when symbols or colors need one.
- HTML/SVG output is inspectable, self-contained where practical, and accessible: meaningful document title, SVG `role="img"`, and an accessible name/description.

## Output format

For HTML/SVG, place the diagram in one saved `.html` file with inline `<svg>`, a `viewBox`, and minimal embedded CSS. Use semantic groups and stable IDs where that helps later edits. Keep presentation notes outside the SVG drawing area. Do not use raster screenshots as the only source when editable vector output is feasible.

For high-stakes or customer-facing architecture, include a separate evidence map and have a knowledgeable reviewer confirm technical semantics before publication.

