# https://github.com/yandex/YandexDriver
import pytest
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = 'http://www.python.org'

@pytest.fixture
def browser():
    browser = webdriver.Chrome(executable_path=".yandexdriver.exe")
    # browser = webdriver.Chrome()
    browser.set_window_size(1416, 1026)
    # browser.maximize_window()
    url = 'http://www.python.org'
    # print(browser.get_window_size())
    browser.get(url=url)
    browser.set_page_load_timeout(10) # sets timeout to 10 sec
    yield browser
    browser.quit()


def test_01_status_code():
    url = 'http://www.python.org'
    responce = requests.get(url=url)
    assert responce.status_code == 200, 'status not 200'

def test_02():
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = '.yandexdriver.exe'

    driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
    driver.get('http://www.python.org')
    time.sleep(3)
    driver.quit()
