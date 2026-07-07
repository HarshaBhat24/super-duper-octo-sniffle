# Cybersecurity Career Engine

A structured knowledge base and resume generation engine for producing highly tailored, ATS-optimized cybersecurity resumes.

This repository is designed for LLMs (ChatGPT, Claude, Gemini, etc.) and serves as the **single source of truth** for the candidate's experience, projects, technical skills, certifications, and achievements.

The objective is to generate truthful, role-specific resumes while maximizing alignment with a supplied Job Description.

---

# Repository Structure

```
career-engine/
│
├── knowledge-base/
│   ├── 01_candidate_profile.md
│   ├── 02_experience.md
│   ├── 03_projects.md
│   ├── 04_security_assessments.md
│   └── 05_achievements.md
│
├── engine/
│   ├── 01_resume_generation_rules.md
│   ├── 02_role_intelligence_matrix.md
│   └── 03_resume_budget.md
│
├── prompts/
│   └── master_resume_prompt.md
│
├── examples/
│   ├── appsec.md
│   ├── detection_engineer.md
│   ├── product_security.md
│   ├── redteam.md
│   └── soc.md
│
└── README.md
```

---

# Purpose

This repository is **not** a resume.

It is a structured knowledge base that allows an LLM to generate resumes, summaries, and role-specific content dynamically.

The repository separates

- Candidate knowledge
- Resume generation logic
- Role intelligence
- Formatting rules
- Reference examples

This prevents duplication and keeps all resume generations factually consistent.

---

# How to Use

## Required Input

Provide

1. Entire repository
2. Target Job Description

No additional context should be necessary.

---

## Files To Read

Always read **every file** before generating a resume.

Read in this order.

### Step 1

Read

```
knowledge-base/
```

These files contain all verified candidate information.

---

### Step 2

Read

```
engine/
```

These files define

- generation rules
- ATS optimization
- role selection
- formatting constraints

---

### Step 3

Read

```
examples/
```

These are reference resumes.

They define

- style
- emphasis
- terminology
- section ordering

Never copy them.

Only imitate their structure.

---

### Step 4

Read

```
prompts/master_resume_prompt.md
```

This is the orchestration prompt.

Follow it exactly.

---

# Resume Generation Workflow

```
Read Repository

↓

Read Job Description

↓

Identify Target Role

↓

Extract ATS Keywords

↓

Determine Resume Strategy

↓

Score Experiences

↓

Select Projects

↓

Rewrite Experience

↓

Generate Skills

↓

Generate Achievements

↓

Validate Resume Budget

↓

Perform Truth Validation

↓

Generate Resume

↓

Generate ATS Analysis
```

Never skip any step.

---

# Supported Roles

The engine currently supports

- Red Team Engineer
- Penetration Tester
- Application Security Engineer
- Product Security Engineer
- Detection Engineer
- Security Engineer
- Security Analyst (SOC)
- Threat Intelligence Analyst
- Security Research Engineer
- Purple Team

The generator should automatically determine the closest role from the supplied Job Description.

---

# Knowledge Base Rules

The knowledge base is the only trusted source.

Never invent

- experience
- responsibilities
- technologies
- metrics
- findings
- certifications
- projects
- achievements

Only rewrite existing information.

---

# Additional Uploaded Files

The user may upload additional files.

Examples

- Project documentation
- Security assessment reports
- GitHub README files
- Technical writeups
- Resume drafts
- Architecture documents
- Portfolio content
- Competition writeups
- Certifications

These files should be inspected before generating the resume.

If they contain verified information,

incorporate it naturally.

Never ignore uploaded files.

---

# Conflict Resolution

If two files disagree,

prefer

1. Newer information
2. More detailed information
3. Candidate knowledge base
4. Uploaded supporting documentation

Never guess.

---

# Confidentiality

Never expose

- company names
- internal domains
- confidential URLs
- credentials
- secrets
- proprietary implementations

Instead,

generalize while preserving

- technical concepts
- demonstrated skills
- engineering depth

---

# Resume Constraints

Always produce

Experience

- 3 bullets

Project 1

- 3 bullets

Project 2

- 3 bullets

Skills

- 12–18

Achievements

- Maximum 3

Certifications

- Maximum 2

Resume Length

- One Page

---

# Optimization Priorities

Priority order

1.

Truthfulness

↓

2.

Role Alignment

↓

3.

Technical Depth

↓

4.

ATS Optimization

↓

5.

Readability

↓

6.

Keyword Density

Never sacrifice factual accuracy for ATS optimization.

---

# Output Requirements

Every generated resume should

- Target a single cybersecurity role
- Be ATS optimized
- Fit on one page
- Use measurable achievements
- Prioritize security concepts
- Avoid generic software engineering terminology
- Demonstrate technical depth
- Remain completely truthful

---

# Supported Outputs

Using this repository, an LLM should be capable of generating

- ATS Resume
- Tailored Resume
- Resume Analysis
- ATS Score
- Keyword Gap Analysis
- Project Rewriting
- Experience Rewriting
- Skills Optimization
- Summary Generation
- Achievement Selection

---

# Future Expansion

The repository is designed to grow over time.

New files may include

- Additional Projects
- Certifications
- Professional Experience
- Research
- Security Assessments
- Conference Talks
- Open Source Contributions

The engine should automatically incorporate new knowledge while preserving existing behavior.

---

# Final Rule

Treat this repository as the authoritative source of truth.

Do not optimize by inventing information.

Optimize only through

- better wording
- better ordering
- stronger technical emphasis
- improved ATS alignment
- role-specific tailoring

The best resume is the one that is technically accurate, evidence-based, concise, and tailored to the target cybersecurity role.