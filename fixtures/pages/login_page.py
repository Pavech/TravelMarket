from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage


class LoginPage(BasePage):
    BUTTON_SING_IN = (By.XPATH, "//*[contains(text(),'sign in')]")
    USERNAME_LOGIN = (By.NAME, "username")
    PASSWORD_LOGIN = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='log in']")
    ERROR_TEXT = (By.XPATH, "//ul[@class='errorlist nonfield']/li")
    DROPDOWN_TOGGLE_USERNAME = (By.CLASS_NAME, "dropdown-toggle")
    TEXT_LOG_IN = (By.CLASS_NAME, "head")

    def open_login_page(self):
        """
        Open login page.
        """
        self.open_page(self.app.url)
        self.click_element(locator=self.BUTTON_SING_IN)

    def entry_data(self, username, password):
        """
        Upload image on reg page.
        """
        self.clear(locator=self.USERNAME_LOGIN)
        self.fill(locator=self.USERNAME_LOGIN, value=username)
        self.clear(locator=self.PASSWORD_LOGIN)
        self.fill(locator=self.PASSWORD_LOGIN, value=password)
        self.click_element(locator=self.LOGIN_BUTTON)

    def dropdown_toggle_main_page(self) -> str:
        """
        Dropdown-toggle on Main page.
        """
        element = self.text(locator=self.DROPDOWN_TOGGLE_USERNAME)
        return element

    def text_error_login_page(self) -> str:
        """
        Errors on login page.
        """
        element = self.text(locator=self.ERROR_TEXT)
        return element

    def log_in(self) -> str:
        """
        Text "Log in" on "sign in" page.
        """
        element = self.text(locator=self.TEXT_LOG_IN)
        return element
