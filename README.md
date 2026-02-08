# Resume Generator

A modern, flexible resume generator that creates beautiful HTML and PDF resumes from YAML or JSON data. Generates multiple output formats: a visually appealing version with modern CSS Grid layout, an ATS-optimized single-column version, and beautifully formatted Markdown.

## Features

- ✨ **Pure YAML/JSON** - Edit your resume in clean YAML or JSON format
- 📄 **Multiple Outputs** - Generates visual PDF, ATS PDF, and beautiful Markdown
- 🎨 **Modern Design** - Uses CSS Grid for professional two-column layout
- 🖨️ **Perfect PDFs** - Uses Playwright (Chromium) for pixel-perfect PDF rendering
- 🔄 **Bidirectional Conversion** - Convert between YAML and JSON formats
- 🌐 **Landing Page** - Professional landing page with buttons for both resume versions
- 🔥 **Hot Reload** - Development server with automatic regeneration on file changes
- 🛠️ **Makefile Automation** - Simple commands for all common tasks
- 🚀 **GitHub Pages Ready** - Automatic deployment via GitHub Actions

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
- Formatted markdown output for GitHub, LinkedIn, or sharing
- Professional layout with emoji icons
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
pip install -r requirements.txt
playwright install chromium
```

## Usage

### Quick Commands

```bash
# Generate all outputs (PDFs + Markdown)
make all

# Convert YAML to JSON
make yaml2json

# Convert JSON to YAML
make json2yaml

# Generate HTML and PDF resumes
make generate

# Generate beautiful markdown
make generate-md

# Start HTTP server to preview
make serve

# Hot reload development server (auto-regenerates)
make watch

# Clean generated files
make clean
```

### File Structure

```
resume-generator/
├── resume.yaml                 # Source: Pure YAML (edit this!)
├── resume.json                 # Source: Pure JSON (alternative)
├── resume.md                   # Generated: Beautiful markdown
├── resume.html / resume.pdf    # Generated: Visual version
├── resume_ats.html / resume_ats.pdf  # Generated: ATS version
├── index.html                  # Landing page with buttons
├── resume_template.html        # Visual template
├── resume_template_ats.html    # ATS template
├── resume_style.css            # Visual stylesheet
├── resume_style_ats.css        # ATS stylesheet
├── generate_resume.py          # Main generator (HTML/PDF)
├── generate_markdown.py        # Markdown generator
├── yaml_to_json.py             # YAML → JSON converter
├── json_to_yaml.py             # JSON → YAML converter
├── watch.py                    # Hot reload dev server
├── Makefile                    # Automation commands
└── .github/workflows/deploy.yml  # GitHub Pages deployment
```

### Editing Your Resume

You can edit your resume in either format:

**Option 1: Edit YAML** (Recommended)
```bash
# 1. Edit resume.yaml
# 2. Generate all outputs
make all
```

**Option 2: Edit JSON**
```bash
# 1. Edit resume.json
# 2. Generate all outputs
make all

# Optional: Sync back to YAML
make json2yaml
```

**Option 3: Use Hot Reload** (Development)
```bash
# Watches for changes and auto-regenerates
make watch
# Opens http://localhost:8000 with live reload
```

### Workflow Examples

**After updating your resume:**
```bash
make all                    # Generate PDFs + Markdown
```

**Preview in browser:**
```bash
make serve                  # Opens http://localhost:8000
# View: http://localhost:8000/             → Landing page
#       http://localhost:8000/resume.html  → Visual version
#       http://localhost:8000/resume_ats.html → ATS version
```

**Development with hot reload:**
```bash
make watch                  # Auto-regenerates on file changes
# Edit resume.yaml and see changes instantly!
```

**Fresh start on new machine:**
```bash
make install               # Install dependencies
make all                   # Generate everything
```

**Deploy to GitHub Pages:**
```bash
# Push to main branch - GitHub Actions handles the rest!
git add resume.yaml
git commit -m "Update resume"
git push origin main
```

## Resume Sections

Your resume supports the following sections:

- **Name & Tagline** - Your name and professional title
- **Contact Info** - Address, phone, email, LinkedIn, GitHub, website
- **Summary** - Professional summary/objective (multi-line string)
- **Technical Skills** - Array of technical competencies
- **Soft Skills** - Array of core competencies
- **Experience** - Work history with role, company, dates, bullets
- **Speaking Engagements** - Conference talks and presentations
- **Publications** - Articles, newsletters, papers, books
- **Education** - Degrees, schools, dates, notes

## YAML Format

```yaml
name: Your Name
tagline: Your Professional Title

summary: >
  Your professional summary goes here. Use the > symbol for multi-line
  strings that will be folded into a single paragraph. This makes it
  easy to write long summaries without worrying about line breaks.

contact:
  address: Your Address
  phone: 555-555-5555
  email: you@example.com
  website: https://yoursite.com
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

publications:
- title: 'Your Article or Newsletter Title'
  publication: Publication Name (e.g., Medium, Substack)
  description: Brief description of the publication and its reach or impact.
  url: https://yourpublication.com

speaking_engagements:
- title: Talk Title
  event: Conference Name - Month Year

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
1. Add data to `resume.yaml` or `resume.json`
2. Update templates: `resume_template.html` and `resume_template_ats.html`
3. Update `generate_markdown.py` if the section should appear in markdown
4. Add CSS styling in `resume_style.css` and `resume_style_ats.css` if needed
5. Run `make all` to generate all outputs

## Tips

- Keep bullet points concise (1-2 lines each)
- Use action verbs to start bullet points
- Quantify achievements when possible
- Quote strings with colons in YAML (e.g., `"Title: Subtitle"`)
- Test ATS version by copying text from PDF to verify parseability
- Use `make serve` to preview before generating final PDFs

## GitHub Pages Deployment

This project includes a GitHub Actions workflow that automatically generates and deploys your resume to GitHub Pages.

### Setup

1. **Enable GitHub Pages in repo settings:**
   - Go to Settings → Pages
   - Under "Source", select **GitHub Actions**

2. **Push to main branch:**
   ```bash
   git push origin main
   ```

3. **View your live resume:**
   - Landing page: `https://yourusername.github.io/resume-generator/`
   - Visual resume: `https://yourusername.github.io/resume-generator/resume.html`
   - ATS resume: `https://yourusername.github.io/resume-generator/resume_ats.html`

The workflow automatically:
- Installs Python dependencies
- Runs Playwright to generate PDFs
- Copies CSS and HTML files
- Deploys to GitHub Pages

### Updating Your Live Resume

Simply edit `resume.yaml` and push to main:
```bash
git add resume.yaml
git commit -m "Update resume"
git push origin main
```

GitHub Actions will automatically regenerate and redeploy within 2-3 minutes.

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
