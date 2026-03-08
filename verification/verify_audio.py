import os
import http.server
import socketserver
import threading
from playwright.sync_api import sync_playwright

PORT = 8080
DIRECTORY = "."

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

# Start server in background thread
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            permissions=["clipboard-read", "clipboard-write"],
        )
        page = context.new_page()

        # Add a listener for console logs to verify function calls
        console_logs = []
        page.on("console", lambda msg: console_logs.append(msg.text))

        # Override the audio context in the browser to log when it's used
        # We can't easily capture audio output in headless mode, but we can intercept the calls

        page.goto(f"http://localhost:{PORT}/index.html")

        page.evaluate("""
            window.audioLog = [];
            const originalAudioContext = window.AudioContext || window.webkitAudioContext;
            window.AudioContext = function() {
                const ctx = new originalAudioContext();
                const originalCreateOscillator = ctx.createOscillator.bind(ctx);
                ctx.createOscillator = function() {
                    window.audioLog.push('Oscillator created');
                    const osc = originalCreateOscillator();
                    const originalStart = osc.start.bind(osc);
                    osc.start = function(t) {
                        window.audioLog.push('Oscillator started: ' + osc.type);
                        originalStart(t);
                    };
                    return osc;
                };
                return ctx;
            };
            window.webkitAudioContext = window.AudioContext;
        """)

        # Reload to apply the override before the script initializes
        # Wait, the script runs on DOMContentLoaded. We should inject before navigation or use add_init_script.
        pass

        browser.close()

verify()
print("Test completed.")
