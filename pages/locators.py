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
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')

    # BASE_BOOKNAME = (By.CSS_SELECTOR, '.product_main h1')  # +
    BASE_BOOKNAME = (By.XPATH, '//*[@id="content_inner"]//h1')  # +

    # BASE_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')  # +
    BASE_PRICE = (By.XPATH, '//*[@id="content_inner"]//p[1]')  # +
