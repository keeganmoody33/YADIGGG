---
title: "ADR-0010: CONTEXT and ADR Are Required Handoff Nodes"
project: yadiggg
status: accepted
type: architecture_decision
tags: [yadiggg, adr, handoff, context]
---

# ADR-0010: CONTEXT and ADR Are Required Handoff Nodes

## Status
Accepted

## Context
The project lost handoff fidelity because chat decisions were not consistently written into `CONTEXT.md` or ADR files. Obsidian then showed many notes but no reliable decision spine.

## Decision
Every future material decision must update at least one of:

- `CONTEXT.md` for domain vocabulary and current architecture map.
- `docs/adr/YYYY-or-number-title.md` for committed decisions and rejected alternatives.
- A status field in the affected file frontmatter.

## Consequences
- New sessions should read `CONTEXT.md` and relevant ADRs first.
- If a file is superseded, that must be stated in metadata or an ADR before the project moves on.
