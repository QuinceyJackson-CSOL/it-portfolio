# CSOL 510: Applied Cryptography

*University of San Diego, M.S. Cybersecurity Operations & Leadership (Fall 2023)*

How cryptography protects data in practice: classical ciphers and modern signature schemes, hardware roots of trust, disk encryption, and the legal context around encrypted platforms.

**Skills & frameworks:** FIPS 199-style impact categorization (CIA), Trusted Platform Module (TPM 2.0), measured boot and attestation, BitLocker and Personal Data Encryption, AES/XTS-AES, HIPAA/HITECH, CFAA, frequency analysis and Vigenère cryptanalysis

---

## 1. BitLocker and TPM cryptographic controls report (group project)

*Group assignment with two classmates. The organization is a fictional healthcare SaaS company used as the course scenario.*

**Objective:** Choose cryptographic controls for a cloud-hosted healthcare platform that stores protected health information (PHI).

**What we did**
- Described the operating environment and the compliance drivers: HIPAA's Privacy and Security Rules, HITECH, and state breach-notification and privacy laws such as the CCPA.
- Compared Windows encryption options:
  - **BitLocker**, which supports AES-CBC and XTS-AES with 128- or 256-bit keys.
  - **TPM-backed hardware encryption.**
  - **Network Unlock**, which skips the PIN on the corporate network and requires it off-network.
  - **Personal Data Encryption (PDE)**, which works at the file level, is tied to Windows Hello for Business, and is meant to sit *underneath* BitLocker rather than replace it.
- Weighed full-volume encryption against used-space-only encryption.

**Key findings / outputs**
- The report recommends an internal audit of the environment before deployment, and a policy requiring BitLocker on every computer because the company handles PHI.
- It also recommends used-space-only encryption for speed, paired with a policy that ePHI is always overwritten or replaced with encrypted data when removed. That second step covers the risk that previously used, unencrypted disk sectors could be recovered.
- Some later sections (key management, AD DS, FIPS support) were outlined but not finished in the copy I have, so I'm not claiming them here.

**Takeaways**
- Encryption choices are trade-offs between speed and residual risk, and a policy control can close the gap a faster technical option leaves open.

---

## 2. Trusted Platform Module use cases (group paper)

*Group assignment with two classmates.*

**Objective:** Explain how TPM chips protect the boot process and the platform.

**What we did**
- Covered:
  - **Platform Configuration Registers (PCRs):** they use a one-way "extend" operation, so they can only be appended to, never overwritten.
  - **Measured boot and attestation.**
  - **Sealed storage:** keys are released only when the system's current measurements match the expected state.
  - **Network (remote) attestation** using an identity key.
  - **What changed in TPM 2.0:** algorithm agility (symmetric and asymmetric algorithms, key-encryption-key hierarchies) and enhanced authorization (policy-based, multi-user, multi-factor, time-limited).

**Key findings / outputs**
- Because PCRs can only be extended, any change to a boot component shows up in its own measurement and in every measurement after it. That makes the boot log hard to tamper with.

**Takeaways**
- This is the foundation behind Secure Boot, BitLocker's TPM protector, and device-health attestation in modern endpoint management.

---

## 3. Security categorization of information systems (individual)

**Objective:** Assign low, moderate, or high impact for loss of confidentiality, integrity, and availability across five scenarios, and justify each rating.

**What I did**
- Rated each scenario: a public web server, a law-enforcement investigative system, routine financial administrative data, a contracting system holding both sensitive pre-solicitation data and routine data, and a SCADA system powering a military installation.
- For the mixed systems I rated each data set separately and then the system as a whole, using the high-water-mark idea: the system takes the highest rating of any data it holds.

**Takeaways**
- Categorization drives everything after it, from control baselines to monitoring priorities. In a mixed system, the most sensitive data sets the bar.

---

## 4. Classical cryptanalysis and modern signature schemes (from my ePortfolio)

**What I did**
- Broke a monoalphabetic substitution cipher using letter-frequency analysis.
- Broke a polyalphabetic (Vigenère) cipher by finding the key length first, then running frequency analysis on each key position. I used the online tools Crypto Corner and The Black Chamber.
- Summarized ElGamal, Schnorr, NIST DSA, ECDSA, and RSA-PSS in a discussion post.

**Takeaways**
- Classical ciphers fail because the plaintext's statistical patterns survive into the ciphertext. Removing that leakage is the core design goal of modern algorithms.

---

**Also completed (group):** a legal and policy recommendations memo for both parties in *WhatsApp v. NSO Group*. It covered patch cadence against zero-click exploits, security requirements and audit rights in third-party contracts, and how the CFAA and *Van Buren* bear on access via code-based barriers like end-to-end encryption. The draft I have is partly unfinished, so I'm listing it rather than featuring it.

## Interview talking points
- I can explain how BitLocker, the TPM, and PDE fit together, and when used-space-only encryption is acceptable under HIPAA.
- I understand measured boot, PCRs, and attestation: the mechanism behind Secure Boot and device-health checks.
- I can categorize a system's CIA impact and apply the high-water mark to mixed data.
- I've broken substitution and Vigenère ciphers by hand-guided frequency analysis.
- I've worked in a three-person team producing technical reports on a weekly deadline.

**ePortfolio:** [Cryptography](https://qjacksoncsol23.weebly.com/cryptography.html)
