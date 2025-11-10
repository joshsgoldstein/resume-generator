"""
generate_resume.py

Render an HTML + PDF resume from a Python data structure using Jinja2 + WeasyPrint.

Usage:
    pip install jinja2 weasyprint

    python generate_resume.py

This will produce:
    - resume.html
    - resume.pdf
"""

from pathlib import Path
from jinja2 import Template
from weasyprint import HTML

# ---------- 1. RESUME DATA: EDIT THIS PART TO POPULATE SECTIONS ----------

resume_data = {
    "name": "Josh Goldstein",
    "tagline": "Creative Technology · Senior Solutions Architect",
    "summary": (
        "Technical services, planning and implementation specialist with over ten years of "
        "customer-facing experience. Proven ability to design, sell, and deliver complex technical "
        "solutions for enterprise customers, including multiple Fortune 500 organizations."
    ),

    "contact": {
        "address": "50 N 1st St, Apt 5H, Brooklyn, NY 11249",
        "phone": "305-321-6144",
        "email": "Josh4goldstein@gmail.com",
        "website": "",   # e.g. "https://your-site.com"
        "linkedin": "https://linkedin.com/in/joshsgoldstein",  # e.g. "https://linkedin.com/in/..."
        "github": "https://github.com/joshsgoldstein"     # e.g. "https://github.com/..."
    },

    "technical_skills": [
       "Data modeling", "Vector Databases", "Agentic Ai Frameworks", "Chunking Frameworks" 
       "AWS", "GCP", "Azure", "MLOps",
       "Python", "Javascript", "Java", "React", "Node.js",
       "Docker", "Kubernetes", "SQL Databases", "NoSQL Databases", "Graph Databases",
        "Solr", "Elasticsearch",
        "Enterprise Authentication and Authorization technologies",
        "Enterprise  Solution/Architecture Desing and Implementation"
        "Spark", "Scala",
    ],

    "soft_skills": [
        "Customer Account Management",
        "Presentation Skills",
        "Collaboration/Knowledge Management Practices",
        "Knowledge Management Practices",
        "Requirements Gathering",
        "Solution Design",
        "Self-motivated",
        "Technical Research and Analysis"
    ],

    "speaking_engagements": [
        {
            "title": "Digital experience for the next generation knowledge worker",
            "event": "Activate 2019"
        },
        {
            "title": "Common mistakes made deploying a search application with Lucidworks Fusion",
            "event": "Activate 2018"
        },
        {
            "title": "Ethics in tech",
            "event": "UC Berkeley EECS Honors Program"
        },
        {
            "title": "From Model to Microservice > MLOps at Scale",
            "event": "Southern Data Science Conference"
        },
        {
            "title": "Various Apache Solr Meetups",
            "event": ""
        },
    ],

    "experience": [
        {
            "role": "Solutions Engineer",
            "company": "Keeeb Inc.",
            "location": "Boston, MA",
            "start": "Jan 2021",
            "end": "Dec 2019",  # fix dates as you like
            "bullets": [
                "Designed sales process leading to first US logo win.",
                "Implemented process for new features and bugs with engineering, improving time-to-resolution.",
                "Collaborated with product and engineering on features to enable upsell opportunities.",
                "Conducted R&D within the Microsoft ecosystem to support product requirements."
            ]
        },
        {
            "role": "Business Innovation Manager",
            "company": "Lucidworks Inc.",
            "location": "San Francisco, CA",
            "start": "Mar 2019",
            "end": "Dec 2019",
            "bullets": [
                "Drove relationships with internal stakeholders and executives to develop new use cases and internal tools.",
                "Led Lucidworks’ first beta program introducing new products to customers.",
                "Coordinated with the Knowledge Management team on contributions to the corporate knowledge base.",
                "Advised Customer Success on product sales using deep knowledge of features and capabilities."
            ]
        },
        {
            "role": "Solution Architect",
            "company": "Lucidworks Inc.",
            "location": "San Francisco, CA",
            "start": "Jun 2017",
            "end": "Mar 2019",
            "bullets": [
                "Designed and implemented custom solutions for internal enterprise applications.",
                "Created product demos for sales and marketing, contributing to inclusion in Gartner Magic Quadrant.",
                "Developed internal enablement programs for new technologies (mentorship, training, 1:1 sessions).",
                "Integrated third-party vendors into Lucidworks stack to drive sales and implementations."
            ]
        },
        {
            "role": "Sales Engineer",
            "company": "Lucidworks Inc.",
            "location": "San Francisco, CA",
            "start": "Feb 2016",
            "end": "Jun 2017",
            "bullets": [
                "Supported sales teams by designing and presenting solutions to complex customer problems.",
                "Contributed to exceeding sales targets across 15 consecutive quarters.",
                "Planned and executed strategic account POCs for multi-million-dollar clients.",
                "Enabled inside sales with deeper technical knowledge to drive new business.",
                "Improved training program reliability by leveraging AWS for a better student experience."
            ]
        },
        {
            "role": "Founder",
            "company": "BluPrinteIT",
            "location": "Miami, FL",
            "start": "Apr 2014",
            "end": "Jan 2016",
            "bullets": [
                "Developed custom dashboard application from concept through implementation centered on real-time news.",
                "Built monitoring application to enhance application/service continuity.",
                "Prioritized and implemented new features for POC, leading to early sales.",
                "Continuously assessed internal business needs to guide technology decisions and drive business value."
            ]
        },
        {
            "role": "SharePoint Consultant",
            "company": "IImagineIT",
            "location": "Houston, TX",
            "start": "Feb 2012",
            "end": "Apr 2014",
            "bullets": [
                "Designed and implemented SharePoint applications to increase employee productivity.",
                "Served as embedded consultant, responding quickly to day-to-day technical needs.",
                "Delivered end-user training programs on behalf of clients.",
                "Advised clients on collaboration and knowledge management best practices."
            ]
        },
    ],

    "education": [
        {
            "degree": "Bachelor of Science: Management Information Systems",
            "school": "Rochester Institute of Technology",
            "location": "Rochester, NY",
            "start": "Aug 2007",
            "end": "Dec 2011",
            "notes": "Additional concentrations/minor in Finance and Communications."
        }
    ]
}

