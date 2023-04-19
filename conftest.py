import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By



host_web ="http://195.189.239.54/"

@pytest.fixture
def browser():
    browser = webdriver.Chrome(executable_path=".chromedriver.exe")
    # browser = webdriver.Chrome()
    browser.set_window_size(1416, 1026)
    # browser.maximize_window()
    url = host_web
    browser.get(url=url)
    browser.set_page_load_timeout(10)
    yield browser
    browser.quit()

@pytest.fixture
def browserY():
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = 'yandexdriver.exe'

    driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
    driver.get(host_web)
    driver.set_page_load_timeout(10)
    yield driver
    driver.quit()
