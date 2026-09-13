# Resume Generation Engine

Version

1.0

Purpose

This document defines the rules that govern resume generation.

It should be used together with

- knowledge-base/01_candidate_profile.md
- knowledge-base/02_experience.md
- knowledge-base/03_projects.md
- knowledge-base/04_security_assessments.md
- knowledge-base/05_achievements.md
- knowledge-base/06_epicor_internship.md
- knowledge-base/07_mindpex_vapt.md

This file defines HOW resumes are generated.

Knowledge-base files define WHAT the candidate has done.

Never generate a resume without reading every knowledge-base file first.

---

# Primary Objective

Generate a one-page ATS-optimized cybersecurity resume that maximizes alignment with the supplied Job Description while remaining completely truthful.

The generator must optimize

- Summary
- Experience
- Projects
- Skills
- Achievements

The generator must NEVER invent

- Experience
- Metrics
- Responsibilities
- Findings
- Certifications
- Technologies
- Team size

---

# Resume Generation Pipeline

The authoritative pipeline is defined in `prompts/master_resume_prompt.md`.

This file (`engine/01_resume_generation_rules.md`) defines the **generation-specific rules** that the master pipeline delegates to:

- How to score experiences and projects (see Candidate Scoring and Project Scoring Rubric)
- How to write bullets (see Experience Rewriting Rules and Bullet Formula)
- How to generate skills (see Skills Generation Rules)
- How to generate achievements (see Achievement Rules)
- How to validate content (see Final Resume Validation)

Do not follow a separate pipeline from this file. Follow `prompts/master_resume_prompt.md` for orchestration.

---

# Job Description Analysis

Before generating anything, classify the Job Description.

Possible categories

- Red Team

- Penetration Testing

- Application Security

- Product Security

- Security Engineering

- DevSecOps

- Detection Engineering

- Threat Intelligence

- Security Research

- SOC

- AI / LLM Security

- API Security

- Offensive Security

If multiple roles are present,

rank them by keyword density.

---

# Keyword Extraction

Extract

Programming Languages

Security Tools

Security Concepts

Frameworks

Operating Systems

Cloud

Networking

Authentication

Authorization

Detection

Threat Intelligence

Threat Hunting

Security Operations

Web Security

DevSecOps

Cryptography

API Security

Product Security

Application Security

Offensive Security

Automation

CI/CD

Compliance

For every keyword,

calculate

High

Medium

Low

importance.

---

# Candidate Scoring

Score every experience and project.

Experience Entries

- Mindpex VAPT Freelance — primary security experience (07_mindpex_vapt.md)
- Epicor Software Internship — primary professional experience (06_epicor_internship.md)

Projects

- VigiLynx
- CipherCrack
- Black-box Security Assessment

Achievements

- HackAthena
- CTFs
- TryHackMe

Each receives a score. Highest scoring experiences become the resume.

---

# Experience Selection Rules

Epicor

Always include. Never remove.

Mindpex VAPT Freelance

Always include in the Experience section. There is no role-based switching.

Mindpex NEVER appears in Projects & Key Achievements — it is always in Experience.

Projects & Key Achievements

Always include all 3 projects: VigiLynx, CipherCrack, and Black-box Security Assessment.

Score all three against the JD and rank them. Order them highest to lowest JD alignment score.

Bullet allocation:
- Slot 1 (highest score): 3 bullets
- Slot 2 (second score):  3 bullets
- Slot 3 (lowest score):  2 bullets

Never drop a project or swap in achievements as a project substitute.

---

# Project Priority by Role

Application Security

1

Security Assessment

2

VigiLynx

---

Product Security

1

Security Assessment

2

VigiLynx

---

Red Team

1

Security Assessment

2

CipherCrack

---

Pentesting

1

Security Assessment

2

CipherCrack

---

Security Research

1

CipherCrack

2

Security Assessment

---

Detection Engineering

1

VigiLynx

2

CipherCrack

---

Threat Intelligence

1

VigiLynx

2

CipherCrack

---

SOC

1

VigiLynx

2

CipherCrack

---

Security Engineering

1

VigiLynx

2

Security Assessment

---

DevSecOps

1

VigiLynx

2

Security Assessment

---

AI / LLM Security

1

VigiLynx

2

Security Assessment

---

API Security

1

Security Assessment

2

VigiLynx

---

Offensive Security

1

CipherCrack

2

Security Assessment

---

# Project Scoring Rubric

Use these weights when choosing which projects to include.

| Criterion | Weight |
|---|---|
| Security relevance to JD role | 40% |
| Technical depth demonstrated | 25% |
| JD keyword match | 20% |
| ATS coverage potential | 10% |
| Verified metrics present | 5% |

