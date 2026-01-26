# Resume Generator

A modern, flexible resume generator that creates beautiful HTML and PDF resumes from YAML or JSON data. Generates both a visually appealing version with modern CSS Grid layout and an ATS-optimized single-column version.

## Features

- ✨ **Pure YAML/JSON** - Edit your resume in clean, structured format
- 📄 **Dual Output** - Generates both visual and ATS-optimized versions
- 🎨 **Modern Design** - Uses CSS Grid for professional two-column layout
- 🖨️ **Perfect PDFs** - Uses Playwright (Chromium) for pixel-perfect PDF rendering
- 🔄 **Bidirectional Conversion** - Convert between YAML and JSON formats
- 🔥 **Hot Reload** - Auto-regenerates and refreshes browser on file changes
- 🌐 **GitHub Pages Ready** - Includes deployment workflow
- 🛠️ **Makefile Automation** - Simple commands for all common tasks

## Live Demo

- **Landing Page**: https://joshsgoldstein.github.io/resume-generator/
- **Visual Resume**: https://joshsgoldstein.github.io/resume-generator/resume.html
- **ATS Resume**: https://joshsgoldstein.github.io/resume-generator/resume_ats.html

## Output Formats

### Visual Version (`resume.html` / `resume.pdf`)
- Modern two-column layout with sidebar
- CSS Grid for professional design
- Perfect for networking, direct submissions, and portfolios

### ATS Version (`resume_ats.html` / `resume_ats.pdf`)
- Single-column layout optimized for Applicant Tracking Systems
- Standard section headings and simple formatting
- Parseable by automated hiring systems

### Beautiful Markdown (`resume.md`)
- Formatted markdown for GitHub/sharing
- Generated from YAML/JSON source

## Installation

### Quick Start
```bash
make install
```

This will install:
- Python packages: `jinja2`, `playwright`, `pyyaml`, `livereload`
- Playwright Chromium browser

### Manual Installation
```bash
pip install jinja2 playwright pyyaml livereload
playwright install chromium
```

## Usage

### Quick Commands

```bash
# Generate all outputs (HTML, PDF, Markdown)
make all

# Hot reload server (auto-regenerates on changes)
make watch

# Convert between formats
make yaml2json    # YAML → JSON
make json2yaml    # JSON → YAML

# Generate HTML and PDF resumes
make generate

# Generate beautiful markdown
make generate-md

# Start HTTP server to preview
make serve

# Clean generated files
make clean
```

### File Structure

```
resume-generator/
├── resume.yaml              # Source: Edit this file!
├── resume.json              # Alternative source (generated)
├── index.html               # Landing page with version buttons
├── resume_template.html     # Visual template
├── resume_template_ats.html # ATS template
├── resume_style.css         # Visual stylesheet
├── resume_style_ats.css     # ATS stylesheet
├── generate_resume.py       # HTML/PDF generator
├── generate_markdown.py     # Markdown generator
├── yaml_to_json.py          # YAML → JSON converter
├── json_to_yaml.py          # JSON → YAML converter
├── watch.py                 # Hot reload server
└── Makefile                 # Automation commands
```

### Generated Files (in .gitignore)
```
resume.html          # Visual HTML
resume.pdf           # Visual PDF
resume_ats.html      # ATS HTML
resume_ats.pdf       # ATS PDF
resume.md            # Beautiful markdown
resume.json          # JSON (if converted from YAML)
```

### Editing Your Resume

**Recommended workflow:**
```bash
# 1. Edit resume.yaml
# 2. Start hot reload server
make watch

# 3. Open browser to http://localhost:8000
# 4. Edit resume.yaml - browser auto-refreshes!
```

**Alternative: Edit JSON**
```bash
# 1. Edit resume.json
# 2. Generate resumes
make generate

# Optional: Sync back to YAML
make json2yaml
```

### Development with Hot Reload

```bash
make watch
```

This starts a server at http://localhost:8000 that:
- Watches `resume.yaml`, templates, and CSS files
- Auto-regenerates HTML when you save changes
- Auto-refreshes your browser

URLs:
- http://localhost:8000/ → Landing page
- http://localhost:8000/resume.html → Visual resume
- http://localhost:8000/resume_ats.html → ATS resume

## Resume Sections

Your resume supports the following sections:

- **Name & Tagline** - Your name and professional title
- **Summary** - Professional summary/objective
- **Contact Info** - Address, phone, email, LinkedIn, GitHub, website
- **Technical Skills** - Array of technical competencies
- **Soft Skills** - Array of core competencies
- **Experience** - Work history with role, company, dates, bullets
- **Speaking Engagements** - Conference talks and presentations
- **Education** - Degrees, schools, dates, notes

## YAML Format

```yaml
name: Your Name
tagline: Your Professional Title

summary: >
  Your professional summary goes here. Use the > character
  for multi-line text that folds into a single paragraph.

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
      - Accomplished X by doing Y, resulting in Z
      - Led team of N engineers to deliver project

speaking_engagements:
  - title: "Talk Title"
    event: Conference Name - Date

education:
  - degree: Bachelor of Science
    school: University Name
    location: City, State
    start: Aug 2015
    end: May 2019
    notes: Optional additional info
```

## Technology Stack

- **Python** - Core scripting language
- **Jinja2** - HTML templating
- **Playwright** - PDF generation (Chromium-based)
- **PyYAML** - YAML parsing
- **Livereload** - Hot reload server
- **CSS Grid** - Modern layout (visual version)
- **Make** - Build automation
- **GitHub Actions** - Automated deployment

## GitHub Pages Deployment

The repository includes a GitHub Actions workflow that automatically:
1. Generates HTML and PDF files from `resume.yaml`
2. Deploys to GitHub Pages

To enable:
1. Go to repo Settings → Pages
2. Set Source to "GitHub Actions"
3. Push to main branch

## Why Playwright?

Playwright uses Chromium (the same engine as Chrome) for PDF generation:
- ✅ Full CSS Grid and Flexbox support
- ✅ Modern CSS features work perfectly
- ✅ Pixel-perfect rendering matching browser output
- ✅ Professional-quality PDFs

## ATS Optimization

The ATS version is specifically designed to pass through Applicant Tracking Systems:
- Single-column layout (no complex multi-column designs)
- Standard section headings
- Simple, parseable formatting
- No complex CSS that could confuse parsers

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
1. Add data to `resume.yaml`
2. Update `resume_template.html` with new section
3. Update `generate_markdown.py` if needed
4. Add CSS styling in `resume_style.css`

## Tips

- Keep bullet points concise (1-2 lines each)
- Use action verbs to start bullet points
- Quantify achievements when possible
- Quote strings with colons in YAML (e.g., `"Title: Subtitle"`)
- Use `>` for multi-line summary text
- Test ATS version by copying text from PDF to verify parseability
- Use `make watch` for rapid iteration

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
