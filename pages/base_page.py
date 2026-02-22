from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BasePageLocators


class BasePage:
    def __init__(self, driver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
        
    def get_products_count_in_cart(self) -> int:
        try:
            element_text = self.find_element(BasePageLocators.CART_COUNT).text
            # Оставляем только цифры
            digits = "".join(filter(str.isdigit, element_text))
            return int(digits) if digits else 0
        except Exception:
            return 0

    def open(self, url):
        self.driver.get(url)

    def go_to_catalog(self):
        self.click(BasePageLocators.CATALOG_LINK)

    def go_to_about_us(self):
        self.click(BasePageLocators.ABOUT_US_LINK)

    def go_to_contacts(self):
        self.click(BasePageLocators.CONTACTS_LINK)

    def go_to_cart(self):
        self.click(BasePageLocators.CART_LINK)

    def go_to_payment_page(self):
        self.click(BasePageLocators.PAYMENT_LINK)

    def go_to_orders_history(self):
        self.click(BasePageLocators.ORDERS_HISTORY_LINK)

    def go_to_login_page(self):
        self.click(BasePageLocators.LOGIN_PAGE_LINK)

    def logout(self):
        self.click(BasePageLocators.LOGOUT_BUTTON)

    def go_to_policy(self):
        self.click(BasePageLocators.POLICY_LINK)
