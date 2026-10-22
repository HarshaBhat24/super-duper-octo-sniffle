#!/usr/bin/env python3
"""
Resume PDF Exporter
Renders a resume HTML file to a clean 1-page PDF using headless Chromium.

Usage:
    python3 engine/export_pdf.py [input_html_path] [output_pdf_path]
"""

import sys
import shutil
import subprocess
from pathlib import Path

def find_browser() -> str:
    """Finds an available Chromium or Chrome executable."""
    candidates = [
        "chromium",
        "google-chrome",
        "google-chrome-stable",
        "chromium-browser",
        "chrome",
    ]
    for c in candidates:
        path = shutil.which(c)
        if path:
            return path
    return "chromium"

def export_to_pdf(input_html: str, output_pdf: str = None) -> bool:
    input_path = Path(input_html).resolve()
    if not input_path.exists():
        print(f"Error: Input file '{input_html}' does not exist.")
        return False
    
    if output_pdf is None:
        output_path = input_path.with_suffix(".pdf")
    else:
        output_path = Path(output_pdf).resolve()

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    browser_bin = find_browser()

    cmd = [
        browser_bin,
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--no-pdf-header-footer",
        "--user-data-dir=/tmp/chromium-profile",
        f"--print-to-pdf={output_path}",
        str(input_path),
    ]

    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(f"Successfully generated PDF: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error exporting PDF: {e.stderr.decode('utf-8', errors='ignore')}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        default_template = Path(__file__).resolve().parent.parent / "templates" / "resume_template.html"
        default_out = Path(__file__).resolve().parent.parent / "outputs" / "resume.pdf"
        print(f"No arguments provided. Rendering default template:\n  Input: {default_template}\n  Output: {default_out}")
        export_to_pdf(str(default_template), str(default_out))
    elif len(sys.argv) == 2:
        export_to_pdf(sys.argv[1])
    else:
        export_to_pdf(sys.argv[1], sys.argv[2])
