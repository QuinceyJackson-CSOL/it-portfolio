# Cybersecurity Fundamentals (CSOL 500: Foundations of Cyber Security)

*University of San Diego, M.S. Cybersecurity Operations & Leadership (Summer 2022)*

The program's foundation course: threats, vulnerabilities, risk, and the controls and policies that reduce them.

**Skills & frameworks:** Cloud Service & Infrastructure Protection (CIP) domains, Cloud Access Security Broker (CASB), HIPAA, risk types and risk-treatment strategies, common threat taxonomy

---

## 1. Cloud security plan for moving PHI to a SaaS provider

*Fictional pharmaceutical/healthcare company used as the course scenario.*

**Objective:** Prepare a healthcare company to move patients' protected health information into Google Workspace without breaking HIPAA.

**What I did**
- Identified the main risk, the gap between healthcare systems and HIPAA's requirements, and its consequences: legal, financial, and reputational.
- Organized the plan around the six CIP domains and listed the tools and practices to adopt in each:

| Domain | Focus in my plan |
|---|---|
| Cloud governance | Ongoing compliance monitoring, malware and intruder detection |
| Cloud data protection | Encryption, digital rights management, dual encryption-key custody |
| Cloud infrastructure protection | Intrusion detection, platform vulnerabilities, website monitoring |
| Cloud security operations | Misconfiguration detection, topology visualization, server hardening |
| Cloud data privacy | Privacy-violation monitoring, security-as-a-service |
| Cloud access & authentication | Monitoring privileged, service, and shared accounts; time-limited port and session access |

**Key findings / outputs**
- A CASB brings strong capabilities (DLP, IPS, malware prevention), but the company has to define its policies *before* turning one on or moving any data.

**Takeaways**
- In the cloud, the provider supplies the tools and the customer still owns the policy. Access control and monitoring of privileged accounts are where insider risk gets caught.

---

## 2. Common threats and risk-management strategies (from my ePortfolio)

**What I did**
- Surveyed the threats that most often hit organizations: malware and viruses, insider threats, hardware breaches, network spoofing, phishing, and brute force.
- Grouped organizational risk into compliance, financial, operational, and strategic categories, then compared the four risk-treatment strategies covered in the course: avoidance, transfer, mitigation, and exploitation (accepting a risk without intervening).

**Takeaways**
- Not every threat can be avoided, so a sound strategy always includes mitigation, and the treatment should match the risk type.

---

## Interview talking points
- I've written a cloud-migration security plan for PHI organized by control domain, from governance through privileged-access monitoring.
- I understand what a CASB does and why policy has to come first.
- I can talk through common threat categories and how to pick a risk-treatment strategy.

**ePortfolio:** [Cybersecurity Fundamentals](https://qjacksoncsol23.weebly.com/cybersecurity-fundamentals.html)
