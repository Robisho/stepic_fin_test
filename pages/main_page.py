# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# pytest -v --tb=line --language=en main_page.py


from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def go_to_login_page(self):
        # login_link = self.browser.find_element_by_css_selector("#login_link")
        login_link = self.browser.find_element(By.CSS_SELECTOR, '#login_link')
        login_link.click()

    def should_be_login_link(self):  # http://prntscr.com/s6ik4f
        assert self.browser.find_element(
            By.CSS_SELECTOR, '#login_link'), 'Login link is not presented'
