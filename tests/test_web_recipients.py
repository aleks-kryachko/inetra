# -*- coding: utf-8 -*-
"""
http://195.189.239.54/recipients
вкладка получатели
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
def test_01_recipients_list(browser):
    browser.find_element(By.LINK_TEXT, 'Получатели').click()
    def test_02():
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'
    def test_03():
        assert browser.find_element(By.CLASS_NAME, 'main'), 'таблица'
    def test_04():
        assert browser.find_element(By.CLASS_NAME, 'active'), 'Получатели'
    def test_05():
        assert browser.find_element(By.LINK_TEXT, 'Контакты получателей'), 'Контакты Получателей'
    def test_06():
        assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'
    def test_07():
        assert browser.find_element(By.CLASS_NAME, 'buttons-top'), 'кнопка Добавить'
    def test_08():
        assert browser.find_element(By.CLASS_NAME, 'button'), 'кнопка Добавить'
    def test_09_add_recipient():
        browser.find_element(By.CLASS_NAME, 'button').click()
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'
        def test_10():
            assert browser.find_element(By.CLASS_NAME, 'button-back'), 'Вернуться'
        def test_11():
            assert browser.find_element(By.CLASS_NAME, 'main'), 'Таблица'
        def test_12():
            assert browser.find_element(By.CLASS_NAME, 'buttons-bottom'), 'Кнопки'
        def test_13():
            assert browser.find_element(By.CLASS_NAME, 'form-input-clear'), 'очистить строку'
        def test_14():
            assert browser.find_element(By.CLASS_NAME, 'recipient_id'), 'ID получателя'
        def test_15():
            assert browser.find_element(By.CLASS_NAME, 'contact_info'), 'контакт получателя'
        def test_16():
            assert browser.find_element(By.CLASS_NAME, 'is_active'), 'признак активности'
