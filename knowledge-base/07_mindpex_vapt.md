# Mindpex VAPT Knowledge Base

> This document is the authoritative knowledge base for the Mindpex freelance VAPT engagement.
>
> This is NOT a resume.
>
> Resume bullets must always be generated from this document after analyzing the target Job Description.
>
> Never disclose:
> - Client name (Mindpex)
> - Product name
> - Internal environment details
> - Specific finding details verbatim from reports
>
> Always describe this engagement generically as:
> "Freelance VAPT Engagement — Enterprise SaaS Platform"

---

# Assessment Information

Assessment Type

Vulnerability Assessment and Penetration Testing (VAPT)

Client

Confidential — Enterprise SaaS Platform

Duration

July 2026 – August 2026

Assessor

Individual (Freelance)

Methodology

Mixed — Static Code Analysis + Dynamic Testing + Black-box Enumeration

Primary Standard

OWASP Web Security Testing Guide (WSTG)

Scope

Multi-tenant enterprise SaaS web application

- Full-stack application (Next.js + FastAPI Python services)
- PostgreSQL database with 47 migration files
- LLM/AI microservices (Groq, Cerebras integrations)
- Session, cookie, CSP, and header configuration
- Audit logging and rate limiting pipelines

---

# Tools Used

Primary

- Burp Suite — Request interception, auth bypass testing, parameter manipulation, injection payload delivery
- Nmap — Port scanning, service enumeration, FastAPI port exposure verification
- ffuf — Endpoint and directory enumeration across 61+ API routes and FastAPI endpoints
- interactsh — SSRF out-of-band detection, OAST callback server for blind vulnerability confirmation
- nikto — Web server scanning, HTTP misconfiguration discovery, security header enumeration
- sqlmap — SQL injection testing, ilike-based wildcard injection validation
- curl — Unauthenticated API testing, direct FastAPI endpoint probing

Supporting

- Browser Developer Tools — CSP analysis, cookie security inspection (HttpOnly, Secure, SameSite), security header review

---

# Audit Domains

## Domain 1 — API Security

Scope

- 61 Next.js API routes
- 3 FastAPI Python service routers

Activities

- Endpoint enumeration (ffuf, Nmap)
- Authentication bypass testing (Burp Suite, curl)
- Parameter manipulation (Burp Suite)
- Wildcard injection testing (sqlmap, Burp Suite)
- Authorization testing (Burp Suite, curl)

Critical Findings

- SSRF via unvalidated URL parameter in webhook endpoint (confirmed OOB with interactsh)
- Mass-deletion bug via fuzzy name matching and SQL wildcard in delete handler
- Missing authentication enforcement on multiple privileged admin routes
- Wildcard ilike filter (`full_name.ilike.%`) enabling bulk employee record deletion in single call
- Cross-tenant deletion possible by supplying foreign organization UUID

High Findings

- ilike wildcard enabling bulk update of employee records (sqlmap parameter injection)
- FastAPI services had zero authentication on all routes (curl + Nmap confirmed port exposure)
- Cascading delete logic with soft name-match bypassing UUID-only deletion
- Auto-provisioning middleware inserting org memberships without explicit invite acceptance

Security Concepts

- SSRF
- SQL Wildcard Injection
- BOLA (Broken Object-Level Authorization)
- Authentication Bypass
- Mass Data Destruction
- Multi-tenant Isolation
- Defense in Depth

Applicable Roles

★★★★★

- Red Team
- Application Security
- Product Security
- Penetration Testing

---

## Domain 2 — AI / LLM Endpoint Security

Scope

- FastAPI LLM routes (Groq, Cerebras)
- ICP memory pipeline
- Prompt construction pipeline

Activities

- Prompt injection payload crafting and delivery (Burp Suite, curl)
- Memory poisoning via unauthenticated test endpoint (curl)
- Static analysis of prompt construction code

Critical Findings

- Direct prompt injection on open `/groq/query` endpoint — raw user input passed verbatim to LLM
- Indirect prompt injection via persistent employee memory poisoning — attacker-controlled transcript stored in long-term memory, flowing into future LLM prompts

High Findings

- Unvalidated LLM context field accepted on recommendation endpoint — no provenance enforcement
- In-memory LLM context store had zero tenant isolation — any caller could read/write any employee memory by UUID
- Raw exception messages from failed LLM calls returned in API response — infrastructure disclosure

Security Concepts

- Prompt Injection
- Indirect Prompt Injection / Memory Poisoning
- LLM Security
- AI Trust Boundaries
- Multi-tenant Isolation
- Input Validation
- OAST

Applicable Roles

★★★★★

- Application Security
- Product Security
- Red Team
- Security Engineering

---

## Domain 3 — Authentication and Authorization

