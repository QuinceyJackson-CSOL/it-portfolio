# CSOL 540: Cybersecurity Law, Privacy & Operational Policy

*University of San Diego, M.S. Cybersecurity Operations & Leadership (Fall 2022)*

The laws, regulations, and duty-of-care standards that shape how organizations protect data, and how to turn them into operational policy.

**Skills & frameworks:** COPPA and FTC enforcement, COPPA Safe Harbor programs, NIST SP 800-53 Rev. 5 control families (AC, IA, MP), NIST SP 800-30 risk assessment, duty of care and board oversight, elements of criminal prosecution, encryption export controls (ITAR, EAR, Wassenaar Arrangement), state privacy and IoT laws (CCPA, NY SHIELD Act, CA SB-327), cyber liability insurance, supply-chain and backdoor risk

---

## 1. COPPA compliance recommendations

*Written as guidance for a fictional new media and entertainment company building apps and games.*

**Objective:** Explain what COPPA requires, learn from past enforcement, and recommend controls to keep a new company compliant.

**What I did**
- Reviewed COPPA's core requirement: verifiable parental consent for collecting data from children under 13.
- Studied two public FTC settlements: a 2020 case against a mobile game developer (about $4 million) and the 2019 Google/YouTube settlement ($170 million). In both, the company claimed it wasn't targeting children, but the evidence showed otherwise.
- Evaluated the FTC's Safe Harbor programs, including the research showing it is hard to measure how well these self-regulatory programs actually work.

**Key findings / outputs**
- Warnings and disclaimers alone aren't enough if the product and its marketing plainly target children.
- The paper recommends joining a Safe Harbor program *and* layering in NIST SP 800-53 controls, especially Access Control, Identification & Authentication, and Media Protection. It also calls for stronger sign-up and age-verification controls such as two-factor authentication.

**Takeaways**
- Compliance is about what the product actually does, not what the policy says. Controls on account creation and data collection are where privacy law becomes engineering.

---

## 2. SolarWinds (SUNBURST): duty of care and board oversight

**Objective:** Analyze the shareholder lawsuit against the SolarWinds board and what it teaches about security governance.

**What I did**
- Summarized the claims in the suit: that leadership knew of internal deficiencies (including a leaked password and outsourced development) and did not act on warnings.
- Discussed how backdoors left in by developers create risk, and how proven negligence affects cyber liability insurance coverage.
- Recommended stronger access controls and a fresh look at the development supply chain, while noting that the investigation was still ongoing.

**Takeaways**
- Leaders can be held personally accountable for ignoring known risks. Documented follow-through on findings matters as much as the controls themselves.

---

## 3. The Bangladesh Bank heist: duty of care across institutions

**Objective:** Reconstruct the 2016 SWIFT heist and decide whether the institutions involved met their duty of care.

**What I did**
- Traced the attack from public reporting: phishing emails planted malware that logged bank employees' keystrokes and credentials for roughly a year. The attackers then used the bank's SWIFT access to send 35 transfer requests, nearly $1 billion in total, against its account at the New York Fed.
- Explained the cover-up steps: tampering with the printer that produced transaction confirmations, and timing the requests so that each bank's days off (a weekend in Bangladesh, a holiday in the Philippines) fell while the others were working, which delayed discovery by about three days.
- Followed the money: the Fed's screening flagged and held 30 of the 35 requests. Of the five that went through, a $20 million transfer to Sri Lanka was caught and recovered, and about $80 million reached four dormant accounts in the Philippines and was laundered through casinos.
- Applied the four obligations of the duty-of-care doctrine from the course text: provide reasonable security, disclose breaches, accurately describe safeguards, and protect information to the standard of comparable organizations.

**Key findings / outputs**
- I concluded the Fed did not breach its duty of care: it followed SWIFT procedures, and its automated controls flagged the requests and sent them back for confirmation, but no one was working at the Bangladesh Bank to respond. Every party acted within a commercially reasonable time once the theft surfaced. Criminally, most of the laundered money was likely unrecoverable; civilly, the Bangladesh Bank maintained it was not at fault.

**Takeaways**
- Controls only help if someone is there to act on the alert. Off-hours monitoring and out-of-band confirmation for high-value transactions matter as much as the authentication itself.

