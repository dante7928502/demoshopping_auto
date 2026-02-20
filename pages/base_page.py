from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BasePageLocators

class BasePage:
    def __init__(self, driver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

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

    def open(self, url):
        self.driver.get(url)
