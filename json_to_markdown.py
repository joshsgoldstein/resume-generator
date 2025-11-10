"""
json_to_markdown.py

Convert JSON resume data to YAML frontmatter markdown format.

Usage:
    pip install pyyaml

    python json_to_markdown.py

This will read resume_data.json and produce resume.md
"""

import json
import yaml
from pathlib import Path


def load_json(json_path: str = "resume_data.json") -> dict:
    """Load resume data from JSON file."""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def convert_to_markdown(data: dict) -> str:
    """Convert resume data to YAML frontmatter markdown format."""
    # Extract summary if present (will go in markdown section)
    summary = data.pop('summary', '')

    # Convert remaining data to YAML frontmatter
    yaml_content = yaml.dump(
        data,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        indent=2
    )

    # Build the markdown file
    markdown = f"---\n{yaml_content}---\n"

    # Add summary section if present
    if summary:
        markdown += f"\n## Summary\n\n{summary}\n"

    return markdown


def save_markdown(markdown: str, md_path: str = "resume.md"):
    """Save markdown content to file."""
    Path(md_path).write_text(markdown, encoding='utf-8')
    print(f"✓ Converted to Markdown -> {md_path}")


if __name__ == "__main__":
    try:
        resume_data = load_json()
        markdown_content = convert_to_markdown(resume_data)
        save_markdown(markdown_content)
    except Exception as e:
        print(f"Error: {e}")
