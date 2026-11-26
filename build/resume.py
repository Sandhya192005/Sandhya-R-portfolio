# Prints build/resume.html to a one-page A4 PDF (needs Playwright and Microsoft Edge or Chromium).
# Usage: python build/resume.py [output.pdf]   (default: build/Sandhya-R-Resume.pdf)
import sys, pathlib
from playwright.sync_api import sync_playwright

here = pathlib.Path(__file__).parent
out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else here / "Sandhya-R-Resume.pdf"
with sync_playwright() as p:
    try:
        browser = p.chromium.launch(channel="msedge")
    except Exception:
        browser = p.chromium.launch()
    page = browser.new_page()
    page.goto((here / "resume.html").resolve().as_uri(), wait_until="networkidle")
    page.pdf(path=str(out), format="A4", print_background=True, prefer_css_page_size=True)
    browser.close()
print("wrote", out)
