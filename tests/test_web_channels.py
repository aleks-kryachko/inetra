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


@pytest.mark.smoke
def test_01_main_page(browser):
    browser.find_element(By.LINK_TEXT, 'Каналы').click()
    assert browser.find_element(By.CLASS_NAME, 'button'), 'Элемент button'
    return browser

    def test_02():
        assert browser.find_element(By.CLASS_NAME, 'main'), 'Таблица'
        return browser
    # assert browser.find_element(By.CLASS_NAME, 'column desc'), 'Элемент ID'

    def test_03():
        assert browser.find_element(By.CLASS_NAME, 'table-filter'), 'Фильтр'
        return browser
    # assert browser.find_element(By.LINK_TEXT, 'Тип канала'), 'Элемент Тип канала'
    # assert browser.find_element(By.LINK_TEXT, 'Отправитель'), 'Элемент Отправитель'
    # assert browser.find_element(By.LINK_TEXT, 'По умолчанию'), 'Элемент По умолчанию'
    # assert browser.find_element(By.LINK_TEXT, 'Количество попыток'), 'Элемент Количество попыток'
    # assert browser.find_element(By.LINK_TEXT, 'Таймаут'), 'Элемент Таймаут'
    # assert browser.find_element(By.LINK_TEXT, 'Email SMTP'), 'Элемент Email SMTP'
    def test_04():
        browser.find_element(By.CLASS_NAME, 'button').click()
        assert browser.find_element(By.CLASS_NAME, 'button-back'), 'Элемент Вернуться'
        return browser

    def test_05():
        assert browser.find_element(By.CLASS_NAME, 'main'), 'Элемент Таблица'
        return browser

    def test_06():
        assert browser.find_element(By.ID, 'channel_type'), 'Элемент Наименование'
        return browser

    def test_07():
        assert browser.find_element(By.ID, 'send_count'), 'Элемент Количество попыток'
        return browser

    def test_08():
        assert browser.find_element(By.ID, 'is_default'), 'По умолчанию'
        return browser

    def test_09():
        assert browser.find_element(By.CLASS_NAME, 'form-input-clear'), 'Элемент Очистить строку'
        return browser

    def test_10():
        assert browser.find_element(By.CLASS_NAME, 'buttons-bottom'), 'Элемент Кнопки'
        return browser

