# Projects Knowledge Base

> This document is the authoritative knowledge base for all candidate projects.
>
> It is intended for LLM consumption only.
>
> Never copy this document into a resume.
>
> Resume bullets must always be generated after analyzing the target Job Description.
>
> Choose ONLY the most relevant project(s) for the target role.
>
> Never fabricate responsibilities or technologies.

---

# Resume Selection Rules

Candidate has two software projects.

- VigiLynx
- CipherCrack

A separate Security Assessment exists in:

04_security_assessments.md

Do NOT automatically include both projects.

The resume generator should choose the strongest projects according to the target role.

Priority Matrix

| Role | Priority 1 | Priority 2 |
|--------|------------|------------|
| SOC | VigiLynx | CipherCrack |
| Detection Engineering | VigiLynx | CipherCrack |
| Threat Intelligence | VigiLynx | CipherCrack |
| Security Engineering | VigiLynx | Security Assessment |
| Application Security | Security Assessment | VigiLynx |
| Product Security | Security Assessment | VigiLynx |
| Red Team | Security Assessment | CipherCrack |
| Pentesting | Security Assessment | CipherCrack |
| Security Research | CipherCrack | Security Assessment |

---

# PROJECT 1

# VigiLynx

Project Type

Hackathon Project

Duration

Apr 2025 – Jun 2025

Team Size

4

Achievement

Winner

HackAthena'25 Cybersecurity Track

---

## Overview

VigiLynx is a cybersecurity platform consisting of

- Chrome Extension
- Web Application
- Backend Services
- Threat Dashboard

Primary objective

Protect users from

- Phishing URLs
- Malicious files

using real-time detection workflows.

---

# Candidate Contributions

Candidate contributed to

- Chrome Extension development
- Backend integration
- Authentication
- Database schema
- Dashboard development
- Threat visualization
- URL detection
- Malware detection integration

---

# Architecture

Frontend

React.js

Backend

Node.js

Database

Supabase

Browser Extension

JavaScript

Chrome Extension APIs

Threat Intelligence

VirusTotal API

Machine Learning

Random Forest

---

# Detection Pipeline

Workflow

User visits URL

↓

Extension intercepts request

↓

URL features extracted

↓

Random Forest classification

↓

Threat verdict

↓

Browser alert

↓

Dashboard logging

---

# URL Detection

Technique

Feature Extraction

Model

Random Forest

Detection Concepts

- URL structure analysis

- Suspicious domains

- Subdomain abuse

- Phishing indicators

Applicable Roles

- Detection Engineering

- SOC

- Threat Intelligence

Priority

★★★★★

---

# Malware Detection

Technique

VirusTotal API Integration

Workflow

- File submission

- Hash lookup

- Detection parsing

- Verdict generation

Security Concepts

- Threat Intelligence

- Malware Analysis

- IOC Validation

Applicable Roles

- Detection Engineering

- SOC

- Threat Intelligence

Priority

★★★★★

---

# Chrome Extension

Built

- Real-time URL inspection

- Browser interception

- Popup alerts

- Backend communication

Security Concepts

- Browser Security

- Client-side detection

- Attack surface monitoring

Applicable Roles

- Product Security

- Detection Engineering

- AppSec

Priority

★★★★★

---

# Backend

Contributions

- Authentication

- Database schema

- API integration

- Extension communication

Security Concepts

- Authentication

- Secure backend design

- User management

Applicable Roles

- Product Security

- Application Security

Priority

★★★★☆

---

# Dashboard

Built

- Detection statistics

- Threat visibility

- Authentication

- User monitoring

Security Concepts

- Monitoring

- Threat visualization

- Detection reporting

Applicable Roles

- SOC

- Detection Engineering

Priority

★★★★☆

---

# Metrics

URLs Tested

1000+

Files Scanned

50+

Users

~10

Hackathon

48 hours

---

# Security Concepts

- Threat Detection

- Malware Detection

- URL Intelligence

- Browser Security

- Authentication

- Threat Visibility

- Threat Intelligence

- Security Automation

---

# ATS Keywords

High Priority

- Threat Detection

- Phishing Detection

- Malware Analysis

- URL Analysis

- Browser Extension

- VirusTotal

- Random Forest

- Threat Intelligence

- Authentication

- Chrome Extension

- Detection Pipeline

