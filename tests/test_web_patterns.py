# -*- coding: utf-8 -*-
"""
http://195.189.239.54/templates
вкладка шаблоны
Проверка наличия всех основных элементов на странице
:author: Aleksandr Kryachko
:copyright: Copyright 2023, Inetra Selenium Tests"
:license: MIT
:version: 1.0.0
:maintainer: Aleksandr Kryachko
:email: aleksan.kryachko@gmail.com
"""

import requests
import pytest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import host_web
from conftest import browser


@pytest.mark.smoke
def test_01_templates_logs_items(browser):
    browser.find_element(By.LINK_TEXT, 'Шаблоны').click()

    def test_02():
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'

    def test_03():
        assert browser.find_element(By.CLASS_NAME, 'main'), 'таблица'

    def test_04():
        assert browser.find_element(By.CLASS_NAME, 'active'), 'Шапка'

    def test_04():
        assert browser.find_element(By.CLASS_NAME, 'active'), 'Шапка'

    def test_05():
        assert browser.find_element(By.CLASS_NAME, 'button'), 'button'

    def test_06():
        assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'

    def test_07():
        assert browser.find_element(By.LINK_TEXT, 'Код'), 'Код'

    def test_08():
        assert browser.find_element(By.LINK_TEXT, 'ID'), 'ID'

    def test_09():
        assert browser.find_element(By.LINK_TEXT, 'Наименование'), 'поле Наименование'

    def test_10():
        assert browser.find_element(By.LINK_TEXT, 'Версия'), 'поле Версия'

    def test_11():
        assert browser.find_element(By.LINK_TEXT, 'Код'), 'поле Код'

    def test_12():
        assert browser.find_element(By.LINK_TEXT, 'Тип канала'), 'поле тип канала'

    def test_13():
        assert browser.find_element(By.LINK_TEXT, 'Тема оповещения'), 'поле Заголовок'

    def test_14():
        assert browser.find_element(By.LINK_TEXT, 'Структура уведомления'), 'поле Структура уведомления'

    def test_15():
        assert browser.find_element(By.LINK_TEXT, 'Файл'), 'поле Файл'
        assert browser.find_element(By.LINK_TEXT, 'Дата создания'), 'поле Дата создания'

    def test_16():
        browser.find_element(By.LINK_TEXT, 'Шаблоны').click()
        browser.find_element(By.CLASS_NAME, 'button').click()
        assert browser.find_element(By.CLASS_NAME, 'main'), 'Таблица'

    def test_17():
        assert browser.find_element(By.CLASS_NAME, 'button-back'), 'кнопка Вернуться'

    def test_18():
        assert browser.find_element(By.CLASS_NAME, 'buttons-bottom'), 'кнопки'

    def test_19():
        assert browser.find_element(By.ID, 'code'), 'Код'

    def test_20():
        assert browser.find_element(By.ID, 'name'), 'Наименование'

    def test_21():
        assert browser.find_element(By.ID, 'version'), 'Версия'

    def test_22():
        assert browser.find_element(By.ID, 'channel_type'), 'Тип канала'

    def test_23():
        assert browser.find_element(By.ID, 'title'), 'Тема оповещения'

    def test_24():
        assert browser.find_element(By.CLASS_NAME, 'form-group'), 'Структура уведомления'