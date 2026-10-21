# Sanitization Policy

Every enterprise case study in this repo is based on real work. Before publishing, each one goes through the process below. I treat a public portfolio as a potential data-exposure surface and handle it the way I would any other.

## What is always removed or replaced

| Data type | Replaced with |
|---|---|
| Employer / client names | "the company", "a consumer company" |
| People's names, emails, usernames | `user@example.com`, `jdoe`, "an executive", "a user" |
| Hostnames and device names | `CORP-LAPTOP-01`, `SRV-APP-01` |
| Internal IP addresses and subnets | RFC 5737 documentation ranges: `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` |
| Domains | `example.com`, `corp.example.com` |
| Tenant / org / customer IDs | `<TENANT_ID>` |
| Serial numbers, asset tags, MAC addresses | `<SERIAL>`, `00:00:5E:00:53:xx` (RFC 7042 documentation range) |
| API keys, tokens, passwords, secrets | Removed entirely, never just masked |
| Ticket numbers, internal URLs | `INC-XXXX`, removed |
| Screenshots | Cropped or redacted; checked for names in tabs, headers, and address bars |

## Process
1. Write the case study from memory and the runbook entry, generalizing as I go.
2. Run [`tools/sanitize_check.py`](../tools/sanitize_check.py), which flags IPs, emails, non-example domains, secrets, and any term in a private denylist kept **outside** the repo.
3. Review every flag by hand. The scanner assists the review; it doesn't replace it.
4. Make sure no detail combination (timeline + vendor + user count) could identify the organization.
5. Commit.

## Why it matters
A security professional who leaks internal details in a portfolio has shown the opposite of the skill they're advertising.
