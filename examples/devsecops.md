# Example Resume
## Target Role

DevSecOps Engineer

---

# Purpose

Reference resume for

- DevSecOps Engineer
- Security Automation Engineer
- CI/CD Security Engineer
- Platform Security Engineer

This file defines the desired emphasis, terminology, ordering, and technical depth.

Do not copy bullets verbatim.

Generate new bullets from the knowledge base.

---

# Target Priorities

Highest Priority

- CI/CD Security
- Security Automation
- Build Security
- Infrastructure Security
- Secrets Management

Medium Priority

- SAST / DAST integration
- Container security
- Cloud security posture
- Scripting and tooling

Low Priority

- Generic QA
- Frontend work
- Academic projects

---

# Section Order

Header

↓

Experience (Mindpex + Epicor — both always in Experience section)

↓

Projects (All 3 projects always included, ordered by JD alignment score: Slot 1: 3 bullets, Slot 2: 3 bullets, Slot 3: 2 bullets)

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

- Static code analysis and dynamic testing methodology
- Perimeter security findings (dead middleware, rate limiting bypass)
- CI/CD-adjacent findings (rate limiting misconfiguration in Next.js middleware chain)
- Remediation delivery (TypeScript, Python, SQL)

Example Bullet

Conducted a full-scope VAPT across 7 security domains on a Next.js + FastAPI SaaS platform, identifying a critical misconfiguration where rate-limiting middleware was wired to the wrong execution layer, disabling all perimeter controls.

Example Bullet

Delivered code-level remediation in TypeScript, Python, and SQL across 30+ CVSS-scored findings, including SSRF, privilege escalation, and broken authentication vulnerabilities.

Example Bullet

Performed static analysis of 47 PostgreSQL migration files identifying unauthenticated write access to security-critical tables, including MFA and webhook configuration.

---

## Epicor Software

Focus

- ADO CI/CD pipeline creation (agent-VM architecture)
- PowerShell scripting deployed within those pipelines
- VM disk cleanup automation
- Log-based root cause analysis on pipeline failures

Suppress

- Pipeline-as-code / Jenkinsfile authoring as primary framing
- Azure Pipelines YAML authoring as primary framing

Star Bullet

Engineered a PowerShell cleanup script deployed across 5 agent VMs via automated ADO pipeline, clearing ~15 GB of logs and temp data weekly — eliminating pipeline failures caused by storage exhaustion.

Example Bullet

Created ADO CI/CD pipelines using agent-VM architecture to automate enterprise build and deployment workflows; authored PowerShell scripts executing within those pipelines for environment provisioning and maintenance.

Example Bullet

Performed log-based root cause analysis on pipeline and script failures — tracing storage exhaustion and network-related execution errors through systematic pipeline execution logs.

---

# VigiLynx

Priority

★★★★★

Focus

- Security automation (ML-based detection pipeline)
- Threat detection integration
- API-based threat intelligence (VirusTotal)
- Browser security tooling

Example Bullet

Engineered a phishing detection pipeline integrating a Random Forest classifier with VirusTotal API analysis, achieving real-time URL threat classification across 1,000+ analyzed URLs via a Chrome extension.

Example Bullet

Automated malware detection and alert generation workflows, integrating browser-side security tooling with a Node.js backend for persistent threat logging.

Example Bullet

Implemented a security dashboard for visualizing phishing detections, malware scan history, and URL risk scores with Supabase-backed storage.

---

# Security Assessment

Priority

★★★★☆

Focus

- Black-box security testing
- API & Auth validation
- Security gates & remediation design

Example Bullet

Performed an authorized black-box assessment evaluating authentication, authorization, and API security across an enterprise SaaS platform.

Example Bullet

Identified access-control and configuration weaknesses including Broken Object-Level Authorization (BOLA) using Burp Suite and ffuf.

Example Bullet

Delivered automated security verification procedures and remediation guidance to establish security gates within development pipelines.

---

# CipherCrack

Priority

★★★☆☆

Focus

- Security Tooling
- Automation
- Python

Suppress

- Educational language

Example Bullet

Developed an offline Python security toolkit implementing 9 classical ciphers with modular CLI architecture and automated execution.

Example Bullet

Automated cryptanalysis workflows to support rapid vulnerability verification and offline security tool development.

---

# Skills

Programming

- Python
- PowerShell
- Bash
- JavaScript
- TypeScript

CI/CD and Automation

- Jenkins
- Azure DevOps
- ADO Pipelines (agent-VM)

Security

- VAPT
- SSRF
- API Security
- Authentication Testing
- Static Code Analysis

Operating Systems

- Linux (Kali, Ubuntu)
- Windows

Tools

- Burp Suite
- Nmap
- ffuf

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

- CI/CD
- Azure DevOps
- ADO Pipelines
- PowerShell
- DevSecOps
- Security Automation
- VAPT
- SSRF
- API Security
- OWASP
- Static Analysis
- Burp Suite
- Python
- Linux

---

# Validation Checklist

✓ No Summary section

✓ Mindpex VAPT in Experience section (always)

✓ Epicor in Experience section (always)

✓ Projects section has 3 entries ordered by JD alignment score (3/3/2 bullet split)

✓ Certifications & Achievements merged into single section

✓ Skills compressed to 12–15

✓ ADO pipeline + VM cleanup script framing in Epicor bullets

✓ No 'Jenkinsfile authoring' or 'pipeline-as-code' as primary Epicor framing

✓ DevSecOps framing in Mindpex bullets

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

Projects: VigiLynx is the primary project for this role.

Agent selects 2–3 projects based on available page space.

Emphasize

- ADO pipeline creation and VM-level automation
- PowerShell scripts executing within pipelines
- Disk cleanup / storage exhaustion elimination
- Full-scope VAPT with remediation delivery
- Security automation scripting

Suppress

- Pipeline-as-code authoring as the primary Epicor narrative
- Generic QA / software testing language
- Frontend development details
- Non-security engineering terminology
