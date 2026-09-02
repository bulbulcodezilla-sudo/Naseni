# =========================================================
#  tests/test_login.py
# =========================================================

from pages.login_page import LoginPage


def test_login_page_displays_correctly(page):
    """Does the login page show its main elements?

    Note: we use expect_visible() here, not is_visible(). The page
    takes a moment to render after open() - expect_visible() WAITS
    for that, is_visible() would check too early and wrongly fail.
    """
    login_page = LoginPage(page)
    login_page.open()

    login_page.expect_visible(login_page.welcome_heading)
    login_page.expect_visible(login_page.email_input)
    login_page.expect_visible(login_page.password_input)
    login_page.expect_visible(login_page.login_button)

    login_page.pause()  # hold here so you can see the loaded login page


def test_successful_login(page, config):
    """Log in with valid credentials and land on My Desk"""
    if not config.get("login_password") or config["login_password"] == "changeme":
        raise AssertionError(
            "Login password is missing or still set to the demo value. "
            "Set the real password in the NASENI_PASSWORD environment variable "
            "before running login-based tests."
        )

    login_page = LoginPage(page)
    login_page.open()
    login_page.login(config["login_email"], config["login_password"])

    page.wait_for_url("**/file-review**", timeout=15000)
    assert "/login" not in page.url

    login_page.pause()  # hold here so you can see the dashboard it landed on
