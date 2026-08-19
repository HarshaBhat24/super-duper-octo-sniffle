# Role Intelligence Matrix

Version

1.0

Purpose

This document maps every supported cybersecurity role to the candidate's strongest experiences, projects, skills, tools, achievements, certifications, and keywords.

It is used AFTER the Job Description has been analyzed.

This file determines

- Which experiences to select
- Which projects to prioritize
- Which skills to surface
- Which achievements to display
- Which technologies to suppress
- Which terminology to prefer

---

# Matrix Rules

Only ONE role may be selected as the primary role.

If the JD overlaps multiple domains,

calculate a confidence score.

Example

Application Security

85%

Product Security

70%

Detection Engineering

40%

Use the highest scoring role.

Never generate hybrid resumes unless explicitly requested.

---

# Experience Priority Scale

★★★★★

Must include

★★★★☆

Strongly recommended

★★★☆☆

Optional

★★☆☆☆

Only if requested

★☆☆☆☆

Suppress

---

# Skill Priority Scale

Critical

Important

Useful

Suppress

---

# ROLE

## Red Team Engineer

Role Score

★★★★★

---

Experience

Note: Layout A applies. Both experience entries appear in the Experience section.

Entry 1 — Mindpex VAPT Freelance

★★★★★

Emphasize

- SSRF exploitation with OOB confirmation (interactsh)
- Account takeover via invitation flow privilege escalation
- SQL wildcard injection enabling mass-deletion
- Attack chain documentation with CVSS scoring
- Penetration testing methodology (OWASP WSTG)

Suppress

- Audit logging gaps (use for Detection Engineering roles)
- RLS analysis detail (save for Product Security roles)

Entry 2 — Epicor Software Internship

★★★★☆

Emphasize

- Adversarial input testing
- Edge-case validation
- Linux
- PowerShell
- Automation

Suppress

- QA terminology
- Regression testing

---

Project Selection

Layout A: 1 slot only (Mindpex is in Experience)

1

CipherCrack

★★★★★

Note: Security Assessment may replace CipherCrack if JD emphasizes methodology over tooling.

Exclude

VigiLynx unless phishing or browser security appears in the JD.

---

Technical Skills

Critical

- Python
- Linux
- Burp Suite
- ffuf
- Gobuster
- Nmap

Important

- Bash
- JavaScript
- Wireshark
- Metasploit
- CyberChef

Useful

- SQL
- Azure DevOps

Suppress

- React
- Supabase

---

Security Concepts

Critical

- Reconnaissance
- Enumeration
- Authentication Testing
- Authorization Testing
- API Security
- OWASP
- Cryptanalysis
- Brute Force
- Web Security

---

Achievements

Order

1.

150+ CTF Challenges

2.

Top 10% TryHackMe

3.

KJSSE CTF Finalist

---

Summary Focus

- Offensive Security
- Web Application Security
- Cryptography
- Practical Security Assessments

---

Preferred Terminology

Use

- Assessed
- Enumerated
- Validated
- Identified
- Exploited
- Analyzed

Avoid

- Developed frontend
- Built dashboard
- UI

---

# ROLE

## Product Security Engineer

Role Score

★★★★★

---

Experience

Note: Layout A applies. Both experience entries appear in the Experience section.

Entry 1 — Mindpex VAPT Freelance

★★★★★

Emphasize

- SSRF and unauthenticated RLS access to security-critical tables (MFA, webhooks)
- Account takeover via invitation flow forced password override
- PostgreSQL RLS static analysis across 47 migration files
- 30+ CVSS-scored findings with code-level remediation (TypeScript, Python, SQL)
- Multi-tenant isolation violations

Entry 2 — Epicor Software Internship

★★★★★

Emphasize

- Input validation
- Secure workflows
- CI/CD
- Automation
- SQL
- Linux

---

Project Selection

Layout A: 1 slot only (Mindpex is in Experience)

1.

VigiLynx

★★★★★

Note: Security Assessment may replace VigiLynx if JD emphasizes assessment work over tooling.

Exclude

CipherCrack unless cryptography is explicitly requested.

---

Technical Skills

Critical

- Authentication
- Authorization
- API Security
- Python
- JavaScript

Important

- Burp Suite
- Linux
- Node.js
- React
- SQL

Useful

- PowerShell
- Azure DevOps

---

Security Concepts

Critical

- Secure Design
- Secure Architecture
- Secret Management
- Authentication
- Authorization
- Least Privilege
- Defense in Depth

---

Achievements

1.

HackAthena Winner

2.

Smart India Hackathon

3.

CTF Experience

---

Summary Focus

- Product Security
- Secure Design
- Secure Applications
- Authentication

---

