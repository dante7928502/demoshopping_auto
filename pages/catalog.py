from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import CatalogPageLocators  # импортируем локаторы

class CatalogPage(BasePage):
    def search_product(self, product_name):
        self.send_keys(CatalogPageLocators.SEARCH_INPUT, product_name)
        self.click(CatalogPageLocators.SEARCH_BUTTON)

    def get_products_count(self):
        return len(self.driver.find_elements(*CatalogPageLocators.PRODUCT_CARDS))

    def add_product_to_cart(self, index=0):
        products = self.driver.find_elements(*CatalogPageLocators.PRODUCT_CARDS)
        products[index].find_element(*CatalogPageLocators.ADD_TO_CART_BUTTON).click()

    def go_to_cart(self):
        self.click(CatalogPageLocators.CART_LINK)