# Output Log

Track every resume generated here.

| Date | Company | Role | JD Source | Experience | Projects Used (2 of 3) | Files Generated |
|---|---|---|---|---|---|---|
| 2026-10-22 | General | Cybersecurity Engineer (Default) | Template / Baseline | Epicor + Mindpex | VigiLynx + Security Assessment | S-Harsha_Bhat_General.html, S-Harsha_Bhat_General.pdf |
| 2026-10-23 | Jiostar | Application Security | Issue Submission | Epicor + Mindpex | VigiLynx + Security Assessment | S-Harsha_Bhat_Jiostar.pdf |
| 2026-10-23 | Avnet | Security Engineering | Issue Submission | Epicor + Mindpex | VigiLynx + CipherCrack | S-Harsha_Bhat_Avnet.pdf |
| 2026-10-23 | Marvell | Product Security | Issue Submission | Epicor + Mindpex | VigiLynx + Security Assessment | S-Harsha_Bhat_Marvell.pdf |
| 2026-10-23 | Autodesk | Security Operations / AppSec | Issue Submission | Epicor + Mindpex | VigiLynx + Security Assessment | S-Harsha_Bhat_Autodesk.pdf |
| 2026-10-23 | Lorven | DevSecOps / Cloud Security | Issue Submission | Epicor + Mindpex | VigiLynx + Security Assessment | S-Harsha_Bhat_Lorven.pdf |
| 2026-10-24 | AI-sec | AI / LLM Security Engineer | Issue Submission | Epicor + Mindpex | VigiLynx + Security Assessment | S-Harsha_Bhat_AI-sec.pdf |
| 2026-10-24 | AI | AI Security Engineer | Issue Submission | Epicor + Mindpex | VigiLynx + CipherCrack | S-Harsha_Bhat_AI.pdf |

---

# Naming Conventions

### 1. Automated Issue & Release Generator (Default in CI/CD)
- HTML: `outputs/S-Harsha_Bhat_{company_slug}.html`
- PDF: `outputs/S-Harsha_Bhat_{company_slug}.pdf`
- Tag / Release: `resume-{company_slug}-{run_number}`

This format ensures that generated files are recruiter-ready with the applicant's name clearly identified.

### 2. Manual Archive Convention (Optional Local Tracking)
- HTML: `outputs/YYYY-MM-DD_company_role.html`
- PDF: `outputs/YYYY-MM-DD_company_role.pdf`

Keep the role and company names lowercase with underscores.

---

# Notes

- The LLM generates the print-ready HTML resume directly, saving AI tokens.
- ATS Analysis, Competing Candidate Benchmarking, Priority Gap Strategy, and Company Intelligence are evaluated internally by the LLM during generation to shape the resume, but are omitted from text output to conserve tokens.
- If a resume is revised before sending, append `_v2`, `_v3` to the base filename.
- `engine/issue_resume_generator.py` automatically records successfully generated PDFs in this log.
