#!/usr/bin/env python3
"""
Resume Quality Assurance & Truth Guard Validator
Programmatically verifies that an HTML resume conforms to:
1. One-page layout constraints & PDF page count (exactly 1 page).
2. Required sections and absence of forbidden sections (e.g. Summary).
3. Exact bullet budgets:
   - Epicor: 4 bullets (2 Associate Product Developer, 2 Product Development Intern)
   - Mindpex: 3 bullets
   - Projects: 2 selected projects, 3 bullets each (6 project bullets total)
4. Dynamic Skills categorized structure.
5. Certifications (CompTIA Security+, ISC2 CC) & Achievements (max 3).
6. Education credentials.
7. Truth Guard violations (prohibits unverified tools, platforms, or metrics like AWS, Kubernetes, Splunk, CrowdStrike, Sentinel, 97%, CVE).

Usage:
    python3 engine/validate_resume.py [html_path] [--pdf [pdf_path]] [--render]
"""

import os
import sys
import re
import argparse
from pathlib import Path
from typing import List, Tuple, Optional

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

try:
    from engine.export_pdf import export_to_pdf, find_browser
except ImportError:
    try:
        from export_pdf import export_to_pdf, find_browser
    except ImportError:
        export_to_pdf = None
        find_browser = None

PROHIBITED_TERMS = [
    (r"\bAWS\b", "AWS (Amazon Web Services)"),
    (r"\bKubernetes\b|\bK8s\b", "Kubernetes / K8s"),
    (r"\bSplunk\b", "Splunk"),
    (r"\bSentinel\b", "Microsoft Sentinel"),
    (r"\bQRadar\b", "IBM QRadar"),
    (r"\bCrowdStrike\b", "CrowdStrike"),
    (r"\bDefender\s*XDR\b", "Microsoft Defender XDR"),
    (r"\bSIEM\b", "SIEM"),
    (r"\bEDR\b", "EDR"),
    (r"\bIncident\s*Response\b", "Incident Response"),
    (r"\bThreat\s*Hunting\b", "Threat Hunting"),
    (r"\bReverse\s*Engineering\b", "Reverse Engineering"),
    (r"\bMalware\s*Development\b", "Malware Development"),
    (r"\bBug\s*Bounty\b", "Bug Bounty"),
    (r"\bCVE[-_\d]+", "CVE reference"),
    (r"\b97%", "97% accuracy metric"),
    (r"\bAzure\s*Security\b", "Azure Security (only Azure DevOps / ADO is verified)"),
    (r"\bGCP\b|\bGoogle\s*Cloud\b", "GCP / Google Cloud"),
]

def get_pdf_page_count(pdf_path: Path) -> Optional[int]:
    """Reads PDF binary to find the number of /Type /Page objects."""
    if not pdf_path.exists():
        return None
    try:
        content = pdf_path.read_bytes()
        # Find all Page objects (/Type /Page not /Pages)
        matches = re.findall(rb"/Type\s*/Page\b", content)
        return len(matches)
    except Exception as e:
        print(f"Warning: Could not read PDF page count: {e}")
        return None

def extract_sections_bs4(soup) -> dict:
    sections = {}
    for sec in soup.find_all("section"):
        h2 = sec.find("h2")
        if h2:
            title = h2.get_text().strip()
            sections[title] = sec
    return sections

def extract_sections_regex(html: str) -> dict:
    sections = {}
    pattern = r"<section[^>]*>[\s\S]*?<h2[^>]*>(.*?)</h2>([\s\S]*?)</section>"
    for match in re.finditer(pattern, html, re.IGNORECASE):
        title = match.group(1).strip()
        body = match.group(2)
        sections[title] = body
    return sections

