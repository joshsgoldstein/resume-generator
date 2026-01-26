# Resume Generator - Claude Context

This document provides context for Claude (or any AI assistant) when working with this resume generator project.

## Project Overview

A modern resume generator that creates professional resumes from YAML or JSON data. Generates multiple output formats:
- **Visual PDF** - Modern CSS Grid two-column layout with sidebar (resume.pdf)
- **ATS PDF** - Single-column layout optimized for Applicant Tracking Systems (resume_ats.pdf)
- **Beautiful Markdown** - Formatted markdown for GitHub/sharing (resume.md)

## Tech Stack

- **Python 3** - Core scripting
- **Jinja2** - HTML templating
- **Playwright** - PDF generation (Chromium-based for perfect CSS rendering)
- **PyYAML** - YAML parsing
- **Livereload** - Hot reload development server
- **Make** - Build automation
- **GitHub Actions** - Automated deployment to GitHub Pages

## Key Files

### Source Files (Edit These)
- `resume.yaml` - Primary source (pure YAML format)
- `resume.json` - Alternative source (pure JSON format)
- Bidirectional conversion supported between YAML ↔ JSON

### Generated Files (Do Not Edit)
- `resume.md` - Beautiful formatted markdown (generated)
- `resume.html` / `resume.pdf` - Visual version (generated)
- `resume_ats.html` / `resume_ats.pdf` - ATS version (generated)

### Templates
- `resume_template.html` - Visual version template (CSS Grid layout)
- `resume_template_ats.html` - ATS version template (single column)

### Stylesheets
- `resume_style.css` - Visual version styling (modern CSS Grid)
- `resume_style_ats.css` - ATS version styling (simple, parseable)

### Scripts
- `generate_resume.py` - Generate HTML and PDF resumes (uses Playwright)
- `generate_markdown.py` - Generate beautiful formatted markdown
- `yaml_to_json.py` - Convert resume.yaml → resume.json
- `json_to_yaml.py` - Convert resume.json → resume.yaml
- `watch.py` - Hot reload development server
- `Makefile` - Common commands and workflows

### Web Files
- `index.html` - Landing page with buttons for visual/ATS versions + PDF downloads
- `.github/workflows/deploy.yml` - GitHub Actions workflow for Pages deployment

## Current Configuration

### Visual Resume (resume.pdf)
- **Target:** 2 pages
- **Layout:** Two-column with 68% main / 32% sidebar
- **Margins:** 10mm
- **Font:** 9pt base, line-height 1.2
- **Sidebar order:** Core Competencies, Technical Skills, Speaking, Education
- **Main content:** Summary, Work History

### ATS Resume (resume_ats.pdf)
- **Target:** 2-3 pages acceptable
- **Layout:** Single column
- **Margins:** 0.5in
- **Font:** 9pt base, line-height 1.2
- **Section order:** Summary, Core Competencies, Technical Skills, Experience, Speaking, Technical Skills, Education

## Design Decisions

### Why Playwright Instead of WeasyPrint?
- WeasyPrint has limited CSS support (no Grid, poor Flexbox)
- Playwright uses Chromium engine = perfect CSS rendering
- PDF output matches browser HTML exactly
- Supports all modern CSS features

### Why Two Versions?
- **Visual** - For human readers, networking, direct submissions
- **ATS** - For automated systems that parse text (single column, simple formatting)

### Current Spacing Strategy
The visual resume has been aggressively compressed to fit 2 pages:
- Minimal margins (10mm)
- Tight line spacing (1.2)
- Reduced font sizes throughout
- Small spacing between sections and items
- Sidebar uses smaller fonts (8.5pt)

## Data Structure

### Resume Sections (in YAML/JSON)
1. **name** - Full name
2. **tagline** - Professional title/headline
3. **summary** - Professional summary paragraph (use `>` for multi-line in YAML)
4. **contact** - address, phone, email, linkedin, github, website
5. **technical_skills** - Array of technical competencies
6. **soft_skills** - Array of soft skills/core competencies
7. **experience** - Array of jobs (role, company, location, start, end, bullets[])
8. **speaking_engagements** - Array of talks (title, event)
9. **education** - Array of degrees (degree, school, location, start, end, notes)

### YAML Formatting Rules
- Multi-line strings use `>` (folds newlines) or `|` (preserves newlines)
- Strings with colons must be quoted: `"Title: Subtitle"`
- Use 2-space indentation (not tabs)
- Lists use `-` prefix
- Nested objects use proper indentation

## Common Tasks

### User wants to edit resume
```bash
# Edit resume.yaml (or resume.json), then:
make all
# This generates PDFs and beautiful markdown
```

