# =========================================================
#  pages/login_page.py
#
#  This represents the LOGIN screen you shared:
#    - "Email" field
#    - "Password" field
#    - "Log In" button
#    - "Forgot your password?" link
#
#  NOTE ON LOCATORS:
#  I built the selectors below from what's visible on screen
#  (labels, button text). This is the beginner-friendly and
#  recommended way to write Playwright locators. If any of
#  them don't match once you run it, the easiest fix is:
#     1. Run:  playwright codegen https://erp.naseni.xyz/login
#     2. Click the field/button in the window that opens
#     3. Copy the exact locator Playwright shows you
#     4. Paste it in below, replacing that line
# =========================================================

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        # --- Elements on the Login screen ---
        self.email_input = page.get_by_label("Email")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Log In")
        self.forgot_password_link = page.get_by_text("Forgot your password?")
        self.welcome_heading = page.get_by_text("Welcome Back")

    # --- Actions you can do on this screen ---

    def open(self):
        """Go to the login page"""
        self.go_to("/login")
        return self

    def login(self, email, password):
        """Fill in email + password and click Log In"""
        self.type_text(self.email_input, email)
        self.type_text(self.password_input, password)
        self.click(self.login_button)
        return self
    