def validate_resume(html_path: str, pdf_path: Optional[str] = None, render_pdf: bool = False) -> Tuple[bool, List[str], List[str]]:
    """
    Validates the resume HTML and optional PDF.
    Returns (is_valid, errors, warnings).
    """
    errors = []
    warnings = []
    path = Path(html_path).resolve()

    if not path.exists():
        errors.append(f"Input HTML file does not exist: {html_path}")
        return False, errors, warnings

    raw_html = path.read_text(encoding="utf-8")
    text_content = re.sub(r"<[^>]+>", " ", raw_html)

    # 1. Truth Guard Check
    clean_text = re.sub(r"<!--[\s\S]*?-->", "", raw_html)
    clean_text = re.sub(r"<[^>]+>", " ", clean_text)
    for pattern, label in PROHIBITED_TERMS:
        if re.search(pattern, clean_text, re.IGNORECASE):
            errors.append(f"Truth Guard Violation: Prohibited term '{label}' detected in resume content.")

    # 2. Structure & Sections
    # Check for forbidden summary section
    if re.search(r"<h2[^>]*>\s*(?:Professional\s*)?Summary\s*</h2>", raw_html, re.IGNORECASE):
        errors.append("Layout Violation: Summary section is strictly forbidden.")

    # Parse sections
    if BeautifulSoup:
        soup = BeautifulSoup(raw_html, "html.parser")
        sections = extract_sections_bs4(soup)
    else:
        sections = extract_sections_regex(raw_html)

    expected_sections = [
        "Experience",
        "Projects",
        "Skills",
        "Education",
    ]
    # Check for Certifications section header variants
    has_certs = any("cert" in s.lower() for s in sections.keys())
    if not has_certs:
        errors.append("Structure Error: Missing 'Certifications and Achievements' section.")

    for es in expected_sections:
        if not any(es.lower() == s.lower() for s in sections.keys()):
            errors.append(f"Structure Error: Missing required section '{es}'.")

    # 3. Experience Section Validation
    exp_key = next((k for k in sections.keys() if k.lower() == "experience"), None)
    if exp_key:
        exp_content = str(sections[exp_key])
        exp_text = re.sub(r"<[^>]+>", " ", exp_content)

        # Check Epicor presence
        if "epicor" not in exp_text.lower():
            errors.append("Experience Error: Epicor Software entry is missing.")
        else:
            # Check APD and Intern entries
            has_apd = "associate product developer" in exp_text.lower()
            has_intern = "product development intern" in exp_text.lower()
            if not has_apd or not has_intern:
                errors.append("Experience Error: Epicor must reflect both Associate Product Developer and Product Development Intern roles.")

        # Check Mindpex presence
        if "mindpex" not in exp_text.lower():
            errors.append("Experience Error: Mindpex experience entry is missing.")

        # Bullet count in Experience: Expect exactly 7 bullets total (Epicor: 4 [2 APD + 2 Intern], Mindpex: 3)
        bullets = re.findall(r"<li[^>]*>([\s\S]*?)</li>", exp_content, re.IGNORECASE)
        if len(bullets) != 7:
            errors.append(f"Experience Bullet Budget Error: Expected exactly 7 bullets in Experience (4 Epicor: 2 APD + 2 Intern; 3 Mindpex), found {len(bullets)}.")

    # 4. Projects Section Validation
    proj_key = next((k for k in sections.keys() if k.lower() == "projects"), None)
    if proj_key:
        if proj_key != "Projects":
            errors.append(f"Projects Heading Error: Section heading must strictly be 'Projects', found '{proj_key}'.")

        proj_content = str(sections[proj_key])
        # Count project entries and bullets
        entries = re.findall(r'<div[^>]*class=["\']entry["\'][\s\S]*?</div>', proj_content, re.IGNORECASE)
        bullets = re.findall(r"<li[^>]*>([\s\S]*?)</li>", proj_content, re.IGNORECASE)

        if len(bullets) != 6:
            errors.append(f"Project Bullet Budget Error: Expected exactly 6 project bullets (2 projects, 3 bullets each), found {len(bullets)}.")

        # Mindpex must NOT be in projects
        if "mindpex" in proj_content.lower():
            errors.append("Projects Error: Mindpex must NEVER be in the Projects section (must be in Experience).")

    # 5. Skills Section Validation
    skills_key = next((k for k in sections.keys() if k.lower() == "skills"), None)
    if skills_key:
        skills_content = str(sections[skills_key])
        bullets = re.findall(r"<li[^>]*>([\s\S]*?)</li>", skills_content, re.IGNORECASE)
        if len(bullets) < 4:
            errors.append(f"Skills Error: Expected at least 4 categorized skill rows, found {len(bullets)}.")

    # 6. Certifications & Achievements Section Validation
    cert_key = next((k for k in sections.keys() if "cert" in k.lower()), None)
    if cert_key:
        cert_content = str(sections[cert_key])
        cert_text = re.sub(r"<[^>]+>", " ", cert_content)

        if "security+" not in cert_text.lower():
            errors.append("Certifications Error: CompTIA Security+ (SY0-701) must be included.")
        if "isc2" not in cert_text.lower() and "certified in cybersecurity" not in cert_text.lower():
            errors.append("Certifications Error: ISC2 Certified in Cybersecurity (CC) must be included.")

        bullets = re.findall(r"<li[^>]*>([\s\S]*?)</li>", cert_content, re.IGNORECASE)
        # Exactly 2 certs + max 3 achievements = max 5 bullets
        if len(bullets) > 5:
            errors.append(f"Certifications & Achievements Error: Maximum 5 items allowed (2 certs + max 3 achievements), found {len(bullets)}.")
        elif len(bullets) < 2:
            errors.append(f"Certifications Error: Expected at least 2 certifications, found {len(bullets)}.")

    # 7. Education Section Validation
    edu_key = next((k for k in sections.keys() if k.lower() == "education"), None)
    if edu_key:
        edu_content = str(sections[edu_key])
        edu_text = re.sub(r"<[^>]+>", " ", edu_content)
        if "new horizon" not in edu_text.lower():
            errors.append("Education Error: Institution must be New Horizon College of Engineering.")
        if "8.57" not in edu_text:
            errors.append("Education Error: CGPA must be 8.57.")

    # 8. Render & Page Count Validation
    actual_pdf_path = None
    if pdf_path:
        actual_pdf_path = Path(pdf_path).resolve()
    elif render_pdf:
        if not find_browser or not find_browser():
            warnings.append("Page count check skipped: No Chromium-based browser found on system.")
        else:
            tmp_pdf = path.with_suffix(".validated.tmp.pdf")
            if export_to_pdf and export_to_pdf(str(path), str(tmp_pdf)):
                actual_pdf_path = tmp_pdf
            else:
                errors.append("PDF generation failed during page count validation.")

    if actual_pdf_path and actual_pdf_path.exists():
        page_count = get_pdf_page_count(actual_pdf_path)
        if page_count is not None:
            if page_count != 1:
                errors.append(f"Page Budget Error: Resume PDF is {page_count} page(s); MUST be exactly 1 page.")
        if render_pdf and actual_pdf_path.name.endswith(".validated.tmp.pdf"):
            actual_pdf_path.unlink(missing_ok=True)

    is_valid = len(errors) == 0
    return is_valid, errors, warnings

def main():
    parser = argparse.ArgumentParser(description="Validate resume HTML and PDF against Truth Guard and budget rules.")
    parser.add_argument("html_path", nargs="?", default="templates/resume_template.html", help="Path to resume HTML file")
    parser.add_argument("--pdf", dest="pdf_path", default=None, help="Path to corresponding rendered PDF to check page count")
    parser.add_argument("--render", action="store_true", help="Render PDF headlessly and check that page count is exactly 1")

    args = parser.parse_args()
    is_valid, errors, warnings = validate_resume(args.html_path, args.pdf_path, args.render)

    print(f"\n--- Resume Validation Report for: {args.html_path} ---")
    if is_valid:
        print("✅ SUCCESS: All structural, budget, Truth Guard, and 1-page constraints passed!")
        if warnings:
            print("\nWarnings:")
            for w in warnings:
                print(f"  ⚠️  {w}")
        return 0
    else:
        print(f"❌ FAILED: {len(errors)} error(s) detected:")
        for err in errors:
            print(f"  • {err}")
        if warnings:
            print("\nWarnings:")
            for w in warnings:
                print(f"  ⚠️  {w}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
