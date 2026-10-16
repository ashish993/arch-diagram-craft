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

Ask your agent to create or review an architecture diagram and provide the source material. If you use a tool that supports skill mentions, invoke `arch-diagram-craft`; otherwise ask the agent to use the installed skill by name. Replace the bracketed sections in these prompts with your requirements or source files.

For broad requests, the skill reviews what is known, asks up to three focused questions if a missing decision would change the diagram, then gives a short plan before implementation. It carries noncritical gaps forward as labeled assumptions instead of turning the first reply into a long questionnaire. A requested plan is not an extra approval step: when you ask it to create the diagram, it proceeds after presenting the plan.

### Start with a vague request

```text
Use the arch-diagram-craft skill to help me create a diagram for [system or process]. First review what I have provided. If any missing detail could change the diagram's purpose, scope, audience, or meaning, ask me up to three focused questions before drawing. After I answer, summarize the selected diagram view, evidence, scope, deliverables, and remaining assumptions in a short plan, then create it. If a detail is not critical, mark it as an assumption and keep going. Render and visually inspect the result, fix and re-render defects, and include an evidence note.
```

### AWS three-tier architecture

```text
Use the arch-diagram-craft skill to create an AWS three-tier architecture diagram for [application/use case].

Requirements:
- Users: [user types and entry points]
- Web tier: [hosting and static-content requirements]
- Application tier: [runtime, APIs, scaling requirements]
- Data tier: [database, storage, backup and recovery requirements]
- Region and availability: [region, AZ count, uptime or recovery targets]
- Security and network: [identity, public/private subnets, ingress/egress, trust boundaries]
- Constraints: [budget, existing services, compliance, or services to avoid]

Use the AWS services and architecture facts I provide. Mark any proposed service or unspecified design choice as an assumption; do not imply it is deployed or validated. Show the account/region boundary, public and private network zones, tier placement, and clearly directed, labeled traffic flows. Save editable HTML with inline SVG and a companion evidence note. Render it and check every label, arrow endpoint, boundary crossing, spacing, and overlap at desktop and mobile sizes. Fix defects and re-render until the visual checks pass. List open design questions.
```

### System context and containers

```text
Use the arch-diagram-craft skill to create a system context and container diagram for [system]. Audience: [audience]. Use these requirements, architecture notes, and source files: [paste or link them]. Show users, the system boundary, neighboring systems, major applications/services/data stores, and labeled relationships. Separate facts from assumptions and unknowns; include an evidence map. Save editable HTML/SVG, render it, and fix any unreadable text, incorrect arrows, clipped content, or overlaps before delivery.
```

### Component diagram from a repository

```text
Use the arch-diagram-craft skill to inspect this repository and create a component diagram for [service/module/path]. Trace responsibilities and dependencies from the actual source code, interfaces, call sites, and tests. Do not infer components from folder names alone. Show supported component relationships and label inferred or uncertain boundaries. Include an evidence map with file references. Save editable HTML/SVG, render and visually inspect it, then correct and re-render any text, arrow, spacing, or overlap defects.
```

### Trust-boundary data flow

```text
Use the arch-diagram-craft skill to diagram [data/process] across its trust boundaries. Show actors, systems, data stores, boundary zones, and each data flow with direction and a concise label. Mark sensitive data and crossings only when supported by the provided evidence; list unknown controls rather than assuming them. Sources: [paste or link requirements/code]. Save editable HTML/SVG and an evidence map. Render and inspect arrow endpoints, labels, boundary crossings, readability, and spacing; fix and re-render any defects.
```

### Sequence diagram

```text
Use the arch-diagram-craft skill to create a sequence diagram for [user or system interaction]. Use these steps and source materials: [describe steps or link code/API docs]. Show participants, calls, responses, asynchronous events, and relevant failure or timeout branches in order. Do not invent behavior that is not specified; mark gaps as open questions. Save editable HTML/SVG with an evidence note, render it, and fix any incorrect message direction, hidden text, or overlap before delivery.
```

### Business flowchart

```text
Use the arch-diagram-craft skill to create a business flowchart for [process]. Audience: [business roles]. Start with [trigger], include [decisions, handoffs, exception/recovery paths], and end with the possible outcomes. Use plain language and show who performs each step. Base the flow on: [paste process notes]. Mark uncertain steps for confirmation. Save editable HTML/SVG, render it, and verify decision branches, arrow direction, readable text, and spacing; correct and re-render any defects.
```

These prompts request a reviewed draft; they do not replace architecture-owner review or production validation. The skill requires inspection of the rendered output. A successful generation or structural check alone is not visual QA.

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
