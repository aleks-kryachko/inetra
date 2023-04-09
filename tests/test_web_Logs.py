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
    assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка '
    assert browser.find_element(By.LINK_TEXT, 'Журналы'), 'элемент поле Журналы'
    assert browser.find_element(By.LINK_TEXT, 'Каналы'), 'элемент поле Каналы'

    assert browser.find_element(By.LINK_TEXT, 'Получатели'), 'элемент Получатели'
    assert browser.find_element(By.LINK_TEXT, 'Каналы'), 'элемент Каналы'
    assert browser.find_element(By.LINK_TEXT, 'Шаблоны'), 'элемент Шаблоны'
    assert browser.find_element(By.LINK_TEXT, 'Внешние системы'), 'элемент Внешние системы'
    assert browser.find_element(By.LINK_TEXT, 'События'), 'элемент События'

    assert browser.find_element(By.LINK_TEXT, 'Журналы'), 'элемент поле Журналы'
    assert browser.find_element(By.LINK_TEXT, 'Каналы'), 'элемент поле Каналы'
    assert browser.find_element(By.LINK_TEXT, 'Получатели'), 'элемент поле Получатели'
    assert browser.find_element(By.LINK_TEXT, 'Шаблоны'),'элемент поле Шаблоны'
    assert browser.find_element(By.LINK_TEXT, 'Внешние системы'), 'элемент поле Внешние системы'
    assert browser.find_element(By.LINK_TEXT, 'Журнал событий'), 'элемент  Журнал событий'
    assert browser.find_element(By.LINK_TEXT, 'Журнал оповещений'), 'элемент  Журнал оповещений'
    browser.find_element(By.LINK_TEXT, 'Журнал событий').click()
    assert browser.find_element(By.CLASS_NAME, 'main'), 'Таблица'
    assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'
    assert browser.find_element(By.LINK_TEXT, 'Журнал оповещений'), 'Журнал оповещений'
    assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'

    browser.find_element(By.LINK_TEXT, 'Журнал оповещений').click()
    assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'
    assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'
    assert browser.find_element(By.CLASS_NAME, 'main'), 'Таблица'
    assert browser.find_element(By.LINK_TEXT, 'Журнал событий'), 'элемент  Журнал событий'
    assert browser.find_element(By.LINK_TEXT, 'Журнал оповещений'), 'элемент  Журнал оповещений'