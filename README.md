# Sandhya R — Portfolio

Personal portfolio for Sandhya R, Software Developer (Python, FastAPI, React, PostgreSQL, AWS, LLMs/RAG).

The page is `index.html` plus the `assets/` folder (styles, scripts and the profile photo). It was redesigned with the Taste Skill design system: a light warm theme with a maroon accent, the Hanken Grotesk font, and one section per screen. Skill icons are embedded in the page, and the resume links to Google Drive.

## Sections

- Skills: 52 skills in eight groups, each with its icon
- Work experience: Finstein Advizory Service LLP, Altruisty, Chennai Metro Rail Limited, Tata Virtual Internship
- Projects: 10 projects with highlights, tech tags and source links
- Education, certifications and contact

## Editing

Edit `build/template.html`, then regenerate `index.html`:

```
python build/build.py
```

`build/icons.json` holds the icons as embedded images. Page styles specific to this site sit in the second `<style>` block of the template; the shared design system lives in `assets/`. To add an icon, add its URL to `build/icons.py` and run `python build/icons.py` once.

## Deploying

Deploy `index.html` together with the `assets/` folder: drag the whole project folder onto Netlify's Deploys tab, or turn on GitHub Pages for this repo's `main` branch.

## Contact

- Email: sandhyasubha192005@gmail.com
- LinkedIn: [sandhya192005](https://linkedin.com/in/sandhya192005)
- GitHub: [Sandhya192005](https://github.com/Sandhya192005)
