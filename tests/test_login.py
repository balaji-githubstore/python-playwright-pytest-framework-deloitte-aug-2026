from playwright.sync_api import Page, expect
import pytest
from utilities.data_source import DataSource
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLogin:

    @pytest.mark.parametrize("username, password, expected_error", DataSource.data_invalid_login_excel)
    def test_invalid_login(self, page: Page, username, password, expected_error):
        login = LoginPage(page)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()

        expect(login.get_invalid_login_error_locator()
               ).to_have_text(expected_error)

    @pytest.mark.parametrize("username,password,expected_text", DataSource.data_valid_login)
    def test_valid_login(self, page: Page, username, password, expected_text):
        login = LoginPage(page)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()

        dashboard = DashboardPage(page)
        expect(dashboard.get_quick_launch_locator()
               ).to_have_text(expected_text)
