# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert (login_url.endswith('login/')), 'LOGIN_URL не найден!'

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert True, 'LOGIN_FORM не найден!'

    def should_be_register_form(self):
        register_form = self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM)
        assert True, 'REGISTER_FORM не найден!'

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        register_email.send_keys(email)
        register_pwd1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM1)
        register_pwd1.send_keys(password)
        register_pwd2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM2)
        register_pwd2.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()
