from product_page import ProductPage
import pytest
from base_page import BasePage
from basket_page import BasketPage


# Тест на параметризацию
@pytest.mark.parametrize('offer_number',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket_and_check_messages()

# Проверка отсутсвия сообщения об успехе
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    page.add_to_basket()  # Добавляем товар в корзину
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

# Проверка отсутсвия сообщения об успехе
def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

# Проверка исчезающего сообщения об успехе
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    page.add_to_basket()  # Добавляем товар в корзину
    page.solve_quiz_and_get_code()
    page.should_be_disappear_success_message()  # Проверяем, что сообщение об успехе исчезает с помощью is_disappeared

# Проверка отображения ссылки на страницу логина со страницы продукта
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# Проверка перехода на страницу логина со страницы продукта
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open() # Гость открывает страницу товара
    page.go_to_basket_page() # Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, link)
    basket_page.check_product_in_basket()# Ожидаем, что в корзине нет товаров
    basket_page.check_basket_is_empty_message()# Ожидаем, что есть текст о том что корзина пуста
