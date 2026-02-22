from .base_page import BasePage
from .locators import LoginPageLocators
from .catalog_page import CatalogPage


class LoginPage(BasePage):
    def open_login_page(self):
        url = "https://intern.demoshopping.ru/login"
        self.open(url)

    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.find_element(LoginPageLocators.LOGIN_FORM), "Can't find login form"

    def should_be_register_form(self):
        assert self.find_element(
            LoginPageLocators.REGISTER_FORM
        ), "Can't find register form"

    def register_new_user(self, random_login, random_password):
        self.find_element(LoginPageLocators.REGISTER_USERNAME).send_keys(random_login)
        self.find_element(LoginPageLocators.REGISTER_PASSWORD).send_keys(
            random_password
        )
        self.find_element(LoginPageLocators.REGISTER_BUTTON).click()

    def login(self, login: str, password: str):
        self.find_element(LoginPageLocators.LOGIN_USERNAME).send_keys(login)
        self.find_element(LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
        return CatalogPage(self.driver)
