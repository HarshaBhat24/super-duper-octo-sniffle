# Company Intelligence Engine

Version

1.0

Purpose

This document defines how to classify the hiring company from the Job Description and apply tone and emphasis modifiers to the resume generation strategy.

Apply AFTER analyzing the Job Description.

Apply BEFORE selecting the target role.

---

# Company Type Classification

## Step 1 — Extract Company Signals

From the Job Description, identify:

- Company name (if stated)
- Industry signals (fintech, healthcare, SaaS, government, consulting, etc.)
- Scale signals (headcount, global, enterprise, startup, Series A/B/C, etc.)
- Security maturity signals (SOC team, CISO office, red team, embedded security, etc.)
- Role context signals (individual contributor, founding member, owns the program, part of large team, etc.)

---

## Step 2 — Classify Company Type

Map signals to ONE primary company type:

### Startup

Signals

- Early stage, Series A–C
- Small team, fast-moving
- "Founding security engineer", "build from scratch", "wearing multiple hats"
- No CISO, no established security program

Emphasis

- Breadth over depth
- Speed and autonomy
- Building security infrastructure from zero
- Proactive risk identification

Tone

- Scrappy, builder-oriented
- Show range across offensive and defensive
- Highlight initiative and independent ownership

---

### Enterprise / Large Corporation

Signals

- Fortune 500, multinational, 10,000+ employees
- Established security teams, CISO org, multiple sub-teams
- "Work within a team of X", "align with compliance", "adhere to policy"

Emphasis

- Depth in one specialty
- Process adherence
- Cross-team collaboration
- Compliance awareness (SOC 2, ISO 27001, PCI-DSS)

Tone

- Structured, methodical
- Demonstrate technical depth and domain expertise
- Highlight collaboration and documentation

---

### Big Tech / Product Company

Signals

- FAANG, large-scale SaaS, global product platform
- "Scale", "millions of users", "production systems"
- Strong engineering culture, security embedded in engineering

Emphasis

- Secure software development lifecycle
- Scalable security tooling
- Automation at scale
- Adversarial thinking applied to product

Tone

- Engineering-first
- Highlight code-level security work
- Emphasize security tooling and automation
- Demonstrate impact through scale metrics

---

### Consultancy / MSSP / Professional Services

Signals

- "Client engagements", "multiple industries", "advisory", "assessment delivery"
- MSSP, boutique security firm, big 4 advisory

Emphasis

- Breadth of assessments
- Client-facing deliverables (reports, findings)
- Methodology adherence (OWASP, PTES, NIST)
- Multi-environment exposure

Tone

- Methodical and professional
- Highlight deliverables and documented findings
- Show variety of assessments across different contexts

---

### Government / Defense / Public Sector

Signals

- Government agency, defense contractor, cleared roles
- "Security clearance", "FISMA", "FedRAMP", "compliance-driven"

Emphasis

- Compliance frameworks (NIST 800-53, FISMA, FedRAMP)
- Process rigor and documentation
- Risk management
- Formal security controls

Tone

- Formal and precise
- Emphasize framework knowledge and process compliance
- De-emphasize offensive work unless explicitly requested

---

## Step 3 — Apply Company Type Modifier

After classifying the company type, apply the following to the resume:

### Summary

Adjust framing to match company type:

- Startup → *"built and owned"*, *"designed from scratch"*
- Enterprise → *"implemented within established workflows"*, *"scaled existing practices"*
- Big Tech → *"automated at scale"*, *"embedded in SDLC"*
- Consultancy → *"delivered findings across"*, *"assessed and documented"*
- Government → *"applied frameworks"*, *"maintained compliance"*

### Bullet Tone

Adjust action verb preference by company type:

- Startup: Built, Designed, Owned, Shipped
- Enterprise: Integrated, Aligned, Documented, Governed
- Big Tech: Engineered, Automated, Scaled, Instrumented
- Consultancy: Assessed, Identified, Reported, Validated
- Government: Implemented, Documented, Audited, Enforced

### Skills Ordering

- Startup: Broad skills first, then depth
- Enterprise: Domain-specific depth first
- Big Tech: Security tooling and automation first
- Consultancy: Assessment tools first (Burp Suite, Nmap, etc.)
- Government: Compliance frameworks first

---

## Step 4 — Unknown Company

If company type cannot be determined from signals:

Default to

Enterprise / Large Corporation

modifier.

Do not guess.

Do not invent company details.

---

## Step 5 — Output Company Intelligence Report

Before proceeding to Gap Analysis, output:

```
Company Intelligence Report
Company Name: [name or "unknown"]
Company Type: [classified type]
Confidence: [High / Medium / Low]
Key Signals: [list of signals detected]
Applied Modifier: [summary of tone/emphasis changes]
```

Do NOT ask the candidate to confirm this unless confidence is Low.

If confidence is Low, ask: "I classified this as [type] — does that sound right?"

---

# End of Company Intelligence Engine
