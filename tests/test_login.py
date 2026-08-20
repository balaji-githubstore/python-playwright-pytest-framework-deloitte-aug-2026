from playwright.sync_api import Page, expect
import pytest
from utilities.data_source import DataSource


class TestLogin:

    @pytest.mark.parametrize("username, password, expected_error", DataSource.data_invalid_login_csv)
    def test_invalid_login(self, page: Page, username, password, expected_error):
        page.locator("xpath=//input[@name='username']").fill(username)
        page.locator("xpath=//input[@name='password']").fill(password)
        page.locator("xpath=//button[normalize-space()='Login']").click()
        expect(page.locator(
            "xpath=//p[contains(normalize-space(),'Invalid')]")).to_have_text(expected_error)

    @pytest.mark.parametrize("username,password,expected_text", DataSource.data_valid_login)
    def test_valid_login(self, page: Page,username,password,expected_text):
        page.locator("xpath=//input[@name='username']").fill(username)
        page.locator("xpath=//input[@name='password']").fill(password)
        page.locator("xpath=//button[normalize-space()='Login']").click()
        expect(page.locator(
            "xpath=//p[text()='Quick Launch']")).to_have_text(expected_text)
