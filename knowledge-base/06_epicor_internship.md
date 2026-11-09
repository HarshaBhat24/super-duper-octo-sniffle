# Epicor Software Internship Knowledge Base

> This file contains the complete knowledge base for the Epicor Software internship.
>
> This is NOT a resume.
>
> Resume bullets must always be generated from this document after analyzing the target Job Description.
>
> Never fabricate responsibilities beyond those documented here.

---

# Experience Information

Company

Epicor Software

Roles

- Associate Product Developer (September 2026 – Present, Full-time)
- Product Development Intern (October 2025 – September 2026, Internship)

Location

Bengaluru, India

---

# Experience Summary

Worked within an enterprise software product development organization as Associate Product Developer (FTE) and Product Development Intern, focusing on application security vulnerability verification, penetration testing bug re-testing, CI/CD pipeline automation, DevOps scripting, environment reliability engineering, application certificate lifecycle, UI automation, and load testing.

Core work:

- Application Security & Penetration Testing Defect Verification (FTE): Re-tested 5 reported penetration testing bugs using Burp Suite, browser DevTools, and manual HTTP/API manipulation; identified incomplete remediations across 3 defects (CSP unsafe-inline bypass, BOLA / unauthorized user-data extraction, and JWT post-logout invalidation failure) plus forced browsing path exposure; authored reproduction PoCs and moved defect tickets back in Jira with remediation guidance.
- Creating and maintaining Azure DevOps (ADO) pipelines for CI/CD orchestration, where each pipeline runs against agent VMs executing PowerShell scripts
- Writing PowerShell scripts that execute on agent VMs within ADO pipelines (build, provisioning, automation tasks)
- Authored a PowerShell cleanup script deployed across 5 agent VMs via an ADO pipeline - auto-triggered weekly, clearing ~ 50 GB of logs and temp data per run, significantly reducing pipeline failures caused by storage exhaustion
- Renewed application certificates and created CA certificates for the enterprise application, managing certificate lifecycle requirements
- UI automation of an enterprise application using TypeScript (click interactions, app navigation, workflow automation)
- Wrote and executed a Python/Locust load testing script that opened multiple parallel Chrome instances and performed UI interactions against the application URL under load
- SQL querying and data retrieval using Microsoft SSMS; performed database backup and restoration
- Log analysis and root cause analysis for pipeline and script execution failures (storage exhaustion, network issues, execution errors)
- Worked within Agile delivery cycles using Azure DevOps Boards and JIRA

The full-time role directly provides verified, enterprise-level Application Security (AppSec), Product Security, and Penetration Testing remediation verification capabilities, while the internship work provides verified DevSecOps, Security Automation, and Infrastructure Reliability evidence.

---

# Primary Responsibilities

- Penetration testing defect re-testing and remediation verification (Burp Suite, DevTools, manual API manipulation)
- Security bug lifecycle tracking and reproduction PoC documentation in Jira
- Azure DevOps (ADO) CI/CD pipeline creation and management
- PowerShell scripting for pipeline automation and agent VM task execution
- VM cleanup automation - authored script deployed across 5 VMs, auto-triggered via ADO pipeline
- Application certificate renewal and CA certificate creation
- UI automation using TypeScript (enterprise application click/navigation automation)
- Python/Locust load testing script development and execution
- SQL querying and data retrieval (Microsoft SSMS)
- Database backup and restoration (Microsoft SSMS)
- Log analysis and root cause analysis of pipeline and script failures
- Agile delivery (JIRA, Azure DevOps Boards)

---

# Technical Responsibilities

## Application Security & Penetration Testing Bug Re-Testing (FTE - Associate Product Developer)

