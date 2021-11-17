from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators:
    # LOGIN_URL = (By.ID, "/en-gb/accounts/login/")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    # SEE_THE_BASKET = (By.ID, "/ru/basket/")
    # SUCCESS_MESSAGE = (By.ID, "messages")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    BOOK_NAME = (By.TAG_NAME, "h1")
    MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
    BOOK_PRICE= (By.CSS_SELECTOR, "div.product_main > p.price_color")
    MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, "div.alert-info p strong")
