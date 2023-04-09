# -*- coding: utf-8 -*-
"""
http://195.189.239.54/templates
вкладка журналы
Проверка наличия всех основных элементов на странице
:author: Aleksandr Kryachko
:copyright: Copyright 2023, Inetra Selenium Tests"
:license: MIT
:version: 1.0.0
:maintainer: Aleksandr Kryachko
:email: aleksan.kryachko@gmail.com
"""
import pytest
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import host_web
from conftest import browser

# http://195.189.239.54/logs/events
# вкладка журналы

def test_01_status_code():
    url = host_web
    responce = requests.get(url=url)
    assert responce.status_code == 200, 'status not 200'
def test_02_main_page(browser):
    assert browser.find_element(By.CLASS_NAME, 'header__title'), 'элемент МУП'

    def test_03():
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка '

    def test_04():
        assert browser.find_element(By.LINK_TEXT, 'Журналы'), 'элемент поле Журналы'

    def test_05():
        assert browser.find_element(By.LINK_TEXT, 'Каналы'), 'элемент поле Каналы'

    def test_06():
        assert browser.find_element(By.LINK_TEXT, 'Получатели'), 'элемент Получатели'

    def test_07():
        assert browser.find_element(By.LINK_TEXT, 'Каналы'), 'элемент Каналы'

    def test_08():
        assert browser.find_element(By.LINK_TEXT, 'Шаблоны'), 'элемент Шаблоны'

    def test_09():
        assert browser.find_element(By.LINK_TEXT, 'Внешние системы'), 'элемент Внешние системы'

    def test_10():
        assert browser.find_element(By.LINK_TEXT, 'События'), 'элемент События'

    def test_11():
        assert browser.find_element(By.LINK_TEXT, 'Журналы'), 'элемент поле Журналы'

    def test_12():
        assert browser.find_element(By.LINK_TEXT, 'Каналы'), 'элемент поле Каналы'

    def test_13():
        assert browser.find_element(By.LINK_TEXT, 'Получатели'), 'элемент поле Получатели'

    def test_14():
        assert browser.find_element(By.LINK_TEXT, 'Шаблоны'),'элемент поле Шаблоны'

    def test_15():
        assert browser.find_element(By.LINK_TEXT, 'Внешние системы'), 'элемент поле Внешние системы'

    def test_16():
        assert browser.find_element(By.LINK_TEXT, 'Журнал событий'), 'элемент  Журнал событий'

    def test_17():
        assert browser.find_element(By.LINK_TEXT, 'Журнал оповещений'), 'элемент  Журнал оповещений'

    def test_18():
        browser.find_element(By.LINK_TEXT, 'Журнал событий').click()
        assert browser.find_element(By.CLASS_NAME, 'main'), 'Таблица'

    def test_19():
        assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'

    def test_20():
        assert browser.find_element(By.LINK_TEXT, 'Журнал оповещений'), 'Журнал оповещений'

    def test_21():
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'

    def test_22():
        browser.find_element(By.LINK_TEXT, 'Журнал оповещений').click()
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'

    def test_23():
        assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'

    def test_24():
        assert browser.find_element(By.CLASS_NAME, 'main'), 'Таблица'

    def test_25():
        assert browser.find_element(By.LINK_TEXT, 'Журнал событий'), 'элемент  Журнал событий'

    def test_26():
        assert browser.find_element(By.LINK_TEXT, 'Журнал оповещений'), 'элемент  Журнал оповещений'