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

Score order for Red Team (highest → lowest JD alignment):

1. Security Assessment
2. CipherCrack
3. VigiLynx

Slot 1 and Slot 2 get 3 bullets each. Slot 3 gets 2 bullets.

VigiLynx drops to last unless phishing or browser security appears in the JD.

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

200+ CTF Challenges

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

Score order for Product Security (highest → lowest JD alignment):

1. Security Assessment
2. VigiLynx
3. CipherCrack

Slot 1 and Slot 2 get 3 bullets each. Slot 3 gets 2 bullets.

CipherCrack drops to last unless cryptography is explicitly requested.

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

Score order for Application Security (highest → lowest JD alignment):

1. Security Assessment
2. VigiLynx
3. CipherCrack

Slot 1 and Slot 2 get 3 bullets each. Slot 3 gets 2 bullets.

CipherCrack drops to last unless cryptography appears in the JD.

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

200+ CTFs

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

200+ CTF Challenges

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

200+ CTF Challenges

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

Score order for Security Engineer (highest → lowest JD alignment):

1. VigiLynx
2. Security Assessment
3. CipherCrack

Slot 1 and Slot 2 get 3 bullets each. Slot 3 gets 2 bullets.

Note: Security Assessment may move to Slot 1 if JD emphasizes web app security over tooling.

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

Score order for DevSecOps (highest → lowest JD alignment):

1. VigiLynx
2. Security Assessment
3. CipherCrack

Slot 1 and Slot 2 get 3 bullets each. Slot 3 gets 2 bullets.

Emphasize VigiLynx's security automation pipeline, threat detection integration, VirusTotal API.

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

200+ CTF Challenges

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

200+ CTF Challenges

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

Score order for Penetration Tester (highest → lowest JD alignment):

1. Security Assessment
2. CipherCrack
3. VigiLynx

Slot 1 and Slot 2 get 3 bullets each. Slot 3 gets 2 bullets.

Note: CipherCrack adds offensive tooling depth. VigiLynx only moves up if browser security or phishing is explicitly requested.

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

Summary Focus

- Offensive and Defensive Security
- Detection Engineering
- Application Security

---

# ROLE

## AI / LLM Security Engineer

Role Score

★★★★★

---

Experience

Entry 1 — Mindpex VAPT Freelance

★★★★★

Emphasize

- Direct prompt injection on open FastAPI `/groq/query` endpoint — raw user input passed verbatim to LLM with no sanitization
- Indirect prompt injection via persistent employee memory poisoning — attacker-controlled transcript stored in long-term memory, influencing future LLM outputs
- In-memory LLM context store with zero tenant isolation — any caller could read/write any employee memory by UUID
- Unvalidated LLM context field on recommendation endpoint — no provenance or input trust boundary enforcement
- Raw exception messages from failed LLM calls returned in API response (infrastructure disclosure)
- Domain 2 (AI/LLM Endpoint Security) is the primary evidence anchor for this role

Suppress

- RLS policy detail (save for Product Security roles)
- Rate limiting misconfiguration (save for DevSecOps)

Entry 2 — Epicor Software Internship

★★★★☆

Emphasize

- Python scripting
- Automation
- CI/CD pipeline as integration layer for security tooling

---

Project Selection

Score order for AI / LLM Security (highest → lowest JD alignment):

1. VigiLynx
2. Security Assessment
3. CipherCrack

Slot 1 and Slot 2 get 3 bullets each. Slot 3 gets 2 bullets.

VigiLynx is primary — demonstrates ML-based detection (Random Forest, VirusTotal API) adjacent to AI/security tooling.
Security Assessment may move to Slot 1 if JD emphasizes traditional web assessment methodology alongside LLM security.

---

Technical Skills

Critical

- Python
- Burp Suite
- Linux
- interactsh

Important

- JavaScript
- Node.js
- ffuf
- curl

Useful

- SQL

Suppress

- React
- PowerShell (unless automation appears in JD)

---

Security Concepts

Critical

- Prompt Injection
- Indirect Prompt Injection
- LLM Security
- AI Trust Boundaries
- Input Validation
- Multi-tenant Isolation
- OWASP LLM Top 10

Important

- API Security
- Authentication
- SSRF
- Static Code Analysis

---

Achievements

Order

1.

HackAthena Winner

2.

200+ CTF Challenges

---

Summary Focus

- AI / LLM Security
- Prompt Injection
- Offensive Security Research
- Multi-tenant SaaS Security

---

Preferred Terminology

Use

- Exploited
- Identified
- Validated
- Assessed
- Crafted (for payload crafting)
- Traced (for attack chain tracing)

Avoid

- Dashboard
- Frontend

---

# ROLE

## API Security Engineer

Role Score

★★★★★

---

Experience

Entry 1 — Mindpex VAPT Freelance

★★★★★

Emphasize

- Enumeration of 61 Next.js API routes and 3 FastAPI Python service routers (ffuf, Nmap)
- SSRF via unvalidated URL parameter in webhook endpoint (confirmed OOB with interactsh)
- Broken Object-Level Authorization (BOLA) and authentication bypass across privileged admin routes
- SQL wildcard injection in admin delete handler enabling mass-deletion in a single authenticated request
- FastAPI services with zero authentication on all routes (confirmed via curl + Nmap port scan)
- Cross-tenant deletion possible by supplying foreign organization UUID
- Dead rate-limiting middleware finding — all perimeter controls completely inactive
- ilike wildcard enabling bulk employee record update (sqlmap parameter injection)

