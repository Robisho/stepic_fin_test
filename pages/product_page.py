# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from .locators import ProductPageLocators
from .base_page import BasePage
# from .login_page import LoginPage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_item_to_basket(self):
        # добавление книги в корзину
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def should_be_add_item_to_basket(self):
        # проверка соответствия добавленного в корзину
        base_name = self.browser.find_element(
            *ProductPageLocators.BASE_BOOKNAME).text
        base_price = self.browser.find_element(
            *ProductPageLocators.BASE_PRICE).text
        add_name = self.browser.find_element_by_xpath(
            '//*[@id="messages"]//strong').text
        add_price = self.browser.find_element_by_xpath(
            '//*[@id="messages"]//p[1]/strong').text

        assert base_name == add_name, 'Добавлена другая книга!'
        assert base_price == add_price, 'Цена не соответствует!'

    def should_be_success_message_is_disappeared(self):
        # проверка исчезновения сообщения об успешном действии
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), 'Сообщение об успехе не исчезло'

    def should_not_be_success_message(self):
        # проверка отсутствия сообщения об успешном действии
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Сообщение об успехе представлено, но не должно быть"
