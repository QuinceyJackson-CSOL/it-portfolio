# Using DNS to find where a company's email actually lives

**Category:** Networking · DNS
**Environment:** Hybrid SaaS tenant (Google Workspace for Drive/apps, Microsoft 365 / Exchange Online for mail), GAM, `dig`
**Skills:** DNS (MX, SPF/TXT), email routing, Google Workspace admin (GAM), Exchange Online distribution lists, troubleshooting methodology
**Status:** 🔍 Diagnosis complete; next step is checking membership in the Exchange admin center
**Outcome so far:** Found the right admin system with a 10-second DNS check, after one wrong turn

---

## Situation
A recently hired manager asked to confirm she was on the **All Staff** and **department** mailing lists, to be added if not, and to be told about any other lists relevant to her role.

## Investigation

**1. First wrong turn (kept here on purpose).** I started in Google Workspace because GAM was the admin tool I already had set up.

```bash
gam user user@example.com print groups   # → 0 groups
gam print groups                          # → 2 groups in the whole domain, neither a mailing list
```

GAM also showed *"Mailbox is setup: False"* for her account, which was the clue that Google wasn't handling her mail.

**2. Ask DNS which system receives the domain's mail.**

```bash
# output sanitized
$ dig +short MX example.com
0 example-com.mail.protection.outlook.com.

$ dig +short TXT example.com | grep spf
"v=spf1 ... include:spf.protection.outlook.com ..."
```

- **MX → `*.mail.protection.outlook.com`** means Exchange Online Protection receives inbound mail.
- **SPF includes `spf.protection.outlook.com`** means Microsoft 365 is an authorized sender.

**Conclusion:** the tenant is hybrid. Google Workspace handles Drive and apps, and **all mail and mailing lists live in Microsoft 365.**

## Planned resolution
1. **Exchange admin center → Recipients → Groups**, checking every tab: a "mailing list" can be a Distribution list, a Microsoft 365 Group, a Mail-enabled security group, or a Dynamic distribution group.
2. Before editing, check whether the list is **synced from the IdP**. If it is, a change made in Exchange gets overwritten, and the edit belongs in the IdP.
3. For "anything else relevant," compare memberships with a teammate in the same role, and get the owner's approval for any list belonging to another department.
4. Least privilege: **Exchange Recipient Administrator** covers all of this, and Global Admin isn't needed.

## Process finding
If she turns out to be missing from All Staff a month after starting, lists aren't part of onboarding. In that case I plan to propose two fixes: add distribution lists to the onboarding checklist, or make All Staff a **dynamic distribution group** built from directory attributes so it maintains itself.

## What I learned
**Check MX first on every email ticket.** It's a 10-second check that tells you which system to open. I automated it: see [`mail-provider-check`](../../03-automation-scripting/mail-provider-check/).

📘 Runbook: [Microsoft 365 distribution lists](../../runbooks/m365-distribution-lists.md)
