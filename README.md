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
│   ├── 00_changelog.md               # KB update log — track new skills, certs, projects
│   ├── 01_candidate_profile.md       # Master profile, skills, tools, Truth Guard
│   ├── 02_experience.md              # Experience index, Layout A/B decision, role pairing table
│   ├── 03_projects.md                # VigiLynx + CipherCrack project KB
│   ├── 04_security_assessments.md    # Black-box web app security assessment KB
│   ├── 05_achievements.md            # Achievements, certifications, role-ordered priority
│   ├── 06_epicor_internship.md       # Epicor internship KB (CI/CD, automation, Linux)
│   └── 07_mindpex_vapt.md            # Mindpex VAPT freelance KB (7-domain security assessment)
│
├── engine/
│   ├── 01_resume_generation_rules.md # Scoring, bullet rules, ATS, Truth Guard, validation
│   ├── 02_role_intelligence_matrix.md# Per-role emphasis, skills ordering, terminology
│   ├── 03_resume_budget.md           # Layout A/B budgets, bullet counts, space constraints
│   └── 04_company_intelligence.md    # Company type classification and tone modifiers
│
├── prompts/
│   └── master_resume_prompt.md       # Orchestration prompt — the 17-step generation pipeline
│
├── examples/
│   ├── appsec.md                     # Layout A — Application Security Engineer
│   ├── product_security.md           # Layout A — Product Security Engineer
│   ├── redteam.md                    # Layout A — Red Team Engineer
│   ├── devsecops.md                  # Layout A — DevSecOps Engineer
│   ├── security_engineering.md       # Layout A — Security Engineer
│   ├── ai_llm_security.md            # Layout A — AI / LLM Security Engineer
│   ├── api_security.md               # Layout A — API Security Engineer
│   ├── offensive_security.md         # Layout A — Offensive Security Engineer
│   ├── detection_engineer.md         # Layout B — Detection Engineer
│   └── soc.md                        # Layout B — SOC Analyst
│
├── outputs/
│   └── log.md                        # Resume version tracking log
│
└── README.md
```

---

# Purpose

This repository is **not** a resume.

It is a structured knowledge base that allows an LLM to generate resumes, summaries, and role-specific content dynamically.

The repository separates

- Candidate knowledge (knowledge-base/)
- Resume generation logic (engine/)
- Role intelligence (engine/02_role_intelligence_matrix.md)
- Formatting constraints (engine/03_resume_budget.md)
- Company tone modifiers (engine/04_company_intelligence.md)
- Reference examples (examples/)

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
- company tone modifiers

---

### Step 3

Read the example file matching the classified role from

```
examples/
```

These are reference resumes.

They define

- section order
- style and emphasis
- terminology
- bullet framing
- skills ordering

Never copy them verbatim.

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
Read Repository (KB + Engine + matching example)

↓

Read Job Description

↓

Company Intelligence — Classify company type; apply tone modifier; output Company Intelligence Report

↓

Gap Analysis — Tag each JD requirement as COVERED / PARTIAL / MISSING

↓

Consolidated MCQ Q&A:
  — MISSING tool/tech: present MCQ with exact JD tool + 2–3 alternatives + None option
  — MISSING concept: A) Yes (describe below) / B) No
  — PARTIAL depth: MCQ with granularity levels
  Wait for candidate response before proceeding.

↓

Incorporate Candidate Answers

↓

Role Classification Report — Score all 14 roles; output top 3 with confidence %; ask candidate to confirm

↓

Experience Structure Decision — Determine Layout A or Layout B from confirmed role

↓

Extract ATS Keywords

↓

Score Experiences and Projects

↓

Select Experiences and Projects per Layout Decision

↓

Rewrite Experience Bullets (3 per entry, max 2 lines each)

↓

Generate Skills (12–15 for Layout A; 12–18 for Layout B)

↓

Generate Achievements (max 2 for Layout A; max 3 for Layout B)

↓

Validate Resume Budget (one page, all counts verified)

↓

Perform Truth Validation (no invented claims)

↓

Generate Draft Resume — present to candidate

↓

Iterative Refinement Loop — targeted section rewrites; repeat until 'approve' (max 3 rounds)

↓

Generate Final Resume

↓

ATS Analysis

↓

Competing Candidate Benchmark — 5 items tagged YOU HAVE IT / YOU'RE CLOSE / GAP TO BUILD + Priority Gap advice
```

Never skip any step.

---

# Supported Roles

The engine currently supports **14 roles** across two layout types.

## Layout A — Two Experience Entries (Mindpex + Epicor in Experience; 1 project slot)

