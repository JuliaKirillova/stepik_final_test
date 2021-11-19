from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    # LOGIN_URL = (By.ID, "/en-gb/accounts/login/")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.XPATH, "// *[ @ id = 'register_form'] / button")

class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    BOOK_NAME = (By.TAG_NAME, "h1")
    MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
    BOOK_PRICE= (By.CSS_SELECTOR, "div.product_main > p.price_color")
    MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, "div.alert-info p strong")

class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_BUTTON_INVALID = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a1")
    CHECK_NO_PRODUCT_IN_BASKET = (By.ID, "basket_formset")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'empty')]")
    FFF = (By.TAG_NAME)


