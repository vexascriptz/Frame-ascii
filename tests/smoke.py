"""Browser smoke test for Frame Studio. Run: pip install playwright; playwright install chromium; python tests/smoke.py"""
import functools
import http.server
import pathlib
import struct
import subprocess
import sys
import tempfile
import threading
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

def main():
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Handler, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    errors = []
    try:
        with sync_playwright() as p, tempfile.TemporaryDirectory() as tmp:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1440, "height": 1000}, accept_downloads=True)
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(f"http://127.0.0.1:{server.server_port}/")
            page.locator("#demo").click()
            page.locator("#output").wait_for(state="visible")
            page.wait_for_function("document.querySelector('#gridStat').textContent !== '—'")
            page.locator("#splitView").click()
            assert page.locator("#splitControls").is_visible()
            page.locator("#asciiView").click()
            page.locator("[data-preset=detail]").click()
            assert page.locator("#width").input_value() == "160"
            page.locator("#undo").click()
            assert page.locator("#width").input_value() == "120"
            page.locator("#redo").click()
            assert page.locator("#width").input_value() == "160"
            page.locator("#glyphs").select_option("braille")
            page.locator("#brailleWrap").wait_for(state="visible")
            for fmt, ext in [("py", ".py"), ("html", ".html"), ("png", ".png"), ("svg", ".svg"), ("json", ".json")]:
                page.locator("#exportChoice").select_option(fmt)
                with page.expect_download(timeout=30000) as info:
                    page.locator("#exportMain").click()
                download = info.value
                assert download.suggested_filename.endswith(ext), download.suggested_filename
                target = pathlib.Path(tmp) / download.suggested_filename
                download.save_as(target)
                assert target.stat().st_size > 20
                if fmt == "py":
                    compile(target.read_text(encoding="utf-8"), str(target), "exec")
                if fmt == "png":
                    assert target.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
                if fmt == "html":
                    exported = browser.new_page()
                    exported.goto(target.as_uri())
                    exported.wait_for_function("document.querySelector('canvas').width > 0")
                    exported.close()
                page.locator("#exportMain").wait_for(state="visible")
                page.wait_for_function("!document.querySelector('#exportMain').disabled")
            page.set_viewport_size({"width": 390, "height": 844})
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth + 1"), "Mobile horizontal overflow"
            assert not errors, errors
            browser.close()
        print("Frame Studio browser smoke test passed.")
    finally:
        server.shutdown()

if __name__ == "__main__":
    main()
