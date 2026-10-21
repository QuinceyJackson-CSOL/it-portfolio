# "Added but can't get in": fixing a stuck SaaS invite behind SSO

**Category:** Software & Systems · Identity & Access
**Environment:** Okta SSO, Figma (enterprise), ITSM ticketing
**Skills:** SSO / SAML app assignment, IdP administration, cross-team coordination, onboarding
**Status:** ✅ Resolved the same day. The IdP fix went in about an hour after the ticket opened
**Outcome:** New hire signed in; produced a reusable runbook for SSO-gated app access

---

## Situation
A design-team admin had added a new hire in Figma's admin console. The invite sat at **Pending**, no invite email ever arrived, and the new hire couldn't get in. The admin suspected SSO.

## Investigation
Two separate systems both have to say yes:

| System | Question it answers | Who manages it |
|---|---|---|
| Figma admin console | Is she a member of the company's Figma, and on what seat? | The app admin (design team) |
| Okta | Is she allowed to open Figma at all? | IT |

The Figma side was done, but the new hire had **no Okta assignment for the app**. Figma hands sign-in to Okta, and Okta blocks anyone the app isn't assigned to, so the invite could never be accepted.

Two details changed how I worked it:
- **"Pending" doesn't mean waiting on an email.** Under SSO, the first successful sign-in is what accepts the invite, and the email may never come.
- **The ticket subject misspelled her surname.** I copied the email from the IdP instead of the ticket and asked the app admin to confirm the invite matched it character for character.

## Resolution
1. Okta Admin → **Applications → Figma → Assignments → Assign to People** → the new hire (individual assignment).
2. Replied to the requester and **CC'd the new user** with exact sign-in steps: the Figma tile on the Okta dashboard, or **Log in with SSO**.
3. The app admin confirmed the invite was pending under the correct email.
4. The new hire signed in, and the invite flipped to active.

| Time | Event |
|---|---|
| +0:00 | Ticket opened and acknowledged |
| +1:04 | Okta assignment made |
| +1:21 | App admin confirmed the email matched |
| Same day | User signed in ✅ |

## Prevention / follow-up
- Wrote a runbook with a decision tree: user exists in the IdP? → app assigned? → invite email matches?
- Documented a provisioning hazard: if SCIM is on, **removing an individual assignment can deactivate the account**. Add the user to the group first, then convert or remove the individual assignment.
- Open items, kept honest: group-based vs. individual assignment norms, whether SCIM is enabled, and whether a paid seat needs budget approval.

## What I learned
Check for an IdP assignment before you spend time on any SSO-protected app ticket. The IdP is the source of truth.

📘 Runbook: [Figma access through SSO](../../runbooks/figma-access-requests.md)
