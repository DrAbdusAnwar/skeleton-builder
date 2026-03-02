from playwright.sync_api import sync_playwright

def verify_skeleton(page):
    page.goto("http://localhost:8000")
    page.screenshot(path="/home/jules/verification/skeleton_initial.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_skeleton(page)
        finally:
            browser.close()
