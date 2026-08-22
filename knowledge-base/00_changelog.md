# Knowledge Base Changelog

Track every update to the knowledge base here.

When you gain a new skill, complete a project, earn a certification, or finish an engagement — update the relevant KB file and log it here.

This log is used during Gap Analysis to determine whether a MISSING item was actually recently added to the KB.

---

## Format

```
## YYYY-MM-DD

File updated: [filename]
Change: [what was added or modified]
Reason: [why — new skill, completed project, new cert, etc.]
```

---

## Log

## 2026-08-19

File updated: 07_mindpex_vapt.md
Change: Created. Full VAPT engagement KB for Mindpex freelance work.
Reason: New freelance engagement completed (July–August 2026).

File updated: 06_epicor_internship.md
Change: Created. Full internship KB for Epicor Product Development role.
Reason: Internship began October 2025, KB created August 2026.

File updated: 01_candidate_profile.md
Change: Added interactsh to security tools. Added bug bounty false positive to Truth Guard.
Reason: Gap analysis fix (project accuracy).

## 2026-08-22

File updated: prompts/master_resume_prompt.md
Change: Step 5b rewritten — Gap Analysis Q&A converted from open-ended questions to MCQ format. Tool/technology gaps now present labeled options (A/B/C/D) with the exact JD tool + close alternatives. Candidate replies with a letter; that specific tool is used in the resume. Conceptual gaps use A/Yes or B/No format. Partial gaps use depth-level MCQs.
Reason: Faster, unambiguous gap resolution; eliminates free-text ambiguity on tool names.

File updated: prompts/master_resume_prompt.md
Change: Step 9 layout table now includes a Layout column (A/B) and explicitly lists Security Research as Layout B. Layout B rows now correctly show Mindpex VAPT as Slot 1 of the project section.
Reason: Security Research was missing from the Step 9 table. Layout B project slot description was incomplete.

File updated: engine/01_resume_generation_rules.md
Change: Final Validation Checklist — corrected project count rule to be layout-conditional (1 for Layout A, 2 for Layout B) instead of incorrectly stating "exactly two".
Reason: Layout A only has 1 project slot; the old rule was factually wrong.

File updated: knowledge-base/02_experience.md
Change: Role-Based Pairing table restructured — added Layout column (A/B), added Slot 1 / Slot 2 columns for Layout B, corrected Detection Eng/SOC/TI rows to show "Mindpex VAPT" as Slot 1 and "VigiLynx" as Slot 2 (not VigiLynx + CipherCrack as two free slots).
Reason: Table was using pre-Mindpex Layout B model. After 07_mindpex_vapt.md was added, Mindpex became the fixed Slot 1 for all Layout B roles.

File updated: examples/detection_engineer.md
Change: Section Order updated to show Epicor (Experience) → Mindpex VAPT (Slot 1) → VigiLynx (Slot 2). Validation checklist updated to match Layout B model including skills cap (12–18), achievements cap (max 3), and Mindpex description check.
Reason: Example file predated the Mindpex-as-Slot-1 rule. It showed VigiLynx + CipherCrack as two free project slots, which is the old model.

File updated: examples/soc.md
Change: Section Order updated to show Epicor (Experience) → Mindpex VAPT (Slot 1) → VigiLynx (Slot 2). Validation checklist updated to match Layout B model.
Reason: Same as detection_engineer.md — predated Mindpex-as-Slot-1 rule.

File updated: knowledge-base/05_achievements.md
Change: Added "Security Research" achievement priority section (CTF Experience → KJSSE CTF → TryHackMe) between the Security Engineering and SOC sections.
Reason: Security Research was the only supported role without a dedicated achievement ordering section.

File updated: engine/01_resume_generation_rules.md
Change: Renamed "Experience Priority" section header to "Project Priority by Role" — the section defines project selection order per role, not experience entry priority.
Reason: Misleading title could cause the model to confuse project selection logic with experience selection logic.

## 2026-08-23

File updated: prompts/master_resume_prompt.md, engine/02_role_intelligence_matrix.md, knowledge-base/02_experience.md, knowledge-base/05_achievements.md, examples/
Change: Added 3 new distinct target roles to the full pipeline:
  1. AI / LLM Security Engineer — anchored on Mindpex Domain 2 (prompt injection, indirect memory poisoning, zero tenant isolation in LLM context store, infrastructure disclosure via LLM exception responses). Layout A. Project: VigiLynx.
  2. API Security Engineer — anchored on Mindpex Domain 1 (61 Next.js routes + 3 FastAPI routers enumerated via ffuf/Nmap, SSRF, BOLA, SQL wildcard injection, dead rate-limiting middleware, zero-auth FastAPI services). Layout A. Project: Security Assessment.
  3. Offensive Security Engineer — distinct from Red Team; tool-building framing anchored on CipherCrack (9-cipher cryptanalysis toolkit, 1,324+ LOC) + Mindpex full exploitation chain. Layout A. Project: CipherCrack.
Each role was added to: Step 6a role list, Step 9 layout table, 02_experience.md pairing table, 02_role_intelligence_matrix.md (full entry), 05_achievements.md (priority section), examples/ (full example file).
Reason: Existing role coverage was too shallow — API Security, AI/LLM Security, and Offensive Security are distinct JD categories that map to different emphasis profiles, skills ordering, and bullet framing despite overlapping evidence.

File updated: engine/01_resume_generation_rules.md
Change: Added AI/LLM Security, API Security, Offensive Security, and DevSecOps to the JD Analysis categories list. Added project priority entries for all 4 in the Project Priority by Role section. Updated Experience Selection Rules to include the 3 new Layout A roles in the Mindpex-in-Experience trigger list.
Reason: The engine categories list and project priority section were not updated when the 3 new roles were added, leaving them without scoring guidance.

File updated: README.md
Change: Full rewrite. Updated to reflect 14 supported roles (was 11), added Layout A/B role tables with evidence anchors and default projects, updated file tree to include all 10 example files, documented MCQ gap analysis format, replaced old budget text with structured tables, added Mindpex confidentiality rule explicitly, added changelog update instruction.
Reason: README was outdated — did not reflect the Layout A/B architecture, new roles, MCQ format, or example file expansion.