Score all three candidates (VigiLynx, CipherCrack, Security Assessment) against this rubric.

Order them highest to lowest. Assign bullets: Slot 1 → 3, Slot 2 → 3, Slot 3 → 2.

# Experience Rewriting Rules

Do NOT copy resume bullets from the knowledge base.

Instead,

generate entirely new bullets.

Each bullet should emphasize

Security

↓

Implementation

↓

Impact

↓

Metrics

Avoid

Technology lists.

Prefer

Security concepts.

---

# Experience Bullet Formula

Every bullet follows

Action Verb

↓

Technical Implementation

↓

Security Concept

↓

Business / Technical Impact

Example

Implemented Random Forest-based phishing detection workflows to classify 1,000+ URLs and generate real-time browser alerts through a Chrome extension.

Not

Worked on phishing detection.

---

# Bullet Prioritization

Rank contributions using

1

Security relevance

2

Technical complexity

3

Business impact

4

Metrics

5

Technology names

Technology names should never be the primary focus.

---

# Resume Budget

Exactly

Experience (per entry)

3 bullets

Project Slot 1 (highest JD score)

3 bullets

Project Slot 2 (second JD score)

3 bullets

Project Slot 3 (lowest JD score)

2 bullets

Maximum

2 lines

per bullet.

Do not violate this rule.

---

# Compression Rules

If a project contains multiple related contributions,

merge them.

Bad

Built Chrome extension.

Implemented URL detection.

Added alerts.

Good

Developed a Chrome extension that performed real-time URL analysis using Random Forest detection and generated phishing alerts.

Always compress before removing information.

---

# Metrics Rules

Metrics strengthen bullets.

Use them whenever verified.

Examples

1000+ URLs

50+ files

200+ CTFs

9 algorithms (CipherCrack)

10+ CTF competitions (CipherCrack)

17 / 662

Top 10%

200+ Participants

Never estimate.

Never invent.

If no metric exists,

omit the metric.

---

# Action Verbs

Prefer

Implemented

Engineered

Developed

Designed

Built

Integrated

Automated

Validated

Analyzed

Discovered

Assessed

Identified

Documented

Avoid

Worked on

Helped

Participated

Responsible for

Assisted with
---

# Summary Generation Rules

Do NOT generate a Summary section.

The Summary section has been permanently removed from the resume format.

The space freed by removing the Summary is used to accommodate more project/achievement entries in the Projects & Key Achievements section.

---

# Skills Generation Rules

Generate dynamic skills.

Never copy the static skills list.

Skills must be selected after analyzing

- Role
- Technologies
- Security concepts
- Required tools

---

Skills Count

Minimum

12

Maximum

18

---

Group Skills

Programming

Security

Operating Systems

Networking

Tools

Development

Do not create more than six categories.

---

Programming Priority

Python

Highest

TypeScript

High

JavaScript

High

Bash

Medium

C

Medium

PowerShell

Medium

SQL

Medium

---

Tool Selection

Only include tools relevant to the JD.

Example

SOC

Include

- Wireshark
- Linux
- TCP/IP

Remove

- Gobuster

---

Red Team

Include

- Burp Suite
- ffuf
- Gobuster
- Nmap
- Metasploit

Suppress

- React

---

Application Security

Include

- Burp Suite
- JWT
- API Security
- Authentication
- Authorization

---

Threat Intelligence

Include

- VirusTotal
- Malware Analysis
- Threat Detection

---

Detection Engineering

Include

- PowerShell
- Python
- VirusTotal
- Automation

---

# Skill Prioritization

Rank every skill

Critical

Important

Useful

Remove Useful skills first if space is limited.

---

# Achievement Generation Rules

Achievements appear in the **Certifications & Achievements** section (compact list, no sub-bullets).

Maximum 3 achievements.

Dynamically order based on target role using priority tables in 05_achievements.md.

Format: one line per achievement, including result and context.

Example: `Winner — HackAthena'25 Cybersecurity Track (National Hackathon, 200+ teams)`

Prefer measurable results (placements, rankings, participant counts).

Never exceed 3 achievements regardless of role.

Examples

Red Team

- KJSSE CTF
- TryHackMe
- 200+ CTFs

---

Product Security

- HackAthena
- Smart India Hackathon
- CTF Experience

---

Detection Engineering

- HackAthena
- TryHackMe
- CTF Experience

---

SOC

- CompTIA Security+
- HackAthena
- CTF Experience

---

Achievement Format

Achievement

↓

Evidence

↓

Impact

Avoid writing full sentences.

---

# Certification Rules

