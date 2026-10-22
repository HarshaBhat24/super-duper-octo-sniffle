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
│   ├── 00_changelog.md               # KB update log - track new skills, certs, projects
│   ├── 01_candidate_profile.md       # Master profile, skills, tools, Truth Guard
│   ├── 02_experience.md              # Experience index, project slot rules
│   ├── 03_projects.md                # VigiLynx + CipherCrack project KB
│   ├── 04_security_assessments.md    # Black-box web app security assessment KB
│   ├── 05_achievements.md            # Achievements, certifications, role-ordered priority
│   ├── 06_epicor_internship.md       # Epicor FTE & Internship KB (AppSec pentest verification, CI/CD, automation)
│   └── 07_mindpex_vapt.md            # Mindpex VAPT freelance KB (7-domain security assessment)
│
├── engine/
│   ├── 01_resume_generation_rules.md # Scoring, bullet rules, ATS, Truth Guard, validation
│   ├── 02_role_intelligence_matrix.md# Per-role emphasis, skills ordering, terminology
│   ├── 03_resume_budget.md           # Bullet counts, space constraints
│   ├── 04_company_intelligence.md    # Company type classification and tone modifiers
│   └── export_pdf.py                 # CLI utility compiling HTML to 1-page PDF (--no-pdf-header-footer)
│
├── templates/
│   └── resume_template.html          # Reference HTML/CSS template matching 1-page PDF layout
│
├── prompts/
│   └── master_resume_prompt.md       # Orchestration prompt - 8-step zero-pause generation pipeline
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
│   ├── log.md                        # Resume version tracking log
│   └── resume.pdf                    # Generated 1-page ATS resume PDF
│
└── README.md
```

---

# Purpose

This repository is **not** a resume.

It is a structured knowledge base that allows an LLM to generate resumes and role-specific content dynamically.

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

Read the example file matching the target cybersecurity domain/role from

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

Apply Company Intelligence (tone & verb preference from 04_company_intelligence.md)

↓

Direct JD & Skills Alignment (silently cross-reference under Truth Guard; no interactive MCQ questionnaire, no role classification report wait, no phantom steps)

↓

Select 2 of 3 Projects based on target JD (3 bullets each)

↓

Rewrite Experience Bullets (Epicor: 2 bullets for Associate Product Developer, 2 bullets for Intern; Mindpex: 3 bullets)

↓

Generate Dynamic Skills (all matching candidate + JD skills, plus valuable verified additions)

↓

Generate Achievements & Certifications (CompTIA Security+ June 2026, ISC2 CC Feb 2026, max 3 achievements)

↓

Validate Resume Budget (strict 1-page fit, bullet constraints) and Truth Guard

↓

Direct Document Generation - Produce final resume directly matching reference PDF layout (Clean Markdown + Self-contained Print-Ready HTML)

↓

ATS Analysis & Competing Candidate Benchmark (5 items tagged + Priority Gap advice)
```

Never skip any step.

---

# Supported Roles

The engine supports **14 roles**. All roles use the same single layout.

| Role | Primary Evidence Anchor | Default Project Rank (Top 2 Selected) |
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

Project rank is the default alignment order (agent selects the top 2). Always override with actual JD keyword scoring.

The generator silently aligns the closest cybersecurity domain/role from the supplied Job Description under the Truth Guard.

---

# Layout Rules (All Roles - Unified)

There is ONE layout. It applies to ALL roles with no exceptions.

- Experience: always Epicor Software (4 bullets: 2 for Associate Product Developer, 2 for Intern) + Mindpex (3 bullets) (both, always)
- Projects: exactly 2 entries selected out of 3 (VigiLynx, CipherCrack, Security Assessment) based on target JD alignment (3 bullets each, 6 project bullets total)
- Skills: dynamic list matching JD requirements + verified candidate skills
- Achievements: max 3, dynamically ordered by role
- Certifications: exactly 2 (CompTIA Security+ - June 2026, ISC2 CC - Feb 2026)

Bullet allocation:
- Epicor Software: exactly 4 bullets total (2 for Associate Product Developer, 2 for Product Development Intern)
- Mindpex: exactly 3 bullets
- Projects: exactly 3 bullets per project for both selected projects (6 project bullets total)

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

Mindpex is titled **"Security Consultant (Freelancer) - Mindpex"** on the resume (or **"Freelance VAPT Engagement - Enterprise SaaS Platform"** if client confidentiality is explicitly requested).

---

# Resume Constraints (All Roles - Unified)

