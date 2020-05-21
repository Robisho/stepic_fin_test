# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_be_go_to_basket_page(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET_BTN)
        basket.click()

    def should_be_basket_empty(self):
        basket_empty = self.browser.find_element(*BasketPageLocators.BACKET_EMPTY).text
        assert len(basket_empty) > 0, 'Корзина не пуста!'

    def should_not_be_items_in_basket(self):
        # проверка отсутствия товаров в корзине
        assert self.is_not_element_present(
            *BasketPageLocators.ITEM_PRICE), "В корзине есть другие товары!"
