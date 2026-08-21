from playwright.sync_api import expect, Page


class TestInfoUI:

    # add the fixture that should be used(page) from conftest.py
    def test_title(self, page: Page, logger):
        logger.info("Validating login page title ")
        expect(page).to_have_title("OrangeHRM")
