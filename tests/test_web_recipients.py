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

def test_01_recipients_list(browser):
    browser.find_element(By.LINK_TEXT, 'Получатели').click()
    assert browser.find_element(By.CLASS_NAME, 'header__main'), 'Шапка'
    assert browser.find_element(By.CLASS_NAME, 'main'), 'таблица'
    assert browser.find_element(By.CLASS_NAME, 'active'), 'Получатели'
    assert browser.find_element(By.LINK_TEXT, 'Контакты получателей'), 'Контакты Получателей'
    assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'
    assert browser.find_element(By.CLASS_NAME, 'buttons-top'), 'кнопка Добавить'
    browser.find_element(By.CLASS_NAME, 'button'), 'кнопка Добавить'
    browser.find_element(By.CLASS_NAME, 'button').click()