Performed:
- Re-tested 5 reported penetration testing defect tickets against the enterprise web application and API endpoints.
- Evaluated remediation implementations and discovered that remediations were **incomplete in 3 of the 5 bugs**, allowing persistent bypasses.
- Discovered and verified 4 critical security vulnerability vectors:
  1. **Content Security Policy (CSP) Incomplete Remediation (XSS Bypass)**: Tested developer's CSP fix intended to mitigate Cross-Site Scripting (XSS). Discovered that `'unsafe-inline'` script directive was still included in the CSP header, rendering the policy ineffective against inline script injection.
  2. **API Broken Object/Function-Level Authorization (BOLA / BFLA)**: Re-tested non-administrative user permissions against form data endpoints. Identified that non-admin authenticated users could make direct API requests to access restricted forms and exfiltrate profile/sensitive data for all users across the organization without required privileges.
  3. **Broken Authentication / Post-Logout JWT Invalidation Failure**: Re-tested session termination and token revocation. Discovered that JWT access tokens were not invalidated or blacklisted on the backend upon logout, allowing expired user sessions to remain active, replay API requests, and access protected resources across different login sessions.
  4. **Forced Browsing / Client-Side Route Access Control**: Demonstrated that unprivileged users knowing restricted application URL paths could navigate directly to privileged views and components without server-side route authorization validation.
  5. **Sensitive Data Exposure in API Responses**: Re-tested API error handling and payloads to ensure verbose traces, stack traces, and internal server parameters were properly sanitized.
- Defect Workflow & Deliverable:
  - Authored comprehensive re-test reports with step-by-step reproduction steps and proof-of-concept (PoC) payloads.
  - Reopened and moved incomplete defect tickets back to development teams in Jira, specifying exact remediation requirements (removing 'unsafe-inline', implementing server-side RBAC checks on API handlers, enforcing server-side token invalidation).
  - Tools utilized: Burp Suite, Browser DevTools, cURL, Jira.

Security Relevance:
HIGHEST (★★★★★)

Concepts:
- Vulnerability remediation verification & re-testing
- Content Security Policy (CSP) enforcement & XSS prevention
- Broken Object-Level Authorization (BOLA / OWASP API1)
- Broken Function-Level Authorization (BFLA / OWASP API5)
- Session lifecycle & JWT revocation/blacklisting
- Forced Browsing & Missing Function-Level Access Control
- Vulnerability management & defect tracking lifecycle in Jira

Applicable Roles:
- Application Security (AppSec) Engineer
- Product Security Engineer
- Penetration Tester / VAPT
- API Security Engineer
- Offensive Security / Red Team
- Security Engineer

Resume Priority:
HIGHEST for AppSec, Product Security, API Security, and Pentesting roles. Combine with the VM cleanup automation bullet.

---

## Azure DevOps (ADO) CI/CD Pipelines

Performed

- Created ADO pipelines for CI/CD orchestration
- Each pipeline uses agent VMs running PowerShell scripts as the execution layer
- Created Jenkins pipelines with PowerShell scripts (pre-migration)
- Migrated pipelines from Jenkins to Azure DevOps
- Monitored and debugged pipeline runs
- Performed root cause analysis on pipeline failures

Security Relevance

High

Concepts

- CI/CD pipeline orchestration
- Agent-based pipeline execution architecture
- Pipeline reliability and failure investigation
- DevSecOps tooling integration layer

Applicable Roles

- DevSecOps
- Security Engineering
- Security Automation

---

## PowerShell Scripting (Pipeline Automation)

Developed

- PowerShell scripts that execute as the core task layer inside ADO agent VMs
- Each script performs a specific automation task triggered by the pipeline
- Authored VM cleanup script (see below for full detail)

Security Relevance

High

Concepts

- Security automation scripting
- Repeatable, script-driven task execution
- Workflow automation transferable to security tooling (log collectors, alert scripts)

Applicable Roles

- Security Automation
- Detection Engineering
- Security Engineering
- DevSecOps

---

## VM Cleanup PowerShell Script - Star Achievement

This is the single most impactful individual contribution from this internship.

Written

- From scratch - no prior script existed

Scope

- Deployed across 5 agent VMs

Trigger

- Auto-triggered weekly via an ADO pipeline

Function

- Clears logs and temporary data that accumulate in agent VMs during pipeline runs

Impact

- Clears approximately  50 GB of junk data per weekly run
- Directly reduced pipeline failures caused by storage exhaustion in VMs
- Improved overall pipeline reliability and reduced manual intervention

Security Relevance

High

Concepts

- Automated log management and cleanup
- Scripted environment hygiene - reduces configuration drift and execution errors
- Scheduled automation for operational reliability

Applicable Roles

- DevSecOps
- Security Automation
- Security Engineering
- Detection Engineering

Resume Priority

