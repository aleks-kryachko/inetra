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
    assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Элемент Фильтр'
    assert browser.find_element(By.LINK_TEXT, 'ID'), 'Элемент ID'
    assert browser.find_element(By.LINK_TEXT, 'Наименование'), 'Элемент Наименование'
    assert browser.find_element(By.LINK_TEXT, 'Тип канала'), 'Элемент Тип канала'
    assert browser.find_element(By.LINK_TEXT, 'Отправитель'), 'Элемент Отправитель'
    assert browser.find_element(By.LINK_TEXT, 'По умолчанию'), 'Элемент По умолчанию'
    assert browser.find_element(By.LINK_TEXT, 'Количество попыток'), 'Элемент Количество попыток'
    assert browser.find_element(By.LINK_TEXT, 'Таймаут'), 'Элемент Таймаут'
    assert browser.find_element(By.LINK_TEXT, 'Email SMTP'), 'Элемент Email SMTP'
    browser.find_element(By.CLASS_NAME, 'button').click()