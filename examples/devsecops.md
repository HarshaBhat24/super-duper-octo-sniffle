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

Experience (Mindpex + Epicor - both always in Experience section)

↓

Projects (Agent should select 2)

↓

Skills

↓

Certifications & Achievements

↓

Education

---

# Experience

## Mindpex VAPT Freelance

Label on resume: Security Consultant (Freelancer) - Mindpex
*(or "Freelance VAPT Engagement - Enterprise SaaS Platform" if client anonymity is requested)*

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

Roles on resume:
- Associate Product Developer (Sep 2026 – Present) (2 bullets)
- Product Development Intern (Oct 2025 – Sep 2026) (2 bullets)

Focus

- ADO CI/CD pipeline automation with PowerShell execution across agent VMs
- Automated VM cleanup PowerShell script (~ 50 GB/wk cleared, eliminating storage exhaustion)
- Re-testing penetration testing defect tickets using Burp Suite (BOLA, JWT, CSP bypasses)
- Application certificate renewal and CA certificate creation
- Log-based root cause analysis across Linux execution environments

Suppress

- QA terminology
- Regression Testing
- Pipeline-as-code / Jenkinsfile authoring as primary framing

### Associate Product Developer (2 bullets)

Star Bullet (AppSec Defect Verification)

Renewed application certificates and created CA certificates for enterprise application components, applying certificate lifecycle management alongside Azure DevOps pipeline orchestration and Agile delivery.

Example Bullet (Certificate Lifecycle & Infrastructure)

Re-tested 5 penetration testing defect tickets using Burp Suite and manual API manipulation; identified incomplete remediations across 3 defects (CSP unsafe-inline bypass, BOLA user-data exposure, JWT post-logout invalidation failure) and returned tickets in Jira with reproduction PoCs.

### Product Development Intern (2 bullets)

Star Bullet (Environment Reliability Automation)

Engineered a PowerShell cleanup script deployed across 5 agent VMs via automated ADO pipeline, clearing ~ 50 GB of logs and temp data weekly - eliminating pipeline failures caused by storage exhaustion.

Example Bullet (Automation & Testing)

Developed TypeScript UI automation of the enterprise application and authored Python/Locust load testing scripts exercising application workflows across multiple parallel Chrome instances under concurrent load.

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

Example Bullet

Applied automated frequency analysis and key-space reduction algorithms to decrypt encrypted artifacts across multiple cipher implementations.

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

CompTIA Security+ (SY0-701) - June 2026

2.

ISC2 Certified in Cybersecurity (CC) - Feb 2026

Achievements

1.

Winner - HackAthena'25 Cybersecurity Track

2.

Solved 200+ CTF challenges

---

# Education

New Horizon College of Engineering, Bengaluru

Nov 2022 - July 2026

B.E. in Information Science and Engineering, CGPA: 8.57

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

✓ Agent should select 2 project slots based on JD alignment (3 bullets each)

✓ Certifications & Achievements merged into single section

✓ Skills dynamically aligned with JD without rigid count caps

✓ ADO pipeline + VM cleanup script framing in Epicor bullets

✓ No 'Jenkinsfile authoring' or 'pipeline-as-code' as primary Epicor framing

✓ DevSecOps framing in Mindpex bullets

✓ No QA terminology

✓ CompTIA Security+ (June 2026) included

✓ ISC2 CC (Feb 2026) included

✓ HackAthena Winner included

✓ 200+ CTF challenges included

✓ Education section with New Horizon College of Engineering, CGPA: 8.57

✓ Epicor has 4 bullets total (2 for Associate Product Developer, 2 for Intern); Mindpex has 3 bullets; selected projects have 3 bullets each

✓ One-page resume

✓ Mindpex described as "Security Consultant (Freelancer) - Mindpex"

✓ No fabricated information

---

# Reference Notes

Both Mindpex and Epicor are always in the Experience section for this role.

Projects: VigiLynx is the primary project for this role.

Agent selects 2 projects based on JD alignment (3 bullets each).

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
