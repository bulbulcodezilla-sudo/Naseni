# =========================================================
#  tests/test_dashboard.py
#
#  All 4 tests below share ONE login (see the "logged_in_page"
#  fixture in conftest.py) - they don't log in individually.
# =========================================================

from pages.dashboard_page import DashboardPage


def test_dashboard_loads_after_login(logged_in_page):
    dashboard_page = DashboardPage(logged_in_page)
    dashboard_page.expect_visible(dashboard_page.department_heading)

    dashboard_page.pause()  # hold here so you can see the dashboard


def test_status_cards_are_visible(logged_in_page):
    dashboard_page = DashboardPage(logged_in_page)

    dashboard_page.expect_visible(dashboard_page.pending_card)
    dashboard_page.expect_visible(dashboard_page.under_query_card)
    dashboard_page.expect_visible(dashboard_page.query_resolved_card)
    dashboard_page.expect_visible(dashboard_page.approved_card)
    dashboard_page.expect_visible(dashboard_page.rejected_card)

    dashboard_page.pause()  # hold here so you can see the status cards


def test_can_search_for_a_file(logged_in_page):
    dashboard_page = DashboardPage(logged_in_page)

    dashboard_page.search_file("test")
    dashboard_page.pause()  # hold here so you can see the typed search text

    # Note: get_input_value(), not get_text() - inputs store their
    # typed value differently from how headings/labels store text.
    assert dashboard_page.get_input_value(dashboard_page.search_input) == "test"


    


def test_can_switch_to_received_tab(logged_in_page):
    dashboard_page = DashboardPage(logged_in_page)

    dashboard_page.open_tab(dashboard_page.received_tab)
    dashboard_page.expect_visible(dashboard_page.received_tab)

    dashboard_page.pause()  # hold here so you can see the Received tab open

def test_open_search_keyword_result(logged_in_page):
    dashboard_page = DashboardPage(logged_in_page)
    dashboard_page.pause()  # hold here so you can see the dashboard

    dashboard_page.search_file("test")
    dashboard_page.open_search_result("test")
