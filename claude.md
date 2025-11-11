# Resume Generator - Claude Context

This document provides context for Claude (or any AI assistant) when working with this resume generator project.

## Project Overview

A modern resume generator that creates professional HTML and PDF resumes from YAML frontmatter Markdown or JSON data. Generates two versions:
- **Visual version** - Modern CSS Grid two-column layout with sidebar
- **ATS version** - Single-column layout optimized for Applicant Tracking Systems

## Tech Stack

- **Python 3** - Core scripting
- **Jinja2** - HTML templating
- **Playwright** - PDF generation (Chromium-based for perfect CSS rendering)
- **PyYAML** - YAML parsing for markdown frontmatter
- **Make** - Build automation

## Key Files

### Source Files
- `resume.md` - Primary source (YAML frontmatter + Markdown)
- `resume_data.json` - Alternative source (JSON format)
- Bidirectional conversion supported between MD ↔ JSON

### Templates
- `resume_template.html` - Visual version template (CSS Grid layout)
- `resume_template_ats.html` - ATS version template (single column)

### Stylesheets
- `resume_style.css` - Visual version styling (modern CSS Grid)
- `resume_style_ats.css` - ATS version styling (simple, parseable)

### Scripts
- `generate_resume.py` - Main generator (uses Playwright for PDF)
- `markdown_to_json.py` - Convert resume.md → resume_data.json
- `json_to_markdown.py` - Convert resume_data.json → resume.md
- `Makefile` - Common commands and workflows

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

### Resume Sections (in order)
1. **name** - Full name
2. **tagline** - Professional title/headline
3. **contact** - address, phone, email, linkedin, github, website
4. **summary** - Professional summary paragraph
5. **technical_skills** - Array of technical competencies
6. **soft_skills** - Array of soft skills/core competencies
7. **experience** - Array of jobs (role, company, location, start, end, bullets[])
8. **speaking_engagements** - Array of talks (title, event)
9. **education** - Array of degrees (degree, school, location, start, end, notes)

### YAML Formatting Rules
- Strings with colons must be quoted: `"Title: Subtitle"`
- Use 2-space indentation (not tabs)
- Lists use `-` prefix
- Nested objects use proper indentation

## Common Tasks

### User wants to edit resume
```bash
# Edit resume.md, then:
make all
```

### User wants to preview
```bash
make serve
# Opens http://localhost:8000
```

### User wants to compress resume
1. Reduce margins (currently 10mm for visual, 0.5in for ATS)
2. Decrease font size (currently 9pt base)
3. Tighten line height (currently 1.2)
4. Remove older/less relevant content
5. Reduce bullet points for older roles

### User wants to add new section
1. Add data to `resume.md` or `resume_data.json`
2. Update relevant template (`resume_template.html` or `resume_template_ats.html`)
3. Add CSS styling if needed
4. Run `make generate`

### YAML parsing errors
- Check indentation (spaces not tabs)
- Quote strings with special characters
- Verify list formatting with `-`

## Important Notes

### Don't Edit These Files Directly
- `resume.html`, `resume.pdf` - Generated output
- `resume_ats.html`, `resume_ats.pdf` - Generated output

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
make all           # MD → JSON → Generate both PDFs
make md2json       # Convert Markdown to JSON
make json2md       # Convert JSON to Markdown
make generate      # Generate HTML/PDF from current JSON
make serve         # Preview in browser
make clean         # Remove generated files
```

## Dependencies Installation

```bash
pip install jinja2 playwright pyyaml
playwright install chromium
```

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
1. User edits `resume.md` primarily (YAML frontmatter format)
2. Current goal is 2-page visual resume
3. ATS version can be 2-3 pages
4. User values modern, professional design
5. Recent experience (Weaviate, Seldon, Keeeb) gets priority
6. Technical skills include AI/MLOps focus
7. Don't make files unless explicitly requested
8. Always run `make generate` after template/CSS changes
9. Test both visual and ATS versions
10. Keep formatting ATS-friendly for the ATS version

## Key Principles

- **Content over style** - ATS version prioritizes parseability
- **Modern CSS** - Visual version uses latest features (Grid, Flexbox)
- **Separation of concerns** - Data (MD/JSON), Templates (HTML), Styling (CSS)
- **Automation** - Makefile for common tasks
- **Flexibility** - Support both YAML and JSON editing
- **Professional output** - Both versions should look polished