| Section | Constraint |
|---|---|
| Experience Entry 1 (Epicor) | Exactly 4 bullets total (2 for Associate Product Developer, 2 for Intern) |
| Experience Entry 2 (Mindpex) | Exactly 3 bullets, max 2 lines each (Security Consultant (Freelancer) - Mindpex) |
| Project Slot 1 (highest JD match) | Exactly 3 bullets, max 2 lines each |
| Project Slot 2 (second JD match) | Exactly 3 bullets, max 2 lines each |
| Skills | Dynamic list (matching candidate + JD skills + valuable additions) |
| Achievements | Max 3 |
| Certifications | Exactly 2 (CompTIA Security+ - June 2026, ISC2 CC - Feb 2026) |
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

- ATS-Optimized Tailored Resume (Clean Markdown + Standalone Print-Ready HTML)
- Exact 1-Page PDF Generation (`engine/export_pdf.py` with `--no-pdf-header-footer`)
- Direct JD & Skills Alignment (Under strict Truth Guard)
- Experience & Project Rewriting (Role-specific framing)
- Dynamic Skills Categorization
- Achievement & Certification Prioritization
- ATS Keyword Matching Analysis & Competing Candidate Benchmark

---

# Zero-Pause Direct Generation & PDF Layout Specification

The engine operates on a **zero-pause direct generation pipeline**. It does NOT pause to question or verify unknown or missing tools with multiple-choice questionnaires before generating the resume.

### Handling Unknowns & Gaps
- The engine cross-references the target JD with the Knowledge Base internally.
- If a tool or technology mentioned in the JD is missing from the Knowledge Base, the **Truth Guard** strictly forbids inventing or claiming experience with it.
- The engine dynamically emphasizes the candidate's verified, relevant skills and transferrable security engineering achievements from the Knowledge Base.

### Direct Document Generation (PDF-Matched Output)
The LLM outputs the finalized resume immediately, formatted to match the reference PDF layout:
- **Header:** Centered candidate name (`S HARSHA BHAT`) in bold uppercase, with a centered single contact line featuring live hyperlinks separated by pipes (`|`):
  `harshabhat666@gmail.com | www.linkedin.com/in/s-harsha-bhat/ | github.com/Harshabhat24 | harsha-bhat.vercel.app/ | 9483022191 | Bengaluru`
- **Section Headings:** Clean headings (`Experience`, `Projects`, `Skills`, `Certifications and Achievements`, `Education`) with full-width horizontal divider rules beneath each heading.
- **Experience Entries:** Two-column rows (`Associate Product Developer - Epicor Software, Bengaluru` [Sep 2026 - Present, 2 bullets], `Product Development Intern - Epicor Software, Bengaluru` [Oct 2025 - Sep 2026, 2 bullets], and `Security Consultant (Freelancer) - Mindpex` [July - Aug 2026, 3 bullets]).
- **Projects Entries:** Two-column rows with project names and clickable repo/live links on left; date ranges on right (exactly 2 projects selected out of 3, 3 bullets each, e.g. VigiLynx with live web app `https://vigilynx-web.vercel.app/`).
- **Skills:** Bulleted list categorized into bold headings: `● Security: ...`, `● Programming: ...`, `● Operating Systems: ...`, `● Networking: ...`, `● Tools: ...`.
- **Certifications and Achievements:** Compact bulleted list.
- **Education:** Institution and dates on line 1, degree and CGPA on line 2.
- **Output Formats:** Delivered simultaneously in formatted Markdown and standalone print-ready HTML/CSS designed for exact 1-page PDF export via `engine/export_pdf.py` (which disables browser print headers/footers automatically).

---

# Mobile / GitHub Actions Remote PDF Exporter

Generate company-specific PDFs (`S-Harsha_Bhat_{company-name}.pdf`) directly from your phone without a laptop or local Git environment:

### Method 1: Via GitHub Issues
1. In the GitHub app or mobile browser, navigate to **Issues** -> **New Issue**.
2. Select **Generate Resume PDF** (or create a blank issue).
3. Set the **Target Company Name** (e.g., `Google`, `Amazon`, `Stripe`).
4. Paste the complete resume HTML code into the description box.
5. Tap **Submit new issue**.
6. The GitHub Action will compile the PDF headlessly, commit it to `outputs/S-Harsha_Bhat_{company}.pdf`, upload it as a release asset, comment on the issue with a direct download link, and auto-close the issue within ~15 seconds.

### Method 2: Via Actions Tab (`workflow_dispatch`)
1. Go to the **Actions** tab on GitHub.
2. Select **Generate Resume PDF** -> **Run workflow**.
3. Enter the `company_name` and either paste raw HTML or specify a path to an existing HTML file in the repository.

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