Scope

- Auth endpoints (login, signup, forgot-password, reset-password)
- Invitation acceptance flows
- Support portal invite flows
- Organization membership middleware

Activities

- Auth flow tracing and validation (Burp Suite, static analysis)
- Token-based authorization testing
- Privilege escalation path analysis

Critical / High Findings

- Account takeover via forced password override in org invitation acceptance flow
- Account takeover via same forced password override pattern in support portal invite flow
- First organization member auto-assigned `admin` role regardless of intended role in invitation
- Unverified account login bypass (code fix existed but not deployed to staging)

Medium Findings

- Middleware auto-heal routine inserting memberships without token verification
- Invitation token exposed in URL query parameter (logged by proxies, browser history)
- RBAC default set to `super_admin` when localStorage was absent

Security Concepts

- Account Takeover
- Privilege Escalation
- Authentication Bypass
- Broken Authentication
- Invitation Flow Security
- RBAC

Applicable Roles

★★★★★

- Red Team
- Product Security
- Application Security

---

## Domain 4 — PostgreSQL RLS Policy Review

Scope

- 47 database migration SQL files (V1–V47)
- All RLS policies, SECURITY DEFINER functions, GRANT statements

Activities

- Full migration chain static analysis
- Policy logic review (USING / WITH CHECK clauses, TO role clauses)
- Function authorization audit

Critical Findings

- `mindpex_platform_settings` — `USING (true)` with `anon` role granted — unauthenticated read/write of global security configuration (SMTP, MFA enforcement, webhook URLs, lockout durations)
- `mindpex_sales_partners` — `USING (true)` with no role restriction — any authenticated user could read/write/delete partner bank details and commit payment fraud

High Findings

- `organization_invitations` — RLS enabled in V47 with zero policies defined — deny-all state breaking invitation acceptance flow
- `mindpex_support_agents` — Policy missing `TO` clause defaulting to `PUBLIC` — all authenticated users could enumerate support staff PII
- `support_tickets` — Blanket `USING (true)` policy without `TO` clause overriding tenant-scoped policies via PostgreSQL OR logic — cross-tenant ticket leakage

Medium Findings

- `assign_workspace_slug()` SECURITY DEFINER function granted EXECUTE to any authenticated user — cross-tenant slug assignment possible
- `profiles` table — no INSERT policy; creation relying silently on SECURITY DEFINER bypass

Security Concepts

- Row-Level Security (RLS)
- PostgreSQL Policy Analysis
- Privilege Escalation
- Multi-tenant Data Isolation
- SECURITY DEFINER Functions
- Least Privilege
- Tenant Data Leakage
- Unauthenticated Data Access

Applicable Roles

★★★★★

- Product Security
- Application Security
- Security Engineering

---

## Domain 5 — Audit Logging and Audit Trail

Scope

- Application-level audit logging pipeline
- Auth audit stub
- Admin action coverage

Activities

- Codebase search for `audit_logs` inserts across all action files
- Auth stub analysis
- IP field population check

Critical Findings

- `auditAuth()` is an unfinished stub — login, logout, and password reset events never persisted to any storage
- 14+ sensitive admin/employee write operations (employee deletion, org creation, partner management) produced zero audit records

High Findings

- `ip_address` column present in `audit_logs` schema but never populated in any insert — no IP traceability for any audit event

Security Concepts

- Audit Trail
- Forensic Logging
- Incident Response Readiness
- Compliance (GDPR, SOC2)
- Security Event Persistence

Applicable Roles

★★★★☆

- Security Engineering
- Detection Engineering
- Product Security

---

## Domain 6 — HTTP Security Headers and CSP

Scope

- Next.js middleware/headers.ts
- next.config.js static headers
- FastAPI service headers

Activities

- Header enumeration (nikto, curl -I, Browser DevTools)
- CSP directive analysis (Browser DevTools)
- XSS sink scan (static analysis)

High Findings

- `'unsafe-inline'` present in production `script-src` — neutralizes CSP XSS protection entirely; any injected script executes

Medium Findings

- No CSP `report-uri` / `report-to` directive — violations invisible to operators
- `Cross-Origin-Opener-Policy` (COOP) not set
- `Cross-Origin-Resource-Policy` (CORP) not set

Low Findings

- FastAPI returns zero security headers on all responses
- `Permissions-Policy` inconsistency between two header layers
- No explicit session JWT expiry / rotation policy configured

Confirmed Positive

- No `dangerouslySetInnerHTML` / XSS sinks found in application code
- Supabase SSR cookies correctly set HttpOnly, Secure, SameSite:Lax

Security Concepts

- Content Security Policy (CSP)
- HTTP Security Headers
- XSS Prevention
- CORS
- Session Security
- Browser Security

