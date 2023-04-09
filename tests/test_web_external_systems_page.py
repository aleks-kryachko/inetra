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



def test_01_templates_logs_items(browser):
    browser.find_element(By.LINK_TEXT, 'Внешние системы').click()

    def test_02():
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'

    def test_03():
        assert browser.find_element(By.CLASS_NAME, 'button'), 'button'

    def test_04():
        assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'

    def test_05():
        assert browser.find_element(By.LINK_TEXT, 'Код'), 'Код'

    def test_06():
        assert browser.find_element(By.LINK_TEXT, 'ID'), 'ID'

    def test_07():
        assert browser.find_element(By.LINK_TEXT, 'Наименование'), 'поле Наименование'

    def test_08():
        assert browser.find_element(By.LINK_TEXT, 'Приём заданий на рассылку'), 'поле Прием задания на рассылку'

    def test_09():
        assert browser.find_element(By.LINK_TEXT, 'Приоритет'), 'поле Приоритет'
        browser.find_element(By.CLASS_NAME, 'button').click()

    def test_10():
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'

    def test_11():
        assert browser.find_element(By.CLASS_NAME, 'button-back'), 'вернуться'

    def test_12():
        assert browser.find_element(By.ID, 'code'), 'Код'

    def test_13():
        assert browser.find_element(By.ID, 'name'), 'Наименованние'

    def test_14():
        assert browser.find_element(By.ID, 'priority'), 'Приоритет'

    def test_15():
        assert browser.find_element(By.ID, 'is_mailing'), 'Разрешен прием заданий'

    def test_16():
        assert browser.find_element(By.ID, 'events'), 'Событие'

    def test_17():
        assert browser.find_element(By.CLASS_NAME, 'buttons-bottom'), 'Сохранить'

    def test_18():
        assert browser.find_element(By.CLASS_NAME, 'form-input-clear'), 'очистить строку'
