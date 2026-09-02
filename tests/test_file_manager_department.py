# =========================================================
#  tests/test_file_manager_department.py
#
#  Drills one level deeper than the Directorate: Directorate ->
#  Department, then uploads a file there. Confirms uploads work
#  at the Department level too, not just the top Directorate.
# =========================================================

from pages.file_manager_page import FileManagerPage
from utils.test_data import random_title, random_file_number, random_keyword


FILE_STATUS = "Active"          # TODO: confirm real option text
CLASSIFICATION = "Public"       # TODO: confirm real option text


def test_upload_file_inside_department_folder(logged_in_page, config):
    file_manager = FileManagerPage(logged_in_page)
    file_manager.open()
    file_manager.open_folder(config["own_directorate"])
    file_manager.open_folder(config["own_department"])

    

    title = random_title()

    file_manager.upload_file(
        file_path=config["sample_file_path"],
        document_type="File",
        title=title,
        file_number=random_file_number(),
        status=FILE_STATUS,
        classification=CLASSIFICATION,
        keyword=random_keyword(),
    )

    file_manager.expect_file_visible(title)
    file_manager.pause()
