# -*- coding: utf-8 -*-
# !/usr/bin/env python3

class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
