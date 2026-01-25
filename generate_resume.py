"""
generate_resume.py

Render an HTML + PDF resume from YAML/JSON data, HTML template, and CSS files.
Generates both a visually appealing version and an ATS-optimized version.
Uses Playwright for PDF generation to support modern CSS (Grid, Flexbox, etc.)

Usage:
    pip install jinja2 playwright pyyaml
    playwright install chromium

    python generate_resume.py

This will read resume.yaml (or resume.json) and produce:
    - resume.html / resume.pdf (visually appealing version)
    - resume_ats.html / resume_ats.pdf (ATS-optimized version)
"""

import json
import yaml
from pathlib import Path
from jinja2 import Template
from playwright.sync_api import sync_playwright


def load_resume_data() -> dict:
    """Load resume data from YAML or JSON file."""
    yaml_path = Path("resume.yaml")
    json_path = Path("resume.json")

    if yaml_path.exists():
        content = yaml_path.read_text(encoding='utf-8')
        return yaml.safe_load(content)
    elif json_path.exists():
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        raise FileNotFoundError("Neither resume.yaml nor resume.json found")


def load_template(template_path: str = "resume_template.html") -> Template:
    """Load and return the Jinja2 template."""
    template_content = Path(template_path).read_text(encoding='utf-8')
    return Template(template_content)


def save_html_and_pdf(
    data: dict,
    template: Template,
    html_path: str = "resume.html",
    pdf_path: str = "resume.pdf"
):
    """Generate and save both HTML and PDF versions of the resume using Playwright."""
    # Generate HTML
    html_content = template.render(**data)
    Path(html_path).write_text(html_content, encoding="utf-8")
    print(f"Saved HTML -> {html_path}")

    # Generate PDF using Playwright (Chromium browser engine)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the HTML file
        page.goto(f'file://{Path(html_path).absolute()}')

        # Wait for page to be fully loaded
        page.wait_for_load_state('networkidle')

        # Generate PDF with proper settings
        page.pdf(
            path=pdf_path,
            format='A4',
            margin={
                'top': '10mm',
                'right': '10mm',
                'bottom': '10mm',
                'left': '10mm'
            },
            print_background=True  # Include background colors/images
        )

        browser.close()

    print(f"Saved PDF  -> {pdf_path}")


if __name__ == "__main__":
    # Load resume data
    resume_data = load_resume_data()

    print("Generating visually appealing version...")
    # Load visual template
    template_visual = load_template("resume_template.html")
    # Generate visual output files
    save_html_and_pdf(
        resume_data,
        template_visual,
        "resume.html",
        "resume.pdf"
    )

    print("\nGenerating ATS-optimized version...")
    # Load ATS template
    template_ats = load_template("resume_template_ats.html")
    # Generate ATS output files
    save_html_and_pdf(
        resume_data,
        template_ats,
        "resume_ats.html",
        "resume_ats.pdf"
    )

    print("\n✓ Both resume versions generated successfully!")
    print("  Visual version uses modern CSS Grid layout")
    print("  ATS version uses simple single-column layout")
