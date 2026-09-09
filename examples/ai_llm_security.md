# Example Resume
## Target Role

AI / LLM Security Engineer

---

# Purpose

Reference resume for

- AI Security Engineer
- LLM Security Engineer
- ML Security Engineer
- Generative AI Security Researcher

This file defines the desired emphasis, terminology, ordering, and technical depth.

Do not copy bullets verbatim.

Generate new bullets from the knowledge base.

---

# Target Priorities

Highest Priority

- Prompt Injection
- Indirect Prompt Injection
- LLM Security
- AI Trust Boundaries
- Input Validation
- Multi-tenant Isolation
- OWASP LLM Top 10

Medium Priority

- API Security
- Authentication Bypass
- SSRF
- Static Code Analysis

Low Priority

- Frontend Development
- Generic Web Development
- Classical Cryptography

---

# Section Order

Header

↓

Experience (Mindpex + Epicor — both always in Experience section)

↓

Projects (2–3 dynamically selected)

↓

Skills

↓

Certifications & Achievements

↓

Education

---

# Experience

## Mindpex VAPT Freelance

Label on resume: Freelance VAPT Engagement — Enterprise SaaS Platform

Focus

- Direct prompt injection on open `/groq/query` FastAPI endpoint — raw user input passed verbatim to LLM with no input sanitization
- Indirect prompt injection via persistent employee memory poisoning — attacker-controlled transcript stored in long-term memory, influencing future LLM outputs
- LLM context store with zero tenant isolation — any caller could read/write any employee memory by UUID
- Unvalidated LLM context field on recommendation endpoint — no provenance or trust boundary enforcement
- Raw LLM exception messages returned in API response — infrastructure disclosure

Example Bullet

Exploited direct prompt injection on an unauthenticated FastAPI LLM endpoint, demonstrating verbatim user input passed to the model without sanitization; crafted payloads to exfiltrate system context and bypass intended model behavior.

Example Bullet

Identified indirect prompt injection via persistent employee memory poisoning — attacker-controlled transcripts stored in long-term LLM memory flowed into subsequent model prompts, enabling persistent influence over AI-generated outputs.

Example Bullet

Discovered in-memory LLM context store with zero tenant isolation; any authenticated caller could read or overwrite any employee's memory store by UUID, enabling cross-tenant context manipulation.

---

## Epicor Software

Focus

- ADO CI/CD pipelines (agent-VM architecture)
- PowerShell scripting deployed within those pipelines
- TypeScript UI automation of enterprise application
- VM disk cleanup and environment maintenance automation

Suppress

- Pipeline-as-code / Jenkinsfile authoring as primary framing
- Azure Pipelines YAML authoring as primary framing

Star Bullet

Engineered a PowerShell cleanup script deployed across 5 agent VMs via automated ADO pipeline, clearing ~15 GB of logs and temp data weekly — eliminating pipeline failures caused by storage exhaustion.

Example Bullet

Created ADO CI/CD pipelines using agent-VM architecture to automate enterprise build workflows; authored PowerShell scripts executing within those pipelines for environment provisioning and maintenance.

Example Bullet

Developed TypeScript UI automation of the enterprise application, supporting automated validation and workflow testing across the enterprise software stack.

---

# VigiLynx

Priority

★★★★☆

Focus

- ML-based detection pipeline (Random Forest)
- VirusTotal threat intelligence API integration
- Security automation
- Browser-based threat detection

Example Bullet

Implemented a Random Forest–based phishing detection pipeline using URL feature extraction to analyze 1,000+ URLs and generate real-time browser alerts through a Chrome extension.

Example Bullet

Integrated VirusTotal threat intelligence APIs to automate malware analysis, parse multi-engine verdicts, and enrich browser-based detection with external threat intelligence.

Example Bullet

Engineered authenticated backend services and dashboards for persistent threat logging, malware scan history, and user-specific security event monitoring.

---

# Security Assessment

Priority

★★★★☆

Focus

- Secure Architecture
- Authentication
- Authorization
- API Security testing

Example Bullet

Performed an authorized black-box assessment of a SaaS application evaluating authentication, authorization, and API security to identify access-control and configuration weaknesses.

Example Bullet

Validated business-logic flaws including Broken Object-Level Authorization and delivered remediation recommendations covering IAM improvements and least-privilege enforcement.

---

# Skills

Security

- Prompt Injection
- LLM Security
- AI Trust Boundaries
- Input Validation
- Multi-tenant Isolation
- OWASP LLM Top 10
- API Security
- SSRF

Programming

- Python
- JavaScript
- TypeScript

Operating Systems

- Linux
- Windows

Tools

- Burp Suite
- interactsh
- ffuf
- Nmap
- Azure DevOps

---

# Certifications & Achievements

Certifications

1.

CompTIA Security+

2.

ISC2 Certified in Cybersecurity (CC)

Achievements

1.

Winner — HackAthena'25 Cybersecurity Track

2.

Solved 200+ CTF challenges

---

# Education

Bachelor of Engineering

Information Science and Engineering

CGPA

8.57

---

# ATS Keywords

Highest Priority

- Prompt Injection
- LLM Security
- Indirect Prompt Injection
- AI Security
- OWASP LLM Top 10
- Input Validation
- AI Trust Boundaries
- Multi-tenant Isolation
- Python
- TypeScript
- Burp Suite
- Linux
- API Security
- Azure DevOps

---

# Validation Checklist

✓ No Summary section

✓ Mindpex VAPT in Experience section (always)

✓ Domain 2 (LLM Endpoint Security) is the primary focus of Mindpex bullets

✓ Epicor in Experience section (always)

✓ 2–3 dynamically selected project slots

✓ Certifications & Achievements merged into single section

✓ ADO pipeline + PowerShell + TypeScript automation framing in Epicor bullets

✓ No 'Jenkinsfile authoring' or 'pipeline-as-code' as primary Epicor framing

✓ Prompt injection findings explicitly covered

✓ Memory poisoning / indirect prompt injection covered

✓ Zero tenant isolation finding covered

✓ CompTIA Security+ included

✓ ISC2 CC included

✓ HackAthena Winner included

✓ 200+ CTF challenges included

✓ Three bullets per section

✓ One-page resume

✓ No fabricated information

✓ Mindpex described as "Freelance VAPT Engagement — Enterprise SaaS Platform"

---

# Reference Notes

AI/LLM Security resumes should communicate the ability to

- Identify prompt injection and indirect injection vectors
- Reason about LLM trust boundaries and input provenance
- Test AI-augmented applications with offensive methodology
- Understand multi-tenant isolation risks in AI systems

This role is distinct from AppSec in that the primary attack surface is the LLM itself — not just traditional web application vulnerabilities.

Security concepts should always precede implementation technologies.
