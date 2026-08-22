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

Summary

↓

Experience (Mindpex + Epicor — both in Experience section)

↓

VigiLynx (ML detection pipeline — AI-adjacent signal)

↓

Skills

↓

Certifications

↓

Achievements

↓

Education

Note: Layout A. Two experience entries, 1 project slot. Mindpex Domain 2 (LLM Endpoint Security) is the primary evidence anchor.

---

# Summary Style

Characteristics

- Security research focused
- AI/ML-adjacent framing
- Technical and concise

Example

CompTIA Security+ and ISC2 Certified in Cybersecurity (CC) professional with hands-on experience identifying prompt injection, indirect memory poisoning, and LLM trust boundary violations in production AI systems. Conducted full-scope VAPT across 7 security domains on a multi-tenant SaaS platform integrating Groq and Cerebras LLMs; developed ML-based phishing detection tooling integrating Random Forest classification and VirusTotal API threat intelligence.

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

## Epicor Software Internship

Focus

- Python scripting
- Automation
- CI/CD pipeline as integration layer for security tooling

Example Bullet

Authored Jenkinsfile and Azure Pipelines YAML definitions for enterprise CI/CD pipelines, providing the integration layer for security tooling (SAST, DAST, secrets scanning).

Example Bullet

Developed PowerShell and Batch automation for build and test environment provisioning; performed log-based root cause analysis for pipeline failures across Linux execution environments.

Example Bullet

Led Jenkins to Azure DevOps pipeline migration, mapping build stages, triggers, and environment parameters while maintaining workflow continuity.

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

Note: Layout A — target 12–15 total skills.

---

# Certifications

1.

CompTIA Security+

2.

ISC2 Certified in Cybersecurity (CC)

---

# Achievements

Layout A cap: max 2

1.

Winner — HackAthena'25 Cybersecurity Track

2.

Solved 150+ CTF challenges

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
- Burp Suite
- Linux
- API Security

---

# Validation Checklist

✓ Mindpex VAPT in Experience section (Layout A)

✓ Domain 2 (LLM Endpoint Security) is the primary focus of Mindpex bullets

✓ Epicor in Experience section

✓ VigiLynx as sole project slot (ML-adjacent signal)

✓ Prompt injection findings explicitly covered

✓ Memory poisoning / indirect prompt injection covered

✓ Zero tenant isolation finding covered

✓ 12–15 skills (Layout A cap)

✓ Max 2 achievements (Layout A cap)

✓ CompTIA Security+ included

✓ ISC2 CC included

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
