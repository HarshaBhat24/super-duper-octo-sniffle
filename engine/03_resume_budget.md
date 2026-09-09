# Resume Budget Engine

Version

2.0

Purpose

This document enforces strict resume formatting constraints to ensure every generated resume fits comfortably on a single page while maximizing technical relevance.

This engine must be applied AFTER

- Candidate selection
- JD analysis
- Experience selection

and BEFORE the final resume is generated.

---

# Primary Rule

Every generated resume must fit on ONE page.

Do not exceed the allocated content budget.

Quality is preferred over quantity.

When space becomes limited,

remove low-impact information rather than compressing everything.

---

# Layout — Unified (All Roles)

There is ONE layout. It applies to all roles.

Both experience entries (Mindpex + Epicor) are always in the Experience section.

There is no Layout A or Layout B.

```
[Header]
[Experience]
  1. Mindpex Security Consulting — Freelance VAPT Engagement — Enterprise SaaS Platform
  2. Epicor Software — Product Development Intern
[Projects & Key Achievements]
  2–3 entries dynamically selected based on JD alignment
[Skills]
[Certifications]
[Education]
```

There is NO Summary section.

---

# Header Budget

Maximum

2 lines

Contains

- Name
- Email
- Phone
- GitHub
- LinkedIn
- Portfolio
- Location

Never include additional links.

---

# Experience Budget

Entry 1: Mindpex VAPT Freelance

- Bullets: exactly 3
- Max 2 lines per bullet
- Preferred length: 28–36 words

Entry 2: Epicor Software Internship

- Bullets: exactly 3
- Max 2 lines per bullet
- Preferred length: 28–36 words

---

# Projects Budget

## Slot Count Decision Rule

Default: 2 slots.

Upgrade to 3 slots ONLY IF:
- All 3 available projects score high on JD alignment, AND
- 3 project entries + both experience entries + Skills + Certifications & Achievements + Education all fit on one page without compression

Never use 3 slots just to fill space. Use 3 only when all 3 are genuinely high-alignment.

## Per Slot

Choose from: VigiLynx / CipherCrack / Security Assessment

- Bullets: exactly 3 per slot
- Max 2 lines per bullet
- Preferred length: 28–36 words

Mindpex is NEVER in the Projects section — it is always in Experience.

---

# Skills Budget

Categories: 4–6

Total skills: 12–15

Prioritize security concepts before technologies.

---

# Certifications & Achievements Budget

Section Name: **Certifications & Achievements** (merged, compact list)

Format: Compact list. No sub-bullets. One line per entry.

Certifications (always first, always both):
1. CompTIA Security+ (SY0-701) — June 2026
2. ISC2 Certified in Cybersecurity (CC)

Achievements (follow certifications, max 3, dynamically ordered by role):
- Choose from: HackAthena Winner, KJSSE CTF 17/662, Smart India Hackathon Finalist, CTF 200+, TryHackMe Top 10%
- Order per role using priority tables in 05_achievements.md

---

# Education

Maximum

2 lines

Include

- Degree
- College
- CGPA

Omit coursework unless requested.

---

# Volunteer Experience

Default

Omit

Include only if

- Leadership is requested
- Resume still fits within one page

Maximum

1 bullet

---

# Content Removal Priority

When reducing content, remove sections in this order.

1

Volunteer Experience

↓

2

Low-priority skills

↓

3

Lower-ranked achievement or project entry

Never reduce

- Experience bullets
- Certifications
- Core security skills

---

# Bullet Compression Rules

Merge related implementation details into one stronger bullet.

Example

Instead of

- Built Chrome extension.
- Added alerts.
- Implemented URL analysis.

Generate

Developed a Chrome extension that analyzed URLs in real time using Random Forest detection and generated phishing alerts.

---

# Metric Usage

Always include verified metrics when available.

Examples

- 1000+ URLs
- 50+ Files
- 1500+ LOC
- 200+ CTFs
- Top 10%
- 17/662 Teams
- 200+ Participants
- 5 VMs / 15 GB / weekly (Epicor VM cleanup script)

Never invent or estimate metrics.

---

# ATS Density

Each major JD keyword should appear naturally.

Target

1–2 mentions

Never repeat keywords excessively.

Avoid keyword stuffing.

---

# Technical Density

Every experience bullet should contain at least one

- Security concept
- Technical implementation
- Verified impact

Avoid generic software engineering wording when a security-specific equivalent exists.

---

# Final Resume Validation

Before returning the resume, verify

✓ One page

✓ No Summary section

✓ Mindpex VAPT in Experience section (described as "Freelance VAPT Engagement — Enterprise SaaS Platform")

✓ Epicor in Experience section

✓ Each experience has exactly 3 bullets

✓ Projects: 2–3 entries, each with exactly 3 bullets

✓ 12–15 skills

✓ Certifications & Achievements section present (compact list format)

✓ Exactly 2 certifications (Security+ first, ISC2 CC second)

✓ Maximum 3 achievements (dynamically ordered by role)

✓ Education within 2 lines

✓ No fabricated information

✓ JD-specific terminology applied

✓ Mindpex not named (described as Freelance VAPT Engagement)

✓ Epicor VM cleanup PowerShell script bullet present

If any validation fails, regenerate the affected section.

---

# End of Resume Budget Engine
