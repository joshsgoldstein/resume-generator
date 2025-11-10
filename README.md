# Resume Generator

A modern, flexible resume generator that creates beautiful HTML and PDF resumes from YAML frontmatter Markdown or JSON data. Generates both a visually appealing version with modern CSS Grid layout and an ATS-optimized single-column version.

## Features

- ✨ **YAML Frontmatter Markdown** - Edit your resume in human-friendly Markdown format
- 📄 **Dual Output** - Generates both visual and ATS-optimized versions
- 🎨 **Modern Design** - Uses CSS Grid for professional two-column layout
- 🖨️ **Perfect PDFs** - Uses Playwright (Chromium) for pixel-perfect PDF rendering
- 🔄 **Bidirectional Conversion** - Convert between Markdown and JSON formats
- 🛠️ **Makefile Automation** - Simple commands for all common tasks

## Output Formats

### Visual Version (`resume.html` / `resume.pdf`)
- Modern two-column layout with sidebar
- CSS Grid for professional design
- Perfect for networking, direct submissions, and portfolios

### ATS Version (`resume_ats.html` / `resume_ats.pdf`)
- Single-column layout optimized for Applicant Tracking Systems
- Standard section headings and simple formatting
- Parseable by automated hiring systems

## Installation

### Quick Start
```bash
make install
```

This will install:
- Python packages: `jinja2`, `playwright`, `pyyaml`
- Playwright Chromium browser

### Manual Installation
```bash
pip install jinja2 playwright pyyaml
playwright install chromium
```

## Usage

### Quick Commands

```bash
# Generate both resume versions (from resume.md)
make all

# Convert Markdown to JSON
make md2json

# Convert JSON to Markdown
make json2md

# Generate HTML and PDF resumes
make generate

# Start HTTP server to preview
make serve

# Clean generated files
make clean
```

### File Structure

```
resume/
├── resume.md                    # Source: YAML frontmatter Markdown
├── resume_data.json            # Source: JSON format
├── resume_template.html        # Visual template
├── resume_template_ats.html    # ATS template
├── resume_style.css            # Visual stylesheet
├── resume_style_ats.css        # ATS stylesheet
├── generate_resume.py          # Main generator script
├── markdown_to_json.py         # MD → JSON converter
├── json_to_markdown.py         # JSON → MD converter
└── Makefile                    # Automation commands
```

### Editing Your Resume

You can edit your resume in either format:

**Option 1: Edit Markdown** (Recommended)
```bash
# 1. Edit resume.md
# 2. Generate resumes
make all
```

**Option 2: Edit JSON**
```bash
# 1. Edit resume_data.json
# 2. Generate resumes
make generate

# Optional: Sync back to Markdown
make json2md
```

### Workflow Examples

**After updating your resume:**
```bash
make all                    # Convert MD → JSON → Generate PDFs
```

**Preview in browser:**
```bash
make serve                  # Opens http://localhost:8000
# View: http://localhost:8000/resume.html
#       http://localhost:8000/resume_ats.html
```

**Fresh start on new machine:**
```bash
make install               # Install dependencies
make all                   # Generate everything
```

## Resume Sections

Your resume supports the following sections:

- **Name & Tagline** - Your name and professional title
- **Contact Info** - Address, phone, email, LinkedIn, GitHub, website
- **Summary** - Professional summary/objective
- **Technical Skills** - Comma-separated technical competencies
- **Soft Skills** - Comma-separated core competencies
- **Experience** - Work history with role, company, dates, bullets
- **Speaking Engagements** - Conference talks and presentations
- **Education** - Degrees, schools, dates, notes

## YAML Frontmatter Format

```markdown
---
name: Your Name
tagline: Your Professional Title

contact:
  address: Your Address
  phone: 555-555-5555
  email: you@example.com
  linkedin: https://linkedin.com/in/yourprofile
  github: https://github.com/yourusername

technical_skills:
  - Skill 1
  - Skill 2
  - Skill 3

soft_skills:
  - Leadership
  - Communication
  - Problem Solving

experience:
  - role: Senior Engineer
    company: Company Name
    location: City, State
    start: Jan 2020
    end: Present
    bullets:
      - Bullet point 1
      - Bullet point 2

education:
  - degree: Bachelor of Science
    school: University Name
    location: City, State
    start: Aug 2015
    end: May 2019
    notes: Optional additional info
---

## Summary

Your professional summary goes here.
```

## Technology Stack

- **Python** - Core scripting language
- **Jinja2** - HTML templating
- **Playwright** - PDF generation (Chromium-based)
- **PyYAML** - YAML parsing
- **CSS Grid** - Modern layout (visual version)
- **Make** - Build automation

## Why Playwright?

Playwright uses Chromium (the same engine as Chrome) for PDF generation, which means:
- ✅ Full CSS Grid and Flexbox support
- ✅ Modern CSS features work perfectly
- ✅ Pixel-perfect rendering matching browser output
- ✅ Professional-quality PDFs

Previous versions used WeasyPrint, which had limited CSS support and caused layout issues.

## ATS Optimization

The ATS version is specifically designed to pass through Applicant Tracking Systems:
- Single-column layout (no complex multi-column designs)
- Standard section headings
- Simple, parseable formatting
- No complex CSS that could confuse parsers
- Skills in comma-separated format

## Customization

### Adjust Spacing
Edit `resume_style.css`:
```css
@page {
    margin: 12mm;  /* Adjust page margins */
}

body {
    font-size: 10pt;      /* Adjust base font size */
    line-height: 1.3;     /* Adjust line spacing */
}
```

### Change Layout
Edit `resume_template.html` to:
- Reorder sections
- Change column widths (currently 68% / 32%)
- Modify section styling

### Add New Sections
1. Add data to `resume.md` or `resume_data.json`
2. Update `resume_template.html` with new section
3. Add CSS styling in `resume_style.css`

## Tips

- Keep bullet points concise (1-2 lines each)
- Use action verbs to start bullet points
- Quantify achievements when possible
- Quote strings with colons in YAML (e.g., `"Title: Subtitle"`)
- Test ATS version by copying text from PDF to verify parseability
- Use `make serve` to preview before generating final PDFs

## Troubleshooting

**YAML parsing errors:**
- Check indentation (use spaces, not tabs)
- Quote strings containing colons or special characters
- Ensure proper list formatting with `-` prefix

**PDF doesn't match HTML:**
- Ensure Playwright is installed: `playwright install chromium`
- Check that CSS file paths are correct
- Regenerate with `make generate`

**Content too long:**
- Reduce margins in CSS (12mm → 10mm)
- Decrease font size (10pt → 9pt)
- Tighten line height (1.3 → 1.2)
- Remove older/less relevant experience

## License

MIT License - Feel free to use and modify for your own resume!

## Contributing

This is a personal resume generator, but feel free to fork and adapt for your needs!