Preferred Terminology

Use

- Engineered
- Secured
- Designed
- Validated

Avoid

- QA
- Testing engineer

---

# ROLE

## Application Security Engineer

Role Score

★★★★★

---

Experience

Note: Layout A applies. Both experience entries appear in the Experience section.

Entry 1 — Mindpex VAPT Freelance

★★★★★

Emphasize

- SSRF via unvalidated webhook URL (confirmed OOB with interactsh)
- BOLA and authentication bypass findings
- SQL wildcard injection in admin delete handler
- Prompt injection and LLM memory poisoning
- Code-level remediation in TypeScript, Python, SQL

Entry 2 — Epicor Software Internship

★★★★★

Focus

- Boundary testing
- Edge cases
- Automation
- Linux
- SQL

---

Project Selection

Layout A: 1 slot only (Mindpex is in Experience)

1.

Security Assessment

★★★★★

Note: VigiLynx may replace Security Assessment if JD emphasizes threat detection alongside AppSec.

Exclude

CipherCrack unless cryptography appears in the JD.

Technical Skills

Critical

- Burp Suite
- Python
- Authentication
- Authorization
- API Security

Important

- JavaScript
- Node.js
- Linux
- OWASP

Useful

- Wireshark
- Bash

---

Security Concepts

Critical

- OWASP
- Business Logic
- JWT
- Access Control
- BOLA
- Input Validation
- Secure Backend

---

Achievements

1.

HackAthena

2.

150+ CTFs

3.

Smart India Hackathon

---

Summary Focus

- Secure Software
- Web Application Security
- Authorization
- Product Security

---

Preferred Terminology

Use

- Validated
- Assessed
- Secured
- Designed

---

# ROLE

## Detection Engineer

Role Score

★★★★★

---

Experience

Epicor

★★★★★

Focus

- PowerShell
- Automation
- Log Analysis
- Jenkins
- Azure DevOps

---

Project Selection

1.

VigiLynx

★★★★★

2.

CipherCrack

★★★★☆

Exclude

Security Assessment unless detection engineering is mentioned alongside AppSec.

---

Technical Skills

Critical

- Python
- PowerShell
- VirusTotal
- Linux

Important

- JavaScript
- Node.js
- Wireshark

Useful

- SQL
- Bash

---

Security Concepts

Critical

- Threat Detection
- Detection Pipeline
- Malware Analysis
- Feature Extraction
- IOC Validation
- Alert Generation
- Security Automation

---

Achievements

1.

HackAthena Winner

2.

150+ CTF Challenges

3.

Top 10% TryHackMe

---

Summary Focus

- Detection Engineering
- Security Automation
- Threat Detection
- Malware Analysis

---

Preferred Terminology

Use

- Implemented
- Automated
- Integrated
- Engineered
- Detection Pipeline

Avoid

- Dashboard
- Frontend
---

# ROLE

## Security Analyst (SOC)

Role Score

★★★★★

---

Experience

Epicor

★★★★★

Focus

- PowerShell log analysis
- Script execution debugging
- Linux
- Root cause analysis
- Automation

Suppress

- Regression testing
- QA terminology

---

Project Selection

1.

VigiLynx

★★★★★

2.

CipherCrack

★★★☆☆

Exclude

Security Assessment unless web application security is explicitly requested.

---

Technical Skills

Critical

- Linux
- Python
- Wireshark
- TCP/IP
- VirusTotal

Important

- PowerShell
- Bash
- SQL
- JavaScript

Useful

- Burp Suite
- Nmap

Suppress

- React

---

Security Concepts

Critical

- Threat Detection
- Malware Analysis
- Threat Visibility
- IOC Validation
- Log Analysis
- URL Analysis
- Security Monitoring

---

Achievements

1.

HackAthena

2.

150+ CTF Challenges

3.

CompTIA Security+

---

Summary Focus

- Threat Detection
- Security Monitoring
- Malware Analysis
- Security Operations Fundamentals

---

Preferred Terminology

Use

- Investigated
- Analyzed
- Validated
- Automated

Avoid

- QA
- Software Testing

---

# ROLE

## Threat Intelligence Analyst

Role Score

★★★★★

---

Experience

Epicor

★★★☆☆

Focus

- Log analysis
- Automation

---

Project Selection

1.

VigiLynx

★★★★★

2.

CipherCrack

★★★★☆

Exclude

Security Assessment unless vulnerability intelligence is requested.

---

Technical Skills

Critical

- VirusTotal
- Python
- Linux

Important

- Wireshark
- JavaScript
- SQL

Useful

- PowerShell

---

Security Concepts

Critical

- IOC Analysis
- Threat Intelligence
- Malware Analysis
- URL Intelligence
- Threat Classification

