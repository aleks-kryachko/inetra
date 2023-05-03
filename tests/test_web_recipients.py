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
        return browser
    def test_03():
        assert browser.find_element(By.CLASS_NAME, 'main'), 'таблица'
        return browser
    def test_04():
        assert browser.find_element(By.CLASS_NAME, 'active'), 'Получатели'
        return browser
    def test_05():
        assert browser.find_element(By.LINK_TEXT, 'Контакты получателей'), 'Контакты Получателей'
        return browser
    def test_06():
        assert browser.find_element(By.CLASS_NAME, 'table-filter__title'),'таблица'
        return browser
    def test_07():
        assert browser.find_element(By.CLASS_NAME, 'buttons-top'), 'кнопка Добавить'
        return browser
    def test_08():
        assert browser.find_element(By.CLASS_NAME, 'button'), 'кнопка Добавить'
        return browser
    def test_09_add_recipient():
        browser.find_element(By.CLASS_NAME, 'button').click()
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'
        return browser
        def test_10():
            assert browser.find_element(By.CLASS_NAME, 'button-back'), 'Вернуться'
            return browser
        def test_11():
            assert browser.find_element(By.CLASS_NAME, 'main'),'шапка'
            return browser
        def test_12():
            assert browser.find_element(By.CLASS_NAME, 'buttons-bottom'), 'Кнопки'
            return browser
        def test_13():
            assert browser.find_element(By.CLASS_NAME, 'form-input-clear'), 'очистить строку'
            return browser
        def test_14():
            assert browser.find_element(By.CLASS_NAME, 'recipient_id'), 'ID получателя'
            return browser
        def test_15():
            assert browser.find_element(By.CLASS_NAME, 'contact_info'), 'контакт получателя'
            return browser
        def test_16():
            assert browser.find_element(By.CLASS_NAME, 'is_active'), 'признак активности'

