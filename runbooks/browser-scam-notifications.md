# Browser "virus" pop-ups / scam notifications (Chrome, Edge, Windows & Mac)

How to handle "Virus caught in browser!", "Your PC is infected", "Run a scan now" pop-ups
that appear in the corner of the screen. These are almost always **fake alerts sent through
the browser's notification feature**. They are not a real infection.

**Related case study:** [Scareware notification triage](../02-cybersecurity/scareware-browser-notification-triage/)

## Glossary

- **Browser notification (push notification)**: a website can ask "Allow notifications?".
  If you click **Allow**, that site can make pop-ups appear in the corner of the screen, even
  when the site isn't open. This is a legitimate feature (Slack and Gmail use it), and scammers
  abuse it.
- **Scareware**: fake security warnings designed to frighten you into clicking. The click goes
  to a page selling fake antivirus, asking you to call a fake "support" number, or pushing a
  download that really is malware.
- **Microsoft Defender**: the real antivirus built into Windows. It shows its warnings in the
  **Windows Security** app, never as a Chrome pop-up from a random website.
- **Extension**: an add-on installed inside the browser. A bad extension can also cause
  pop-ups and redirects, so check extensions too.

## The one concept: the pop-up is the website, not the computer

Look at the **top line** of the pop-up. It shows the website that sent it, e.g.
`<random-subdomain>.<scam-domain>.com`. A random-looking web address means a website was given
permission to send notifications, usually by an accidental **Allow** click on some page.

The fix is to **take that permission away**. You don't need to "remove a virus". The pop-up is
trying to get the user to click something, and that click is the actual danger.

How to spot that it's fake:

| Clue | Why it gives it away |
| --- | --- |
| Sent from a random web address | Real antivirus doesn't send warnings through Chrome |
| Mixed-up brand names ("Google Windows Defender") | No such product exists. Google and Microsoft are different companies |
| Urgency ("immediately!", red banners, ⚠️) | Pressure tactic so you click before you think |

## Triage questions (ask first, these decide how serious it is)

1. **Did you click the pop-up?** If yes: did a page open, what did it ask for?
2. **Did you download or install anything** it offered?
3. **Did you type a password or payment details** into anything it opened?
4. **Did you call a phone number** or let anyone connect to your computer remotely?
5. **Mac or PC, and which browser?**

- **All "no"** (she only saw it): **low severity**. Follow the fix below.
- **Any "yes"**: **treat it as a security incident.** Escalate to the IT manager right away. Reset the user's
  password (and Okta MFA if credentials were entered), have the device scanned or reimaged,
  and if a remote-access tool was installed, take the device off the network. **TODO**: confirm
  the company's security-incident process and which endpoint protection (EDR) we use.

## Fix: Chrome (Windows or Mac)

1. **Don't click the pop-up itself.** Close it with the **X**.
2. Open Chrome → click **⋮** (top right) → **Settings**.
3. Left side: **Privacy and security** → **Site settings** → **Notifications**.
   (Shortcut: paste `chrome://settings/content/notifications` into the address bar.)
4. Under **Allowed to send notifications**, find the bad site (`the scam domain` or
   anything else unfamiliar) → click **⋮** next to it → **Remove** (or **Block**).
   Remove anything else you don't recognize too. Keep familiar sites like Slack or Gmail.
5. Check extensions: **⋮** → **Extensions** → **Manage Extensions**. Remove anything the user
   doesn't recognize or didn't install on purpose.
6. Run Chrome's own check: **Settings** → **Privacy and security** → **Safety Check**
   → **Check now**.
7. **Windows only:** open **Windows Security** → **Virus & threat protection** →
   **Quick scan**. This is the real Defender. (Mac: **TODO** confirm what company Macs run.)
8. Confirm with the user that the pop-ups have stopped.

## Fix: Microsoft Edge

Same idea: **⋯** → **Settings** → **Cookies and site permissions** → **Notifications** →
remove the site under **Allow**. Extensions are at `edge://extensions`.

## What NOT to do

- **Don't** click "Scan", "Fix", or "Call support" in the pop-up, even to "see what it is".
- **Don't** install any "cleaner" or antivirus the page recommends.
- **Don't** reset or reinstall Chrome first. It's overkill when removing one permission fixes it.
- **Don't** dismiss it as "just spam" without asking the triage questions. If they clicked
  and entered a password, it's a real incident.

## Prevention tip for users

When any website asks **"Show notifications?"**, click **Block** unless it's a work tool you
actually use. A legitimate site works fine without notifications.
