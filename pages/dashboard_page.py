from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__quick_launch_locator = "xpath=//p[text()='Quick Launch']"

    def get_quick_launch_locator(self):
        return self.__page.locator(self.__quick_launch_locator)
