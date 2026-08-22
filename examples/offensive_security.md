# Example Resume
## Target Role

Offensive Security Engineer

---

# Purpose

Reference resume for

- Offensive Security Engineer
- Security Tool Developer
- Exploit Developer
- Offensive Security Researcher

This role is distinct from Red Team Engineer in framing:

- Red Team → simulation, adversary emulation, campaign thinking
- Offensive Security Engineer → tool building, exploitation methodology, automated offensive workflows

CipherCrack is the primary anchor for tool-building credibility alongside the Mindpex VAPT exploitation chain.

Do not copy bullets verbatim.

Generate new bullets from the knowledge base.

---

# Target Priorities

Highest Priority

- Offensive Security
- Security Tooling Development
- Exploitation
- Cryptanalysis
- Reconnaissance
- Enumeration
- Automation

Medium Priority

- Authentication Testing
- API Security
- Web Security
- Brute Force

Low Priority

- Frontend Development
- UI Development
- Generic Software Engineering

---

# Section Order

Header

↓

Summary

↓

Experience (Mindpex + Epicor — both in Experience section)

↓

CipherCrack

↓

Skills

↓

Certifications

↓

Achievements

↓

Education

Note: Layout A. Two experience entries, 1 project slot (CipherCrack). CipherCrack anchors offensive tooling credibility.

---

# Summary Style

Characteristics

- Tool-building and exploitation focused
- Technical and evidence-driven
- Concise

Example

CompTIA Security+ and ISC2 Certified in Cybersecurity (CC) offensive security professional with hands-on experience exploiting SSRF, account takeover, SQL wildcard injection, and prompt injection across a multi-tenant SaaS platform. Developed a Python-based cryptanalysis toolkit used across 10–20 CTF competitions, solved 150+ CTF challenges, and ranked Top 10% on TryHackMe through consistent offensive security practice.

---

# Experience

## Mindpex VAPT Freelance

Label on resume: Freelance VAPT Engagement — Enterprise SaaS Platform

Focus

- SSRF exploitation via unvalidated webhook URL with OOB confirmation (interactsh)
- Account takeover via invitation flow forced password override — full privilege escalation chain documented
- SQL wildcard injection enabling full organization data wipe in a single authenticated request
- Prompt injection on open LLM endpoint — raw input passed verbatim to model
- Cross-tenant deletion via foreign UUID injection
- Attack chain documentation with CVSS scoring
- Manual testing methodology (OWASP WSTG)

Example Bullet

Exploited SSRF via unvalidated webhook URL to demonstrate internal network access; confirmed OOB callback using interactsh and delivered full attack chain with CVSS-scored findings and TypeScript remediation.

Example Bullet

Discovered privilege escalation via invitation flow forced password override, tracing attack path from low-privilege invite to full account takeover on any target email; identified cross-tenant deletion via foreign UUID injection.

Example Bullet

Identified SQL wildcard injection in admin delete handler enabling full organization data wipe in a single authenticated request; crafted and validated mass-deletion payload and delivered SQL-level remediation.

---

## Epicor Software Internship

Focus

- Linux
- Scripting (PowerShell, Bash)
- Automation
- CI/CD pipeline knowledge

Suppress

- QA terminology
- Regression

Example Bullet

Developed PowerShell and Batch automation scripts for build and environment provisioning across Linux-based CI/CD execution environments; performed log-based root cause analysis for pipeline failures.

Example Bullet

Authored Jenkinsfile and Azure Pipelines YAML definitions for enterprise CI/CD pipelines; led Jenkins to Azure DevOps migration mapping build stages, triggers, and environment parameters.

Example Bullet

Worked with Linux systems, Azure DevOps, SQL-backed environments, and Jenkins pipelines across enterprise software delivery cycles.

---

# CipherCrack

Priority

★★★★★

Focus

- Offensive tooling development
- Cryptanalysis automation
- Brute force workflows
- Python security scripting

Suppress

- Educational project framing
- Generic Python learning

Example Bullet

Developed an offline Python-based cryptanalysis toolkit implementing 9 classical cipher algorithms with automated brute-force workflows; used across 10–20 CTF competitions to accelerate cryptanalysis (1,324+ LOC).

Example Bullet

Implemented modular cryptographic algorithms including Hill, Affine, Vigenère, and Four-Square ciphers using modular arithmetic and matrix operations, enabling rapid offline analysis during offensive competitions.

Example Bullet

Designed reusable CLI architecture enabling independent cipher invocation, reducing repetitive manual effort during offensive security competitions.

---

# Skills

Security

- Offensive Security
- Exploitation
- Reconnaissance
- Enumeration
- Cryptanalysis
- Web Security
- OWASP

Programming

- Python
- Bash
- PowerShell

Operating Systems

- Linux (Kali, Ubuntu)
- Windows

Tools

- Burp Suite
- ffuf
- Nmap
- interactsh
- Metasploit
- CyberChef

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

Solved 150+ CTF challenges across web exploitation, cryptography, and digital forensics

2.

Finalist — KJSSE CTF 2.0 (17th of 662 teams)

---

# Education

Bachelor of Engineering

Information Science and Engineering

CGPA

8.57

---

# ATS Keywords

Highest Priority

- Offensive Security
- Penetration Testing
- Exploitation
- Cryptanalysis
- Reconnaissance
- Enumeration
- Burp Suite
- Python
- Linux
- SSRF
- OWASP
- Security Tooling

---

# Validation Checklist

✓ Mindpex VAPT in Experience section (Layout A)

✓ Exploitation chain (SSRF, account takeover, SQL wildcard) explicitly covered

✓ Epicor in Experience section (Linux, scripting, automation framing)

✓ CipherCrack as sole project slot

✓ Security Assessment excluded (covered by Mindpex in Experience)

✓ Offensive tooling framing in CipherCrack bullets

✓ Tool-building language used (Developed, Implemented, Designed)

✓ 12–15 skills (Layout A cap)

✓ Max 2 achievements (Layout A cap)

✓ CTF experience prioritized over HackAthena for this role

✓ CompTIA Security+ included

✓ ISC2 CC included

✓ Three bullets per section

✓ One-page resume

✓ No fabricated information

✓ Mindpex described as "Freelance VAPT Engagement — Enterprise SaaS Platform"

---

# Reference Notes

Offensive Security Engineer resumes should communicate the ability to

- Build and maintain offensive security tooling
- Conduct manual exploitation and attack chain analysis
- Automate offensive workflows (brute force, enumeration, payload delivery)
- Apply cryptanalysis and mathematical security concepts
- Document findings with CVSS scoring and remediation

This role is distinct from Red Team in that the framing is engineering-first: building tools and automating offensive workflows, not campaign simulation.

Suppress monitoring, detection, and defensive framing entirely.
