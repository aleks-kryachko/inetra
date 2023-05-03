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
def test_01_logs_items(browser):
    browser.find_element(By.LINK_TEXT, 'Шаблоны').click()
    return browser
    def test_02(self):
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'
        return browser
    def test_03(self):
        assert browser.find_element(By.CLASS_NAME, 'main'), 'таблица'
        return browser
    def test_04(self):
        assert browser.find_element(By.CLASS_NAME, 'active'), 'Шапка'
        return browser
    def test_04(self):
        assert browser.find_element(By.CLASS_NAME, 'active'), 'Шапка'
        return browser
    def test_05(self):
        assert browser.find_element(By.CLASS_NAME, 'button'), 'button'
        return browser
    def test_06(self):
        assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'
        return browser
    def test_07(self):
        assert browser.find_element(By.LINK_TEXT, 'Код'), 'Код'
        return browser
    def test_08(self):
        assert browser.find_element(By.LINK_TEXT, 'ID'), 'ID'
        return browser
    def test_09(self):
        assert browser.find_element(By.LINK_TEXT, 'Наименование'), 'поле Наименование'
        return browser
    def test_10(self):
        assert browser.find_element(By.LINK_TEXT, 'Версия'), 'поле Версия'
        return browser
    def test_11(self):
        assert browser.find_element(By.LINK_TEXT, 'Код'), 'поле Код'
        return browser
    def test_12(self):
        assert browser.find_element(By.LINK_TEXT, 'Тип канала'), 'поле тип канала'
        return browser
    def test_13(self):
        assert browser.find_element(By.LINK_TEXT, 'Тема оповещения'), 'поле Заголовок'
        return browser
    def test_14(self):
        assert browser.find_element(By.LINK_TEXT, 'Структура уведомления'), 'поле Структура уведомления'
        return browser
    def test_15(self):
        assert browser.find_element(By.LINK_TEXT, 'Файл'), 'поле Файл'
        assert browser.find_element(By.LINK_TEXT, 'Дата создания'), 'поле Дата создания'
        return browser
    def test_16(self):
        browser.find_element(By.LINK_TEXT, 'Шаблоны').click()
        browser.find_element(By.CLASS_NAME, 'button').click()
        assert browser.find_element(By.CLASS_NAME, 'main'), 'Таблица'
        return browser
    def test_17(self):
        assert browser.find_element(By.CLASS_NAME, 'button-back'), 'кнопка Вернуться'
        return browser

    def test_18(self):
        assert browser.find_element(By.CLASS_NAME, 'buttons-bottom'), 'кнопки'
        return browser
    def test_19(self):
        assert browser.find_element(By.ID, 'code'), 'Код'
        return browser
    def test_20(self):
        assert browser.find_element(By.ID, 'name'), 'Наименование'
        return browser
    def test_21(self):
        assert browser.find_element(By.ID, 'version'), 'Версия'
        return browser
    def test_22(self):
        assert browser.find_element(By.ID, 'channel_type'), 'Тип канала'
        return browser
    def test_23(self):
        assert browser.find_element(By.ID, 'title'), 'Тема оповещения'
        return browser
    def test_24(self):
        assert browser.find_element(By.CLASS_NAME, 'form-group'), 'Структура уведомления'
        return browser