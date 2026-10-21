# CSOL 530: Cyber Security Risk Management (NIST RMF Walkthrough)

**Course:** University of San Diego, M.S. Cybersecurity Operations & Leadership (Summer 2022). Managing information-system risk with the NIST Risk Management Framework (RMF), from categorization through continuous monitoring.

**Skills & frameworks:** NIST RMF (SP 800-37), FIPS 199 / FIPS 200, NIST SP 800-60 (information types), SP 800-53 Rev. 5 (control selection and tailoring), SP 800-30 (risk assessment), SP 800-137 (continuous monitoring), CIA triad, HIPAA context, System Security Plan (SSP), Security Assessment Plan / Report (SAP / SAR), POA&M, Authorization to Operate (ATO), change management.

**Scenario:** I took one **fictional case-study company**, *BioHuman*, a healthcare organization moving to cloud services, through every RMF step in a weekly series of individual papers. The system in scope was its payroll system, which holds Social Security numbers, tax records, salary, pension, and insurance data.

---

## The RMF walkthrough at a glance

| RMF step | Paper | What I decided or produced |
|---|---|---|
| **Prepare** | 1.1 Developing a Cybersecurity Plan | Framed BioHuman's cloud-launch risks around confidentiality, integrity, and availability, with HIPAA and the NIST CSF in mind |
| **Categorize** | Module 2 Preparation & Categorization | Applied FIPS 199 impact levels and the SP 800-60 four-step categorization process to the payroll system |
| **Select** | Module 3 Baseline Security Controls | Rated C, I, and A each **High**, making it a high-impact system under FIPS 200, and selected 11 SP 800-53 control families |
| **Implement** | Week 4 Implementation | Implemented the "-1" Policy and Procedures control for each family, mapped to physical, technical, and administrative safeguards |
| **Assess** | Week 5 Assessment | Assessed Access Control after new-hire lockouts led to credential and device sharing; produced a SAP approach and a POA&M |
| **Authorize** | Week 6 Authorization | Summarized the SAR, the remediation, and an AO recommendation for an **ATO**, with flagged controls to be reviewed within six months |
| **Monitor** | Module 7 Continuous Monitoring | Built a monitoring and change-management approach, updated AC-1, and added **AC-3(14)** |
| Supporting artifact | Information System Security Plan template | Started an SSP for "BioHuman Payroll Services (BHPS)", categorized **High** |

---

## 1. Prepare & Categorize

**Objective:** Figure out what's at stake and how bad a compromise would be before choosing any controls.

**What I did**
- Framed the cloud-launch risks for a healthcare organization through the CIA triad. Confidentiality covers the misuse of patient health and financial data. Integrity means data arrives unaltered. Availability means patients can reach their information at any time.
- Applied the FIPS 199 low / moderate / high impact definitions and the SP 800-60 categorization steps: identify information types, choose provisional impact levels, review and adjust them, then assign the system's security category.

**Key findings / outputs:** The payroll system holds highly sensitive PII and financial data, so it needs a careful, documented categorization before any controls are chosen.

**Takeaways:** Categorization drives everything after it. If you skip it, you end up choosing controls by habit instead of by risk.

## 2. Select baseline controls

**Objective:** Choose and justify a control baseline for the payroll system.

**What I did and key findings**
- **Confidentiality = High.** A breach would expose employee tax and financial data and could lead to lawsuits and fines.
- **Integrity = High.** Laws and policy prohibit unauthorized changes to payroll records.
- **Availability = High.** Availability was only Moderate while paper timesheets served as a backup. After the move to the cloud, a paper backup was no longer realistic, which raised it to High.
- Under FIPS 200, one High objective makes the whole system **high-impact**.
- I selected 11 control families: **AC, AT, AU, CA, IA, IR, MA, PT, RA, SC, SI**.
- I grouped the controls as managerial, operational, or technical, and by function as preventive, detective, or compensating. I recommended inheriting policies from comparable payroll systems as a starting point.

**Takeaways:** The availability rating changed because the operating environment changed. That taught me to re-check impact levels whenever the architecture shifts.

## 3. Implement

**Objective:** Turn the selected baseline into policies and procedures that can actually be enforced.

