import threading
import time
from playwright.sync_api import sync_playwright

PORT = 8081

def test_audio():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Override AudioContext to track calls
        page.add_init_script("""
            window.audioCalls = [];
            const OriginalAudioContext = window.AudioContext || window.webkitAudioContext;
            class MockAudioContext extends OriginalAudioContext {
                createOscillator() {
                    const osc = super.createOscillator();
                    const originalStart = osc.start.bind(osc);
                    osc.start = function(...args) {
                        window.audioCalls.push({ type: 'start', oscType: osc.type });
                        return originalStart(...args);
                    };
                    return osc;
                }
            }
            window.AudioContext = MockAudioContext;
            window.webkitAudioContext = MockAudioContext;
        """)

        page.goto(f"http://localhost:{PORT}/index.html")
        page.wait_for_load_state("networkidle")

        # Trigger playSnapSound directly to test it
        page.evaluate("playSnapSound()")

        # Give it a tiny bit of time to execute
        time.sleep(0.5)

        # Check logs
        calls = page.evaluate("window.audioCalls")
        print(f"Audio calls after snap: {calls}")
        assert len(calls) == 1, "Snap sound should create 1 oscillator start"
        assert calls[0]['oscType'] == 'triangle', "Snap sound should use a triangle wave"

        # Trigger playWinSound
        page.evaluate("window.audioCalls = []")
        page.evaluate("playWinSound()")
        time.sleep(0.5)

        calls = page.evaluate("window.audioCalls")
        print(f"Audio calls after win: {calls}")
        assert len(calls) == 4, "Win sound should create 4 oscillator starts (arpeggio)"
        for call in calls:
            assert call['oscType'] == 'sine', "Win sound should use sine waves"

        page.screenshot(path="verification/verification.png")
        print("Audio functions successfully verified in browser environment.")
        browser.close()

if __name__ == "__main__":
    test_audio()
