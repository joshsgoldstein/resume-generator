"""
generate_resume.py

Render an HTML + PDF resume from separate JSON, HTML template, and CSS files.
Generates both a visually appealing version and an ATS-optimized version.

Usage:
    pip install jinja2 weasyprint

    python generate_resume.py

This will produce:
    - resume.html / resume.pdf (visually appealing version)
    - resume_ats.html / resume_ats.pdf (ATS-optimized version)
"""

import json
from pathlib import Path
from jinja2 import Template
from weasyprint import HTML


def load_resume_data(json_path: str = "resume_data.json") -> dict:
    """Load resume data from JSON file."""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_template(template_path: str = "resume_template.html") -> Template:
    """Load and return the Jinja2 template."""
    template_content = Path(template_path).read_text(encoding='utf-8')
    return Template(template_content)


def load_css(css_path: str = "resume_style.css") -> str:
    """Load CSS content."""
    return Path(css_path).read_text(encoding='utf-8')


def render_resume_html(data: dict, template: Template, css_content: str, css_link: str) -> str:
    """Render the HTML string from resume data with inline CSS for PDF."""
    html_output = template.render(**data)
    # For PDF generation, we need to inline the CSS
    html_output = html_output.replace(
        f'<link rel="stylesheet" href="{css_link}">',
        f'<style>{css_content}</style>'
    )
    return html_output


def save_html_and_pdf(
    data: dict,
    template: Template,
    css_content: str,
    css_link: str,
    html_path: str = "resume.html",
    pdf_path: str = "resume.pdf"
):
    """Generate and save both HTML and PDF versions of the resume."""
    # For standalone HTML, keep the link tag
    html_standalone = template.render(**data)
    Path(html_path).write_text(html_standalone, encoding="utf-8")

    # For PDF, use inline CSS
    html_for_pdf = render_resume_html(data, template, css_content, css_link)
    HTML(string=html_for_pdf).write_pdf(pdf_path)

    print(f"Saved HTML -> {html_path}")
    print(f"Saved PDF  -> {pdf_path}")


if __name__ == "__main__":
    # Load resume data
    resume_data = load_resume_data()

    print("Generating visually appealing version...")
    # Load visual components
    template_visual = load_template("resume_template.html")
    css_visual = load_css("resume_style.css")
    # Generate visual output files
    save_html_and_pdf(
        resume_data,
        template_visual,
        css_visual,
        "resume_style.css",
        "resume.html",
        "resume.pdf"
    )

    print("\nGenerating ATS-optimized version...")
    # Load ATS components
    template_ats = load_template("resume_template_ats.html")
    css_ats = load_css("resume_style_ats.css")
    # Generate ATS output files
    save_html_and_pdf(
        resume_data,
        template_ats,
        css_ats,
        "resume_style_ats.css",
        "resume_ats.html",
        "resume_ats.pdf"
    )

    print("\n✓ Both resume versions generated successfully!")
