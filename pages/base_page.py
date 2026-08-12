# =========================================================
#  pages/base_page.py
#  Shared toolbox every Page Object inherits from.
# =========================================================

from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def go_to(self, path):
        """Navigate to a URL path, e.g. self.go_to('/login')"""
        self.page.goto(path)

    def click(self, locator):
        """Click any element. Playwright automatically waits for it
        to be ready before clicking - no manual wait needed here."""
        locator.click()

    def type_text(self, locator, text):
        """Type text into an input field. Also auto-waits."""
        locator.fill(text)

    def expect_visible(self, locator, timeout=10000):
        """
        Use this in tests to CONFIRM something is visible.

        Unlike a plain "is it visible right now?" check, this WAITS
        (up to `timeout` milliseconds) and keeps retrying until the
        element shows up, or fails with a clear error if it never
        does. Real web apps take a moment to render after a page
        loads - this is the reliable way to check for that.
        """
        expect(locator).to_be_visible(timeout=timeout)

    def is_visible(self, locator) -> bool:
        """
        Instant check - True/False right now, no waiting.
        Useful for simple yes/no logic, but for test assertions
        prefer expect_visible() above (it waits, this doesn't).
        """
        return locator.is_visible()

    def get_text(self, locator) -> str:
        """Read the displayed text inside an element (e.g. a heading)."""
        return locator.inner_text()

    def get_input_value(self, locator) -> str:
        """Read what's currently typed into an <input> or <textarea>.
        (get_text() won't work for inputs - use this instead.)"""
        return locator.input_value()

    def pause(self, milliseconds=2000):
        """
        Freeze the browser for a moment so YOU can actually see the
        result of the last action, before the test moves on (or the
        browser tab closes). slow_mo only pauses BEFORE actions -
        this is what lets you see AFTER an action too.
        """
        self.page.wait_for_timeout(milliseconds)
