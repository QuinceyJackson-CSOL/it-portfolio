# Triage of a fake "virus detected" browser alert (scareware via push notifications)

**Category:** Cybersecurity · Endpoint / User-reported incident
**Environment:** Google Chrome on Windows, Microsoft Defender
**Skills:** Phishing/scareware analysis, severity triage, incident-escalation criteria, user education, documentation
**Status:** Assessed as low severity; remediation steps delivered; awaiting the user's confirmation that the pop-ups stopped
**Outcome:** Separated a nuisance from a potential compromise with five questions, and produced a reusable triage runbook

---

## Situation
A user reported a pop-up in the corner of her screen: **"⚠️ Virus caught in browser ⚠️ Run a PC scan immediately!"**, with a "Google Windows Defender" box and a red "TROJAN found" banner.

## Analysis
The alert was **scareware delivered through the browser's notification permission**, not a real detection.

| Indicator | Why it gives the alert away |
|---|---|
| Sender line showed a random subdomain on an unfamiliar domain | Real AV doesn't alert through a website's Chrome notifications |
| "Google Windows Defender" | Not a real product, since it mashes up two vendors |
| Urgency, red banners, ⚠️ | Pressure to click before thinking |

**Likely initial access:** the user clicked **Allow** on a "Show notifications?" prompt at some point, which gave the site persistent permission to push alerts, even when the site wasn't open.

**Key insight:** the danger isn't the pop-up. It's the click it's trying to get, which leads to fake AV, a fake support number, or a real malware download.

## Severity triage
Along with the fix steps, I asked:
1. Did you click the pop-up? What opened?
2. Did you download or install anything?
3. Did you enter a password or payment details?
4. Did you call a number or allow remote access?
5. Which device and browser?

| Answers | Severity | Response |
|---|---|---|
| All "no" | Low | Remove the permission, check extensions, run a local scan |
| Any "yes" | **Security incident** | Escalate; reset password and MFA if credentials were entered; scan or reimage; isolate from the network if a remote-access tool was installed |

The user confirmed she **didn't click**, so the case was classified as low severity with no escalation.

## Remediation steps
_My reply to the user covered removing the site and running a Defender scan. The rest comes from the runbook checklist._

1. Close the pop-up with the **X**, not the alert body.
2. `chrome://settings/content/notifications` → remove the offending site and anything unfamiliar.
3. Review **Extensions** and remove anything not installed on purpose.
4. Chrome **Safety Check**.
5. **Windows Security → Quick scan** (the real Defender).
6. Confirm the alerts stopped, then resolve.

**Deliberately avoided:** resetting or reinstalling the browser first, which is overkill when one permission is the cause, and dismissing it as "just spam" without asking the triage questions.

## Prevention
User guidance: click **Block** on any "Show notifications?" prompt unless it's a work tool you actively use.

**Recommended next control (not yet implemented):** manage Chrome by policy to default-block site notifications and allowlist work tools (`DefaultNotificationsSetting` plus an allowlist), so the fix doesn't depend on each user.

## Open items
- Confirm the company's formal security-incident process and the EDR in use, so the "any yes" path has a named owner.

📘 Runbook: [Browser scam notifications](../../runbooks/browser-scam-notifications.md)