| Role | Primary Evidence Anchor | Default Project |
|---|---|---|
| Application Security Engineer | Mindpex Domain 1–7 (full-scope VAPT) | Security Assessment |
| Product Security Engineer | Mindpex Domain 1–7 + RLS analysis | Security Assessment |
| Red Team Engineer | Mindpex exploitation chain + CTFs | CipherCrack |
| Penetration Tester | Mindpex SSRF, ATO, wildcard injection | CipherCrack or Security Assessment |
| DevSecOps Engineer | Epicor CI/CD + Mindpex VAPT as security gate | VigiLynx |
| Security Engineer | Mindpex multi-domain + Epicor automation | VigiLynx |
| AI / LLM Security Engineer | Mindpex Domain 2 (prompt injection, memory poisoning, LLM trust boundaries) | VigiLynx |
| API Security Engineer | Mindpex Domain 1 (61 API routes, SSRF, BOLA, rate limiting, zero-auth FastAPI) | Security Assessment |
| Offensive Security Engineer | CipherCrack (9-cipher toolkit, 1,324+ LOC) + Mindpex exploitation chain | CipherCrack |

## Layout B — One Experience Entry (Epicor only in Experience; 2 project slots)

| Role | Slot 1 (Fixed) | Slot 2 |
|---|---|---|
| Detection Engineer | Mindpex VAPT | VigiLynx |
| SOC Analyst | Mindpex VAPT | VigiLynx |
| Threat Intelligence Analyst | Mindpex VAPT | VigiLynx |
| Security Research Engineer | Mindpex VAPT | CipherCrack |
| Purple Team | Mindpex VAPT | VigiLynx or Security Assessment |

The generator automatically determines the closest role from the supplied Job Description.

---

# Layout Rules

## Layout A (9 roles)

Triggers when JD targets: AppSec, ProdSec, Red Team, Pentesting, DevSecOps, Security Engineering, AI/LLM Security, API Security, Offensive Security

- Experience: Mindpex VAPT + Epicor (both in Experience section)
- Projects: 1 slot (choose from VigiLynx / CipherCrack / Security Assessment per role matrix)
- Skills: 12–15 items
- Achievements: max 2
- Certifications: exactly 2 (CompTIA Security+, ISC2 CC)

## Layout B (5 roles)

Triggers when JD targets: Detection Engineering, SOC, Threat Intelligence, Security Research, Purple Team

- Experience: Epicor only (in Experience section)
- Projects: 2 slots — Slot 1 is always Mindpex VAPT; Slot 2 chosen by scoring rubric
- Skills: 12–18 items
- Achievements: max 3
- Certifications: exactly 2 (CompTIA Security+, ISC2 CC)

**Rule:** Mindpex VAPT never appears in both Experience and Projects simultaneously.

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

If they contain verified information, incorporate it naturally.

Never ignore uploaded files.

---

# Conflict Resolution

If two files disagree, prefer

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

Instead, generalize while preserving

- technical concepts
- demonstrated skills
- engineering depth

Mindpex must always be described as **"Freelance VAPT Engagement — Enterprise SaaS Platform"** on the resume.

---

# Resume Constraints

## Layout A (Two Experience Entries)

| Section | Constraint |
|---|---|
| Experience Entry 1 (Mindpex VAPT) | Exactly 3 bullets, max 2 lines each |
| Experience Entry 2 (Epicor) | Exactly 3 bullets, max 2 lines each |
| Project (1 slot) | Exactly 3 bullets, max 2 lines each |
| Skills | 12–15 items |
| Achievements | Max 2 |
| Certifications | Exactly 2 |
| Resume Length | One page |

## Layout B (One Experience Entry)

| Section | Constraint |
|---|---|
| Experience Entry (Epicor) | Exactly 3 bullets, max 2 lines each |
| Project Slot 1 (Mindpex VAPT) | Exactly 3 bullets, max 2 lines each |
| Project Slot 2 | Exactly 3 bullets, max 2 lines each |
| Skills | 12–18 items |
| Achievements | Max 3 |
| Certifications | Exactly 2 |
| Resume Length | One page |

---

# Optimization Priorities

Priority order

1. Truthfulness
2. Role Alignment
3. Technical Depth
4. ATS Optimization
5. Readability
6. Keyword Density

Never sacrifice factual accuracy for ATS optimization.

---

# Output Requirements

Every generated resume should

- Target a single cybersecurity role
- Be ATS optimized
- Fit on one page
- Use measurable achievements where verified
- Prioritize security concepts over technology names
- Avoid generic software engineering terminology
- Demonstrate technical depth in every bullet
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

# Gap Analysis — MCQ Format

During Step 5b of the pipeline, the AI conducts interactive gap analysis using **Multiple Choice Questions** rather than open-ended questions.

- **Missing tool/technology:** Presents the exact JD tool + 2–3 close alternatives + "None" option. Candidate replies with a letter. That exact tool is used in the resume.
- **Missing concept/process:** A) Yes (describe it) / B) No
- **Partial experience:** Granularity MCQ — e.g., A) Custom rule writing / B) Ad-hoc usage / C) Conceptual familiarity

All questions are consolidated into a **single message**. Candidate replies with letters only. Answers are incorporated before any resume bullets are written.

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

When adding new content, always update `00_changelog.md` with the change, reason, and date.

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