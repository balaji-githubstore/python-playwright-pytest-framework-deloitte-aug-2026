from playwright.sync_api import sync_playwright, expect


class TestLoginUI:
    def test_title(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://opensource-demo.orangehrmlive.com/")
            expect(page).to_have_title("OrangeHRM")

    def test_header(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome", headless=False)
            context = browser.new_context()
            page = context.new_page()

            page.goto("https://opensource-demo.orangehrmlive.com/")

            # Assert the Login Header //h5[text()='Login']  
            # 
            expect(page.locator("xpath=//h5[text()='Login']")).to_have_text("Login")
            expect(page.locator("xpath=//div[@class='orangehrm-login-slot']/h5")).to_have_text("Login")

            assert  page.locator("xpath=//h5[text()='Login']").is_visible()
         

