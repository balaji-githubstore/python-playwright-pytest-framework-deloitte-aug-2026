from playwright.sync_api import expect, Page
import pytest


class TestLogin:

    @pytest.mark.parametrize("username, password, expected_error", [
        ["saul", "saul123", "Invalid credentials"],
        ["kim", "kim123", "Invalid credentials"]
    ])
    def test_invalid_login(self, page: Page, username, password, expected_error):
        page.locator("xpath=//input[@name='username']").fill(username)
        page.locator("xpath=//input[@name='password']").fill(password)
        page.locator("xpath=//button[normalize-space()='Login']").click()
        expect(page.locator(
            "xpath=//p[contains(normalize-space(),'Invalid')]")).to_have_text(expected_error)

    def test_valid_login(self, page: Page):
        page.locator("xpath=//input[@name='username']").fill("Admin")
        page.locator("xpath=//input[@name='password']").fill("admin123")
        page.locator("xpath=//button[normalize-space()='Login']").click()
        expect(page.locator(
            "xpath=//p[text()='Quick Launch']")).to_have_text("Quick Launch")
