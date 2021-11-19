from base_page import BasePage
from locators import LoginPageLocators
# from test_product_last import test_setup


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "There is no 'login' in URL"
        # assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        # assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        # assert True

    def register_new_user(self, email, password):
        # регистрация нового пользователя
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field.send_keys(password)
        password_field_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        password_field_confirm.send_keys(password)
        page = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        page.click()