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
            # //div[@class='orangehrm-login-slot']/h5
            actual_header=page.locator("xpath=//h5[text()='Login'] ").inner_text()
            assert  actual_header=="Login"