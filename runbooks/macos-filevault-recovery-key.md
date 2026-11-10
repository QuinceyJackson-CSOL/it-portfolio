# Runbook: Mac locked out, asking for a FileVault recovery key

**The ticket this solves:** "I reset my password and now I'm locked out of my laptop. It's asking
for a recovery key and I don't know what that is."

> **Trainer's note:** Read §1–§4 to work a ticket. §5 is the security checklist; don't skip it.
> This one came out of a real ticket that was resolved the same afternoon in about a 15-minute call.

**Related case study:** [FileVault lockout recovery](../01-basic-it-support/macos-filevault-lockout-recovery/)

---

## 1. Words you need first

| Word | Plain meaning |
| --- | --- |
| **FileVault** | Apple's full-disk encryption. Everything on the Mac is scrambled until someone unlocks it with the Mac password or the recovery key. |
| **Recovery key** | A long backup code that can unlock the disk when the password doesn't work. Think of it as the master key kept in the office safe. |
| **Escrow** | The MDM keeps a copy of each Mac's recovery key so IT can help when a user is locked out. The user never has to save it. |
| **MDM (Kandji)** | The tool IT uses to manage company Macs. It's where the escrowed recovery key lives. |
| **Recovery Assistant** | The Mac screen that appears after a password reset or failed login, offering "Reset Password" and asking for the recovery key. |
| **Identity provider password (Okta/email)** | A different password from the laptop password. Resetting one does not change the other. |

## 2. The one concept that explains everything

**The recovery key is a master key. Whoever holds it can open the laptop and everything on it.**
So the job isn't just "give them the key." It's **prove who they are, prove it's the right Mac,
then hand over the key in a way that leaves no copy behind.**

```
 Is it really them?  ──►  Is it really their Mac?  ──►  Key read out loud, live  ──►  New password set
 (camera on, video)       (serial on the laptop          (never typed into chat,       (user picks it;
                           matches the MDM record)        email or the ticket)           IT never sees it)
```

## 3. First reply to the user (send right away)

Ask them to **stop trying passwords or keys**. Repeated failed tries make the recovery harder.
Then ask three questions:

1. **Mac or Windows?**
2. **A photo of the screen** that's asking for the recovery key.
3. **Which password did you reset:** the laptop password, or the Okta/email password?

> If the ticket portal is giving the user trouble, it's fine to collect these answers in a direct
> chat message. Copy the facts back into the ticket so the record is complete.

## 4. Steps

1. **Find the Mac in the MDM.** Kandji → Devices → search the user → open the device →
   FileVault. Confirm:
   - FileVault is **on**.
   - A **personal recovery key is escrowed** (on file).
   - It's the **only device** that matches this user. If there are two, use the serial number to pick.
2. **Tell the user you have the key, and that you'll give it on a video call.** Say why, in one
   line: *"For security, we never send recovery keys by email or chat."*
3. **Start the video call safely:** waiting room **on**, recording **off**, transcription/AI notes **off**.
4. **Verify identity:** camera on. Confirm it's the person on the ticket.
5. **Verify the device:** ask them to read the **serial number printed on the bottom of the Mac**.
   It must match the serial in the MDM record. If it doesn't, stop and escalate.
6. **Ask them not to type anything** until you're both looking at the recovery screen.
7. **Read the recovery key out loud**, a few characters at a time, while they type it.
8. When it's accepted: they pick **their own account** and set a **new laptop password**.
   IT never hears or sees the new password.
9. Watch for a **keychain prompt** ("update your keychain password"). If one appears, walk them through it.
10. **Leave the Mac online** for a while so it checks in with the MDM and a **fresh recovery key is
    escrowed**. The old key has now been seen, so it shouldn't be the one on file forever.
11. **Write the ticket note** (see §6) and resolve.

## 5. Security checklist (all must be true)

- [ ] Identity verified on live video
- [ ] Serial number on the laptop matched the MDM record
- [ ] Key was spoken only, never typed into chat, email, the ticket, or a screenshot
- [ ] Call was not recorded or transcribed
- [ ] User set their own new password
- [ ] Mac checked back in with the MDM so a new key is escrowed

## 6. Ticket note template

```
Issue: Locked out after a laptop-password reset; Recovery Assistant asked for the FileVault key.
Checked: Mac / laptop password reset / Okta password unchanged.
MDM: FileVault on, personal key escrowed, one matching device.
Call: waiting room on, no recording, no transcription. Identity verified on video.
Serial on device matched MDM record. Key read verbally; not recorded anywhere.
Result: Key accepted, user set a new laptop password, logged in and working.
Follow-up: Mac left online to escrow a fresh recovery key.
```

## 7. What NOT to do

- **Don't** paste the recovery key into chat, email, the ticket, or a text "just this once."
- **Don't** give the key to someone who can't show the device's serial number.
- **Don't** reset their Okta/email password unless that's actually the problem. It's a different lock.
- **Don't** let them keep guessing passwords while you look things up.

## 8. Why it matters (the identity angle)

This is **device trust + identity proofing**. The MDM proves the device is ours; the video call
proves the person is who they say; the verbal handoff keeps a powerful secret from being copied.
Same pattern as an account recovery or MFA reset: verify, then grant, then rotate.
