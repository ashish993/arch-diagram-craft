# Evidence map

Use this lightweight table when a diagram is derived from documents, source code, or an existing architecture.

| Diagram ID | Element or flow | Evidence location | Evidence statement | Status |
|---|---|---|---|---|
| N1 | API gateway | `architecture.md`, “Ingress” | Gateway accepts client HTTPS requests | Fact |
| F1 | Client → gateway | `sequence.md`, step 1 | Client sends authenticated request | Fact |
| N2 | Regional cache | No source found | Added as a likely optimization | Inference; omit unless confirmed |

Status values: **Fact**, **Inference**, **Open question**, or **Out of scope**. Cite a page/section, source file and symbol, or stable requirement ID when available. Do not treat a diagram in an older document as current without checking its date and authority.

Before delivery, check that every important node and flow has a source or is visibly marked as an inference/open question, and that important source statements are not silently omitted.