Medium Priority

- React

- Node.js

- Supabase

---

# Technologies

Programming

- JavaScript

Frameworks

- React

Runtime

- Node.js

Database

- Supabase

Security

- VirusTotal API

- Random Forest

- Chrome Extension APIs

Version Control

- Git

---

# Role Mapping

SOC

★★★★★

Emphasize

- Detection

- Monitoring

- Malware

- Threat visibility

Suppress

- React

---

Detection Engineering

★★★★★

Emphasize

- Feature extraction

- Detection pipeline

- Alert generation

- Random Forest

---

Threat Intelligence

★★★★★

Emphasize

- VirusTotal

- IOC

- Threat enrichment

---

Application Security

★★★★☆

Emphasize

- Authentication

- Backend

- Secure workflows

---

Product Security

★★★★★

Emphasize

- Browser security

- Authentication

- Secure architecture

---

Red Team

★★★☆☆

Only emphasize

- Phishing indicators

- Browser attack surface

---

# Never Emphasize

Unless JD explicitly requests frontend

Do not focus on

- React components

- UI implementation

- Styling

- Generic frontend

---

# PROJECT 2

# CipherCrack

Project Type

Personal Project

Duration

Jun 2025 – Present

Developer

Individual

---

# Overview

Offline Python cryptography toolkit.

Purpose

Provide a centralized CLI utility for

- Cryptography

- CTF competitions

- Cipher experimentation

- Cryptanalysis

---

# Implemented Ciphers

- Caesar

- Affine

- Atbash

- Baconian

- Vigenère

- Monoalphabetic

- Hill

- Four Square

- ROT13

---

# Features

- Encryption

- Decryption

- Brute force

- Key validation

- Error handling

- Modular CLI

---

# Automation

Implemented

- Caesar brute forcing

- Cipher automation

- Workflow optimization

Purpose

Reduce repetitive work during CTFs.

---

# Mathematical Concepts

- Modular arithmetic

- Matrix multiplication

- Matrix inversion

- Determinants

- Linear algebra

---

# Architecture

CLI

Menu driven

Language

Python

Design

Modular

Reusable

Independent cipher implementations

---

# Real Usage

Used during

10–20 CTF competitions

Purpose

Rapid cryptanalysis.

---

# Metrics

Codebase

1324+ LOC

Supported Algorithms

9

---

# Security Concepts

- Cryptography

- Cryptanalysis

- Automation

- Brute force

- Classical ciphers

- CLI tooling

- Security scripting

---

# ATS Keywords

High Priority

- Cryptography

- Cryptanalysis

- Python

- CLI

- Automation

- Brute Force

- Modular Programming

- Security Tooling

Medium Priority

- Matrix Operations

- Linear Algebra

- argparse

---

# Technologies

Language

Python

Libraries

- argparse

- itertools

- math

- string

---

# Role Mapping

Red Team

★★★★★

Emphasize

- Offensive tooling

- Automation

- Cryptanalysis

- Brute force

---

Security Research

★★★★★

Emphasize

- Algorithm implementation

- Mathematical cryptography

- Research tooling

---

Detection Engineering

★★★★☆

Emphasize

- Automation

- Modular architecture

---

SOC

★★☆☆☆

Only mention

- Cryptography fundamentals

---

Threat Intelligence

★★☆☆☆

Mention only if cryptography appears in JD.

---

Application Security

★★★☆☆

Mention

- Secure implementation

- Validation

---

# Never Emphasize

Do not focus on

- Python syntax

- Educational value

- Beginner CLI

Instead emphasize

- Security tooling

- Offensive automation

- Cryptanalysis workflows

---

# Resume Generation Rules

Exactly three bullets.

Maximum two lines per bullet.

Every bullet must contain

Action

↓

Technical implementation

↓

Security relevance

↓

Impact

Choose the strongest contributions after analyzing the Job Description.

Never use generic software engineering language when a cybersecurity equivalent exists.

Examples

Good

"Implemented Random Forest–based phishing detection workflows to analyze 1,000+ URLs and generate real-time browser alerts through a Chrome extension."

Good

"Developed an offline cryptanalysis toolkit implementing nine classical ciphers with automated brute-force workflows used during CTF competitions."

Bad

"Worked on frontend."

Bad

"Built a Python project."

Bad

"Used React and Node.js."
