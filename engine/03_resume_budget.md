# Resume Budget Engine

Version

1.0

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

# Section Budget

Header

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

# Summary

Optional

Maximum

3 lines

Maximum

60 words

Only include if

- It improves JD alignment.
- It does not remove stronger technical content.

Otherwise omit.

---

# Layout Selection

Before applying any budget, determine the layout from the Experience Structure Decision (master_resume_prompt.md Step 9).

**Layout A** — Mindpex VAPT + Epicor both in Experience section

Applies when JD targets: AppSec, ProdSec, Red Team, Pentesting, DevSecOps, Security Engineering

**Layout B** — Epicor only in Experience section

Applies when JD targets: Detection Engineering, SOC, Threat Intelligence, Security Research

---

# Experience Budget

## Layout A (Two Experience Entries)

Entry 1: Mindpex VAPT Freelance

- Bullets: exactly 3
- Max 2 lines per bullet
- Preferred length: 28–36 words

Entry 2: Epicor Software Internship

- Bullets: exactly 3
- Max 2 lines per bullet
- Preferred length: 28–36 words

## Layout B (One Experience Entry)

Entry 1: Epicor Software Internship

- Bullets: exactly 3
- Max 2 lines per bullet
- Preferred length: 28–36 words

---

# Projects Budget

## Layout A (Two Experience Entries)

Project slots: exactly 1

Choose from: VigiLynx / CipherCrack / Security Assessment

- Bullets: exactly 3
- Max 2 lines per bullet
- Preferred length: 28–36 words

Note: Mindpex is in Experience, not here.

## Layout B (One Experience Entry)

Project slots: exactly 2

Slot 1: Mindpex VAPT (always, described as "Freelance VAPT Engagement — Enterprise SaaS Platform")

Slot 2: choose from VigiLynx / CipherCrack / Security Assessment per Role Intelligence Matrix

- Bullets: exactly 3 per slot
- Max 2 lines per bullet
- Preferred length: 28–36 words

Never include all three of VigiLynx + CipherCrack + Security Assessment.

---

# Skills Budget

Categories: 4–6

Layout A (two experience entries): 12–15 total skills

Layout B (one experience entry): 12–18 total skills

Prioritize security concepts before technologies.

---

# Certifications

Maximum

2

Always

1.

CompTIA Security+

2.

ISC2 Certified in Cybersecurity (CC)

Never exceed two certifications unless explicitly requested.

---

# Achievements Budget

Layout A (two experience entries): max 2

Layout B (one experience entry): max 3

Order dynamically by target role.

Prefer measurable achievements.

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

Summary

↓

3

Low-priority skills

↓

4

Lower-ranked achievement

↓

5

Less relevant project

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
- 1324+ LOC
- 150+ CTFs
- Top 10%
- 17/662 Teams
- 200+ Participants

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

## Layout A (Two Experience Entries)

✓ One page

✓ Exactly 3 bullets for Mindpex experience

✓ Exactly 3 bullets for Epicor experience

✓ Exactly 3 bullets for the single project slot

✓ 12–15 skills

✓ Maximum 2 achievements

✓ Exactly 2 certifications

✓ Education within 2 lines

✓ No fabricated information

✓ JD-specific terminology applied

✓ Mindpex described as "Freelance VAPT Engagement — Enterprise SaaS Platform" (no client name)

## Layout B (One Experience Entry)

✓ One page

✓ Exactly 3 bullets for Epicor experience

✓ Exactly 3 bullets for Mindpex project slot

✓ Exactly 3 bullets for second project slot

✓ 12–18 skills

✓ Maximum 3 achievements

✓ Exactly 2 certifications

✓ Education within 2 lines

✓ No fabricated information

✓ JD-specific terminology applied

If any validation fails, regenerate the affected section.

---

# End of Resume Budget Engine