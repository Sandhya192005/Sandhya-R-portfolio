# Builds one HTML page per section from template.html, inlining tool icons from icons.json.
# In the template, each <!--name-->...<!--/name--> block appears only on that page
# (home -> index.html, skills -> skills.html, and so on); everything outside the blocks
# (head, nav, footer) is shared by all pages.
import json, re, pathlib
here = pathlib.Path(__file__).parent
icons = json.loads((here / "icons.json").read_text())
src = (here / "template.html").read_text(encoding="utf8")

PAGES = {
    "home": ("index.html", "Sandhya R: software developer, DevOps and AI engineer",
             "Sandhya R, software developer, DevOps engineer and AI engineer in Chennai: backend services and AI apps with Python, FastAPI, PostgreSQL, Docker, AWS, LLMs and RAG."),
    "skills": ("skills.html", "Skills: Sandhya R",
               "Skills and tools of Sandhya R: Python, FastAPI, PostgreSQL, Docker, Kubernetes, AWS, CI/CD, LLMs, RAG and more."),
    "experience": ("experience.html", "Experience: Sandhya R",
                   "Work experience of Sandhya R: internships in full-stack development, MERN stack development, IT systems and data analytics."),
    "projects": ("projects.html", "Projects: Sandhya R",
                 "Projects by Sandhya R: AI apps, workflow automation and full-stack web apps built with Python, FastAPI, React and PostgreSQL."),
    "education": ("education.html", "Education: Sandhya R",
                  "Education of Sandhya R: B.E. Computer Science and Engineering at Velammal Engineering College, certificates and awards."),
}

def chips(html):
    def sub(m):
        key, label = m.group(2), m.group(3)
        return f'<li><span class="ic"><img src="{icons[key]}" alt="" width="18" height="18" loading="lazy"></span>{label}</li>'
    html = re.sub(r"\{\{(chip|tag):(\w+)\|([^}]+)\}\}", sub, html)
    # {{logo:key}}: a bare logo image, for links that carry their own label
    return re.sub(r"\{\{logo:(\w+)\}\}", lambda m: f'<img src="{icons[m.group(1)]}" alt="" width="20" height="20">', html)

for page, (file, title, desc) in PAGES.items():
    html = src
    for name in PAGES:
        html = re.sub(rf"<!--{name}-->\n?(.*?)<!--/{name}-->\n?",
                      lambda m: m.group(1) if name == page else "", html, flags=re.S)
    html = re.sub(r"\{\{current:(\w+)\}\}", lambda m: ' aria-current="page"' if m.group(1) == page else "", html)
    html = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", html, count=1)
    html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', html, count=1)
    html = chips(html)
    assert "{{" not in html and not re.search(r"<!--/?(" + "|".join(PAGES) + ")-->", html)
    (here.parent / file).write_text(html, encoding="utf8")
    print("built", file, len(html), "bytes;", html.count('class="ic"'), "tool icons")