Applicable Roles

★★★★☆

- Application Security
- Product Security
- Security Engineering

---

## Domain 7 — Rate Limiting and File Upload Security

Scope

- Next.js rate limiting middleware
- FastAPI rate limiting
- Audio file processing pipeline

Activities

- Middleware execution path tracing (static analysis)
- Rate limit bypass testing (ffuf)
- File path handling review

Critical Findings

- Rate limiting middleware wired to `proxy.ts` instead of `middleware.ts` — Next.js never executes it; ALL perimeter controls (rate limiting, body size guard, method guard, suspicious path blocking, security headers) are completely inactive

High Findings

- FastAPI LLM endpoints have zero rate limiting — unlimited prompt injection attempts, API cost abuse possible
- In-memory rate limit store resets on cold start — serverless bypass possible
- Audio processing accepts raw file paths from caller — path traversal risk when HTTP-exposed

Security Concepts

- Rate Limiting
- DoS Prevention
- Path Traversal
- Perimeter Security
- File Upload Security
- Serverless Security

Applicable Roles

★★★★☆

- Security Engineering
- Product Security
- Application Security

---

# Full Findings Inventory (Generic)

| Severity | Count | Example Classes |
|---|---|---|
| Critical | 9 | SSRF, account takeover, mass-deletion bug, prompt injection, anon RLS access, dead middleware |
| High | 15 | Auth bypass, wildcard SQL injection, FastAPI zero auth, LLM memory poisoning, privilege escalation |
| Medium | 12 | Auto-heal race condition, RBAC localStorage default, missing COOP/CORP, invite token in URL, audit log gaps |
| Low | 7 | Import error disclosure, path traversal risk, unbounded pagination, missing COEP |
| Informational | 6 | Good patterns identified, design observations |

---

# Deliverables Produced

- 7 domain-specific audit reports
- Executive summaries with severity matrices per domain
- CVSS-scored findings for all Critical and High items
- Code-level remediation in TypeScript, Python, and SQL
- Prioritized remediation roadmap (P0 → backlog)
- SQL migration scripts for RLS policy fixes

---

# Resume Generation Rules

Treat this engagement as primary professional security experience.

For AppSec / ProdSec / Red Team / DevSecOps JDs:

- Always include in Experience section
- Describe as "Freelance VAPT Engagement — Enterprise SaaS Platform"
- Emphasize finding severity, tool usage, and remediation produced

For Detection Engineering / SOC JDs:

- Emphasize audit logging gap findings
- May appear in project slot instead of experience

Never include all three of: Mindpex Freelance + both projects.

---

# Resume Bullet Rules

Generate exactly 3 bullets.

Maximum 2 lines per bullet.

Each bullet must follow:

Action → Technical implementation → Security relevance → Impact

Example high-quality bullets (DO NOT copy verbatim — generate fresh from JD analysis):

AppSec / ProdSec:

- Identified SSRF and mass-deletion vulnerabilities in a multi-tenant SaaS API via Burp Suite and interactsh; confirmed OOB callback and documented exploit chain with remediation code.
- Audited 47 PostgreSQL RLS migrations; discovered two Critical misconfigurations granting unauthenticated write access to security-critical tables including MFA and webhook configuration.
- Delivered 7-domain security audit with 30+ CVSS-scored findings and code-level remediation in TypeScript, Python, and SQL across a Next.js + FastAPI SaaS platform.

Red Team:

- Exploited SSRF via unvalidated webhook URL to demonstrate internal network access; used interactsh for OOB confirmation and documented attack chain with remediation.
- Discovered privilege escalation via invitation flow forced password override; traced attack path from low-privilege invite to full account takeover on any target email.
- Identified mass-deletion bug via SQL wildcard injection in admin delete handler; demonstrated full organization data wipe in single authenticated request.

---

# Evidence Confidence

Overall

★★★★★

Reason

All 30+ findings independently identified, exploited or statically confirmed, CVSS-scored, and documented with remediation by the candidate.

---

# ATS Keywords

Highest Priority

- VAPT
- Penetration Testing
- Vulnerability Assessment
- SSRF
- Prompt Injection
- LLM Security
- AI Security
- Multi-tenant Security
- API Security
- Authentication Bypass
- SQL Injection
- PostgreSQL RLS
- OWASP
- CVSS
- DevSecOps
- Static Analysis
- Dynamic Testing
- Remediation Design
- Burp Suite
- Nmap
- ffuf
- interactsh
- nikto
- sqlmap

Medium Priority

- Secure Architecture
- Defense in Depth
- Least Privilege
- CSP
- Rate Limiting
- Audit Logging
- Content Security Policy
- BOLA
- IDOR
