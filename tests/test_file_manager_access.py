# =========================================================
#  tests/test_file_manager_access.py
#
#  Negative test: this user belongs to the "EVC/CEOs office"
#  Directorate only. Confirms they can't upload into a
#  DIFFERENT Directorate - either the folder isn't reachable,
#  or the Upload button is missing/disabled once inside it.
# =========================================================

from playwright.sync_api import expect
from pages.file_manager_page import FileManagerPage


def test_cannot_upload_to_a_different_directorate(logged_in_page, config):
    file_manager = FileManagerPage(logged_in_page)
    file_manager.open()
    file_manager.open_folder(config["other_directorate"])

    # We expect Upload to be either hidden or disabled here, since this
    # Directorate isn't the logged-in user's own.
    expect(file_manager.upload_button).not_to_be_visible()

    file_manager.pause()  # hold here so you can see the restricted view