Maximum

2

Always order

1

CompTIA Security+

2

ISC2 Certified in Cybersecurity (CC)

Never include additional certifications unless specifically requested.

---

# ATS Optimization Rules

Extract every important keyword.

Categories

Programming

Security

Networking

Cloud

Authentication

Authorization

OWASP

Threat Detection

Cryptography

Malware

Endpoint Security

Web Security

Application Security

Product Security

Detection Engineering

DevSecOps

Automation

Operating Systems

Databases

CI/CD

---

Keyword Usage

Each important keyword should appear naturally.

Never keyword stuff.

Avoid repeating the same keyword more than twice.

Use synonyms when appropriate.

---

Keyword Matching Priority

Exact Match

↓

Equivalent Security Term

↓

Related Technical Concept

Example

JD

Access Control

Resume

Authorization

Identity Validation

Authentication

---

# Security Terminology Rules

Always prefer security terminology.

Example

Instead of

Backend

Prefer

Secure Backend Services

---

Instead of

Database

Prefer

Security Data Store

ONLY if technically accurate.

---

Instead of

Testing

Prefer

Security Validation

ONLY if supported by evidence.

---

# Resume Language

Preferred

Engineered

Implemented

Validated

Developed

Analyzed

Automated

Integrated

Assessed

Documented

Discovered

Avoid

Worked on

Responsible for

Helped

Participated

Contributed to

Exposure to

---

# Quantification Rules

Always include metrics when verified.

Examples

1000+ URLs

50+ Files

9 algorithms (CipherCrack)

10+ CTF competitions (CipherCrack)

200+ CTFs

Top 10%

17/662

200+ Participants

Do not invent metrics.

Do not estimate.

Do not extrapolate.

---

# Technical Depth

Every bullet should answer

What?

How?

Why?

Impact?

Poor

Implemented authentication.

Good

Implemented authentication workflows and backend integration to secure user access across browser extension and web application components.

---

# Cybersecurity First Principle

Whenever two equivalent descriptions exist,

choose the one emphasizing cybersecurity.

Example

Bad

Built a dashboard.

Good

Developed a threat visualization dashboard for monitoring phishing detections and malware scan history.

---

# Resume Consistency Rules

Every section must reinforce the same target role.

Do not mix priorities.

Example

If targeting Red Team

Projects

Red Team

Skills

Red Team

Achievements

Red Team

Summary

Red Team

Do not generate a SOC summary with Red Team projects.

---

# Section Ordering

Header

↓

Experience

↓

Projects

↓

Skills

↓

Certifications & Achievements

↓

Education

No Summary section.

No separate Achievements section — achievements are merged with Certifications into the compact 'Certifications & Achievements' section.

No additional sections unless explicitly requested.

---

# Truth Guard

Truthfulness is mandatory.

The resume generator may

- Rewrite
- Reorder
- Compress
- Merge related work
- Improve wording
- Improve ATS alignment

The resume generator may NEVER

- Invent technologies
- Invent experience
- Invent vulnerabilities
- Invent responsibilities
- Invent team size
- Invent metrics
- Invent certifications
- Invent achievements
- Invent leadership
- Invent security findings
- Invent production responsibilities

If evidence is unavailable,

omit the information.

Never guess.

---

# Evidence Hierarchy

Every generated statement must originate from the knowledge base.

Evidence Priority

★★★★★

Direct implementation

Examples

- Built Chrome Extension
- Implemented Random Forest detection
- Performed penetration testing
- Wrote assessment report

★★★★☆

Primary contribution

Examples

- Backend integration
- Authentication
- Dashboard implementation

★★★☆☆

Exposure

Examples

- Azure DevOps
- Jenkins
- SQL

★★☆☆☆

General familiarity

Should only appear in Skills.

★☆☆☆☆

Do not generate resume bullets.

---

# Role Alignment Engine

Every resume must represent ONE primary role.

If multiple roles exist,

choose the highest scoring role.

Everything should align with that role.

This includes

- Experience bullets (Mindpex + Epicor)
- Projects & Key Achievements selection and framing
- Skills ordering
- Certifications ordering

Never generate mixed-role resumes.

---

# Red Team Rules

Primary Focus

- Offensive Security
- Manual Testing
- Enumeration
- Exploitation
- Cryptanalysis
- Reconnaissance
- Burp Suite
- ffuf
- Gobuster
- Nmap

Projects

1. Security Assessment

2. CipherCrack

Suppress

- React
- Dashboard UI
- Frontend

Preferred Words

- Enumerated
- Assessed
- Validated
- Exploited
- Analyzed
- Identified

---

# Product Security Rules

Primary Focus

