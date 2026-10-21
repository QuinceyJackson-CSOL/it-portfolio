# mail-provider-check: "Which console do I open?" for email tickets

**Category:** Automation & Scripting · Networking
**Tech:** Python 3 (standard library only), `dig`, DNS MX/SPF, `unittest`
**Status:** Working; 5 offline unit tests, run in CI

## Why I built it
On a mailing-list ticket I lost time searching the wrong admin console, because the company used Google Workspace for apps and Microsoft 365 for mail ([case study](../../04-networking/email-routing-dns-mx-diagnosis/)). The MX record answers that in seconds, so I turned the check into a tool.

## What it does
- Resolves **MX** and **SPF** for one or more domains
- Maps them to known platforms: Microsoft 365, Google Workspace, Proofpoint, Mimecast, Barracuda, and others
- Detects a **secure email gateway** in front of the mailbox and uses SPF to infer the mailbox platform behind it
- Flags **email-security risks**: missing SPF, or SPF ending in `+all` (anyone can spoof the domain)
- `--json` output for scripting or feeding into reports

## Usage
```bash
python3 mail_provider_check.py example.com
python3 mail_provider_check.py --json example.com example.org
```

Example output (illustrative):
```
example.com
  Mail is handled by: Microsoft 365 (Exchange Online)
    MX   0  example-com.mail.protection.outlook.com  [Microsoft 365 (Exchange Online)]
  SPF: v=spf1 include:spf.protection.outlook.com -all
    authorized sender: spf.protection.outlook.com  [Microsoft 365]
```

## Tests
```bash
python3 -m unittest -v test_mail_provider_check
```
The tests run against captured `dig +short` output, so they're deterministic and need no network.

## Ideas for v2
- DKIM selector and **DMARC** policy checks (`_dmarc.<domain>`) for a fuller email-security posture report
- CSV input to audit many domains at once (for example, during vendor onboarding)
