# -*- coding: utf-8 -*-
# !/usr/bin/env python3


from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#id_login-username')
    REGISTER_FORM = (By.CSS_SELECTOR, '#id_registration-email')


class ProductPageLocators():
    # BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BASKET_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')

    # BASE_BOOKNAME = (By.CSS_SELECTOR, '.product_main h1')  # +
    BASE_BOOKNAME = (By.XPATH, '//*[@id="content_inner"]//h1')  # +

    # BASE_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')  # +
    BASE_PRICE = (By.XPATH, '//*[@id="content_inner"]//p[1]')  # +

    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]//strong')
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_BTN = (By.XPATH, '//*[@id="default"]//span/a')
    BACKET_EMPTY = (By.XPATH, '//*[@id ="content_inner"]/p')
    ITEM_PRICE = (By.XPATH, '//*[@id="basket_formset"]//div[5]/p')
    # ITEM_PRICE = (By.CSS_SELECTOR, '.col-sm-2 p.price_color')
