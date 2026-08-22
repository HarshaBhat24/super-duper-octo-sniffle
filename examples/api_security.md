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

Summary

↓

Experience (Mindpex + Epicor — both in Experience section)

↓

Security Assessment

↓

Skills

↓

Certifications

↓

Achievements

↓

Education

Note: Layout A. Two experience entries, 1 project slot (Security Assessment). Mindpex Domain 1 (API Security — 61+ routes) is the primary evidence anchor.

---

# Summary Style

Characteristics

- API-focused, offensive methodology
- Technical and tool-precise
- Concise

Example

CompTIA Security+ and ISC2 Certified in Cybersecurity (CC) professional with hands-on experience enumerating 61+ API routes and identifying SSRF, BOLA, SQL wildcard injection, and authentication bypass vulnerabilities across a multi-tenant SaaS platform. Conducted an authorized black-box assessment using Burp Suite, ffuf, interactsh, and sqlmap; delivered code-level remediation in TypeScript, Python, and SQL.

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

## Epicor Software Internship

Focus

- CI/CD pipeline as API security integration layer
- Automation scripting
- Linux execution environments

Example Bullet

Authored Jenkinsfile and Azure Pipelines YAML definitions for enterprise CI/CD pipelines, providing the integration layer for security tooling including SAST, DAST, and API vulnerability scanning.

Example Bullet

Developed PowerShell automation for build and test environment provisioning; performed log-based root cause analysis for pipeline failures across Linux environments.

Example Bullet

Led Jenkins to Azure DevOps pipeline migration, mapping build stages, triggers, and execution parameters while maintaining workflow continuity.

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
- Python
- Linux
- Penetration Testing

---

# Validation Checklist

✓ Mindpex VAPT in Experience section (Layout A)

✓ Domain 1 (API Security — 61 routes) is the primary focus of Mindpex bullets

✓ Epicor in Experience section

✓ Security Assessment as sole project slot

✓ SSRF finding explicitly covered

✓ BOLA / authentication bypass explicitly covered

✓ Rate limiting dead middleware finding covered

✓ SQL wildcard injection covered

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

API Security resumes should communicate the ability to

- Enumerate and map API attack surfaces
- Identify BOLA, SSRF, injection, and rate-limiting weaknesses
- Conduct manual API testing with Burp Suite and CLI tools
- Reason about REST authentication and authorization models
- Produce actionable remediation for API security findings

This role is distinct from general AppSec — the emphasis is specifically on API attack surfaces, not broad web application security.

Suppress generic software engineering terminology.
