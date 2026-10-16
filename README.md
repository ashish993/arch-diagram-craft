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

## Scope

The initial version focuses on architecture, data flow, deployment boundaries, and diagram review. It guides an agent; it is not a diagram editor, layout engine, or guarantee that an agent's output is correct. Quality depends on source evidence, the agent, and visual review.

## Development

Keep changes focused. For behavior changes, add a realistic fixture/request and record whether the resulting diagram meets the quality checks in `SKILL.md`. Review the rendered artifact, not just its source.

## License

MIT. See [LICENSE](LICENSE).
