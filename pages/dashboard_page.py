# =========================================================
#  pages/dashboard_page.py
#
#  This represents the "My Desk" screen you land on after
#  logging in. It shows:
#    - A department heading (e.g. "Department: EVC/CEOs office")
#    - 5 status cards: Pending, Under Query, Query Resolved,
#      Approved, Rejected
#    - A search box
#    - Tabs: All, Sent Files, Received, Only Invited, KIV, Endorsements
#    - A table listing files
# =========================================================

from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        # --- Elements on the My Desk screen ---
        self.my_desk_menu_item = page.get_by_text("My Desk", exact=True)
        self.department_heading = page.get_by_text("Department:")

        # Status cards (top of the page)
        self.pending_card = page.get_by_text("Pending", exact=True)
        self.under_query_card = page.get_by_text("Under Query", exact=True)
        self.query_resolved_card = page.get_by_text("Query Resolved", exact=True)
        self.approved_card = page.get_by_text("Approved", exact=True)
        self.rejected_card = page.get_by_text("Rejected", exact=True)

        # Search box + tabs above the file table
        self.search_input = page.get_by_placeholder("Search with File number and File title")
        self.all_tab = page.get_by_text("All", exact=True)
        self.sent_files_tab = page.get_by_text("Sent Files", exact=True)
        self.received_tab = page.get_by_text("Received", exact=True)
        self.only_invited_tab = page.get_by_text("Only Invited", exact=True)
        self.kiv_tab = page.get_by_text("KIV", exact=True)
        self.endorsements_tab = page.get_by_text("Endorsements", exact=True)

    # --- Actions you can do on this screen ---

    def search_file(self, keyword):
        """Type into the search box (file number / title)"""
        self.type_text(self.search_input, keyword)
        return self

    def open_tab(self, tab_locator):
        """Click one of the tabs, e.g. dashboard.open_tab(dashboard.received_tab)"""
        self.click(tab_locator)
        return self
