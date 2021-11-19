from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
from locators import ProductPageLocators
import math
import time


class ProductPage(BasePage):
    def add_product_to_basket_and_check_messages(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_message_add_product_to_basket()
        self.should_be_message_price_product_to_basket()

    def add_to_basket(self):
        # Добавляем товар в корзину
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def solve_quiz_and_get_code(self):
        # Заполняем проверочный код для всплывающего окна
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            time.sleep(20)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_message_add_product_to_basket(self):
        # Проверяем сообщение о том, что товар добавлен в корзину
        message_book_name = self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_NAME)
        print(message_book_name.text)
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        print(book_name.text)
        assert message_book_name.text == book_name.text, "Not the same book"

    def should_be_message_price_product_to_basket(self):
        # Проверяем сообщение о цене товара после добавления в корзину
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        print(book_price.text)
        message_book_price = self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_PRICE)
        print(message_book_price.text)
        assert book_price.text == message_book_price.text, "Not the same price"

    def should_not_be_success_message(self):
        # Проверяем, что нет сообщения о добавлении продукта в корзину
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_be_disappear_success_message(self):
        # Проверяем, что сообщение о добавлении продукта в корзину исчезает
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappear"
