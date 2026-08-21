from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.__page = page
        self.__username_locator = "xpath=//input[@name='username']"
        self.__password_locator = "xpath=//input[@name='password']"
        self.__login_locator = "xpath=//button[normalize-space()='Login']"
        self.__error_locator = "xpath=//p[contains(normalize-space(),'Invalid')]"

    def enter_username(self, username: str):
        self.__page.locator(self.__username_locator).fill(username)

    def enter_password(self, password: str):
        self.__page.locator(self.__password_locator).fill(password)

    def click_login(self):
        self.__page.locator(self.__login_locator).click()

    def get_username_placeholder(self):
        return self.__page.locator(self.__username_locator).get_attribute("placeholder")

    def get_invalid_login_error_locator(self):
        return self.__page.locator(self.__error_locator)
