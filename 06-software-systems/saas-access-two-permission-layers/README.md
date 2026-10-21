# Untangling a "simple" folder-access request across an IdP and a SaaS app

**Category:** Software & Systems · Identity & Access
**Environment:** Okta (IdP, provisioning), Box (enterprise content), ITSM ticketing
**Skills:** Identity & access management, least privilege, SaaS provisioning, root-cause analysis, access governance, documentation
**Status:** 🔍 Diagnosis complete; no grants made yet. Plan: set my app role through the IdP, grant Viewer on her own department's folder, and get owner approval for the cross-department folder
**Outcome so far:** Turned one confusing ticket into a reusable runbook, and identified a structural access-governance gap (below)

---

## Situation
A senior manager asked for access to two department folders in Box: her own department's and another department's. She could **see** both folders but couldn't **open** them. It looked like a two-minute task, but it took a morning of investigation and changed how I approach SaaS access requests.

## Investigation

**1. Scope the request before touching anything.**
Her screenshot identified the exact folders. Her job title settled the approval question: her own department's folder was routine, while the other department's folder needed the owner's written approval in the ticket as an audit trail. That split the ticket into two tracks, so the first wouldn't have to wait on the second.

**2. Explain "can see it but can't open it."**
Box permissions inherit downward, but a subfolder can override inheritance with its own collaborator list. She collaborated on the parent and wasn't on the subfolders' lists. That's expected behavior, not a bug. The fix is a grant on the **subfolder**, not a wider role on the parent, which would have granted far more than she asked for.

**3. Find out why I couldn't see the folders.**
API lookups from my account returned nothing: no search results and an empty root. I treated that as *"I can't see it"*, not *"it doesn't exist"*, because Box search only covers content the caller can access.

**4. Map the two separate permission systems.**

```
┌─ Collaboration role ───────────┐   ┌─ Enterprise role ─────────────┐
│ Scope: one folder              │   │ Scope: the whole tenant       │
│ Viewer → Editor → Co-owner     │   │ User → Co-Admin → Admin       │
│ Set by: the folder owner       │   │ Set by: admin / provisioning  │
└────────────────────────────────┘   └───────────────────────────────┘
```

The ticket needed both: a collaboration for her, and enough rights for me to make it.

**5. Correct my own misdiagnoses, twice.**
- I'd asked my manager for scoped admin rights. He said he'd made a change, but Box looked unchanged, and my first conclusion was that nothing had landed. My next theory was that **an unaccepted Box invite is invisible** (it stays Pending), which is the #1 cause in my own troubleshooting table, and one I'd applied to the requester but not to myself.
- That wasn't it either. My manager hinted that I could do it in Okta, and that was the answer: **he'd given me IdP admin rights, not Box rights.** Admin access in the IdP looks like nothing at all from inside the downstream app. Because Box is provisioned from Okta, a Box role should be pushable from the IdP as a profile attribute (not yet verified), so my earlier note that "self-elevation is impossible in Box" was true only inside Box's own console.

**6. Check the group path in the IdP.**
- The Okta group named after the app was the **licensing** group (nearly every employee), which controls who gets an account, not which folders they can open.
- **Push Groups was empty.** No IdP group maps to any Box group, so every folder permission in the tenant is an individual, hand-managed collaboration.

## Planned resolution
1. After the admin route stalled, I realized the **folder owner** could make the grant without any admin rights. Box's **Request Access** button emails the true owner, so that's now step one in the runbook. Admin rights are for when the owner is unknown or unreachable.
2. Where elevation was needed, I asked for **named permissions** instead of "admin," and offered a narrower alternative (Co-owner on two folders) instead of tenant-wide content access.
3. Chose **Viewer** as the starting role. Upgrading later is one click, while clawing back over-granted access is a cleanup job.
4. Verification steps planned before closing: the collaboration shows the right person at the right role, and **the requester confirms she can open it.** Clicking the button doesn't close the ticket.

## Security considerations
- **Least privilege:** Viewer first, a subfolder grant instead of widening the parent, and named Co-Admin permissions instead of blanket admin. *View and edit users' content* is effectively read/write on every file the company owns, so I flagged it as such.
- **Source of truth:** a role changed directly in Box would be overwritten on the next IdP sync, so the fix belongs in the IdP.
- **Change control:** any role elevation gets logged in the ticket (what, when, and who approved), alongside the IdP's own system log.
- **Destructive-action hazards documented:** in the IdP console, "Remove all people from this group" on the licensing group would deprovision the app company-wide, and the unassign ✕ sits right next to the edit pencil. Both are recorded as do-not-touch items in the runbook.

## Governance finding (to raise with my manager)
With no group push, folder access can't be reviewed or revoked in one place, so offboarding means hunting down individual collaborations. **Recommendation:** IdP groups pushed to the app and collaborated onto department folders, so that access reviews and offboarding have a single control point.

## What I learned
- Ask **where a permission is administered** before deciding what's possible. An IdP changes the answer.
- "I gave you access" needs a follow-up question: *in which system?*
- Run your own troubleshooting table on yourself before you escalate.

📘 Runbook produced from this ticket: [Box folder access](../../runbooks/box-access-requests.md)
