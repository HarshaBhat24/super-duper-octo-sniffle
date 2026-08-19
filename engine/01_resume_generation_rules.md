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

- Detection Engineering

- Threat Intelligence

- Security Research

- SOC

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

Include in Experience section when JD targets: AppSec, ProdSec, Red Team, Pentesting, DevSecOps, Security Engineering.

For all other roles: Mindpex occupies one project slot.

Never appear in both Experience and Projects simultaneously.

Projects

Choose ONLY the number of project slots determined by the Experience Structure Decision:

- 2 experience entries → 1 project slot
- 1 experience entry → 2 project slots (one may be Mindpex)

Never include all three projects (VigiLynx + CipherCrack + Security Assessment).

---

# Experience Priority

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

Select the top-scoring entries up to the project slot limit.

Never select based on personal preference or default habits.

Note: When Mindpex is in the project slot (non-AppSec/ProdSec/RedTeam roles), it automatically occupies one slot and is scored as primary. The second slot is chosen from the remaining two projects using the rubric above.

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

Experience

3 bullets

Project 1

3 bullets

Project 2

3 bullets

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

150+ CTFs

1324 LOC

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

The summary is optional.

Generate a summary ONLY IF

- It increases alignment with the Job Description.
- It fits within the one-page budget.
- It does not replace stronger technical content.

Otherwise

Do not generate a summary.

---

Summary Length

2–3 lines

Maximum

60 words

---

Summary Priority

Every summary should communicate

1

Current career focus

↓

2

Technical strengths

↓

3

Certifications

↓

4

Competitive cybersecurity experience

---

Always Mention

If a summary is generated,

include

- CompTIA Security+
- ISC2 Certified in Cybersecurity (CC)

unless explicitly irrelevant.

---

Example Structure

CompTIA Security+ and ISC2 Certified cybersecurity professional with hands-on experience in offensive security, phishing detection, and web application security. Developed practical security tooling, performed authorized security assessments, and solved 150+ CTF challenges while ranking in the Top 10% on TryHackMe.

---

Never Mention

- Passionate learner
- Highly motivated
- Fast learner
- Hardworking
- Team player
- Excellent communication

Demonstrate these through evidence.

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

Maximum

3 achievements

Never exceed.

---

Choose achievements based on the target role.

Examples

Red Team

- KJSSE CTF
- TryHackMe
- 150+ CTFs

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

1324 LOC

150+ CTFs

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

Summary (Optional)

↓

Experience

↓

Projects / Security Assessment

↓

Skills

↓

Certifications

↓

Achievements

↓

Education

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

- Summary
- Internship
- Projects
- Skills
- Achievements

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

Experience

Exactly 3 bullets

Project / Assessment 1

Exactly 3 bullets

Project / Assessment 2

Exactly 3 bullets

Skills

12–18

Achievements

≤3

Certifications

Exactly 2

Summary

Optional

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
- Epicor experience is included.
- Exactly two projects/assessments are selected.
- Bullet counts match the resume budget.
- Skills are tailored to the JD.
- CompTIA Security+ and ISC2 CC are included.
- Achievements are reordered for the role.
- ATS keywords are naturally integrated.
- No unsupported claims exist.
- No confidential information is disclosed.
- The resume fits on one page.
- Every statement is backed by the knowledge base.

If any check fails, regenerate the affected section before returning the resume.

---

# End of Resume Generation Engine