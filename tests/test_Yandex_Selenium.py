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

