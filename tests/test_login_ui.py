from playwright.sync_api import sync_playwright, expect
import pytest


class TestLoginUI:

    @pytest.fixture(scope="function",autouse=True)
    def setup(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=False)
            context = browser.new_context()
            self.page = context.new_page()
            self.page.goto("https://opensource-demo.orangehrmlive.com/")
            yield
            browser.close()

    def test_title(self):
        expect(self.page).to_have_title("OrangeHRM")

    def test_header(self):
        expect(self.page.locator("xpath=//h5[text()='Login']")).to_have_text("Login")
