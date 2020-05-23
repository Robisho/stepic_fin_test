# -*- coding: utf-8 -*-
# !/usr/bin/env python3

# pytest -v -s test_foo.py

from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
import time
import pytest
from .pages.login_page import LoginPage


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.browser = browser

    def test_register_new_user(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        email = str(time.time()) + '@fakemail.org'
        password = '1231231234'
        reg_user = LoginPage(self.browser, link)
        reg_user.open()
        reg_user.register_new_user(email, password)
        reg_user.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(self.browser, link)
        page.open()  # Открываем страницу товара
        time.sleep(1)
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        no_report_msg = ProductPage(self.browser, link)
        no_report_msg.should_not_be_success_message()  # ждет 4 сек

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(self.browser, link)
        page.open()  # Открываем страницу товара
        page.add_item_to_basket()  # Добавляем товар в корзину
        page.solve_quiz_and_get_code()
        # time.sleep(200)  # если надо залезть в код страницы
        # проверяем, добавлена ли в корзину выбранная книга с правильной ценой
        page.should_be_add_item_to_basket()


# @pytest.mark.parametrize('link', [
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfile),
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    page.add_item_to_basket()  # Добавляем товар в корзину
    page.solve_quiz_and_get_code()
    # time.sleep(200)  # если надо залезть в код страницы
    # проверяем, добавлена ли в корзину выбранная книга с правильной ценой
    page.should_be_add_item_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    time.sleep(1)
    page.add_item_to_basket()  # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    item_add = ProductPage(browser, link)
    item_add.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    time.sleep(1)
    page.add_item_to_basket()  # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    no_report_msg = ProductPage(browser, link)
    no_report_msg.should_be_success_message_is_disappeared()  # ждет 4 сек


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    time.sleep(1)
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    no_report_msg = ProductPage(browser, link)
    no_report_msg.should_not_be_success_message()  # ждет 4 сек


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()  # Гость открывает страницу товара
    basket_page = BasketPage(browser, link)
    # Переходит в корзину по кнопке в шапке сайта
    basket_page.should_be_go_to_basket_page()
    # Ожидаем, что в корзине нет товаров
    basket_page.should_not_be_items_in_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_basket_empty()
