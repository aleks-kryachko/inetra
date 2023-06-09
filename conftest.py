import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By



host_web ="http://195.189.239.**/"

@pytest.fixture
def browser():
    browser = webdriver.Chrome(executable_path=".chromedriver.exe")
    # browser = webdriver.Chrome()
    browser.set_window_size(1416, 1026)
    # browser.maximize_window()
    url = host_web
    browser.get(url=url)
    browser.find_element(By.XPATH, '/html/body/main/form/label[2]').click()
    browser.find_element(By.CSS_SELECTOR, 'body > main > form > button').click()
    browser.set_page_load_timeout(10)
    # time.sleep(5)

    yield browser
    browser.quit()

@pytest.fixture
def browserY():
    options = webdriver.ChromeOptions()
    binary_yandex_driver_file = '.yandexdriver.exe'

    driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
    driver.get(host_web)
    # авторизация классов тегов и ид нет, поэтому кликает по кривому , так делать нельзя
    driver.find_element(By.CSS_SELECTOR, 'body > main > form > label:nth-child(3) > input[type=radio]').click()
    driver.find_element(By.CSS_SELECTOR, 'body > main > form > button').click()
    driver.set_page_load_timeout(10)
    yield driver
    driver.quit()
