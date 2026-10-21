# CSOL 590: Incident Response & Computer Network Forensics

**University of San Diego, M.S. Cybersecurity Operations & Leadership** · Summer 2023

How to plan an incident response, and how to acquire, preserve, analyze, and report on digital evidence so it holds up to scrutiny.

**Skills & tools:** FTK Imager (E01 imaging and verification), Autopsy, Cellebrite Reader / Physical Analyzer, Magnet AXIOM Examine, Windows Disk Management, hash verification, incident response planning (six-phase lifecycle, NIST SP 800-61 as a reference), RACI-style responsibility matrices, chain of custody, Fourth Amendment considerations, forensic report writing

> Privacy note: the mobile forensics labs used a course-provided training image. I replaced every name, phone number, email address, street address, serial number, and credential from that image with generic placeholders.

---

## Contents

| # | Lab / paper | Type |
|---|---|---|
| 1 | [Forensic imaging with FTK Imager](#1-forensic-imaging-with-ftk-imager) | Hands-on lab (guided) |
| 2 | [Recovering a deleted file with Autopsy](#2-recovering-a-deleted-file-with-autopsy) | Hands-on lab (guided) |
| 3 | [Mobile forensics: Cellebrite vs. Magnet AXIOM](#3-mobile-forensics-cellebrite-vs-magnet-axiom) | Hands-on lab (guided, question-driven) |
| 4 | [Final forensics report: iPhone image](#4-final-forensics-report-iphone-image) | Written deliverable |
| 5 | [Incident response plan and responsibility matrix](#5-incident-response-plan-and-responsibility-matrix) | Written deliverable |
| 6 | [Chain of custody and the Fourth Amendment](#6-chain-of-custody-and-the-fourth-amendment) | Discussion |

---

## 1. Forensic imaging with FTK Imager

**Objective:** Make forensically sound images of a USB flash drive and see how a single change to the evidence shows up in the hash values.

**What I did** (I followed the step-by-step lab instructions)
- I loaded the flash drive with a small set of test files and a course folder, then recorded the drive's disk number in Windows Disk Management.
- I tried to take the drive offline as a software write-block. **Disk Management didn't give me that option**, so I noted it in my write-up.
- I created **Image 1** with FTK Imager: E01 format, 50 MB fragments, compression level 7. I filled in the case number, evidence number, examiner name, and notes, and saved the image to a structured case folder.
- I deleted one file from the drive and created **Image 2** under a new evidence number.
- I compared the acquisition and verification reports for the two images.

**Findings/results**

| | Image 1 | Image 2 |
|---|---|---|
| Acquisition time | 8 min 57 s | 7 min 10 s |
| Verification time | 1 min 56 s | 50 s |
| Hash matches the other image? | No | No |

The two hashes were different because Image 2 was missing the deleted file. Any change to the source data changes the hash.

**Takeaways:** Hashing is how you prove an image matches its source, and how you catch a source that has changed. I also learned that software write-blocking isn't always available. That makes a hardware write-blocker and good notes even more important.

---

## 2. Recovering a deleted file with Autopsy

**Objective:** Load the earlier flash drive image into Autopsy, find the deleted file, and compare its metadata and hash to the original.

**What I did** (guided lab)
- I created a new Autopsy case, added the E01 image as evidence, and set the ingest options.
- The analysis stalled at 55%. I fixed it by turning on **"Ignore orphan files in FAT file systems"**, and the analysis then finished.
- I browsed the results, found the deleted file, and recorded its timestamps and hash.

**Findings/results**
- I recovered the file I'd deleted in the imaging lab. Its dates matched the original.
- I couldn't find the original image for a side-by-side hash comparison, so that comparison was **incomplete**.
- Autopsy showed Created, Modified, and Accessed times, but none of them told me when the file was deleted.

**Takeaways:** Tuning the ingest settings can decide whether an analysis finishes at all. Timestamps also have limits: MAC times alone don't prove when a file was deleted. And I learned to keep the reference image and its hashes with the case.

---

## 3. Mobile forensics: Cellebrite vs. Magnet AXIOM

**Objective:** Answer a set of investigative questions about an iPhone training image with two commercial mobile forensics platforms, then compare the two tools.

**What I did** (guided, question-driven lab)
- **Cellebrite Reader:** I reviewed the device report (message retention setting, Apple ID, the subscriber number tied to the SIM, the computer that last backed up the phone). I also looked at call logs (call direction and duration), Maps entries, chat and photo attachments, step counts from activity data, and saved app credentials.
- **Magnet AXIOM:** I looked up the partner location for a call, parked-car locations, Snapchat chat messages, iOS home-screen layout, cell tower location history (date, time, and cell ID), and KnowledgeC application-usage records.

**Findings/results**
- I answered every lab question. For example, I identified a 23-second outgoing call, a step count for a given day, the app placed in a specific home-screen position, and the app launched at a specific time, which KnowledgeC showed was Maps.
- The image also contained a plaintext stored credential for a messaging app. It's a good example of how much sensitive data a phone extraction can expose. (I left the credential out here.)
- **Tool comparison:** Both platforms covered roughly the same ground. I found AXIOM easier to learn as a first-time user, because it groups evidence into clear categories that you can expand.

**Takeaways:** A single question often needs several artifact sources to answer, such as call logs, cell towers, maps, and app-usage databases. Being able to move between tools, and check one against the other, is a practical skill.

---

## 4. Final forensics report: iPhone image

**Objective:** Write a formal forensic report on the iPhone SE image, focused on where the device was and what it was doing on one date.

**What I did**
- I structured the report as an executive summary, evidence and custodians, methodology (preservation and analysis), findings, and conclusion.
- I documented my tools, including Cellebrite Physical Analyzer (version 7.62) and Magnet AXIOM Examine. I used Cellebrite mainly for messages and AXIOM for call logs, device locations, and cell tower data.
- I checked several location sources against each other: a Maps search, parked-car records, cell tower data from a call, and app usage.
- I linked the device to a likely custodian (**[Device Owner]**) through the backup computer name, messages, and call records.

**Findings/results**
- Every location artifact pointed to the same U.S. state during the period in question. I found nothing suggesting the device was anywhere else.
- The device's backups and its communications both tied back to the same individual, so I named that person as the likely custodian.

**Takeaways:** A conclusion is stronger when independent artifacts agree. Writing for a non-technical reader meant leading with the answer and putting the methodology behind it. Looking back, I would also add hash values and a custodian log to the report itself.

---

## 5. Incident response plan and responsibility matrix

**Objective:** Describe the incident response lifecycle and assign clear responsibilities for each phase.

**What I did**
- I wrote up a six-phase lifecycle: **Preparation → Identification → Containment → Eradication → Recovery → Lessons Learned**. I drew on NIST SP 800-61 (Computer Security Incident Handling Guide).
- I defined four team roles: **Proactive Monitoring** (collects data), **Reporting/Technical** (analyzes it), **Communication** (keeps stakeholders and executives informed), and **Team Management** (coordination and readiness).
- I built a matrix with two concrete tasks for each role in each phase, 48 tasks in all. Examples include quarterly mock breaches, criteria for telling events apart from incidents, confirming that restore backups predate the compromise, and routine rescans after eradication.

**Findings/results:** The result is a plan and responsibility chart that someone can actually run, organized by phase and role.

**Takeaways:** A response goes faster when everyone already knows their role, and stakeholder communication is a job in every phase, not just at the end. The Lessons Learned phase is what feeds back into Preparation.

---

## 6. Chain of custody and the Fourth Amendment

**Objective:** Explain why chain of custody protects evidence integrity, and how Fourth Amendment protections apply to digital evidence.

**What I did:** I wrote discussion posts covering these points:
- Chain of custody as the record of who handled the evidence, when, where, how, and why.
- An example of preserving surveillance footage by working from a forensically sound copy.
- A case where files found outside a warrant's scope were ruled inadmissible.

**Takeaways:** Collecting evidence correctly matters as much as analyzing it. A search has to stay within the scope of the authorization. Otherwise even strong evidence can be thrown out.

---

## Interview talking points

- I've made E01 forensic images in FTK Imager and checked them with hashes. When the write-block step wasn't available, I wrote down the limitation instead of hiding it.
- I've pulled answers from a mobile image in both Cellebrite and Magnet AXIOM, including KnowledgeC usage records and cell tower data, and I can explain where each tool is stronger.
- I fixed a stalled Autopsy analysis by changing an ingest option, and I can explain why MAC timestamps alone don't prove when a file was deleted.
- I wrote an IR plan with a phase-by-role responsibility matrix, using NIST SP 800-61 as a reference.
- I understand chain of custody and search scope, so the evidence I handle stays defensible.

---

**ePortfolio:** [Incident Response and Computer Network Forensics](https://qjacksoncsol23.weebly.com/incident-response-and-computer-network-forensics.html)
