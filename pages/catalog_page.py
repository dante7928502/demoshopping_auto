from .base_page import BasePage
from .locators import CatalogPageLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement  # Импорт типа


class CatalogPage(BasePage):
    def get_names_of_all_products_on_page(self):
        elements = self.find_elements(CatalogPageLocators.PRODUCTS_LIST)
        return [el.text for el in elements]

    def add_product_to_cart(self, index=0):
        # Указываем тип через двоеточие
        products: list[WebElement] = self.find_elements(
            *CatalogPageLocators.PRODUCTS_LIST
        )

        # Чтобы метод не был серым
        products[index].find_element(*CatalogPageLocators.ADD_TO_CART_BUTTON).click()

    def set_min_price(self, price=0):
        self.find_element(CatalogPageLocators.MIN_PRICE_FIELD).send_keys(price)

    def set_max_price(self, price=0):
        self.find_element(CatalogPageLocators.MAX_PRICE_FIELD).send_keys(price)

    def set_product_category(self, category="Все категории"):
        # Находим сам элемент выпадающего списка
        dropdown = self.find_element(CatalogPageLocators.FILTER_CATEGORIES_DROPDOWN)

        # Оборачиваем его в класс Select
        select = Select(dropdown)

        # Выбираем по видимому тексту
        select.select_by_visible_text(category)

    def set_product_manufacturer(self, manufacturer="Все производители"):
        dropdown = self.find_element(CatalogPageLocators.FILTER_MANUFACTURERS_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(manufacturer)

    def set_free_shipping(self):
        self.find_element(CatalogPageLocators.FREE_SHIPMENT_CHECKBOX).click()

    def apply_filters(self):
        self.find_element(CatalogPageLocators.APPLY_FILTERS_BUTTON).click()

    def reset_filters(self):
        self.find_element(CatalogPageLocators.RESET_FILTERS_BUTTON).click()

    def set_sort(self, sort_type="От A до Z"):
        dropdown = self.find_element(CatalogPageLocators.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_visible_text(sort_type)
