# Output Log

Track every resume generated here.

| Date | Company | Role | JD Source | Experience | Projects Used (2 of 3) | Files Generated |
|---|---|---|---|---|---|---|
| YYYY-MM-DD | Company Name | Role Title | [URL or "pasted"] | Epicor + Mindpex | [e.g. VigiLynx + Security Assessment] | .md, .html, .pdf |

---

# Naming Convention

Base name: `outputs/YYYY-MM-DD_company_role`

Deliverables per application:
- `outputs/YYYY-MM-DD_company_role.md` (Markdown resume, ATS analysis, Competing benchmark)
- `outputs/YYYY-MM-DD_company_role.html` (Standalone print-ready HTML matching reference PDF layout)
- `outputs/YYYY-MM-DD_company_role.pdf` (Headless Chromium 1-page PDF export via `engine/export_pdf.py`)

Examples:
- `outputs/2026-10-21_google_appsec.md`
- `outputs/2026-10-21_google_appsec.html`
- `outputs/2026-10-21_google_appsec.pdf`

Keep the role name lowercase with underscores. Keep the company name lowercase.

---

# Notes

- One set of deliverables (.md, .html, .pdf) per application.
- Include the ATS Analysis and Competing Benchmark output in the Markdown file alongside the resume.
- If a resume is revised before sending, append `_v2`, `_v3` to the base filename.
