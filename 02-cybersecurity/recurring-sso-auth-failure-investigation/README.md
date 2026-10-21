# Investigating a recurring SSO lockout: pattern analysis across seven tickets

**Category:** Cybersecurity · Identity & Access
**Environment:** Okta (SSO, Okta Verify MFA, sign-on policies), 1Password (unlock with SSO), Slack, macOS
**Skills:** Authentication troubleshooting, log analysis planning, MFA/device-trust concepts, ticket-history analysis, hypothesis-driven investigation
**Status:** 🔍 Open. The investigation plan is built and a live repro session with the user is being arranged. Root cause not yet confirmed.
**Outcome so far:** Reframed one user's "ongoing issue" from a string of one-off fixes into a single root-cause investigation

---

## Situation
A senior employee reported being locked out of Slack on her laptop, though it still worked on her phone. Her password manager said *"Log in with Okta,"* and Okta said **"Unable to sign in."** She described it as an ongoing issue: "sometimes it is working and sometimes not."

## Why this ticket was different: the history
I pulled her ticket history before going further:

| When | Symptom | Outcome |
|---|---|---|
| Month 1 | Okta "Unable to sign in. Contact support" | Account looked active; **auto-closed** with no reply |
| Month 2 | After a laptop update: "User is not assigned to this application" | Resolved |
| Month 2 | Teams sign-in loop | Resolved |
| Month 5 | New phone; couldn't move the MFA app (old phone lost) | Factor reset |
| Month 5 | New phone; second authenticator app | Resolved |
| Month 7 | Password-manager unlock hangs at the SSO step | Logs "showed nothing weird"; **auto-closed** with no reply |
| Month 7 | **This ticket**: Okta denial; Slack locked on laptop | Open |

**The common thread:** the failures happen on the laptop, they're intermittent, and the IdP sits in the middle. Two prior tickets closed automatically after 48–72 hours in "Waiting on Customer" without the cause ever being found.

## How the pieces fit
- **The IdP is the front door.** When Okta denies a sign-in, every app behind it fails, which explains how the password manager, Slack, and other apps can all break at once.
- **The password manager unlocks through SSO.** If the IdP refuses her, the vault stays locked, and with it every other credential she has.
- **"Unable to sign in. Contact support" is Okta's generic *policy deny*, not a wrong password.** A sign-on or device-assurance rule (device, browser, OS version, network, MFA state) can pass on a phone and fail on a laptop, which matches "sometimes it works."
- **Account recovery in the password manager doesn't touch the IdP.** That's why the earlier recovery didn't fix it.

## Working hypothesis (two faults that look like one)
1. **Primary:** an IdP sign-on or device-assurance policy intermittently denies the laptop. One possibility is that Okta Verify on the Mac is still bound to the phone she lost in Month 5.
2. **Secondary:** the password manager's browser extension can't hand off to the desktop app (a frozen "trying to unlock" spinner), caused by a version mismatch, duplicate extensions, or browser integration being turned off.

## Investigation plan
**Before the session**
- [ ] Okta **System Log**, filtered to the user and failure dates, looking for `outcome = DENY/FAILURE`, and read the **reason** and the **matched policy rule**. Widen the time window, since an earlier check may have looked at the wrong one.
- [ ] User profile: status (Active/Locked?) and **authenticators**: which devices Okta Verify is enrolled on.
- [ ] Confirm which sign-on and device-assurance policies apply to her group.

**During the screen share**
- [ ] Reproduce live and **note the exact timestamp** to match it to the log entry.
- [ ] Record macOS version, browser, and password manager app and extension versions, and whether Okta Verify is on the Mac.
- [ ] Find out where Slack fails: at the IdP step or after it.
- [ ] Password manager: browser integration on, exactly one extension, both components updated.

## Follow-up
- The user asked for a short call, and I asked for her availability. Getting a live session keeps the ticket from auto-closing a third time without a root cause.

## Security considerations
- Resetting factors or loosening policy to get her in would be a quick fix that weakens controls. The goal is to find **which rule** denies her and fix the device or enrollment state so it passes legitimately.
- Repeated "unexplained" auth failures are also a signal worth ruling out (for example, sign-in attempts from elsewhere). The System Log review covers that.

_This case study will be updated with the confirmed root cause after the session._