**What I did:** I implemented the policy and procedures control for each family (AC-1, AT-1, AU-1, CA-1, IA-1, IR-1, MA-1, PT-1, RA-1, SC-1, SI-1). I showed how these work across three kinds of safeguards:
- **Physical:** role-based keycard access, so front-desk staff can only open limited areas.
- **Technical:** only HR can handle payroll password resets.
- **Administrative:** written policies that hold every user accountable for activity on the system.

**Takeaways:** Policies set the minimum bar. Procedures describe how that bar is actually met, and remote and IoT access make both more important.

## 4. Assess

**Objective:** Test whether Access Control was actually working after implementation.

**What I did:** I scoped an assessment of the AC control after new hires couldn't log in and began sharing credentials and devices with coworkers to work around the problem. I followed the SP 800-30 process of framing, assessing, responding, and maintaining. Framing defined the assessment's purpose, scope, constraints, information sources, and risk model. The assessment looked for relevant threats, threat sources, and adverse impacts.

**Key findings / outputs**
- The workaround was a **high-impact insider-risk issue**, because shared credentials undermine accountability.
- I wrote a **POA&M** with planned milestones, control updates, follow-up dates, and points of contact. The control would be periodically reassessed until its risk could be lowered.
- **The POA&M entry itself** (FedRAMP template, system rated High): the weakness was detected from Nessus reports showing repeated login failures for the same accounts from multiple trusted devices, evidence that new hires were borrowing coworkers' machines. The remediation was to implement **AC-2 Account Management**, with the cloud provider's account manager listed as a vendor dependency. The first milestone was zero new-hire login failures within 180 days. A later status update recorded it as on pace to finish 30 days early and set a tighter 30-day target. Risk stayed rated High and the item was marked an operational requirement, with the deviation rationale that most new hires could now get into their accounts.

**Takeaways:** Users who are stuck will find a workaround, and the workaround is often the real vulnerability.

## 5. Authorize

**Objective:** Package the results so an Authorizing Official (AO) can make a risk decision.

**What I did and key findings**
- The SAR confirmed **high-level weaknesses in both physical and technical access control**. Because the system was mission-critical, the overall risk was still judged acceptable.
- **Remediation in the scenario:** accounts for employees hired in the last six months were reset. Those employees, and anyone on hardware from 2017 or earlier, got upgraded computers. That covered nearly 80% of staff at the corporate office, because the older machines couldn't run the required applications.
- **AO recommendation:** issue an **Authorization to Operate** and review the flagged controls within six months. The technical access control would be monitored annually for further authentication failures.

**Takeaways:** Authorization is a business decision about accepting risk, not a pass/fail grade. Your job is to give the AO a clear SAR and POA&M to decide from.

## 6. Monitor

**Objective:** Keep the authorization valid as people, technology, and regulations change.

**What I did**
- Tied continuous monitoring to RMF **Task P-7** (the organization-wide monitoring strategy) and to SP 800-137, noting that automated tools allow near-real-time risk management.
- Applied four change-management principles: understand the change, plan it, implement it, and communicate it.
- **Control adjustments:** I updated **AC-1** so policies get reissued whenever hardware, software, or firmware changes. I added **AC-3(14) Access Enforcement: Individual Access** to cover onboarding, promotions, and departures. That means issuing keys and equipment, assigning roles, and updating or revoking access.
- Fed the findings back into the SSP and POA&M.

**Takeaways:** Most access problems happen during onboarding, role changes, and offboarding. Monitoring those joiner/mover/leaver events is where the RMF connects to everyday sysadmin work.

---

## Interview talking points
- I've taken one system through every RMF step: categorize, select, implement, assess, authorize, monitor. I can explain which artifact (SSP, SAP, SAR, POA&M, ATO) belongs to each step.
- I can explain a FIPS 199 / FIPS 200 high-water-mark decision, including how a move to the cloud raised availability from Moderate to High.
- I've written a POA&M for a real-world-style finding: credential sharing caused by a broken onboarding process.
- I know the difference between fixing a control and accepting risk: the AO granted an ATO with a six-month review.
- I can connect continuous monitoring and AC-3(14) to joiner/mover/leaver access reviews.

**ePortfolio page:** https://qjacksoncsol23.weebly.com/risk-management.html
