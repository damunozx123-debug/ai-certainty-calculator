"""Capture a fully rendered Streamlit app, never a blank initial HTML shell."""
from pathlib import Path
import shutil
from playwright.sync_api import sync_playwright

out = Path("docs/screenshots/scenario-desktop.png")
out.parent.mkdir(parents=True, exist_ok=True)
chrome = shutil.which("google-chrome") or shutil.which("google-chrome-stable") or shutil.which("chromium")
if not chrome:
    raise RuntimeError("Chrome is unavailable")
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(executable_path=chrome, headless=True, args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": 1380, "height": 920}, device_scale_factor=1)
    page.goto("http://127.0.0.1:8501/", wait_until="domcontentloaded", timeout=30000)
    page.get_by_text("Illustrative monthly difference", exact=True).wait_for(state="visible", timeout=30000)
    page.get_by_text("Annualised scenario difference", exact=True).wait_for(state="visible", timeout=30000)
    page.screenshot(path=str(out), full_page=True, animations="disabled")
    browser.close()
print(f"Verified screenshot from rendered metrics: {out}, {out.stat().st_size} bytes")
