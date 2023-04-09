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
    assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'
    assert browser.find_element(By.CLASS_NAME, 'buttons-top'), 'Кнопка добавить'
    assert browser.find_element(By.CLASS_NAME, 'table-filter'), 'Фильтр'
    assert browser.find_element(By.LINK_TEXT, 'Код типа события'), 'Код типа события'
    assert browser.find_element(By.LINK_TEXT, 'ID'), 'ID'
    assert browser.find_element(By.LINK_TEXT, 'Наименование'), 'поле Наименование'
    # assert browser.find_elment(By.LINK_TEXT, 'Получатели'), 'поле Получатели'
    # assert browser.find_element(By.LINK_TEXT, 'Шаблоны оповещений'), 'поле Шаблоны оповещений'
