# 📄 Resume Generator

> A modern, production-ready resume generator that transforms YAML/JSON data into beautiful HTML, PDF, and Markdown formats. Built with Python, Jinja2, and Playwright, featuring automated GitHub Pages deployment and hot-reload development.

[![Live Demo](https://img.shields.io/badge/Live-Demo-blue?style=for-the-badge)](https://joshsgoldstein.github.io/resume-generator/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 🎯 Overview

This project demonstrates modern DevOps practices and full-stack development skills by implementing a sophisticated document generation pipeline. It showcases infrastructure-as-code principles, automated CI/CD workflows, and clean architecture patterns.

**Key Technical Achievements:**
- 🏗️ Clean separation of data (YAML/JSON), templates (Jinja2), and styling (CSS)
- 🚀 Automated deployment pipeline with GitHub Actions
- 🔥 Hot-reload development environment with livereload
- 📱 Responsive design with CSS Grid and Flexbox
- 🎨 Professional PDF generation using Playwright's Chromium engine
- 🔄 Bidirectional data transformation (YAML ↔ JSON)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Multiple Output Formats** | Generate Visual PDF, ATS-optimized PDF, and GitHub-ready Markdown from a single source |
| **Modern Tech Stack** | Python 3.11+, Jinja2 templating, Playwright PDF rendering, PyYAML parsing |
| **Developer Experience** | Hot-reload dev server, Makefile automation, clear project structure |
| **Production Ready** | GitHub Actions CI/CD, automated deployments, professional landing page |
| **ATS Optimized** | Dedicated single-column layout for Applicant Tracking Systems |
| **Flexible Data Sources** | Edit in YAML or JSON, with automatic bidirectional conversion |

---

## 🚀 Live Demo

**[View Live Site →](https://joshsgoldstein.github.io/resume-generator/)**

The live demo includes:
- Professional landing page with resume version selector
- Visual resume with modern CSS Grid two-column layout
- ATS-optimized single-column version
- Automatic regeneration on every push to main

---

## 📸 Screenshots

### Landing Page
Clean, professional landing page with version selection:
- Gradient background design
- Clear call-to-action buttons
- Responsive mobile layout

### Visual Resume
Modern two-column layout featuring:
- CSS Grid-based responsive design
- Sidebar with skills and education
- Professional typography and spacing
- Chromium-rendered PDF for perfect fidelity

### ATS Resume
Single-column layout optimized for parsing:
- Standard section headings
- Linear content flow
- No complex CSS that could break parsers
- Plain-text friendly structure

---

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.11+** - Core scripting and data processing
- **Jinja2** - Powerful HTML templating engine
- **Playwright** - Chromium-based PDF generation with full CSS support
- **PyYAML** - YAML parsing and serialization
- **livereload** - Development server with hot reload

### DevOps & Infrastructure
- **GitHub Actions** - Automated CI/CD pipeline
- **GitHub Pages** - Static site hosting
- **Make** - Build automation and task orchestration

### Design & Styling
- **CSS Grid** - Modern two-column layout system
- **CSS Flexbox** - Responsive component layouts
- **Custom CSS** - Professional styling with print optimization

---

## 📦 Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git

### Quick Start

```bash
# Clone the repository
git clone https://github.com/joshsgoldstein/resume-generator.git
cd resume-generator

# Install dependencies
make install

# Generate all outputs
make all

# Start development server with hot reload
make watch
```

### Manual Installation

```bash
# Install Python packages
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

---

## 💻 Usage

### Quick Commands

| Command | Description |
|---------|-------------|
| `make install` | Install all dependencies and Playwright browsers |
| `make all` | Generate HTML, PDF, and Markdown outputs |
| `make generate` | Generate HTML and PDF resumes only |
| `make generate-md` | Generate beautiful Markdown resume |
| `make watch` | Start hot-reload dev server (recommended for development) |
| `make serve` | Start basic HTTP server for preview |
| `make yaml2json` | Convert resume.yaml → resume.json |
| `make json2yaml` | Convert resume.json → resume.yaml |
| `make clean` | Remove all generated files |

### Development Workflow

**Option 1: Hot Reload (Recommended)**
```bash
# Start development server
make watch

# Edit resume.yaml
# Browser automatically refreshes on save
# View at http://localhost:8000
```

**Option 2: Manual Generation**
```bash
# Edit resume.yaml
vim resume.yaml

# Generate all outputs
make all

# Preview in browser
make serve
```

### Editing Your Resume

Your resume data lives in `resume.yaml` (or `resume.json`):

```yaml
name: Your Name
tagline: Your Professional Title

summary: >
  Multi-line professional summary using YAML's fold operator.
  This gets rendered as a single paragraph in all output formats.

contact:
  email: you@example.com
  phone: 555-555-5555
  linkedin: https://linkedin.com/in/yourprofile
  github: https://github.com/yourusername

technical_skills:
- Skill 1
- Skill 2

experience:
  - role: Senior Engineer
    company: Company Name
    start: Jan 2020
    end: Present
    bullets:
    - Achievement with quantifiable impact
    - Technical leadership example
```

---

## 📁 Project Structure

```
resume-generator/
├── 📝 Source Files (Edit These)
│   ├── resume.yaml              # Resume data (YAML format)
│   ├── resume.json              # Resume data (JSON format - alternative)
│   ├── resume_template.html     # Visual resume template
│   ├── resume_template_ats.html # ATS resume template
│   ├── resume_style.css         # Visual resume styling
│   └── resume_style_ats.css     # ATS resume styling
│
├── 🤖 Generation Scripts
│   ├── generate_resume.py       # Main generator (HTML + PDF)
│   ├── generate_markdown.py     # Markdown generator
│   ├── yaml_to_json.py          # YAML → JSON converter
│   ├── json_to_yaml.py          # JSON → YAML converter
│   └── watch.py                 # Hot reload development server
│
├── 🚀 Generated Files (Git Ignored)
│   ├── resume.html              # Visual HTML output
│   ├── resume.pdf               # Visual PDF output
│   ├── resume_ats.html          # ATS HTML output
│   ├── resume_ats.pdf           # ATS PDF output
│   └── resume.md                # Markdown output
│
├── 🌐 Deployment
│   ├── index.html               # Landing page
│   └── .github/workflows/
│       └── deploy.yml           # GitHub Actions workflow
│
└── 📋 Configuration
    ├── Makefile                 # Build automation
    ├── requirements.txt         # Python dependencies
    └── .gitignore               # Git ignore rules
```

---

## 🎨 Customization

### Styling

**Adjust spacing and typography:**
```css
/* resume_style.css */
@page {
    margin: 10mm;  /* Page margins */
}

body {
    font-size: 9pt;      /* Base font size */
    line-height: 1.2;    /* Line height for compact layout */
}
```

**Change color scheme:**
```css
/* Visual resume colors */
.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

/* Landing page gradient */
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Layout

**Modify sidebar width:**
```css
/* resume_style.css */
.layout {
    grid-template-columns: 68% 32%;  /* Main / Sidebar ratio */
}
```

**Reorder sections:**
Edit `resume_template.html` to change section order in the sidebar or main content area.

### Adding New Sections

1. **Add data to `resume.yaml`:**
```yaml
certifications:
- name: AWS Solutions Architect
  year: 2024
```

2. **Update template (`resume_template.html`):**
```html
{% if certifications %}
<section class="sidebar-section">
    <h2 class="section-title">Certifications</h2>
    {% for cert in certifications %}
    <div>{{ cert.name }} ({{ cert.year }})</div>
    {% endfor %}
</section>
{% endif %}
```

3. **Add CSS styling if needed**
4. **Update `generate_markdown.py` for markdown output**
5. **Run `make all` to generate**

---

## 📝 Supported Resume Sections

| Section | Description | Format |
|---------|-------------|--------|
| **Name & Tagline** | Professional identity | String values |
| **Contact Info** | Address, phone, email, social links | Nested object |
| **Summary** | Professional objective | Multi-line string (`>` operator) |
| **Technical Skills** | Technical competencies | Array of strings |
| **Soft Skills** | Core competencies | Array of strings |
| **Publications** | Articles, newsletters, books | Array of objects |
| **Speaking Engagements** | Conference talks | Array of objects |
| **Experience** | Work history | Array of job objects with bullets |
| **Education** | Academic background | Array of degree objects |

---

## 🚀 GitHub Pages Deployment

### Setup (One Time)

1. **Enable GitHub Pages:**
   ```
   Repository Settings → Pages → Source: GitHub Actions
   ```

2. **Push to main branch:**
   ```bash
   git push origin main
   ```

3. **Access your live site:**
   ```
   https://yourusername.github.io/resume-generator/
   ```

### Automated Deployment Pipeline

The included GitHub Actions workflow automatically:
1. ✅ Installs Python dependencies
2. ✅ Installs Playwright Chromium browser
3. ✅ Generates HTML and PDF files
4. ✅ Copies assets (CSS, landing page)
5. ✅ Deploys to GitHub Pages

**Deployment triggers:**
- Every push to `main` branch
- Manual trigger via Actions tab

**Deployment time:** ~2-3 minutes

### Updating Your Live Resume

```bash
# Edit your resume
vim resume.yaml

# Commit and push
git add resume.yaml
git commit -m "Update resume content"
git push origin main

# GitHub Actions automatically rebuilds and deploys
```

---

## 🏗️ Architecture

### Data Flow

```
resume.yaml (source)
    ↓
yaml_to_json.py
    ↓
resume.json (intermediate)
    ↓
generate_resume.py + Jinja2 templates
    ↓
resume.html (with CSS)
    ↓
Playwright + Chromium
    ↓
resume.pdf (final output)
```

### Design Principles

1. **Separation of Concerns**
   - Data layer (YAML/JSON)
   - Template layer (Jinja2 HTML)
   - Presentation layer (CSS)
   - Generation layer (Python scripts)

2. **Single Source of Truth**
   - All resume data in one YAML/JSON file
   - Templates pull from data only
   - No hardcoded content in templates

3. **Output Format Flexibility**
   - Same data → multiple outputs
   - Easy to add new formats (LinkedIn, plain text, etc.)

4. **Developer Experience**
   - Hot reload for instant feedback
   - Clear error messages
   - Simple Makefile commands

---

## 🐛 Troubleshooting

### Common Issues

**YAML parsing errors:**
```bash
# Check indentation (spaces, not tabs)
# Quote strings with special characters
# Verify list formatting with `-` prefix

# Example:
title: "Title: Subtitle"  # Correct (quoted)
title: Title: Subtitle    # Error (unquoted colon)
```

**PDF generation fails:**
```bash
# Reinstall Playwright browsers
playwright install chromium --force
```

**CSS not loading on GitHub Pages:**
- Verify `_site` directory includes CSS files
- Check deploy.yml includes CSS copy step
- Clear browser cache

**Content doesn't fit on page:**
```css
/* Adjust in resume_style.css */
@page { margin: 8mm; }      /* Reduce margins */
body { font-size: 8.5pt; }  /* Smaller font */
```

**Hot reload not working:**
```bash
# Check if livereload is installed
pip install livereload

# Verify port 8000 is available
lsof -i :8000  # Kill any conflicting process
```

---

## 📊 Technical Highlights

### Why Playwright for PDF Generation?

| Feature | Playwright | WeasyPrint |
|---------|-----------|------------|
| CSS Grid Support | ✅ Full | ❌ Limited |
| Modern CSS | ✅ All features | ⚠️ Partial |
| Rendering Accuracy | ✅ Pixel-perfect | ⚠️ Approximate |
| Font Support | ✅ System fonts | ⚠️ Requires embedding |
| Maintenance | ✅ Active (Microsoft) | ⚠️ Community |

### Performance Optimization

- **Lazy browser initialization** - Only when generating PDFs
- **Concurrent generation** - Visual and ATS versions in sequence
- **Asset optimization** - Minimal CSS with no external dependencies
- **Caching strategy** - GitHub Pages serves static assets with caching headers

### Code Quality

- **Type hints** where beneficial for readability
- **Error handling** with informative messages
- **Modular design** - Each script has single responsibility
- **Documentation** - Inline comments for complex logic

---

## 🤝 Contributing

While this is a personal resume generator, contributions are welcome! Feel free to:

- 🐛 Report bugs via GitHub Issues
- 💡 Suggest features or improvements
- 🔧 Submit pull requests
- ⭐ Star the repo if you find it useful

---

## 📄 License

**MIT License** - Feel free to use, modify, and distribute for your own resume.

See [LICENSE](LICENSE) file for full details.

---

## 🙏 Acknowledgments

- **Jinja2** - Powerful and flexible templating
- **Playwright** - Reliable browser automation and PDF generation
- **GitHub Pages** - Free hosting for static sites
- **GitHub Actions** - Seamless CI/CD integration

---

## 📧 Contact

**Josh Goldstein**
- 🌐 Website: [joshsgoldstein.github.io/resume-generator](https://joshsgoldstein.github.io/resume-generator/)
- 💼 LinkedIn: [linkedin.com/in/joshsgoldstein](https://linkedin.com/in/joshsgoldstein)
- 🐙 GitHub: [@joshsgoldstein](https://github.com/joshsgoldstein)

---

<div align="center">

Made with ❤️ by Josh Goldstein

**[View Live Demo](https://joshsgoldstein.github.io/resume-generator/)** | **[Report Bug](https://github.com/joshsgoldstein/resume-generator/issues)** | **[Request Feature](https://github.com/joshsgoldstein/resume-generator/issues)**

</div>
