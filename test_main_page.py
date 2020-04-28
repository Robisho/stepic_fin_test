# -*- coding: utf-8 -*-
# !/usr/bin/env python3

# pytest -v --tb=line --language=en test_main_page.py
# http://selenium1py.pythonanywhere.com/en-gb/accounts/login/

from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    # link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_should_be_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    # page.should_be_login_url()
    # page.should_be_login_form()
    # page.should_be_register_form()
