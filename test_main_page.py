# -*- coding: utf-8 -*-
# !/usr/bin/env python3

# pytest -v --tb=line --language=en test_main_page.py

from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    page.open()  # открываем страницу
    page.go_to_login_page  # выполняем метод страницы - переходим на страницу логина