Suppress

- LLM/AI security detail (save for AI Security roles)
- RLS policy detail (save for Product Security roles)

Entry 2 — Epicor Software Internship

★★★★☆

Emphasize

- CI/CD pipeline knowledge as integration layer for API security tooling
- Automation scripting
- Linux execution environments

---

Project Selection

Score order for API Security (highest → lowest JD alignment):

1. Security Assessment
2. VigiLynx
3. CipherCrack

Slot 1 and Slot 2 get 3 bullets each. Slot 3 gets 2 bullets.

Security Assessment provides additional API security evidence — Burp Suite-based API request manipulation, parameter injection, authorization testing, and remediation design.
VigiLynx moves to Slot 1 only if JD emphasizes detection-side API monitoring.

---

Technical Skills

Critical

- Burp Suite
- Python
- ffuf
- Nmap
- interactsh

Important

- Linux
- JavaScript
- Node.js
- sqlmap
- curl

Useful

- SQL
- Wireshark

Suppress

- React
- Supabase
- PowerShell (unless scripting appears in JD)

---

Security Concepts

Critical

- API Security
- OWASP API Top 10
- BOLA / IDOR
- SSRF
- Authentication Bypass
- Rate Limiting
- REST Security
- Authorization Testing

Important

- SQL Injection
- Business Logic Testing
- Parameter Manipulation
- Enumeration

---

Achievements

Order

1.

HackAthena Winner

2.

200+ CTF Challenges

---

Summary Focus

- API Security
- Offensive Testing
- OWASP API Top 10
- Multi-tenant SaaS Vulnerability Research

---

Preferred Terminology

Use

- Enumerated
- Assessed
- Identified
- Exploited
- Validated
- Mapped

Avoid

- Dashboard
- Frontend
- QA

---

# ROLE

## Offensive Security Engineer

Role Score

★★★★★

---

Experience

Entry 1 — Mindpex VAPT Freelance

★★★★★

Emphasize

- SSRF exploitation via unvalidated webhook URL with OOB confirmation (interactsh)
- Account takeover via invitation flow forced password override — full privilege escalation chain
- SQL wildcard injection enabling mass-deletion in a single authenticated request
- Prompt injection on open LLM endpoint — raw input passed verbatim to model
- Cross-tenant deletion via foreign UUID injection
- Attack chain documentation with CVSS scoring
- Full-scope manual testing methodology (OWASP WSTG)

Suppress

- Audit logging gaps (save for Detection Engineering)
- RLS detail (save for Product Security)

Entry 2 — Epicor Software Internship

★★★★☆

Emphasize

- Linux
- Scripting (PowerShell, Bash)
- Automation
- CI/CD pipeline knowledge

Suppress

- QA terminology
- Regression

---

Project Selection

Score order for Offensive Security Engineer (highest → lowest JD alignment):

1. CipherCrack
2. Security Assessment
3. VigiLynx

Slot 1 and Slot 2 get 3 bullets each. Slot 3 gets 2 bullets.

CipherCrack is primary — demonstrates offensive tooling development and cryptanalysis automation.
Security Assessment may move to Slot 1 if JD explicitly emphasizes methodology and reporting over tooling.

---

Technical Skills

Critical

- Python
- Burp Suite
- ffuf
- Nmap
- Linux

Important

- Bash
- Metasploit
- CyberChef
- interactsh
- Gobuster
- Wireshark

Useful

- SQL
- PowerShell

Suppress

- React
- Supabase

---

Security Concepts

Critical

- Offensive Security
- Exploitation
- Reconnaissance
- Enumeration
- Cryptanalysis
- Web Security
- OWASP

Important

- Authentication Testing
- API Security
- Brute Force
- Automation

---

Achievements

Order

1.

200+ CTF Challenges

2.

KJSSE CTF Finalist (17th / 662)

3.

Top 10% TryHackMe

---

Summary Focus

- Offensive Security Engineering
- Security Tooling Development
- Exploitation and Cryptanalysis
- Practical Security Assessments

---

Preferred Terminology

Use

- Exploited
- Enumerated
- Assessed
- Identified
- Automated
- Developed (for tooling)

Avoid

- Monitored
- Dashboard
- QA

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

The layout is fixed. There is ONE layout for ALL roles.

Experience section: always Mindpex VAPT Freelance + Epicor Software (both, always).

Projects section: always all 3 projects — VigiLynx, CipherCrack, and Black-box Security Assessment.

Step 1: Score all 3 projects against the JD using the evaluation criteria below.

Step 2: Order them highest to lowest score.

Step 3: Assign bullets:
- Slot 1 (highest score): 3 bullets
- Slot 2 (second score):  3 bullets
- Slot 3 (lowest score):  2 bullets

Use the "Score order" guidance in each role's Project Selection block as the default starting rank. Override it if JD keywords shift the scores.

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

Epicor is always in Experience. Never place Epicor in a project slot.

Mindpex is always in Experience. Never place Mindpex in a project slot.

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