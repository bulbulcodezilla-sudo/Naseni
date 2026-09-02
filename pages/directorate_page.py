# =========================================================
#  pages/directorate_page.py
#
#  Represents the "Directorate" screen (left sidebar > Directorate),
#  where new Directorates are created.
#
#  IMPORTANT: I don't have a screenshot of this specific screen
#  (the doc you shared only covered File Manager), so every
#  selector below is a best-guess placeholder. Before running
#  test_directorate_creation.py, confirm these using:
#      playwright codegen https://erp.naseni.xyz
#  Click Directorate > whatever "Add/Create" button exists, type
#  a name, and copy the exact locators it shows you into here.
# =========================================================

from pages.base_page import BasePage


class DirectoratePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.directorate_menu_item = page.get_by_text("Directorate", exact=True)

        # TODO: confirm against the real "Add Directorate" form
        self.add_button = page.get_by_role("button", name="Add")
        self.name_input = page.get_by_placeholder("Enter Name")
        self.description_input = page.get_by_placeholder("Enter description")
        self.save_button = page.get_by_role("button", name="Submit")

    def open(self):
        """Go to the Directorate screen from the left sidebar"""
        self.click(self.directorate_menu_item)
        return self

    def create_directorate(self, name):
        self.click(self.add_button)
        self.type_text(self.name_input, name)
        self.type_text(self.description_input, "Created by automated test")
        self.click(self.save_button)
        return self
