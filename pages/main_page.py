from base_page import BasePage
# from locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

# До переноса элементов в BasePage https://stepik.org/lesson/201964/step/8?unit=176022 см. ниже
# class MainPage(BasePage):
#     def go_to_login_page(self):
#         link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#         link.click()





