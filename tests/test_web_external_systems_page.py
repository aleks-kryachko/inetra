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
    assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'
    assert browser.find_element(By.CLASS_NAME, 'button'), 'button'
    assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'
    assert browser.find_element(By.LINK_TEXT, 'Код'), 'Код'
    assert browser.find_element(By.LINK_TEXT, 'ID'), 'ID'
    assert browser.find_element(By.LINK_TEXT, 'Наименование'), 'поле Наименование'
    assert browser.find_element(By.LINK_TEXT, 'Приём заданий на рассылку'), 'поле Прием задания на рассылку'
    assert browser.find_element(By.LINK_TEXT, 'Приоритет'), 'поле Приоритет'
    browser.find_element(By.CLASS_NAME, 'button').click()
    assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'
    assert browser.find_element(By.CLASS_NAME, 'button-back'), 'вернуться'
    assert browser.find_element(By.ID, 'code'), 'Код'
    assert browser.find_element(By.ID, 'name'), 'Наименованние'
    assert browser.find_element(By.ID, 'priority'), 'Приоритет'
    assert browser.find_element(By.ID, 'is_mailing'), 'Разрешен прием заданий'
    assert browser.find_element(By.ID, 'events'), 'Событие'
    assert browser.find_element(By.CLASS_NAME, 'buttons-bottom'), 'Сохранить'
    assert browser.find_element(By.CLASS_NAME, 'form-input-clear'), 'очистить строку'
