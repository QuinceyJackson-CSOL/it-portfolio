# Microsoft 365 — Mailing lists (distribution lists & groups)

How to check and change who gets email sent to a shared address like all-staff@example.com.

## Glossary

- **MX record**: a public DNS entry that says which server receives a domain's email. To see
  it, run `dig +short MX example.com`. This company's points at `*.mail.protection.outlook.com`, which
  means **Microsoft 365 handles the company's email**.
- **Exchange Online**: Microsoft's email service, part of Microsoft 365.
- **Distribution list (DL)**: one email address that forwards to a list of people. It has no
  shared inbox or files; it just fans the message out. Most "mailing lists" are DLs.
- **Microsoft 365 Group**: a list that also comes with a shared inbox, calendar, and
  SharePoint/Teams space. Emailing it still reaches the members.
- **Mail-enabled security group**: a list that both receives mail and grants permissions.
  Less common.
- **Dynamic distribution group**: a list whose members are calculated automatically from a
  rule, such as "everyone in department = Sales". You can't add people to it by hand; you change
  their profile attributes instead.

## The one concept: email is not in Google here

This company uses Google Workspace for some things and has GAM set up, but **mail is in Microsoft 365**.
The Google side has no mailing lists (checked at time of writing: only 2 groups, neither a list). Any
email or mailing-list ticket goes to the Exchange admin center.

## 1. Checking someone's memberships

1. Go to **admin.exchange.microsoft.com**.
2. Open **Recipients → Groups**. You'll see tabs for **Microsoft 365**, **Distribution list**,
   **Mail-enabled security**, and **Dynamic distribution list**. Check every tab, because a
   list can be any of these types.
3. Click a list, then the **Members** tab, then search for the person's name.

Shortcut for "which lists is this person on": **admin.microsoft.com → Users → Active users →**
the person **→ Account tab → Groups → Manage groups**. **TODO:** confirm this shows DLs here.

## 2. Adding someone

1. Recipients → Groups → the list → **Members** → **View all and manage members**.
2. **Add members**, search for the person, select them, then **Add**.
3. Changes take effect within minutes. Exchange's address book (GAL) can lag up to a day, but
   mail delivery doesn't.

If there's no **Add** option, the list is either dynamic (see §4) or synced from another system
(see §3).

## 3. Before you edit: is this list managed somewhere else?

Okta is the source of truth for SaaS access here (see the Box runbook). If Okta pushes
groups into Microsoft 365, any change you make in Exchange will be **overwritten on the next
sync**. To check:

- In Okta, go to **Applications → Office 365 (or Microsoft 365) → Push Groups**. If the list's
  name appears there, add the person to the Okta group instead. **TODO:** check what's in
  there here.
- In Exchange, a synced group usually can't be edited and may show a message saying it's
  managed on-premises or by another source.

## 4. Dynamic lists

If a list is **dynamic**, a missing person usually means their profile is wrong (department,
office, or similar), not that the list is wrong. Fix the attribute, which may live in Okta or
HR rather than in Exchange. **TODO:** find out whether All Staff is dynamic.

## 5. "Add me to anything relevant"

No admin screen answers this directly. Find a teammate with the same job, look at their
memberships (§1), and offer the person the same lists. If a list belongs to another department
or looks restricted, ask its **owner** (shown on the list's settings page) before adding.

## 6. Permissions you need

**Exchange Recipient Administrator** (an Entra/Azure AD role) covers all of the above. You
don't need Global Admin. **TODO:** confirm which role you hold.

## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Person is on the list but gets no mail | Mail went to Junk/Other, or delivery restrictions | Check their Junk folder and the list's **Delivery management** settings |
| Can't add members | Dynamic list, or synced from Okta/on-prem | §3 / §4 |
| Your change disappeared later | Okta overwrote it | Make the change in Okta |
| Person can't send *to* the list | List only accepts mail from members, or only internal senders | List → **Settings → Delivery management** |

## Don't

- Don't look in Google/GAM for mailing lists. There aren't any there.
- Don't add people to another department's list without that list owner's OK.
- Don't edit a list in Exchange that Okta manages. The change won't stick.
