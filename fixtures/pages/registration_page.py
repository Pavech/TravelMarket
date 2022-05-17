from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from models.registration import RegisterUserModel


class RegistrationPage(BasePage):
    BUTTON_SING_IN = (By.XPATH, "//*[contains(text(),'sign in')]")
    BUTTON_REGISTER = (By.XPATH, "//*[contains(text(),'register')]")
    USERNAME = (By.NAME, "username")
    FIRST_NAME = (By.NAME, "first_name")
    PASSWORD_1 = (By.NAME, "password1")
    PASSWORD_2 = (By.NAME, "password2")
    EMAIL = (By.NAME, "email")
    AGE = (By.NAME, "age")
    BUTTON_REGISTER_REGPAGE = (By.XPATH, "//input[@value='register']")
    TEXT_IN_LOG_IN_PAGE = (By.CLASS_NAME, "head")
    ERROR_TEXT = (By.XPATH, "//ul[@class='errorlist']/li")
    USERNAME_LOGIN = (By.NAME, "username")
    PASSWORD_LOGIN = (By.NAME, "password")
    BUTTON_LOGIN_LOGIN_PAGE = (By.XPATH, "//input[@class='form-control'][@type='submit']")

    def open_registration_page(self):
        """
        Open registration page.
        """
        self.open_page(self.app.url)
        self.click_element(locator=self.BUTTON_SING_IN)
        self.click_element(locator=self.BUTTON_REGISTER)

    def entry_data_registration(self, data: RegisterUserModel):
        """
        Data entry in fields.
        """
        self.clear(locator=self.USERNAME)
        self.fill(locator=self.USERNAME, value=data.username)
        self.clear(locator=self.FIRST_NAME)
        self.fill(locator=self.FIRST_NAME, value=data.firstname)
        self.clear(locator=self.PASSWORD_1)
        self.fill(locator=self.PASSWORD_1, value=data.password_1)
        self.clear(locator=self.PASSWORD_2)
        self.fill(locator=self.PASSWORD_2, value=data.password_2)
        self.clear(locator=self.EMAIL)
        self.fill(locator=self.EMAIL, value=data.email)
        self.click_element(locator=self.BUTTON_REGISTER_REGPAGE)

    def text_log_in(self) -> str:
        """
        Text "Log in" on "sign in" page.
        """
        element = self.text(locator=self.TEXT_IN_LOG_IN_PAGE)
        return element

    def text_error(self) -> str:
        """
        Text "Error" on "sign in" page.
        """
        element = self.text(locator=self.ERROR_TEXT)
        return element

    def clear_and_fill(self, data):
        """
        Element "Age" on reg page.
        """
        self.clear(locator=self.AGE)
        self.fill(locator=self.AGE, value=data)

