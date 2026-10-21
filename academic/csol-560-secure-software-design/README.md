# CSOL 560: Secure Software Design & Development

*University of San Diego, M.S. Cybersecurity Operations & Leadership (Spring 2023)*

Building security into every phase of the software development life cycle, and knowing how to observe, test, and measure the systems that software runs on.

**Skills & frameworks:** Windows 11 logging and monitoring (Event Viewer, AppLocker, Performance/Resource Monitor, IIS Manager, SQL Server Management Studio), ransomware simulation (KnowBe4 RanSim), web site security and SEO checks, threat/vulnerability/risk matrices, SDLC security, CIA triad

This was my most hands-on course. Below are the four deliverables that best show how I work at the keyboard and how I turn findings into a plan.

---

## 1. Ransomware simulation with KnowBe4 RanSim

**Objective:** Run a ransomware simulator against a Windows endpoint, see which attack techniques the machine could withstand, and research each scenario well enough to rate its severity.

**What I did**
- Ran KnowBe4 RanSim and documented every scenario it executed in a results table.
- For each scenario I wrote a short description of the technique it mimics (for example process hollowing, reflective injection, slow "low-and-slow" encryption, encrypt-and-delete, crypto-mining, and simulated key exfiltration over HTTP) and tied it to the real-world family it imitates, such as Locky, Thor, Maze, DoppelPaymer, DearCry, Black Kingdom, Critroni/CTB-Locker, and Virlock.
- Assigned each scenario a severity rating from my research and from whether the test machine was vulnerable.

**Key findings / outputs**
- My table covers 25 scenario entries. 14 were recorded as **vulnerable**, 6 as **not vulnerable or blocked** (including the Archiver, HollowInjector, Injector, LockyVariant, and VirlockVariant scenarios), 1 (RIPlacer) did not execute, and 4 were rated High by research alone, with no pass/fail recorded.
- Most of the vulnerable results were "strong encryption" patterns: encrypting in place, moving or streaming the data to a new file, then deleting the originals.
- I noted that the Remover scenario is meant as a control (plain file deletion that a good tool should *not* block), and I kept RIPlacer at High even though it never ran, because it is an evasion technique built to slip past anti-ransomware tools.

**Takeaways**
- A simulator shows you which specific techniques get through, which is more useful than "is antivirus installed?" It also makes a clear case for layered controls: EDR, offline backups, and patching (several of the families exploited Exchange Server).

---

## 2. Microsoft logging and monitoring audit (Windows 11)

**Objective:** Find and interpret the main log and telemetry sources a Windows administrator relies on.

**What I did**
- The course's VMware link did not work on my Mac, so I set up a Windows 11 evaluation VM in Parallels instead.
- Worked through each data source and recorded a sample and my interpretation:
  - **Event Viewer:** application, system, and security logs. I pulled apart a successful-logon security event and walked through its properties and timestamp.
  - **AppLocker logs:** filtered Event Viewer to find the events produced by application-control rules.
  - **Performance Monitor and Resource Monitor:** real-time CPU, memory, disk, and network data.
  - **IIS Manager:** turned on Internet Information Services and the IIS Hostable Web Core through Windows Features, then reviewed its site, security, and error options.
  - **SQL Server Management Studio:** installed it to reach the SQL Server logs.
  - **Diagnostic Data Viewer:** reviewed the telemetry Windows sends to Microsoft.
  - **Privacy & Security settings:** looked at call-history and app-permission records.

**Key findings / outputs**
- I wrote down the gaps honestly. I could not find System Center data, a native syslog viewer, or a "quality of experience" log on a standalone Windows 11 machine. For syslog, I documented what it is (a protocol for forwarding events to a central collector) rather than claiming I had captured it.

**Takeaways**
- Knowing where each log lives, and which ones a single host does *not* produce on its own, is the starting point for centralized logging and SIEM work.

---

## 3. Website SEO and security site-check report

*Course assessment of a real public commercial website. I've left the site unnamed here.*

**Objective:** Use an online site-checkup tool to audit a public website, then add my own analysis of its strengths and weaknesses.

**What I did**
- Ran the tool's general analysis and filled in a report template test by test, adding my own pros and cons, which the tool does not provide.
- Covered the content and performance checks (title and meta-description length, page objects, code-to-text ratio, caching, image expiry headers, canonicalization) as well as the security checks.

**Key findings / outputs**
- Overall result: SEO score of 94 (top 10th percentile), with 65 tests passed, 1 warning (meta description shorter than recommended), and 5 failed (including social-media meta tags, inline CSS, DOM size, and page objects, which made more than 20 HTTP requests).
- **Security checks:** libwww-perl user agent blocked; server signature disabled; no plaintext email addresses on the page; not listed for malware or phishing in safe-browsing checks.
- My own notes: navigation was easy, but there was no link back to the home page, several images had no links, and text made up only about 5% of the page source.

**Takeaways**
- Many basic hardening steps (hiding the server banner, disabling directory listing, blocking scripted user agents, not exposing email addresses) can be checked from the outside in minutes. That makes them a cheap first pass in any web assessment.

---

## 4. Risk management plan for a hotel's IT environment

*Fictional scenario: a hotel I created for the assignment.*

**Objective:** Build a threat, vulnerability, asset, and risk matrix for a hospitality business and propose a risk-assessment policy.

**What I did**
- Rated six threats: insider threats, flooding, a compromised administrative Wi-Fi network, stolen or damaged property, revenue loss from malware on the guest-ledger server, and inventory theft. For each one I rated the vulnerability, the asset and consequences, and the overall risk, and proposed a fix.
- Wrote a defined event → response → analysis → mitigation flow for unauthorized access to the admin Wi-Fi. Depending on the root cause, it ends in either insider-threat training or a disaster-recovery restore.

**Key findings / outputs**
- The controls I recommended include least-privilege accounts and limited admin access, changing the router's default SSID and password, mounting network hardware off the floor, physical access controls (lobby locks, keycard-only access to amenities), and staff security training.
- The policy I wrote calls for vulnerability testing every quarter, tightening to every 30 days whenever new vulnerabilities are found, plus annual employee training.

**Takeaways**
- A simple matrix makes priorities easy to defend, and a written event-to-mitigation flow turns a plan into something staff can actually follow.

---

**Also covered (see the ePortfolio):** anomaly vs. behavioral analysis, APIs/DLLs/device drivers, containerization, and vulnerability-scanning methods (passive/active, static/dynamic).

## Interview talking points
- I ran a ransomware simulator, recorded which of 25 scenario entries the test endpoint was vulnerable to, and can explain the techniques behind them: process hollowing, reflective injection, and encrypt-and-delete.
- I can find and read the core Windows logs: security logon events in Event Viewer, AppLocker events, Performance and Resource Monitor, IIS, and SQL Server. I can also say which sources a standalone host doesn't provide.
- I've done an outside-in web check covering server signature, directory browsing, bot blocking, and safe-browsing status, and wrote it up with my own analysis.
- I can build a risk matrix and turn it into a concrete testing cadence and incident flow.
- When a lab tool didn't work on my hardware, I found another way to run it (Parallels) and recorded gaps instead of papering over them.

**ePortfolio:** [Secure Software Design & Development](https://qjacksoncsol23.weebly.com/secure-software-design--development.html)
