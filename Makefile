.PHONY: help all install yaml2json json2yaml generate generate-md clean serve

# Default target
help:
	@echo "Resume Generator - Available Commands:"
	@echo ""
	@echo "  make install      - Install required Python packages"
	@echo "  make all          - Generate all outputs (PDFs + Markdown)"
	@echo "  make yaml2json    - Convert resume.yaml → resume.json"
	@echo "  make json2yaml    - Convert resume.json → resume.yaml"
	@echo "  make generate     - Generate HTML and PDF resumes (both versions)"
	@echo "  make generate-md  - Generate beautiful markdown resume (resume.md)"
	@echo "  make serve        - Start HTTP server to view HTML resumes"
	@echo "  make clean        - Remove all generated files"
	@echo ""

# Install dependencies
install:
	@echo "Installing Python dependencies..."
	pip install jinja2 playwright pyyaml
	@echo "Installing Playwright browsers..."
	playwright install chromium
	@echo "✓ Installation complete!"

# Convert YAML to JSON
yaml2json:
	@echo "Converting resume.yaml → resume.json..."
	python yaml_to_json.py

# Convert JSON to YAML
json2yaml:
	@echo "Converting resume.json → resume.yaml..."
	python json_to_yaml.py

# Generate all resume versions (HTML + PDF)
generate:
	@echo "Generating resumes..."
	python generate_resume.py

# Generate beautiful markdown resume
generate-md:
	@echo "Generating beautiful markdown..."
	python generate_markdown.py

# Full workflow: generate all outputs
all: generate generate-md
	@echo ""
	@echo "✓ Complete! Generated files:"
	@echo "  - resume.html / resume.pdf (visual version)"
	@echo "  - resume_ats.html / resume_ats.pdf (ATS version)"
	@echo "  - resume.md (formatted markdown)"

# Start HTTP server to view resumes
serve:
	@echo "Starting HTTP server on http://localhost:8000"
	@echo "View your resumes at:"
	@echo "  - http://localhost:8000/resume.html"
	@echo "  - http://localhost:8000/resume_ats.html"
	@echo ""
	@echo "Press Ctrl+C to stop the server"
	python -m http.server 8000

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -f resume.html resume.pdf resume_ats.html resume_ats.pdf resume.md
	@echo "✓ Cleaned!"
