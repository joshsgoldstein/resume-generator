"""
json_to_yaml.py

Convert JSON resume data to YAML format.

Usage:
    pip install pyyaml

    python json_to_yaml.py

This will read resume.json and produce resume.yaml
"""

import json
import yaml
from pathlib import Path


def load_json(json_path: str = "resume.json") -> dict:
    """Load resume data from JSON file."""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def convert_to_yaml(data: dict) -> str:
    """Convert resume data to YAML format."""
    yaml_content = yaml.dump(
        data,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        indent=2
    )
    return yaml_content


def save_yaml(yaml_content: str, yaml_path: str = "resume.yaml"):
    """Save YAML content to file."""
    Path(yaml_path).write_text(yaml_content, encoding='utf-8')
    print(f"✓ Converted to YAML -> {yaml_path}")


if __name__ == "__main__":
    try:
        resume_data = load_json()
        yaml_content = convert_to_yaml(resume_data)
        save_yaml(yaml_content)
    except Exception as e:
        print(f"Error: {e}")
