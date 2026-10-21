# CSOL 580: Cyber Threat Intelligence

**Course:** University of San Diego, M.S. Cybersecurity Operations & Leadership (Summer 2023). How to collect, analyze, and act on intelligence about threat actors and their tactics, techniques, and procedures (TTPs).

**Skills & frameworks:** Cyber threat intelligence (operational, strategic, tactical), threat actor profiling, Lockheed Martin Cyber Kill Chain, MITRE ATT&CK, FAIR risk quantification, IOC/TTP analysis, security product evaluation (gap, total cost of ownership, ROI), executive risk communication.

All work on this page was individual. The school in the main project is a **fictional case-study organization**. The breaches I analyzed are real, publicly reported incidents.

---

## 1. Cyber Threat Intelligence Program Plan for the Education Sector (final project)

**Objective:** Write a CTI program plan and risk-reduction plan for a fictional high-profile private high school in Los Angeles. The plan had to brief leaders and stakeholders on the threats facing schools and recommend affordable protection.

**What I did**
- Researched why education is a prime target: schools hold a lot of sensitive data (student health records, family and contractor information) and usually have small security budgets.
- Profiled three threat groups, using a who / what / when / where / why / how breakdown for each.
- Walked through the 2017 NotPetya attack on Maersk stage by stage using the Cyber Kill Chain.
- Summarized the TTPs that come up again and again in these attacks, and explained the three types of intelligence a CTI program produces.
- Wrote a risk-reduction chapter that compares three endpoint and identity protection platforms (see section 2).

**Plan structure**

| Section | Contents |
|---|---|
| Executive summary & purpose | Why the academy's data (high-profile families, student-athletes, contractors) needs protecting |
| 1. Emerging threats | Threat actor profiles and common TTPs |
| 2. Attack surface intelligence | Operational, strategic, and tactical intelligence, and what each is good for |
| 3. Risk management | Risk-reduction plan built around endpoint protection platforms |
| Conclusion | Key takeaways and next steps for choosing a platform |

**Threat actors profiled**

| Actor | Incident analyzed | Main techniques described | Motive |
|---|---|---|---|
| Vice Society | 2022 Los Angeles Unified School District breach (about two months of access, roughly 500 GB stolen and leaked after the district refused to pay) | Living-off-the-land via Windows Management Instrumentation (WMI); double extortion | Financial |
| Snatch ransomware group | 2022 attack on a Wisconsin school district | Rebooting victim machines into Safe Mode so security tools don't run, then encrypting | Financial |
| Sandworm | 2017 NotPetya / Maersk | Backdoored software-update supply chain (M.E.Doc), EternalBlue exploit, Mimikatz credential theft; fake ransomware with no working decryption | Destructive / nation-state |

**TTPs discussed, mapped to MITRE ATT&CK**

The paper describes these behaviors in plain language. I added the ATT&CK technique IDs for this page so the mapping is easy to see; they are not in the original submission.

| Behavior in the plan | ATT&CK technique |
|---|---|
| Phishing emails, texts, and sites | T1566 Phishing |
| WMI used for remote execution (LOTL) | T1047 Windows Management Instrumentation |
| PowerShell and other built-in tools (LOTL) | T1059.001 PowerShell |
| Mimikatz pulling credentials | T1003 OS Credential Dumping |
| EternalBlue spreading across unpatched hosts | T1210 Exploitation of Remote Services |
| Trojanized M.E.Doc update | T1195.002 Compromise Software Supply Chain |
| Safe Mode reboot to dodge AV | T1562.009 Impair Defenses: Safe Mode Boot |
| Encrypting victim data / NotPetya wiping | T1486 Data Encrypted for Impact |

**Key findings / outputs**
- Schools keep getting hit by the same groups using the same TTPs, so intelligence on attacks against peer organizations transfers directly to a new school.
- The LAUSD case shows the damage of living-off-the-land attacks. They use tools that are already on the network, so signature-only defenses can miss them.
- NotPetya spread through systems that were never patched. Basic patch hygiene would have closed the delivery path.
- The plan recommends an endpoint protection platform covering endpoint, cloud, and identity protection, chosen with budget in mind.

**Takeaways:** A good CTI plan starts with "who is likely to attack us and how," not with a product list. The Kill Chain helped me turn one incident into a narrative a non-technical audience can follow.

---

## 2. Selecting Cyber Threat Intelligence as a Service

**Objective:** Recommend a threat-intelligence and endpoint protection service for a charter school scenario with about 300 endpoints.

**What I did:** I compared three services against the same three questions: what gap does it fill, what is the total cost of ownership, and what return or savings can we expect? I used public pricing and vendor-provided ROI and savings estimates as of July 2023. I also drew on my own hands-on experience as a Google for Education user.

**Key findings / outputs**

| Service | Gaps addressed | Est. annual cost for 300 endpoints | Vendor-supplied ROI / savings |
|---|---|---|---|
| Microsoft 365 Education (A5) | Endpoint, cloud, identity; plus compliance & management tools | ~$17,280 ($57.60/user/yr) | Not calculated |
| CrowdStrike Falcon Complete | Managed NGAV + EDR, 24/7 managed service | ~$64,764 ($17.99/endpoint/mo) | ~403% (from a vendor sales chat) |
| Google for Education Plus | Endpoint, cloud, identity | ~$1,500 ($5/user/yr) | ~286% ROI; ~$86,276 estimated impact over 3 years (vendor calculator) |

- **Recommendation:** Google for Education Plus. It covered the same three protection areas at a much lower cost, which matters for a school with a fixed budget.
- I noted that ROI doesn't strictly apply to a non-profit school, so I framed the value as cost savings instead.

**Takeaways:** In a tool evaluation, fit and total cost of ownership matter as much as features. I also learned to label vendor ROI numbers as the vendor's own claims.

---

## 3. Discussions: FAIR and MITRE ATT&CK

**Objective:** Explain two frameworks analysts use alongside threat intelligence.

**What I did and key points**
- **FAIR:** FAIR is a quantitative risk model, not a framework, and it works alongside NIST or ISO. It puts loss exposure in financial terms, which helps technical teams talk risk with executives. Checklist and maturity-model approaches don't do that.
- **MITRE ATT&CK:** ATT&CK builds on the Kill Chain idea. Instead of describing a single attack, it tracks adversary behavior across 14 tactic categories, each with its own techniques. It's useful for SOC work, threat analysis, and incident response. Its main limitation is that every adversary's technique set is different, so no single view fits all.

**Takeaways:** ATT&CK shows *how* adversaries behave and FAIR shows *how much* that could cost. Used together, they connect technical findings to business decisions.

---

## Interview talking points
- I built a full CTI program plan for a fictional school, from threat-actor profiles through a budgeted risk-reduction recommendation.
- I can walk through NotPetya stage by stage on the Cyber Kill Chain and explain how basic patching would have broken the chain.
- I understand living-off-the-land attacks (WMI, PowerShell, Mimikatz) and why they're hard to catch with signature-based tools.
- I compared three security services on gap, TCO, and ROI, and I flagged vendor-supplied numbers as vendor claims.
- I can explain how ATT&CK (adversary behavior) and FAIR (financial risk) work together.

**ePortfolio page:** https://qjacksoncsol23.weebly.com/cyber-threat-intelligence.html
