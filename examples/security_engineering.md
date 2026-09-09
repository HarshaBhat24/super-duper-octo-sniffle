# Example Resume
## Target Role

Security Engineer

---

# Purpose

Reference resume for

- Security Engineer
- Security Software Engineer
- Infrastructure Security Engineer
- Platform Security Engineer

This file defines the desired emphasis, terminology, ordering, and technical depth.

Do not copy bullets verbatim.

Generate new bullets from the knowledge base.

---

# Target Priorities

Highest Priority

- Secure Architecture
- API Security
- Authentication and Authorization
- Security Tooling Development
- Security Automation

Medium Priority

- CI/CD pipeline security integration
- Web Application Security
- Detection and Logging
- OWASP

Low Priority

- Generic QA
- Frontend work
- Non-security development

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

- Multi-domain assessment coverage (API, Auth, RLS, LLM, Headers, Rate Limiting, Audit Logging)
- Code-level remediation delivery (TypeScript, Python, SQL)
- Static and dynamic testing methodology
- Secure architecture recommendations

Example Bullet

Performed a full-scope VAPT across 7 security domains on a Next.js + FastAPI multi-tenant SaaS platform, identifying 9 Critical and 15 High severity findings including SSRF, account takeover, and SQL wildcard injection.

Example Bullet

Audited 47 PostgreSQL RLS migration files identifying two Critical misconfigurations granting unauthenticated access to security-critical tables; delivered SQL migration scripts for remediation.

Example Bullet

Delivered code-level remediation in TypeScript, Python, and SQL across 30+ CVSS-scored findings with a prioritized P0→backlog remediation roadmap and 7 domain-specific audit reports.

---

## Epicor Software

Focus

- ADO CI/CD pipelines (agent-VM architecture)
- PowerShell scripting deployed within those pipelines
- VM disk cleanup automation
- Log-based root cause analysis on pipeline failures

Suppress

- Pipeline-as-code / Jenkinsfile authoring as primary framing
- Generic QA / testing terminology

Star Bullet

Engineered a PowerShell cleanup script deployed across 5 agent VMs via automated ADO pipeline, clearing ~15 GB of logs and temp data weekly — eliminating pipeline failures caused by storage exhaustion.

Example Bullet

Created ADO CI/CD pipelines using agent-VM architecture to automate enterprise build workflows; authored PowerShell scripts executing within those pipelines for environment provisioning and maintenance.

Example Bullet

Performed log-based root cause analysis for pipeline and script execution failures across Linux environments, applying systematic investigation methodology to recurring production build issues.

---

# VigiLynx

Priority

★★★★★

Focus

- Security tooling development
- Threat detection pipeline
- Secure backend design
- API-based threat intelligence

Example Bullet

Engineered a phishing detection pipeline combining Random Forest URL classification with VirusTotal API malware analysis, deployed as a Chrome extension performing real-time threat assessment across 1,000+ analyzed URLs.

Example Bullet

Developed a secure Node.js backend with Supabase-backed authentication, persistent detection logging, and threat visualization dashboards for security monitoring.

Example Bullet

Implemented browser-side security tooling with real-time phishing alerts and malware scan history, integrating frontend detection with backend threat intelligence APIs.

---

# Security Assessment

Priority

★★★★☆

Focus

- Secure Architecture
- Authentication
- Authorization
- API Security
- IAM

Example Bullet

Performed an authorized black-box assessment of a SaaS application evaluating authentication, authorization, and API security to identify access-control and configuration weaknesses.

Example Bullet

Validated business-logic flaws including Broken Object-Level Authorization and delivered remediation recommendations covering IAM, least-privilege enforcement, and secure middleware architecture.

---

# Skills

Security

- API Security
- Authentication
- Authorization
- OWASP
- Secure Architecture
- VAPT
- Static Code Analysis
- SSRF

Programming

- Python
- TypeScript
- JavaScript
- PowerShell
- Bash

Operating Systems

- Linux (Kali, Ubuntu)
- Windows

Tools

- Burp Suite
- Nmap
- ffuf
- interactsh
- Azure DevOps

Development

- Node.js
- SQL
- CI/CD (ADO, Jenkins)

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

CGPA 8.57

---

# ATS Keywords

High Priority

- Security Engineering
- API Security
- Authentication
- Authorization
- VAPT
- SSRF
- Static Analysis
- Secure Architecture
- Python
- Linux
- Burp Suite
- CI/CD
- PowerShell
- Azure DevOps
- OWASP
- Security Automation

---

# Validation Checklist

✓ No Summary section

✓ Mindpex VAPT in Experience section (always)

✓ Epicor in Experience section (always)

✓ 2–3 dynamically selected project slots

✓ Certifications & Achievements merged into single section

✓ ADO pipeline + VM cleanup script framing in Epicor bullets

✓ No 'Jenkinsfile authoring' or 'pipeline-as-code' as primary Epicor framing

✓ Secure architecture language in Mindpex bullets

✓ Automation and pipeline language in Epicor bullets

✓ No QA terminology

✓ CompTIA Security+ included

✓ ISC2 CC included

✓ HackAthena Winner included

✓ 200+ CTF challenges included

✓ Three bullets per section

✓ One-page resume

✓ No fabricated information

---

# Reference Notes

Both Mindpex and Epicor are always in the Experience section for this role.

Projects: VigiLynx primary, Security Assessment secondary. Agent selects 2–3 based on page space.

Security Engineering sits between AppSec and DevSecOps. Tone should be:
- Less tool-specific than AppSec
- More architecture/design-oriented
- Pipeline security positioned as security-engineering work, not just CI/CD ops

Suppress

- QA / testing language
- Generic frontend development
- Non-security engineering terminology
