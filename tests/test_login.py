from playwright.sync_api import expect, Page


class TestLogin:
    def test_invalid_login(self, page: Page):
        page.locator("xpath=//input[@name='username']").fill("john")
        page.locator("xpath=//input[@name='password']").fill("john123")
        page.locator("xpath=//button[normalize-space()='Login']").click()
        expect(page.locator(
            "xpath=//p[contains(normalize-space(),'Invalid')]")).to_have_text("Invalid credentials")

    def test_valid_login(self,page: Page):
        # valid login - Admin and admin123
        # assert - Quick Launch  text
