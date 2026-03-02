from playwright.sync_api import sync_playwright
import os

def verify_svg(page):
    filepath = "file://" + os.path.abspath("verification/svg_test.html")
    page.goto(filepath)
    page.screenshot(path="/home/jules/verification/svg_test.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_svg(page)
        finally:
            browser.close()
