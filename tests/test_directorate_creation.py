# =========================================================
#  tests/test_directorate_creation.py
#
#  Creates a new Directorate from the left-panel "Directorate"
#  tab, then confirms it shows up as a folder in File Manager.
#
#  NOTE: pages/directorate_page.py has placeholder selectors -
#  see the TODO comments there before trusting this test.
# =========================================================

from pages.directorate_page import DirectoratePage
from pages.file_manager_page import FileManagerPage
from utils.test_data import random_directorate_name


def test_create_new_directorate_and_see_it_in_file_manager(logged_in_page):
    new_name = random_directorate_name()

    directorate_page = DirectoratePage(logged_in_page)
    directorate_page.open()
    directorate_page.create_directorate(new_name)
    directorate_page.pause()  # hold here so you can see it get created

    file_manager = FileManagerPage(logged_in_page)
    file_manager.open()
    file_manager.expect_file_visible(new_name)

    file_manager.pause()  # hold here so you can see it listed as a folder
