# Sandhya R — Portfolio

Personal portfolio for Sandhya R, Software Developer, DevOps Engineer and AI Engineer (Python, FastAPI, PostgreSQL, Docker, AWS, LLMs/RAG).

The page is `index.html` plus the `assets/` folder (styles, scripts and the profile photo). It was redesigned with the Taste Skill design system: a light warm theme with a maroon accent, the Hanken Grotesk font, and one section per screen. Skill icons are embedded in the page, and the resume is `assets/Sandhya-R-Resume.pdf`. Its source is `build/resume.html`: edit that, then run `python build/resume.py assets/Sandhya-R-Resume.pdf` to print a new one-page PDF.

## Pages

The home page (`index.html`) is the introduction only: photo, roles, resume and contact. Each section has its own page, opened from the menu:

- `skills.html`: skills in nine groups, each tool with its icon
- `experience.html`: Finstein Advizory Service LLP, Altruisty, Chennai Metro Rail Limited, Tata Virtual Internship
- `projects.html`: 10 projects with highlights, tech tags and source links
- `education.html`: education, certificates and awards

## Editing

Edit `build/template.html`, then regenerate all the pages:

```
python build/build.py
```

In the template, each `<!--name-->...<!--/name-->` block (home, skills, experience, projects, education) appears only on that page; the head, menu and footer are shared by all of them.

`build/icons.json` holds the icons as embedded images. Page styles specific to this site sit in the second `<style>` block of the template; the shared design system lives in `assets/`. To add an icon, add its URL to `build/icons.py` and run `python build/icons.py` once.

## Deploying

Deploy the five HTML pages together with the `assets/` folder: drag the whole project folder onto Netlify's Deploys tab, or turn on GitHub Pages for this repo's `main` branch.

## Contact

- Email: sandhyasubha192005@gmail.com
- LinkedIn: [sandhya192005](https://linkedin.com/in/sandhya192005)
- GitHub: [Sandhya192005](https://github.com/Sandhya192005)
