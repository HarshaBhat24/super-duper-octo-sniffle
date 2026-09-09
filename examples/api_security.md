# Example Resume
## Target Role

API Security Engineer

---

# Purpose

Reference resume for

- API Security Engineer
- API Penetration Tester
- REST Security Specialist
- Backend Security Engineer

This file defines the desired emphasis, terminology, ordering, and technical depth.

Do not copy bullets verbatim.

Generate new bullets from the knowledge base.

---

# Target Priorities

Highest Priority

- API Security
- OWASP API Top 10
- BOLA / IDOR
- SSRF
- Authentication Bypass
- Rate Limiting
- REST Security
- Authorization Testing

Medium Priority

- SQL Injection
- Business Logic Testing
- Parameter Manipulation
- Enumeration
- Web Application Security

Low Priority

- Frontend Development
- UI Development
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

- Enumeration of 61 Next.js API routes and 3 FastAPI Python service routers using ffuf and Nmap
- SSRF via unvalidated URL parameter in webhook endpoint (OOB confirmed with interactsh)
- BOLA and authentication bypass across privileged admin routes
- SQL wildcard injection in admin delete handler enabling full organization data wipe in a single request
- FastAPI services with zero authentication on all routes (confirmed via curl and Nmap port scan)
- Cross-tenant deletion via foreign UUID injection
- Dead rate-limiting middleware — all perimeter controls inactive

Example Bullet

Enumerated 61 Next.js API routes and 3 FastAPI service routers using ffuf and Nmap; identified SSRF via unvalidated webhook URL confirmed OOB with interactsh, and authentication bypass on privileged admin endpoints.

Example Bullet

Discovered SQL wildcard injection in admin delete handler enabling full organization data wipe in a single authenticated request; validated mass-deletion impact using sqlmap and delivered parameterized query remediation.

Example Bullet

Identified dead rate-limiting middleware misconfiguration in Next.js middleware chain — all perimeter controls (rate limiting, body size guard, suspicious path blocking) were completely inactive; FastAPI LLM endpoints also had zero rate limiting.

---

## Epicor Software

Focus

- Python/Locust load testing across multiple parallel Chrome instances
- ADO CI/CD pipelines (agent-VM architecture)
- SQL/SSMS queries for data validation
- Boundary testing and input validation under load

Suppress

- Pipeline-as-code / Jenkinsfile authoring as primary framing
- Azure Pipelines YAML authoring as primary framing

Star Bullet

Engineered a PowerShell cleanup script deployed across 5 agent VMs via automated ADO pipeline, clearing ~15 GB of logs and temp data weekly — eliminating pipeline failures caused by storage exhaustion.

Example Bullet

Authored Python/Locust load testing scripts exercising application API flows across multiple parallel Chrome instances under concurrent load, validating application behavior under sustained traffic.

Example Bullet

Created ADO CI/CD pipelines using agent-VM architecture; wrote SQL queries against SSMS-backed databases for test data validation and application state inspection under load test conditions.

---

# Security Assessment

Priority

★★★★★

Focus

- API enumeration and request manipulation
- Authentication and authorization testing
- Parameter injection
- BOLA / access control validation

Example Bullet

Performed an authorized black-box assessment of a SaaS web application targeting API security; enumerated endpoints with ffuf and Gobuster, then validated authentication, authorization, and parameter manipulation using Burp Suite.

Example Bullet

Identified Broken Object-Level Authorization through manual request manipulation, validating cross-user and cross-object access control weaknesses via direct API calls.

Example Bullet

Produced remediation guidance covering API authentication enforcement, BOLA prevention, rate limiting architecture, and secure CORS configuration.

---

# VigiLynx

Priority

★★★★☆

Focus

- API-based threat intelligence integration (VirusTotal)
- Security automation
- Browser-based threat detection

Example Bullet

Engineered a phishing detection pipeline integrating VirusTotal API analysis for real-time URL threat classification across 1,000+ analyzed URLs via a Chrome extension.

Example Bullet

Developed authenticated backend API services and dashboards for persistent threat logging, malware scan history, and user-specific security event monitoring.

---

# Skills

Security

- API Security
- OWASP API Top 10
- BOLA / IDOR
- SSRF
- Authentication Bypass
- Rate Limiting
- REST Security
- Penetration Testing

Programming

- Python
- JavaScript

Operating Systems

- Linux
- Windows

Tools

- Burp Suite
- ffuf
- Nmap
- interactsh
- sqlmap
- Locust
- SSMS
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

- API Security
- OWASP API Top 10
- BOLA
- IDOR
- SSRF
- Authentication Bypass
- Rate Limiting
- REST Security
- Burp Suite
- ffuf
- interactsh
- Locust
- SSMS
- Python
- Linux
- Penetration Testing

---

# Validation Checklist

✓ No Summary section

✓ Mindpex VAPT in Experience section (always)

✓ Domain 1 (API Security — 61 routes) is the primary focus of Mindpex bullets

✓ Epicor in Experience section (always)

✓ 2–3 dynamically selected project slots

✓ Certifications & Achievements merged into single section

✓ Locust load testing (parallel Chrome instances under load) framing in Epicor bullets

✓ No 'Jenkinsfile authoring' or 'pipeline-as-code' as primary Epicor framing

✓ SSRF finding explicitly covered

✓ BOLA / authentication bypass explicitly covered

✓ Rate limiting dead middleware finding covered

✓ SQL wildcard injection covered

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

API Security resumes should communicate the ability to

- Enumerate and map API attack surfaces
- Identify BOLA, SSRF, injection, and rate-limiting weaknesses
- Conduct manual API testing with Burp Suite and CLI tools
- Reason about REST authentication and authorization models
- Produce actionable remediation for API security findings

This role is distinct from general AppSec — the emphasis is specifically on API attack surfaces, not broad web application security.

Suppress generic software engineering terminology.
