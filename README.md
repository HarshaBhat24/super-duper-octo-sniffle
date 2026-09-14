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
│   ├── 02_experience.md              # Experience index, project slot rules
│   ├── 03_projects.md                # VigiLynx + CipherCrack project KB
│   ├── 04_security_assessments.md    # Black-box web app security assessment KB
│   ├── 05_achievements.md            # Achievements, certifications, role-ordered priority
│   ├── 06_epicor_internship.md       # Epicor internship KB (CI/CD, automation, Linux)
│   └── 07_mindpex_vapt.md            # Mindpex VAPT freelance KB (7-domain security assessment)
│
├── engine/
│   ├── 01_resume_generation_rules.md # Scoring, bullet rules, ATS, Truth Guard, validation
│   ├── 02_role_intelligence_matrix.md# Per-role emphasis, skills ordering, terminology
│   ├── 03_resume_budget.md           # Bullet counts, space constraints
│   └── 04_company_intelligence.md    # Company type classification and tone modifiers
│
├── prompts/
│   └── master_resume_prompt.md       # Orchestration prompt — the 15-step generation pipeline
│
├── examples/
│   ├── appsec.md                     # Application Security Engineer
│   ├── product_security.md           # Product Security Engineer
│   ├── redteam.md                    # Red Team Engineer
│   ├── devsecops.md                  # DevSecOps Engineer
│   ├── security_engineering.md       # Security Engineer
│   ├── ai_llm_security.md            # AI / LLM Security Engineer
│   ├── api_security.md               # API Security Engineer
│   ├── offensive_security.md         # Offensive Security Engineer
│   ├── detection_engineer.md         # Detection Engineer
│   ├── soc.md                        # SOC Analyst
│   ├── penetration_tester.md         # Penetration Tester
│   ├── threat_intel.md               # Threat Intelligence Analyst
│   ├── security_research.md          # Security Research Engineer
│   └── purple_team.md                # Purple Team
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

Role Classification Report — Score all 14 roles; output top 3 with confidence %; ask "Proceeding with [Primary Role] — reply with a different role name to override, or anything else to continue." Wait one turn before proceeding.

↓

Experience Structure Decision — single unified layout for all roles

↓

Extract ATS Keywords

↓

Score and Rank All 3 Projects by JD alignment

↓

Rewrite Experience Bullets (3 per entry, max 2 lines each)

↓

Generate Skills (12–15 items, reordered by role and company modifier)

↓

Generate Achievements (max 3, dynamically ordered by role)

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

The engine supports **14 roles**. All roles use the same single layout.

| Role | Primary Evidence Anchor | Default Project Order (Slot 1 → 2 → 3) |
|---|---|---|
| Application Security Engineer | Mindpex Domain 1–7 (full-scope VAPT) | Security Assessment → VigiLynx → CipherCrack |
| Product Security Engineer | Mindpex Domain 1–7 + RLS analysis | Security Assessment → VigiLynx → CipherCrack |
| Red Team Engineer | Mindpex exploitation chain + CTFs | Security Assessment → CipherCrack → VigiLynx |
| Penetration Tester | Mindpex SSRF, ATO, wildcard injection | Security Assessment → CipherCrack → VigiLynx |
| DevSecOps Engineer | Epicor CI/CD + Mindpex VAPT as security gate | VigiLynx → Security Assessment → CipherCrack |
| Security Engineer | Mindpex multi-domain + Epicor automation | VigiLynx → Security Assessment → CipherCrack |
| AI / LLM Security Engineer | Mindpex Domain 2 (prompt injection, memory poisoning) | VigiLynx → Security Assessment → CipherCrack |
| API Security Engineer | Mindpex Domain 1 (61 API routes, SSRF, BOLA) | Security Assessment → VigiLynx → CipherCrack |
| Offensive Security Engineer | CipherCrack (9-cipher toolkit) + Mindpex exploitation | CipherCrack → Security Assessment → VigiLynx |
| Detection Engineer | Mindpex VAPT + Epicor automation | VigiLynx → CipherCrack → Security Assessment |
| SOC Analyst | Mindpex VAPT + Epicor log analysis | VigiLynx → CipherCrack → Security Assessment |
| Threat Intelligence Analyst | VirusTotal pipeline + IOC analysis | VigiLynx → CipherCrack → Security Assessment |
| Security Research Engineer | CipherCrack cryptanalysis + Mindpex research | CipherCrack → Security Assessment → VigiLynx |
| Purple Team | Mindpex + VigiLynx detection layer | Security Assessment → VigiLynx → CipherCrack |

Project order is the default scoring rank. Always override with actual JD keyword scoring.

The generator automatically determines the closest role from the supplied Job Description.

---

# Layout Rules (All Roles — Unified)

There is ONE layout. It applies to ALL roles with no exceptions.

- Experience: always Mindpex VAPT Freelance + Epicor Software (both, always)
- Projects: always all 3 entries (VigiLynx, CipherCrack, Security Assessment)
- Skills: 12–15 items, reordered dynamically by role
- Achievements: max 3, dynamically ordered by role
- Certifications: exactly 2 (CompTIA Security+, ISC2 CC)

Bullet allocation for Projects is determined by JD alignment score:
- Slot 1 (highest score): 3 bullets
- Slot 2 (second score):  3 bullets
- Slot 3 (lowest score):  2 bullets

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

# Resume Constraints (All Roles — Unified)

| Section | Constraint |
|---|---|
| Experience Entry 1 (Epicor) | Exactly 3 bullets, max 2 lines each |
| Experience Entry 2 (Mindpex VAPT) | Exactly 3 bullets, max 2 lines each |
| Project Slot 1 (highest JD score) | Exactly 3 bullets, max 2 lines each |
| Project Slot 2 (second JD score) | Exactly 3 bullets, max 2 lines each |
| Project Slot 3 (lowest JD score) | Exactly 2 bullets, max 2 lines each |
| Skills | 12–15 items |
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