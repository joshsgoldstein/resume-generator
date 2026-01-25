"""
yaml_to_json.py

Convert a YAML resume file to JSON format.

Usage:
    pip install pyyaml

    python yaml_to_json.py

This will read resume.yaml and produce resume.json
"""

import json
import yaml
from pathlib import Path


def parse_yaml_resume(yaml_path: str = "resume.yaml") -> dict:
    """Parse a YAML resume file."""
    content = Path(yaml_path).read_text(encoding='utf-8')
    resume_data = yaml.safe_load(content)
    return resume_data


def save_json(data: dict, json_path: str = "resume.json"):
    """Save resume data as JSON."""
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✓ Converted to JSON -> {json_path}")


if __name__ == "__main__":
    try:
        resume_data = parse_yaml_resume()
        save_json(resume_data)
    except Exception as e:
        print(f"Error: {e}")
