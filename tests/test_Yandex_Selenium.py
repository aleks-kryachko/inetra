# https://github.com/yandex/YandexDriver
import pytest
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import host_web

def test_01_status_code():
    responce = requests.get(host_web)
    assert responce.status_code == 200, 'status not 200'

def test_02(browserY):
    print('Yandex_Fail')
    assert browserY.find_element(By.CLASS_NAME, 'header__title'), 'элемент МУП'
    return browserY
    def test_03():
        assert browserY.find_element(By.CLASS_NAME, 'header__main'), 'Шапка '

        return browserY
    def test_04():
        assert browserY.find_element(By.LINK_TEXT, 'Журналы'), 'элемент поле Журналы'
        return browserY
    def test_05():
        assert browserY.find_element(By.LINK_TEXT, 'Каналы'), 'элемент поле Каналы'
        return browserY
    def test_06():
        assert browserY.find_element(By.LINK_TEXT, 'Получатели'), 'элемент Получатели'
        return browserY
    def test_07():
        assert browserY.find_element(By.LINK_TEXT, 'Каналы'), 'элемент Каналы'
        return browserY
    def test_08():
        assert browserY.find_element(By.LINK_TEXT, 'Шаблоны'), 'элемент Шаблоны'
        return browserY
    def test_09():
        assert browserY.find_element(By.LINK_TEXT, 'Внешние системы'), 'элемент Внешние системы'