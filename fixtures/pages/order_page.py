from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage


class OrderPage(BasePage):
    BUTTON_SING_IN = (By.XPATH, "//*[contains(text(),'sign in')]")
    USERNAME_LOGIN = (By.NAME, "username")
    PASSWORD_LOGIN = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='log in']")
    BUTTON = (By.CLASS_NAME, "btn-danger")
    CARD = (By.CLASS_NAME, "card")
    DESCRIPTION = (By.CLASS_NAME, "ml-3")
    PROFILE_BUTTON = (By.CLASS_NAME, "dropdown-toggle")
    BASKET_BUTTON_DROPDOWN = (By.XPATH, "//*[contains(text(),'basket')]")
    TEXT_HEAD_BASKET = (By.CLASS_NAME, "head")
    BUTTON_TO_THE_DESIGN = (By.CLASS_NAME, "btn-outline-success")
    TEXT_CUSTOMER_ORDER_CREATE = (By.CLASS_NAME, "h4")
    BUTTON_SAVE = (By.XPATH, "//button[@type='submit']")
    TEXT_ORDER = (By.CLASS_NAME, "head")
    LOOK_ORDER = (By.XPATH, "//*[@class='table orders_list']//a[1]")
    CUSTOMER = (By.XPATH, "//*[contains(text(),'customer')]")

    def open_login_page(self):
        """
        Open login page.
        """
        self.open_page(self.app.url)

        self.click_element(locator=self.BUTTON_SING_IN)

    def login(self, username, password):
        """
        Data entry in fields.
        """
        self.clear(locator=self.USERNAME_LOGIN)
        self.fill(locator=self.USERNAME_LOGIN, value=username)
        self.clear(locator=self.PASSWORD_LOGIN)
        self.fill(locator=self.PASSWORD_LOGIN, value=password)
        self.click_element(locator=self.LOGIN_BUTTON)

    def button_click(self):
        """
        Click other button.
        """
        self.click_element(locator=self.BUTTON)

    def card_on_list_of_accommodation(self) -> str:
        """
        Hotel card on list of accommodation.
        """
        element = self.text(locator=self.CARD)
        return element

    def description_accommodation_details(self) -> str:
        """
        Description on page accommodation details .
        """
        element = self.text(locator=self.DESCRIPTION)
        return element

    def enter_on_basket_page(self):
        """
        Open profile menu.
        """
        self.click_element(locator=self.PROFILE_BUTTON)
        self.click_element(locator=self.BASKET_BUTTON_DROPDOWN)

    def text_on_basket_header(self):
        """
        Text on basket header.
        """
        element = self.text(locator=self.TEXT_HEAD_BASKET)
        return element

    def click_button_to_the_design(self):
        """
        Click on button to the design.
        """
        self.click_element(locator=self.BUTTON_TO_THE_DESIGN)

    def text_on_order_create(self):
        """
        Name customer on order create page.
        """
        element = self.text(locator=self.TEXT_CUSTOMER_ORDER_CREATE)
        return element

    def click_button_order_save(self):
        """
        Order save
        """
        self.click_element(locator=self.BUTTON_SAVE)

    def text_on_order(self):
        """
        Text on order page.
        """
        element = self.text(locator=self.TEXT_ORDER)
        return element

    def click_button_look_order(self):
        """
        Click button look.
        """
        self.click_element(locator=self.LOOK_ORDER)

    def customer_order(self):
        """
        Name customer.
        """
        element = self.text(locator=self.CUSTOMER)
        return element