---

Achievements

1.

HackAthena

2.

CTF Experience

3.

TryHackMe

---

Summary Focus

- Threat Intelligence
- Malware Analysis
- Detection Engineering
- Security Automation

---

Preferred Terminology

Use

- Threat Intelligence
- Detection Pipeline
- IOC
- Threat Classification

Avoid

- Frontend
- Dashboard

---

# ROLE

## Security Engineer

Role Score

★★★★★

---

Experience

Note: Layout A applies. Both experience entries appear in the Experience section.

Entry 1 — Mindpex VAPT Freelance

★★★★★

Emphasize

- Full-scope VAPT across 7 security domains
- Static code analysis + dynamic testing methodology
- 30+ CVSS-scored findings with code-level remediation
- Dead middleware (rate limiting bypass), audit logging gaps
- Multi-tenant SaaS security architecture findings

Entry 2 — Epicor Software Internship

★★★★★

Focus

- Automation
- CI/CD
- Linux
- Azure DevOps
- SQL
- PowerShell

---

Project Selection

Layout A: 1 slot only (Mindpex is in Experience)

1.

VigiLynx

★★★★★

Note: Security Assessment may replace VigiLynx if JD emphasizes web app security over tooling.

---

Technical Skills

Critical

- Python
- Linux
- PowerShell
- SQL
- Git

Important

- Node.js
- JavaScript
- Burp Suite

Useful

- Wireshark

---

Security Concepts

Critical

- Secure Design
- Authentication
- Authorization
- Threat Detection
- Security Automation

---

Achievements

1.

HackAthena

2.

Smart India Hackathon

3.

CTF Experience

---

Summary Focus

- Security Engineering
- Automation
- Secure Systems
- Application Security

---

Preferred Terminology

Use

- Engineered
- Secured
- Automated
- Validated
- Implemented

---

# ROLE

## DevSecOps Engineer

Role Score

★★★★★

---

Experience

Note: Layout A applies. Both experience entries appear in the Experience section.

Entry 1 — Mindpex VAPT Freelance

★★★★★

Emphasize

- Full-scope VAPT as security gate before production
- Dead middleware finding (rate limiting misconfiguration in Next.js middleware chain)
- Code-level remediation delivery (TypeScript, Python, SQL)
- Static analysis of infrastructure-layer security (RLS policies, header configs)
- 7 domain-specific audit reports

Suppress

- Prompt injection detail (save for AI Security roles)

Entry 2 — Epicor Software Internship

★★★★★

Emphasize

- CI/CD pipeline-as-code (Jenkinsfile + Azure Pipelines YAML)
- Jenkins to Azure DevOps migration
- Build and test environment provisioning automation (PowerShell + Batch)
- Log-based root cause analysis across Linux execution environments

Suppress

- QA/testing language
- SQL database updates

---

Project Selection

Layout A: 1 slot only (Mindpex is in Experience)

1.

VigiLynx

★★★★★

Emphasize: security automation pipeline, threat detection integration, VirusTotal API

---

Technical Skills

Critical

- CI/CD
- Jenkins
- Azure DevOps
- Azure Pipelines YAML
- PowerShell
- Python
- Linux

Important

- Bash
- VAPT
- SSRF
- API Security
- Static Analysis

Useful

- Burp Suite
- Nmap
- ffuf

Suppress

- React
- Supabase

---

Security Concepts

Critical

- DevSecOps
- CI/CD Security
- Pipeline-as-Code
- Security Automation
- VAPT
- Secure SDLC
- Remediation Design

Important

- Static Code Analysis
- Dynamic Testing
- OWASP
- API Security

---

Achievements

Order

1.

HackAthena Winner

2.

150+ CTF Challenges

---

Summary Focus

- DevSecOps
- CI/CD Security
- Security Automation
- Full-Scope VAPT

---

Preferred Terminology

Use

- Engineered
- Automated
- Integrated
- Deployed
- Instrumented

Avoid

- QA
- Test engineer
- Regression

---

# ROLE

## Security Research Engineer

Role Score

★★★★★

---

Experience

Epicor

★★★☆☆

Focus

- Root Cause Analysis
- Automation

---

Project Selection

1.

CipherCrack

★★★★★

2.

Security Assessment

★★★★★

Exclude

VigiLynx unless detection research is requested.

---

Technical Skills

Critical

- Python
- Cryptography
- Burp Suite
- Linux

Important

- Bash
- JavaScript

Useful

- SQL

---

Security Concepts

Critical

- Cryptanalysis
- Vulnerability Research
- Mathematical Cryptography
- Automation

---

Achievements

1.

150+ CTF Challenges

2.

TryHackMe

