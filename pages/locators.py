from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK = (By.ID, "#login_link")

class LoginPageLocators:
    # LOGIN_URL = (By.ID, "/en-gb/accounts/login/")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
