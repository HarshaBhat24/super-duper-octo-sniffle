# Example Resume
## Target Role

Application Security Engineer

---

# Purpose

Reference resume for

- Application Security Engineer
- Secure Software Engineer
- Application Security Analyst

This file defines the desired emphasis, terminology, ordering, and technical depth.

Do not copy bullets verbatim.

Generate new bullets from the knowledge base.

---

# Target Priorities

Highest Priority

- Application Security
- Authentication
- Authorization
- API Security
- Secure Design
- Business Logic
- OWASP
- Secure Development

Medium Priority

- Product Security
- Secure Backend
- Detection

Low Priority

- Cryptography
- Generic Frontend

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

- SSRF via unvalidated webhook URL (confirmed OOB with interactsh)
- BOLA and authentication bypass in API routes
- SQL wildcard injection in admin delete handler
- Prompt injection and LLM memory poisoning
- Code-level remediation (TypeScript, Python, SQL)

Example Bullet

Identified SSRF and mass-deletion vulnerabilities in a multi-tenant SaaS API via Burp Suite and interactsh OOB callbacks; documented attack chains with CVSS scoring and delivered TypeScript remediation.

Example Bullet

Audited 47 PostgreSQL RLS migrations discovering two Critical misconfigurations granting unauthenticated write access to security-critical tables (MFA configuration, webhook URLs).

Example Bullet

Delivered a 7-domain security audit with 30+ CVSS-scored findings and code-level remediation across a Next.js + FastAPI SaaS platform, covering API security, auth flows, LLM endpoints, and rate limiting.

---

## Epicor Software

Roles on resume:
- Associate Product Developer (Sep 2026 – Present) (2 bullets)
- Product Development Intern (Oct 2025 – Sep 2026) (2 bullets)

Focus

- Re-testing 5 penetration testing defect tickets with Burp Suite
- Incomplete remediation verification (CSP unsafe-inline bypass, BOLA, JWT revocation failure)
- TypeScript UI automation of enterprise application
- Python/Locust load testing across multiple parallel Chrome instances
- Automated VM cleanup PowerShell script (~ 50 GB/wk cleared across 5 VMs)

Suppress

- QA terminology
- Pipeline-as-code / Jenkinsfile authoring as primary framing

### Associate Product Developer (2 bullets)

Star Bullet (AppSec Defect Verification)

Re-tested 5 penetration testing defect tickets using Burp Suite and manual API manipulation; identified incomplete remediations across 3 defects (CSP unsafe-inline bypass, BOLA user-data exposure, JWT post-logout invalidation failure) and returned tickets in Jira with reproduction PoCs.

Example Bullet (Certificate Lifecycle & Infrastructure)

Renewed application certificates and created CA certificates for enterprise application components, applying certificate lifecycle management alongside Azure DevOps pipeline orchestration and Agile delivery.

### Product Development Intern (2 bullets)

Star Bullet (Environment Reliability Automation)

Engineered a PowerShell cleanup script deployed across 5 agent VMs via automated ADO pipeline, clearing ~ 50 GB of logs and temp data weekly - eliminating pipeline failures caused by storage exhaustion.

Example Bullet (Automation & Testing)

Developed TypeScript UI automation of the enterprise application and authored Python/Locust load testing scripts exercising application workflows across multiple parallel Chrome instances under concurrent load.

---

# Security Assessment

Priority

★★★★★

Focus

- Authentication
- Authorization
- API Security
- Access Control
- Secure Architecture
- Business Logic

Example Bullet

Performed an authorized black-box assessment of a SaaS application evaluating authentication, authorization, and API security; identified access-control and configuration weaknesses using Burp Suite and ffuf.

Example Bullet

Validated business-logic vulnerabilities including Broken Object-Level Authorization through manual request manipulation and authorization testing.

Example Bullet

Produced remediation guidance covering secure authentication design, IAM redesign, least-privilege enforcement, and secure middleware architecture.

---

# VigiLynx

Priority

★★★★☆

Focus

- Security automation
- ML-based threat detection
- Browser security tooling
- API-based threat intelligence

Example Bullet

Engineered a phishing detection pipeline integrating a Random Forest classifier with VirusTotal API analysis, achieving real-time URL threat classification across 1,000+ analyzed URLs via a Chrome extension.

Example Bullet

Developed authenticated backend services for persistent threat logging, malware scan history, and user-specific security event monitoring.

Example Bullet

Implemented secure REST APIs and Supabase authentication handlers for threat telemetry logging and security event monitoring.

---

# CipherCrack

Priority

★★★☆☆

Focus

- Security Tooling
- Cryptography
- Automation
- Python

Suppress

- Educational language

Example Bullet

Developed an offline Python cryptanalysis toolkit implementing 9 classical ciphers with automated brute-force workflows.

Example Bullet

Designed reusable command-line utilities supporting rapid cryptanalysis experimentation during Capture The Flag competitions.

Example Bullet

Applied automated frequency analysis and key-space reduction algorithms to decrypt encrypted artifacts across multiple cipher implementations.

---

# Skills

Security

- Application Security
- API Security
- Authentication
- Authorization
- OWASP
- SSRF
- BOLA
- Penetration Testing

Programming

- Python
- TypeScript

Operating Systems

- Linux
- Windows

Tools

- Burp Suite
- Nmap
- ffuf
- interactsh
- SSMS
- Locust

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

- Application Security
- Authentication
- Authorization
- API Security
- Secure Design
- OWASP
- Secure Development
- Product Security
- Burp Suite
- Python
- TypeScript
- Linux
- SQL
- SSMS
- Locust
- Threat Detection

---

# Validation Checklist

✓ No Summary section

✓ Mindpex VAPT in Experience section (always)

✓ Epicor in Experience section (always)

✓ Agent should select 2 project slots based on JD alignment (3 bullets each)

✓ Certifications & Achievements merged into single section

✓ TypeScript UI automation + Locust load testing framing in Epicor bullets

✓ No 'Jenkinsfile authoring' or 'pipeline-as-code' as primary Epicor framing

✓ Authentication emphasized

✓ Authorization emphasized

✓ OWASP concepts reflected

✓ SSRF and BOLA mentioned in Mindpex bullets

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

This file defines the expected style for Application Security roles.

Emphasize

- Secure software engineering
- Authentication
- Authorization
- API security
- Secure architecture

Suppress

- Cryptography implementation details
- Generic frontend work
- Non-security development terminology
