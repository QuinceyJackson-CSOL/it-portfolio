# Runbook: Figma access (through Okta SSO)

**The ticket this solves:** "Please get X into Figma," "X was added but never got an invite,"
"X can't log in to Figma."

> **Trainer's note:** Read §1–§4 to work a ticket. §5 covers troubleshooting. Anything marked
> **TODO** is a company detail nobody has confirmed yet. Confirm it, then delete the TODO.

---

## 1. Words you need first

| Word | Plain meaning |
| --- | --- |
| **SSO (single sign-on)** | Figma doesn't check passwords. It hands the person to Okta, and Okta decides. |
| **Okta** | The company's "front door" for apps. One login, then tiles for every app you're allowed. |
| **Assignment** | In Okta, the link "this person may use this app." No assignment means Okta blocks them. |
| **Individual vs Group assignment** | Assigned directly to the person, or inherited because they're in a group that has the app. Both work the same way. |
| **Figma admin console** | Figma's own settings, where Figma admins (usually on the design team) add members and pick seat types. |
| **Pending invite** | The person was added in Figma but hasn't signed in yet. Their first sign-in accepts it. |
| **Provisioning / SCIM** | Okta automatically creating, updating and deactivating accounts inside Figma. |

## 2. The one concept that explains everything

**Two separate systems both have to say yes.**

```
┌─ FIGMA ADMIN CONSOLE ──────────────┐   ┌─ OKTA ─────────────────────────────┐
│ Question: Is she a member of the    │   │ Question: Is she allowed to open   │
│           company Figma? What seat? │   │           Figma at all?            │
│ Done by:  Figma admin (design team) │   │ Done by:  IT (you)                 │
│ Where:    figma.com → Admin         │   │ Where:    Okta Admin → Applications│
│                                     │   │           → Figma → Assignments    │
└─────────────────────────────────────┘   └────────────────────────────────────┘
```

If the Figma side is done but Okta isn't, the person sees a **pending** invite that they can't
accept, because the SSO step bounces them. That's what happened in [this case study](../06-software-systems/figma-sso-pending-invite/).

**Don't wait on the invite email.** With SSO, the email may never arrive. The person accepts by
**signing in**.

## 3. Decision tree: start here

```
Ticket: "get X into Figma"
│
├─ Okta Admin → Directory → People → search X. Do they exist and are they Active?
│  │
│  ├─ NO  → New hire? Find the onboarding request; Okta account comes first.
│  │        Freelancer / non-work email? Okta isn't the route → Figma guest access.
│  │        That's a policy call → ask the IT manager + the Figma admin.
│  │
│  └─ YES → Applications → Figma → Assignments → search X. Are they listed?
│           ├─ NO  → §4: assign them. Then tell them how to sign in.
│           └─ YES → Okta isn't the blocker. Check the Figma side (§5):
│                    was the invite sent to the EXACT Okta email? Seat approved?
```

## 4. Procedure: give someone Figma

1. **Okta Admin → Applications → Applications → Figma → Assignments** tab.
2. Check the left filter: **Groups**. Is there a group that grants Figma?
   - **Yes:** **Directory → Groups → that group → Assign people** → add the person. This is
     the preferred route.
   - **No / unsure:** **Assign → Assign to People** → search → **Assign** → **Save and Go
     Back** → **Done**. The assignment will show as **Type: Individual**.
   - **TODO:** record which one this environment uses for Figma.
3. Confirm the **exact email** with the Figma admin. It must match the Okta username
   character for character. Copy it from Okta, not from the ticket.
4. Reply on the ticket to the requester, **CC'ing the new user**, with these sign-in steps:
   - click the **Figma** tile on the Okta dashboard, **or**
   - figma.com → **Log in** → **Log in with SSO** → work email.
5. Set the ticket to **Waiting on Customer**. Follow up after about 2 days so the auto-closer
   doesn't close it without an answer.
6. Verify: Figma app → **View Logs** (or **Reports → System Log**) shows an SSO success.
   Confirm with the requester, then resolve.

### Don't

- **Don't remove an Individual assignment before the person is in the group.** If provisioning
  is on, unassigning can **deactivate their Figma account**. Add them to the group first, then
  use **Convert assignments** or remove the individual entry.
- **Don't trust the spelling in the ticket.** One ticket's subject said "<misspelled surname>". The real
  account is "<surname>".
- **Don't try to fix access inside Figma alone.** Okta is the source of truth. See
  [box-access-requests.md](box-access-requests.md) for the same lesson.

## 5. Symptom → cause → fix

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Added in Figma, invite **pending**, can't get in | No Okta assignment | §4 |
| "Never got an invite email" | Normal under SSO | Sign in through the Okta tile or **Log in with SSO** |
| Okta: "User is not assigned to this application" | No Okta assignment | §4 |
| Signs in but lands in an empty/personal Figma, not the company's | Figma invite went to a different email | Figma admin re-invites using the exact Okta email |
| Not in Okta at all | New hire not onboarded, or a freelancer | §3, "NO" branch |
| Okta: "Unable to sign in" | A sign-on policy denied it | System Log → read the DENY reason. See [this investigation](../02-cybersecurity/recurring-sso-auth-failure-investigation/) |

## 6. Environment facts confirmed so far

- Figma here signs in through **Okta SSO**. Confirmed.
- A **design-team Figma admin** adds people in Figma's console.
- An **Individual** Okta assignment is enough for access. Confirmed.
- **TODO:** group-based or individual assignment as the norm?
- **TODO:** Is Provisioning (SCIM) on? Check the **Provisioning** tab.
- **TODO:** Does a Figma seat need approval from the IT manager or a budget owner?

## Past tickets

| Date | Ticket | What happened |
| --- | --- | --- |
| — | [New hire stuck at pending invite](../06-software-systems/figma-sso-pending-invite/) | Added in Figma but no Okta assignment → assigned in Okta → in |
