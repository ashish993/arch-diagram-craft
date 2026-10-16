# Architecture Diagram Craft

An agent skill for producing source-grounded software architecture and data-flow diagrams with readable labels, clear boundaries, and correctly directed connectors.

**Created and maintained by Ashish Sharma.**

**Project page:** [Architecture Diagram Craft](https://ashish993.github.io/arch-diagram-craft/)

## Install

This repository follows the Agent Skills folder convention. Install with a compatible skills installer, or copy/symlink `skills/arch-diagram-craft/` into your agent's skills directory.

Example with the `skills` CLI:

```sh
npx skills add ashish993/arch-diagram-craft
```

## Use

Ask your agent to create or review an architecture diagram and provide the source material. Example:

> Create a data-flow diagram from these architecture notes. Keep facts separate from assumptions, number the flows, save editable HTML/SVG, and include an evidence map.

The skill requires inspection of the rendered output. A successful generation or structural check alone is not visual QA.

## Examples

The [`examples/`](examples/) directory contains original, fictional HTML/SVG examples for different audiences:

- `context-container.html` — system context and logical containers for solution architects.
- `sequence.html` — ordered booking interaction for developers.
- `deployment.html` — runtime placement for platform and solution architects.
- `business-process.html` — roles, decisions, handoffs, and outcomes for business and delivery teams.
- `order-flow.html` — numbered synchronous and asynchronous data flows.
- `QA_REPORT.md` — visual review iterations, acceptance checks, and limits for the example gallery.

Each new scenario has a companion `*-evidence.md` that states what the example assumes and what would need confirmation. [Research notes](docs/research-notes.md) explain why these view types were selected; they are common established forms, not a measured popularity ranking.

## Scope

The skill covers architecture, data flow, deployment, sequence, business-process views, and diagram review. It guides an agent; it is not a diagram editor, layout engine, or guarantee that an agent's output is correct. It can work with HTML/SVG, diagram-as-code tools, or visual editors. Quality depends on source evidence and review of the actual rendered output.

## Development

Keep changes focused. For behavior changes, add a realistic fixture/request and record whether the resulting diagram meets the quality checks in `SKILL.md`. Review the rendered artifact, not just its source.

## License

MIT. See [LICENSE](LICENSE).
