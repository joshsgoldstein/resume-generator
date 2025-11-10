"""
markdown_to_json.py

Convert a YAML frontmatter markdown file to JSON format.

Usage:
    pip install pyyaml

    python markdown_to_json.py

This will read resume.md and produce resume_data.json
"""

import json
import yaml
from pathlib import Path


def parse_markdown_resume(md_path: str = "resume.md") -> dict:
    """Parse a markdown file with YAML frontmatter and extract resume data."""
    content = Path(md_path).read_text(encoding='utf-8')

    # Split the frontmatter from the markdown content
    if not content.startswith('---'):
        raise ValueError("Markdown file must start with YAML frontmatter (---)")

    # Find the second --- that closes the frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        raise ValueError("Invalid frontmatter format. Expected '---' to close frontmatter.")

    # Parse the YAML frontmatter
    frontmatter = parts[1].strip()
    markdown_content = parts[2].strip()

    resume_data = yaml.safe_load(frontmatter)

    # Extract summary from markdown if present
    if markdown_content:
        # Look for a "## Summary" section
        lines = markdown_content.split('\n')
        summary_lines = []
        in_summary = False

        for line in lines:
            if line.strip().startswith('## Summary'):
                in_summary = True
                continue
            elif line.strip().startswith('##') and in_summary:
                # Hit another section, stop collecting summary
                break
            elif in_summary and line.strip():
                summary_lines.append(line.strip())

        if summary_lines:
            resume_data['summary'] = ' '.join(summary_lines)

    return resume_data


def save_json(data: dict, json_path: str = "resume_data.json"):
    """Save resume data as JSON."""
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✓ Converted to JSON -> {json_path}")


if __name__ == "__main__":
    try:
        resume_data = parse_markdown_resume()
        save_json(resume_data)
    except Exception as e:
        print(f"Error: {e}")
