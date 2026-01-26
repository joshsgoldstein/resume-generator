"""
watch.py

Hot reload server for resume development.
Watches for changes to resume.yaml and templates, regenerates HTML, and refreshes browser.

Usage:
    python watch.py
"""

from livereload import Server
import subprocess


def regenerate():
    """Regenerate HTML files from resume data."""
    print("🔄 Regenerating resumes...")
    subprocess.run(["python", "generate_resume.py"], check=True)
    print("✓ Done!")


if __name__ == "__main__":
    server = Server()

    # Watch source files and regenerate on change
    server.watch("resume.yaml", regenerate)
    server.watch("resume.json", regenerate)
    server.watch("resume_template.html", regenerate)
    server.watch("resume_template_ats.html", regenerate)
    server.watch("resume_style.css")
    server.watch("resume_style_ats.css")

    # Initial generation
    regenerate()

    print("\n🚀 Hot reload server running!")
    print("   http://localhost:8000/            → Landing page")
    print("   http://localhost:8000/resume.html → Visual resume")
    print("   http://localhost:8000/resume_ats.html → ATS resume")
    print("\n   Watching: resume.yaml, templates, CSS files")
    print("   Press Ctrl+C to stop\n")

    # Serve current directory
    server.serve(root=".", port=8000)
