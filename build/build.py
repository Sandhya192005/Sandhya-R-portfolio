# Builds ../index.html from template.html, inlining icons from icons.json
import json, re, pathlib
here = pathlib.Path(__file__).parent
icons = json.loads((here / "icons.json").read_text())
html = (here / "template.html").read_text(encoding="utf8")
def sub(m):
    kind, key, label = m.group(1), m.group(2), m.group(3)
    src = icons[key]
    if kind == "ico":
        return f'<span class="{label}" aria-hidden="true"><img src="{src}" alt="" width="24" height="24"></span>'
    if kind == "chip":
        return f'<li class="chip"><span class="ic"><img src="{src}" alt="" width="24" height="24"></span><span>{label}</span></li>'
    return f'<li><span class="mini"><img src="{src}" alt="" width="14" height="14"></span>{label}</li>'
html = re.sub(r"\{\{(chip|tag|ico):(\w+)\|([^}]+)\}\}", sub, html)
assert "{{" not in html
(here.parent / "index.html").write_text(html, encoding="utf8")
print("built", len(html), "bytes;", html.count('class="chip"'), "skill chips")
