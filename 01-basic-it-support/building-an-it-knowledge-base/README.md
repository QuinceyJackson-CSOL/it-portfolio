# Building an IT runbook system that a new hire can work from alone

**Category:** Basic IT Support · Documentation / Knowledge management
**Environment:** Plain Markdown in a git-friendly folder structure, searchable with `grep`
**Skills:** Technical writing, knowledge management, process design, continuous improvement
**Status:** Ongoing; this portfolio's [runbooks](../../runbooks/) are sanitized versions of it

---

## Problem
As a new member of the IT team, my ticket knowledge was scattered across closed tickets and chat threads. Repeat issues meant re-solving the same problems, and nothing showed what had worked before.

## Design
Two document types, each with a clear job:

| Type | Purpose | Example |
|---|---|---|
| **Runbooks** (one per system) | "How do I do this?" A reusable procedure | Box folder access, Outlook troubleshooting |
| **Ticket notes** (one per ticket) | "What actually happened?" Raw material | The request, what I checked, what surprised me |

**The loop:** check the runbook → work the ticket → write the ticket note while it's fresh → fold anything reusable back into the runbook. *The runbook is the asset, and the ticket notes are raw material for it.*

A **symptom lookup table** at the top answers *"how have we fixed this before?"* by going from symptom to runbook to past tickets to what fixed it.

## The writing standard
The test I hold every runbook to: **could a new hire work the ticket from this file alone, with no one to ask?**

1. **Glossary first.** Define vendor jargon in plain words before using it.
2. **Lead with the one concept that explains the rest.** For Box, that's "there are two separate permission systems."
3. **Decision tree before procedures.** Work out which situation you're in before you click anything.
4. **Numbered clicks, with bold button names.**
5. **Symptom → cause → fix tables,** because they're faster to scan mid-ticket than prose.
6. **Say what NOT to do, and why.** The traps are the valuable part.
7. **Annotated, redacted screenshots** for anything visual.
8. **Mark unknowns `TODO`** rather than guessing. A confident wrong runbook is worse than a short honest one.

## Results
- Five runbooks in the first month: content management with IdP-provisioned access, design-tool SSO, distribution lists, browser scareware, and Outlook.
- Every runbook here came out of a real ticket, and the lessons are written back in, including my own mistakes.

## Why this matters for systems and security roles
Runbooks are how operations teams scale, and incident-response playbooks follow the same pattern.
