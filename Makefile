.PHONY: help all install playwright-install yaml2json json2yaml generate generate-md clean serve watch

# Default target
help:
	@echo "Resume Generator - Available Commands:"
	@echo ""
	@echo "  make install      - Sync Python environment with uv"
	@echo "  make playwright-install - Install Playwright Chromium browser"
	@echo "  make all          - Generate all outputs (PDFs + Markdown)"
	@echo "  make yaml2json    - Convert resume.yaml → resume.json"
	@echo "  make json2yaml    - Convert resume.json → resume.yaml"
	@echo "  make generate     - Generate HTML and PDF resumes (both versions)"
	@echo "  make generate-md  - Generate beautiful markdown resume (resume.md)"
	@echo "  make serve        - Start HTTP server to view HTML resumes"
	@echo "  make watch        - Hot reload server (auto-regenerates on changes)"
	@echo "  make clean        - Remove all generated files"
	@echo ""

# Install dependencies
install:
	@echo "Syncing Python dependencies with uv..."
	uv sync
	@echo "Installing Playwright browsers..."
	$(MAKE) playwright-install
	@echo "✓ Installation complete!"

# Install Playwright browser binaries
playwright-install:
	uv run playwright install chromium

# Convert YAML to JSON
yaml2json:
	@echo "Converting resume.yaml → resume.json..."
	uv run python yaml_to_json.py

# Convert JSON to YAML
json2yaml:
	@echo "Converting resume.json → resume.yaml..."
	uv run python json_to_yaml.py

# Generate all resume versions (HTML + PDF)
generate: playwright-install
	@echo "Generating resumes..."
	uv run python generate_resume.py

# Generate beautiful markdown resume
generate-md:
	@echo "Generating beautiful markdown..."
	uv run python generate_markdown.py

# Full workflow: generate all outputs
all: generate generate-md
	@echo ""
	@echo "✓ Complete! Generated files:"
	@echo "  - resume.html / resume.pdf (visual version)"
	@echo "  - resume_ats.html / resume_ats.pdf (ATS version)"
	@echo "  - resume.md (formatted markdown)"

# Start HTTP server to view resumes
serve: generate generate-md
	@echo "Starting HTTP server on http://localhost:8000"
	@echo "  http://localhost:8000/            → Landing page"
	@echo "  http://localhost:8000/resume.html → Visual resume"
	@echo "  http://localhost:8000/resume_ats.html → ATS resume"
	@echo ""
	@echo "Press Ctrl+C to stop the server"
	uv run python -m http.server 8000

# Hot reload server - auto-regenerates on file changes
watch:
	@echo "Starting hot reload server..."
	uv run python watch.py

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -f resume.html resume.pdf resume_ats.html resume_ats.pdf resume.md
	@echo "✓ Cleaned!"
