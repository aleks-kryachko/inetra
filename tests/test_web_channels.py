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

url = host_web

# @pytest.fixture
# def browser():
#     browser = webdriver.Chrome(executable_path=".chromedriver.exe")
#     # browser = webdriver.Chrome()
#     browser.set_window_size(1416, 1026)
#     # browser.maximize_window()
#     url = host_web
#     # print(browser.get_window_size())
#     browser.get(url=url)
#     browser.set_page_load_timeout(10) # sets timeout to 10 sec
#     yield browser
#     browser.quit()
def test_01_main_page(browser):
    browser.find_element(By.LINK_TEXT, 'Журналы').click()
    assert browser.find_element(By.CLASS_NAME, 'button'), 'button'
    assert browser.find_element(By.CLASS_NAME, 'table-filter__title'), 'Фильтр'
    assert browser.find_element(By.LINK_TEXT, 'Журнал событий'), 'Журнал событий'
    assert browser.find_element(By.LINK_TEXT, 'Журнал событий'), 'Журнал событий'
    assert browser.find_element(By.LINK_TEXT, 'Журнал событий'), 'Журнал событий'
