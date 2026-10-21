# Outlook (Windows & Mac): troubleshooting

How to fix Outlook when it misbehaves: copy/paste not working, freezing, features that stop
responding. Covers the desktop app on Windows and Mac, Outlook on the web, and the New Outlook.

**Related case study:** [Outlook copy/paste triage](../01-basic-it-support/outlook-copy-paste-triage/) (a restart fixed it)

## Glossary

- **Clipboard**: the temporary storage area where your computer keeps whatever you copied
  until you paste it. Windows and macOS each run one clipboard for the whole computer, and every
  app uses it.
- **Classic Outlook vs. New Outlook**: Microsoft is replacing the old Windows Outlook
  ("classic") with a "New Outlook" built on web technology. In the top-right corner of Outlook,
  a **New Outlook** toggle shows which one is running. New Outlook has more bugs and doesn't
  support classic add-ins.
- **Outlook on the web (OWA)**: Outlook in a browser at **outlook.office.com**. It's separate
  from the desktop app, which makes it a useful comparison test.
- **Add-in**: an extra built into Outlook, such as Grammarly, Zoom, Teams, or Adobe. Add-ins
  can intercept keystrokes and commands like copy/paste, and they're a very common cause of
  odd Outlook behavior.
- **Safe Mode**: starts Outlook with every add-in turned off. If the problem disappears in
  Safe Mode, an add-in is the cause.
- **Quick Repair / Online Repair**: Windows tools that fix a damaged Office install. Quick
  Repair runs offline in a few minutes. Online Repair reinstalls Office completely and takes
  longer.
- **Sensitivity label / "Do Not Forward"**: protection someone can apply to an email. It
  deliberately blocks copying, forwarding, or printing **that one email**.

## The one concept: first decide whether it's the computer or Outlook

Before you fix anything, ask **"Does it work in other apps (Word, a browser)?"**

- **Fails everywhere**: the problem is the computer (clipboard, keyboard, remote desktop).
  Outlook is just where she noticed it.
- **Fails only in Outlook**: the problem is Outlook (add-in, version, damaged install, or a
  protected email).

That one question cuts the list of suspects in half.

## Triage questions to send the user

Copy/paste these into Slack or the ticket:

> - Are you on a Mac or PC? Desktop Outlook, Outlook in the browser, or your phone?
> - Does it work in other apps, like Word or the web browser?
> - Does it fail in every email or only some?
> - Does right-click → Copy/Paste work, or only the keyboard shortcuts? Neither?
> - Have you restarted your computer since this started?

How to read the answers:

| Answer | Means | Rules out / points to |
| --- | --- | --- |
| Works in other apps | Clipboard and keyboard are fine | It's **Outlook** |
| Fails in other apps too | Computer-level problem | Restart, check keyboard, remote desktop clipboard |
| Only **some** emails | Those emails are probably protected | Sensitivity label / "Do Not Forward" (working as designed) |
| **Every** email | Outlook as a whole is broken | Not a protected email |
| Right-click works, keyboard doesn't | Shortcut being intercepted | Add-in grabbing keystrokes, or a stuck Ctrl key |
| **Neither** works | Outlook isn't running the command at all | Stuck process, add-in, damaged install |
| On a phone | Company security policy | Intune app protection blocks copying out of work apps |
| Hasn't restarted | Try that first | Fixes stuck clipboard/Outlook processes |

## Fix ladder: copy/paste not working in Outlook

Work through these **in order**. Stop as soon as one works, then write down which step fixed it
in the ticket note.

### 1. Restart the computer (fixed the last occurrence)

Not just Outlook, the **whole computer**. This clears a stuck clipboard and any frozen Outlook
background processes. It's the most common fix, so always try it first.

### 2. Check which Outlook they're on

Look for the **New Outlook** toggle in Outlook's top-right corner.

- **On**: switch it **off** to go back to classic Outlook, then test. New Outlook has known
  clipboard bugs.
- **Off / not there**: classic Outlook. Continue.

### 3. Compare with Outlook on the web

Have them try copy/paste at **outlook.office.com**.

- **Works on the web**: the desktop app is the problem. Continue to step 4.
- **Fails on the web too**: check browser extensions, or escalate.

### 4. Safe Mode (find a bad add-in)

**Windows:**

1. Close Outlook completely.
2. Press **Win+R**, type `outlook.exe /safe`, then **Enter**. Pick the default profile if it
   asks.
3. Test copy/paste.
   - **Works**: an add-in is the cause. Go to step 5.
   - **Still fails**: skip to step 6.

**Mac:** there's no Safe Mode. Go to **Get Add-ins → My add-ins** (or **… → Get Add-ins**) and
remove or disable add-ins, especially Grammarly or anything installed recently.

### 5. Find the bad add-in (Windows)

1. Open Outlook normally → **File → Options → Add-ins**.
2. At the bottom, set **Manage: COM Add-ins**, then **Go**.
3. Uncheck everything, restart Outlook, and test.
4. Turn add-ins back on **one at a time**, restarting Outlook each time, until it breaks again.
   The last one you turned on is the cause. Leave it off, or update or reinstall it.

### 6. Repair Office (Windows)

1. Close all Office apps.
2. **Settings → Apps → Installed apps → Microsoft 365 → ⋯ → Modify**.
3. **Quick Repair** first. If that doesn't fix it, **Online Repair** (longer, reinstalls
   Office, so warn the user first).

**Mac:** **Help → Check for Updates** (Microsoft AutoUpdate). If it's still broken, reinstall
Outlook.

### 7. Update Office

**Windows:** in Outlook, **File → Office Account → Update Options → Update Now**.

### 8. Still broken

Rebuild the Outlook profile (**TODO:** write up the profile-rebuild steps), or escalate to the IT manager.

## Don't

- **Don't skip the restart** because it seems too simple. It fixed the last occurrence.
- **Don't start with Online Repair.** It's slow and disruptive. Work up the ladder.
- **Don't "fix" a protected email.** If copy fails in only one or two emails, check for a
  sensitivity label first. That's the sender's protection doing its job.
- **Don't assume Mac or PC.** Ask. The steps are different.