---

## 4. Guccifer: defining and prosecuting cybercrime

**Objective:** Use a real prosecution to explain how cybercrime is defined and proven, and which controls would have prevented it.

**What I did**
- Summarized the U.S. Department of Justice case against the Romanian hacker known as "Guccifer," who broke into the personal email and social-media accounts of about 100 Americans, including political figures, between 2012 and 2014, and leaked private material. He was extradited, pleaded guilty to unauthorized access and aggravated identity theft, and was sentenced to 52 months.
- Distinguished civil cases (an organization or person sued for harm from an attack) from criminal ones (an insider or outsider breaking into systems), and walked through the four elements prosecutors must prove: **mens rea**, **actus reus**, **concurrence**, and **causation**. I noted why intent is especially hard to prove when attackers work remotely without witnesses.
- Wrote what I would have done as the IT lead: an SP 800-30 risk assessment of the email environment, multifactor authentication, and controls from the AC, CA, IA, IR, MA, and SI families.

**Takeaways**
- An attacker who stays in accounts for over a year points to long-standing weaknesses nobody assessed. MFA and regular risk assessments are cheap compared with the damage.

---

## 5. Encryption law for a company going multinational

*Fictional children's ed-tech company ("BioKidz") expanding overseas through a new partnership.*

**Objective:** Brief leadership on the legal limits on using and exporting cryptography before the company sells encrypted products abroad.

**What I did**
- Explained the basics leadership needed (encryption keys, why longer keys are harder to break, symmetric vs. asymmetric algorithms) and why governments regulate cryptography as a dual-use technology.
- Covered the export regime: the U.S. treats strong cryptography as a munition under ITAR (administered by the Directorate of Defense Trade Controls), the non-binding Wassenaar Arrangement among 42 countries, and the Export Administration Regulations' country groups, where some destinations need close monitoring and others are prohibited outright.
- Flagged that products with embedded encryption may need **import licenses** country by country, so launch plans have to be set per market.
- Noted that obligations grow beyond California's CCPA to laws like New York's SHIELD Act, that patented algorithms create infringement risk, and that breach evidence needs a documented chain of custody to hold up in court.

**Key findings / outputs**
- Recommended retaining counsel experienced in multinational trade, keeping exported products within the key-length limits cited in the course text, and preferring open-source or expired-patent code during development.

**Takeaways**
- Encryption choices aren't purely technical. Where a product ships decides which algorithms and key lengths it can legally use.

---

## 6. Building a cyberlaw program for a growing company

*Fictional Los Angeles ed-tech company selling software to school districts.*

**Objective:** Lay out the legal and regulatory factors a cyberlaw program has to cover as the company expands to other states and, eventually, other countries.

**What I did**
- Recommended regular risk and business impact assessments, because privacy laws differ widely by state and country, and data governance has to match the law wherever cloud data travels or is stored.
- Used state laws as examples of emerging requirements: California SB-327 (security for connected IoT devices) and Vermont's 2018 data-broker law (registration and security standards for brokers, plus free credit freezes).
- Summarized the five components of U.S. cybersecurity foreign policy and the role of trade pacts as the company moves into international markets.
- Proposed lightweight customer-side controls for cloud data, from keeping passwords secure to scanning files for malware before upload.
- Recommended **network security and privacy liability** insurance, a hybrid policy that covers both the company and its third-party providers for breach response, recovery, and penalties.

**Takeaways**
- Insurers and courts both look for adherence to accepted industry standards. Staying compliant protects the company's coverage as well as its customers.

---

## Interview talking points
- I can explain COPPA's consent requirement, why Safe Harbor membership helps, and why it isn't a guarantee.
- I can map a privacy requirement to concrete NIST 800-53 control families.
- I understand duty of care and how negligence affects both liability and cyber insurance.
- I use breach case studies (SolarWinds, the Bangladesh Bank heist) to argue for supply-chain review, off-hours monitoring, and acting on known findings.
- I can explain how encryption export controls (ITAR, EAR, Wassenaar) and import licensing affect where a product can ship.

**ePortfolio:** [Operational Policy](https://qjacksoncsol23.weebly.com/operational-policy.html)
