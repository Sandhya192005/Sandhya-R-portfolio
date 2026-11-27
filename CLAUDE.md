# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A static, multi-page personal portfolio (no framework, no package.json, no tests). The five root HTML pages (`index.html`, `skills.html`, `experience.html`, `projects.html`, `education.html`) are **generated output**: never edit them directly. Deploy = the five pages plus `assets/` (Netlify drag-and-drop or GitHub Pages on `main`).

## Commands

All scripts are plain Python, run from the repo root:

```
python build/build.py                                   # regenerate all five pages from build/template.html
python build/shots.py                                   # redraw project card mockups -> assets/img/projects/*.svg
python build/icons.py                                   # re-download icons into build/icons.json (only after adding an icon URL)
python build/resume.py assets/Sandhya-R-Resume.pdf      # print build/resume.html to a one-page A4 PDF (needs Playwright + Edge/Chromium)
```

To preview, open the generated HTML files in a browser (or serve the root with `python -m http.server`; the JS in `assets/` is loaded as ES modules, which may not work over `file://`).

## Architecture

**Single template → five pages.** `build/template.html` holds everything. `build/build.py`:
- Keeps only the `<!--name-->...<!--/name-->` block matching the current page (`home`, `skills`, `experience`, `projects`, `education`) and strips the others; everything outside those blocks (head, nav, footer, scripts) is shared.
- Sets each page's `<title>` and meta description from the `PAGES` dict in `build.py` — edit them there, not in the template.
- Replaces `{{current:page}}` with `aria-current="page"` in the nav.
- Expands `{{chip:key|Label}}` / `{{tag:key|Label}}` into `<li>` items with an inlined icon, and `{{logo:key}}` into a bare image. Keys must exist in `build/icons.json` (data URIs). The build asserts no `{{` placeholders or block markers survive.
- Adding a new page means adding it to `PAGES`, adding a block in the template, and adding a nav link.

**Icons.** `build/icons.py` maps icon keys to CDN SVG URLs (devicon, simple-icons, lucide) and embeds them as data URIs in `icons.json`, so the built pages make no icon requests.

**Project pictures.** `build/shots.py` hand-draws an SVG app-screen mockup per project (one accent color per project in `THEMES`). The template references `assets/img/projects/*.svg`, so run this script if those files are missing.

**Styling.** The shared design system lives in `assets/` (`system.css/js`, `ui/`, `layout/`, `motion/`, `icons/`), produced by the Taste Skill (`design-taste-frontend`) design system. Site-specific CSS sits in the second `<style>` block of `build/template.html`. Theme: light warm background, maroon accent, Hanken Grotesk (Google Fonts), one section per screen.

**Resume.** Source is `build/resume.html`; the PDF in `assets/` is printed from it with `resume.py`.

`shots/` and `.taste-skill/` are git-ignored screenshots and design-checker reports.
