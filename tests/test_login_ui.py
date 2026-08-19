from playwright.sync_api import expect, Page


class TestLoginUI:

    # add the fixture that should be used(page) from conftest.py
    def test_title(self, page: Page):
        expect(page).to_have_title("OrangeHRM")

    def test_header(self, page: Page):
        expect(page.locator(
            "xpath=//h5[text()='Login']")).to_have_text("Login")
