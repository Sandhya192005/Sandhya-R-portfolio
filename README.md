# Sandhya R — Portfolio

Personal portfolio for Sandhya R, Software Developer (Python, FastAPI, React, PostgreSQL, AWS, LLMs/RAG).

It's a single self-contained page: plain HTML and CSS, no frameworks and no build step needed to view it. All skill icons are embedded in the page, and the resume download links to Google Drive, so `index.html` is the only file to deploy.

## Sections

- Tech stack: 48 skills grouped by area, each with its icon
- Work experience: Finstein Advizory Service LLP, Altruisty, Chennai Metro Rail Limited, Tata Virtual Internship
- Projects: 10 projects with highlights, tech tags and source links
- Education, certifications and contact

## Editing

Edit `build/template.html`, then regenerate `index.html`:

```
python build/build.py
```

`build/icons.json` holds the icons as embedded images. To add an icon, add its URL to `build/icons.py` and run `python build/icons.py` once.

## Deploying

Upload `index.html` to Netlify (drag it onto the site's Deploys tab), or turn on GitHub Pages for this repo's `main` branch.

## Contact

- Email: sandhyasubha192005@gmail.com
- LinkedIn: [sandhya192005](https://linkedin.com/in/sandhya192005)
- GitHub: [Sandhya192005](https://github.com/Sandhya192005)