HIGHEST - always include this in at least one bullet

---

## UI Automation (TypeScript)

Performed

- Automated clicking, interaction, and navigation of an enterprise application using TypeScript
- Built automation workflows that launch, navigate, and interact with the application UI

Security Relevance

Medium

Concepts

- Automated application interaction (directly applicable to security test automation)
- Client-side scripting and automation tooling
- Enterprise application workflow automation

Applicable Roles

- Application Security
- Product Security
- DevSecOps
- Security Engineering

---

## Python / Locust Load Testing

Written and Executed

- Developed a Python script using Locust that puts load on the enterprise application URL
- Script opens multiple Chrome instances in parallel and performs UI interactions (click actions) under load
- Executed the script personally - both wrote and ran the load tests

Security Relevance

Medium

Concepts

- Load and performance testing methodology
- Multi-instance parallel execution
- Stress testing application behavior under concurrent load (relevant to DoS resilience, API security)

Applicable Roles

- Application Security
- API Security
- Security Engineering
- Product Security

---

## SQL and Database Management (Microsoft SSMS)

Used SQL for

- Querying results based on project requirements
- Data retrieval and validation during pipeline and testing workflows
- Performing database backup and restoration using Microsoft SSMS

Do NOT claim

- Database design or schema architecture
- Query optimization or performance tuning
- Database administration as a primary responsibility

Tool

- Microsoft SSMS (SQL Server Management Studio)

Applicable Roles

- Application Security
- Security Engineering
- Product Security

---

## Log Analysis and Root Cause Analysis

Performed

Analysis of:

- PowerShell script execution logs
- Pipeline execution output and failure traces
- Storage-related failures in agent VMs
- Network-related failures in pipeline execution environments

Common failure types investigated

- VM storage exhaustion (disk space issues causing script failures)
- Network connectivity issues during pipeline execution
- Script execution errors (timeouts, permission errors)

Process

- Systematic log inspection
- Execution path tracing
- Root cause identification
- Failure remediation

Security Concepts

- Log-based investigation methodology
- Execution tracing
- Systematic root cause analysis (directly applicable to incident analysis and detection engineering)

Applicable Roles

- Detection Engineering
- Security Engineering
- SOC

Priority

High

---

## Azure DevOps (Platform)

Usage

- Source code repository management
- CI/CD pipeline creation, management, and monitoring
- Work item and sprint tracking (Boards)
- Agile team collaboration

Applicable Roles

- Security Engineering
- DevSecOps

---

## Jenkins (Pre-Migration)

Usage

- Created Jenkins pipelines with PowerShell scripts as the execution layer
- Ran and monitored existing Jenkins pipelines
- Supported migration of Jenkins pipelines to Azure DevOps

Applicable Roles

- DevSecOps
- Security Engineering

---

## Agile

Worked in

- Agile environment

Exposure

- Sprint planning
- Task tracking
- Team collaboration

Tools

- JIRA
- Azure DevOps Boards

---

# Security Mapping

## DevSecOps

Evidence

★★★★★

Concepts

- ADO CI/CD pipeline creation and management
- Agent-VM based pipeline execution architecture
- VM cleanup automation (PowerShell, ADO-triggered)
- Pipeline failure root cause analysis

---

## Security Automation

Evidence

★★★★★

Concepts

- PowerShell scripting for pipeline task automation
- VM cleanup script (5 VMs, ~ 50 GB/week, ADO-triggered)
- Python/Locust load testing scripting
- TypeScript UI automation

Applicable Roles

- Detection Engineering
- Security Engineering

---

## Log-Based Investigation

Evidence

★★★★☆

Concepts

- Log inspection for pipeline failure root cause
- Storage and network failure investigation
- Systematic investigation methodology

Applicable Roles

- Detection Engineering
- SOC

---

## Enterprise Software Architecture Exposure

Evidence

★★★★★

Exposure

- Large-scale enterprise ERP software product
- Enterprise CI/CD workflows with multiple agent VMs
- Multi-team Agile delivery

Applicable Roles

All

---

# ATS Keywords

High Priority

- CI/CD
- Azure DevOps
- ADO
- PowerShell
- Automation
- Pipeline Automation
- Build Automation
- Log Analysis
- Root Cause Analysis
- Agile
- JIRA
- TypeScript
- Python
- Load Testing
- SQL
- SSMS

