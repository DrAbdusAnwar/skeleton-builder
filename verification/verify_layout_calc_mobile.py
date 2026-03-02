from playwright.sync_api import sync_playwright
import os

def verify_layout_mobile(page):
    filepath = "file://" + os.path.abspath("verification/layout_test_calc_mobile.html")
    page.goto(filepath)
    page.screenshot(path="/home/jules/verification/layout_test_calc_mobile.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_layout_mobile(page)
        finally:
            browser.close()
