#!/usr/bin/env python3
"""
Unit and Integration Tests for Resume Engine
Tests export_pdf, issue_resume_generator, and validate_resume.
"""

import os
import sys
import tempfile
import unittest
import subprocess
from pathlib import Path

# Add project root to sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from engine.export_pdf import export_to_pdf, find_browser
from engine.validate_resume import validate_resume

class TestExportPdf(unittest.TestCase):
    def test_find_browser(self):
        browser = find_browser()
        # Ensure it found a valid browser binary or None
        if browser:
            self.assertTrue(Path(browser).exists() or shutil_which_exists(browser))

    def test_export_pdf_missing_file(self):
        res = export_to_pdf("nonexistent_file_12345.html")
        self.assertFalse(res)

    def test_export_pdf_cli_error_code(self):
        cmd = [sys.executable, str(REPO_ROOT / "engine" / "export_pdf.py"), "nonexistent_file_12345.html"]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertNotEqual(res.returncode, 0, "export_pdf.py should exit with non-zero on missing input")

    def test_export_pdf_success(self):
        template = REPO_ROOT / "templates" / "resume_template.html"
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
            out_pdf = f.name
        try:
            res = export_to_pdf(str(template), out_pdf)
            self.assertTrue(res)
            self.assertTrue(Path(out_pdf).exists())
            self.assertGreater(Path(out_pdf).stat().st_size, 1000)
        finally:
            Path(out_pdf).unlink(missing_ok=True)

class TestIssueResumeGenerator(unittest.TestCase):
    def test_module_import_and_cli_execution(self):
        clean_env = {k: v for k, v in os.environ.items() if k != "GITHUB_EVENT_PATH"}
        cmd = [sys.executable, "-m", "engine.issue_resume_generator", "UnitTestCompany"]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=str(REPO_ROOT), env=clean_env)
        self.assertEqual(res.returncode, 0, f"Module execution failed: {res.stderr.decode()}")
        # Clean up generated files
        (REPO_ROOT / "outputs" / "S-Harsha_Bhat_UnitTestCompany.html").unlink(missing_ok=True)
        (REPO_ROOT / "outputs" / "S-Harsha_Bhat_UnitTestCompany.pdf").unlink(missing_ok=True)

        # Verify that UnitTestCompany was NOT written to outputs/log.md
        log_content = (REPO_ROOT / "outputs" / "log.md").read_text(encoding="utf-8")
        self.assertNotIn("UnitTestCompany", log_content, "outputs/log.md should not be polluted with test companies")

    def test_validation_failure_exits_with_error(self):
        clean_env = {k: v for k, v in os.environ.items() if k != "GITHUB_EVENT_PATH"}
        # Create a temporary HTML file violating truth guard
        bad_html = "<html><body><h1>S Harsha Bhat</h1><p>Kubernetes AWS Splunk</p></body></html>"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False, encoding="utf-8") as f:
            f.write(bad_html)
            tmp_path = f.name
        try:
            cmd = [sys.executable, "-m", "engine.issue_resume_generator", "UnitTestBad", tmp_path]
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=str(REPO_ROOT), env=clean_env)
            self.assertEqual(res.returncode, 1, "issue_resume_generator should exit 1 on validation failure")
            self.assertIn("Resume validation failed", res.stdout.decode() + res.stderr.decode())
        finally:
            Path(tmp_path).unlink(missing_ok=True)
            (REPO_ROOT / "outputs" / "S-Harsha_Bhat_UnitTestBad.html").unlink(missing_ok=True)
            (REPO_ROOT / "outputs" / "S-Harsha_Bhat_UnitTestBad.pdf").unlink(missing_ok=True)

class TestValidateResume(unittest.TestCase):
    def test_validate_default_template(self):
        template = REPO_ROOT / "templates" / "resume_template.html"
        is_valid, errors, _ = validate_resume(str(template), render_pdf=True)
        self.assertTrue(is_valid, f"Template validation failed with errors: {errors}")

    def test_validate_s_harsha_bhat_html(self):
        resume_html = REPO_ROOT / "S-Harsha-Bhat.html"
        is_valid, errors, _ = validate_resume(str(resume_html), render_pdf=True)
        self.assertTrue(is_valid, f"S-Harsha-Bhat.html validation failed with errors: {errors}")

    def test_truth_guard_catches_violations(self):
        bad_html = "<html><body><h1>S Harsha Bhat</h1><p>Managed AWS infrastructure and Kubernetes clusters with Splunk and 97% accuracy.</p></body></html>"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False, encoding="utf-8") as f:
            f.write(bad_html)
            tmp_path = f.name
        try:
            is_valid, errors, _ = validate_resume(tmp_path)
            self.assertFalse(is_valid)
            violation_str = " ".join(errors)
            self.assertIn("AWS", violation_str)
            self.assertIn("Kubernetes", violation_str)
            self.assertIn("Splunk", violation_str)
            self.assertIn("97%", violation_str)
        finally:
            Path(tmp_path).unlink(missing_ok=True)

    def test_catches_summary_section(self):
        bad_html = "<html><body><section><h2>Summary</h2><p>Experienced engineer</p></section></body></html>"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False, encoding="utf-8") as f:
            f.write(bad_html)
            tmp_path = f.name
        try:
            is_valid, errors, _ = validate_resume(tmp_path)
            self.assertFalse(is_valid)
            self.assertTrue(any("Summary section is strictly forbidden" in e for e in errors))
        finally:
            Path(tmp_path).unlink(missing_ok=True)

def shutil_which_exists(cmd):
    import shutil
    return bool(shutil.which(cmd))

if __name__ == "__main__":
    unittest.main()
