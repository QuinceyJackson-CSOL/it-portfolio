# IT, Security & Automation Portfolio — Quincey Jackson

> Real problems I've fixed, systems I've built, and security work I've done. Everything is written as a case study: **the problem → how I diagnosed it → the fix → how I prevented it from happening again.**

**M.S. Cybersecurity Operations & Leadership (University of San Diego, 2024)** · IT Operations at a consumer company (Okta, Microsoft 365, Google Workspace, macOS/Windows endpoints, ITSM)

**Target roles:** Systems Administrator · Systems Engineer · Cybersecurity Analyst · Cybersecurity Engineer

---

## How to navigate

| Folder | What's inside | Maps to roles |
|---|---|---|
| [01 · Basic IT Support](01-basic-it-support/) | Help desk, identity & access, onboarding/offboarding, endpoint troubleshooting | SysAdmin |
| [02 · Cybersecurity](02-cybersecurity/) | Incident response, phishing analysis, access reviews, hardening, policy | Security Analyst / Engineer |
| [03 · Automation & Scripting](03-automation-scripting/) | Bash/Python/PowerShell, GAM, API integrations, workflow automation | Systems Engineer |
| [04 · Networking](04-networking/) | Wi-Fi, DNS, VPN, firewall and connectivity troubleshooting | SysAdmin / Security Engineer |
| [05 · Hardware](05-hardware/) | Device lifecycle, imaging, peripherals, A/V, repairs | SysAdmin |
| [06 · Software & Systems](06-software-systems/) | SaaS administration, MDM, licensing, application support | Systems Engineer |
| [Academic](academic/) | Graduate coursework and capstone work | All |

## Featured work

| Project | Category | Skills shown |
|---|---|---|
| [Untangling SaaS access across an IdP and an app](06-software-systems/saas-access-two-permission-layers/) | Software · IAM | Okta provisioning, least privilege, access governance, root-cause analysis |
| [Recurring SSO lockout investigation](02-cybersecurity/recurring-sso-auth-failure-investigation/) | Cybersecurity | Sign-on policy, MFA, log analysis, ticket-pattern analysis |
| [Scareware notification triage](02-cybersecurity/scareware-browser-notification-triage/) | Cybersecurity | Threat triage, severity criteria, user education |
| [Using DNS to find where email lives](04-networking/email-routing-dns-mx-diagnosis/) | Networking | DNS MX/SPF, GAM, Exchange Online |
| [mail-provider-check](03-automation-scripting/mail-provider-check/) | Automation | Python, DNS, unit tests, CI |
| [Pre-publish sensitive-data scanner](tools/) | Automation · Security | Python, regex, DLP concepts, git hooks |
| [Digital forensics & IR lab series](academic/csol-590-incident-response-forensics/) | Cybersecurity · Grad | FTK Imager, Autopsy, Cellebrite, AXIOM, IR planning |
| [Security lab & vulnerability scanning](academic/csol-570-network-vulnerability-detection/) | Networking · Grad | Kali, Nmap, Wireshark, Nessus, OpenVAS, Kismet |
| [NIST RMF end-to-end](academic/risk-management-nist-rmf/) | GRC · Grad | SP 800-37/53, SSP, POA&M, ATO |

**Also:** [All graduate coursework](academic/) · [5 sanitized operational runbooks](runbooks/) · [How I build a knowledge base](01-basic-it-support/building-an-it-knowledge-base/) · [Outlook triage](01-basic-it-support/outlook-copy-paste-triage/) · [SSO pending-invite fix](06-software-systems/figma-sso-pending-invite/)

## Skills matrix

Every skill links to work that shows it.

| Area | Skills | Evidence |
|---|---|---|
| Identity & Access | Okta (app assignments, provisioning, Push Groups, System Log), SSO, MFA, least-privilege role design | [IdP + SaaS access](06-software-systems/saas-access-two-permission-layers/) · [SSO invite](06-software-systems/figma-sso-pending-invite/) · [SSO lockout](02-cybersecurity/recurring-sso-auth-failure-investigation/) |
| Security Operations | Scareware/phishing triage, severity and escalation criteria, access governance, sensitive-data handling | [Scareware triage](02-cybersecurity/scareware-browser-notification-triage/) · [Sanitizer](tools/) · [Sanitization policy](docs/SANITIZATION-POLICY.md) |
| Cloud / SaaS | Microsoft 365 / Exchange Online, Google Workspace (GAM), Box, Figma, 1Password, Slack | [Distribution lists](04-networking/email-routing-dns-mx-diagnosis/) · [Runbooks](runbooks/) |
| Networking | DNS (MX, SPF/TXT), email routing | [DNS MX diagnosis](04-networking/email-routing-dns-mx-diagnosis/) |
| Endpoint Support | Windows & macOS, Outlook/Office, Chrome management, Microsoft Defender | [Outlook triage](01-basic-it-support/outlook-copy-paste-triage/) · [Scareware triage](02-cybersecurity/scareware-browser-notification-triage/) |
| Scripting & Automation | Python (stdlib, argparse, regex, unittest), Bash, git hooks, GitHub Actions CI | [mail-provider-check](03-automation-scripting/mail-provider-check/) · [Sanitizer](tools/) |
| Forensics & IR | Disk and mobile forensics, hash verification, chain of custody, IR planning | [CSOL 590](academic/csol-590-incident-response-forensics/) |
| Vulnerability Mgmt | Nmap, Nessus, OpenVAS, Wireshark, Kismet, Kali lab | [CSOL 570](academic/csol-570-network-vulnerability-detection/) |
| GRC & Threat Intel | NIST RMF, SP 800-53, FIPS 199, HIPAA, COPPA, MITRE ATT&CK, Kill Chain, FAIR, SABSA | [RMF](academic/risk-management-nist-rmf/) · [CTI](academic/csol-580-cyber-threat-intelligence/) · [SABSA](academic/csol-520-security-architecture/) |
| Documentation | Runbooks, decision trees, KB design | [Knowledge base](01-basic-it-support/building-an-it-knowledge-base/) |

## About the case studies

All enterprise work has been **anonymized** in line with [my sanitization policy](docs/SANITIZATION-POLICY.md): no company names, hostnames, IP addresses, user names, tenant IDs, or credentials appear anywhere in this repo. Handling sensitive operational data responsibly is part of the job, and this repo does it on purpose.

## Contact

- Graduate ePortfolio: [qjacksoncsol23.weebly.com](https://qjacksoncsol23.weebly.com)
- LinkedIn: _add link_
- Email: qjackson0@gmail.com
