from selenium.webdriver.common.by import By


class BasePageLocators:
    CATALOG_LINK = (By.CSS_SELECTOR, 'nav a[href="/"]')
    ABOUT_US_LINK = (By.CSS_SELECTOR, 'nav a[href="/about"]')
    CONTACTS_LINK = (By.CSS_SELECTOR, 'nav a[href="/contacts"]')
    CART_LINK = (By.CSS_SELECTOR, 'nav a[href="/cart"]')
    CART_COUNT = (By.ID, "cart-count")
    PAYMENT_LINK = (By.CSS_SELECTOR, 'nav a[href="/payment"]')
    ORDERS_HISTORY_LINK = (By.CSS_SELECTOR, 'nav a[href="/history"]')
    LOGIN_PAGE_LINK = (By.ID, "login-button")
    LOGOUT_BUTTON = (By.ID, "logout-button")
    POLICY_LINK = (By.CSS_SELECTOR, 'footer a[hreg="/policy"]')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login-form")
    LOGIN_USERNAME = (By.ID, "login-username")
    LOGIN_PASSWORD = (By.ID, "login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-form button[type="submit"]')
    REGISTER_FORM = (By.ID, "register-form")
    REGISTER_USERNAME = (By.ID, "register-username")
    REGISTER_PASSWORD = (By.ID, "register-password")
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register-form button[type="submit"]')


class CatalogPageLocators:
    MIN_PRICE_FIELD = (By.ID, "min-price")
    MAX_PRICE_FIELD = (By.ID, "max-price")
    FILTER_CATEGORIES_DROPDOWN = (By.ID, "category")
    FILTER_MANUFACTURERS_DROPDOWN = (By.ID, "manufacturer")
    FREE_SHIPMENT_CHECKBOX = (By.ID, "free-shipping")
    APPLY_FILTERS_BUTTON = (By.ID, "apply-filters")
    RESET_FILTERS_BUTTON = (By.ID, "reset-filters")
    SORT_DROPDOWN = (By.ID, "sort-order")
    PRODUCTS_LIST = (By.CSS_SELECTOR, "#product-list div")
    PAGINATION = (By.ID, "pagination")
    CURRENT_PAGE = (By.CSS_SELECTOR, '#pagination .active')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.add-to-cart-button')


class OrdersHistoryLocators:
    pass


class CartPageLocators:
    CART_FORM = (By.ID, "cart")
    TOTAL_PRICE_IN_CART = (By.ID, "cart-total")
    CHECKOUT_BUTTON = (By.ID, "checkout-button")


class PaymentPageLocators:
    PAYMENT_FORM = (By.CLASS_NAME, "payment-form")
    TOTAL_PRICE_FOR_PAYMENT = (By.ID, "total-price")
    PAYMENT_METHODS = (By.CLASS_NAME, "payment-method")
    PAYMENT_METHOD_VISA = (By.CSS_SELECTOR, '.payment-method input[value="VISA"]')
    PAYMENT_METHOD_MASTERCARD = (
        By.CSS_SELECTOR,
        '.payment-method input[value="MasterCard"]',
    )
    PAYMENT_METHOD_PAYPAL = (By.CSS_SELECTOR, '.payment-method input[value="Paypal"]')
    CARD_NUMBER = (By.ID, "card-number")
    CARD_FIRST_NAME = (By.ID, "card-name")
    CARD_LAST_NAME = (By.ID, "card_surname")
    CARD_EXPIRY_MONTH = (By.ID, "card-expiry-month")
    CARD_EXPIRY_YEAR = (By.ID, "card-expiry-year")
    CARD_CVV = (By.ID, "card-cvv")
    RECEIPT_EMAIL = (By.ID, "receipt-email")
    SUBMIT_PAYMENT_BUTTON = (By.ID, "checkout-button")

    
