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

    def test_03():
        assert browserY.find_element(By.CLASS_NAME, 'header__main'), 'Шапка '

    def test_04():
        assert browserY.find_element(By.LINK_TEXT, 'Журналы'), 'элемент поле Журналы'

    def test_05():
        assert browserY.find_element(By.LINK_TEXT, 'Каналы'), 'элемент поле Каналы'

    def test_06():
        assert browserY.find_element(By.LINK_TEXT, 'Получатели'), 'элемент Получатели'

    def test_07():
        assert browserY.find_element(By.LINK_TEXT, 'Каналы'), 'элемент Каналы'

    def test_08():
        assert browserY.find_element(By.LINK_TEXT, 'Шаблоны'), 'элемент Шаблоны'

    def test_09():
        assert browserY.find_element(By.LINK_TEXT, 'Внешние системы'), 'элемент Внешние системы'