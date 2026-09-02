# =========================================================
#  pages/file_manager_page.py
#
#  Represents the File Manager screen. Built from the Naseni
#  "Module: File Manager" doc, which shows the actual Upload
#  modal fields: Document Type, Title, File Number, File Status,
#  Keyword, Classification.
#
#  Real folder structure: Directorate -> Department -> Unit -> Files
#  (e.g. "EVC/CEOs office" is a Directorate). Use open_folder() as
#  many times as needed to drill down a level - it works the same
#  way at every level, so the same method handles all three.
#
#  NOTE: A couple of things weren't fully visible in the doc's
#  screenshots (the exact "attach file" step before the metadata
#  form, and the real option text inside File Status/Classification
#  dropdowns). Those are marked TODO below - use:
#      playwright codegen https://erp.naseni.xyz
#  to confirm and fix them quickly if a test fails on them.
# =========================================================

import re

from pages.base_page import BasePage

class FileManagerPage(BasePage):

    # The 5 document types shown in the real Upload modal
    DOCUMENT_TYPES = ["File", "Memo", "Mail", "Contract", "Other"]

    def __init__(self, page):
        super().__init__(page)

        # --- Sidebar / top-level ---
        self.file_manager_menu_item = page.get_by_text("File Manager", exact=True)
        # self.upload_button = page.get_by_role("button", name=re.compile(r"upload", re.IGNORECASE)) using below code for upload button
        self.upload_button = page.get_by_role("button", name="Upload")
        self.file_input = page.locator("input[type='file']")
        self.next_button = page.get_by_role("button", name="Next")
        self.search_input = page.get_by_placeholder(re.compile(r"search", re.IGNORECASE))

        # --- Upload modal: metadata form (confirmed from screenshot) ---
        self.document_type_dropdown = page.get_by_text("Select Document Type")
        self.title_input = page.get_by_placeholder("Title")
        self.file_number_input = page.get_by_placeholder("File Number")
        self.file_status_dropdown = page.get_by_text("Select File Status")
        self.keyword_input = page.get_by_placeholder("Type a keyword and press enter")
        self.classification_dropdown = page.get_by_text("Select Classification")

        self.next_button = page.get_by_role("button", name="Next")
        self.create_button = page.get_by_role("button", name="Create")
        self.back_button = page.get_by_role("button", name="Back")
        self.close_button = page.get_by_role("button", name="Close")

    # ---------------------------------------------------
    # Navigation
    # ---------------------------------------------------

    def open(self):
        """Go to File Manager from the left sidebar"""
        self.click(self.file_manager_menu_item)
        return self

    def open_folder(self, folder_name):
        """
        Open a Directorate, Department, or Unit folder by its visible
        name - all three levels work the same way, so this one method
        handles all of them. Call it more than once to drill down:

            file_manager.open_folder("EVC/CEOs office") \\
                         .open_folder("Some Department") \\
                         .open_folder("Some Unit")

        WHY THIS LOOKS MORE COMPLICATED THAN A SIMPLE CLICK:
        Different folder levels in this app render differently -
        sometimes the folder name is a <button>, sometimes a plain
        link/card, and sometimes the SAME name appears twice on
        screen (e.g. a breadcrumb + the folder tile). A single fixed
        locator broke on one level or the other, so instead we try a
        few strategies in order and use the first one that uniquely
        matches exactly one element.
        """
        strategies = [
            self.page.get_by_role("button", name=folder_name, exact=True),
            self.page.get_by_role("link", name=folder_name, exact=True),
        ]

        for locator in strategies:
            try:
                locator.wait_for(state="visible", timeout=5000)
            except Exception:
                continue  # this strategy didn't find anything - try the next one

            if locator.count() == 1:
                self.click(locator)
                return self

        # Nothing matched exactly once above - fall back to plain text,
        # and just take the first match rather than erroring out.
        fallback = self.page.get_by_text(folder_name, exact=True).first
        self.click(fallback)
        return self

    # ---------------------------------------------------
    # Uploading a file - step by step
    # ---------------------------------------------------

    def click_upload(self):
        print("Clicked Upload button")             
        self.click(self.upload_button)
        
        return self


    # def attach_file(self, file_path):                                         tried below Attached_file
    #     """
    #     Attach a file. Tries the direct <input type="file"> element
    #     first (works even if it's hidden behind a styled button/drop
    #     zone). Falls back to clicking a visible "Choose File" button
    #     and catching the native file-picker dialog, for apps that
    #     don't expose a plain file input.
    #     """
    #     choose_file_text = re.compile(r"choose\s*file", re.IGNORECASE)
    #     choose_file_controls = [
    #         self.page.get_by_role("button", name=choose_file_text),
    #         self.page.locator("label").filter(has_text=choose_file_text),
    #         self.page.get_by_text(choose_file_text),
    #     ]

    #     for control in choose_file_controls:
    #         if control.count() == 0 or not control.first.is_visible():
    #             continue

    #         try:
    #             with self.page.expect_file_chooser(timeout=5000) as file_chooser_info:
    #                 control.first.click()
    #             file_chooser_info.value.set_files(file_path)
    #             return self
    #         except Exception:
    #             continue

        # try:
        #     self.file_input.first.wait_for(state="attached", timeout=5000)
        # except Exception as error:
        #     raise AssertionError(
        #         "Could not attach the file: no working Choose File control or "       tried with below code for upload file 1
        #         "input[type='file'] was found in the upload popup."                    
        #     ) from error

        # self.file_input.first.set_input_files(file_path)
        # return self

        # try:
        #     self.file_input.first.set_input_files(file_path, timeout=10000)  tried with below code for upload file 2
        # except Exception as error:
        #  raise AssertionError(
        #   f"Could not upload file: {file_path}"
        #  ) from error

        # return self
        
        # try:
        #    print("File path:", file_path)
        #    print("File input count:", self.file_input.count()) tried below simple method for upload file 3

        #    self.file_input.first.set_input_files(
        #    file_path,
        #    timeout=10000
        #  )

        #    print("File successfully attached")

        # except Exception as error:
        #   print("ACTUAL PLAYWRIGHT ERROR:")
        #   print(error)
        #   raise
        # self.file_input.first.set_input_files(file_path, timeout=10000)


    # def attach_file(self, file_path):
    #         self.file_input.set_input_files(file_path)
    #         return self 
    #   
    # def attach_file(self, file_path):
    #     print("FILE PATH:", file_path)
    #     print("FILE INPUT COUNT:", self.file_input.count())

    #     self.file_input.first.set_input_files(file_path)

    #     return self

    # def attach_file(self, file_path):
    #     print("FILE PATH:", file_path)
    #     print("FILE INPUT COUNT:", self.file_input.count())

    #     print("VISIBLE:", self.file_input.first.is_visible())
    #     print("ENABLED:", self.file_input.first.is_enabled())

    #     self.file_input.first.set_input_files(file_path)

    #     return self

    def attach_file(self, file_path):
        with self.page.expect_file_chooser() as file_chooser_info:
         self.file_input.first.click()

        file_chooser = file_chooser_info.value
        file_chooser.set_files(file_path)

        return self



    def click_next(self):
        """
        Some upload flows keep the metadata form on the same screen after
        a file is attached, while others require an explicit "Next" step.
        Only click when that button is actually present.
        """
        if self.next_button.count() > 0 and self.next_button.first.is_visible():
            self.click(self.next_button.first)
        return self

    def select_document_type(self, document_type):
        """document_type must be one of FileManagerPage.DOCUMENT_TYPES"""
        self.click(self.document_type_dropdown)
        option = self.page.get_by_text(document_type, exact=True)
        self.click(option)
        return self

    def select_file_status(self, status_text):
        """TODO: confirm real status option text (e.g. 'Active', 'Draft')"""
        self.click(self.file_status_dropdown)
        option = self.page.get_by_text(status_text, exact=True)
        self.click(option)
        return self

    def select_classification(self, classification_text):
        """TODO: confirm real classification option text (e.g. 'Public', 'Confidential')"""
        self.click(self.classification_dropdown)
        option = self.page.get_by_text(classification_text, exact=True)
        self.click(option)
        return self

    def fill_title(self, title):
        self.type_text(self.title_input, title)
        return self

    def fill_file_number(self, file_number):
        self.type_text(self.file_number_input, file_number)
        return self

    def add_keyword(self, keyword):
        """Types a keyword and presses Enter (this is a tag-style input)"""
        self.type_text(self.keyword_input, keyword)
        self.keyword_input.press("Enter")
        return self

    def submit_upload(self):
        self.click(self.create_button)
        return self

    def upload_file(self, file_path, document_type, title, file_number,
                     status, classification, keyword):
        """
        Full upload flow in ONE call - this is what most tests use.
        Runs: Upload -> attach file -> Next -> fill metadata -> Create
        """
        self.click_upload()
        self.attach_file(file_path)
        self.click_next()

        self.select_document_type(document_type)
        self.fill_title(title)
        self.fill_file_number(file_number)
        self.select_file_status(status)
        self.add_keyword(keyword)
        self.select_classification(classification)

        self.submit_upload()
        return self

    # ---------------------------------------------------
    # Verifying an upload
    # ---------------------------------------------------

    def search_file(self, title):
        self.type_text(self.search_input, title)
        return self

    def expect_file_visible(self, title, timeout=15000):
        """
        Confirms a file shows up in the list.
        Uses a longer timeout (15s) because real uploads on this
        app take roughly 7-9 seconds to finish processing.
        """
        file_card = self.page.get_by_text(title, exact=True)
        self.expect_visible(file_card, timeout=timeout)
