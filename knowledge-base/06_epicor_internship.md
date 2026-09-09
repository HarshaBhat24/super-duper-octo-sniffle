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

Role

Product Development Intern

Duration

October 2025 – Present

Type

Full-time Internship

Location

Bengaluru, India

---

# Experience Summary

Worked within an enterprise software product development organization on CI/CD pipeline automation, DevOps scripting, environment reliability engineering, UI automation, and load testing.

Core work:

- Creating and maintaining Azure DevOps (ADO) pipelines for CI/CD orchestration, where each pipeline runs against agent VMs executing PowerShell scripts
- Writing PowerShell scripts that execute on agent VMs within ADO pipelines (build, provisioning, automation tasks)
- Authored a PowerShell cleanup script deployed across 5 agent VMs via an ADO pipeline — auto-triggered weekly, clearing ~15 GB of logs and temp data per run, significantly reducing pipeline failures caused by storage exhaustion
- UI automation of an enterprise application using TypeScript (click interactions, app navigation, workflow automation)
- Wrote and executed a Python/Locust load testing script that opened multiple parallel Chrome instances and performed UI interactions against the application URL under load
- SQL querying and data retrieval using Microsoft SSMS; performed database backup and restoration
- Log analysis and root cause analysis for pipeline and script execution failures (storage exhaustion, network issues, execution errors)
- Worked within Agile delivery cycles using Azure DevOps Boards and JIRA

Although the role is a product development position, the skills directly map to DevSecOps, Security Automation, Security Engineering, and Detection Engineering.

---

# Primary Responsibilities

- Azure DevOps (ADO) CI/CD pipeline creation and management
- PowerShell scripting for pipeline automation and agent VM task execution
- VM cleanup automation — authored script deployed across 5 VMs, auto-triggered via ADO pipeline
- UI automation using TypeScript (enterprise application click/navigation automation)
- Python/Locust load testing script development and execution
- SQL querying and data retrieval (Microsoft SSMS)
- Database backup and restoration (Microsoft SSMS)
- Log analysis and root cause analysis of pipeline and script failures
- Agile delivery (JIRA, Azure DevOps Boards)

---

# Technical Responsibilities

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

## VM Cleanup PowerShell Script — Star Achievement

This is the single most impactful individual contribution from this internship.

Written

- From scratch — no prior script existed

Scope

- Deployed across 5 agent VMs

Trigger

- Auto-triggered weekly via an ADO pipeline

Function

- Clears logs and temporary data that accumulate in agent VMs during pipeline runs

Impact

- Clears approximately 15 GB of junk data per weekly run
- Directly reduced pipeline failures caused by storage exhaustion in VMs
- Improved overall pipeline reliability and reduced manual intervention

Security Relevance

High

Concepts

- Automated log management and cleanup
- Scripted environment hygiene — reduces configuration drift and execution errors
- Scheduled automation for operational reliability

Applicable Roles

- DevSecOps
- Security Automation
- Security Engineering
- Detection Engineering

Resume Priority

HIGHEST — always include this in at least one bullet

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
- Executed the script personally — both wrote and ran the load tests

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
- VM cleanup script (5 VMs, 15GB/week, ADO-triggered)
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
- VM cleanup PowerShell script (5 VMs, 15GB/week, ADO-triggered)
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

Medium

Emphasize

- TypeScript UI automation (enterprise app)
- Python/Locust load testing
- SQL and SSMS usage
- CI/CD pipeline knowledge (integration point for security tooling)

Suppress

- QA/testing terminology

---

## Red Team

Priority

Medium

Emphasize

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

Generate exactly 3 bullets.

Maximum 2 lines per bullet.

Each bullet must follow:

Action → Technical implementation → Cybersecurity relevance → Impact

## Preferred Bullet Framings (in order of priority)

Bullet 1 (Always — highest impact):
The VM cleanup PowerShell script:
- Action: Engineered / Developed / Authored
- What: PowerShell cleanup script deployed across 5 agent VMs via automated ADO pipeline
- Impact: Clears ~15 GB of logs and temp data weekly, eliminating pipeline failures caused by storage exhaustion

Bullet 2 (Role-adaptive — DevSecOps / Security Engineering / Automation):
- ADO pipeline creation and CI/CD automation
- PowerShell scripting for pipeline task execution
- Jenkins to Azure DevOps migration support

Bullet 3 (Role-adaptive — choose the strongest match to JD):
- AppSec / ProdSec: TypeScript UI automation of enterprise application
- Detection / SOC: Log-based root cause analysis of pipeline failures (storage, network)
- API Security / AppSec: Python/Locust load testing (parallel Chrome instances, UI interactions under load)
- SQL/Data-adjacent: SQL querying and database backup/restoration using SSMS

## Always Avoid

- "Regression testing", "smoke testing", "test cases", "test execution"
- "QA", "software quality assurance"
- Generic testing language
- Claiming to author Jenkinsfiles or Azure Pipelines YAML as the primary output

## Always Use

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

- Security Analyst
- Penetration Tester
- Detection Engineer title
- SOC Analyst
- Incident Responder
- Adversarial input testing or attack simulation

Never imply

- Production security monitoring
- SIEM administration
- Vulnerability scanning from this role
- Docker or containerization
- Kubernetes or infrastructure design
- Authored Jenkinsfile or Azure Pipelines YAML as the primary deliverable

---

# Dynamic Resume Logic

If JD is DevSecOps

Focus on

- ADO CI/CD pipeline creation and automation
- VM cleanup PowerShell script (5 VMs, 15GB/week, auto-triggered)
- Pipeline failure root cause analysis

---

If JD is Security Engineering

Focus on

- Automation scripting (PowerShell, Python, TypeScript)
- Azure DevOps and CI/CD
- VM cleanup automation
- Log analysis

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
