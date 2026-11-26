# Downloads skill icons once and saves them as data URIs in icons.json
import json, urllib.request, base64, pathlib
DV = "https://cdn.jsdelivr.net/gh/devicons/devicon@v2.16.0/icons/"
SI = "https://cdn.jsdelivr.net/npm/simple-icons@13.21.0/icons/"
LU = "https://cdn.jsdelivr.net/npm/lucide-static@0.460.0/icons/"
MAROON = "#9e2a4a"
icons = {
 "python": DV+"python/python-original.svg", "java": DV+"java/java-original.svg",
 "javascript": DV+"javascript/javascript-original.svg", "typescript": DV+"typescript/typescript-original.svg",
 "sql": LU+"database.svg", "html": DV+"html5/html5-original.svg", "css": DV+"css3/css3-original.svg",
 "react": DV+"react/react-original.svg", "nextjs": DV+"nextjs/nextjs-original.svg",
 "tailwind": DV+"tailwindcss/tailwindcss-original.svg", "threejs": DV+"threejs/threejs-original.svg",
 "vite": DV+"vitejs/vitejs-original.svg",
 "fastapi": DV+"fastapi/fastapi-original.svg", "django": DV+"django/django-plain.svg",
 "nodejs": DV+"nodejs/nodejs-original.svg", "express": DV+"express/express-original.svg",
 "rest": LU+"network.svg", "celery": SI+"celery.svg", "sqlalchemy": DV+"sqlalchemy/sqlalchemy-original.svg",
 "postgresql": DV+"postgresql/postgresql-original.svg", "mongodb": DV+"mongodb/mongodb-original.svg",
 "redis": DV+"redis/redis-original.svg", "mysql": DV+"mysql/mysql-original.svg", "sqlite": DV+"sqlite/sqlite-original.svg",
 "vectordb": LU+"boxes.svg",
 "pytest": DV+"pytest/pytest-original.svg", "playwright": DV+"playwright/playwright-original.svg",
 "aws": DV+"amazonwebservices/amazonwebservices-original-wordmark.svg",
 "git": DV+"git/git-original.svg", "github": DV+"github/github-original.svg",
 "githubactions": DV+"githubactions/githubactions-original.svg", "jenkins": DV+"jenkins/jenkins-original.svg",
 "docker": DV+"docker/docker-original.svg", "linux": DV+"ubuntu/ubuntu-original.svg",
 "kubernetes": DV+"kubernetes/kubernetes-original.svg", "nginx": DV+"nginx/nginx-original.svg", "terraform": DV+"terraform/terraform-original.svg",
 "llm": LU+"brain-circuit.svg", "rag": LU+"file-search.svg", "embeddings": LU+"chart-scatter.svg",
 "openai": LU+"sparkles.svg",
 "vscode": DV+"vscode/vscode-original.svg", "canva": DV+"canva/canva-original.svg", "antigravity": LU+"rocket.svg",  # no Antigravity logo on the icon CDNs yet
 "swagger": DV+"swagger/swagger-original.svg", "postman": DV+"postman/postman-original.svg", "n8n": SI+"n8n.svg",
 "oop": LU+"blocks.svg", "dbms": LU+"database-zap.svg", "mvc": LU+"layers.svg", "http": LU+"arrow-left-right.svg",
 "restfund": LU+"globe.svg", "cicd": LU+"infinity.svg",
 "chunking": LU+"scissors.svg", "orchestration": LU+"workflow.svg", "finetuning": LU+"sliders-horizontal.svg",
 "sklearn": DV+"scikitlearn/scikitlearn-original.svg", "numpy": DV+"numpy/numpy-original.svg",
 "pandas": DV+"pandas/pandas-original.svg", "matplotlib": DV+"matplotlib/matplotlib-original.svg",
 "tensorflow": DV+"tensorflow/tensorflow-original.svg", "pytorch": DV+"pytorch/pytorch-original.svg",
 "pydantic": SI+"pydantic.svg",
 "huggingface": SI+"huggingface.svg", "langchain": SI+"langchain.svg", "ollama": SI+"ollama.svg",
 "coursera": SI+"coursera.svg", "colab": SI+"googlecolab.svg", "tableau": SI+"tableau.svg",
 "excel": LU+"sheet.svg", "powerbi": LU+"chart-column-big.svg",  # no Excel or Power BI logo on the icon CDNs
 "databricks": SI+"databricks.svg", "pyspark": DV+"apachespark/apachespark-original.svg",
 "linkedin": DV+"linkedin/linkedin-original.svg", "email": LU+"mail.svg",
 # section icons for the skills, experience and education pages
 "i_code": LU+"code-xml.svg", "i_server": LU+"server.svg", "i_cloud": LU+"cloud-cog.svg", "i_ai": LU+"brain-circuit.svg",
 "i_db": LU+"database.svg", "i_frontend": LU+"monitor-smartphone.svg", "i_test": LU+"flask-conical.svg",
 "i_tools": LU+"wrench.svg", "i_data": LU+"chart-column.svg", "i_ideas": LU+"lightbulb.svg", "i_star": LU+"star.svg",
 "i_grad": LU+"graduation-cap.svg", "i_school": LU+"school.svg", "i_cert": LU+"badge-check.svg", "i_trophy": LU+"trophy.svg",
}
brand = {"celery": "#37814A", "n8n": "#EA4B71", "databricks": "#FF3621", "huggingface": "#FFD21E", "langchain": "#1C3C3C", "pydantic": "#E92063", "colab": "#F9AB00", "tableau": "#E97627", "coursera": "#0056D2"}
out, bad = {}, []
for k, url in icons.items():
    try:
        svg = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "portfolio-build"}), timeout=20).read().decode("utf8")
        if "<svg" not in svg: raise ValueError("not svg")
    except Exception as e:
        bad.append((k, url, str(e))); continue
    if url.startswith(LU): svg = svg.replace('stroke="currentColor"', f'stroke="{MAROON}"')
    if k in brand: svg = svg.replace("<svg ", f'<svg fill="{brand[k]}" ', 1)
    out[k] = "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()
pathlib.Path(__file__).with_name("icons.json").write_text(json.dumps(out))
print(len(out), "ok; failed:", bad)
