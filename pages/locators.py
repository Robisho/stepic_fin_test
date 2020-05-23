# -*- coding: utf-8 -*-
# !/usr/bin/env python3


from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # REGISTER_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#id_login-username')
    REGISTER_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FORM1 = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_FORM2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BTN = (By.XPATH, '//*[@id="register_form"]/button')


class ProductPageLocators():
    BASKET_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    BASE_BOOKNAME = (By.XPATH, '//*[@id="content_inner"]//h1')
    BASE_PRICE = (By.XPATH, '//*[@id="content_inner"]//p[1]')
    ADD_NAME = (By.XPATH, '//*[@id="messages"]//strong')
    ADD_PRICE = (By.XPATH, '//*[@id="messages"]//p[1]/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]//strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_BTN = (By.XPATH, '//*[@id="default"]//span/a')
    BACKET_EMPTY = (By.XPATH, '//*[@id ="content_inner"]/p')
    ITEM_PRICE = (By.XPATH, '//*[@id="basket_formset"]//div[5]/p')
