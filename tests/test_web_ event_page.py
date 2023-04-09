# -*- coding: utf-8 -*-
"""
http://195.189.239.54/events
страница события
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
    browser.find_element(By.LINK_TEXT, 'События').click()

    def test_02():
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'

    def test_02():
        assert browser.find_element(By.CLASS_NAME, 'buttons-top'), 'Кнопка добавить'

    def test_03():
        assert browser.find_element(By.CLASS_NAME, 'table-filter'), 'Фильтр'

    def test_04():
        assert browser.find_element(By.CLASS_NAME, 'main'), 'Таблица'

    def test_05():
        assert browser.find_element(By.LINK_TEXT, 'Код типа события'), 'Код типа события'

    def test_06():
        assert browser.find_element(By.LINK_TEXT, 'ID'), 'ID'

    def test_07():
        assert browser.find_element(By.LINK_TEXT, 'Наименование'), 'поле Наименование'
    # assert browser.find_elment(By.LINK_TEXT, 'Получатели'), 'поле Получатели'
    # assert browser.find_element(By.LINK_TEXT, 'Шаблоны оповещений'), 'поле Шаблоны оповещений'
    def test_08():
        browser.find_element(By.CLASS_NAME, 'button').click()
        assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'

    def test_09():
        assert browser.find_element(By.CLASS_NAME, 'button-back'), 'вернуться'

    def test_10():
        assert browser.find_element(By.CLASS_NAME, 'main'), 'поля ввода'

    def test_11():
        assert browser.find_element(By.NAME, 'external_systems[]'), 'внешние системы'

    def test_12():
        assert browser.find_element(By.NAME, 'recipients[]'), 'Получатели'

    def test_13():
        assert browser.find_element(By.ID, 'name'), 'Наименование'

    def test_14():
        assert browser.find_element(By.NAME, 'priority'), 'Приоритет'

    def test_15():
        assert browser.find_element(By.CLASS_NAME, 'buttons-bottom'), 'кнопки'

    def test_16():
        assert browser.find_element(By.ID, 'type_code'), 'Тип события'

    def test_17():
        assert browser.find_element(By.ID, 'sending_count'), 'количество отправок'

    def test_18():
        assert browser.find_element(By.ID, 'is_ready'), 'Готов к использованию'

    def test_19():
        assert browser.find_element(By.ID, 'is_public'), 'Общесистемный'

    def test_20():
        assert browser.find_element(By.CLASS_NAME, 'form-input-clear'), 'Очистить строку'