# Locked out after a password reset: recovering a FileVault-encrypted Mac without leaking the key

**Category:** Basic IT Support · Identity & Access · Endpoint
**Environment:** macOS (FileVault), Kandji MDM, Okta, ITSM ticketing, Slack, Zoom
**Skills:** Identity proofing, device verification, MDM key escrow, secure secret handling, user communication
**Status:** ✅ Resolved the same afternoon. About 2 hours 40 minutes from ticket to back at work; the recovery itself took a ~15-minute call
**Outcome:** User back in with a new password she chose; the recovery key was never written down anywhere; produced a reusable [runbook](../../runbooks/macos-filevault-recovery-key.md)

---

## Situation
An employee reset her laptop password and then couldn't log in at all. The Mac's Recovery
Assistant was asking for a **recovery key** for the disk, and she didn't know what that was.
She also had trouble replying through the ticket portal, so the conversation moved to chat.

## Investigation
My first reply asked her to **stop trying passwords**, because repeated failures make recovery
harder, and to answer three questions:

| Question | Her answer | Why it mattered |
|---|---|---|
| Mac or Windows? | Mac | FileVault, not BitLocker |
| Which password did you reset? | The laptop password | Her Okta/email password was unchanged, so this wasn't an identity-provider problem |
| Photo of the screen? | Sent | Confirmed the prompt was the FileVault recovery key for the startup disk |

Then I checked the MDM:
- FileVault **on**
- A **personal recovery key escrowed** (IT had a copy on file)
- **Only one device** matched her, so there was no risk of reading out the wrong key

The fix was clear. The real question was **how to hand over a master key safely.**

## Resolution
A recovery key unlocks everything on the disk, so I treated the handoff like an account recovery:
**prove the person, prove the device, then hand over the secret without leaving a copy.**

1. Told her we had the key and that I'd give it on a video call: *"For security, we never send recovery keys by email or chat."*
2. Started the call with the **waiting room on**, **no recording**, **no transcription**.
3. **Verified her identity** on camera.
4. Had her read the **serial number on the bottom of the laptop**. It matched the MDM record.
5. **Read the recovery key out loud** while she typed it. It was never pasted into chat, email or the ticket.
6. Key accepted. She chose her own account and **set a new laptop password herself**. No keychain prompt appeared.
7. Left the Mac **online so it could check in with the MDM and escrow a fresh key**, since the old one had now been seen.

| Time | Event |
|---|---|
| +0:00 | Ticket opened |
| +0:50 | First reply: stop retrying, three triage questions |
| +1:13 | Answers and screen photos received over chat |
| +2:14 | Key confirmed on file; video-call plan sent |
| +2:25 | Call started; identity and serial verified |
| +2:39 | User logged in with a new password; ticket resolved ✅ |

## Prevention / Follow-up
- Wrote the [FileVault recovery-key runbook](../../runbooks/macos-filevault-recovery-key.md) with a six-item security checklist and a ticket-note template, so anyone on the team handles it the same way.
- The ticket note records **that** the key was issued and when, but **never the key itself**.

## What I learned
The technical fix took minutes. The part that mattered was the process around it: the key is the
most sensitive thing on that laptop, so who receives it, how, and what record is left behind matter more than the clicks.

## Security considerations
- **Identity proofing:** live video plus a physical serial number. Something she is, and something only the person holding the laptop can read.
- **No secret at rest:** spoken only. Not in chat, email, the ticket, a screenshot or a call recording.
- **Rotation:** the Mac re-escrows a new key after check-in, so the disclosed key doesn't stay valid on file.
- **Least change:** her Okta/email password was left alone because it wasn't the problem.
