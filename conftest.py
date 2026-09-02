# =========================================================
#  conftest.py
#  Fixtures - reusable setup code pytest hands to your tests.
# =========================================================

import pytest
from playwright.sync_api import sync_playwright

from utils.config_reader import get_config
from pages.login_page import LoginPage


# ---------------------------------------------------------
# 1) Load settings from config.yaml (once per test run)
# ---------------------------------------------------------
@pytest.fixture(scope="session")
def config():
    return get_config()


# ---------------------------------------------------------
# 2) Start Playwright itself (once per test run)
# ---------------------------------------------------------
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


# ---------------------------------------------------------
# 3) Open ONE browser for the whole test run.
#    - "slow_mo" (config.yaml) pauses BEFORE every click/type.
#    - The two --window-* args below force a large window even
#      when --start-maximized doesn't work (common on Windows).
# ---------------------------------------------------------
@pytest.fixture(scope="session")
def browser(playwright_instance, config):
    browser = playwright_instance.chromium.launch(
        headless=config["headless"],
        slow_mo=config.get("slow_mo", 0),
        args=[
            "--start-maximized",
            "--window-position=0,0",
            "--window-size=1920,1080",
        ],
    )
    yield browser
    browser.close()


# ---------------------------------------------------------
# 4) A fresh, NOT-logged-in browser tab for each test.
#    viewport=None lets the page use the real window size above,
#    instead of Playwright's default fixed 1280x720 box.
# ---------------------------------------------------------
@pytest.fixture
def page(browser, config):
    context = browser.new_context(base_url=config["base_url"], viewport=None)
    page = context.new_page()

    yield page

    context.close()


# ---------------------------------------------------------
# 5) An ALREADY-logged-in browser tab, shared across every
#    test in one test file ("module" scope) - so we only log
#    in ONCE per file instead of once per test.
# ---------------------------------------------------------
@pytest.fixture
def logged_in_page(browser, config):
    if not config.get("login_password") or config["login_password"] == "changeme":
        pytest.skip(
            "Login password is missing or still set to the demo value. "
            "Set the real password in the NASENI_PASSWORD environment variable "
            "before running login-based tests."
        )

    context = browser.new_context(base_url=config["base_url"], viewport=None)
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(config["login_email"], config["login_password"])
    page.wait_for_url("**/file-review**", timeout=15000)

    yield page

    context.close()
    