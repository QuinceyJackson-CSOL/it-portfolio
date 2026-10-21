# CSOL 550: Management & Cybersecurity

*University of San Diego, M.S. Cybersecurity Operations & Leadership (Fall 2022)*

Running security as a business function: audit and compliance, acquisitions and vendor management, and planning for an organization's information systems security.

**Skills & frameworks:** Compliance auditing vs. assessment, FISMA, FIPS 199, NIST guidance, CISA auditors, penetration testing and red teams, Request for Proposal (RFP) writing, vendor risk and evaluation criteria, HIPAA and PCI DSS, business continuity (BCP) vs. disaster recovery (DRP), DRaaS

---

## 1. Request for Proposal: cyber awareness training program

*Fictional Fortune 500 pharmaceutical company used as the course scenario.*

**Objective:** Write a complete RFP to bring in an outside vendor to build and run a security awareness training application for on-site and remote staff.

**What I did**
- Wrote the full RFP: company background, project goals, scope of work, a deliverable schedule (a 60-day bidding window and about six months to launch), known roadblocks, budget constraints, evaluation metrics, required bidder questions, and submission rules.
- Built security requirements into the procurement itself:
  - Vendors must carry full liability insurance.
  - No subcontracting to other third parties.
  - Vulnerability testing before deployment.
  - Secure off-site backups.
  - 24/7 support across time zones.
  - Activity and test logs handed over to the company.
  - The company owns the training app outright, so it can be reused for new hires.

**Key findings / outputs**
- Five evaluation criteria: past performance (excluding vendors with recent breaches or negligence lawsuits), samples from similar projects, projected cost with no hidden fees, technical expertise, and how well bidders answered in interviews.
- Seven screening questions for bidders, covering breach history and downtime, third-party use, backups, and pre-release testing.

**Takeaways**
- Vendor risk is easiest to manage *before* the contract is signed. Writing the security requirements into the RFP makes them non-negotiable.

---

## 2. Audit & compliance paper

**Objective:** Explain why compliance audits matter and what auditors look for under FISMA.

**What I did**
- Separated **audits** (are the controls in place?) from **assessments** (how well do they work?).
- Laid out the documentation FISMA expects: a system inventory, FIPS 199 risk categorization, a system security plan, risk assessments, and certification and accreditation.
- Compared three ways to verify controls: certified information systems auditors (CISAs), penetration testers, and multidisciplinary red teams that also test physical security, communications security, and administrative procedures.

**Takeaways**
- Written policies only count if there's proof people actually follow them. That's why audits typically run every year and again whenever major new controls go in.

---

## 3. Ethics & compliance memo: HIPAA and PCI DSS gaps

*Fictional health-software company ("BioKidz") that had just signed a contract with a large national hospital system.*

**Objective:** Tell leadership, candidly, where the company's growth had outrun its HIPAA and PCI DSS controls, and what to fix before a breach or a fine.

**What I did**
- Identified two urgent gaps:
  - **Third-party processing:** customer card transactions were handled by an offshore development team chosen to cut costs. I raised the known risk of developers leaving backdoors that bypass normal security.
  - **Physical storage:** paper copies of patients' payment and health information sat in a storage room at the only office, and every employee's badge opened every door.
- Noted the legal side of growth: the company now served patients in many states, so California-only consumer protections no longer covered its obligations.
- Framed the fixes as an ethical duty, not just a compliance one: knowingly cutting costs or ignoring a known risk is unethical even if no damage has happened yet.

**Key findings / outputs**
- Recommendations: move the paper records to secured digital storage, limit the storage room to staff who need it for their jobs until then, replace the offshore provider, and build compliance for every state the company serves.

**Takeaways**
- Controls that were adequate for a small company can quietly become violations after a big contract. Growth is a trigger for re-checking compliance.

---

## 4. Disaster recovery & continuity management briefing

*Slide briefing written as CISO of a fictional ed-tech company serving Southern California school districts.*

**Objective:** Get leadership to plan for disruption (breaches, natural disasters, and acts of terror) before it happens.

**What I did**
- Opened from an "assume we will be hacked" position: attack surfaces keep growing, so the company has to analyze its own surface to prioritize vulnerabilities and build cyber resilience.
- Separated the two plans that are often confused: the **BCP** keeps normal business running and limits operational downtime; the **DRP** restores data access and infrastructure and limits the impact of technology failures.
- Recommended keeping backups off-site rather than in the same building, a flexible master plan, and practicing the DRP with all staff.
- Evaluated cloud-hosted recovery (DaaS/DRaaS): replicating and hosting servers off-site through a third party, with the cloud data encrypted, and pay-as-needed pricing that suits a small company.

**Takeaways**
- Never keep all your information at one site. Continuity is about not stopping; recovery is about restoring correctly.

---

## Interview talking points
- I've written a full RFP that puts security requirements (insurance, no subcontracting, pre-release testing, off-site backups, log handover) directly into vendor selection.
- I can explain the difference between an audit and an assessment, and list FISMA's core documentation.
- I understand when to use auditors, pen testers, or red teams.
- I can explain the difference between a business continuity plan and a disaster recovery plan, and why off-site or DRaaS backups belong in both.
- I think about security in budget and schedule terms, not just technical ones.

**ePortfolio:** [Management & Cybersecurity](https://qjacksoncsol23.weebly.com/management--cybersecurity.html)
