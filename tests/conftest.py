from playwright.sync_api import sync_playwright, expect
import pytest
import datetime
import os


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/")
    # page.set_default_timeout(50000)
    expect.set_options(30000)
    yield page
    page.close()
