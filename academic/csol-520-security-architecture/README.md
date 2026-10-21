# CSOL 520: Security Architecture (SABSA)

**Course:** University of San Diego, M.S. Cybersecurity Operations & Leadership. Designing enterprise security architecture that starts from business requirements and traces down to components.

**Skills & frameworks:** SABSA (six layers, 36-cell matrix, Security Service Management), business-driven and risk-driven architecture, traceability from requirements to controls, defense in depth, Zero Trust, endpoint detection, compliance drivers (PCI, healthcare data protection).

---

## 1. Applying the SABSA layers to an urgent-care medical office

**Objective:** Show how each SABSA layer would apply to a healthcare organization that stores sensitive patient data. The urgent-care office was a **case-study scenario**, not a real client.

**What I did**
- Built a table of the six SABSA layers, each with a description and a healthcare example.
- Wrote an architecture artifact for each layer from Conceptual through Component. My ePortfolio displays these as separate documents.
- Planned physical devices such as laptops and heart monitors at the Physical layer. Passwords, endpoint detection, and Zero Trust went in the other layers.

**How I framed each layer**

| SABSA layer | Focus as I described it |
|---|---|
| Contextual | Which business requirements have to be met |
| Conceptual | The vision for the project and the security principles it will follow |
| Logical | High-level abstractions and the broad policies that will apply across the enterprise |
| Physical | Building the logical plans as real mechanisms |
| Component | How specific tools and products carry out the design |
| Security Service Management | Runs through all of the above (see below) |

**Key findings / outputs:** SABSA is a "through-life" method. It applies from requirements design through solution management, and each decision can be traced back to a business objective. That traceability matters in healthcare, where regulators expect protection to be both justified and documented.

**Takeaways:** Starting from business context keeps the architecture from turning into a list of tools. Every control should answer the question "which requirement does this serve?"

---

## 2. Discussion: Security Service Management across the layers

**Objective:** Explain what the Security Service Management layer means within each of the other five layers, with an example issue for each.

**What I did and key points**

| Layer | What service management covers | My example issue |
|---|---|---|
| Contextual | Business drivers, business risk assessment, performance management | A new business that must keep every system's PCI software up to date |
| Conceptual | Operational risk management, service delivery planning, service performance criteria | An organization trying to account for every possible protection strategy |
| Logical | Locating the structural elements of the system | Compliance problems caused by not protecting assets adequately |
| Physical | Identifying the physical security mechanisms needed to deploy the design | Protecting assets by managing employee privileges at work |
| Component | Identifying risks in the tools and products used | Keeping security software and tools updated and safe from attack |

**Takeaways:** Operations and management concerns show up at every layer, not only at the end. Planning for them early makes the design easier to run.

---

## Interview talking points
- I can explain SABSA's six layers and how traceability links each technical control back to a business requirement.
- I applied SABSA to a healthcare case study, placing devices, identity controls, endpoint detection, and Zero Trust at the right layers.
- I see security architecture as risk-driven and business-driven, which helps me explain design choices to non-technical stakeholders.
- I know how service management runs across all layers, so operational concerns get designed in rather than added later.

**ePortfolio page:** https://qjacksoncsol23.weebly.com/security-architecture.html
