# =========================================================
#  tests/test_file_manager_unit.py
#
#  Drills two levels deep: Directorate -> Department -> Unit,
#  then uploads a file there. Confirms uploads work at the
#  deepest folder level too.
# =========================================================

from pages.file_manager_page import FileManagerPage
from utils.test_data import random_title, random_file_number, random_keyword


FILE_STATUS = "Active"          # TODO: confirm real option text
CLASSIFICATION = "Public"       # TODO: confirm real option text


def test_upload_file_inside_unit_folder(logged_in_page, config):
    file_manager = FileManagerPage(logged_in_page)
    file_manager.open()
    file_manager.open_folder(config["own_directorate"])
    file_manager.open_folder(config["own_department"])
    file_manager.open_folder(config["own_unit"])

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