### User wants to preview with hot reload
```bash
make watch
# Opens http://localhost:8000 with auto-refresh on file changes
# Edit resume.yaml and browser auto-updates!
```

### User wants simple preview (no hot reload)
```bash
make serve
# Opens http://localhost:8000 to view HTML versions
```

### User wants to convert between formats
```bash
make yaml2json   # Convert resume.yaml → resume.json
make json2yaml   # Convert resume.json → resume.yaml
```

### User wants to compress resume
1. Reduce margins (currently 10mm for visual, 0.5in for ATS)
2. Decrease font size (currently 9pt base)
3. Tighten line height (currently 1.2)
4. Remove older/less relevant content
5. Reduce bullet points for older roles

### User wants to add new section
1. Add data to `resume.yaml` or `resume.json`
2. Update relevant template (`resume_template.html` or `resume_template_ats.html`)
3. Update `generate_markdown.py` if the section should appear in markdown output
4. Add CSS styling if needed
5. Run `make all`

### YAML parsing errors
- Check indentation (spaces not tabs)
- Quote strings with special characters
- Verify list formatting with `-`

## Important Notes

### Don't Edit These Files Directly (Generated Outputs)
- `resume.md` - Generated beautiful markdown
- `resume.html`, `resume.pdf` - Generated visual version
- `resume_ats.html`, `resume_ats.pdf` - Generated ATS version

### Content Removed from Current Resume
- SharePoint Consultant role (2012-2014) - Removed to fit 2-page target

### When Helping with Content
- Keep bullet points concise (1-2 lines max)
- Use action verbs
- Quantify achievements when possible
- Recent roles (last 3-5 years) get more detail
- Older roles can be condensed

### When Modifying CSS
- Visual version: Balance readability with space constraints
- ATS version: Keep simple, parseable formatting
- Test with `make generate` after changes
- Check PDF output, not just HTML

## Workflow Commands

```bash
make help          # Show all commands
make install       # Install dependencies
make all           # Generate all outputs (PDFs + Markdown)
make watch         # Hot reload server (auto-regenerates on changes)
make yaml2json     # Convert resume.yaml → resume.json
make json2yaml     # Convert resume.json → resume.yaml
make generate      # Generate HTML/PDF from YAML/JSON
make generate-md   # Generate beautiful markdown
make serve         # Preview in browser (no hot reload)
make clean         # Remove all generated files
```

## Dependencies Installation

```bash
pip install jinja2 playwright pyyaml livereload
playwright install chromium
```

## GitHub Pages Deployment

The repo includes `.github/workflows/deploy.yml` which:
1. Triggers on push to main
2. Installs Python + Playwright
3. Runs `generate_resume.py` to create HTML/PDF
4. Deploys to GitHub Pages

Live URLs:
- Landing page: https://joshsgoldstein.github.io/resume-generator/
- Visual resume: https://joshsgoldstein.github.io/resume-generator/resume.html
- ATS resume: https://joshsgoldstein.github.io/resume-generator/resume_ats.html

## Troubleshooting

### PDF doesn't match HTML
- Ensure Playwright Chromium is installed
- Check CSS file paths are correct
- Regenerate with `make generate`

### Content overflows pages
- Reduce margins in CSS
- Decrease font sizes
- Tighten line height
- Remove or condense older content
- Reduce bullet points

### YAML parsing errors
- Check for proper indentation
- Quote strings with colons/special chars
- Verify list syntax with `-`

## Future Improvements to Consider

- Add support for projects section
- Add certifications section
- Make sidebar width configurable
- Add color themes
- Create multi-page handling for very long resumes
- Add support for custom fonts

## Context for AI Assistants

When helping with this project:
1. User edits `resume.yaml` primarily (pure YAML format)
2. `resume.md` is a GENERATED file - beautiful markdown output
3. Current goal is 2-page visual resume
4. ATS version can be 2-3 pages
5. User values modern, professional design
6. Recent experience (Weaviate, Seldon, Keeeb) gets priority
7. Technical skills include AI/MLOps focus
8. Don't make files unless explicitly requested
9. Always run `make all` after changes to generate all outputs
10. Test both visual and ATS PDF versions
11. Keep formatting ATS-friendly for the ATS version

## Key Principles

- **Content over style** - ATS version prioritizes parseability
- **Modern CSS** - Visual version uses latest features (Grid, Flexbox)
- **Separation of concerns** - Data (MD/JSON), Templates (HTML), Styling (CSS)
- **Automation** - Makefile for common tasks
- **Flexibility** - Support both YAML and JSON editing
- **Professional output** - Both versions should look polished
