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

## Epicor Software

Focus

- PowerShell scripting and automation
- VM environment knowledge (agent-VM ADO pipelines)
- Linux systems
- Automation

Suppress

- QA terminology
- Regression
- Pipeline-as-code / Jenkinsfile authoring as primary framing

Star Bullet

Engineered a PowerShell cleanup script deployed across 5 agent VMs via automated ADO pipeline, clearing ~15 GB of logs and temp data weekly — eliminating pipeline failures caused by storage exhaustion.

Example Bullet

Developed PowerShell automation scripts for agent-VM environment provisioning within ADO pipelines; applied scripting and automation skills across Linux-based enterprise execution environments.

Example Bullet

Worked with ADO pipelines, Linux systems, and SQL-backed environments across enterprise delivery cycles; gained practical understanding of agent-VM architecture and pipeline execution models.

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

Developed an offline Python-based cryptanalysis toolkit implementing 9 classical cipher algorithms with automated brute-force workflows; used across 10+ CTF competitions to accelerate cryptanalysis.

Example Bullet

Implemented modular cryptographic algorithms including Hill, Affine, Vigenère, and Four-Square ciphers using modular arithmetic and matrix operations, enabling rapid offline analysis during offensive competitions.

Example Bullet

Designed reusable CLI architecture enabling independent cipher invocation, reducing repetitive manual effort during offensive security competitions.

---

# Security Assessment

Priority

★★★★☆

Focus

- Black-box web application testing
- Authentication and authorization validation
- Enumeration and parameter manipulation
- Exploitation of BOLA / access control weaknesses

Example Bullet

Performed an authorized black-box assessment of a SaaS application targeting authentication, authorization, and API security; enumerated endpoints with ffuf and validated access-control weaknesses using Burp Suite.

Example Bullet

Identified Broken Object-Level Authorization through manual request manipulation and validated cross-user access control weaknesses via direct API calls.

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

---

# Certifications & Achievements

Certifications

1.

CompTIA Security+

2.

ISC2 Certified in Cybersecurity (CC)

Achievements

1.

Finalist — KJSSE CTF 2.0 (17th of 662 teams)

2.

Solved 200+ CTF challenges across web exploitation, cryptography, and digital forensics

3.

Top 10% TryHackMe

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
- PowerShell
- Linux
- SSRF
- OWASP
- Security Tooling

---

# Validation Checklist

✓ No Summary section

✓ Mindpex VAPT in Experience section (always)

✓ Exploitation chain (SSRF, account takeover, SQL wildcard) explicitly covered

✓ Epicor in Experience section (always)

✓ 2–3 dynamically selected project slots

✓ Certifications & Achievements merged into single section

✓ PowerShell scripting + VM environment knowledge framing in Epicor bullets

✓ No 'Jenkinsfile authoring' or 'pipeline-as-code' as primary Epicor framing

✓ Offensive tooling framing in CipherCrack bullets

✓ Tool-building language used (Developed, Implemented, Designed)

✓ CTF experience prioritized — KJSSE CTF 17/662 included

✓ 200+ CTF challenges included

✓ TryHackMe Top 10% included

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
