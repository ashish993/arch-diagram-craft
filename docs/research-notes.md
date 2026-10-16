# Diagram types selected for the examples

**Research date:** 2026-10-16

This is a practical cross-audience selection, not a statistical ranking of diagram popularity. The sources establish recognized diagram families and intended uses; they do not provide a comparable frequency survey across solution architects, developers, and business users.

| Example | Audience question | Basis |
| --- | --- | --- |
| Context + container | What is the system boundary and what are its major parts? | The [C4 model](https://c4model.com/diagrams) names context, container, component, and code as its core static views, and says context/container may be sufficient for many development teams. |
| Component | How is one application container divided into cohesive responsibilities? | [C4 component guidance](https://c4model.com/diagrams/component) recommends this view only when it adds value; components belong inside one container. |
| Cloud architecture | Which workload components, managed services, network zones, and paths make up a cloud solution? | [AWS reference architecture diagrams](https://docs.aws.amazon.com/reference-architecture-diagrams/) show recurring domain and deployment patterns; [Azure architecture-diagram guidance](https://learn.microsoft.com/azure/well-architected/architect-role/design-diagrams) discusses context, container, deployment, and data-flow views. |
| Trust-boundary data flow | What data crosses ownership/trust zones, and where should threat-model questions be asked? | Azure's [data-flow and threat-model diagram guidance](https://learn.microsoft.com/azure/well-architected/architect-role/design-diagrams) calls out processes, stores, external entities, flows, and trust boundaries. AWS guidance also recommends documenting workload data flows before selecting network controls. |
| Flowchart / user flow | What steps and decisions shape a user's route and recovery options? | Azure Well-Architected diagram guidance identifies user-flow/journey views as a way to show end-to-end persona steps. |
| Sequence | What messages occur, in what order, and what happens on a branch? | [OMG UML](https://www.omg.org/UML/what-is-uml.htm) lists sequence diagrams among UML interaction diagrams. |
| Deployment | Where does software run and how is it placed? | C4 includes deployment as a supporting diagram; [AWS reference architecture diagrams](https://docs.aws.amazon.com/reference-architecture-diagrams/) illustrate recurring deployment and cloud architecture views. |
| Business process | Who performs each activity, where are decisions, and what outcomes follow? | [OMG BPMN](https://www.omg.org/bpmn/) says its process notation is intended to be understandable to business users while representing semantics for technical users. |

The repository examples are original fictional scenarios and native HTML/SVG drawings. They do not copy text or diagrams from these sources. The standards and catalogs inform the view selection only. See each adjacent `*-evidence.md` file for scenario facts and assumptions.

## Diagram-tool review

The skill was also compared with current official documentation for several established authoring approaches:

- The [Mermaid repository](https://github.com/mermaid-js/mermaid) describes text-based generation for diagrams; its [architecture syntax](https://mermaid.js.org/syntax/architecture) and [layout documentation](https://mermaid.js.org/config/layouts) cover grouped services and generated layout options.
- The [PlantUML repository](https://github.com/plantuml/plantuml) describes diagrams from textual descriptions. Its [sequence-diagram documentation](https://plantuml.com/en/sequence-diagram) defines participants and messages in text and handles their placement.
- The [Structurizr repository](https://github.com/structurizr/structurizr) describes a C4 model that produces multiple views. Its [DSL documentation](https://docs.structurizr.com/dsl) models elements and relationships once, while its [dynamic-view cookbook](https://docs.structurizr.com/dsl/cookbook/dynamic-view/) shows ordered interactions drawn from those relationships.
- The [draw.io repository](https://github.com/jgraph/drawio) and [developer wiki](https://github.com/jgraph/drawio/wiki) describe a visual editor with a native XML graph model and editable diagram formats. That makes retaining the editable source beside rendered exports a useful handoff check.

The useful common design lessons are to separate the system model from each audience-specific view, keep a text/native model source available when repeatability matters, and treat generated layout as a draft that still needs semantic and visual review. The skill adds those ideas without requiring one authoring tool: exact rendering, evidence, relationship direction, accessibility, and intended-use checks remain necessary whichever tool is chosen.
