# Architecture Diagram Craft

Architecture Diagram Craft is an open-source skill that helps AI agents create and review software diagrams from architecture notes, requirements, and code. It is designed for solution architects, developers, platform teams, and business stakeholders who need diagrams that explain systems and processes clearly—and can be checked against their source material.

The skill guides the agent to identify the audience and purpose, distinguish documented facts from assumptions, map components and flows, choose an appropriate view, and preserve an evidence trail. It also requires rendering and inspecting the finished diagram for correct arrow direction, readable text, spacing, and overlaps, then correcting defects and checking the updated output.

This repository includes the reusable skill, original fictional examples for system design, cloud architecture, components, trust boundaries, flowcharts, sequence, deployment, business processes, and data flow; companion evidence notes; visual QA records; and a GitHub Pages site. The skill works with HTML/SVG, diagram-as-code tools, and visual editors; it provides guidance rather than a diagram editor or automatic layout engine.

**Created and maintained by Ashish Sharma.**

**Project page:** [Architecture Diagram Craft](https://ashish993.github.io/arch-diagram-craft/)

## Install

### Claude Code and Codex

From the root of the project where you want the skill available, install it for both tools with the [Agent Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add ashish993/arch-diagram-craft --skill arch-diagram-craft --agent claude-code --agent codex
```

For one tool, use `--agent claude-code` or `--agent codex`. Add `--global` to make it available across your projects for those tools instead of adding it to the current project.

### Other compatible tools

The repository uses the open Agent Skills folder format. The CLI supports many compatible agents; for example, to install the skill in Cursor, GitHub Copilot, or Gemini CLI, replace the agent names in the command:

```sh
npx skills add ashish993/arch-diagram-craft --skill arch-diagram-craft --agent cursor
```

You can target several agents in one command by repeating `--agent`. See the CLI's [supported agents](https://github.com/vercel-labs/skills#supported-agents) for exact names and project/global directories.

### Manual installation

Copy the skill folder into the location your tool scans. For example, from this repository:

```sh
# Claude Code, for this user
mkdir -p ~/.claude/skills
cp -R skills/arch-diagram-craft ~/.claude/skills/

# Codex, for this user
mkdir -p ~/.agents/skills
cp -R skills/arch-diagram-craft ~/.agents/skills/
```

For team-shared project installs, use `.claude/skills/arch-diagram-craft/` for Claude Code or `.agents/skills/arch-diagram-craft/` for Codex, then commit the copied folder. Restart the agent if it does not discover the new skill automatically. See the official [Claude Code skills guide](https://code.claude.com/docs/en/skills) and [Codex skills guide](https://developers.openai.com/codex/skills) for current discovery rules.

## Use

Ask your agent to create or review an architecture diagram and provide the source material. Example:

> Create a data-flow diagram from these architecture notes. Keep facts separate from assumptions, number the flows, save editable HTML/SVG, and include an evidence map.

The skill requires inspection of the rendered output. A successful generation or structural check alone is not visual QA.

## Examples

The [`examples/`](examples/) directory contains original, fictional HTML/SVG examples for different audiences:

- `context-container.html` — system context and logical containers for solution architects.
- `cloud-architecture.html` — illustrative cloud media-processing workload for architecture and platform teams.
- `component.html` — a focused component decomposition of one appointment API container.
- `trust-boundary.html` — a document-upload data flow crossing user, application, and third-party zones.
- `flowchart.html` — a patient appointment-rescheduling flow with decisions and recovery paths.
- `sequence.html` — ordered booking interaction for developers.
- `deployment.html` — runtime placement for platform and solution architects.
- `business-process.html` — roles, decisions, handoffs, and outcomes for business and delivery teams.
- `order-flow.html` — numbered synchronous and asynchronous data flows.
- `QA_REPORT.md` — visual review iterations, acceptance checks, and limits for the example gallery.

Each new scenario has a companion `*-evidence.md` that states what the example assumes and what would need confirmation. [Research notes](docs/research-notes.md) explain why these view types were selected; they are common established forms, not a measured popularity ranking.

## Scope

The skill covers system and cloud architecture, component, trust-boundary/data-flow, flowchart, deployment, sequence, and business-process views, plus diagram review. It guides an agent; it is not a diagram editor, layout engine, or guarantee that an agent's output is correct. It can work with HTML/SVG, diagram-as-code tools, or visual editors. Quality depends on source evidence and review of the actual rendered output.

## Development

Keep changes focused. For behavior changes, add a realistic fixture/request and record whether the resulting diagram meets the quality checks in `SKILL.md`. Review the rendered artifact, not just its source.

## License

MIT. See [LICENSE](LICENSE).
