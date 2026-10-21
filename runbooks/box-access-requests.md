# Runbook: Box folder access

**The ticket this solves:** "Please give me access to folder X."

> **Trainer's note:** Read §1–§4 to work a ticket. §5 is for when you're blocked.
> Anything marked **TODO** is a company detail nobody has confirmed yet — confirm it, then
> delete the TODO.

---

## 1. Words you need first

| Word | Plain meaning |
| --- | --- |
| **Collaborator** | A person added to one specific folder. |
| **Collaboration** | The link between a person and a folder. "Add a collaboration" = "give access." |
| **Collaboration role** | How much they can do *in that one folder* (Viewer, Editor…). |
| **Enterprise role** | What they can do *across the whole company account* (User, Co-Admin, Admin). |
| **Admin Console** | The admin-only control panel at box.com. Plain users don't have it. |
| **Inherit** | Access flows down from a folder to its subfolders — unless a subfolder overrides it. |

## 2. The one concept that explains everything

Box has **two separate permission systems.** They are not connected. Mixing them up is the #1
source of confusion.

```
┌─ SYSTEM 1: COLLABORATION ROLE ─────┐   ┌─ SYSTEM 2: ENTERPRISE ROLE ────────┐
│ Scope:  ONE folder                 │   │ Scope:  THE WHOLE COMPANY          │
│ Values: Previewer → Viewer →       │   │ Values: User → Co-Admin →          │
│         Editor → Co-owner → Owner  │   │         Primary Admin              │
│ Set by: that folder's owner        │   │ Set by: the Primary Admin ONLY     │
│ Where:  the Share button           │   │ Where:  Admin Console              │
│ Use it: to give a user access      │   │ Use it: to give YOURSELF the       │
│                                    │   │         power to do that           │
└────────────────────────────────────┘   └────────────────────────────────────┘
```

**A plain user sees only folders they own or collaborate on.** So an empty Files list and empty
search results are *normal* for a new account — not a bug, and not proof a folder is missing.

## 3. Decision tree — start here

```
Ticket: "give me access to folder X"
│
├─ Can YOU see folder X in your own Box Files list?
│  │
│  ├─ YES → is there a Share button (not greyed out)?
│  │        ├─ YES → §4, Way A. Done.
│  │        └─ NO  → you're only a Viewer. Ask the owner for Co-owner. → §5
│  │
│  └─ NO  → can you identify the folder's OWNER?
│           ├─ YES → ask them to add the person. No admin rights needed. ✅
│           └─ NO  → have the requester click "Request Access" in Box —
│                    it emails the real owner. → §5
│                    Still stuck? Do you have "Admin Console" in the left nav?
│                    ├─ YES → §4, Way B.
│                    └─ NO  → blocked on admin rights. → §5
│
└─ Before you click anything, always: check the attachment, confirm
   the requester's department, confirm approval. → §4, step 0.
```

## 4. Working the ticket

### Step 0 — Before you touch anything

1. **Open the attachment.** People screenshot their folder tree. It tells you the exact folder.
2. **Check the requester's department.** In-department = routine. Out-of-department = an
   approval question, not a task.
3. **Get approval if needed.** The folder *owner* decides who gets in, not IT. Own department
   and clearly job-related → go ahead. Another department, or sensitive (finance, HR, legal,
   unreleased product) → get the owner's written OK **in the ticket**. That thread is your
   audit trail.
4. **Pick the lowest role that does the job** (table below). Upgrading later is one click.
   Taking access back is an awkward conversation and maybe a cleanup job.

**TODO:** confirm the company's approval policy and who owns each top-level folder.

### Step 1 — Grant it

**Way A — you can see the folder**

1. box.com → click the folder
2. **Share** → **Invite People**
3. Type their work email
4. Pick the role
5. Message: the ticket number → **Send**

**Way B — you can't see the folder (needs Co-Admin)**

