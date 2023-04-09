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
    assert browser.find_element(By.CLASS_NAME, 'main'), 'Таблица'
    assert browser.find_element(By.CLASS_NAME, 'ID'), 'Элемент ID'
    assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'
    assert browser.find_element(By.LINK_TEXT, 'Тип канала'), 'Элемент Тип канала'
    assert browser.find_element(By.LINK_TEXT, 'Отправитель'), 'Элемент Отправитель'
    assert browser.find_element(By.LINK_TEXT, 'По умолчанию'), 'Элемент По умолчанию'
    assert browser.find_element(By.LINK_TEXT, 'Количество попыток'), 'Элемент Количество попыток'
    assert browser.find_element(By.LINK_TEXT, 'Таймаут'), 'Элемент Таймаут'
    assert browser.find_element(By.LINK_TEXT, 'Email SMTP'), 'Элемент Email SMTP'
    browser.find_element(By.CLASS_NAME, 'button').click()
    assert browser.find_element(By.CLASS_NAME, 'button-back'), 'Элемент Вернуться'
    assert browser.find_element(By.CLASS_NAME, 'main'), 'Элемент Таблица'
    assert browser.find_element(By.ID, 'channel_type'), 'Элемент Наименование'
    assert browser.find_element(By.CLASS_NAME, 'ID'), 'Элемент ID'
    assert browser.find_element(By.CLASS_NAME, 'ID'), 'Элемент ID'