Medium Priority

- DevSecOps
- Security Automation
- Enterprise Software
- Scripting
- Jenkins
- Database Management
- UI Automation
- Locust
- Environment Reliability

---

# Role Mapping

## DevSecOps

Priority

Very High

Emphasize

- ADO CI/CD pipeline creation
- VM cleanup PowerShell script (5 VMs, ~ 50 GB/week, ADO-triggered)
- Pipeline failure root cause analysis

Suppress

- SQL database queries
- JIRA task tracking

---

## Security Engineering

Priority

Very High

Emphasize

- Pipeline automation
- PowerShell scripting
- Azure DevOps
- VM cleanup automation
- Log analysis

Suppress

- Agile process details

---

## Security Automation

Priority

High

Emphasize

- PowerShell automation scripts
- VM cleanup script
- Python/Locust load testing
- TypeScript UI automation

---

## Detection Engineering

Priority

High

Emphasize

- Log analysis
- Root cause analysis (storage/network failures)
- PowerShell execution
- Pipeline failure investigation

---

## Application Security / Product Security

Priority

★★★★★ (Highest)

Emphasize

- Penetration testing defect re-testing and remediation verification (Burp Suite, DevTools)
- Incomplete fix discovery: CSP unsafe-inline bypass, API BOLA / unauthorized user extraction, JWT post-logout invalidation failure, forced browsing route access
- Defect tracking and reproduction PoC documentation in Jira
- Application certificate renewal and CA certificate creation
- TypeScript UI automation and Python/Locust load testing under concurrent load
- CI/CD pipeline security and environment automation

Suppress

- QA/testing terminology

---

## Red Team

Priority

★★★★☆

Emphasize

- Vulnerability verification and exploitation bypass analysis
- Manual API manipulation and authorization testing (BOLA, forced browsing)
- Scripting (PowerShell, Python, TypeScript)
- Automation knowledge
- Pipeline and environment knowledge

Suppress

- Enterprise testing details

---

## SOC

Priority

Medium

Emphasize

- Log analysis
- Execution tracing
- Storage and network failure investigation methodology

---

# Resume Bullet Rules

Generate exactly 4 bullets total:
- Associate Product Developer (Sep 2026 – Present): exactly 2 bullets
- Product Development Intern (Oct 2025 – Sep 2026): exactly 2 bullets

Maximum 2 lines per bullet.

Each bullet must follow:

Action → Technical implementation → Cybersecurity relevance → Impact

## Preferred Bullet Framings by Role Entry

### Associate Product Developer (FTE, Sep 2026 – Present) - Exactly 2 Bullets:
- **Bullet 1 (AppSec / Defect Verification Star Bullet - Priority for AppSec / ProdSec / Pentest / API roles)**:
  Re-tested 5 penetration testing defect tickets using Burp Suite and manual API manipulation; identified incomplete remediations across 3 defects (CSP unsafe-inline bypass, BOLA user-data exposure, JWT post-logout invalidation failure) and returned tickets in Jira with reproduction PoCs.
- **Bullet 2 (Certificate Lifecycle / Pipeline / Agile - Priority for Infrastructure / DevSecOps)**:
  Renewed application certificates and created CA certificates for enterprise application components, applying certificate lifecycle management alongside Azure DevOps pipeline orchestration and Agile defect tracking in Jira.
- **Alternative APD Bullet (Root Cause Analysis)**:
  Conducted root-cause investigation and log analysis on failed CI/CD pipeline runs and agent execution errors across Azure DevOps environments, diagnosing storage limits and credential expirations.

### Product Development Intern (Oct 2025 – Sep 2026) - Exactly 2 Bullets:
- **Bullet 1 (DevOps / Reliability Star Bullet - Highest Priority)**:
  Engineered a PowerShell cleanup script deployed across 5 agent VMs via automated weekly ADO pipeline, clearing ~ 50 GB of logs and temp data per run - eliminating pipeline failures caused by storage exhaustion.
