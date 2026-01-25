"""
generate_markdown.py

Generate a beautifully formatted Markdown resume from YAML or JSON data.

Usage:
    pip install pyyaml

    python generate_markdown.py

This will read resume.yaml (or resume.json if YAML not found) and produce resume.md
"""

import json
import yaml
from pathlib import Path


def load_resume_data():
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


def generate_markdown(data: dict) -> str:
    """Generate beautifully formatted markdown from resume data."""
    md = []

    # Header
    md.append(f"# {data.get('name', 'Resume')}")
    if data.get('tagline'):
        md.append(f"**{data['tagline']}**\n")

    # Contact Info
    contact = data.get('contact', {})
    contact_parts = []
    if contact.get('email'):
        contact_parts.append(f"📧 {contact['email']}")
    if contact.get('phone'):
        contact_parts.append(f"📱 {contact['phone']}")
    if contact.get('address'):
        contact_parts.append(f"📍 {contact['address']}")

    if contact_parts:
        md.append(" | ".join(contact_parts))

    link_parts = []
    if contact.get('linkedin'):
        md_link = contact['linkedin'].replace('https://', '').replace('http://', '')
        link_parts.append(f"[LinkedIn]({contact['linkedin']})")
    if contact.get('github'):
        link_parts.append(f"[GitHub]({contact['github']})")
    if contact.get('website'):
        link_parts.append(f"[Website]({contact['website']})")

    if link_parts:
        md.append(" | ".join(link_parts))

    md.append("\n---\n")

    # Summary
    if data.get('summary'):
        md.append("## Summary\n")
        md.append(f"{data['summary']}\n")
        md.append("---\n")

    # Core Competencies (Soft Skills)
    if data.get('soft_skills'):
        md.append("## Core Competencies\n")
        for skill in data['soft_skills']:
            md.append(f"- {skill}")
        md.append("\n---\n")

    # Technical Skills
    if data.get('technical_skills'):
        md.append("## Technical Skills\n")
        for skill in data['technical_skills']:
            md.append(f"- {skill}")
        md.append("\n---\n")

    # Experience
    if data.get('experience'):
        md.append("## Experience\n")
        for job in data['experience']:
            md.append(f"### {job.get('role', 'Role')}")

            job_meta = []
            if job.get('company'):
                job_meta.append(f"**{job['company']}**")
            if job.get('location'):
                job_meta.append(job['location'])

            date_range = []
            if job.get('start'):
                date_range.append(job['start'])
            if job.get('end'):
                date_range.append(job['end'])
            if date_range:
                job_meta.append(" - ".join(date_range))

            if job_meta:
                md.append(" | ".join(job_meta) + "\n")

            if job.get('bullets'):
                for bullet in job['bullets']:
                    md.append(f"- {bullet}")

            md.append("")  # Empty line between jobs

        md.append("---\n")

    # Speaking Engagements
    if data.get('speaking_engagements'):
        md.append("## Speaking Engagements\n")
        for talk in data['speaking_engagements']:
            title = talk.get('title', 'Talk')
            event = talk.get('event', '')
            if event:
                md.append(f"- **{title}** — {event}")
            else:
                md.append(f"- **{title}**")
        md.append("\n---\n")

    # Education
    if data.get('education'):
        md.append("## Education\n")
        for edu in data['education']:
            degree = edu.get('degree', 'Degree')
            school = edu.get('school', '')
            location = edu.get('location', '')

            md.append(f"### {degree}")

            edu_meta = []
            if school:
                edu_meta.append(f"**{school}**")
            if location:
                edu_meta.append(location)

            date_range = []
            if edu.get('start'):
                date_range.append(edu['start'])
            if edu.get('end'):
                date_range.append(edu['end'])
            if date_range:
                edu_meta.append(" - ".join(date_range))

            if edu_meta:
                md.append(" | ".join(edu_meta) + "\n")

            if edu.get('notes'):
                md.append(f"_{edu['notes']}_\n")

    return "\n".join(md)


def save_markdown(content: str, output_path: str = "resume.md"):
    """Save markdown content to file."""
    Path(output_path).write_text(content, encoding='utf-8')
    print(f"✓ Generated beautiful markdown -> {output_path}")


if __name__ == "__main__":
    try:
        data = load_resume_data()
        markdown = generate_markdown(data)
        save_markdown(markdown)
    except Exception as e:
        print(f"Error: {e}")
