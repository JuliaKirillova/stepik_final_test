from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK = (By.ID, "#login_link")

class LoginPageLocators:
    # LOGIN_URL = (By.ID, "/en-gb/accounts/login/")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class AddToBasketLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.TAG_NAME, "h1")
    MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
    BOOK_PRICE= (By.CSS_SELECTOR, "div.product_main > p.price_color")
    MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, "div.alert-info p strong")