- Authentication
- Authorization
- Secure Design
- Threat Modeling
- API Security
- Browser Security

Projects

1. Security Assessment

2. VigiLynx

Suppress

- Cryptography implementation details
- UI development

Preferred Words

- Engineered
- Secured
- Designed
- Validated
- Integrated

---

# Application Security Rules

Primary Focus

- Authentication
- Authorization
- Input Validation
- Business Logic
- OWASP
- Secure Backend

Projects

1. Security Assessment

2. VigiLynx

Suppress

- Generic frontend implementation

---

# Detection Engineering Rules

Primary Focus

- Detection Logic
- Automation
- Threat Detection
- VirusTotal
- PowerShell
- Feature Extraction

Projects

1. VigiLynx

2. CipherCrack

Suppress

- React
- Generic CLI implementation

---

# Threat Intelligence Rules

Primary Focus

- VirusTotal
- Malware Analysis
- IOC Validation
- Threat Visibility
- Detection Pipeline

Projects

1. VigiLynx

2. CipherCrack

Suppress

- Matrix mathematics
- Frontend implementation

---

# SOC Rules

Primary Focus

- Threat Monitoring
- Malware Detection
- Log Analysis
- Linux
- Detection

Projects

1. VigiLynx

2. CipherCrack

Experience

Emphasize

- Log analysis
- PowerShell
- Linux

Suppress

- React

---

# Security Research Rules

Primary Focus

- Cryptography
- Security Tooling
- Technical Research
- Vulnerability Analysis

Projects

1. CipherCrack

2. Security Assessment

Suppress

- Dashboard implementation

---

# Bullet Quality Checklist

Every generated bullet should satisfy

✓ Strong action verb

✓ Technical implementation

✓ Security concept

✓ Impact

✓ Verified metric (if available)

Reject bullets missing two or more items.

---

# Resume Quality Score

Before returning the resume,

internally evaluate

Security Relevance

0–10

ATS Alignment

0–10

Technical Depth

0–10

Truthfulness

0–10

Impact

0–10

Overall

0–50

Target

45+

If below 45,

rewrite before returning.

---

# Resume Budget Validation

Validate

Experience Entry 1 (Mindpex)

Exactly 3 bullets

Experience Entry 2 (Epicor)

Exactly 3 bullets

Projects & Key Achievements

Exactly 3 entries, ordered by JD alignment score
- Slot 1 (highest): exactly 3 bullets
- Slot 2 (second):  exactly 3 bullets
- Slot 3 (lowest):  exactly 2 bullets

Skills

12–15

Certifications

Exactly 2

No Summary section

Resume

One page

Reject output that violates these limits.

---

# Hallucination Prevention

Never infer

- SIEM experience
- EDR experience
- Splunk
- Sentinel
- QRadar
- CrowdStrike
- Defender XDR
- Kubernetes
- Docker
- AWS Security
- Azure Security
- GCP Security
- Incident Response
- Threat Hunting
- Reverse Engineering
- Malware Development
- Bug Bounty
- CVEs

unless explicitly documented in the knowledge base.

---

# Knowledge Base Priority

When conflicts exist,

use this order

1. Candidate Profile

2. Experience

3. Security Assessments

4. Projects

5. Achievements

Ignore contradictory assumptions.

---

# Resume Style Guide

Tone

Professional

Technical

Concise

Evidence-driven

Avoid

Marketing language

Buzzwords

Filler

Opinion

First-person writing

Passive voice

Every bullet should read like an engineering accomplishment rather than a job responsibility.

---

# Final Validation Checklist

Before producing the final resume, verify that:

- The resume targets a single cybersecurity role.
- Mindpex VAPT is in the Experience section (not in Projects).
- Epicor is in the Experience section.
- Each experience has exactly 3 bullets.
- Projects & Key Achievements has exactly 3 entries, ordered by JD alignment score.
  - Slot 1 (highest): exactly 3 bullets.
  - Slot 2 (second):  exactly 3 bullets.
  - Slot 3 (lowest):  exactly 2 bullets.
- No Summary section is present.
- Skills are tailored to the JD (12–15 items).
- CompTIA Security+ and ISC2 CC are included.
- ATS keywords are naturally integrated.
- No unsupported claims exist.
- No confidential information is disclosed (Mindpex described as "Freelance VAPT Engagement — Enterprise SaaS Platform").
- The resume fits on one page.
- Every statement is backed by the knowledge base.
- Epicor VM cleanup PowerShell script bullet is present unless a stronger JD-aligned bullet replaces it.

If any check fails, regenerate the affected section before returning the resume.

---

# End of Resume Generation Engine