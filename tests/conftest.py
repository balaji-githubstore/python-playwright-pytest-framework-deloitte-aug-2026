from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.fixture(scope="function", autouse=True)
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/")
        yield page
        browser.close()
