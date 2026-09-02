# =========================================================
#  tests/test_file_manager_upload.py
#
#  Uploads one file of EACH of the 5 real document types
#  (File, Memo, Mail, Contract, Other) directly into the user's
#  own Directorate (EVC/CEOs office), and confirms each shows
#  up afterward.
# =========================================================

import pytest
from pages.file_manager_page import FileManagerPage
from utils.test_data import random_title, random_file_number, random_keyword


# TODO: confirm these match the real dropdown option text in the app
FILE_STATUS = "Active"
CLASSIFICATION = "Public"


# @pytest.mark.parametrize runs this same test once per document type
# below, automatically - so this one function creates 5 separate test
# runs: one for "File", one for "Memo", one for "Mail", etc.
@pytest.mark.parametrize("document_type", FileManagerPage.DOCUMENT_TYPES)
def test_upload_each_file_type_in_own_directorate(logged_in_page, config, document_type):
    file_manager = FileManagerPage(logged_in_page)
    file_manager.open()
    file_manager.open_folder(config["own_directorate"])

    title = random_title()

    file_manager.upload_file(
        file_path=config["sample_file_path"],
        document_type=document_type,
        title=title,
        file_number=random_file_number(),
        status=FILE_STATUS,
        classification=CLASSIFICATION,
        keyword=random_keyword(),
    )

    # Real uploads take ~7-9 seconds to process - expect_file_visible
    # waits up to 15 seconds, retrying until it appears.
    file_manager.expect_file_visible(title)

    file_manager.pause()  # hold here so you can see the uploaded file