# ---------- 2. HTML TEMPLATE (LAYOUT) ----------

RESUME_TEMPLATE = Template(r"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>{{ name }} - Resume</title>
    <style>
        @page {
            size: A4;
            margin: 18mm;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
            color: #222;
            line-height: 1.5;
            font-size: 11pt;
        }
        * {
            box-sizing: border-box;
        }
        .page {
            display: flex;
            flex-direction: column;
        }

        /* Header */
        .header {
            border-bottom: 2px solid #333;
            padding-bottom: 8px;
            margin-bottom: 10px;
        }
        .name {
            font-size: 24pt;
            font-weight: 700;
            letter-spacing: 0.03em;
        }
        .tagline {
            font-size: 11pt;
            color: #555;
            margin-top: 4px;
        }

        .contact-line {
            margin-top: 6px;
            font-size: 9.5pt;
            color: #555;
        }
        .contact-line span {
            margin-right: 10px;
        }

        /* Layout: main content + sidebar */
        .layout {
            display: grid;
            grid-template-columns: 3fr 1.4fr;
            gap: 18px;
            margin-top: 10px;
        }

        /* Sections */
        h2.section-title {
            font-size: 11pt;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            border-bottom: 1px solid #ccc;
            padding-bottom: 3px;
            margin: 14px 0 8px;
        }

        .summary {
            font-size: 10.5pt;
        }

        .experience-item {
            margin-bottom: 10px;
        }
        .experience-header {
            display: flex;
            justify-content: space-between;
            font-weight: 600;
            font-size: 10.5pt;
        }
        .experience-role-company {
            max-width: 70%;
        }
        .experience-dates-location {
            text-align: right;
            font-size: 9pt;
            color: #555;
        }
        .experience-bullets {
            margin: 4px 0 0 0;
            padding-left: 18px;
            font-size: 10pt;
        }

        /* Sidebar */
        .sidebar-section {
            margin-bottom: 14px;
        }
        .sidebar-list {
            list-style: none;
            padding-left: 0;
            margin: 4px 0 0 0;
            font-size: 9.5pt;
        }
        .sidebar-list li {
            margin-bottom: 3px;
        }
        .skills-comma-list {
            margin: 4px 0 0 0;
            font-size: 9.5pt;
            line-height: 1.6;
        }

        .speaking-item {
            font-size: 9.5pt;
            margin-bottom: 4px;
        }
        .speaking-title {
            font-weight: 600;
        }
        .speaking-event {
            color: #555;
        }

        .education-item {
            margin-bottom: 8px;
            font-size: 10pt;
        }
        .degree {
            font-weight: 600;
        }
        .school {
            margin-top: 2px;
        }
        .edu-dates {
            font-size: 9pt;
            color: #555;
        }
    </style>
</head>
<body>
<div class="page">

    <!-- HEADER -->
    <header class="header">
        <div class="name">{{ name }}</div>
        {% if tagline %}
        <div class="tagline">{{ tagline }}</div>
        {% endif %}

        <div class="contact-line">
            {% if contact.address %}<span>{{ contact.address }}</span>{% endif %}
            {% if contact.phone %}<span>{{ contact.phone }}</span>{% endif %}
            {% if contact.email %}<span>{{ contact.email }}</span>{% endif %}
        </div>
        <div class="contact-line">
            {% if contact.website %}<span>{{ contact.website }}</span>{% endif %}
            {% if contact.linkedin %}<span>{{ contact.linkedin }}</span>{% endif %}
            {% if contact.github %}<span>{{ contact.github }}</span>{% endif %}
        </div>
    </header>

    <div class="layout">
        <!-- MAIN COLUMN -->
        <main>
            <!-- Summary -->
            {% if summary %}
            <section>
                <h2 class="section-title">Highlights</h2>
                <div class="summary">
                    {{ summary }}
                </div>
            </section>
            {% endif %}

            <!-- Experience -->
            {% if experience %}
            <section>
                <h2 class="section-title">Work History</h2>
                {% for job in experience %}
                <div class="experience-item">
                    <div class="experience-header">
                        <div class="experience-role-company">
                            {{ job.role }} &mdash; {{ job.company }}
                        </div>
                        <div class="experience-dates-location">
                            {{ job.start }} &ndash; {{ job.end }}{% if job.location %} · {{ job.location }}{% endif %}
                        </div>
                    </div>
                    {% if job.bullets %}
                    <ul class="experience-bullets">
                        {% for bullet in job.bullets %}
                        <li>{{ bullet }}</li>
                        {% endfor %}
                    </ul>
                    {% endif %}
                </div>
                {% endfor %}
            </section>
            {% endif %}

            <!-- Education -->
            {% if education %}
            <section>
                <h2 class="section-title">Education</h2>
                {% for edu in education %}
                <div class="education-item">
                    <div class="degree">{{ edu.degree }}</div>
                    <div class="school">{{ edu.school }}{% if edu.location %}, {{ edu.location }}{% endif %}</div>
                    <div class="edu-dates">{{ edu.start }} – {{ edu.end }}</div>
                    {% if edu.notes %}
                    <div class="edu-notes">{{ edu.notes }}</div>
                    {% endif %}
                </div>
                {% endfor %}
            </section>
            {% endif %}
        </main>

        <!-- SIDEBAR -->
        <aside>
            {% if technical_skills %}
            <section class="sidebar-section">
                <h2 class="section-title">Technical Skills</h2>
                <div class="skills-comma-list">
                    {{ technical_skills|join(', ') }}
                </div>
            </section>
            {% endif %}

            {% if soft_skills %}
            <section class="sidebar-section">
                <h2 class="section-title">Soft Skills</h2>
                <div class="skills-comma-list">
                    {{ soft_skills|join(', ') }}
                </div>
            </section>
            {% endif %}

            {% if speaking_engagements %}
            <section class="sidebar-section">
                <h2 class="section-title">Speaking</h2>
                {% for talk in speaking_engagements %}
                <div class="speaking-item">
                    <div class="speaking-title">{{ talk.title }}</div>
                    {% if talk.event %}
                    <div class="speaking-event">{{ talk.event }}</div>
                    {% endif %}
                </div>
                {% endfor %}
            </section>
            {% endif %}
        </aside>
    </div>
</div>
</body>
</html>
""")


# ---------- 3. RENDER FUNCTIONS ----------

def render_resume_html(data: dict) -> str:
    """Render the HTML string from resume_data."""
    return RESUME_TEMPLATE.render(**data)


def save_html_and_pdf(data: dict, html_path: str = "resume.html", pdf_path: str = "resume.pdf"):
    html_str = render_resume_html(data)
    Path(html_path).write_text(html_str, encoding="utf-8")
    # Generate PDF
    HTML(string=html_str).write_pdf(pdf_path)
    print(f"Saved HTML -> {html_path}")
    print(f"Saved PDF  -> {pdf_path}")


if __name__ == "__main__":
    save_html_and_pdf(resume_data)
