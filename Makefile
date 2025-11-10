.PHONY: help all install md2json json2md generate clean serve

# Default target
help:
	@echo "Resume Generator - Available Commands:"
	@echo ""
	@echo "  make install      - Install required Python packages"
	@echo "  make all          - Convert markdown to JSON and generate all resumes"
	@echo "  make md2json      - Convert resume.md to resume_data.json"
	@echo "  make json2md      - Convert resume_data.json to resume.md"
	@echo "  make generate     - Generate HTML and PDF resumes (both versions)"
	@echo "  make serve        - Start HTTP server to view HTML resumes"
	@echo "  make clean        - Remove generated HTML and PDF files"
	@echo ""

# Install dependencies
install:
	@echo "Installing Python dependencies..."
	pip install jinja2 playwright pyyaml
	@echo "Installing Playwright browsers..."
	playwright install chromium
	@echo "✓ Installation complete!"

# Convert markdown to JSON
md2json:
	@echo "Converting resume.md → resume_data.json..."
	python markdown_to_json.py

# Convert JSON to markdown
json2md:
	@echo "Converting resume_data.json → resume.md..."
	python json_to_markdown.py

# Generate all resume versions
generate:
	@echo "Generating resumes..."
	python generate_resume.py

# Full workflow: markdown → JSON → resumes
all: md2json generate
	@echo ""
	@echo "✓ Complete! Generated files:"
	@echo "  - resume.html / resume.pdf (visual version)"
	@echo "  - resume_ats.html / resume_ats.pdf (ATS version)"

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
	rm -f resume.html resume.pdf resume_ats.html resume_ats.pdf
	@echo "✓ Cleaned!"
