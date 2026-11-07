# Builds ../index.html from template.html, inlining tool icons from icons.json
import json, re, pathlib
here = pathlib.Path(__file__).parent
icons = json.loads((here / "icons.json").read_text())
html = (here / "template.html").read_text(encoding="utf8")
def sub(m):
    key, label = m.group(2), m.group(3)
    return f'<li><span class="ic"><img src="{icons[key]}" alt="" width="18" height="18" loading="lazy"></span>{label}</li>'
html = re.sub(r"\{\{(chip|tag):(\w+)\|([^}]+)\}\}", sub, html)
# {{logo:key}}: a bare logo image, for links that carry their own label
html = re.sub(r"\{\{logo:(\w+)\}\}", lambda m: f'<img src="{icons[m.group(1)]}" alt="" width="20" height="20">', html)
assert "{{" not in html
(here.parent / "index.html").write_text(html, encoding="utf8")
print("built", len(html), "bytes;", html.count('class="ic"'), "tool icons")
