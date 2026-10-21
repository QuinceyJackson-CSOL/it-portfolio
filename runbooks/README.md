# Runbooks

Sanitized versions of the operational runbooks I maintain. Each one came out of a real ticket, and each is written so that **a new hire could work the ticket from the file alone.** See [how I build them](../01-basic-it-support/building-an-it-knowledge-base/).

| System | Runbook | Covers | Case study |
|---|---|---|---|
| Box + Okta | [box-access-requests.md](box-access-requests.md) | Folder access, the two permission systems, IdP-provisioned roles, least-privilege elevation | [Two permission layers](../06-software-systems/saas-access-two-permission-layers/) |
| Figma + Okta SSO | [figma-access-requests.md](figma-access-requests.md) | SSO app assignment, pending invites, SCIM hazards | [Pending invite behind SSO](../06-software-systems/figma-sso-pending-invite/) |
| Microsoft 365 | [m365-distribution-lists.md](m365-distribution-lists.md) | Distribution list types, membership, synced/dynamic lists, MX check | [DNS MX diagnosis](../04-networking/email-routing-dns-mx-diagnosis/) |
| Chrome / Edge | [browser-scam-notifications.md](browser-scam-notifications.md) | Scareware triage, severity tree, notification-permission removal | [Scareware triage](../02-cybersecurity/scareware-browser-notification-triage/) |
| Outlook | [outlook-troubleshooting.md](outlook-troubleshooting.md) | Triage questions, Safe Mode, add-in bisection, Office repair | [Copy/paste triage](../01-basic-it-support/outlook-copy-paste-triage/) |

> Items marked **TODO** are environment details that hadn't been confirmed when the runbook was written. I leave them visible on purpose, because a confident wrong runbook is worse than an honest incomplete one.