1. **Admin Console** → **Content Manager**
   *(or Users & Groups → the folder's owner → Show Details)*
2. Navigate to the folder
3. Manage its collaborators from there

**Way C — groups — ❌ NOT AVAILABLE IN THIS ENVIRONMENT**

Normally the best option: add the person to a group that's already collaborated onto the folder,
so access reviews and offboarding have one place to look.

**Verified at time of writing: this environment doesn't use it.** Okta → Box → Push Groups is empty, so no Okta
group reaches Box. Every folder permission here is an individual collaboration. Kept in the
runbook because it's the right pattern to advocate for, and in case it's set up later.

### Step 2 — Verify, then close

Never close on "I clicked the button."

- [ ] Collaboration shows the right person at the right role
- [ ] Status is **Accepted** or **Pending** (Pending is fine — they haven't clicked the email yet)
- [ ] **The requester confirms they can open it.** Their confirmation closes the ticket.

### Collaboration roles, least → most access

| Role | Can do |
| --- | --- |
| Previewer | Look, in preview only. No download. |
| Uploader | Put files in. Can't see what's already there. |
| Previewer Uploader | Preview + upload |
| **Viewer** | **View + download. ← start here for read-only requests** |
| Viewer Uploader | View + download + upload |
| **Editor** | **+ edit, delete, and invite others. ← use if they'll contribute files** |
| Co-owner | + manage collaborators and folder settings |
| Owner | Full control. One per folder. |

⚠️ **Editor and above can invite other people.** Granting Editor hands part of your access
control to them.

## 5. When you're blocked

### First: check whether you already have access and don't know it

⚠️ **Do this before anything else, including before asking for admin rights.**

**A collaboration you haven't accepted is invisible.** When someone adds you to a folder, Box
emails you an invitation. Until you accept it, the collaboration status is **Pending** and the
folder does **not** appear in your Files list — and the Claude connector can't see it either.
An empty Files list looks identical to having no access at all.

So if someone tells you they've granted you access and you can't see it:

1. **Click the envelope icon** at the top right of box.com, left of your avatar. That's the
   notifications/invites inbox. Accept anything waiting there.
2. **Check your work email** for "invited you to collaborate" messages from Box.
3. **Click the chevron next to the "Files" heading** and confirm you're on **All Files**, not a
   filtered view.
4. Reload, then re-check.

This is the same #1 cause listed in §6 for when a *requester* says they still can't see a
folder. It applies to you too — remember to run your own troubleshooting on yourself.

If the folder appears but **Share is greyed out**, you were given Viewer. Viewers can't invite.
Ask for **Co-owner** on that folder — a small, easy-to-approve request.

### Second: ask whether you need admin rights at all

**The folder's owner can add collaborators themselves.** Admin access is the shortcut for when
the owner is unknown or unreachable — it is not the default path. Before escalating, try:

1. **Have the requester click "Request Access."** When a Box user clicks a folder they can't
   open, Box offers a **Request Access** prompt that emails the real owner directly. Free, no
   admin rights, identifies the true owner, and often just resolves the ticket. **Try this first.**
2. **Ask the likely owner directly.** Usually the department's VP or director. A Slack profile
   title is a good first guess — but it's a *guess* until Box confirms ownership.
3. **Check the requester's own job title.** It often answers the approval question outright:
   in-department and job-related needs no sign-off. Cross-department does.

Only if the owner is unknown, unreachable, or slow does this become an admin-rights problem.

### 🔑 This company provisions Box through OKTA — check there first

**This is the company-specific fact that overrides the generic Box advice below.** Box access here
is managed in Okta, not (only) in the Box Admin Console.

**❌ Group Push is NOT in use here.** Verified at time of writing: Applications → Box →
**Push Groups** is empty ("No groups found for this filter"). No Okta group pushes into Box.

That means **Way C (groups) is not available here.** Every Box folder permission here is an
individual, hand-managed collaboration. Re-check this tab occasionally in case it changes.

📷 **TODO** `images/okta-box-push-groups-empty.png`

**What Okta *is* used for with Box:** provisioning accounts (the Box licensing group, nearly every
employee) and pushing the per-user **Box role** attribute — see below.

**Set a Box role from Okta — the expected path here (not yet tested):**

1. Applications → **Box** → **Provisioning** → **To App** → confirm **Push Profile Updates**
   is enabled. If it's off, nothing set in Okta reaches Box.
2. Applications → **Box** → **Assignments** → search the person → **pencil** (edit)
3. Set the Box **Role** attribute (values like *User* / *Coadmin*) → **Save**
4. Sign fully out of box.com and back in — **Admin Console** appears in the left nav

Tip: open another user's assignment with the pencil first, just to see which attributes exist
and their exact values, before editing anyone's.

**Log any role elevation in the ticket** — what was set, when, and who approved it. Okta records
the change in its system log regardless; your note is what explains it to whoever reviews it.

⚠️ **Okta is the source of truth.** Manual changes made directly in Box get overwritten on the
next sync. Don't "fix" a role in Box if it's provisioned from Okta — fix it in Okta.

**Confirmed company detail:** the Okta group named after the app is the *licensing* group: nearly
every employee is in it. It controls **who gets a Box account at all**, not who can open
which folder. Don't look for folder access there.

🚫 **Two things never to click in Okta:**
- Directory → Groups → the Box licensing group → Actions → **"Remove all people from this group"** —
  deprovisions Box for the entire company.
- Applications → Box → Assignments → the **✕** beside a person — unassigns Box from that user.
  The pencil (edit) is right next to it. Read before you click.

**Okta admin access looks like nothing from inside Box.** If someone grants you rights and Box
appears unchanged, check whether they gave you *Okta* admin rather than Box co-admin. Confirm
your own role at Security → **Administrators**.

**TODO:** confirm which Okta admin role is needed to edit app assignments vs. group membership.

📷 `images/okta-box-users-group.png` — the license group, for contrast with a real access group.

### About self-elevation: it depends where the role lives

- **Inside Box's own Admin Console:** you cannot change your own enterprise role. A Co-Admin
  can't edit their own permissions or the Primary Admin's. Only the Primary Admin can.
- **Via Okta provisioning:** the role is pushed *into* Box from Okta, so Box's self-edit
  restriction doesn't apply. Whoever can edit the Box app assignment in Okta can set a Box
  role — including their own.

Here, assume the Okta path. Don't repeat the mistake of insisting it's impossible: ask
**where the role is administered** before concluding anything.

### Ask for named permissions, not "admin"

Co-Admin isn't one switch — it's a checklist. Ask for specific boxes.

| Permission | What it gets you | Need it? |
| --- | --- | --- |
| **View and edit users' content** | Reach *any* user's folders and manage collaborators | **YES — this is what unblocks folder tickets** |
| View users' content | Read-only version of the above | No — can't add a collaborator with it |
| Manage users | Create/edit/deactivate users, reset 2FA | For onboarding tickets |
| Manage groups | Required for Way C above | If we use groups |
| Run reports / view activity | Audit logs | For investigations |
| Enterprise settings, apps, retention, legal holds, Box Sign, Shield | — | No. Each one widens the damage if your account is compromised. |

**Standard ask:** Co-Admin with *Manage users*, *Manage groups*, and *View and edit users' content*.

⚠️ *View and edit users' content* is effectively read/write on **every file the company owns.**
Expect questions. That's appropriate, not distrust.

### Always offer the smaller option too

Company-wide file access is a big hammer for "add one person to two folders." The narrow fix:
ask the folder **owner** to make you **Co-owner** on the relevant top-level folders. Handles
this whole ticket type without enterprise-wide access. Offering it unprompted gets you a
faster yes.

### The clicks — send these to the Primary Admin

1. Admin Console → **Users & Groups**
2. Click the user
3. **Access Permissions** → change *User* → *Co-Admin*
4. Tick the specific permissions
5. **Save**

### Did it work? Check the web UI, not the connector

1. **Sign fully out of box.com and back in.** Not a refresh. A role change never shows in an
   old session — this is the most common reason a correct change looks broken. Also allow a
   few minutes to propagate.
2. Look at the left nav.

```
PLAIN USER (blocked)          CO-ADMIN (good to go)
├ Files                       ├ Files
├ Notes                       ├ Notes
├ Automate                    ├ Automate
├ Integrations                ├ Integrations
├ More                        ├ More
├ Collections                 ├ Collections
└ Favorites                   ├ Favorites
                              └ ADMIN CONSOLE   ← the thing you're looking for
```

Profile menu (top-right avatar) tells you the same thing: a plain user's menu stops at Account
Settings / Integrations / Collaborators / Download Box Drive / Help / Log Out. An admin sees
admin and enterprise entries there too.

📷 `images/box-plain-user-nav.png` — what a blocked plain-user account looks like.
📷 **TODO** `images/box-coadmin-nav.png` — capture this once you have Admin Console.

🚫 **Do not use the Claude Box connector as your test.** A Co-Admin's content access works
through the Admin Console and admin-scoped API calls — *not* through the connector's ordinary
user token. So `who_am_i` and folder searches can look **completely unchanged after a
successful elevation.** The connector can confirm a role when it reports `coadmin`, but its
silence proves nothing.

### If it didn't work, report observations — not "it didn't work"

Include:
- Which nav entries are missing
- Whether your Files list is empty
- **Your Box user ID** — so they can confirm they edited the right record

Also know: **no setting on anyone's laptop can grant a Box role or collaboration.** Those live
server-side on the Box account. If someone says they "changed a setting on my computer," that
almost certainly wasn't it.

### Log the elevation in the ticket

Who approved it, when, and exactly which permissions. Self-service admin elevation is a
standard audit question, and a dated ticket line beats a Slack message nobody can find.
Box also logs every admin content access where the Primary Admin can read it — use the
permission for the ticket in front of you and nothing else.

## 6. Troubleshooting

| Symptom | What's actually wrong | Fix |
| --- | --- | --- |
| **"I see the folder but can't open it"** — most common version of this ticket | They collaborate on the *parent*. The subfolder overrides inheritance with its own list, and they're not on it. Not a bug. | Add them to **the subfolder itself**. ⚠️ Don't widen their role on the parent — that grants far more than they asked for. |
| Your search finds nothing for a folder you know exists | Box search only covers content *you* can access | Use the Admin Console. Empty ≠ missing. |
| "Still can't see it" after you granted | Usually: invite not accepted (status Pending) | Or: signed into a personal vs. a company account; or browser cache — sign out and in |
| "This user is outside your enterprise" | Email doesn't match a company Box account | Typo, or they're not provisioned in Box yet. External sharing may also be blocked by policy. |
| Share button greyed out | You're a Viewer/Previewer — those can't invite | Get Editor or above, or use the Admin Console |
| Nothing in your Files list at all | Normal for a new account with no collaborations | Not a problem to fix |

## 7. The Claude connector: what it can and can't do

| Can | Can't |
| --- | --- |
| Look up folder IDs | **Add or remove a collaborator — no tool exists** |
| Check who has access (`list_item_collaborations`) | See content you don't have access to |
| Search, list, move, copy | Act as an admin |
| Confirm a grant landed | Prove a grant *didn't* land |

It runs as **your own user**, never as an admin. So **every access grant is a manual click in
Box.** Use the connector to look things up and to verify afterward.

## 8. Offboarding / access removal

The mirror image of this runbook. When someone leaves or changes teams, remove their
collaborations too — and their group memberships (Way C is why groups are worth it).

**TODO:** document the company's offboarding checklist and where Box sits in it.