3.

KJSSE CTF

---

Summary Focus

- Security Research
- Offensive Security
- Cryptography
- Practical Security Tooling

---

# ROLE

## Penetration Tester

Role Score

★★★★★

---

Experience

Note: Layout A applies. Both experience entries appear in the Experience section.

Entry 1 — Mindpex VAPT Freelance

★★★★★

Emphasize

- SSRF exploitation and OOB confirmation (interactsh)
- SQL wildcard injection enabling mass-deletion in single request
- Account takeover via invitation flow privilege escalation
- Attack chain documentation with CVSS scoring
- Full-scope manual penetration testing methodology (OWASP WSTG)

Entry 2 — Epicor Software Internship

★★★★☆

Focus

- Edge-case validation
- Linux
- PowerShell

---

Project Selection

Layout A: 1 slot only (Mindpex is in Experience)

1.

CipherCrack

★★★★★

Note: Security Assessment is already covered by Mindpex; CipherCrack adds offensive tooling depth.

Exclude

VigiLynx unless browser security or phishing is requested.

---

Technical Skills

Critical

- Burp Suite
- ffuf
- Gobuster
- Nmap
- Python

Important

- Bash
- Linux
- Wireshark
- Metasploit
- CyberChef

Useful

- SQL

---

Security Concepts

Critical

- Enumeration
- Reconnaissance
- Authentication
- Authorization
- API Security
- Web Security
- OWASP

---

Achievements

1.

CTF Experience

2.

TryHackMe

3.

KJSSE CTF

---

Summary Focus

- Penetration Testing
- Offensive Security
- Web Application Security
- Practical Security Assessments

---

# ROLE

## Purple Team

Role Score

★★★★☆

---

Experience

Epicor

★★★★★

Focus

- Automation
- Linux
- Log Analysis

---

Project Selection

1.

Security Assessment

★★★★★

2.

VigiLynx

★★★★★

Exclude

CipherCrack unless cryptography appears in the JD.

---

Technical Skills

Critical

- Python
- Linux
- Burp Suite
- Wireshark
- PowerShell

Important

- VirusTotal
- JavaScript
- SQL

---

Security Concepts

Critical

- Detection
- Offensive Security
- Threat Detection
- Secure Design
- Security Validation

---

Achievements

1.

HackAthena

2.

CTF Experience

3.

TryHackMe

---

Summary Focus

- Offensive and Defensive Security
- Detection Engineering
- Application Security

---

# Skill Suppression Matrix

When space is limited, remove skills in this order.

Lowest Priority

- React
- TypeScript
- Supabase
- C

Medium Priority

- JavaScript
- SQL
- Azure DevOps

High Priority (never remove unless irrelevant)

- Python
- Linux
- Burp Suite
- PowerShell
- Wireshark
- VirusTotal
- Bash
- Git

---

# Project Selection Algorithm

First, determine the number of project slots from the Experience Structure Decision (master_resume_prompt.md Step 9):

**Layout A roles** (AppSec, ProdSec, Red Team, Pentesting, DevSecOps, Security Engineering): 1 project slot

**Layout B roles** (Detection Engineering, SOC, Threat Intelligence, Security Research): 2 project slots (Slot 1 is always Mindpex VAPT)

Then score available projects against these criteria:

Evaluation Criteria

Security Relevance

40%

Technical Depth

25%

JD Keyword Match

20%

ATS Coverage

10%

Metrics

5%

For Layout A: select the single highest-scoring project from VigiLynx / CipherCrack / Security Assessment.

For Layout B: Slot 1 = Mindpex VAPT (fixed). Slot 2 = highest-scoring from VigiLynx / CipherCrack / Security Assessment.

Epicor is always in Experience. Never place Epicor in a project slot.

Never include Mindpex in both Experience and Projects simultaneously.

---

# Keyword Weighting

Critical Keywords

Weight 5

Examples

- OWASP
- Authentication
- Authorization
- Python
- Linux
- Burp Suite
- API Security
- Threat Detection
- Product Security
- Application Security
- Red Team

Important Keywords

Weight 3

Examples

- SQL
- PowerShell
- Wireshark
- JavaScript
- Automation
- CI/CD

Supporting Keywords

Weight 1

Examples

- React
- TypeScript
- Supabase

---

# Final Role Validation

Before generating the resume, verify:

✓ Exactly one primary role selected

✓ Experience rewritten for that role

✓ Correct projects selected

✓ Skills reordered

✓ Achievements reordered

✓ Keywords naturally integrated

✓ Suppressed technologies omitted

✓ Resume remains factually accurate

If any validation fails, regenerate the affected section before producing the final resume.

---

# End of Role Intelligence Matrix