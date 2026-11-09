# Example Resume
## Target Role

Product Security Engineer

---

# Purpose

Reference resume for

- Product Security Engineer
- Security Engineer
- Secure Software Engineer

This file defines

- emphasis
- ordering
- terminology
- ATS keyword priorities

Generate new bullets from the knowledge base.

Never copy this example verbatim.

---

# Target Priorities

Highest Priority

- Product Security
- Secure Software Design
- Authentication
- Authorization
- Secure Architecture
- API Security
- Browser Security

Medium Priority

- Detection Engineering
- Secure Backend
- CI/CD
- Threat Detection

Lower Priority

- Offensive Cryptography
- Frontend Development

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

- SSRF and unauthenticated RLS access to security-critical tables (MFA, webhook config)
- Account takeover via invitation flow forced password override
- PostgreSQL RLS static analysis across 47 migration files
- 30+ CVSS-scored findings with code-level remediation
- Multi-tenant isolation violations

Example Bullet

Audited 47 PostgreSQL RLS migration files identifying two Critical misconfigurations granting unauthenticated write access to global security configuration tables (MFA enforcement, SMTP, webhook URLs).

Example Bullet

Identified account takeover via invitation flow forced password override and privilege escalation with first-member auto-assigned admin role; delivered TypeScript and SQL remediation.

Example Bullet

Delivered 7-domain security audit with 30+ CVSS-scored findings covering API security, auth flows, RLS policies, LLM endpoints, and rate limiting across a Next.js + FastAPI SaaS platform.

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
- Automated VM cleanup PowerShell script (~ 50 GB/wk cleared)

Suppress

- Regression
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

- Secure Architecture
- Authentication
- Authorization
- API Security
- IAM
- Secret Management

Example Bullet

Performed an authorized black-box assessment of a SaaS application evaluating authentication, authorization, and API security to identify access-control and configuration weaknesses.

Example Bullet

Validated business-logic flaws including Broken Object-Level Authorization through manual request manipulation and authorization testing with Burp Suite.

Example Bullet

Designed remediation recommendations covering IAM improvements, secure middleware, least-privilege enforcement, and secret management.

---

# VigiLynx

Priority

★★★★☆

Focus

- Browser security tooling
- ML-based threat detection pipeline
- Secure backend design
- API-based threat intelligence

Example Bullet

Engineered a phishing detection pipeline combining Random Forest URL classification with VirusTotal API malware analysis, deployed as a Chrome extension performing real-time threat assessment across 1,000+ analyzed URLs.

Example Bullet

Developed a secure Node.js backend with Supabase-backed authentication, persistent detection logging, and threat visualization dashboards for security monitoring.

Example Bullet

Implemented authenticated REST endpoints and API security controls to enforce secure data access for threat logs and user security statistics.

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

Developed an offline Python cryptanalysis toolkit implementing 9 classical ciphers with modular CLI execution and brute-force automation.

Example Bullet

Built reusable cryptographic utilities supporting rapid cryptanalysis experimentation and offline security tool development.

Example Bullet

Applied automated frequency analysis and key-space reduction algorithms to decrypt encrypted artifacts across multiple cipher implementations.

---

# Skills

Security

- Product Security
- Authentication
- Authorization
- API Security
- SSRF
- OWASP
- Secure Architecture
- Penetration Testing

Programming

- Python
- TypeScript

Systems

- Linux
- CI/CD
- Azure DevOps
- SSMS

Tools

- Burp Suite
- Nmap
- ffuf
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

Smart India Hackathon Finalist

---

# Education

New Horizon College of Engineering, Bengaluru

Nov 2022 - July 2026

B.E. in Information Science and Engineering, CGPA: 8.57

---

# ATS Keywords

Highest Priority

- Product Security
- Secure SDLC
- Authentication
- Authorization
- Secure Architecture
- Browser Security
- API Security
- Threat Detection
- TypeScript
- SSMS
- Locust
- OWASP
- Python
- Linux

---

# Validation Checklist

✓ No Summary section

✓ Mindpex VAPT in Experience section (always)

✓ Epicor in Experience section (always)

✓ Agent should select 2 project slots based on JD alignment (3 bullets each)

✓ Certifications & Achievements merged into single section

✓ TypeScript UI automation + Locust load testing framing in Epicor bullets

✓ No 'Jenkinsfile authoring' or 'pipeline-as-code' as primary Epicor framing

✓ RLS misconfigs, SSRF, and account takeover mentioned in Mindpex bullets

✓ Authentication emphasized

✓ Authorization emphasized

✓ Secure Architecture emphasized

✓ CompTIA Security+ (June 2026) included

✓ ISC2 CC (Feb 2026) included

✓ HackAthena Winner included

✓ SIH Finalist included

✓ Education section with New Horizon College of Engineering, CGPA: 8.57

✓ Epicor has 4 bullets total (2 for Associate Product Developer, 2 for Intern); Mindpex has 3 bullets; selected projects have 3 bullets each

✓ One page

✓ ATS optimized

✓ No fabricated information

✓ Mindpex described as "Security Consultant (Freelancer) - Mindpex"

---

# Reference Notes

Product Security resumes should demonstrate the ability to

- Build secure products
- Review product security
- Secure authentication systems
- Design secure architectures
- Understand software engineering

Avoid making the resume appear like a frontend developer profile.
