# -*- coding: utf-8 -*-
# !/usr/bin/env python3

# pytest -v -s test_foo.py

from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time
import pytest
# from .pages.login_page import LoginPage


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
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    page.add_item_to_basket()  # Добавляем товар в корзину
    # answer = BasePage(browser, link)  # сначала было так
    # answer.solve_quiz_and_get_code()
    page.solve_quiz_and_get_code()  # оказывается, так тоже работает!
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


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    time.sleep(1)
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    no_report_msg = ProductPage(browser, link)
    no_report_msg.should_not_be_success_message()  # ждет 4 сек


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


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    pass
'''
    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
'''
