from base_page import BasePage
from locators import BasketPageLocators

class BasketPage(BasePage):
    def check_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECK_NO_PRODUCT_IN_BASKET), "There is some product in the basket"

    def check_basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is no message that basket is empty"