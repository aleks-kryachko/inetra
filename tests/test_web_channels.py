# -*- coding: utf-8 -*-
"""
http://195.189.239.54/channels
вкладка каналы
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



def test_01_main_page(browser):
    browser.find_element(By.LINK_TEXT, 'Каналы').click()
    assert browser.find_element(By.CLASS_NAME, 'button'), 'Элемент button'

    def test_02():
        assert browser.find_element(By.CLASS_NAME, 'main'), 'Таблица'
    # assert browser.find_element(By.CLASS_NAME, 'column desc'), 'Элемент ID'
    def test_03():
        assert browser.find_element(By.CLASS_NAME, 'table-filter'), 'Фильтр'
    # assert browser.find_element(By.LINK_TEXT, 'Тип канала'), 'Элемент Тип канала'
    # assert browser.find_element(By.LINK_TEXT, 'Отправитель'), 'Элемент Отправитель'
    # assert browser.find_element(By.LINK_TEXT, 'По умолчанию'), 'Элемент По умолчанию'
    # assert browser.find_element(By.LINK_TEXT, 'Количество попыток'), 'Элемент Количество попыток'
    # assert browser.find_element(By.LINK_TEXT, 'Таймаут'), 'Элемент Таймаут'
    # assert browser.find_element(By.LINK_TEXT, 'Email SMTP'), 'Элемент Email SMTP'
    def test_04():
        browser.find_element(By.CLASS_NAME, 'button').click()
        assert browser.find_element(By.CLASS_NAME, 'button-back'), 'Элемент Вернуться'

    def test_05():
        assert browser.find_element(By.CLASS_NAME, 'main'), 'Элемент Таблица'

    def test_06():
        assert browser.find_element(By.ID, 'channel_type'), 'Элемент Наименование'

    def test_07():
        assert browser.find_element(By.ID, 'send_count'), 'Элемент Количество попыток'

    def test_08():
        assert browser.find_element(By.ID, 'is_default'), 'По умолчанию'

    def test_09():
        assert browser.find_element(By.CLASS_NAME, 'form-input-clear'), 'Элемент Очистить строку'

    def test_10():
        assert browser.find_element(By.CLASS_NAME, 'buttons-bottom'), 'Элемент Кнопки'

