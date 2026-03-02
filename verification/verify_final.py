from playwright.sync_api import sync_playwright

def verify_skeleton_final(page):
    page.goto("http://localhost:8000")
    page.screenshot(path="/home/jules/verification/skeleton_final_desktop.png")

    # Test mobile
    page.set_viewport_size({"width": 375, "height": 667})
    page.screenshot(path="/home/jules/verification/skeleton_final_mobile.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_skeleton_final(page)
        finally:
            browser.close()