- **Bullet 2 (Automation / Load Testing / Database - Role-adaptive)**:
  - API / Stress Testing: Authored Python/Locust load testing scripts exercising enterprise application workflows across multiple parallel Chrome instances under concurrent load.
  - UI Automation: Developed TypeScript UI automation workflows to validate enterprise application functionality and input boundaries.
  - Database Inspection: Wrote SQL queries against SSMS-backed databases for test data validation and application state inspection; performed database backup and restoration.

## Always Avoid

- "Regression testing", "smoke testing", "test cases", "test execution"
- "QA", "software quality assurance"
- Generic testing language
- Claiming to author Jenkinsfiles or Azure Pipelines YAML as the primary output

## Always Use

- "Penetration testing defect re-testing", "Remediation verification"
- "Burp Suite", "Browser DevTools", "Manual API request manipulation"
- "Content Security Policy (CSP)", "unsafe-inline", "XSS mitigation"
- "Broken Object-Level Authorization (BOLA)", "User data extraction"
- "JWT invalidation", "Session revocation"
- "Jira defect tracking", "PoC reproduction steps"
- "Application certificate renewal", "CA certificate creation"
- "Pipeline automation", "CI/CD orchestration"
- "Agent VM", "pipeline agent"
- "PowerShell scripting", "automation script"
- "VM cleanup automation"
- "Log inspection", "root cause analysis"
- "Azure DevOps", "ADO pipeline"
- "TypeScript UI automation" (for relevant roles)
- "Load testing" (for relevant roles)
- "Database backup and restoration" (for relevant roles)

---

# Never Claim

Never state

- That the official job title at Epicor was Penetration Tester, Security Analyst, or Security Engineer (the titles are strictly Associate Product Developer and Product Development Intern)
- SOC Analyst title
- Incident Responder title

Never imply

- Production security monitoring or SOC operations
- SIEM administration (Splunk, Sentinel, QRadar)
- Production automated vulnerability scanning ownership
- Docker or containerization
- Kubernetes or cloud infrastructure architecture
- Authored Jenkinsfile or Azure Pipelines YAML as the primary deliverable

---

# Dynamic Resume Logic

If JD is Application Security / Product Security / Penetration Testing / API Security

Focus on

- Re-testing 5 penetration testing defect tickets using Burp Suite; discovering 3 incomplete fixes (CSP unsafe-inline, BOLA user extraction, JWT invalidation failure) and returning tickets in Jira with reproduction PoCs
- VM cleanup PowerShell script (5 VMs, ~ 50 GB/week cleared, eliminating storage exhaustion)
- Application certificate renewal and CA certificate creation
- Python/Locust load testing under concurrent load
- TypeScript UI automation and input boundary validation

---

If JD is DevSecOps

Focus on

- ADO CI/CD pipeline creation and automation
- VM cleanup PowerShell script (5 VMs, ~ 50 GB/week, auto-triggered)
- Pipeline failure root cause analysis
- Re-testing penetration testing bugs (BOLA, JWT, CSP) and managing defect remediation lifecycle

---

If JD is Security Engineering

Focus on

- Penetration testing vulnerability re-testing and remediation validation
- Automation scripting (PowerShell, Python, TypeScript)
- Azure DevOps and CI/CD orchestration
- Application certificate renewal and CA creation
- VM cleanup automation
- Log analysis and root cause investigation

---

If JD is Detection Engineering

Focus on

- Log analysis and root cause analysis (storage/network failures)
- PowerShell automation
- Pipeline failure investigation

---

If JD is Application Security or Product Security

Focus on

- TypeScript UI automation (enterprise application)
- Python/Locust load testing
- SQL and SSMS (querying, backup/restoration)
- CI/CD pipeline knowledge as integration point for security tooling

---

If JD is API Security

Focus on

- Python/Locust load testing (parallel Chrome instances under load)
- CI/CD pipeline automation
- ADO pipeline management

---

If JD is Red Team

Focus on

- Scripting and automation (PowerShell, Python, TypeScript)
- CI/CD and pipeline knowledge
- Automation tooling

---

# Evidence Confidence

Overall

★★★★★

Reason

All experience is directly performed by the candidate and verified. This experience should always be included in the resume and dynamically rewritten to maximize alignment with the target cybersecurity role while remaining factually accurate.

The VM cleanup PowerShell script is the strongest quantifiable individual contribution from this role and should anchor the Epicor experience bullets whenever possible.
