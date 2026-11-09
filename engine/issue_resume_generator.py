#!/usr/bin/env python3
"""
Issue-driven Resume Generator
Parses GitHub Issue or workflow dispatch inputs, extracts target company & HTML,
and generates S-Harsha_Bhat_{company-name}.pdf.
"""

import os
import sys
import json
import re
import uuid
from pathlib import Path
try:
    from engine.export_pdf import export_to_pdf
    from engine.validate_resume import validate_resume
except ImportError:
    from export_pdf import export_to_pdf
    from validate_resume import validate_resume

def set_github_output(name: str, value: str):
    """Writes an output parameter to GITHUB_OUTPUT for GitHub Actions."""
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8") as f:
        if "\n" in value:
            delimiter = uuid.uuid4().hex
            f.write(f"{name}<<{delimiter}\n{value}\n{delimiter}\n")
        else:
            f.write(f"{name}={value}\n")

def sanitize_company_name(name: str) -> str:
    """Sanitizes company name for clean file naming."""
    # Replace spaces and special characters with underscores
    slug = re.sub(r"[^\w\-]+", "_", name.strip())
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "General"

def extract_from_issue(title: str, body: str, labels: list = None):
    """Extracts company name and HTML content from issue title and body."""
    labels = labels or []
    is_resume_issue = any(l.lower() in ["resume", "generate-resume"] for l in labels)
    
    # 1. Company Name
    company = None
    # Check for Issue Form pattern: ### Target Company Name or ### Company Name
    m_comp = re.search(r"###\s*(?:Target\s*)?Company\s*(?:Name)?\s*\n+([^\n#]+)", body, re.IGNORECASE)
    if m_comp:
        company = m_comp.group(1).strip()
    
    if not company:
        # Extract from title: e.g. "[Resume] Google", "Resume: Google", "Google"
        clean_title = re.sub(r"^\[?(?:resume|generate resume)\]?[:\s\-]*", "", title, flags=re.IGNORECASE).strip()
        if clean_title:
            company = clean_title
        else:
            company = "General"

    company_slug = sanitize_company_name(company)

    # 2. Extract HTML content
    # Check if inside Issue Form section: ### Resume HTML
    m_html_section = re.search(r"###\s*Resume HTML(?:\s*Code)?\s*\n+([\s\S]+)", body, re.IGNORECASE)
    candidate_body = m_html_section.group(1) if m_html_section else body

    # Check for markdown code fences: ```html ... ``` or ``` ... ```
    m_code_block = re.search(r"```(?:html)?\s*([\s\S]*?)```", candidate_body, re.IGNORECASE)
    if m_code_block:
        candidate_html = m_code_block.group(1).strip()
    else:
        candidate_html = candidate_body.strip()

    # Validate that candidate looks like HTML
    lower_cand = candidate_html.lower()
    has_html_tags = any(tag in lower_cand for tag in ["<!doctype", "<html", "<head", "<body", "<style", "<div"])

    if not has_html_tags:
        # If this wasn't clearly an issue intended for resume generation, skip it
        if not is_resume_issue and not re.search(r"^\[?(?:resume)\]?", title, re.IGNORECASE):
            return None, None, None, "skipped"
        return company, company_slug, None, "missing_html"

    return company, company_slug, candidate_html, "valid"

