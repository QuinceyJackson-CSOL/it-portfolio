# Five questions that halve the problem: Outlook copy/paste failure

**Category:** Basic IT Support · Endpoint troubleshooting
**Environment:** Microsoft Outlook desktop, Windows
**Skills:** Structured triage, fault isolation, end-user communication, runbook writing
**Status:** ✅ Resolved in a single triage conversation
**Outcome:** Fixed without escalation, and built an ordered fix ladder for the next occurrence

---

## Situation
A user emailed the help desk: *"For some reason, I am not able to copy and paste in Outlook."* There was no platform and no detail.

## Investigation
I moved to chat for faster back-and-forth and sent a fixed set of triage questions. Each answer eliminates a class of causes:

| Question | Answer | What it ruled out |
|---|---|---|
| Does it work in other apps? | **Yes** | OS clipboard and keyboard, so the problem is **Outlook** |
| Every email or only some? | **Every** | A protected email (sensitivity label / Do Not Forward) |
| Right-click, keyboard, or neither? | **Neither** | A stuck key or intercepted shortcut, so Outlook isn't executing the command |
| Restarted since it started? | **No** | (Gives the cheapest fix to try first) |
| Mac or PC? | **Windows PC** | Picks the right fix path |

**The pivot question is "Does it work in other apps?"** It decides whether to troubleshoot the computer or the application.

## Resolution
**A full restart fixed it.** The most likely cause was a hung Outlook background process that had stopped passing copy/paste commands to the system clipboard. A restart clears all of those processes.

## Prevention / follow-up
If it recurs, a restart is only masking the problem, so I documented an ordered escalation ladder that goes from least to most disruptive:

1. Full restart
2. Check the **New Outlook** toggle (it has known clipboard bugs and doesn't support classic add-ins)
3. Compare with Outlook on the web
4. **Safe Mode**: `outlook.exe /safe` (all add-ins disabled)
5. Bisect the **COM add-ins**, re-enabling one at a time
6. Office **Quick Repair**, then **Online Repair** (warn the user first)
7. Update Office, then rebuild the profile or escalate

**Deliberate "don'ts":** don't open with Online Repair, don't skip the restart because it seems too simple, and don't "fix" a protected email, which is working as designed.

## What I learned
Ask **Mac or PC** up front, since the ticket didn't say. A short, standardized question set resolves tickets faster than open-ended back-and-forth.

📘 Runbook: [Outlook troubleshooting](../../runbooks/outlook-troubleshooting.md)
