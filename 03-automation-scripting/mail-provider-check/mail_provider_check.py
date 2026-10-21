#!/usr/bin/env python3
"""
mail_provider_check.py: identify which platform handles a domain's email.

Answers the first question on any email ticket: "Which admin console do I
open?" It reads the domain's MX and SPF records and maps them to known
providers (Microsoft 365, Google Workspace, Proofpoint, Mimecast, ...).

Usage:
    python3 mail_provider_check.py example.com [more.example ...]
    python3 mail_provider_check.py --json example.com

Requires `dig` (preinstalled on macOS and most Linux distros). Standard
library only.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys

# Substring of an MX host or SPF include -> provider name
MX_SIGNATURES = {
    "mail.protection.outlook.com": "Microsoft 365 (Exchange Online)",
    "aspmx.l.google.com": "Google Workspace",
    "googlemail.com": "Google Workspace",
    "smtp.google.com": "Google Workspace",
    "pphosted.com": "Proofpoint (secure email gateway)",
    "ppe-hosted.com": "Proofpoint Essentials (secure email gateway)",
    "mimecast.com": "Mimecast (secure email gateway)",
    "barracudanetworks.com": "Barracuda (secure email gateway)",
    "messagelabs.com": "Broadcom/Symantec Email Security",
    "zoho.com": "Zoho Mail",
    "secureserver.net": "GoDaddy / Microsoft 365 via GoDaddy",
    "icloud.com": "iCloud Mail",
}
SPF_SIGNATURES = {
    "spf.protection.outlook.com": "Microsoft 365",
    "_spf.google.com": "Google Workspace",
    "pphosted.com": "Proofpoint",
    "mimecast.com": "Mimecast",
    "sendgrid.net": "SendGrid (bulk/transactional sender)",
    "mailgun.org": "Mailgun (bulk/transactional sender)",
    "amazonses.com": "Amazon SES (bulk/transactional sender)",
    "servers.mcsv.net": "Mailchimp (marketing sender)",
}


def dig(name: str, rtype: str) -> list[str]:
    if not shutil.which("dig"):
        sys.exit("error: `dig` not found. Install bind-utils/dnsutils, or run this on macOS.")
    out = subprocess.run(["dig", "+short", rtype, name], capture_output=True, text=True, timeout=15)
    return [ln.strip() for ln in out.stdout.splitlines() if ln.strip() and not ln.startswith(";")]


def parse_mx(lines: list[str]) -> list[tuple[int, str]]:
    records = []
    for ln in lines:
        parts = ln.split()
        if len(parts) == 2 and parts[0].isdigit():
            records.append((int(parts[0]), parts[1].rstrip(".").lower()))
    return sorted(records)


def parse_spf(lines: list[str]) -> str | None:
    for ln in lines:
        txt = "".join(seg.strip('"') for seg in ln.split('" "')).strip('"')
        if txt.lower().startswith("v=spf1"):
            return txt
    return None


def match(value: str, signatures: dict[str, str]) -> str | None:
    value = value.lower()
    return next((name for sig, name in signatures.items() if sig in value), None)


def classify(mx: list[tuple[int, str]], spf: str | None) -> dict:
    inbound = [{"priority": p, "host": h, "provider": match(h, MX_SIGNATURES) or "Unknown"} for p, h in mx]
    senders = []
    if spf:
        for term in spf.split():
            if term.startswith("include:"):
                senders.append({"include": term[8:], "provider": match(term, SPF_SIGNATURES) or "Unknown"})
    primary = inbound[0]["provider"] if inbound else "No MX records (domain may not receive mail)"
    notes = []
    if inbound and "gateway" in primary:
        mailbox = {s["provider"] for s in senders} & {"Microsoft 365", "Google Workspace"}
        notes.append("Inbound mail passes through a security gateway first. "
                     + (f"Mailboxes are likely in {', '.join(sorted(mailbox))} (from SPF)."
                        if mailbox else "Check SPF or the gateway to find the mailbox platform."))
    if spf is None:
        notes.append("No SPF record found. That's a deliverability and spoofing risk worth flagging.")
    elif spf.rstrip().endswith("+all"):
        notes.append("SPF ends in +all, so ANY server may send as this domain. That's a spoofing risk.")
    return {"primary_inbound": primary, "mx": inbound, "spf": spf, "spf_senders": senders, "notes": notes}


def check(domain: str) -> dict:
    result = classify(parse_mx(dig(domain, "MX")), parse_spf(dig(domain, "TXT")))
    result["domain"] = domain
    return result


def render(r: dict) -> str:
    lines = [f"\n{r['domain']}", f"  Mail is handled by: {r['primary_inbound']}"]
    for m in r["mx"]:
        lines.append(f"    MX {m['priority']:>3}  {m['host']}  [{m['provider']}]")
    lines.append(f"  SPF: {r['spf'] or '(none)'}")
    for s in r["spf_senders"]:
        lines.append(f"    authorized sender: {s['include']}  [{s['provider']}]")
    lines += [f"  ! {n}" for n in r["notes"]]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Identify which platform handles a domain's email.")
    ap.add_argument("domains", nargs="+")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()
    results = [check(d) for d in args.domains]
    print(json.dumps(results, indent=2) if args.json else "\n".join(render(r) for r in results))
    return 0


if __name__ == "__main__":
    sys.exit(main())
