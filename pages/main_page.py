# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# pytest -v --tb=line --language=en main_page.py

from .locators import MainPageLocators
from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

