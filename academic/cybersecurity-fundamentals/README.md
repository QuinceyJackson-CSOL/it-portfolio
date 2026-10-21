# Cybersecurity Fundamentals (CSOL 500: Foundations of Cyber Security)

*University of San Diego, M.S. Cybersecurity Operations & Leadership (Summer 2022)*

The program's foundation course: threats, vulnerabilities, risk, and the controls and policies that reduce them.

**Skills & frameworks:** Cloud Service & Infrastructure Protection (CIP) domains, Cloud Access Security Broker (CASB), NIST Cybersecurity Framework, HIPAA, risk types and risk-treatment strategies, common threat taxonomy, CIA triad, backup vs. disaster recovery, application-security best practices

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

- In a follow-up program-development paper for the same scenario, I listed the assets most at risk (clinician and patient mobile devices, remote patient-monitoring devices, and clinic hardware) and layered the **NIST Cybersecurity Framework** over the CIP domains. Identify, Protect (through a CASB), Detect, Respond (paired with cloud governance), and Recover give the structure. Each HIPAA rule then maps to a domain:
  - **Privacy Rule** → cloud data privacy (privacy-violation monitoring, security-as-a-service)
  - **Security Rule** (required risk assessments) → cloud governance
  - **Breach Notification Rule** → cloud security operations

**Key findings / outputs**
- A CASB brings strong capabilities (DLP, IPS, malware prevention), but the company has to define its policies *before* turning one on or moving any data.
- The NIST CSF is deliberately broad and not healthcare-specific, so I combined it with the CIP domains and HIPAA's rules to cover each other's gaps.

**Takeaways**
- In the cloud, the provider supplies the tools and the customer still owns the policy. Access control and monitoring of privileged accounts are where insider risk gets caught.

---

## 2. Common threats facing organizations

**Objective:** Survey the threats organizations most often face and give a way to decide which ones matter most.

**What I did**
- Started from the scale of the problem (global cybercrime costs estimated at about $6 trillion by the end of 2021) and noted a research gap: organizations rarely share data about their own incidents, which makes objective rankings hard.
- Explained how each threat works and what it leads to:
  - **Phishing and spear phishing:** convincing messages that trick users into handing over data or installing malware.
  - **Password attacks:** stealing password hashes and cracking them with rainbow tables, dictionaries, or brute force.
  - **Malware, spyware, and keyloggers:** code that exploits software weaknesses, then records activity or keystrokes to steal credentials and funds.
  - **Viruses, worms, and Trojans:** self-spreading or disguised programs that are hard to trace back to their source once inside.
  - **DoS and DDoS:** floods of requests, from one source or a botnet, that leave a system unable to respond.
  - **Stack-based buffer overflows:** malformed input that corrupts memory and crashes or takes over the system.
- Showed that the threat mix depends on the industry: a bank attack leans on spyware, keyloggers, and password theft, while an attack like Colonial Pipeline relies on ransomware.

**Key findings / outputs**
- Across almost every category, the damage depends on how much administrative access the attacker gets. I proposed the CIA triad as the test for prioritizing: any threat that breaks confidentiality, integrity, or availability belongs on the top list.

**Takeaways**
- Limiting privilege shrinks the impact of nearly every threat on the list.

---

## 3. Risk-treatment strategies for operational risk

**Objective:** Pick one of the course text's four risk types (compliance, financial, operational, strategic) and show how each treatment strategy would apply.

**What I did**
- Chose **operational risk**: cyberattacks, data theft, supply-chain and utility disruptions, loss of key personnel, physical damage, and product counterfeiting.
- Applied each strategy to a public school district, drawing on my own work in education:
  - **Avoidance:** block third-party learning platforms. Safer, but students lose valuable tools.
  - **Transfer:** hand security to a third party. Useful for a new IT team, but the district loses visibility into what is happening on its own network.
  - **Mitigation:** restrict access, unauthorized users, and unnecessary programs while keeping the web open for schoolwork.
  - **Exploitation (accepting the risk):** knowingly leaving vulnerable applications in use. I rejected this because student safety comes first.

**Key findings / outputs**
- I recommended mitigation as the default, because threats can be reduced but not avoided entirely, and it keeps administrators hands-on.

**Takeaways**
- The right strategy depends on who is affected. With minors involved, accepting a known risk isn't a real option.

---

## 4. Business continuity: backup vs. disaster recovery

**Objective:** Analyze how a major disruption would affect a large consumer streaming service, and compare recovery approaches.

**What I did**
- Mapped where a disruption could hit across the seven domains of a typical IT infrastructure: user, workstation, LAN, LAN-to-WAN, remote access, WAN, and system/application.
- Compared simple **backup and restore** with a **disaster recovery** setup in which production is replicated and kept live elsewhere.
- Assessed the business effects: existing customers locked out, new sign-ups lost to competitors, and damaged trust in the brand. I also covered the data risk, since billing details exposed during an incident can feed identity theft.

**Key findings / outputs**
- Restores are slow and don't always go smoothly, so small incidents that need a restore can cost more productivity than a large one handled by a replicated DR site. Any downtime during sign-up or renewal periods directly hits revenue.

**Takeaways**
- Recovery design should start from the two goals that matter most: minimize data loss and minimize downtime.

---

## 5. Securing a K-12 district: remote learning and application security

*Two papers applying course concepts to public education.*

**Objective:** Identify the threats schools took on when they moved online during COVID-19, and choose application-security practices that fit a school district.

**What I did**
- Reviewed research on parents', educators', and caregivers' security concerns during remote learning, and focused on four issues: **meeting authentication**, **phishing aimed at students**, **cyberbullying**, and **Zoombombing** (uninvited users disrupting classes, which can also put required instruction hours at risk).
- From an industry list of 15 application-security best practices, selected the five that fit a district: regular updates and patching, data encryption, risk assessment, limiting user access to data, and automating routine security tasks.
- Grounded each choice in the district setting: online payments from families, students' health records and learning plans, and one shared domain for students, teachers, and administrators, so a single compromised account could reach much of the system.

**Key findings / outputs**
- Remote learning: unique accounts on a single locked-down school domain for every student and staff member, ongoing training on current threats, and smaller learning groups to give students more support.
- Applications: least-privilege access across the shared domain, encryption of student records, daily and weekly review of domain traffic, and automation for routine fixes so staff can focus on bigger threats.

**Takeaways**
- In schools, identity is the control plane: one well-managed domain with proper authentication fixes several problems at once.

---

## Interview talking points
- I've written a cloud-migration security plan for PHI organized by control domain, from governance through privileged-access monitoring.
- I understand what a CASB does and why policy has to come first.
- I can talk through common threat categories and how to pick a risk-treatment strategy.
- I've applied security planning to K-12 education: identity on a single locked-down domain, least privilege, and training for remote learning.

**ePortfolio:** [Cybersecurity Fundamentals](https://qjacksoncsol23.weebly.com/cybersecurity-fundamentals.html)
