import pytest
import time
from login_page import LoginPage
from product_page import ProductPage
from base_page import BasePage
from basket_page import BasketPage

link_login_page = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
link_product_page = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
link_promo_offer = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"


@pytest.mark.need_review
# Тест на параметризацию
@pytest.mark.parametrize('offer_number',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket_and_check_messages()


@pytest.mark.xfail(reason="must be failed")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Проверка отсутсвия сообщения об успехе (должен проходить как failed)
    link = link_promo_offer
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # Проверка отсутсвия сообщения об успехе
    link = link_promo_offer
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="must be failed")
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Проверка исчезающего сообщения об успехе (должен проходить как failed)
    link = link_promo_offer
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    # Проверка отображения ссылки на страницу логина со страницы продукта
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # Проверка перехода на страницу логина со страницы продукта
    link = link_product_page
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = link_product_page
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.check_product_in_basket()
    basket_page.check_basket_is_empty_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def test_setup(self, browser):
        link = link_login_page
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "12345qwerty!"
        page.register_new_user(email, password)
        page = BasePage(browser, link)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Проверка отсутсвия сообщения об успехе
        link = link_promo_offer
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # Проверка вывода сообщения после добавления товара в корзину
        link = link_promo_offer
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket_and_check_messages()
