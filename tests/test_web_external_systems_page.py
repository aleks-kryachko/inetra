# -*- coding: utf-8 -*-
"""
http://195.189.239.54/external-systems
вкладка внешние системы
Проверка наличия всех основных элементов на странице
:author: Aleksandr Kryachko
:copyright: Copyright 2023, Inetra Selenium Tests"
:license: MIT
:version: 1.0.0
:maintainer: Aleksandr Kryachko
:email: aleksan.kryachko@gmail.com
"""
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
    browser.find_element(By.LINK_TEXT, 'Внешние системы').click()
    return browser

    def test_02(browser):
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'

    return browser
    def test_03(browser):
        assert browser.find_element(By.CLASS_NAME, 'button'), 'button'

    return browser
    def test_04():
        assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'

    return browser
    def test_05():
        assert browser.find_element(By.LINK_TEXT, 'Код'), 'Код'

    return browser
    def test_06():
        assert browser.find_element(By.LINK_TEXT, 'ID'), 'ID'

    return browser
    def test_07():
        assert browser.find_element(By.LINK_TEXT, 'Наименование'), 'поле Наименование'

    return browser
    def test_08():
        assert browser.find_element(By.LINK_TEXT, 'Приём заданий на рассылку'), 'поле Прием задания на рассылку'
        return browser

    def test_09():
        assert browser.find_element(By.LINK_TEXT, 'Приоритет'), 'поле Приоритет'
        browser.find_element(By.CLASS_NAME, 'button').click()

        return browser
    def test_10():
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'

    return browser
    def test_11():
        assert browser.find_element(By.CLASS_NAME, 'button-back'), 'вернуться'

    return browser
    def test_12():
        assert browser.find_element(By.ID, 'code'), 'Код'

    return browser
    def test_13():
        assert browser.find_element(By.ID, 'name'), 'Наименованние'

    return browser
    def test_14():
        assert browser.find_element(By.ID, 'priority'), 'Приоритет'

    return browser
    def test_15():
        assert browser.find_element(By.ID, 'is_mailing'), 'Разрешен прием заданий'

    return browser
    def test_16():
        assert browser.find_element(By.ID, 'events'), 'Событие'

    return browser
    def test_17():
        assert browser.find_element(By.CLASS_NAME, 'buttons-bottom'), 'Сохранить'

    return browser
    def test_18():
        assert browser.find_element(By.CLASS_NAME, 'form-input-clear'), 'очистить строку'
        return browser