def main():
    repo_root = Path(__file__).resolve().parent.parent
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    
    company_name = "General"
    company_slug = "General"
    html_content = None
    issue_number = ""

    # Check CLI arguments first (allows manual testing or programmatic subprocessing)
    if len(sys.argv) > 1:
        print("Running in CLI standalone mode...")
        company_name = sys.argv[1]
        company_slug = sanitize_company_name(company_name)
        if len(sys.argv) > 2:
            html_file = Path(sys.argv[2])
            if html_file.exists():
                html_content = html_file.read_text(encoding="utf-8")
        if not html_content:
            default_template = repo_root / "templates" / "resume_template.html"
            if default_template.exists():
                html_content = default_template.read_text(encoding="utf-8")

    # If no CLI arguments provided, check GitHub Actions event
    elif event_path and os.path.exists(event_path):
        with open(event_path, "r", encoding="utf-8") as f:
            event = json.load(f)
        
        # Scenario A: Triggered by an Issue
        if "issue" in event:
            issue = event["issue"]
            issue_number = str(issue.get("number", ""))
            title = issue.get("title", "")
            body = issue.get("body", "") or ""
            labels = [lbl.get("name", "") if isinstance(lbl, dict) else str(lbl) for lbl in issue.get("labels", [])]
            
            comp, slug, html, status = extract_from_issue(title, body, labels)
            if status == "skipped":
                print("Issue is not a resume generation request. Skipping.")
                set_github_output("status", "skipped")
                return 0
            if status == "missing_html":
                err = "No valid HTML code found in the issue body. Please paste complete resume HTML."
                print(f"Error: {err}")
                set_github_output("status", "error")
                set_github_output("error_message", err)
                set_github_output("issue_number", issue_number)
                return 0
            
            company_name = comp
            company_slug = slug
            html_content = html

        # Scenario B: Triggered by workflow_dispatch
        elif "inputs" in event:
            inputs = event["inputs"]
            company_name = inputs.get("company_name", "General") or "General"
            company_slug = sanitize_company_name(company_name)
            
            raw_html = inputs.get("raw_html", "")
            html_file = inputs.get("html_file_path", "")
            
            if raw_html and raw_html.strip():
                html_content = raw_html.strip()
            elif html_file and (repo_root / html_file).exists():
                html_content = (repo_root / html_file).read_text(encoding="utf-8")
            else:
                err = "No HTML content or valid HTML file path provided in workflow inputs."
                print(f"Error: {err}")
                set_github_output("status", "error")
                set_github_output("error_message", err)
                return 0
        else:
            # Running in CI on push/PR where GITHUB_EVENT_PATH exists but isn't an issue or dispatch
            print("Running in non-issue event environment without CLI arguments. Loading default template...")
            default_template = repo_root / "templates" / "resume_template.html"
            if default_template.exists():
                html_content = default_template.read_text(encoding="utf-8")
    else:
        # CLI fallback for manual testing without arguments
        print("Running in CLI standalone mode without arguments...")
        default_template = repo_root / "templates" / "resume_template.html"
        if default_template.exists():
            html_content = default_template.read_text(encoding="utf-8")

    if not html_content:
        err = "Could not resolve HTML content."
        print(f"Error: {err}")
        set_github_output("status", "error")
        set_github_output("error_message", err)
        return 1

    # Desired file name format: S-Harsha_Bhat_{company-name}.pdf
    pdf_filename = f"S-Harsha_Bhat_{company_slug}.pdf"
    html_filename = f"S-Harsha_Bhat_{company_slug}.html"

    outputs_dir = repo_root / "outputs"
    outputs_dir.mkdir(parents=True, exist_ok=True)

    target_html_path = outputs_dir / html_filename
    target_pdf_path = outputs_dir / pdf_filename

    target_html_path.write_text(html_content, encoding="utf-8")
    print(f"Saved input HTML to: {target_html_path}")

    # Generate PDF
    success = export_to_pdf(str(target_html_path), str(target_pdf_path))
    if not success:
        err = f"Failed to generate PDF from {target_html_path}"
        set_github_output("status", "error")
        set_github_output("error_message", err)
        if issue_number:
            set_github_output("issue_number", issue_number)
        return 1

    # Validate generated resume (Truth Guard, bullet budget, 1-page fit)
    is_valid, val_errors, _ = validate_resume(str(target_html_path), str(target_pdf_path))
    if not is_valid:
        err = "Resume validation failed:\n• " + "\n• ".join(val_errors)
        print(f"Error: {err}")
        set_github_output("status", "error")
        set_github_output("error_message", err)
        if issue_number:
            set_github_output("issue_number", issue_number)
        return 1

    print(f"Successfully generated: {target_pdf_path}")
    set_github_output("status", "success")
    set_github_output("company_name", company_name)
    set_github_output("company_slug", company_slug)
    set_github_output("pdf_filename", pdf_filename)
    set_github_output("pdf_path", f"outputs/{pdf_filename}")
    set_github_output("html_path", f"outputs/{html_filename}")
    if issue_number:
        set_github_output("issue_number", issue_number)

    # Optional: Append record to outputs/log.md Markdown table
    log_file = repo_root / "outputs" / "log.md"
    if log_file.exists() and not company_name.startswith("UnitTest"):
        try:
            import datetime
            today = datetime.date.today().isoformat()
            log_entry = f"| {today} | {company_name} | Customized Resume | GitHub Actions / Issue | Epicor + Mindpex | Dynamic Selection (2 of 3) | {pdf_filename} |\n"
            content = log_file.read_text(encoding="utf-8")
            if log_entry not in content and "\n---\n" in content:
                parts = content.split("\n---\n", 1)
                new_content = parts[0].rstrip() + "\n" + log_entry + "\n---\n" + parts[1]
                log_file.write_text(new_content, encoding="utf-8")
        except Exception as e:
            print(f"Warning: Could not update log.md: {e}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
